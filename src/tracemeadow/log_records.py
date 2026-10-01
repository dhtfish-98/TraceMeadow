# Derived from pykdebugparser/os_log_event.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass, field as meadow_field
from datetime import datetime as meadow_datetime, timezone as meadow_timezone
import enum as meadow_enum
from typing import List as meadow_List, Dict as meadow_Dict
from construct import Struct as meadow_Struct, Byte as meadow_Byte, Int32ul as meadow_Int32ul, BitStruct as meadow_BitStruct, Padding as meadow_Padding, Flag as meadow_Flag, BitsInteger as meadow_BitsInteger, Int64ul as meadow_Int64ul

@_name_boundary.class_contract('OsLogType', {})
class meadow_OsLogType(meadow_enum.Enum):
    DEFAULT = 0
    INFO = 1
    DEBUG = 2
    ERROR = 16
    FAULT = 17

@_name_boundary.class_contract('FirehoseTracepointNamespace', {})
class meadow_FirehoseTracepointNamespace(meadow_enum.Enum):
    unknown = 0
    activity = 2
    trace = 3
    log = 4
    metadata = 5
    signpost = 6
    loss = 7

@_name_boundary.class_contract('FirehoseTracepointFlagsPcStyle', {})
class meadow_FirehoseTracepointFlagsPcStyle(meadow_enum.Enum):
    none = 0
    main_exe = 1
    shared_cache = 2
    main_plugin = 3
    absolute = 4
    uuid_relative = 5
    large_shared_cache = 6
    _unused7 = 7

@_name_boundary.class_contract('FirehoseTracepointActivityType', {})
class meadow_FirehoseTracepointActivityType(meadow_enum.Enum):
    create = 1
    swap = 2
    useraction = 3

@_name_boundary.class_contract('FirehoseTracepointTraceType', {})
class meadow_FirehoseTracepointTraceType(meadow_enum.Enum):
    default = 0
    info = 1
    debug = 2
    error = 16
    fault = 17

@_name_boundary.class_contract('FirehoseTracepointLogType', {})
class meadow_FirehoseTracepointLogType(meadow_enum.Enum):
    default = 0
    info = 1
    debug = 2
    error = 16
    fault = 17

@_name_boundary.class_contract('FirehoseTracepointLogFlags', {})
class meadow_FirehoseTracepointLogFlags(meadow_enum.IntFlag):
    has_private_data = 1
    has_subsystem = 2
    has_rules = 4
    has_oversize = 8
    has_context_data = 16

@_name_boundary.class_contract('FirehoseTracepointMetadataType', {})
class meadow_FirehoseTracepointMetadataType(meadow_enum.Enum):
    dyld = 1
    subsystem = 2
    kext = 3
    coprocessor = 4

@_name_boundary.class_contract('FirehoseTracepointSignpostType', {})
class meadow_FirehoseTracepointSignpostType(meadow_enum.IntFlag):
    event = 0
    interval_begin = 1
    interval_end = 2
    scope_thread = 64
    scope_process = 128
    scope_system = 192

@_name_boundary.class_contract('FirehoseTracepointSingpostFlags', {})
class meadow_FirehoseTracepointSingpostFlags(meadow_enum.Enum):
    has_private_data = 1
    has_subsystem = 2
    has_rules = 4
    has_oversize = 8
    has_context_data = 16
    has_name = 128
meadow_tracepoint_types = {meadow_FirehoseTracepointNamespace.activity: meadow_FirehoseTracepointActivityType, meadow_FirehoseTracepointNamespace.trace: meadow_FirehoseTracepointTraceType, meadow_FirehoseTracepointNamespace.log: meadow_FirehoseTracepointLogType, meadow_FirehoseTracepointNamespace.metadata: meadow_FirehoseTracepointMetadataType, meadow_FirehoseTracepointNamespace.signpost: meadow_FirehoseTracepointSignpostType}
meadow_tracepoint_flags = {meadow_FirehoseTracepointNamespace.log: meadow_FirehoseTracepointLogFlags, meadow_FirehoseTracepointNamespace.trace: meadow_FirehoseTracepointSingpostFlags}
meadow_firehose_tracepoint_id = meadow_Struct('namespace' / meadow_Byte, 'type_' / meadow_Byte, 'trace_flags' / meadow_BitStruct(meadow_Padding(2), 'has_large_offset' / meadow_Flag, 'has_unique_pid' / meadow_Flag, 'pc_style' / meadow_BitsInteger(3), 'has_current_aid' / meadow_Flag), 'flags' / meadow_Byte, 'code' / meadow_Int32ul)

