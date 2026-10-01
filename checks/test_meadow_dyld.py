# Derived from tests/traces/test_dyld.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from uuid import UUID as meadow_UUID
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent
from tracemeadow.handlers.image_events import meadow_RtldFlag as meadow_RtldFlag

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_d99e423'}, 'test_uuid_map_a')
def meadow_test_uuid_map_a(meadow_traces_parser_d99e423):
    meadow_events_4496a3c = [meadow_Kevent(timestamp=2087564153638, data=b'\x19\xdd*\xd4E\xe01\x97\xa5\xc4S\xb3W\xf3a\xa0\x000u\xaa\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(10894735564102884633, 11556785676805719205, 7154774016, 0), tid=200651, debugid=520421376, eventid=520421376, func_qualifier=0)]
    meadow_ret_7320b31 = list(_name_boundary.attributes(meadow_traces_parser_d99e423)['feed_generator'](meadow_events_4496a3c))
    assert meadow_ret_7320b31[0].uuid == meadow_UUID('19dd2ad4-45e0-3197-a5c4-53b357f361a0')
    assert meadow_ret_7320b31[0].load_addr == 7154774016
    assert meadow_ret_7320b31[0].fsid == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_e48a8e7'}, 'test_uuid_map_b')
def meadow_test_uuid_map_b(meadow_traces_parser_e48a8e7):
    meadow_events_f049afe = [meadow_Kevent(timestamp=2086624121103, data=b'\xe9@\x02\x00\xff\xff\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(1152921500312027369, 0, 0, 0), tid=200063, debugid=520421380, eventid=520421380, func_qualifier=0)]
    meadow_ret_12bfd2a = list(_name_boundary.attributes(meadow_traces_parser_e48a8e7)['feed_generator'](meadow_events_f049afe))
    assert meadow_ret_12bfd2a[0].fid_objno == 147689
    assert meadow_ret_12bfd2a[0].fid_generation == 268435455

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_1db6c37'}, 'test_uuid_shared_cache_a')
def meadow_test_uuid_shared_cache_a(meadow_traces_parser_1db6c37):
    meadow_events_d6d108c = [meadow_Kevent(timestamp=2086625169813, data=b'\n\x01x\x91Y\xfd>"\xb8\x9e\x148K0\xb5\n\x00\x80e\x8a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(2467688206980088074, 771576010785463992, 6616875008, 0), tid=200065, debugid=520421416, eventid=520421416, func_qualifier=0)]
    meadow_ret_7fa6b44 = list(_name_boundary.attributes(meadow_traces_parser_1db6c37)['feed_generator'](meadow_events_d6d108c))
    assert meadow_ret_7fa6b44[0].uuid == meadow_UUID('0a017891-59fd-3e22-b89e-14384b30b50a')
    assert meadow_ret_7fa6b44[0].load_addr == 6616875008
    assert meadow_ret_7fa6b44[0].fsid == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_b8e71f2'}, 'test_uuid_shared_cache_b')
def meadow_test_uuid_shared_cache_b(meadow_traces_parser_b8e71f2):
    meadow_events_35d657c = [meadow_Kevent(timestamp=2086625169822, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=200065, debugid=520421420, eventid=520421420, func_qualifier=0)]
    meadow_ret_0d6fd22 = list(_name_boundary.attributes(meadow_traces_parser_b8e71f2)['feed_generator'](meadow_events_35d657c))
    assert meadow_ret_0d6fd22[0].fid_objno == 0
    assert meadow_ret_0d6fd22[0].fid_generation == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_33efff6'}, 'test_timing_launch_executable')
def meadow_test_timing_launch_executable(meadow_traces_parser_33efff6):
    meadow_events_8ed7d58 = [meadow_Kevent(timestamp=2375523588323, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x97\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(1, 4304863232, 0, 0), tid=227140, debugid=520552453, eventid=520552452, func_qualifier=1), meadow_Kevent(timestamp=2087564153638, data=b'\x19\xdd*\xd4E\xe01\x97\xa5\xc4S\xb3W\xf3a\xa0\x000u\xaa\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(10894735564102884633, 11556785676805719205, 7154774016, 0), tid=227140, debugid=520421376, eventid=520421376, func_qualifier=0), meadow_Kevent(timestamp=2375524298242, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00', values=(1, 0, 0, 3), tid=227140, debugid=520552454, eventid=520552452, func_qualifier=2)]
    meadow_ret_d3c347e = list(_name_boundary.attributes(meadow_traces_parser_33efff6)['feed_generator'](meadow_events_8ed7d58))
    assert meadow_ret_d3c347e[1].main_executable_mh == 4304863232
    assert meadow_ret_d3c347e[1].uuid_map_a[0].uuid == meadow_UUID('19dd2ad4-45e0-3197-a5c4-53b357f361a0')
    assert meadow_ret_d3c347e[1].uuid_map_a[0].load_addr == 7154774016

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_24ef0bc'}, 'test_timing_func_for_add_image')
def meadow_test_timing_func_for_add_image(meadow_traces_parser_24ef0bc):
    meadow_events_90ceacb = [meadow_Kevent(timestamp=2375525615541, data=b'\xd1\x06\x00\x00\x00\x00\x00\x80\x00\xa0\xa1\xb9\x01\x00\x00\x00\xbcOD\x9c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777553, 7409344512, 6916689852, 0), tid=227140, debugid=520552473, eventid=520552472, func_qualifier=1), meadow_Kevent(timestamp=2375525615595, data=b'\xd1\x06\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777553, 0, 0, 0), tid=227140, debugid=520552474, eventid=520552472, func_qualifier=2)]
    meadow_ret_bcc8732 = list(_name_boundary.attributes(meadow_traces_parser_24ef0bc)['feed_generator'](meadow_events_90ceacb))
    assert meadow_ret_bcc8732[0].addr == 7409344512
    assert meadow_ret_bcc8732[0].func == 6916689852

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_a34da7d'}, 'test_timing_bootstrap_start')
def meadow_test_timing_bootstrap_start(meadow_traces_parser_a34da7d):
    meadow_events_b2c0897 = [meadow_Kevent(timestamp=2375523577973, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=227140, debugid=520552500, eventid=520552500, func_qualifier=0)]
    meadow_ret_459de82 = list(_name_boundary.attributes(meadow_traces_parser_a34da7d)['feed_generator'](meadow_events_b2c0897))
    assert str(meadow_ret_459de82[0]) == 'DBG_DYLD_TIMING_BOOTSTRAP_START'

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_7c95246'}, 'test_timing_dlopen')
def meadow_test_timing_dlopen(meadow_traces_parser_7c95246):
    meadow_events_0167473 = [meadow_Kevent(timestamp=2375526922507, data=b'\x00\x00\x08\x1f\x00\x00\x00\x00\x0f\xda\x00\x00\x00\x00\xacp/System/Library/', values=(520617984, 8118864228242217487, 3417499243072017199, 3420891154821048652), tid=227157, debugid=117506049, eventid=117506048, func_qualifier=1), meadow_Kevent(timestamp=2375526922509, data=b'PrivateFrameworks/AppleFSCompres', values=(5072588517250003536, 7742373267996762482, 5072579785478188915, 8315178114207400787), tid=227157, debugid=117506048, eventid=117506048, func_qualifier=0), meadow_Kevent(timestamp=2375526922512, data=b'sion.framework/AppleFSCompressio', values=(7021787118631348595, 4697091075611256173, 8017343323464036464, 8028074750225051757), tid=227157, debugid=117506048, eventid=117506048, func_qualifier=0), meadow_Kevent(timestamp=2375526922515, data=b'n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(110, 0, 0, 0), tid=227157, debugid=117506050, eventid=117506048, func_qualifier=2), meadow_Kevent(timestamp=2375526922532, data=b'(\x08\x00\x00\x00\x00\x00\x80\x0f\xda\x00\x00\x00\x00\xacp\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777896, 8118864228242217487, 256, 0), tid=227157, debugid=520617985, eventid=520617984, func_qualifier=1), meadow_Kevent(timestamp=2375526922543, data=b'\x00\x00\x08\x1f\x00\x00\x00\x00\x0f\xda\x00\x00\x00\x00\xacp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(520617984, 8118864228242217487, 0, 0), tid=227157, debugid=117506051, eventid=117506048, func_qualifier=3), meadow_Kevent(timestamp=2375526922709, data=b'(\x08\x00\x00\x00\x00\x00\x80\x81\xfd\xfa\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777896, 234552705, 0, 0), tid=227157, debugid=520617986, eventid=520617984, func_qualifier=2)]
    meadow_ret_a31a59c = list(_name_boundary.attributes(meadow_traces_parser_7c95246)['feed_generator'](meadow_events_0167473))
    meadow_dlopen_ec4002a = meadow_ret_a31a59c[-1]
    assert meadow_dlopen_ec4002a.path == '/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression'
    assert meadow_dlopen_ec4002a.flags == [meadow_RtldFlag.RTLD_FIRST]
    assert meadow_dlopen_ec4002a.handle == 234552705

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_4df01a9'}, 'test_timing_dlopen_preflight')
def meadow_test_timing_dlopen_preflight(meadow_traces_parser_4df01a9):
    meadow_events_0e52683 = [meadow_Kevent(timestamp=2375540021590, data=b'\x04\x00\x08\x1f\x00\x00\x00\x00]\xdb\x00\x00\x00\x00\xacp/System/Library/', values=(520617988, 8118864228242217821, 3417499243072017199, 3420891154821048652), tid=227191, debugid=117506049, eventid=117506048, func_qualifier=1), meadow_Kevent(timestamp=2375540021596, data=b'Frameworks/AVFoundation.framewor', values=(8245940720249172550, 8462059561127211883, 3345734071897646190, 8245940720249172582), tid=227191, debugid=117506048, eventid=117506048, func_qualifier=0), meadow_Kevent(timestamp=2375540021598, data=b'k/AVFoundation\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(7959390264332726123, 121424789660004, 0, 0), tid=227191, debugid=117506050, eventid=117506048, func_qualifier=2), meadow_Kevent(timestamp=2375540021616, data=b'\xb4\x04\x00\x00\x00\x00\x00\x80]\xdb\x00\x00\x00\x00\xacp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777012, 8118864228242217821, 0, 0), tid=227191, debugid=520617989, eventid=520617988, func_qualifier=1), meadow_Kevent(timestamp=2375540021631, data=b'\x04\x00\x08\x1f\x00\x00\x00\x00]\xdb\x00\x00\x00\x00\xacp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(520617988, 8118864228242217821, 0, 0), tid=227191, debugid=117506051, eventid=117506048, func_qualifier=3), meadow_Kevent(timestamp=2375540021742, data=b'\xb4\x04\x00\x00\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777012, 1, 0, 0), tid=227191, debugid=520617990, eventid=520617988, func_qualifier=2)]
    meadow_ret_862f8ae = list(_name_boundary.attributes(meadow_traces_parser_4df01a9)['feed_generator'](meadow_events_0e52683))
    meadow_preflight_df69940 = meadow_ret_862f8ae[-1]
    assert meadow_preflight_df69940.path == '/System/Library/Frameworks/AVFoundation.framework/AVFoundation'
    assert meadow_preflight_df69940.compatible

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_cbefba6'}, 'test_timing_dlclose')
def meadow_test_timing_dlclose(meadow_traces_parser_cbefba6):
    meadow_events_56e4642 = [meadow_Kevent(timestamp=2375542917792, data=b'k\x07\x00\x00\x00\x00\x00\x80\x80O\x1d\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777707, 236801920, 0, 0), tid=227240, debugid=520617993, eventid=520617992, func_qualifier=1), meadow_Kevent(timestamp=2375542919124, data=b'k\x07\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854777707, 0, 0, 0), tid=227240, debugid=520617994, eventid=520617992, func_qualifier=2)]
    meadow_ret_04277b1 = list(_name_boundary.attributes(meadow_traces_parser_cbefba6)['feed_generator'](meadow_events_56e4642))
    assert meadow_ret_04277b1[0].handle == 236801920

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_4938075'}, 'test_timing_dlsym')
def meadow_test_timing_dlsym(meadow_traces_parser_4938075):
    meadow_events_f88880f = [meadow_Kevent(timestamp=2375529754749, data=b'\x0c\x00\x08\x1f\x00\x00\x00\x00\xcc\xda\x00\x00\x00\x00\xacpUIApplicationDid', values=(520617996, 8118864228242217676, 7163375912484948309, 7235389517453685857), tid=227140, debugid=117506049, eventid=117506048, func_qualifier=1), meadow_Kevent(timestamp=2375529754752, data=b'EnterBackgroundNotification\x00\x00\x00\x00\x00', values=(7161077941591633477, 5648761283289442155, 8386093285481477231, 7237481), tid=227140, debugid=117506050, eventid=117506048, func_qualifier=2), meadow_Kevent(timestamp=2375529754762, data=b'\xf3\x08\x00\x00\x00\x00\x00\x80\x80\xf0\xe0\r\x00\x00\x00\x00\xcc\xda\x00\x00\x00\x00\xacp\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854778099, 232845440, 8118864228242217676, 0), tid=227140, debugid=520617997, eventid=520617996, func_qualifier=1), meadow_Kevent(timestamp=2375529754772, data=b'\x0c\x00\x08\x1f\x00\x00\x00\x00\xcc\xda\x00\x00\x00\x00\xacp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(520617996, 8118864228242217676, 0, 0), tid=227140, debugid=117506051, eventid=117506048, func_qualifier=3), meadow_Kevent(timestamp=2375529754963, data=b'\xf3\x08\x00\x00\x00\x00\x00\x80P!\x9e\xd9\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854778099, 7945986384, 0, 0), tid=227140, debugid=520617998, eventid=520617996, func_qualifier=2)]
    meadow_ret_bd45dd9 = list(_name_boundary.attributes(meadow_traces_parser_4938075)['feed_generator'](meadow_events_f88880f))
    meadow_dlsym_94fbd3c = meadow_ret_bd45dd9[-1]
    assert meadow_dlsym_94fbd3c.handle == 232845440
    assert meadow_dlsym_94fbd3c.symbol == 'UIApplicationDidEnterBackgroundNotification'
    assert meadow_dlsym_94fbd3c.address == 7945986384

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_d03b403'}, 'test_timing_dladdr')
def meadow_test_timing_dladdr(meadow_traces_parser_d03b403):
    meadow_events_ee98110 = [meadow_Kevent(timestamp=2375525034640, data=b'\x86\x04\x00\x00\x00\x00\x00\x80(}\xe9\x8d\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9223372036854776966, 6675856680, 0, 0), tid=227161, debugid=520618001, eventid=520618000, func_qualifier=1), meadow_Kevent(timestamp=2375525034950, data=b'\x86\x04\x00\x00\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00`\xe5\x8d\x01\x00\x00\x00\x0c|\xe9\x8d\x01\x00\x00\x00', values=(9223372036854776966, 1, 6675587072, 6675856396), tid=227161, debugid=520618002, eventid=520618000, func_qualifier=2)]
    meadow_ret_9bdd0d6 = list(_name_boundary.attributes(meadow_traces_parser_d03b403)['feed_generator'](meadow_events_ee98110))
    assert meadow_ret_9bdd0d6[0].addr == 6675856680
    assert meadow_ret_9bdd0d6[0].ret == 1
_name_boundary.module_contract(globals(), {'test_uuid_map_a': 'meadow_test_uuid_map_a', 'test_timing_bootstrap_start': 'meadow_test_timing_bootstrap_start', 'test_uuid_shared_cache_b': 'meadow_test_uuid_shared_cache_b', 'test_timing_launch_executable': 'meadow_test_timing_launch_executable', 'test_timing_func_for_add_image': 'meadow_test_timing_func_for_add_image', 'test_timing_dlopen': 'meadow_test_timing_dlopen', 'test_timing_dladdr': 'meadow_test_timing_dladdr', 'test_timing_dlclose': 'meadow_test_timing_dlclose', 'test_uuid_shared_cache_a': 'meadow_test_uuid_shared_cache_a', 'Kevent': 'meadow_Kevent', 'test_timing_dlopen_preflight': 'meadow_test_timing_dlopen_preflight', 'test_timing_dlsym': 'meadow_test_timing_dlsym', 'UUID': 'meadow_UUID', 'RtldFlag': 'meadow_RtldFlag', 'test_uuid_map_b': 'meadow_test_uuid_map_b'})
