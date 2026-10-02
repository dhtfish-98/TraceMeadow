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
assert importlib.metadata.version('tracemeadow') == '1.0.3'
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
from tracemeadow.stack_stream import meadow_CallstacksParser, meadow_Frame
from tracemeadow.handlers.performance_events import meadow_PerfEvent
from tracemeadow.trace_stream import meadow_TracesParser
sample_source = meadow_from_kd_buf(wire)
images = meadow_CallstacksParser([], [], max_frames=2)
images.insert_image(0x1000, None)
sample = meadow_PerfEvent([sample_source], [], 0, cs_frames=[0x0fff, 0x1004])
frames = list(images.feed_generator([sample]))[0].frames
assert frames == [meadow_Frame(0x0fff, None, None), meadow_Frame(0x1004, None, 4)]
groups = meadow_TracesParser({}, {}, {}, max_groups=1)
start = sample_source._replace(eventid=4, func_qualifier=1)
groups.feed(start)
try:
    groups.feed(start._replace(eventid=8))
except TraceFormatError:
    pass
else:
    raise AssertionError('installed aggregation must enforce its pending-group limit')
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
