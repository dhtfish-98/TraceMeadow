# Derived from tests/traces/test_trace.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_acb3608'}, 'test_trace_data_thread_terminate')
def meadow_test_trace_data_thread_terminate(meadow_traces_parser_acb3608):
    meadow_events_aede3d5 = [meadow_Kevent(timestamp=1805581011060, data=b'z\x1b\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(269178, 0, 0, 0), tid=479, debugid=117440524, eventid=117440524, func_qualifier=0)]
    _name_boundary.attributes(meadow_traces_parser_acb3608)['threads_pids'][269178] = 61
    _name_boundary.attributes(meadow_traces_parser_acb3608)['tids_names'][269178] = 'terminated thread'
    meadow_ret_cb54dd4 = list(_name_boundary.attributes(meadow_traces_parser_acb3608)['feed_generator'](meadow_events_aede3d5))
    assert str(meadow_ret_cb54dd4[0]) == 'Thread terminated tid: 269178, pid: 61, name: terminated thread'

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_a23d383'}, 'test_trace_data_thread_terminate_missing_tid')
def meadow_test_trace_data_thread_terminate_missing_tid(meadow_traces_parser_a23d383):
    meadow_events_6d46393 = [meadow_Kevent(timestamp=1805581011060, data=b'z\x1b\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(269178, 0, 0, 0), tid=479, debugid=117440524, eventid=117440524, func_qualifier=0)]
    meadow_ret_c6b9284 = list(_name_boundary.attributes(meadow_traces_parser_a23d383)['feed_generator'](meadow_events_6d46393))
    assert str(meadow_ret_c6b9284[0]) == 'Thread terminated tid: 269178'
_name_boundary.module_contract(globals(), {'test_trace_data_thread_terminate_missing_tid': 'meadow_test_trace_data_thread_terminate_missing_tid', 'Kevent': 'meadow_Kevent', 'test_trace_data_thread_terminate': 'meadow_test_trace_data_thread_terminate'})
