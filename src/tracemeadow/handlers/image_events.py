# Derived from pykdebugparser/trace_handlers/dyld.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass
from enum import Enum as meadow_Enum
from typing import List as meadow_List
from uuid import UUID as meadow_UUID

@_name_boundary.class_contract('RtldFlag', {})
class meadow_RtldFlag(meadow_Enum):
    RTLD_LAZY = 1
    RTLD_NOW = 2
    RTLD_LOCAL = 4
    RTLD_GLOBAL = 8
    RTLD_NOLOAD = 16
    RTLD_NODELETE = 128
    RTLD_FIRST = 256

@_name_boundary.callable_contract({'flags': 'meadow_flags_9d23bec'}, 'to_rtld_flags')
def meadow_to_rtld_flags(meadow_flags_9d23bec: int):
    return [meadow_r_7a23369 for meadow_r_7a23369 in meadow_RtldFlag if meadow_r_7a23369.value & meadow_flags_9d23bec]

@_name_boundary.class_contract('DyldUuidMapA', {})
@meadow_dataclass
class meadow_DyldUuidMapA:
    ktraces: meadow_List
    uuid: meadow_UUID
    load_addr: int
    fsid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_72a8149'}, '__str__')
    def __str__(meadow_self_72a8149):
        return f'DYLD_uuid_map_a, uuid: "{meadow_self_72a8149.uuid}", load_addr: {hex(meadow_self_72a8149.load_addr)}, fsid: {hex(meadow_self_72a8149.fsid)}'

@_name_boundary.class_contract('DyldUuidMapB', {})
@meadow_dataclass
class meadow_DyldUuidMapB:
    ktraces: meadow_List
    fid_objno: int
    fid_generation: int

    @_name_boundary.callable_contract({'self': 'meadow_self_bffbe26'}, '__str__')
    def __str__(meadow_self_bffbe26):
        return f'DYLD_uuid_map_b, fid_objno: {meadow_self_bffbe26.fid_objno}, fid_generation: {hex(meadow_self_bffbe26.fid_generation)}'

@_name_boundary.class_contract('DyldUuidUnmapA', {})
@meadow_dataclass
class meadow_DyldUuidUnmapA:
    ktraces: meadow_List
    uuid: meadow_UUID
    load_addr: int
    fsid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ffc32f3'}, '__str__')
    def __str__(meadow_self_ffc32f3):
        return f'DYLD_uuid_unmap_a, uuid: "{meadow_self_ffc32f3.uuid}", load_addr: {hex(meadow_self_ffc32f3.load_addr)}, fsid: {hex(meadow_self_ffc32f3.fsid)}'

@_name_boundary.class_contract('DyldUuidUnmapB', {})
@meadow_dataclass
class meadow_DyldUuidUnmapB:
    ktraces: meadow_List
    fid_objno: int
    fid_generation: int

    @_name_boundary.callable_contract({'self': 'meadow_self_b7c6554'}, '__str__')
    def __str__(meadow_self_b7c6554):
        return f'DYLD_uuid_unmap_b, fid_objno: {meadow_self_b7c6554.fid_objno}, fid_generation: {hex(meadow_self_b7c6554.fid_generation)}'

@_name_boundary.class_contract('DyldUuidSharedCacheA', {})
@meadow_dataclass
class meadow_DyldUuidSharedCacheA:
    ktraces: meadow_List
    uuid: meadow_UUID
    load_addr: int
    fsid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_e4c42d5'}, '__str__')
    def __str__(meadow_self_e4c42d5):
        return f'DYLD_uuid_shared_cache_a, uuid: "{meadow_self_e4c42d5.uuid}", load_addr: {hex(meadow_self_e4c42d5.load_addr)}, fsid: {hex(meadow_self_e4c42d5.fsid)}'

@_name_boundary.class_contract('DyldUuidSharedCacheB', {})
@meadow_dataclass
class meadow_DyldUuidSharedCacheB:
    ktraces: meadow_List
    fid_objno: int
    fid_generation: int

    @_name_boundary.callable_contract({'self': 'meadow_self_89df484'}, '__str__')
    def __str__(meadow_self_89df484):
        return f'DYLD_uuid_shared_cache_b, fid_objno: {meadow_self_89df484.fid_objno}, fid_generation: {hex(meadow_self_89df484.fid_generation)}'