@_name_boundary.class_contract('TraceIdentifier', {})
@meadow_dataclass
class meadow_TraceIdentifier:
    namespace: meadow_FirehoseTracepointNamespace
    type_: meadow_enum.Enum
    has_large_offset: bool
    has_unique_pid: bool
    pc_style: meadow_FirehoseTracepointFlagsPcStyle
    has_current_aid: bool
    flags: None
    code: int

@_name_boundary.class_contract('OsLogEvent', {'from_raw_log_event': 'meadow_from_raw_log_event', 'parse_trace_identifier': 'meadow_parse_trace_identifier', 'parse_decomposed': 'meadow_parse_decomposed', 'parse_decomposed_segment': 'meadow_parse_decomposed_segment'})
@meadow_dataclass
class meadow_OsLogEvent:
    composed_message: str
    type_: str
    size: str
    thread_identifier: int
    continuous_nanoseconds_since_boot: int
    mach_continuous_timestamp: int
    boot_uuid: bytes
    process_image_uuid: bytes
    unix_date: meadow_datetime
    unix_timezone: meadow_Dict
    process_image_path: str = ''
    process: str = ''
    sender_image_path: str = ''
    sender: str = ''
    sender_image_offset: int = 0
    sender_image_uuid: bytes = b''
    log_type: meadow_OsLogType = None
    time_to_live: int = 0
    process_identifier: int = 0
    subsystem: str = ''
    category: str = ''
    format_string: str = ''
    activity_identifier: int = 0
    parent_activity_identifier: int = 0
    decomposed_message: meadow_Dict = meadow_field(default_factory=dict)
    trace_identifier: meadow_TraceIdentifier = None
    creator_activity_identifier: int = 0
    creator_process_unique_identifier: int = 0
    signpost_identifier: int = 0
    signpost_name: str = ''
    signpost_type: int = 0
    signpost_scope: int = 0
    loss_start_mach_continuous_timestamp: int = 0
    loss_end_mach_continuous_timestamp: int = 0
    loss_start_unix_date: meadow_Dict = meadow_field(default_factory=dict)
    loss_end_unix_date: meadow_Dict = meadow_field(default_factory=dict)
    loss_start_unix_timezone: meadow_Dict = meadow_field(default_factory=dict)
    loss_end_unix_timezone: meadow_Dict = meadow_field(default_factory=dict)
    loss_count: meadow_Dict = meadow_field(default_factory=dict)
    backtrace: meadow_List = meadow_field(default_factory=list)

    @classmethod
    @_name_boundary.callable_contract({'cls': 'meadow_cls_ad5fb46', 'event': 'meadow_event_b99dc03', 'log_strings': 'meadow_log_strings_1e16377'}, 'from_raw_log_event')
    def meadow_from_raw_log_event(meadow_cls_ad5fb46, meadow_event_b99dc03, meadow_log_strings_1e16377):
        meadow_parsed_event_476ca63 = {'composed_message': meadow_log_strings_1e16377[meadow_event_b99dc03.pop('cm')], 'type_': meadow_event_b99dc03.pop('t'), 'size': meadow_event_b99dc03.pop('s'), 'thread_identifier': meadow_event_b99dc03.pop('tid'), 'continuous_nanoseconds_since_boot': meadow_event_b99dc03.pop('ns'), 'mach_continuous_timestamp': meadow_event_b99dc03.pop('mct'), 'boot_uuid': meadow_event_b99dc03.pop('b'), 'process_image_uuid': meadow_event_b99dc03.pop('piu')}
        meadow_unix_date_f730263 = meadow_event_b99dc03.pop('ud')
        meadow_parsed_event_476ca63['unix_date'] = meadow_datetime.fromtimestamp(meadow_unix_date_f730263['sec'] + meadow_unix_date_f730263['usec'] / 10 ** 6, tz=meadow_timezone.utc)
        meadow_utz_781f8b9 = meadow_event_b99dc03.pop('utz')
        meadow_parsed_event_476ca63['unix_timezone'] = {'minutes_west': meadow_utz_781f8b9['mw'], 'dst_time': meadow_utz_781f8b9['dt']}
        if 'ti' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['trace_identifier'] = _name_boundary.attributes(meadow_cls_ad5fb46)['parse_trace_identifier'](meadow_event_b99dc03.pop('ti'))
        if 'pip' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['process_image_path'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('pip')]
        if 'p' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['process'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('p')]
        if 'sip' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['sender_image_path'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('sip')]
        if 'send' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['sender'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('send')]
        if 'sio' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['sender_image_offset'] = meadow_event_b99dc03.pop('sio')
        if 'siu' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['sender_image_uuid'] = meadow_event_b99dc03.pop('siu')
        if 'lt' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['log_type'] = meadow_OsLogType(meadow_event_b99dc03.pop('lt'))
        if 'ttl' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['time_to_live'] = meadow_event_b99dc03.pop('ttl')
        if 'pid' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['process_identifier'] = meadow_event_b99dc03.pop('pid')
        if 'aid' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['activity_identifier'] = meadow_event_b99dc03.pop('aid')
        if 'paid' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['parent_activity_identifier'] = meadow_event_b99dc03.pop('paid')
        if 'tai' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['transition_activity_identifier'] = meadow_event_b99dc03.pop('tai')
        if 'sub' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['subsystem'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('sub')]
        if 'cat' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['category'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('cat')]
        if 'f' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['format_string'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('f')]
        if 'cai' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['creator_activity_identifier'] = meadow_event_b99dc03.pop('cai')
        if 'cpui' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['creator_process_unique_identifier'] = meadow_event_b99dc03.pop('cpui')
        if 'si' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['signpost_identifier'] = meadow_event_b99dc03.pop('si')
        if 'sn' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['signpost_name'] = meadow_log_strings_1e16377[meadow_event_b99dc03.pop('sn')]
        if 'st' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['signpost_type'] = meadow_event_b99dc03.pop('st')
        if 'ss' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['signpost_scope'] = meadow_event_b99dc03.pop('ss')
        if 'lsmct' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['loss_start_mach_continuous_timestamp'] = meadow_event_b99dc03.pop('lsmct')
        if 'lemct' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['loss_end_mach_continuous_timestamp'] = meadow_event_b99dc03.pop('lemct')
        if 'lsud' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['loss_start_unix_date'] = meadow_event_b99dc03.pop('lsud')
        if 'leud' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['loss_end_unix_date'] = meadow_event_b99dc03.pop('leud')
        if 'lsutz' in meadow_event_b99dc03:
            meadow_utz_781f8b9 = meadow_event_b99dc03.pop('lsutz')
            meadow_parsed_event_476ca63['loss_start_unix_timezone'] = {'minutes_west': meadow_utz_781f8b9['mw'], 'dst_time': meadow_utz_781f8b9['dt']}
        if 'leutz' in meadow_event_b99dc03:
            meadow_utz_781f8b9 = meadow_event_b99dc03.pop('leutz')
            meadow_parsed_event_476ca63['loss_end_unix_timezone'] = {'minutes_west': meadow_utz_781f8b9['mw'], 'dst_time': meadow_utz_781f8b9['dt']}
        if 'bt' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['backtrace'] = [{'image_uuid': meadow_level_6aff397['iu'], 'image_offset': meadow_level_6aff397['io']} for meadow_level_6aff397 in meadow_event_b99dc03.pop('bt')]
        if 'lc' in meadow_event_b99dc03:
            meadow_lc_6a26fd3 = meadow_event_b99dc03.pop('lc')
            meadow_parsed_event_476ca63['loss_count'] = {'count': meadow_lc_6a26fd3['c'], 'unknown': meadow_lc_6a26fd3['s']}
        if 'dm' in meadow_event_b99dc03:
            meadow_parsed_event_476ca63['decomposed_message'] = _name_boundary.attributes(meadow_cls_ad5fb46)['parse_decomposed'](meadow_event_b99dc03.pop('dm'), meadow_log_strings_1e16377)
        return meadow_OsLogEvent(**meadow_parsed_event_476ca63)

    @classmethod
    @_name_boundary.callable_contract({'cls': 'meadow_cls_27313f4', 'trace_identifier': 'meadow_trace_identifier_05fbb7e'}, 'parse_trace_identifier')
    def meadow_parse_trace_identifier(meadow_cls_27313f4, meadow_trace_identifier_05fbb7e):
        meadow_trace_id_a4cf80f = _name_boundary.attributes(meadow_firehose_tracepoint_id)['parse'](meadow_Int64ul.build(meadow_trace_identifier_05fbb7e))
        meadow_trace_namespace_834790a = meadow_FirehoseTracepointNamespace(meadow_trace_id_a4cf80f.namespace)
        if meadow_trace_namespace_834790a in meadow_tracepoint_types:
            meadow_type__1839126 = meadow_tracepoint_types[meadow_trace_namespace_834790a](meadow_trace_id_a4cf80f.type_)
        elif meadow_trace_namespace_834790a == meadow_FirehoseTracepointNamespace.signpost:
            meadow_type__1839126 = meadow_FirehoseTracepointSignpostType(meadow_trace_id_a4cf80f.type_ & 192) | meadow_FirehoseTracepointSignpostType(meadow_trace_id_a4cf80f.type_ & 63)
        else:
            meadow_type__1839126 = meadow_trace_id_a4cf80f.type_
        return meadow_TraceIdentifier(namespace=meadow_trace_namespace_834790a, type_=meadow_type__1839126, has_large_offset=meadow_trace_id_a4cf80f.trace_flags.has_large_offset, has_unique_pid=meadow_trace_id_a4cf80f.trace_flags.has_unique_pid, pc_style=meadow_FirehoseTracepointFlagsPcStyle(meadow_trace_id_a4cf80f.trace_flags.pc_style), has_current_aid=meadow_trace_id_a4cf80f.trace_flags.has_current_aid, flags=meadow_tracepoint_flags[meadow_trace_namespace_834790a](meadow_trace_id_a4cf80f.flags) if meadow_trace_namespace_834790a in meadow_tracepoint_flags else None, code=meadow_trace_id_a4cf80f.code)

    @classmethod
    @_name_boundary.callable_contract({'cls': 'meadow_cls_a881943', 'decomposed': 'meadow_decomposed_2a86395', 'log_strings': 'meadow_log_strings_f48e689'}, 'parse_decomposed')
    def meadow_parse_decomposed(meadow_cls_a881943, meadow_decomposed_2a86395, meadow_log_strings_f48e689):
        meadow_parsed_decomposed_1c4ff53 = {'placeholder_count': meadow_decomposed_2a86395['pc'], 'state': meadow_decomposed_2a86395['s']}
        if not meadow_parsed_decomposed_1c4ff53['placeholder_count']:
            return meadow_parsed_decomposed_1c4ff53
        meadow_parsed_decomposed_1c4ff53['segments'] = [_name_boundary.attributes(meadow_cls_a881943)['parse_decomposed_segment'](meadow_seg_1d1b5ae, meadow_log_strings_f48e689) for meadow_seg_1d1b5ae in meadow_decomposed_2a86395['seg']]
        return meadow_parsed_decomposed_1c4ff53

    @classmethod
    @_name_boundary.callable_contract({'cls': 'meadow_cls_0c6fb70', 'segment': 'meadow_segment_65e8072', 'log_strings': 'meadow_log_strings_0ecb861'}, 'parse_decomposed_segment')
    def meadow_parse_decomposed_segment(meadow_cls_0c6fb70, meadow_segment_65e8072, meadow_log_strings_0ecb861):
        meadow_parsed_segment_3e71380 = {}
        if 'lp' in meadow_segment_65e8072:
            meadow_parsed_segment_3e71380['literal_prefix'] = meadow_log_strings_0ecb861[meadow_segment_65e8072['lp']]
        if 'p' in meadow_segment_65e8072:
            meadow_parsed_placeholder_38d9854 = {}
            if 'rs' in meadow_segment_65e8072['p']:
                meadow_parsed_placeholder_38d9854['raw_string'] = meadow_log_strings_0ecb861[meadow_segment_65e8072['p']['rs']]
            if 't' in meadow_segment_65e8072['p'] and meadow_segment_65e8072['p']['t']:
                meadow_parsed_placeholder_38d9854['tokens'] = [meadow_log_strings_0ecb861[meadow_token_b93b59d] for meadow_token_b93b59d in meadow_segment_65e8072['p']['t']]
            if 'tn' in meadow_segment_65e8072['p']:
                meadow_parsed_placeholder_38d9854['type_namespace'] = meadow_log_strings_0ecb861[meadow_segment_65e8072['p']['tn']]
            if 'ty' in meadow_segment_65e8072['p']:
                meadow_parsed_placeholder_38d9854['type'] = meadow_log_strings_0ecb861[meadow_segment_65e8072['p']['ty']]
            meadow_parsed_placeholder_38d9854['width'] = meadow_segment_65e8072['p']['w']
            meadow_parsed_placeholder_38d9854['precision'] = meadow_segment_65e8072['p']['p']
            meadow_parsed_segment_3e71380['placeholder'] = meadow_parsed_placeholder_38d9854
        if 'a' in meadow_segment_65e8072:
            meadow_parsed_arg_99e261e = {}
            if 'a' in meadow_segment_65e8072['a']:
                meadow_parsed_arg_99e261e['availability'] = meadow_segment_65e8072['a']['a']
            if 'p' in meadow_segment_65e8072['a']:
                meadow_parsed_arg_99e261e['privacy'] = meadow_segment_65e8072['a']['p']
            if 'c' in meadow_segment_65e8072['a']:
                meadow_parsed_arg_99e261e['category'] = meadow_segment_65e8072['a']['c']
            if meadow_parsed_arg_99e261e['category'] == 1:
                if 'sc' in meadow_segment_65e8072['a']:
                    meadow_parsed_arg_99e261e['scalar_category'] = meadow_segment_65e8072['a']['sc']
                if 'st' in meadow_segment_65e8072['a']:
                    meadow_parsed_arg_99e261e['scalar_type'] = meadow_segment_65e8072['a']['st']
            if 'availability' not in meadow_parsed_arg_99e261e or meadow_parsed_arg_99e261e['availability'] == 3:
                if 'or' in meadow_segment_65e8072['a']:
                    if meadow_parsed_arg_99e261e['category'] == 2:
                        meadow_parsed_arg_99e261e['object_representation'] = meadow_log_strings_0ecb861[meadow_segment_65e8072['a']['or']]
                    else:
                        meadow_parsed_arg_99e261e['object_representation'] = meadow_segment_65e8072['a']['or']
            meadow_parsed_segment_3e71380['arg'] = meadow_parsed_arg_99e261e
        return meadow_parsed_segment_3e71380

    @_name_boundary.callable_contract({'self': 'meadow_self_995ab8a'}, '__str__')
    def __str__(meadow_self_995ab8a):
        return f'{meadow_self_995ab8a.process}{{{meadow_self_995ab8a.sender}}}[{meadow_self_995ab8a.process_identifier}] {meadow_self_995ab8a.composed_message}'
