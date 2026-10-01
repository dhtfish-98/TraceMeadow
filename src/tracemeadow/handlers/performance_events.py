# Derived from pykdebugparser/trace_handlers/perf.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass
from enum import Enum as meadow_Enum
from itertools import chain as meadow_chain
from typing import List as meadow_List, Any as meadow_Any

@_name_boundary.class_contract('SamplerAction', {})
class meadow_SamplerAction(meadow_Enum):
    SAMPLER_TH_INFO = 1
    SAMPLER_TH_SNAPSHOT = 2
    SAMPLER_KSTACK = 4
    SAMPLER_USTACK = 8
    SAMPLER_PMC_THREAD = 16
    SAMPLER_PMC_CPU = 32
    SAMPLER_PMC_CONFIG = 64
    SAMPLER_MEMINFO = 128
    SAMPLER_TH_SCHEDULING = 256
    SAMPLER_TH_DISPATCH = 512
    SAMPLER_TK_SNAPSHOT = 1024
    SAMPLER_SYS_MEM = 2048
    SAMPLER_TH_INSCYC = 4096
    SAMPLER_TK_INFO = 8192

@_name_boundary.callable_contract({'flags': 'meadow_flags_79725ac'}, 'to_sampler_action')
def meadow_to_sampler_action(meadow_flags_79725ac: int):
    return [meadow_s_3f75a8c for meadow_s_3f75a8c in meadow_SamplerAction if meadow_s_3f75a8c.value & meadow_flags_79725ac]

@_name_boundary.class_contract('KperfTiState', {})
class meadow_KperfTiState(meadow_Enum):
    KPERF_TI_RUNNING = 1
    KPERF_TI_RUNNABLE = 2
    KPERF_TI_WAIT = 4
    KPERF_TI_UNINT = 8
    KPERF_TI_SUSP = 16
    KPERF_TI_TERMINATE = 32
    KPERF_TI_IDLE = 64

@_name_boundary.callable_contract({'flags': 'meadow_flags_569abf6'}, 'to_kperf_ti_state')
def meadow_to_kperf_ti_state(meadow_flags_569abf6: int):
    return [meadow_s_96b341c for meadow_s_96b341c in meadow_KperfTiState if meadow_s_96b341c.value & meadow_flags_569abf6]

@_name_boundary.class_contract('CallstackFlag', {})
class meadow_CallstackFlag(meadow_Enum):
    CALLSTACK_VALID = 1
    CALLSTACK_DEFERRED = 2
    CALLSTACK_64BIT = 4
    CALLSTACK_KERNEL = 8
    CALLSTACK_TRUNCATED = 16
    CALLSTACK_CONTINUATION = 32
    CALLSTACK_KERNEL_WORDS = 64
    CALLSTACK_TRANSLATED = 128
    CALLSTACK_FIXUP_PC = 256

@_name_boundary.callable_contract({'flags': 'meadow_flags_a4d64b2'}, 'to_callstack_flags')
def meadow_to_callstack_flags(meadow_flags_a4d64b2: int):
    return [meadow_c_582015f for meadow_c_582015f in meadow_CallstackFlag if meadow_c_582015f.value & meadow_flags_a4d64b2]

@_name_boundary.class_contract('PerfEvent', {})
@meadow_dataclass
class meadow_PerfEvent:
    ktraces: meadow_List
    sample_what: meadow_List
    actionid: int
    th_info: meadow_Any = None
    cs_flags: meadow_List = None
    cs_frames: meadow_List = None

    @_name_boundary.callable_contract({'self': 'meadow_self_2ead68e'}, '__str__')
    def __str__(meadow_self_2ead68e):
        meadow_sample_what_2031646 = ' | '.join(map(lambda meadow_s_a53417b: _name_boundary.attributes(meadow_s_a53417b)['name'], meadow_self_2ead68e.sample_what))
        meadow_rep_fcfd258 = f'PERF_Event, sample_what: {meadow_sample_what_2031646}, actionid: {meadow_self_2ead68e.actionid}'
        if meadow_self_2ead68e.cs_frames is not None:
            meadow_rep_fcfd258 += f', frames count: {len(meadow_self_2ead68e.cs_frames)}'
        return meadow_rep_fcfd258

