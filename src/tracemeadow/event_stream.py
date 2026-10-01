# Derived from pykdebugparser/pykdebugparser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from datetime import datetime as meadow_datetime
import io as meadow_io
from pygments import highlight as meadow_highlight, lexers as meadow_lexers, formatters as meadow_formatters
from termcolor import colored as meadow_colored
from tracemeadow.stack_stream import meadow_CallstacksParser as meadow_CallstacksParser
from tracemeadow.binary_stream import meadow_KdBufParser as meadow_KdBufParser
from tracemeadow.event_records import meadow_DgbFuncQual as meadow_DgbFuncQual
from tracemeadow.code_index import meadow_default_trace_codes as meadow_default_trace_codes
from tracemeadow.trace_stream import meadow_TracesParser as meadow_TracesParser
from tracemeadow.log_records import meadow_OsLogEvent as meadow_OsLogEvent
meadow_c_lexer = meadow_lexers.CLexer()
meadow_color_formatter = meadow_formatters.TerminalTrueColorFormatter(style='stata-dark')
meadow_DBG_TRACE = 7
meadow_DBG_FSYSTEM = 3
meadow_DBG_BSD = 4

@_name_boundary.class_contract('PyKdebugParser', {'kevents': 'meadow_kevents', 'formatted_kevents': 'meadow_formatted_kevents', 'traces': 'meadow_traces', 'formatted_traces': 'meadow_formatted_traces', 'callstacks': 'meadow_callstacks', 'formatted_callstacks': 'meadow_formatted_callstacks', 'os_log_events': 'meadow_os_log_events', 'formatted_logs': 'meadow_formatted_logs', '_filter_process_callback': 'meadow__filter_process_callback', '_format_timestamp': 'meadow__format_timestamp', '_format_process': 'meadow__format_process', '_format_kevent': 'meadow__format_kevent', '_format_trace': 'meadow__format_trace', '_format_callstack': 'meadow__format_callstack', '_format_log': 'meadow__format_log', '_is_eventid_allowed': 'meadow__is_eventid_allowed', 'filter_tid': 'meadow_filter_tid', 'filter_process': 'meadow_filter_process', 'filter_class': 'meadow_filter_class', 'filter_subclass': 'meadow_filter_subclass', 'show_timestamp': 'meadow_show_timestamp', 'show_name': 'meadow_show_name', 'show_func_qual': 'meadow_show_func_qual', 'show_tid': 'meadow_show_tid', 'show_process': 'meadow_show_process', 'show_args': 'meadow_show_args', 'color': 'meadow_color', 'numer': 'meadow_numer', 'denom': 'meadow_denom', 'mach_absolute_time': 'meadow_mach_absolute_time', 'usecs_since_epoch': 'meadow_usecs_since_epoch', 'timezone': 'meadow_timezone', 'threads_pids': 'meadow_threads_pids', 'pids_names': 'meadow_pids_names', 'dyld_addresses': 'meadow_dyld_addresses', 'dyld_uuids': 'meadow_dyld_uuids'})
class meadow_PyKdebugParser:

    @_name_boundary.callable_contract({'self': 'meadow_self_c6be574'}, '__init__')
    def __init__(meadow_self_c6be574):
        _name_boundary.attributes(meadow_self_c6be574)['filter_tid'] = None
        _name_boundary.attributes(meadow_self_c6be574)['filter_process'] = None
        _name_boundary.attributes(meadow_self_c6be574)['filter_class'] = []
        _name_boundary.attributes(meadow_self_c6be574)['filter_subclass'] = []
        _name_boundary.attributes(meadow_self_c6be574)['show_timestamp'] = True
        _name_boundary.attributes(meadow_self_c6be574)['show_name'] = True
        _name_boundary.attributes(meadow_self_c6be574)['show_func_qual'] = True
        _name_boundary.attributes(meadow_self_c6be574)['show_tid'] = False
        _name_boundary.attributes(meadow_self_c6be574)['show_process'] = True
        _name_boundary.attributes(meadow_self_c6be574)['show_args'] = True
        _name_boundary.attributes(meadow_self_c6be574)['color'] = True
        _name_boundary.attributes(meadow_self_c6be574)['numer'] = None
        _name_boundary.attributes(meadow_self_c6be574)['denom'] = None
        _name_boundary.attributes(meadow_self_c6be574)['mach_absolute_time'] = None
        _name_boundary.attributes(meadow_self_c6be574)['usecs_since_epoch'] = None
        _name_boundary.attributes(meadow_self_c6be574)['timezone'] = None
        _name_boundary.attributes(meadow_self_c6be574)['threads_pids'] = {}
        _name_boundary.attributes(meadow_self_c6be574)['pids_names'] = {}
        _name_boundary.attributes(meadow_self_c6be574)['dyld_addresses'] = []
        _name_boundary.attributes(meadow_self_c6be574)['dyld_uuids'] = []

    @_name_boundary.callable_contract({'self': 'meadow_self_79130e4', 'kdebug': 'meadow_kdebug_8b9e275'}, 'kevents')
    def meadow_kevents(meadow_self_79130e4, meadow_kdebug_8b9e275: meadow_io.IOBase):
        meadow_events_generator_635d4b8 = _name_boundary.attributes(meadow_KdBufParser(_name_boundary.attributes(meadow_self_79130e4)['threads_pids'], _name_boundary.attributes(meadow_self_79130e4)['pids_names']))['parse'](meadow_kdebug_8b9e275)
        meadow_events_generator_635d4b8 = filter(lambda meadow_e_38680e2: not isinstance(meadow_e_38680e2, meadow_OsLogEvent), meadow_events_generator_635d4b8)
        if _name_boundary.attributes(meadow_self_79130e4)['filter_tid'] is not None:
            meadow_events_generator_635d4b8 = filter(lambda meadow_e_5192565: meadow_e_5192565.tid == _name_boundary.attributes(meadow_self_79130e4)['filter_tid'], meadow_events_generator_635d4b8)
        if _name_boundary.attributes(meadow_self_79130e4)['filter_class'] or _name_boundary.attributes(meadow_self_79130e4)['filter_subclass']:
            meadow_events_generator_635d4b8 = filter(lambda meadow_e_11a6c23: _name_boundary.attributes(meadow_self_79130e4)['_is_eventid_allowed'](meadow_e_11a6c23.eventid), meadow_events_generator_635d4b8)
        return meadow_events_generator_635d4b8

    @_name_boundary.callable_contract({'self': 'meadow_self_f7629d1', 'kdebug': 'meadow_kdebug_1f5984a', 'trace_codes': 'meadow_trace_codes_5380519'}, 'formatted_kevents')
    def meadow_formatted_kevents(meadow_self_f7629d1, meadow_kdebug_1f5984a: meadow_io.IOBase, meadow_trace_codes_5380519=None):
        meadow_trace_codes_map_43a67bf = meadow_default_trace_codes() if meadow_trace_codes_5380519 is None else meadow_trace_codes_5380519
        return map(lambda meadow_e_e90ea2f: _name_boundary.attributes(meadow_self_f7629d1)['_format_kevent'](meadow_e_e90ea2f, meadow_trace_codes_map_43a67bf), _name_boundary.attributes(meadow_self_f7629d1)['kevents'](meadow_kdebug_1f5984a))

    @_name_boundary.callable_contract({'self': 'meadow_self_76ddb40', 'kdebug': 'meadow_kdebug_2e37c24', 'trace_codes': 'meadow_trace_codes_b1b23af'}, 'traces')
    def meadow_traces(meadow_self_76ddb40, meadow_kdebug_2e37c24: meadow_io.IOBase, meadow_trace_codes_b1b23af=None):
        meadow_trace_codes_map_a80c653 = meadow_default_trace_codes() if meadow_trace_codes_b1b23af is None else meadow_trace_codes_b1b23af
        meadow_has_filters_da7dd72 = _name_boundary.attributes(meadow_self_76ddb40)['filter_class'] or _name_boundary.attributes(meadow_self_76ddb40)['filter_subclass']
        meadow_add_trace_class_50271b4 = meadow_has_filters_da7dd72 and meadow_DBG_TRACE not in _name_boundary.attributes(meadow_self_76ddb40)['filter_class']
        if meadow_add_trace_class_50271b4:
            _name_boundary.attributes(meadow_self_76ddb40)['filter_class'].append(meadow_DBG_TRACE)
        meadow_has_bsd_d3cc675 = meadow_DBG_BSD in _name_boundary.attributes(meadow_self_76ddb40)['filter_class'] or any(filter(lambda meadow_sc_b4dc4c7: meadow_sc_b4dc4c7 >> 8 == meadow_DBG_BSD, _name_boundary.attributes(meadow_self_76ddb40)['filter_subclass']))
        meadow_add_fs_class_faaa282 = meadow_has_filters_da7dd72 and meadow_has_bsd_d3cc675 and (meadow_DBG_FSYSTEM not in _name_boundary.attributes(meadow_self_76ddb40)['filter_class'])
        if meadow_add_fs_class_faaa282:
            _name_boundary.attributes(meadow_self_76ddb40)['filter_class'].append(meadow_DBG_FSYSTEM)
        meadow_traces_parser_3e13aa9 = meadow_TracesParser(meadow_trace_codes_map_a80c653, _name_boundary.attributes(meadow_self_76ddb40)['threads_pids'], _name_boundary.attributes(meadow_self_76ddb40)['pids_names'])
        meadow_trace_generator_a7bd299 = _name_boundary.attributes(meadow_traces_parser_3e13aa9)['feed_generator'](_name_boundary.attributes(meadow_self_76ddb40)['kevents'](meadow_kdebug_2e37c24))
        if _name_boundary.attributes(meadow_self_76ddb40)['filter_process'] is not None:
            meadow_trace_generator_a7bd299 = filter(_name_boundary.attributes(meadow_self_76ddb40)['_filter_process_callback'], meadow_trace_generator_a7bd299)
        if meadow_add_trace_class_50271b4:
            meadow_trace_generator_a7bd299 = filter(lambda meadow_t_36d90c2: meadow_t_36d90c2.ktraces[0].eventid >> 24 != meadow_DBG_TRACE, meadow_trace_generator_a7bd299)
        if meadow_add_fs_class_faaa282:
            meadow_trace_generator_a7bd299 = filter(lambda meadow_t_e06025d: meadow_t_e06025d.ktraces[0].eventid >> 24 != meadow_DBG_FSYSTEM, meadow_trace_generator_a7bd299)
        return meadow_trace_generator_a7bd299

    @_name_boundary.callable_contract({'self': 'meadow_self_7169fa0', 'kdebug': 'meadow_kdebug_04b273f', 'trace_codes': 'meadow_trace_codes_b013b38'}, 'formatted_traces')
    def meadow_formatted_traces(meadow_self_7169fa0, meadow_kdebug_04b273f: meadow_io.IOBase, meadow_trace_codes_b013b38=None):
        return map(lambda meadow_t_fe26bbe: _name_boundary.attributes(meadow_self_7169fa0)['_format_trace'](meadow_t_fe26bbe), _name_boundary.attributes(meadow_self_7169fa0)['traces'](meadow_kdebug_04b273f, meadow_trace_codes_b013b38))

    @_name_boundary.callable_contract({'self': 'meadow_self_207667c', 'kdebug': 'meadow_kdebug_ab6470d', 'trace_codes': 'meadow_trace_codes_3dc0c35'}, 'callstacks')
    def meadow_callstacks(meadow_self_207667c, meadow_kdebug_ab6470d: meadow_io.IOBase, meadow_trace_codes_3dc0c35=None):
        meadow_callstacks_parser_a3ffd28 = meadow_CallstacksParser(_name_boundary.attributes(meadow_self_207667c)['dyld_addresses'], _name_boundary.attributes(meadow_self_207667c)['dyld_uuids'])
        return _name_boundary.attributes(meadow_callstacks_parser_a3ffd28)['feed_generator'](_name_boundary.attributes(meadow_self_207667c)['traces'](meadow_kdebug_ab6470d, meadow_trace_codes_3dc0c35))

    @_name_boundary.callable_contract({'self': 'meadow_self_4aa282f', 'kdebug': 'meadow_kdebug_ce2e1df', 'trace_codes': 'meadow_trace_codes_bc8bb44'}, 'formatted_callstacks')
    def meadow_formatted_callstacks(meadow_self_4aa282f, meadow_kdebug_ce2e1df: meadow_io.IOBase, meadow_trace_codes_bc8bb44=None):
        return map(lambda meadow_t_a18d2e9: _name_boundary.attributes(meadow_self_4aa282f)['_format_callstack'](meadow_t_a18d2e9), _name_boundary.attributes(meadow_self_4aa282f)['callstacks'](meadow_kdebug_ce2e1df, meadow_trace_codes_bc8bb44))

    @_name_boundary.callable_contract({'self': 'meadow_self_43697e1', 'kdebug': 'meadow_kdebug_2442e28'}, 'os_log_events')
    def meadow_os_log_events(meadow_self_43697e1, meadow_kdebug_2442e28: meadow_io.IOBase):
        meadow_events_generator_0c80764 = _name_boundary.attributes(meadow_KdBufParser(_name_boundary.attributes(meadow_self_43697e1)['threads_pids'], _name_boundary.attributes(meadow_self_43697e1)['pids_names']))['parse'](meadow_kdebug_2442e28)
        meadow_events_generator_0c80764 = filter(lambda meadow_e_9008c46: isinstance(meadow_e_9008c46, meadow_OsLogEvent), meadow_events_generator_0c80764)
        if _name_boundary.attributes(meadow_self_43697e1)['filter_tid'] is not None:
            meadow_events_generator_0c80764 = filter(lambda meadow_e_ab65148: meadow_e_ab65148.thread_identifier == _name_boundary.attributes(meadow_self_43697e1)['filter_tid'], meadow_events_generator_0c80764)
        if _name_boundary.attributes(meadow_self_43697e1)['filter_process'] is not None:
            meadow_events_generator_0c80764 = filter(lambda meadow_e_f90070d: _name_boundary.attributes(meadow_self_43697e1)['filter_process'] in (meadow_e_f90070d.process, str(meadow_e_f90070d.process_identifier)), meadow_events_generator_0c80764)
        return meadow_events_generator_0c80764

    @_name_boundary.callable_contract({'self': 'meadow_self_68237b2', 'kdebug': 'meadow_kdebug_8266d64'}, 'formatted_logs')
    def meadow_formatted_logs(meadow_self_68237b2, meadow_kdebug_8266d64: meadow_io.IOBase):
        return map(lambda meadow_t_458c5f5: _name_boundary.attributes(meadow_self_68237b2)['_format_log'](meadow_t_458c5f5), _name_boundary.attributes(meadow_self_68237b2)['os_log_events'](meadow_kdebug_8266d64))

    @_name_boundary.callable_contract({'self': 'meadow_self_10ac099', 'trace': 'meadow_trace_5e01a7b'}, '_filter_process_callback')
    def meadow__filter_process_callback(meadow_self_10ac099, meadow_trace_5e01a7b):
        meadow_tid_8c62f43 = meadow_trace_5e01a7b.ktraces[0].tid
        meadow_pid_37eaf02 = _name_boundary.attributes(meadow_self_10ac099)['threads_pids'].get(meadow_tid_8c62f43, -1)
        meadow_process_name_b795a9f = _name_boundary.attributes(meadow_self_10ac099)['pids_names'].get(meadow_pid_37eaf02, '')
        return _name_boundary.attributes(meadow_self_10ac099)['filter_process'] == str(meadow_pid_37eaf02) or _name_boundary.attributes(meadow_self_10ac099)['filter_process'] == meadow_process_name_b795a9f

    @_name_boundary.callable_contract({'self': 'meadow_self_c04af90', 'timestamp': 'meadow_timestamp_50c5a0b'}, '_format_timestamp')
    def meadow__format_timestamp(meadow_self_c04af90, meadow_timestamp_50c5a0b):
        if None in (_name_boundary.attributes(meadow_self_c04af90)['mach_absolute_time'], _name_boundary.attributes(meadow_self_c04af90)['numer'], _name_boundary.attributes(meadow_self_c04af90)['denom'], _name_boundary.attributes(meadow_self_c04af90)['usecs_since_epoch'], _name_boundary.attributes(meadow_self_c04af90)['timezone']):
            return str(meadow_timestamp_50c5a0b) + ' '
        meadow_offset_usec_68809a2 = (meadow_timestamp_50c5a0b - _name_boundary.attributes(meadow_self_c04af90)['mach_absolute_time']) * _name_boundary.attributes(meadow_self_c04af90)['numer'] / (_name_boundary.attributes(meadow_self_c04af90)['denom'] * 1000)
        meadow_ts_1570968 = meadow_datetime.fromtimestamp((_name_boundary.attributes(meadow_self_c04af90)['usecs_since_epoch'] + meadow_offset_usec_68809a2) / 1000000, tz=_name_boundary.attributes(meadow_self_c04af90)['timezone'])
        meadow_time_string_cc5b429 = meadow_ts_1570968.strftime('%Y-%m-%d %H:%M:%S.%f')
        return f'{meadow_time_string_cc5b429:<27}'

    @_name_boundary.callable_contract({'self': 'meadow_self_269e6bd', 'tid': 'meadow_tid_3b6660d'}, '_format_process')
    def meadow__format_process(meadow_self_269e6bd, meadow_tid_3b6660d):
        meadow_pid_1ffa04c = _name_boundary.attributes(meadow_self_269e6bd)['threads_pids'].get(meadow_tid_3b6660d, -1)
        meadow_process_name_18a8f4b = _name_boundary.attributes(meadow_self_269e6bd)['pids_names'].get(meadow_pid_1ffa04c, '')
        return f'{meadow_process_name_18a8f4b}({meadow_pid_1ffa04c})' if meadow_pid_1ffa04c != -1 else f'Error: tid {meadow_tid_3b6660d}'

    @_name_boundary.callable_contract({'self': 'meadow_self_182b5e6', 'event': 'meadow_event_b36a905', 'trace_codes_map': 'meadow_trace_codes_map_67f1718'}, '_format_kevent')
    def meadow__format_kevent(meadow_self_182b5e6, meadow_event_b36a905, meadow_trace_codes_map_67f1718):
        meadow_tid_01788d9 = meadow_event_b36a905.tid
        if meadow_event_b36a905.eventid in meadow_trace_codes_map_67f1718:
            meadow_name_2c6254d = meadow_trace_codes_map_67f1718[meadow_event_b36a905.eventid] + f' ({hex(meadow_event_b36a905.eventid)})'
        else:
            meadow_name_2c6254d = hex(meadow_event_b36a905.eventid)
        meadow_formatted_data_3c5596f = ''
        if _name_boundary.attributes(meadow_self_182b5e6)['show_timestamp']:
            meadow_formatted_data_3c5596f += _name_boundary.attributes(meadow_self_182b5e6)['_format_timestamp'](meadow_event_b36a905.timestamp)
        meadow_formatted_data_3c5596f += f'{meadow_name_2c6254d:<58}' if _name_boundary.attributes(meadow_self_182b5e6)['show_name'] else ''
        if _name_boundary.attributes(meadow_self_182b5e6)['show_func_qual']:
            try:
                meadow_formatted_data_3c5596f += f"{_name_boundary.attributes(meadow_DgbFuncQual(meadow_event_b36a905.func_qualifier))['name']:<15}"
            except ValueError:
                meadow_formatted_data_3c5596f += f"{'Error':<16}"
        meadow_formatted_data_3c5596f += f'{hex(meadow_tid_01788d9):<12}' if _name_boundary.attributes(meadow_self_182b5e6)['show_tid'] else ''
        if _name_boundary.attributes(meadow_self_182b5e6)['show_process']:
            meadow_formatted_data_3c5596f += f"{_name_boundary.attributes(meadow_self_182b5e6)['_format_process'](meadow_tid_01788d9):<27}"
        meadow_formatted_data_3c5596f += f'{str(meadow_event_b36a905.data):<34}' if _name_boundary.attributes(meadow_self_182b5e6)['show_args'] else ''
        return meadow_formatted_data_3c5596f

    @_name_boundary.callable_contract({'self': 'meadow_self_9e0614c', 'trace': 'meadow_trace_0765ef1'}, '_format_trace')
    def meadow__format_trace(meadow_self_9e0614c, meadow_trace_0765ef1):
        meadow_tid_0ca4836 = meadow_trace_0765ef1.ktraces[0].tid
        meadow_formatted_data_ab0e902 = ''
        if _name_boundary.attributes(meadow_self_9e0614c)['show_timestamp']:
            meadow_formatted_data_ab0e902 += _name_boundary.attributes(meadow_self_9e0614c)['_format_timestamp'](meadow_trace_0765ef1.ktraces[0].timestamp)
        meadow_formatted_data_ab0e902 += f'{meadow_tid_0ca4836:>11} ' if _name_boundary.attributes(meadow_self_9e0614c)['show_tid'] else ''
        if _name_boundary.attributes(meadow_self_9e0614c)['show_process']:
            meadow_formatted_data_ab0e902 += f"{_name_boundary.attributes(meadow_self_9e0614c)['_format_process'](meadow_tid_0ca4836):<34}"
        meadow_event_rep_2e1ddf5 = str(meadow_trace_0765ef1)
        if _name_boundary.attributes(meadow_self_9e0614c)['color']:
            meadow_event_rep_2e1ddf5 = meadow_highlight(meadow_event_rep_2e1ddf5, meadow_c_lexer, meadow_color_formatter).strip()
        return meadow_formatted_data_ab0e902 + meadow_event_rep_2e1ddf5

    @_name_boundary.callable_contract({'self': 'meadow_self_65958cd', 'callstack': 'meadow_callstack_d7b87a5'}, '_format_callstack')
    def meadow__format_callstack(meadow_self_65958cd, meadow_callstack_d7b87a5):
        meadow_tid_e996b7f = meadow_callstack_d7b87a5.tid
        meadow_formatted_data_15b9664 = ''
        if _name_boundary.attributes(meadow_self_65958cd)['show_timestamp']:
            meadow_formatted_data_15b9664 += _name_boundary.attributes(meadow_self_65958cd)['_format_timestamp'](meadow_callstack_d7b87a5.timestamp)
        meadow_formatted_data_15b9664 += f'{meadow_tid_e996b7f:>11} ' if _name_boundary.attributes(meadow_self_65958cd)['show_tid'] else ''
        if _name_boundary.attributes(meadow_self_65958cd)['show_process']:
            meadow_formatted_data_15b9664 += f"{_name_boundary.attributes(meadow_self_65958cd)['_format_process'](meadow_tid_e996b7f):<34}"
        meadow_ret_380af6a = [meadow_formatted_data_15b9664]
        for meadow_i_b17031f, meadow_frame_4ae1a04 in enumerate(meadow_callstack_d7b87a5.frames):
            meadow_line_7aaef71 = f'{meadow_frame_4ae1a04.uuid}:0x{meadow_frame_4ae1a04.offset:016x}' if meadow_frame_4ae1a04.uuid is not None else f'0x{meadow_frame_4ae1a04.address:016x}'
            meadow_ret_380af6a.append(' ' * meadow_i_b17031f + meadow_line_7aaef71)
        return '\n'.join(meadow_ret_380af6a)

    @_name_boundary.callable_contract({'self': 'meadow_self_1138950', 'os_log': 'meadow_os_log_195985d'}, '_format_log')
    def meadow__format_log(meadow_self_1138950, meadow_os_log_195985d: meadow_OsLogEvent):
        meadow_time_string_f845dca = meadow_os_log_195985d.unix_date.strftime('%Y-%m-%d %H:%M:%S.%f')
        meadow_timestamp_4c9169b = f'{meadow_time_string_f845dca:<27}'
        meadow_event_rep_a23a533 = meadow_colored(str(meadow_timestamp_4c9169b), 'green') if _name_boundary.attributes(meadow_self_1138950)['color'] else str(meadow_timestamp_4c9169b)
        if meadow_os_log_195985d.process:
            meadow_process_1ec5c59 = _name_boundary.attributes(meadow_self_1138950)['_format_process'](meadow_os_log_195985d.thread_identifier)
            meadow_process_1ec5c59 = meadow_colored(meadow_process_1ec5c59, 'magenta') if _name_boundary.attributes(meadow_self_1138950)['color'] else meadow_process_1ec5c59
            meadow_event_rep_a23a533 += f' {meadow_process_1ec5c59:<27} '
        meadow_event_rep_a23a533 += meadow_colored(meadow_os_log_195985d.composed_message, 'white') if _name_boundary.attributes(meadow_self_1138950)['color'] else meadow_os_log_195985d.composed_message
        return meadow_event_rep_a23a533

    @_name_boundary.callable_contract({'self': 'meadow_self_b1f8922', 'event_id': 'meadow_event_id_ef02ec9'}, '_is_eventid_allowed')
    def meadow__is_eventid_allowed(meadow_self_b1f8922, meadow_event_id_ef02ec9):
        return meadow_event_id_ef02ec9 >> 24 in _name_boundary.attributes(meadow_self_b1f8922)['filter_class'] or meadow_event_id_ef02ec9 >> 16 in _name_boundary.attributes(meadow_self_b1f8922)['filter_subclass']
_name_boundary.module_contract(globals(), {'CallstacksParser': 'meadow_CallstacksParser', 'colored': 'meadow_colored', 'default_trace_codes': 'meadow_default_trace_codes', 'TracesParser': 'meadow_TracesParser', 'OsLogEvent': 'meadow_OsLogEvent', 'io': 'meadow_io', 'DBG_BSD': 'meadow_DBG_BSD', 'highlight': 'meadow_highlight', 'DBG_TRACE': 'meadow_DBG_TRACE', 'DBG_FSYSTEM': 'meadow_DBG_FSYSTEM', 'KdBufParser': 'meadow_KdBufParser', 'c_lexer': 'meadow_c_lexer', 'DgbFuncQual': 'meadow_DgbFuncQual', 'PyKdebugParser': 'meadow_PyKdebugParser', 'formatters': 'meadow_formatters', 'lexers': 'meadow_lexers', 'datetime': 'meadow_datetime', 'color_formatter': 'meadow_color_formatter'})
