# Derived from pykdebugparser/kd_buf_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import struct as meadow_struct
from collections import namedtuple as meadow_namedtuple
import io as meadow_io
import plistlib as meadow_plistlib
from construct import Container as meadow_Container, Adapter as meadow_Adapter, Struct as meadow_Struct, Const as meadow_Const, Padding as meadow_Padding, Int32ul as meadow_Int32ul, Int64ul as meadow_Int64ul, Array as meadow_Array, GreedyRange as meadow_GreedyRange, Byte as meadow_Byte, FixedSized as meadow_FixedSized, CString as meadow_CString, Prefixed as meadow_Prefixed, GreedyBytes as meadow_GreedyBytes, Aligned as meadow_Aligned, Bytes as meadow_Bytes, Select as meadow_Select
from tracemeadow.event_records import meadow_from_kd_buf as meadow_from_kd_buf, meadow_KD_BUF_FORMAT as meadow_KD_BUF_FORMAT
from tracemeadow.log_records import meadow_OsLogEvent as meadow_OsLogEvent
meadow_KEVENT_SIZE = meadow_struct.calcsize(meadow_KD_BUF_FORMAT)
meadow_ProcessData = _name_boundary.named_record('ProcessData', ['pid', 'name'])
meadow_RAW_VERSION_SIZE = 4
meadow_RAW_VERSION2_BYTES = b'\x00\x02\xaaU'
meadow_RAW_VERSION3_BYTES = b'\x00\x03\xaaU'
meadow_TRACEV3_STACKSHOT_END = b'stackshot_out_fl'
meadow_TRACEV3_THREADMAP_TAG = b'\x00\x1d\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_EVENTS_TAG = b'\x00\x1e\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_MORE_EVENTS = b'\x00 \x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_DYLD_MODULES = b'\x01\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_TRACE_CODES = b'\x0f\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_PROCESSES = b'\x10\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_LOG_EVENTS = b'\x11\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_LOG_STRINGS = b'\x12\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_KERNEL_EXTENSIONS = b'\x05\x80\x00\x00\x00\x00\x00\x00'
meadow_TRACEV3_IMAGES = b'\x04\x80\x00\x00\x01\x00\x00\x00'
meadow_kd_threadmap = meadow_Struct('tid' / meadow_Int64ul, 'pid' / meadow_Int32ul, 'process' / meadow_FixedSized(20, meadow_CString('utf8')))

@_name_boundary.class_contract('BplistAdapter', {})
class meadow_BplistAdapter(meadow_Adapter):
    """
    Construct adapter ti build and parse plists.
    """

    @_name_boundary.callable_contract({'self': 'meadow_self_5077f15', 'obj': 'meadow_obj_e0a635c', 'context': 'meadow_context_849b4ee', 'path': 'meadow_path_ded750f'}, '_decode')
    def _decode(meadow_self_5077f15, meadow_obj_e0a635c, meadow_context_849b4ee, meadow_path_ded750f):
        return meadow_checked_plist(meadow_obj_e0a635c, MeadowLimits())

    @_name_boundary.callable_contract({'self': 'meadow_self_675f428', 'obj': 'meadow_obj_7957e58', 'context': 'meadow_context_7e8133e', 'path': 'meadow_path_4a479b6'}, '_encode')
    def _encode(meadow_self_675f428, meadow_obj_7957e58, meadow_context_7e8133e, meadow_path_4a479b6):
        return meadow_plistlib.dumps(meadow_obj_7957e58)