@_name_boundary.class_contract('PerfThdData', {})
@meadow_dataclass
class meadow_PerfThdData:
    """
    According to kperf_thread_info_sample, osfmk/kperf/thread_samplers.c
    """
    ktraces: meadow_List
    pid: int
    tid: int
    dq_addr: int
    runmode: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_b35cbb2'}, '__str__')
    def __str__(meadow_self_b35cbb2):
        meadow_runmode_9ebf019 = ' | '.join(map(lambda meadow_r_85d1802: _name_boundary.attributes(meadow_r_85d1802)['name'], meadow_self_b35cbb2.runmode))
        return f'PERF_THD_Data, pid: {meadow_self_b35cbb2.pid}, tid: {meadow_self_b35cbb2.tid}, dq_addr: {hex(meadow_self_b35cbb2.dq_addr)}, runmode: {meadow_runmode_9ebf019}'

@_name_boundary.class_contract('PerfThdCswitch', {})
@meadow_dataclass
class meadow_PerfThdCswitch:
    """
    According to kperf_on_cpu_internal, osfmk/kperf/kperf.c
    """
    ktraces: meadow_List
    tid: int
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_e3d1d60'}, '__str__')
    def __str__(meadow_self_e3d1d60):
        return f'PERF_THD_CSwitch, tid: {meadow_self_e3d1d60.tid}, pid: {meadow_self_e3d1d60.pid}'

@_name_boundary.class_contract('PerfStkUdata', {})
@meadow_dataclass
class meadow_PerfStkUdata:
    """
    According to callstack_log, osfmk/kperf/callstack.c
    """
    ktraces: meadow_List
    frames: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_99ab165'}, '__str__')
    def __str__(meadow_self_99ab165):
        meadow_frames_7e3a689 = ', '.join(map(hex, meadow_self_99ab165.frames))
        return f'PERF_STK_UData, frames: [{meadow_frames_7e3a689}]'

@_name_boundary.class_contract('PerfStkUhdr', {})
@meadow_dataclass
class meadow_PerfStkUhdr:
    """
    According to callstack_log, osfmk/kperf/callstack.c
    """
    ktraces: meadow_List
    flags: meadow_List
    nframes: int

    @_name_boundary.callable_contract({'self': 'meadow_self_2124058'}, '__str__')
    def __str__(meadow_self_2124058):
        meadow_flags_6e898d7 = ' | '.join(map(lambda meadow_c_5368219: _name_boundary.attributes(meadow_c_5368219)['name'], meadow_self_2124058.flags))
        return f'PERF_STK_UHdr, flags: {meadow_flags_6e898d7}, frames count: {meadow_self_2124058.nframes}'

@_name_boundary.callable_contract({'parser': 'meadow_parser_9460581', 'events': 'meadow_events_cd24de8'}, 'handle_event')
def meadow_handle_event(meadow_parser_9460581, meadow_events_cd24de8):
    meadow_args_4d9a627 = meadow_events_cd24de8[0].values
    meadow_e_b5e371e = meadow_PerfEvent(meadow_events_cd24de8, meadow_to_sampler_action(meadow_args_4d9a627[0]), meadow_args_4d9a627[1])
    if meadow_SamplerAction.SAMPLER_TH_INFO in meadow_e_b5e371e.sample_what:
        meadow_sub_events_60f8383 = [meadow_ev_e99bae9 for meadow_ev_e99bae9 in meadow_events_cd24de8 if _name_boundary.attributes(meadow_parser_9460581)['trace_codes'].get(meadow_ev_e99bae9.eventid, '') == 'PERF_THD_Data']
        if meadow_sub_events_60f8383:
            meadow_e_b5e371e.th_info = meadow_handle_thd_data(meadow_parser_9460581, meadow_sub_events_60f8383)
    if meadow_SamplerAction.SAMPLER_USTACK in meadow_e_b5e371e.sample_what:
        meadow_sub_events_60f8383 = [meadow_ev_f6d7b3d for meadow_ev_f6d7b3d in meadow_events_cd24de8 if _name_boundary.attributes(meadow_parser_9460581)['trace_codes'].get(meadow_ev_f6d7b3d.eventid, '') == 'PERF_STK_UHdr']
        if meadow_sub_events_60f8383:
            meadow_header_df7a0f6 = meadow_handle_stk_uhdr(meadow_parser_9460581, meadow_sub_events_60f8383)
            meadow_stk_data_ff82d90 = [meadow_handle_stk_udata(meadow_parser_9460581, [meadow_ev_f58fd7b]).frames for meadow_ev_f58fd7b in meadow_events_cd24de8 if _name_boundary.attributes(meadow_parser_9460581)['trace_codes'].get(meadow_ev_f58fd7b.eventid, '') == 'PERF_STK_UData']
            meadow_e_b5e371e.cs_frames = list(meadow_chain.from_iterable(meadow_stk_data_ff82d90))[:meadow_header_df7a0f6.nframes]
            meadow_e_b5e371e.cs_flags = meadow_header_df7a0f6.flags
    return meadow_e_b5e371e