@_name_boundary.class_contract('DyldLaunchExecutable', {})
@meadow_dataclass
class meadow_DyldLaunchExecutable:
    ktraces: meadow_List
    main_executable_mh: int
    uuid_map_a: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_0586118'}, '__str__')
    def __str__(meadow_self_0586118):
        return f'DBG_DYLD_TIMING_LAUNCH_EXECUTABLE, main_executable_mh: {hex(meadow_self_0586118.main_executable_mh)}'

@_name_boundary.class_contract('DyldMapImage', {})
@meadow_dataclass
class meadow_DyldMapImage:
    ktraces: meadow_List
    path: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3404804'}, '__str__')
    def __str__(meadow_self_3404804):
        return f'DBG_DYLD_TIMING_MAP_IMAGE, path: {meadow_self_3404804.path}'

@_name_boundary.class_contract('DyldFuncForAddImage', {})
@meadow_dataclass
class meadow_DyldFuncForAddImage:
    ktraces: meadow_List
    addr: int
    func: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c10867e'}, '__str__')
    def __str__(meadow_self_c10867e):
        return f'DBG_DYLD_TIMING_FUNC_FOR_ADD_IMAGE, addr: {hex(meadow_self_c10867e.addr)}, func: {hex(meadow_self_c10867e.func)}'

@_name_boundary.class_contract('DyldBootstrapStart', {})
@meadow_dataclass
class meadow_DyldBootstrapStart:
    ktraces: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_a9aa2e6'}, '__str__')
    def __str__(meadow_self_a9aa2e6):
        return 'DBG_DYLD_TIMING_BOOTSTRAP_START'

@_name_boundary.class_contract('Dlopen', {})
@meadow_dataclass
class meadow_Dlopen:
    ktraces: meadow_List
    path: str
    flags: meadow_List
    handle: int

    @_name_boundary.callable_contract({'self': 'meadow_self_176140b'}, '__str__')
    def __str__(meadow_self_176140b):
        meadow_flags_f33087b = ' | '.join(map(lambda meadow_f_f3e1628: _name_boundary.attributes(meadow_f_f3e1628)['name'], meadow_self_176140b.flags))
        return f'dlopen("{meadow_self_176140b.path}", {meadow_flags_f33087b}), handle: {hex(meadow_self_176140b.handle)}'

@_name_boundary.class_contract('DlopenPreflight', {})
@meadow_dataclass
class meadow_DlopenPreflight:
    ktraces: meadow_List
    path: str
    compatible: bool

    @_name_boundary.callable_contract({'self': 'meadow_self_50ff92a'}, '__str__')
    def __str__(meadow_self_50ff92a):
        return f'dlopen_preflight("{meadow_self_50ff92a.path}"), compatible: {meadow_self_50ff92a.compatible}'

@_name_boundary.class_contract('Dlclose', {})
@meadow_dataclass
class meadow_Dlclose:
    ktraces: meadow_List
    handle: int

    @_name_boundary.callable_contract({'self': 'meadow_self_eb1b0a8'}, '__str__')
    def __str__(meadow_self_eb1b0a8):
        return f'dlclose({hex(meadow_self_eb1b0a8.handle)})'

@_name_boundary.class_contract('Dlsym', {})
@meadow_dataclass
class meadow_Dlsym:
    ktraces: meadow_List
    handle: int
    symbol: str
    address: int

    @_name_boundary.callable_contract({'self': 'meadow_self_02454cd'}, '__str__')
    def __str__(meadow_self_02454cd):
        return f'dlsym({hex(meadow_self_02454cd.handle)}, "{meadow_self_02454cd.symbol}"), address: {hex(meadow_self_02454cd.address)}'

@_name_boundary.class_contract('Dladdr', {})
@meadow_dataclass
class meadow_Dladdr:
    ktraces: meadow_List
    addr: int
    ret: int

    @_name_boundary.callable_contract({'self': 'meadow_self_f2e8f06'}, '__str__')
    def __str__(meadow_self_f2e8f06):
        return f'dladdr({hex(meadow_self_f2e8f06.addr)}), ret: {meadow_self_f2e8f06.ret}'

