# Derived from tests/traces/test_perf.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent
from tracemeadow.handlers.performance_events import meadow_CallstackFlag as meadow_CallstackFlag, meadow_KperfTiState as meadow_KperfTiState, meadow_SamplerAction as meadow_SamplerAction

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_0c1436c'}, 'test_perf_event')
def meadow_test_perf_event(meadow_traces_parser_0c1436c):
    meadow_events_5fb46be = [meadow_Kevent(timestamp=7006023115068, data=b'\t\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9, 32, 0, 0), tid=1957, debugid=620756993, eventid=620756992, func_qualifier=1), meadow_Kevent(timestamp=7006023115085, data=b'E\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(69, 5, 0, 0), tid=1957, debugid=620888088, eventid=620888088, func_qualifier=0), meadow_Kevent(timestamp=7006023115105, data=b'\xf0[\xc0\xb5\x01\x00\x00\x00\xd4\xe4v\x93\x01\x00\x00\x000\x99\\\x02\x01\x00\x00\x00<\x0b\x16\xd1\x01\x00\x00\x00', values=(7344249840, 6769009876, 4334590256, 7802850108), tid=1957, debugid=620888080, eventid=620888080, func_qualifier=0), meadow_Kevent(timestamp=7006023115123, data=b'\xd4\xe6v\x93\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(6769010388, 0, 0, 0), tid=1957, debugid=620888080, eventid=620888080, func_qualifier=0), meadow_Kevent(timestamp=7006023115140, data=b'\x95\x00\x00\x00\x00\x00\x00\x00\xa5\x07\x00\x00\x00\x00\x00\x00\x80\xb1\x94m\x01\x00\x00\x00\x03\x00\xfc\xff\x00\x00\x00\x00', values=(149, 1957, 6133428608, 4294705155), tid=1957, debugid=620822532, eventid=620822532, func_qualifier=0), meadow_Kevent(timestamp=7006023115153, data=b'\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9, 0, 0, 0), tid=1957, debugid=620756994, eventid=620756992, func_qualifier=2)]
    meadow_ret_7e236e6 = list(_name_boundary.attributes(meadow_traces_parser_0c1436c)['feed_generator'](meadow_events_5fb46be))[4]
    assert meadow_ret_7e236e6.sample_what == [meadow_SamplerAction.SAMPLER_TH_INFO, meadow_SamplerAction.SAMPLER_USTACK]
    assert meadow_ret_7e236e6.actionid == 32
    assert meadow_ret_7e236e6.th_info.pid == 149
    assert meadow_ret_7e236e6.th_info.tid == 1957
    assert meadow_ret_7e236e6.th_info.dq_addr == 6133428608
    assert meadow_ret_7e236e6.th_info.runmode == [meadow_KperfTiState.KPERF_TI_RUNNING, meadow_KperfTiState.KPERF_TI_RUNNABLE]
    assert meadow_ret_7e236e6.cs_flags == [meadow_CallstackFlag.CALLSTACK_VALID, meadow_CallstackFlag.CALLSTACK_64BIT, meadow_CallstackFlag.CALLSTACK_KERNEL_WORDS]
    assert meadow_ret_7e236e6.cs_frames == [7344249840, 6769009876, 4334590256, 7802850108, 6769010388]

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_75b1180'}, 'test_perf_event_without_stack')
def meadow_test_perf_event_without_stack(meadow_traces_parser_75b1180):
    meadow_events_2c0df10 = [meadow_Kevent(timestamp=7006023115068, data=b'\t\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9, 32, 0, 0), tid=1957, debugid=620756993, eventid=620756992, func_qualifier=1), meadow_Kevent(timestamp=7006023115153, data=b'\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(9, 0, 0, 0), tid=1957, debugid=620756994, eventid=620756992, func_qualifier=2)]
    meadow_ret_5830db2 = list(_name_boundary.attributes(meadow_traces_parser_75b1180)['feed_generator'](meadow_events_2c0df10))
    assert meadow_ret_5830db2[0].sample_what == [meadow_SamplerAction.SAMPLER_TH_INFO, meadow_SamplerAction.SAMPLER_USTACK]
    assert meadow_ret_5830db2[0].actionid == 32
    assert meadow_ret_5830db2[0].th_info is None
    assert meadow_ret_5830db2[0].cs_flags is None
    assert meadow_ret_5830db2[0].cs_frames is None

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_110a91a'}, 'test_thd_data')
def meadow_test_thd_data(meadow_traces_parser_110a91a):
    meadow_events_ac55262 = [meadow_Kevent(timestamp=15773877915, data=b'P\x00\x00\x00\x00\x00\x00\x00\x9d\x04\x00\x00\x00\x00\x00\x00\x00\xfa\x17\x05\x01\x00\x00\x00\x03\x00\xfc\xff\x00\x00\x00\x00', values=(80, 1181, 4380424704, 4294705155), tid=1181, debugid=620822532, eventid=620822532, func_qualifier=0)]
    meadow_ret_efbdb3b = list(_name_boundary.attributes(meadow_traces_parser_110a91a)['feed_generator'](meadow_events_ac55262))
    meadow_thd_data_3322be6 = meadow_ret_efbdb3b[0]
    assert meadow_thd_data_3322be6.pid == 80
    assert meadow_thd_data_3322be6.tid == 1181
    assert meadow_thd_data_3322be6.dq_addr == 4380424704
    assert meadow_thd_data_3322be6.runmode == [meadow_KperfTiState.KPERF_TI_RUNNING, meadow_KperfTiState.KPERF_TI_RUNNABLE]

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_feffa1e'}, 'test_thd_cswitch')
def meadow_test_thd_cswitch(meadow_traces_parser_feffa1e):
    meadow_events_eb62435 = [meadow_Kevent(timestamp=15779569737, data=b'`\x10\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(4192, 80, 0, 0), tid=4192, debugid=620822548, eventid=620822548, func_qualifier=0)]
    meadow_ret_dbb8425 = list(_name_boundary.attributes(meadow_traces_parser_feffa1e)['feed_generator'](meadow_events_eb62435))
    meadow_thd_cswitch_545ab17 = meadow_ret_dbb8425[0]
    assert meadow_thd_cswitch_545ab17.tid == 4192
    assert meadow_thd_cswitch_545ab17.pid == 80

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_adbccef'}, 'test_stk_udata')
def meadow_test_stk_udata(meadow_traces_parser_adbccef):
    meadow_events_71cfd54 = [meadow_Kevent(timestamp=15771902115, data=b'\x94\xec\x12\x93\x01\x00\x00\x00\xa8\xf8\x12\x93\x01\x00\x00\x008\x93\x13\x93\x01\x00\x00\x00\xa4\xa5\xbe\xd9\x01\x00\x00\x00', values=(6762458260, 6762461352, 6762500920, 7948117412), tid=7565, debugid=620888080, eventid=620888080, func_qualifier=0)]
    meadow_ret_ef6941f = list(_name_boundary.attributes(meadow_traces_parser_adbccef)['feed_generator'](meadow_events_71cfd54))
    meadow_stk_udata_de91292 = meadow_ret_ef6941f[0]
    assert meadow_stk_udata_de91292.frames == [6762458260, 6762461352, 6762500920, 7948117412]

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_8de9551'}, 'test_stk_uhdr')
def meadow_test_stk_uhdr(meadow_traces_parser_8de9551):
    meadow_events_94c3983 = [meadow_Kevent(timestamp=15772304192, data=b'E\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(69, 7, 0, 0), tid=6206, debugid=620888088, eventid=620888088, func_qualifier=0)]
    meadow_ret_8e45ebd = list(_name_boundary.attributes(meadow_traces_parser_8de9551)['feed_generator'](meadow_events_94c3983))
    meadow_stk_uhdr_575bafc = meadow_ret_8e45ebd[0]
    assert meadow_stk_uhdr_575bafc.flags == [meadow_CallstackFlag.CALLSTACK_VALID, meadow_CallstackFlag.CALLSTACK_64BIT, meadow_CallstackFlag.CALLSTACK_KERNEL_WORDS]
    assert meadow_stk_uhdr_575bafc.nframes == 7
_name_boundary.module_contract(globals(), {'test_thd_cswitch': 'meadow_test_thd_cswitch', 'test_stk_udata': 'meadow_test_stk_udata', 'SamplerAction': 'meadow_SamplerAction', 'test_perf_event': 'meadow_test_perf_event', 'test_perf_event_without_stack': 'meadow_test_perf_event_without_stack', 'Kevent': 'meadow_Kevent', 'test_stk_uhdr': 'meadow_test_stk_uhdr', 'test_thd_data': 'meadow_test_thd_data', 'CallstackFlag': 'meadow_CallstackFlag', 'KperfTiState': 'meadow_KperfTiState'})
