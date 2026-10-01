# Derived from pykdebugparser/callstacks_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from bisect import bisect as meadow_bisect
from collections import namedtuple as meadow_namedtuple
from tracemeadow.handlers.performance_events import meadow_PerfEvent as meadow_PerfEvent
from tracemeadow.handlers.image_events import meadow_DyldUuidMapA as meadow_DyldUuidMapA, meadow_DyldLaunchExecutable as meadow_DyldLaunchExecutable
meadow_Callstack = _name_boundary.named_record('Callstack', ['timestamp', 'tid', 'frames'])
meadow_Frame = _name_boundary.named_record('Frame', ['address', 'uuid', 'offset'])

@_name_boundary.class_contract('CallstacksParser', {'feed_generator': 'meadow_feed_generator', 'insert_image': 'meadow_insert_image', 'dyld_addresses': 'meadow_dyld_addresses', 'dyld_uuids': 'meadow_dyld_uuids'})
class meadow_CallstacksParser:

    @_name_boundary.callable_contract({'self': 'meadow_self_fa5ae3a', 'dyld_addresses': 'meadow_dyld_addresses_a465635', 'dyld_uuids': 'meadow_dyld_uuids_a8be7e2'}, '__init__')
    def __init__(meadow_self_fa5ae3a, meadow_dyld_addresses_a465635, meadow_dyld_uuids_a8be7e2):
        _name_boundary.attributes(meadow_self_fa5ae3a)['dyld_addresses'] = meadow_dyld_addresses_a465635
        _name_boundary.attributes(meadow_self_fa5ae3a)['dyld_uuids'] = meadow_dyld_uuids_a8be7e2

    @_name_boundary.callable_contract({'self': 'meadow_self_c45a5c6', 'generator': 'meadow_generator_4517800'}, 'feed_generator')
    def meadow_feed_generator(meadow_self_c45a5c6, meadow_generator_4517800):
        for meadow_trace_498c124 in meadow_generator_4517800:
            if isinstance(meadow_trace_498c124, meadow_PerfEvent) and meadow_trace_498c124.cs_frames is not None:
                meadow_frames_dec8c76 = []
                for meadow_frame_be113fb in meadow_trace_498c124.cs_frames:
                    meadow_index__4ec998d = meadow_bisect(_name_boundary.attributes(meadow_self_c45a5c6)['dyld_addresses'], meadow_frame_be113fb) - 1
                    if meadow_index__4ec998d > -1:
                        meadow_frames_dec8c76.append(meadow_Frame(meadow_frame_be113fb, _name_boundary.attributes(meadow_self_c45a5c6)['dyld_uuids'][meadow_index__4ec998d], meadow_frame_be113fb - _name_boundary.attributes(meadow_self_c45a5c6)['dyld_addresses'][meadow_index__4ec998d]))
                    else:
                        meadow_frames_dec8c76.append(meadow_Frame(meadow_frame_be113fb, None, None))
                yield meadow_Callstack(meadow_trace_498c124.ktraces[0].timestamp, meadow_trace_498c124.ktraces[0].tid, meadow_frames_dec8c76)
            elif isinstance(meadow_trace_498c124, meadow_DyldUuidMapA):
                _name_boundary.attributes(meadow_self_c45a5c6)['insert_image'](meadow_trace_498c124.load_addr, meadow_trace_498c124.uuid)
            elif isinstance(meadow_trace_498c124, meadow_DyldLaunchExecutable):
                for meadow_image_a792200 in meadow_trace_498c124.uuid_map_a:
                    _name_boundary.attributes(meadow_self_c45a5c6)['insert_image'](meadow_image_a792200.load_addr, meadow_image_a792200.uuid)

    @_name_boundary.callable_contract({'self': 'meadow_self_e3604d8', 'address': 'meadow_address_1010c9e', 'uuid': 'meadow_uuid_2d1772b'}, 'insert_image')
    def meadow_insert_image(meadow_self_e3604d8, meadow_address_1010c9e, meadow_uuid_2d1772b):
        if meadow_address_1010c9e in _name_boundary.attributes(meadow_self_e3604d8)['dyld_addresses']:
            return
        meadow_index__fbb5f90 = meadow_bisect(_name_boundary.attributes(meadow_self_e3604d8)['dyld_addresses'], meadow_address_1010c9e)
        _name_boundary.attributes(meadow_self_e3604d8)['dyld_addresses'].insert(meadow_index__fbb5f90, meadow_address_1010c9e)
        _name_boundary.attributes(meadow_self_e3604d8)['dyld_uuids'].insert(meadow_index__fbb5f90, meadow_uuid_2d1772b)
_name_boundary.module_contract(globals(), {'bisect': 'meadow_bisect', 'Frame': 'meadow_Frame', 'CallstacksParser': 'meadow_CallstacksParser', 'Callstack': 'meadow_Callstack', 'DyldLaunchExecutable': 'meadow_DyldLaunchExecutable', 'namedtuple': 'meadow_namedtuple', 'PerfEvent': 'meadow_PerfEvent', 'DyldUuidMapA': 'meadow_DyldUuidMapA'})
