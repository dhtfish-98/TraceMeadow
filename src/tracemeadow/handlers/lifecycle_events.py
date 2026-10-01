# Derived from pykdebugparser/trace_handlers/trace.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass
from typing import List as meadow_List
from tracemeadow.event_records import meadow_DgbFuncQual as meadow_DgbFuncQual

@_name_boundary.class_contract('TraceDataNewthread', {})
@meadow_dataclass
class meadow_TraceDataNewthread:
    ktraces: meadow_List
    tid: int
    pid: int
    is_exec_copy: int
    uniqueid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_1ff8f8a'}, '__str__')
    def __str__(meadow_self_1ff8f8a):
        return f'New thread {meadow_self_1ff8f8a.tid} of parent: {meadow_self_1ff8f8a.pid}'

@_name_boundary.class_contract('TraceDataExec', {})
@meadow_dataclass
class meadow_TraceDataExec:
    ktraces: meadow_List
    pid: int
    fsid: int
    fileid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_77eae8c'}, '__str__')
    def __str__(meadow_self_77eae8c):
        return f'New process pid: {meadow_self_77eae8c.pid}'

@_name_boundary.class_contract('TraceDataThreadTerminate', {})
@meadow_dataclass
class meadow_TraceDataThreadTerminate:
    ktraces: meadow_List
    tid: int
    pid: int = None
    name: str = ''

    @_name_boundary.callable_contract({'self': 'meadow_self_a65728f'}, '__str__')
    def __str__(meadow_self_a65728f):
        meadow_rep_b4f5638 = f'Thread terminated tid: {meadow_self_a65728f.tid}'
        if meadow_self_a65728f.pid is not None:
            meadow_rep_b4f5638 += f', pid: {meadow_self_a65728f.pid}'
        if _name_boundary.attributes(meadow_self_a65728f)['name']:
            meadow_rep_b4f5638 += f", name: {_name_boundary.attributes(meadow_self_a65728f)['name']}"
        return meadow_rep_b4f5638

@_name_boundary.class_contract('TraceDataThreadTerminatePid', {})
@meadow_dataclass
class meadow_TraceDataThreadTerminatePid:
    ktraces: meadow_List
    pid: int
    uniqueid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ce88996'}, '__str__')
    def __str__(meadow_self_ce88996):
        return f'Thread terminated thread pid: {meadow_self_ce88996.pid}, unique id {meadow_self_ce88996.uniqueid}'

@_name_boundary.class_contract('TraceStringGlobal', {})
@meadow_dataclass
class meadow_TraceStringGlobal:
    ktraces: meadow_List
    debugid: int
    str_id: int
    vstr: str

    @_name_boundary.callable_contract({'self': 'meadow_self_156726b'}, '__str__')
    def __str__(meadow_self_156726b):
        return f'New global string: "{meadow_self_156726b.vstr}", id: {meadow_self_156726b.str_id}'

@_name_boundary.class_contract('TraceStringNewthread', {})
@meadow_dataclass
class meadow_TraceStringNewthread:
    ktraces: meadow_List
    name: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f04c914'}, '__str__')
    def __str__(meadow_self_f04c914):
        return f"New thread of parent: {_name_boundary.attributes(meadow_self_f04c914)['name']}"

@_name_boundary.class_contract('TraceStringExec', {})
@meadow_dataclass
class meadow_TraceStringExec:
    ktraces: meadow_List
    name: str

    @_name_boundary.callable_contract({'self': 'meadow_self_232c379'}, '__str__')
    def __str__(meadow_self_232c379):
        return f"New process name: {_name_boundary.attributes(meadow_self_232c379)['name']}"

@_name_boundary.class_contract('TraceStringProcExit', {})
@meadow_dataclass
class meadow_TraceStringProcExit:
    ktraces: meadow_List
    name: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d001d7e'}, '__str__')
    def __str__(meadow_self_d001d7e):
        return f"Process exit name: {_name_boundary.attributes(meadow_self_d001d7e)['name']}"