@_name_boundary.callable_contract({'parser': 'meadow_parser_56b0b6c', 'events': 'meadow_events_66a09c9'}, 'handle_uuid_map_a')
def meadow_handle_uuid_map_a(meadow_parser_56b0b6c, meadow_events_66a09c9):
    meadow_args_fae6139 = meadow_events_66a09c9[0].values
    return meadow_DyldUuidMapA(meadow_events_66a09c9, meadow_UUID(bytes=meadow_events_66a09c9[0].data[:16]), meadow_args_fae6139[2], meadow_args_fae6139[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_ef91e6d', 'events': 'meadow_events_3f7ee19'}, 'handle_uuid_map_b')
def meadow_handle_uuid_map_b(meadow_parser_ef91e6d, meadow_events_3f7ee19):
    meadow_arg_438a915 = meadow_events_3f7ee19[0].values[0]
    return meadow_DyldUuidMapB(meadow_events_3f7ee19, meadow_arg_438a915 & 4294967295, meadow_arg_438a915 >> 32)

@_name_boundary.callable_contract({'parser': 'meadow_parser_6e04f9d', 'events': 'meadow_events_dc12355'}, 'handle_uuid_unmap_a')
def meadow_handle_uuid_unmap_a(meadow_parser_6e04f9d, meadow_events_dc12355):
    meadow_args_508c2dc = meadow_events_dc12355[0].values
    return meadow_DyldUuidUnmapA(meadow_events_dc12355, meadow_UUID(bytes=meadow_events_dc12355[0].data[:16]), meadow_args_508c2dc[2], meadow_args_508c2dc[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_c1c37f7', 'events': 'meadow_events_97a7be2'}, 'handle_uuid_unmap_b')
def meadow_handle_uuid_unmap_b(meadow_parser_c1c37f7, meadow_events_97a7be2):
    meadow_arg_be858a1 = meadow_events_97a7be2[0].values[0]
    return meadow_DyldUuidUnmapB(meadow_events_97a7be2, meadow_arg_be858a1 & 4294967295, meadow_arg_be858a1 >> 32)

@_name_boundary.callable_contract({'parser': 'meadow_parser_c17053e', 'events': 'meadow_events_a7bc6b2'}, 'handle_uuid_shared_cache_a')
def meadow_handle_uuid_shared_cache_a(meadow_parser_c17053e, meadow_events_a7bc6b2):
    meadow_args_5754444 = meadow_events_a7bc6b2[0].values
    return meadow_DyldUuidSharedCacheA(meadow_events_a7bc6b2, meadow_UUID(bytes=meadow_events_a7bc6b2[0].data[:16]), meadow_args_5754444[2], meadow_args_5754444[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_b46991d', 'events': 'meadow_events_8d26c90'}, 'handle_uuid_shared_cache_b')
def meadow_handle_uuid_shared_cache_b(meadow_parser_b46991d, meadow_events_8d26c90):
    meadow_arg_e7542eb = meadow_events_8d26c90[0].values[0]
    return meadow_DyldUuidSharedCacheB(meadow_events_8d26c90, meadow_arg_e7542eb & 4294967295, meadow_arg_e7542eb >> 32)

@_name_boundary.callable_contract({'parser': 'meadow_parser_8ba1e1a', 'events': 'meadow_events_1f995be'}, 'handle_timing_launch_executable')
def meadow_handle_timing_launch_executable(meadow_parser_8ba1e1a, meadow_events_1f995be):
    meadow_map_a_33a88ad = [meadow_handle_uuid_map_a(meadow_parser_8ba1e1a, [meadow_e_3699bc7]) for meadow_e_3699bc7 in meadow_events_1f995be if _name_boundary.attributes(meadow_parser_8ba1e1a)['trace_codes'].get(meadow_e_3699bc7.eventid) == 'DYLD_uuid_map_a']
    meadow_map_a_33a88ad += [meadow_handle_uuid_shared_cache_a(meadow_parser_8ba1e1a, [meadow_e_5b8ff63]) for meadow_e_5b8ff63 in meadow_events_1f995be if _name_boundary.attributes(meadow_parser_8ba1e1a)['trace_codes'].get(meadow_e_5b8ff63.eventid) == 'DYLD_uuid_shared_cache_a']
    meadow_map_a_33a88ad = sorted(meadow_map_a_33a88ad, key=lambda meadow_x_50b567a: meadow_x_50b567a.load_addr)
    return meadow_DyldLaunchExecutable(meadow_events_1f995be, meadow_events_1f995be[0].values[1], meadow_map_a_33a88ad)

@_name_boundary.callable_contract({'parser': 'meadow_parser_d0bfd98', 'events': 'meadow_events_3966b2d'}, 'handle_timing_map_image')
def meadow_handle_timing_map_image(meadow_parser_d0bfd98, meadow_events_3966b2d):
    meadow_args_f140eb9 = meadow_events_3966b2d[0].values
    meadow_path_d8997f5 = _name_boundary.attributes(meadow_parser_d0bfd98)['global_strings'][meadow_args_f140eb9[1]] if meadow_args_f140eb9[1] else ''
    return meadow_DyldMapImage(meadow_events_3966b2d, meadow_path_d8997f5)

@_name_boundary.callable_contract({'parser': 'meadow_parser_ddbcba2', 'events': 'meadow_events_99b313f'}, 'handle_timing_func_for_add_image')
def meadow_handle_timing_func_for_add_image(meadow_parser_ddbcba2, meadow_events_99b313f):
    meadow_args_ffa027c = meadow_events_99b313f[0].values
    return meadow_DyldFuncForAddImage(meadow_events_99b313f, meadow_args_ffa027c[1], meadow_args_ffa027c[2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_0e9cd06', 'events': 'meadow_events_5d28ec5'}, 'handle_timing_bootstrap_start')
def meadow_handle_timing_bootstrap_start(meadow_parser_0e9cd06, meadow_events_5d28ec5):
    return meadow_DyldBootstrapStart(meadow_events_5d28ec5)

@_name_boundary.callable_contract({'parser': 'meadow_parser_7392649', 'events': 'meadow_events_074d84f'}, 'handle_timing_dlopen')
def meadow_handle_timing_dlopen(meadow_parser_7392649, meadow_events_074d84f):
    meadow_args_08c1a77 = meadow_events_074d84f[0].values
    meadow_path_170e712 = _name_boundary.attributes(meadow_parser_7392649)['global_strings'][meadow_args_08c1a77[1]] if meadow_args_08c1a77[1] else ''
    return meadow_Dlopen(meadow_events_074d84f, meadow_path_170e712, meadow_to_rtld_flags(meadow_args_08c1a77[2]), meadow_events_074d84f[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_d11ab6b', 'events': 'meadow_events_7a3b84f'}, 'handle_timing_dlopen_preflight')
def meadow_handle_timing_dlopen_preflight(meadow_parser_d11ab6b, meadow_events_7a3b84f):
    return meadow_DlopenPreflight(meadow_events_7a3b84f, _name_boundary.attributes(meadow_parser_d11ab6b)['global_strings'][meadow_events_7a3b84f[0].values[1]], bool(meadow_events_7a3b84f[-1].values[1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c20c32d', 'events': 'meadow_events_d812ce9'}, 'handle_timing_dlclose')
def meadow_handle_timing_dlclose(meadow_parser_c20c32d, meadow_events_d812ce9):
    return meadow_Dlclose(meadow_events_d812ce9, meadow_events_d812ce9[0].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_a84295b', 'events': 'meadow_events_f2208de'}, 'handle_timing_dlsym')
def meadow_handle_timing_dlsym(meadow_parser_a84295b, meadow_events_f2208de):
    meadow_args_d4a4bb0 = meadow_events_f2208de[0].values
    return meadow_Dlsym(meadow_events_f2208de, meadow_args_d4a4bb0[1], _name_boundary.attributes(meadow_parser_a84295b)['global_strings'][meadow_args_d4a4bb0[2]], meadow_events_f2208de[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_044e328', 'events': 'meadow_events_5797006'}, 'handle_timing_dladdr')
def meadow_handle_timing_dladdr(meadow_parser_044e328, meadow_events_5797006):
    return meadow_Dladdr(meadow_events_5797006, meadow_events_5797006[0].values[1], meadow_events_5797006[-1].values[1])
meadow_handlers = {'DYLD_uuid_map_a': meadow_handle_uuid_map_a, 'DYLD_uuid_map_b': meadow_handle_uuid_map_b, 'DYLD_uuid_unmap_a': meadow_handle_uuid_unmap_a, 'DYLD_uuid_unmap_b': meadow_handle_uuid_unmap_b, 'DYLD_uuid_shared_cache_a': meadow_handle_uuid_shared_cache_a, 'DYLD_uuid_shared_cache_b': meadow_handle_uuid_shared_cache_b, 'DBG_DYLD_TIMING_LAUNCH_EXECUTABLE': meadow_handle_timing_launch_executable, 'DBG_DYLD_TIMING_MAP_IMAGE': meadow_handle_timing_map_image, 'DBG_DYLD_TIMING_FUNC_FOR_ADD_IMAGE': meadow_handle_timing_func_for_add_image, 'DBG_DYLD_TIMING_BOOTSTRAP_START': meadow_handle_timing_bootstrap_start, 'DBG_DYLD_TIMING_DLOPEN': meadow_handle_timing_dlopen, 'DBG_DYLD_TIMING_DLOPEN_PREFLIGHT': meadow_handle_timing_dlopen_preflight, 'DBG_DYLD_TIMING_DLCLOSE': meadow_handle_timing_dlclose, 'DBG_DYLD_TIMING_DLSYM': meadow_handle_timing_dlsym, 'DBG_DYLD_TIMING_DLADDR': meadow_handle_timing_dladdr}
_name_boundary.module_contract(globals(), {'Dlclose': 'meadow_Dlclose', 'handle_timing_bootstrap_start': 'meadow_handle_timing_bootstrap_start', 'DyldFuncForAddImage': 'meadow_DyldFuncForAddImage', 'handle_timing_func_for_add_image': 'meadow_handle_timing_func_for_add_image', 'UUID': 'meadow_UUID', 'handle_timing_dladdr': 'meadow_handle_timing_dladdr', 'RtldFlag': 'meadow_RtldFlag', 'handle_timing_map_image': 'meadow_handle_timing_map_image', 'handlers': 'meadow_handlers', 'dataclass': 'meadow_dataclass', 'handle_uuid_shared_cache_a': 'meadow_handle_uuid_shared_cache_a', 'DyldLaunchExecutable': 'meadow_DyldLaunchExecutable', 'DyldBootstrapStart': 'meadow_DyldBootstrapStart', 'DyldUuidMapA': 'meadow_DyldUuidMapA', 'handle_uuid_unmap_a': 'meadow_handle_uuid_unmap_a', 'DyldUuidMapB': 'meadow_DyldUuidMapB', 'handle_timing_dlclose': 'meadow_handle_timing_dlclose', 'handle_uuid_shared_cache_b': 'meadow_handle_uuid_shared_cache_b', 'Dlsym': 'meadow_Dlsym', 'to_rtld_flags': 'meadow_to_rtld_flags', 'handle_timing_launch_executable': 'meadow_handle_timing_launch_executable', 'handle_uuid_map_b': 'meadow_handle_uuid_map_b', 'DyldUuidSharedCacheB': 'meadow_DyldUuidSharedCacheB', 'Dlopen': 'meadow_Dlopen', 'Enum': 'meadow_Enum', 'handle_uuid_unmap_b': 'meadow_handle_uuid_unmap_b', 'handle_timing_dlsym': 'meadow_handle_timing_dlsym', 'List': 'meadow_List', 'DyldUuidUnmapB': 'meadow_DyldUuidUnmapB', 'handle_timing_dlopen': 'meadow_handle_timing_dlopen', 'DyldMapImage': 'meadow_DyldMapImage', 'DyldUuidUnmapA': 'meadow_DyldUuidUnmapA', 'Dladdr': 'meadow_Dladdr', 'DyldUuidSharedCacheA': 'meadow_DyldUuidSharedCacheA', 'handle_timing_dlopen_preflight': 'meadow_handle_timing_dlopen_preflight', 'handle_uuid_map_a': 'meadow_handle_uuid_map_a', 'DlopenPreflight': 'meadow_DlopenPreflight'})
