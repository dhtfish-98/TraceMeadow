# Derived from pykdebugparser/traces_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from collections import namedtuple as meadow_namedtuple
from tracemeadow.event_records import meadow_DgbFuncQual as meadow_DgbFuncQual
from tracemeadow.handlers.unix_calls import meadow_handlers as meadow_bsd_handlers
from tracemeadow.handlers.image_events import meadow_handlers as meadow_dyld_handlers
from tracemeadow.handlers.file_events import meadow_handlers as meadow_fsystem_handlers
from tracemeadow.handlers.kernel_calls import meadow_handlers as meadow_mach_handlers
from tracemeadow.handlers.performance_events import meadow_handlers as meadow_perf_handlers
from tracemeadow.handlers.lifecycle_events import meadow_handlers as meadow_trace_handlers
from tracemeadow.handlers.priority_events import meadow_handlers as meadow_turnstile_handlers
meadow_Vnode = _name_boundary.named_record('Vnode', ['ktraces', 'vnode_id', 'path'])

@_name_boundary.class_contract('TracesParser', {'feed': 'meadow_feed', 'feed_generator': 'meadow_feed_generator', 'parse_event_list': 'meadow_parse_event_list', 'vnode_generator': 'meadow_vnode_generator', 'parse_vnode': 'meadow_parse_vnode', 'parse_vnodes': 'meadow_parse_vnodes', '_feed_start_event': 'meadow__feed_start_event', '_feed_end_event': 'meadow__feed_end_event', '_feed_single_event': 'meadow__feed_single_event', 'trace_codes': 'meadow_trace_codes', 'on_going_events': 'meadow_on_going_events', 'on_going_traces': 'meadow_on_going_traces', 'global_strings': 'meadow_global_strings', 'threads_pids': 'meadow_threads_pids', 'pids_names': 'meadow_pids_names', 'tids_names': 'meadow_tids_names', 'qualifiers_actions': 'meadow_qualifiers_actions', 'last_data_newthread': 'meadow_last_data_newthread', 'last_data_exec': 'meadow_last_data_exec', 'handlers': 'meadow_handlers'})
class meadow_TracesParser:

    @_name_boundary.callable_contract({'self': 'meadow_self_59c1697', 'trace_codes_map': 'meadow_trace_codes_map_8c4fdb1', 'threads_pids': 'meadow_threads_pids_2f170eb', 'pids_names': 'meadow_pids_names_36e8abb'}, '__init__')
    def __init__(meadow_self_59c1697, meadow_trace_codes_map_8c4fdb1, meadow_threads_pids_2f170eb, meadow_pids_names_36e8abb):
        _name_boundary.attributes(meadow_self_59c1697)['trace_codes'] = meadow_trace_codes_map_8c4fdb1
        _name_boundary.attributes(meadow_self_59c1697)['on_going_events'] = {}
        _name_boundary.attributes(meadow_self_59c1697)['on_going_traces'] = {}
        _name_boundary.attributes(meadow_self_59c1697)['global_strings'] = {}
        _name_boundary.attributes(meadow_self_59c1697)['threads_pids'] = meadow_threads_pids_2f170eb
        _name_boundary.attributes(meadow_self_59c1697)['pids_names'] = meadow_pids_names_36e8abb
        _name_boundary.attributes(meadow_self_59c1697)['tids_names'] = {}
        _name_boundary.attributes(meadow_self_59c1697)['qualifiers_actions'] = {meadow_DgbFuncQual.DBG_FUNC_START.value: _name_boundary.attributes(meadow_self_59c1697)['_feed_start_event'], meadow_DgbFuncQual.DBG_FUNC_END.value: _name_boundary.attributes(meadow_self_59c1697)['_feed_end_event'], meadow_DgbFuncQual.DBG_FUNC_ALL.value: _name_boundary.attributes(meadow_self_59c1697)['_feed_single_event'], meadow_DgbFuncQual.DBG_FUNC_NONE.value: _name_boundary.attributes(meadow_self_59c1697)['_feed_single_event']}
        _name_boundary.attributes(meadow_self_59c1697)['last_data_newthread'] = None
        _name_boundary.attributes(meadow_self_59c1697)['last_data_exec'] = None
        _name_boundary.attributes(meadow_self_59c1697)['handlers'] = {}
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_bsd_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_dyld_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_fsystem_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_mach_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_perf_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_trace_handlers)
        _name_boundary.attributes(meadow_self_59c1697)['handlers'].update(meadow_turnstile_handlers)

    @_name_boundary.callable_contract({'self': 'meadow_self_2ba3847', 'event': 'meadow_event_2f5c2e2'}, 'feed')
    def meadow_feed(meadow_self_2ba3847, meadow_event_2f5c2e2):
        if meadow_event_2f5c2e2.eventid in _name_boundary.attributes(meadow_self_2ba3847)['trace_codes']:
            meadow_trace_name_d383d33 = _name_boundary.attributes(meadow_self_2ba3847)['trace_codes'][meadow_event_2f5c2e2.eventid]
            if meadow_trace_name_d383d33 in meadow_trace_handlers:
                return _name_boundary.attributes(meadow_self_2ba3847)['qualifiers_actions'][meadow_event_2f5c2e2.func_qualifier](meadow_event_2f5c2e2, _name_boundary.attributes(meadow_self_2ba3847)['on_going_traces'])
        return _name_boundary.attributes(meadow_self_2ba3847)['qualifiers_actions'][meadow_event_2f5c2e2.func_qualifier](meadow_event_2f5c2e2, _name_boundary.attributes(meadow_self_2ba3847)['on_going_events'])

    @_name_boundary.callable_contract({'self': 'meadow_self_0de6094', 'generator': 'meadow_generator_c1a2f51'}, 'feed_generator')
    def meadow_feed_generator(meadow_self_0de6094, meadow_generator_c1a2f51):
        for meadow_event_f67a803 in meadow_generator_c1a2f51:
            meadow_ret_8f8c708 = _name_boundary.attributes(meadow_self_0de6094)['feed'](meadow_event_f67a803)
            if meadow_ret_8f8c708 is not None:
                yield meadow_ret_8f8c708

    @_name_boundary.callable_contract({'self': 'meadow_self_ea6c165', 'events': 'meadow_events_8046657'}, 'parse_event_list')
    def meadow_parse_event_list(meadow_self_ea6c165, meadow_events_8046657):
        if meadow_events_8046657[0].eventid not in _name_boundary.attributes(meadow_self_ea6c165)['trace_codes']:
            return None
        meadow_trace_name_479c376 = _name_boundary.attributes(meadow_self_ea6c165)['trace_codes'][meadow_events_8046657[0].eventid]
        if meadow_trace_name_479c376 not in _name_boundary.attributes(meadow_self_ea6c165)['handlers']:
            return None
        return _name_boundary.attributes(meadow_self_ea6c165)['handlers'][meadow_trace_name_479c376](meadow_self_ea6c165, meadow_events_8046657)

    @staticmethod
    @_name_boundary.callable_contract({'events': 'meadow_events_c6ded3a'}, 'vnode_generator')
    def meadow_vnode_generator(meadow_events_c6ded3a):
        meadow_path_348af7c = b''
        meadow_vnodeid_1412b86 = 0
        meadow_lookup_events_d105d16 = []
        for meadow_event_5cfb079 in meadow_events_c6ded3a:
            meadow_lookup_events_d105d16.append(meadow_event_5cfb079)
            if meadow_event_5cfb079.func_qualifier & meadow_DgbFuncQual.DBG_FUNC_START.value:
                meadow_vnodeid_1412b86 = meadow_event_5cfb079.values[0]
                meadow_path_348af7c += meadow_event_5cfb079.data[8:]
            else:
                meadow_path_348af7c += meadow_event_5cfb079.data
            if meadow_event_5cfb079.func_qualifier & meadow_DgbFuncQual.DBG_FUNC_END.value:
                yield meadow_Vnode(meadow_lookup_events_d105d16, meadow_vnodeid_1412b86, meadow_path_348af7c.replace(b'\x00', b'').decode())
                meadow_path_348af7c = b''
                meadow_vnodeid_1412b86 = 0
                meadow_lookup_events_d105d16 = []

    @_name_boundary.callable_contract({'self': 'meadow_self_79e580d', 'events': 'meadow_events_05ad2cd'}, 'parse_vnode')
    def meadow_parse_vnode(meadow_self_79e580d, meadow_events_05ad2cd):
        try:
            return _name_boundary.attributes(meadow_self_79e580d)['parse_vnodes'](meadow_events_05ad2cd)[0]
        except IndexError:
            return meadow_Vnode([], 0, '')

    @_name_boundary.callable_contract({'self': 'meadow_self_4f4c825', 'events': 'meadow_events_b30b099'}, 'parse_vnodes')
    def meadow_parse_vnodes(meadow_self_4f4c825, meadow_events_b30b099):
        return list(_name_boundary.attributes(meadow_self_4f4c825)['vnode_generator']([meadow_e_813108c for meadow_e_813108c in meadow_events_b30b099 if _name_boundary.attributes(meadow_self_4f4c825)['trace_codes'].get(meadow_e_813108c.eventid) == 'VFS_LOOKUP']))

    @_name_boundary.callable_contract({'self': 'meadow_self_842dba4', 'event': 'meadow_event_b8bf5ae', 'state': 'meadow_state_3369136'}, '_feed_start_event')
    def meadow__feed_start_event(meadow_self_842dba4, meadow_event_b8bf5ae, meadow_state_3369136):
        if meadow_event_b8bf5ae.tid not in meadow_state_3369136:
            meadow_state_3369136[meadow_event_b8bf5ae.tid] = {}
        meadow_state_3369136[meadow_event_b8bf5ae.tid][meadow_event_b8bf5ae.eventid] = []
        for meadow_eventid_51666b0 in meadow_state_3369136[meadow_event_b8bf5ae.tid]:
            meadow_state_3369136[meadow_event_b8bf5ae.tid][meadow_eventid_51666b0].append(meadow_event_b8bf5ae)

    @_name_boundary.callable_contract({'self': 'meadow_self_8171a04', 'event': 'meadow_event_70898a6', 'state': 'meadow_state_f0bb72e'}, '_feed_end_event')
    def meadow__feed_end_event(meadow_self_8171a04, meadow_event_70898a6, meadow_state_f0bb72e):
        if meadow_event_70898a6.tid not in meadow_state_f0bb72e or meadow_event_70898a6.eventid not in meadow_state_f0bb72e[meadow_event_70898a6.tid]:
            return
        for meadow_eventid_9c4881f in meadow_state_f0bb72e[meadow_event_70898a6.tid]:
            meadow_state_f0bb72e[meadow_event_70898a6.tid][meadow_eventid_9c4881f].append(meadow_event_70898a6)
        meadow_events_0b9f55f = meadow_state_f0bb72e[meadow_event_70898a6.tid].pop(meadow_event_70898a6.eventid)
        return _name_boundary.attributes(meadow_self_8171a04)['parse_event_list'](meadow_events_0b9f55f)

    @_name_boundary.callable_contract({'self': 'meadow_self_1dab47b', 'event': 'meadow_event_9125a81', 'state': 'meadow_state_1e8cbfc'}, '_feed_single_event')
    def meadow__feed_single_event(meadow_self_1dab47b, meadow_event_9125a81, meadow_state_1e8cbfc):
        for meadow_eventid_50b86d8 in meadow_state_1e8cbfc.get(meadow_event_9125a81.tid, {}):
            meadow_state_1e8cbfc[meadow_event_9125a81.tid][meadow_eventid_50b86d8].append(meadow_event_9125a81)
        return _name_boundary.attributes(meadow_self_1dab47b)['parse_event_list']([meadow_event_9125a81])
_name_boundary.module_contract(globals(), {'Vnode': 'meadow_Vnode', 'bsd_handlers': 'meadow_bsd_handlers', 'TracesParser': 'meadow_TracesParser', 'fsystem_handlers': 'meadow_fsystem_handlers', 'trace_handlers': 'meadow_trace_handlers', 'perf_handlers': 'meadow_perf_handlers', 'turnstile_handlers': 'meadow_turnstile_handlers', 'dyld_handlers': 'meadow_dyld_handlers', 'DgbFuncQual': 'meadow_DgbFuncQual', 'namedtuple': 'meadow_namedtuple', 'mach_handlers': 'meadow_mach_handlers'})
