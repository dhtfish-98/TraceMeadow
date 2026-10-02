"""Bounded offline reads and checked metadata; no tracing or input execution."""
from dataclasses import dataclass
import plistlib
import struct
from xml.parsers import expat


class TraceFormatError(ValueError):
    """Incomplete, unsupported or over-limit trace data."""


@dataclass(frozen=True)
class MeadowLimits:
    input_bytes: int = 1024 * 1024 * 1024
    block_bytes: int = 64 * 1024 * 1024
    search_bytes: int = 16 * 1024 * 1024
    threads: int = 65536
    events: int = 4194304
    blocks: int = 4096
    metadata_nodes: int = 1048576
    metadata_depth: int = 128

    def __post_init__(self):
        if any(type(value) is not int or value <= 0 for value in vars(self).values()):
            raise ValueError('limits must be positive integers')


class MeadowReader:
    """Borrow a caller's stream; account raw bytes once and support bounded pushback."""
    def __init__(self, source, limits):
        self.source, self.limits = source, limits
        self.received = self.position = 0
        self.pending = b''

    def read(self, count):
        if type(count) is not int or not 0 <= count <= self.limits.block_bytes:
            raise TraceFormatError('read size exceeds block limit')
        if not count:
            return b''
        if self.pending:
            data, self.pending = self.pending[:count], self.pending[count:]
        else:
            count = min(count, self.limits.input_bytes - self.received + 1)
            data = self.source.read(count)
            if not isinstance(data, (bytes, bytearray)) or len(data) > count:
                raise TraceFormatError('binary stream returned an invalid read')
            data = bytes(data)
            self.received += len(data)
            if self.received > self.limits.input_bytes:
                raise TraceFormatError('input byte limit exceeded; analysis is incomplete')
        self.position += len(data)
        return data

    def exact(self, count, label, eof=False):
        if type(count) is not int or not 0 <= count <= self.limits.block_bytes:
            raise TraceFormatError(label + ': length exceeds block limit')
        result = bytearray()
        while len(result) < count:
            data = self.read(count - len(result))
            if not data:
                if eof and not result:
                    return b''
                raise TraceFormatError(label + ': truncated data at byte ' + str(self.position))
            result.extend(data)
        return bytes(result)

    def unread(self, data):
        if len(data) + len(self.pending) > 8192 or len(data) > self.position:
            raise TraceFormatError('pushback limit exceeded')
        self.pending = bytes(data) + self.pending
        self.position -= len(data)

    def marker(self, marker, chunk_size=4096):
        if not isinstance(marker, bytes) or not 1 <= len(marker) <= 64:
            raise TraceFormatError('marker must contain 1 to 64 bytes')
        scanned, tail = 0, b''
        while scanned < self.limits.search_bytes:
            data = self.read(min(chunk_size, self.limits.block_bytes, self.limits.search_bytes - scanned))
            if not data:
                raise TraceFormatError('required trace marker is missing at EOF')
            scanned += len(data)
            window = tail + data
            position = window.find(marker)
            if position >= 0:
                self.unread(window[position + len(marker):])
                return
            tail = window[-(len(marker) - 1):] if len(marker) > 1 else b''
        raise TraceFormatError('marker search limit exceeded; analysis is incomplete')


class MeadowUniqueDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise TraceFormatError('duplicate plist dictionary key')
        super().__setitem__(key, value)



def _meadow_binary_plist_limits(data, limits):
    if len(data) < 40:
        raise TraceFormatError('short binary plist')
    offset_size, reference_size = data[-26], data[-25]
    count = int.from_bytes(data[-24:-16], 'big')
    root = int.from_bytes(data[-16:-8], 'big')
    table = int.from_bytes(data[-8:], 'big')
    if not (1 <= offset_size <= 8 and 1 <= reference_size <= 8 and
            1 <= count <= limits.metadata_nodes and root < count and
            8 <= table <= len(data) - 32 and count * offset_size <= len(data) - 32 - table):
        raise TraceFormatError('invalid or over-limit binary plist table')
    edges = 0
    for index in range(count):
        position = table + index * offset_size
        offset = int.from_bytes(data[position:position + offset_size], 'big')
        if not 8 <= offset < table:
            raise TraceFormatError('binary plist object offset exceeds object area')
        kind, size = data[offset] >> 4, data[offset] & 15
        payload = offset + 1
        if kind in (4, 5, 6, 10, 12, 13):
            if size == 15:
                if payload >= table or data[payload] >> 4 != 1:
                    raise TraceFormatError('invalid binary plist length marker')
                width = 1 << (data[payload] & 15)
                payload += 1
                if width > 8 or width > table - payload:
                    raise TraceFormatError('binary plist length exceeds supported width')
                size = int.from_bytes(data[payload:payload + width], 'big')
                payload += width
            if kind in (10, 12, 13):
                references = size * (2 if kind == 13 else 1)
                edges += references
                if edges > limits.metadata_nodes:
                    raise TraceFormatError('binary plist reference limit exceeded')
                width = references * reference_size
            else:
                width = size * (2 if kind == 6 else 1)
            if width > table - payload:
                raise TraceFormatError('binary plist payload exceeds object area')


def meadow_checked_plist(data, limits):
    """Preflight format-specific depth/count, then validate a decoded finite object graph."""
    if len(data) > limits.block_bytes:
        raise TraceFormatError('plist byte limit exceeded')
    try:
        if data.startswith(b'bplist00'):
            _meadow_binary_plist_limits(data, limits)
        else:
            parser = expat.ParserCreate()
            depth = nodes = 0
            def start(name, attributes):
                nonlocal depth, nodes
                depth += 1; nodes += 1
                if depth > limits.metadata_depth or nodes > limits.metadata_nodes:
                    raise TraceFormatError('XML plist depth or node limit exceeded')
            def end(name):
                nonlocal depth
                depth -= 1
            def entity(*arguments):
                raise TraceFormatError('plist entity declarations are unsupported')
            parser.StartElementHandler = start
            parser.EndElementHandler = end
            parser.EntityDeclHandler = entity
            parser.ExternalEntityRefHandler = entity
            parser.Parse(data, True)
        result = plistlib.loads(data, dict_type=MeadowUniqueDict)
        stack, active, finished = [(result, 0, False)], set(), set()
        nodes = 0
        while stack:
            value, depth, leaving = stack.pop()
            if leaving:
                active.remove(id(value)); finished.add(id(value)); continue
            nodes += 1
            if nodes > limits.metadata_nodes or depth > limits.metadata_depth:
                raise TraceFormatError('plist depth or node limit exceeded')
            if isinstance(value, (dict, list, tuple)):
                identity = id(value)
                if identity in active:
                    raise TraceFormatError('cyclic plist metadata is unsupported')
                if identity in finished:
                    continue
                active.add(identity)
                stack.append((value, depth, True))
                children = list(value.values()) if isinstance(value, dict) else value
                stack.extend((child, depth + 1, False) for child in reversed(children))
        return result
    except TraceFormatError:
        raise
    except (ValueError, TypeError, OverflowError, RecursionError, expat.ExpatError, struct.error, IndexError):
        raise TraceFormatError('invalid plist metadata') from None