@_name_boundary.class_contract('TraceStringThreadname', {})
@meadow_dataclass
class meadow_TraceStringThreadname:
    ktraces: meadow_List
    name: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3258307'}, '__str__')
    def __str__(meadow_self_3258307):
        return f"New thread name: {_name_boundary.attributes(meadow_self_3258307)['name']}"

@_name_boundary.class_contract('TraceStringThreadnamePrev', {})
@meadow_dataclass
class meadow_TraceStringThreadnamePrev:
    ktraces: meadow_List
    name: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c81972d'}, '__str__')
    def __str__(meadow_self_c81972d):
        return f"Thread terminated name: {_name_boundary.attributes(meadow_self_c81972d)['name']}"

@_name_boundary.callable_contract({'parser': 'meadow_parser_7906fe8', 'events': 'meadow_events_9983202'}, 'handle_trace_data_newthread')
def meadow_handle_trace_data_newthread(meadow_parser_7906fe8, meadow_events_9983202):
    meadow_result_0088e8f = meadow_events_9983202[0].values
    _name_boundary.attributes(meadow_parser_7906fe8)['last_data_newthread'] = meadow_TraceDataNewthread(meadow_events_9983202, meadow_result_0088e8f[0], meadow_result_0088e8f[1], meadow_result_0088e8f[2], meadow_result_0088e8f[3])
    _name_boundary.attributes(meadow_parser_7906fe8)['threads_pids'][_name_boundary.attributes(meadow_parser_7906fe8)['last_data_newthread'].tid] = _name_boundary.attributes(meadow_parser_7906fe8)['last_data_newthread'].pid
    return _name_boundary.attributes(meadow_parser_7906fe8)['last_data_newthread']

@_name_boundary.callable_contract({'parser': 'meadow_parser_5c32762', 'events': 'meadow_events_e9d168c'}, 'handle_trace_data_exec')
def meadow_handle_trace_data_exec(meadow_parser_5c32762, meadow_events_e9d168c):
    meadow_result_2313d56 = meadow_events_e9d168c[0].values
    _name_boundary.attributes(meadow_parser_5c32762)['last_data_exec'] = meadow_TraceDataExec(meadow_events_e9d168c, meadow_result_2313d56[0], meadow_result_2313d56[1], meadow_result_2313d56[2])
    return _name_boundary.attributes(meadow_parser_5c32762)['last_data_exec']

@_name_boundary.callable_contract({'parser': 'meadow_parser_27ed492', 'events': 'meadow_events_00f78e6'}, 'handle_trace_data_thread_terminate')
def meadow_handle_trace_data_thread_terminate(meadow_parser_27ed492, meadow_events_00f78e6):
    meadow_tid_c2bf755 = meadow_events_00f78e6[0].values[0]
    meadow_event_f363333 = meadow_TraceDataThreadTerminate(meadow_events_00f78e6, meadow_tid_c2bf755, _name_boundary.attributes(meadow_parser_27ed492)['threads_pids'].get(meadow_tid_c2bf755))
    _name_boundary.attributes(meadow_event_f363333)['name'] = _name_boundary.attributes(meadow_parser_27ed492)['tids_names'].get(meadow_tid_c2bf755, '')
    return meadow_event_f363333

@_name_boundary.callable_contract({'parser': 'meadow_parser_b0295d6', 'events': 'meadow_events_484d07f'}, 'handle_trace_data_thread_terminate_pid')
def meadow_handle_trace_data_thread_terminate_pid(meadow_parser_b0295d6, meadow_events_484d07f):
    meadow_result_db41ef9 = meadow_events_484d07f[0].values
    meadow_event_b868676 = meadow_TraceDataThreadTerminatePid(meadow_events_484d07f, meadow_result_db41ef9[0], meadow_result_db41ef9[1])
    _name_boundary.attributes(meadow_parser_b0295d6)['threads_pids'][meadow_events_484d07f[0].tid] = meadow_event_b868676.pid
    return meadow_event_b868676

