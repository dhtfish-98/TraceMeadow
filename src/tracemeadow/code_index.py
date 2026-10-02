"""Bounded trace-code catalog loading; attributed upstream contracts in ORIGIN.md."""
import os as meadow_os
import stat as meadow_stat
from pathlib import Path as meadow_Path
from typing import Mapping as meadow_Mapping
import tracemeadow_boundary as _name_boundary
from tracemeadow.bounded_stream import TraceFormatError

meadow_CODE_BYTES = 8 * 1024 * 1024
meadow_CODE_ENTRIES = 131072


def meadow_from_trace_codes_text(codes_text: str) -> meadow_Mapping[int, str]:
    if not isinstance(codes_text, str) or len(codes_text) > meadow_CODE_BYTES:
        raise TraceFormatError('trace-code text exceeds supported size')
    result = {}
    for number, line in enumerate(codes_text.splitlines(), 1):
        if number > meadow_CODE_ENTRIES:
            raise TraceFormatError('trace-code line limit exceeded')
        fields = line.split()
        if not fields:
            continue
        if len(fields) < 2 or len(fields[0]) > 10:
            raise TraceFormatError('invalid trace-code entry on line ' + str(number))
        try:
            code = int(fields[0], 16)
        except ValueError:
            raise TraceFormatError('invalid trace-code identifier on line ' + str(number)) from None
        if not 0 <= code <= 0xFFFFFFFF:
            raise TraceFormatError('trace-code identifier exceeds unsigned 32-bit range')
        result[code] = fields[1]  # Preserve the upstream last-definition-wins catalog contract.
    return result


def meadow_from_trace_codes_file(path: str) -> meadow_Mapping[int, str]:
    descriptor = meadow_os.open(path, meadow_os.O_RDONLY | meadow_os.O_NOFOLLOW | meadow_os.O_NONBLOCK | getattr(meadow_os, 'O_CLOEXEC', 0))
    try:
        before = meadow_os.fstat(descriptor)
        if not meadow_stat.S_ISREG(before.st_mode) or not 0 <= before.st_size <= meadow_CODE_BYTES:
            raise TraceFormatError('trace-code input must be a regular file of at most 8 MiB')
        data = bytearray()
        while len(data) < before.st_size:
            block = meadow_os.read(descriptor, min(65536, before.st_size - len(data)))
            if not block:
                raise TraceFormatError('trace-code file was truncated while reading')
            data.extend(block)
        extra = meadow_os.read(descriptor, 1)
        after = meadow_os.fstat(descriptor)
        fields = ('st_dev', 'st_ino', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
        if extra or any(getattr(before, f) != getattr(after, f) for f in fields):
            raise TraceFormatError('trace-code file changed while reading')
    finally:
        meadow_os.close(descriptor)
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        raise TraceFormatError('trace-code file is not UTF-8') from None
    return meadow_from_trace_codes_text(text)


def meadow_default_trace_codes() -> meadow_Mapping[int, str]:
    return meadow_from_trace_codes_file(meadow_Path(__file__).resolve().parent / 'trace.codes')


_name_boundary.module_contract(globals(), {'default_trace_codes':'meadow_default_trace_codes',
    'from_trace_codes_text':'meadow_from_trace_codes_text', 'from_trace_codes_file':'meadow_from_trace_codes_file',
    'Path':'meadow_Path', 'Mapping':'meadow_Mapping'})
