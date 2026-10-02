"""Run using python -I after wheel installation; never add the source tree."""
from pathlib import Path
import importlib.metadata
import io
import json
import plistlib
import struct
import subprocess
import sys
import tempfile
import tracemeadow
from tracemeadow.event_records import meadow_from_kd_buf
from tracemeadow.code_index import meadow_default_trace_codes
from tracemeadow.binary_stream import meadow_KdBufParser, meadow_seek_until
from tracemeadow.bounded_stream import TraceFormatError

location = Path(tracemeadow.__file__).resolve()
assert 'site-packages' in location.parts, location
assert importlib.metadata.version('tracemeadow') == '1.0.2'
record = meadow_from_kd_buf(bytes([255]) * 64)
assert record.eventid == 0xfffffffc and record.func_qualifier == 3
assert repr(record).startswith('Kevent(') and meadow_default_trace_codes()
wire = struct.pack('<Q4QQIIQ', 256, 1, 2, 3, 4, 42, 0x040C0002, 0, 0)
trace = bytes.fromhex('0002aa55') + bytes(284) + wire
assert [event.timestamp for event in meadow_KdBufParser().meadow_parse(io.BytesIO(trace))] == [256]
padded = bytes.fromhex('0002aa55') + bytes(284 + 32) + wire
assert [event.timestamp for event in meadow_KdBufParser(v2_padding=32).meadow_parse(io.BytesIO(padded))] == [256]
try:
    meadow_seek_until(io.BytesIO(b'missing'), b'required')
except TraceFormatError:
    pass
else:
    raise AssertionError('EOF without a marker must fail')

cpu = plistlib.dumps({'CPUCount': 1}, fmt=plistlib.FMT_BINARY)
header = struct.pack('<IIQIIQQIIIIIQ', 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, len(cpu)) + cpu
prefix = bytes.fromhex('0003aa55') + header + bytes((-len(header)) % 8) + bytes(4)
prefix += b'stackshot_out_fl' + bytes.fromhex('001d000000000000') + bytes(8)
events = bytes.fromhex('001e000000000000') + struct.pack('<Q', 64) + bytes(8) + wire
meta = plistlib.dumps({'Processes': []}, fmt=plistlib.FMT_BINARY)
complete = prefix + events + bytes.fromhex('1080000000000000') + struct.pack('<Q', len(meta)) + meta
assert len(list(meadow_KdBufParser().meadow_parse(io.BytesIO(complete)))) == 1
with tempfile.TemporaryDirectory(prefix='tracemeadow-consumer-') as folder:
    root = Path(folder)
    good = root / 'owned-v3.bin'; good.write_bytes(complete)
    cli = [sys.executable, '-I', '-m', 'tracemeadow.console']
    # The installed console entry point is used directly; module execution has no __main__ contract.
    cli = [str(Path(sys.executable).parent / 'tracemeadow')]
    result = subprocess.run(cli + ['processes', str(good)], capture_output=True, timeout=3)
    assert result.returncode == 0 and json.loads(result.stdout) == {'Processes': []}, result
    bad = root / 'truncated.bin'; bad.write_bytes(trace[:-1])
    result = subprocess.run(cli + ['kevents', str(bad), '--count', '-1'], capture_output=True, timeout=3)
    assert result.returncode == 2 and b'truncated' in result.stderr and b'Traceback' not in result.stderr, result
    assert good.read_bytes() == complete and bad.read_bytes() == trace[:-1]
print('TraceMeadow installed consumer PASS')
