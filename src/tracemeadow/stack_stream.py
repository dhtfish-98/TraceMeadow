# Derived from pykdebugparser/callstacks_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from bisect import bisect as meadow_bisect
from collections import namedtuple as meadow_namedtuple
from tracemeadow.handlers.performance_events import meadow_PerfEvent as meadow_PerfEvent
from tracemeadow.handlers.image_events import meadow_DyldUuidMapA as meadow_DyldUuidMapA, meadow_DyldLaunchExecutable as meadow_DyldLaunchExecutable
meadow_Callstack = _name_boundary.named_record('Callstack', ['timestamp', 'tid', 'frames'])
meadow_Frame = _name_boundary.named_record('Frame', ['address', 'uuid', 'offset'])

from tracemeadow.bounded_stream import TraceFormatError

@_name_boundary.class_contract('CallstacksParser', {'feed_generator': 'meadow_feed_generator', 'insert_image': 'meadow_insert_image', 'dyld_addresses': 'meadow_dyld_addresses', 'dyld_uuids': 'meadow_dyld_uuids'})
class meadow_CallstacksParser:
    """Bounded nearest-preceding-image attribution; offsets are heuristic candidates."""

    def __init__(self, dyld_addresses, dyld_uuids, *, max_images=65536,
                 max_frames=65536, max_traces=4194304):
        for value in (max_images, max_frames, max_traces):
            if type(value) is not int or value <= 0:
                raise ValueError('call-stack limits must be positive integers')
        if not isinstance(dyld_addresses, list) or not isinstance(dyld_uuids, list):
            raise TraceFormatError('image address and identifier tables must be lists')
        self._max_images, self._max_frames, self._max_traces = max_images, max_frames, max_traces
        self.dyld_addresses, self.dyld_uuids = dyld_addresses, dyld_uuids
        self._check_tables()
        previous = -1
        for address in dyld_addresses:
            self._check_address(address)
            if address < previous:
                raise TraceFormatError('image addresses must be sorted')
            previous = address

    @staticmethod
    def _check_address(address):
        if type(address) is not int or not 0 <= address <= 0xffffffffffffffff:
            raise TraceFormatError('call-stack address must be an unsigned 64-bit integer')

    def _check_tables(self):
        if len(self.dyld_addresses) != len(self.dyld_uuids):
            raise TraceFormatError('image address and identifier tables have different lengths')
        if len(self.dyld_addresses) > self._max_images:
            raise TraceFormatError('call-stack image limit exceeded')

    def _frame(self, address):
        self._check_address(address)
        index = meadow_bisect(self.dyld_addresses, address) - 1
        if index < 0:
            return meadow_Frame(address, None, None)
        return meadow_Frame(address, self.dyld_uuids[index],
                            address - self.dyld_addresses[index])

    def meadow_feed_generator(self, generator):
        for index, trace in enumerate(generator):
            if index >= self._max_traces:
                raise TraceFormatError('call-stack trace limit exceeded; analysis is incomplete')
            self._check_tables()
            if isinstance(trace, meadow_PerfEvent) and trace.cs_frames is not None:
                if not trace.ktraces:
                    raise TraceFormatError('sample has no source event')
                frames = []
                for address in trace.cs_frames:
                    if len(frames) >= self._max_frames:
                        raise TraceFormatError('call-stack frame limit exceeded; analysis is incomplete')
                    frames.append(self._frame(address))
                first = trace.ktraces[0]
                yield meadow_Callstack(first.timestamp, first.tid, frames)
            elif isinstance(trace, meadow_DyldUuidMapA):
                self.meadow_insert_image(trace.load_addr, trace.uuid)
            elif isinstance(trace, meadow_DyldLaunchExecutable):
                for image_index, image in enumerate(trace.uuid_map_a):
                    if image_index >= self._max_images:
                        raise TraceFormatError('launch image list limit exceeded')
                    self.meadow_insert_image(image.load_addr, image.uuid)

    def meadow_insert_image(self, address, uuid):
        self._check_address(address)
        self._check_tables()
        position = meadow_bisect(self.dyld_addresses, address)
        if position and self.dyld_addresses[position - 1] == address:
            return
        if len(self.dyld_addresses) >= self._max_images:
            raise TraceFormatError('call-stack image limit exceeded; analysis is incomplete')
        self.dyld_addresses.insert(position, address)
        self.dyld_uuids.insert(position, uuid)

_name_boundary.module_contract(globals(), {'bisect': 'meadow_bisect', 'Frame': 'meadow_Frame', 'CallstacksParser': 'meadow_CallstacksParser', 'Callstack': 'meadow_Callstack', 'DyldLaunchExecutable': 'meadow_DyldLaunchExecutable', 'namedtuple': 'meadow_namedtuple', 'PerfEvent': 'meadow_PerfEvent', 'DyldUuidMapA': 'meadow_DyldUuidMapA'})