meadow_kd_header_v2 = meadow_Struct('number_of_treads' / meadow_Int32ul, meadow_Padding(8), meadow_Padding(4), 'is_64bit' / meadow_Int32ul, 'tick_frequency' / meadow_Int64ul, meadow_Padding(256), 'threadmap' / meadow_Array(lambda meadow_ctx_90ee768: meadow_ctx_90ee768.number_of_treads, meadow_kd_threadmap), '_pad' / meadow_GreedyRange(meadow_Const(0, meadow_Byte)))
meadow_kd_header_v3 = meadow_Struct('tag' / meadow_Int32ul, 'sub_tag' / meadow_Int32ul, 'length' / meadow_Int64ul, 'timebase_numer' / meadow_Int32ul, 'timebase_denom' / meadow_Int32ul, 'timestamp' / meadow_Int64ul, 'walltime_secs' / meadow_Int64ul, 'walltime_usecs' / meadow_Int32ul, 'timezone_minuteswest' / meadow_Int32ul, 'timezone_dst' / meadow_Int32ul, 'flags' / meadow_Int32ul, 'tag2' / meadow_Int32ul, 'cpu_info' / meadow_Prefixed(meadow_Int64ul, meadow_BplistAdapter(meadow_GreedyBytes)))
meadow_kd_v3_threadmap = meadow_Struct('threadmap' / meadow_Prefixed(meadow_Int64ul, meadow_GreedyRange(meadow_kd_threadmap)))
meadow_kd_v3_additional_data = meadow_GreedyRange(meadow_Struct('tag' / meadow_Bytes(8), 'data' / meadow_Select(meadow_Aligned(8, meadow_Prefixed(meadow_Int64ul, meadow_GreedyBytes)), meadow_Prefixed(meadow_Int64ul, meadow_GreedyBytes))))


from tracemeadow.bounded_stream import MeadowLimits, MeadowReader, TraceFormatError, meadow_checked_plist


def meadow_seek_until(reader, data):
    """Find a bounded marker or fail at EOF; borrowing a stream never closes it."""
    cursor = reader if isinstance(reader, MeadowReader) else MeadowReader(reader, MeadowLimits())
    # A bare stream uses exact one-byte lookahead, preserving nonseekable callers.
    cursor.marker(data, chunk_size=4096 if isinstance(reader, MeadowReader) else 1)