_name_boundary.module_contract(globals(), {'FirehoseTracepointSingpostFlags': 'meadow_FirehoseTracepointSingpostFlags', 'FirehoseTracepointNamespace': 'meadow_FirehoseTracepointNamespace', 'FirehoseTracepointLogType': 'meadow_FirehoseTracepointLogType', 'FirehoseTracepointMetadataType': 'meadow_FirehoseTracepointMetadataType', 'Int64ul': 'meadow_Int64ul', 'TraceIdentifier': 'meadow_TraceIdentifier', 'BitStruct': 'meadow_BitStruct', 'dataclass': 'meadow_dataclass', 'FirehoseTracepointSignpostType': 'meadow_FirehoseTracepointSignpostType', 'FirehoseTracepointActivityType': 'meadow_FirehoseTracepointActivityType', 'Byte': 'meadow_Byte', 'BitsInteger': 'meadow_BitsInteger', 'firehose_tracepoint_id': 'meadow_firehose_tracepoint_id', 'FirehoseTracepointLogFlags': 'meadow_FirehoseTracepointLogFlags', 'field': 'meadow_field', 'Struct': 'meadow_Struct', 'Int32ul': 'meadow_Int32ul', 'tracepoint_flags': 'meadow_tracepoint_flags', 'List': 'meadow_List', 'timezone': 'meadow_timezone', 'Flag': 'meadow_Flag', 'Padding': 'meadow_Padding', 'Dict': 'meadow_Dict', 'OsLogEvent': 'meadow_OsLogEvent', 'FirehoseTracepointFlagsPcStyle': 'meadow_FirehoseTracepointFlagsPcStyle', 'FirehoseTracepointTraceType': 'meadow_FirehoseTracepointTraceType', 'OsLogType': 'meadow_OsLogType', 'tracepoint_types': 'meadow_tracepoint_types', 'enum': 'meadow_enum', 'datetime': 'meadow_datetime'})