@_name_boundary.callable_contract({'parser': 'meadow_parser_3a3c4d5', 'events': 'meadow_events_15c9b83'}, 'handle_thd_data')
def meadow_handle_thd_data(meadow_parser_3a3c4d5, meadow_events_15c9b83):
    meadow_args_9ca235f = meadow_events_15c9b83[0].values
    meadow_pid_414a794 = meadow_args_9ca235f[0]
    meadow_tid_2c6e33b = meadow_args_9ca235f[1]
    _name_boundary.attributes(meadow_parser_3a3c4d5)['threads_pids'][meadow_tid_2c6e33b] = meadow_pid_414a794
    return meadow_PerfThdData(meadow_events_15c9b83, meadow_pid_414a794, meadow_tid_2c6e33b, meadow_args_9ca235f[2], meadow_to_kperf_ti_state(meadow_args_9ca235f[3] & 65535))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f5dceeb', 'events': 'meadow_events_0cd52fa'}, 'handle_thd_cswitch')
def meadow_handle_thd_cswitch(meadow_parser_f5dceeb, meadow_events_0cd52fa):
    meadow_args_f56fccc = meadow_events_0cd52fa[0].values
    return meadow_PerfThdCswitch(meadow_events_0cd52fa, meadow_args_f56fccc[0], meadow_args_f56fccc[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_9ae831d', 'events': 'meadow_events_6c7b60e'}, 'handle_stk_udata')
def meadow_handle_stk_udata(meadow_parser_9ae831d, meadow_events_6c7b60e):
    return meadow_PerfStkUdata(meadow_events_6c7b60e, list(meadow_events_6c7b60e[0].values))

@_name_boundary.callable_contract({'parser': 'meadow_parser_645976a', 'events': 'meadow_events_9d99ae9'}, 'handle_stk_uhdr')
def meadow_handle_stk_uhdr(meadow_parser_645976a, meadow_events_9d99ae9):
    meadow_args_a98328a = meadow_events_9d99ae9[0].values
    return meadow_PerfStkUhdr(meadow_events_9d99ae9, meadow_to_callstack_flags(meadow_args_a98328a[0]), meadow_args_a98328a[1])
meadow_handlers = {'PERF_Event': meadow_handle_event, 'PERF_THD_Data': meadow_handle_thd_data, 'PERF_THD_CSwitch': meadow_handle_thd_cswitch, 'PERF_STK_UData': meadow_handle_stk_udata, 'PERF_STK_UHdr': meadow_handle_stk_uhdr}
_name_boundary.module_contract(globals(), {'PerfThdData': 'meadow_PerfThdData', 'chain': 'meadow_chain', 'handle_event': 'meadow_handle_event', 'KperfTiState': 'meadow_KperfTiState', 'handlers': 'meadow_handlers', 'dataclass': 'meadow_dataclass', 'PerfStkUhdr': 'meadow_PerfStkUhdr', 'handle_thd_data': 'meadow_handle_thd_data', 'PerfThdCswitch': 'meadow_PerfThdCswitch', 'CallstackFlag': 'meadow_CallstackFlag', 'Any': 'meadow_Any', 'handle_stk_udata': 'meadow_handle_stk_udata', 'to_sampler_action': 'meadow_to_sampler_action', 'SamplerAction': 'meadow_SamplerAction', 'to_kperf_ti_state': 'meadow_to_kperf_ti_state', 'Enum': 'meadow_Enum', 'to_callstack_flags': 'meadow_to_callstack_flags', 'List': 'meadow_List', 'handle_stk_uhdr': 'meadow_handle_stk_uhdr', 'PerfStkUdata': 'meadow_PerfStkUdata', 'handle_thd_cswitch': 'meadow_handle_thd_cswitch', 'PerfEvent': 'meadow_PerfEvent'})