@_name_boundary.class_contract('KdBufParser', {'parse': 'meadow_parse', 'set_thread_map': 'meadow_set_thread_map', 'parse_v2': 'meadow_parse_v2', 'parse_v3': 'meadow_parse_v3', 'threads_pids': 'meadow_threads_pids', 'pids_names': 'meadow_pids_names', 'versions': 'meadow_versions', 'trace_codes': 'meadow_trace_codes', 'images': 'meadow_images', 'dyld_modules': 'meadow_dyld_modules', 'processes': 'meadow_processes', 'kernel_extensions': 'meadow_kernel_extensions', 'v3_header': 'meadow_v3_header'})
class meadow_KdBufParser:
    """Parse supported v2/v3 records using bounded reads and explicit v2 padding."""
    def __init__(self, threads_pids=None, pids_names=None, *, limits=None, v2_padding=0):
        self.threads_pids = {} if threads_pids is None else threads_pids
        self.pids_names = {} if pids_names is None else pids_names
        self._limits = limits or MeadowLimits()
        if type(v2_padding) is not int or not 0 <= v2_padding <= self._limits.search_bytes:
            raise ValueError('v2_padding must be an explicit nonnegative byte count within the search limit')
        self._v2_padding = v2_padding
        self.versions = {meadow_RAW_VERSION2_BYTES: self.meadow_parse_v2,
                         meadow_RAW_VERSION3_BYTES: self.meadow_parse_v3}
        self._events = self._blocks = self._metadata_bytes = 0
        self._clear_metadata()
        self.v3_header = None

    def _clear_metadata(self):
        self.trace_codes = ''
        self.images, self.dyld_modules, self.processes = {}, {}, {}
        self.kernel_extensions = {'Binaries': []}

    def _reader(self, reader):
        return reader if isinstance(reader, MeadowReader) else MeadowReader(reader, self._limits)

    def _event(self, data):
        if self._events >= self._limits.events:
            raise TraceFormatError('event limit exceeded; analysis is incomplete')
        self._events += 1
        return meadow_from_kd_buf(data)

    def _block(self):
        self._blocks += 1
        if self._blocks > self._limits.blocks:
            raise TraceFormatError('chunk limit exceeded; analysis is incomplete')

    def _plist(self, data):
        self._metadata_bytes += len(data)
        if self._metadata_bytes > self._limits.block_bytes:
            raise TraceFormatError('cumulative metadata byte limit exceeded')
        result = meadow_checked_plist(data, self._limits)
        if not isinstance(result, dict):
            raise TraceFormatError('trace metadata plist must be a dictionary')
        return result

    def meadow_parse(self, reader):
        cursor = self._reader(reader)
        version = cursor.exact(4, 'trace version')
        if version not in self.versions:
            raise TraceFormatError('unsupported trace version')
        self._events = self._blocks = self._metadata_bytes = 0
        self.v3_header = None
        self._clear_metadata()
        return self.versions[version](cursor)

    def meadow_set_thread_map(self, parsed_threadmap):
        tids, names = {}, {}
        for thread in parsed_threadmap:
            if len(tids) >= self._limits.threads:
                raise TraceFormatError('thread-map limit exceeded')
            if thread.tid in tids:
                raise TraceFormatError('duplicate thread-map identifier')
            tids[thread.tid], names[thread.pid] = thread.pid, thread.process
        self.threads_pids.clear(); self.threads_pids.update(tids)
        self.pids_names.clear(); self.pids_names.update(names)

    def _threads(self, cursor, count):
        if count > self._limits.threads:
            raise TraceFormatError('thread-map count exceeds limit')
        records = []
        for _ in range(count):
            data = cursor.exact(32, 'thread-map record')
            tid, pid = meadow_struct.unpack_from('<QI', data)
            label = data[12:]
            if b'\0' not in label:
                raise TraceFormatError('unterminated thread-map process name')
            try:
                name = label.split(b'\0', 1)[0].decode('utf-8')
            except UnicodeDecodeError:
                raise TraceFormatError('invalid thread-map process encoding') from None
            records.append(meadow_Container(tid=tid, pid=pid, process=name))
        self.meadow_set_thread_map(records)

    def meadow_parse_v2(self, reader):
        cursor = self._reader(reader)
        fixed = cursor.exact(284, 'v2 header')
        count = meadow_struct.unpack_from('<I', fixed)[0]
        self._threads(cursor, count)
        padding = cursor.exact(self._v2_padding, 'explicit v2 padding')
        if any(padding):
            raise TraceFormatError('explicit v2 padding is not zero-filled')
        while True:
            data = cursor.exact(meadow_KEVENT_SIZE, 'v2 event', eof=True)
            if not data:
                return
            yield self._event(data)

    def meadow_parse_v3(self, reader):
        cursor = self._reader(reader)
        fixed = cursor.exact(68, 'v3 header')
        cpu_size = meadow_struct.unpack_from('<Q', fixed, 60)[0]
        cpu_info = cursor.exact(cpu_size, 'v3 CPU metadata')
        fields = ('tag', 'sub_tag', 'length', 'timebase_numer', 'timebase_denom',
                  'timestamp', 'walltime_secs', 'walltime_usecs', 'timezone_minuteswest',
                  'timezone_dst', 'flags', 'tag2')
        self._metadata_bytes += len(cpu_info)
        if self._metadata_bytes > self._limits.block_bytes:
            raise TraceFormatError('cumulative metadata byte limit exceeded')
        self.v3_header = meadow_Container(**dict(zip(fields, meadow_struct.unpack('<IIQIIQQIIIII', fixed[:60]))))
        self.v3_header.cpu_info = meadow_checked_plist(cpu_info, self._limits)
        cursor.exact((-(68 + cpu_size)) % 8, 'v3 header alignment')
        cursor.exact(4, 'v3 version alignment')
        cursor.marker(meadow_TRACEV3_STACKSHOT_END)
        cursor.marker(meadow_TRACEV3_THREADMAP_TAG)
        thread_size = meadow_struct.unpack('<Q', cursor.exact(8, 'v3 thread-map size'))[0]
        if thread_size % 32 or thread_size > self._limits.block_bytes:
            raise TraceFormatError('invalid v3 thread-map size')
        self._threads(cursor, thread_size // 32)
        while True:
            self._block()
            cursor.marker(meadow_TRACEV3_EVENTS_TAG)
            size = meadow_struct.unpack('<Q', cursor.exact(8, 'v3 event chunk size'))[0]
            # The existing dialect permits either event bytes or event bytes plus its 8-byte prefix.
            if size > self._limits.block_bytes or size % meadow_KEVENT_SIZE not in (0, 8):
                raise TraceFormatError('invalid v3 event chunk size')
            cursor.exact(8, 'v3 event chunk prefix')
            for _ in range(size // meadow_KEVENT_SIZE):
                yield self._event(cursor.exact(meadow_KEVENT_SIZE, 'v3 event'))
            tag = cursor.exact(8, 'v3 continuation or metadata tag', eof=True)
            if tag == meadow_TRACEV3_MORE_EVENTS:
                continue
            if tag:
                cursor.unread(tag)
            break
        logs, strings = [], {}
        while True:
            tag = cursor.exact(8, 'metadata tag', eof=True)
            if not tag:
                break
            self._block()
            size = meadow_struct.unpack('<Q', cursor.exact(8, 'metadata chunk size'))[0]
            data = cursor.exact(size, 'metadata chunk')
            padding = (-size) % 8
            if padding:
                pad = cursor.exact(padding, 'metadata alignment', eof=True)
                if pad and any(pad):
                    raise TraceFormatError('nonzero metadata alignment')
            if tag == meadow_TRACEV3_TRACE_CODES:
                self._metadata_bytes += len(data)
                if self._metadata_bytes > self._limits.block_bytes:
                    raise TraceFormatError('cumulative metadata byte limit exceeded')
                try:
                    self.trace_codes += data.decode('utf-8')
                except UnicodeDecodeError:
                    raise TraceFormatError('invalid trace-code encoding') from None
            elif tag in (meadow_TRACEV3_DYLD_MODULES, meadow_TRACEV3_PROCESSES,
                         meadow_TRACEV3_KERNEL_EXTENSIONS, meadow_TRACEV3_IMAGES,
                         meadow_TRACEV3_LOG_EVENTS, meadow_TRACEV3_LOG_STRINGS):
                value = self._plist(data)
                if tag in (meadow_TRACEV3_DYLD_MODULES, meadow_TRACEV3_KERNEL_EXTENSIONS):
                    if not isinstance(value.get('Binaries'), list):
                        raise TraceFormatError('metadata Binaries must be a list')
                    target = self.dyld_modules if tag == meadow_TRACEV3_DYLD_MODULES else self.kernel_extensions
                    if not target:
                        target.update(value)
                    else:
                        target['Binaries'].extend(value['Binaries'])
                elif tag == meadow_TRACEV3_PROCESSES:
                    self.processes = value
                elif tag == meadow_TRACEV3_IMAGES:
                    self.images = value
                elif tag == meadow_TRACEV3_LOG_EVENTS:
                    if not isinstance(value.get('Events'), list):
                        raise TraceFormatError('metadata Events must be a list')
                    logs.extend(value['Events'])
                    if len(logs) > self._limits.events:
                        raise TraceFormatError('OS log event limit exceeded')
                elif tag == meadow_TRACEV3_LOG_STRINGS:
                    index = value.get('StringIndex')
                    if not isinstance(index, dict) or any(not isinstance(k, str) or type(v) is not int for k, v in index.items()):
                        raise TraceFormatError('invalid log string index')
                    if len(set(index.values())) != len(index):
                        raise TraceFormatError('duplicate log string identifier')
                    strings = {v: k for k, v in index.items()}
        for raw in logs:
            try:
                event = meadow_OsLogEvent.from_raw_log_event(raw, strings)
            except (TypeError, ValueError, KeyError, IndexError, OverflowError, RecursionError):
                raise TraceFormatError('invalid OS log event metadata') from None
            if event.process and event.thread_identifier:
                self.threads_pids[event.thread_identifier] = event.process_identifier
                self.pids_names[event.process_identifier] = event.process
            if self._events >= self._limits.events:
                raise TraceFormatError('event limit exceeded; analysis is incomplete')
            self._events += 1
            yield event

_name_boundary.module_contract(globals(), {'RAW_VERSION2_BYTES': 'meadow_RAW_VERSION2_BYTES', 'kd_threadmap': 'meadow_kd_threadmap', 'TRACEV3_STACKSHOT_END': 'meadow_TRACEV3_STACKSHOT_END', 'KD_BUF_FORMAT': 'meadow_KD_BUF_FORMAT', 'kd_v3_additional_data': 'meadow_kd_v3_additional_data', 'TRACEV3_LOG_STRINGS': 'meadow_TRACEV3_LOG_STRINGS', 'Int64ul': 'meadow_Int64ul', 'kd_header_v3': 'meadow_kd_header_v3', 'seek_until': 'meadow_seek_until', 'TRACEV3_TRACE_CODES': 'meadow_TRACEV3_TRACE_CODES', 'plistlib': 'meadow_plistlib', 'Array': 'meadow_Array', 'BplistAdapter': 'meadow_BplistAdapter', 'namedtuple': 'meadow_namedtuple', 'Const': 'meadow_Const', 'Byte': 'meadow_Byte', 'Adapter': 'meadow_Adapter', 'RAW_VERSION_SIZE': 'meadow_RAW_VERSION_SIZE', 'TRACEV3_THREADMAP_TAG': 'meadow_TRACEV3_THREADMAP_TAG', 'GreedyRange': 'meadow_GreedyRange', 'from_kd_buf': 'meadow_from_kd_buf', 'struct': 'meadow_struct', 'TRACEV3_MORE_EVENTS': 'meadow_TRACEV3_MORE_EVENTS', 'Prefixed': 'meadow_Prefixed', 'io': 'meadow_io', 'kd_v3_threadmap': 'meadow_kd_v3_threadmap', 'TRACEV3_IMAGES': 'meadow_TRACEV3_IMAGES', 'TRACEV3_EVENTS_TAG': 'meadow_TRACEV3_EVENTS_TAG', 'Select': 'meadow_Select', 'KdBufParser': 'meadow_KdBufParser', 'TRACEV3_PROCESSES': 'meadow_TRACEV3_PROCESSES', 'Struct': 'meadow_Struct', 'Int32ul': 'meadow_Int32ul', 'TRACEV3_DYLD_MODULES': 'meadow_TRACEV3_DYLD_MODULES', 'TRACEV3_LOG_EVENTS': 'meadow_TRACEV3_LOG_EVENTS', 'GreedyBytes': 'meadow_GreedyBytes', 'kd_header_v2': 'meadow_kd_header_v2', 'KEVENT_SIZE': 'meadow_KEVENT_SIZE', 'Padding': 'meadow_Padding', 'OsLogEvent': 'meadow_OsLogEvent', 'TRACEV3_KERNEL_EXTENSIONS': 'meadow_TRACEV3_KERNEL_EXTENSIONS', 'Bytes': 'meadow_Bytes', 'ProcessData': 'meadow_ProcessData', 'CString': 'meadow_CString', 'FixedSized': 'meadow_FixedSized', 'Aligned': 'meadow_Aligned', 'RAW_VERSION3_BYTES': 'meadow_RAW_VERSION3_BYTES'})