@_name_boundary.callable_contract({'parser': 'meadow_parser_d67bfc2', 'events': 'meadow_events_b922a35'}, 'handle_trace_string_global')
def meadow_handle_trace_string_global(meadow_parser_d67bfc2, meadow_events_b922a35):
    meadow_debugid_1104719 = 0
    meadow_str_id_d0cc92e = 0
    meadow_vstr_57b7f46 = b''
    meadow_lookup_events_25f4712 = []
    for meadow_event_4347c66 in meadow_events_b922a35:
        meadow_lookup_events_25f4712.append(meadow_event_4347c66)
        if meadow_event_4347c66.func_qualifier & meadow_DgbFuncQual.DBG_FUNC_START.value:
            meadow_debugid_1104719 = meadow_event_4347c66.values[0]
            meadow_str_id_d0cc92e = meadow_event_4347c66.values[1]
            meadow_vstr_57b7f46 += meadow_event_4347c66.data[16:]
        else:
            meadow_vstr_57b7f46 += meadow_event_4347c66.data
        if meadow_event_4347c66.func_qualifier & meadow_DgbFuncQual.DBG_FUNC_END.value:
            break
    meadow_event_4347c66 = meadow_TraceStringGlobal(meadow_lookup_events_25f4712, meadow_debugid_1104719, meadow_str_id_d0cc92e, meadow_vstr_57b7f46.replace(b'\x00', b'').decode(errors='backslashreplace'))
    if meadow_event_4347c66.vstr:
        _name_boundary.attributes(meadow_parser_d67bfc2)['global_strings'][meadow_event_4347c66.str_id] = meadow_event_4347c66.vstr
    return meadow_event_4347c66

@_name_boundary.callable_contract({'parser': 'meadow_parser_38b99bb', 'events': 'meadow_events_3c94539'}, 'handle_trace_string_newthread')
def meadow_handle_trace_string_newthread(meadow_parser_38b99bb, meadow_events_3c94539):
    meadow_event_5f88a92 = meadow_TraceStringNewthread(meadow_events_3c94539, meadow_events_3c94539[0].data.replace(b'\x00', b'').decode())
    _name_boundary.attributes(meadow_parser_38b99bb)['pids_names'][_name_boundary.attributes(meadow_parser_38b99bb)['last_data_newthread'].pid] = _name_boundary.attributes(meadow_event_5f88a92)['name']
    return meadow_event_5f88a92

@_name_boundary.callable_contract({'parser': 'meadow_parser_ba0935d', 'events': 'meadow_events_5e3d0bf'}, 'handle_trace_string_exec')
def meadow_handle_trace_string_exec(meadow_parser_ba0935d, meadow_events_5e3d0bf):
    meadow_event_19beda6 = meadow_TraceStringExec(meadow_events_5e3d0bf, meadow_events_5e3d0bf[0].data.replace(b'\x00', b'').decode())
    _name_boundary.attributes(meadow_parser_ba0935d)['pids_names'][_name_boundary.attributes(meadow_parser_ba0935d)['last_data_exec'].pid] = _name_boundary.attributes(meadow_event_19beda6)['name']
    return meadow_event_19beda6

@_name_boundary.callable_contract({'parser': 'meadow_parser_bdc394e', 'events': 'meadow_events_ec58aa2'}, 'handle_trace_string_proc_exit')
def meadow_handle_trace_string_proc_exit(meadow_parser_bdc394e, meadow_events_ec58aa2):
    return meadow_TraceStringProcExit(meadow_events_ec58aa2, meadow_events_ec58aa2[0].data.replace(b'\x00', b'').decode())

@_name_boundary.callable_contract({'parser': 'meadow_parser_4449c35', 'events': 'meadow_events_dc52839'}, 'handle_trace_string_threadname')
def meadow_handle_trace_string_threadname(meadow_parser_4449c35, meadow_events_dc52839):
    meadow_name_209650d = b''.join([meadow_e_bed346b.data for meadow_e_bed346b in meadow_events_dc52839]).replace(b'\x00', b'').decode()
    meadow_event_b1d6b1f = meadow_TraceStringThreadname(meadow_events_dc52839, meadow_name_209650d)
    _name_boundary.attributes(meadow_parser_4449c35)['tids_names'][meadow_events_dc52839[0].tid] = _name_boundary.attributes(meadow_event_b1d6b1f)['name']
    return meadow_event_b1d6b1f

@_name_boundary.callable_contract({'parser': 'meadow_parser_666dbcb', 'events': 'meadow_events_7c49eae'}, 'handle_trace_string_threadname_prev')
def meadow_handle_trace_string_threadname_prev(meadow_parser_666dbcb, meadow_events_7c49eae):
    meadow_name_73a5ff8 = b''.join([meadow_e_030da3b.data for meadow_e_030da3b in meadow_events_7c49eae]).replace(b'\x00', b'').decode()
    meadow_event_e4b0126 = meadow_TraceStringThreadnamePrev(meadow_events_7c49eae, meadow_name_73a5ff8)
    _name_boundary.attributes(meadow_parser_666dbcb)['tids_names'][meadow_events_7c49eae[0].tid] = _name_boundary.attributes(meadow_event_e4b0126)['name']
    return meadow_event_e4b0126
meadow_handlers = {'TRACE_DATA_NEWTHREAD': meadow_handle_trace_data_newthread, 'TRACE_DATA_EXEC': meadow_handle_trace_data_exec, 'TRACE_DATA_THREAD_TERMINATE': meadow_handle_trace_data_thread_terminate, 'TRACE_DATA_THREAD_TERMINATE_PID': meadow_handle_trace_data_thread_terminate_pid, 'TRACE_STRING_GLOBAL': meadow_handle_trace_string_global, 'TRACE_STRING_NEWTHREAD': meadow_handle_trace_string_newthread, 'TRACE_STRING_EXEC': meadow_handle_trace_string_exec, 'TRACE_STRING_PROC_EXIT': meadow_handle_trace_string_proc_exit, 'TRACE_STRING_THREADNAME': meadow_handle_trace_string_threadname, 'TRACE_STRING_THREADNAME_PREV': meadow_handle_trace_string_threadname_prev}
_name_boundary.module_contract(globals(), {'TraceStringProcExit': 'meadow_TraceStringProcExit', 'handle_trace_string_proc_exit': 'meadow_handle_trace_string_proc_exit', 'handle_trace_string_newthread': 'meadow_handle_trace_string_newthread', 'handle_trace_string_exec': 'meadow_handle_trace_string_exec', 'handlers': 'meadow_handlers', 'TraceDataThreadTerminate': 'meadow_TraceDataThreadTerminate', 'dataclass': 'meadow_dataclass', 'handle_trace_data_thread_terminate': 'meadow_handle_trace_data_thread_terminate', 'TraceStringThreadname': 'meadow_TraceStringThreadname', 'TraceStringNewthread': 'meadow_TraceStringNewthread', 'handle_trace_string_threadname_prev': 'meadow_handle_trace_string_threadname_prev', 'handle_trace_string_global': 'meadow_handle_trace_string_global', 'TraceDataThreadTerminatePid': 'meadow_TraceDataThreadTerminatePid', 'TraceDataExec': 'meadow_TraceDataExec', 'handle_trace_string_threadname': 'meadow_handle_trace_string_threadname', 'DgbFuncQual': 'meadow_DgbFuncQual', 'TraceStringExec': 'meadow_TraceStringExec', 'TraceDataNewthread': 'meadow_TraceDataNewthread', 'List': 'meadow_List', 'handle_trace_data_thread_terminate_pid': 'meadow_handle_trace_data_thread_terminate_pid', 'TraceStringThreadnamePrev': 'meadow_TraceStringThreadnamePrev', 'TraceStringGlobal': 'meadow_TraceStringGlobal', 'handle_trace_data_exec': 'meadow_handle_trace_data_exec', 'handle_trace_data_newthread': 'meadow_handle_trace_data_newthread'})
