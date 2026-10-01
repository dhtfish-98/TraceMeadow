# Derived from pykdebugparser/trace_handlers/turnstile.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass
from enum import Enum as meadow_Enum
from typing import List as meadow_List

@_name_boundary.class_contract('TurnstileType', {})
class meadow_TurnstileType(meadow_Enum):
    TURNSTILE_NONE = 0
    TURNSTILE_KERNEL_MUTEX = 1
    TURNSTILE_ULOCK = 2
    TURNSTILE_PTHREAD_MUTEX = 3
    TURNSTILE_SYNC_IPC = 4
    TURNSTILE_WORKLOOPS = 5
    TURNSTILE_WORKQS = 6
    TURNSTILE_KNOTE = 7
    TURNSTILE_SLEEP_INHERITOR = 8
    TURNSTILE_EPOCH_KERNEL = 9
    TURNSTILE_EPOCH_USER = 10
    TURNSTILE_TOTAL_TYPES = 11

@_name_boundary.class_contract('TurnstileWaitqAddThreadPriorityQueue', {})
@meadow_dataclass
class meadow_TurnstileWaitqAddThreadPriorityQueue:
    ktraces: meadow_List
    turnstile: int
    tid: int
    priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c406adb'}, '__str__')
    def __str__(meadow_self_c406adb):
        return f'turnstile_waitq_add_thread_priority_queue, turnstile: {hex(meadow_self_c406adb.turnstile)}, tid: {meadow_self_c406adb.tid}, priority: {meadow_self_c406adb.priority}'

@_name_boundary.class_contract('ThreadRemovedFromTurnstileWaitq', {})
@meadow_dataclass
class meadow_ThreadRemovedFromTurnstileWaitq:
    ktraces: meadow_List
    turnstile: int
    tid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_20a794b'}, '__str__')
    def __str__(meadow_self_20a794b):
        return f'thread_removed_from_turnstile_waitq, turnstile: {hex(meadow_self_20a794b.turnstile)}, tid: {meadow_self_20a794b.tid}'

@_name_boundary.class_contract('ThreadMovedInTurnstileWaitq', {})
@meadow_dataclass
class meadow_ThreadMovedInTurnstileWaitq:
    ktraces: meadow_List
    dst_turnstile: int
    tid: int
    priority: int
    thread_link_priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_efc4995'}, '__str__')
    def __str__(meadow_self_efc4995):
        return f'turnstile_update_thread_promotion_locked, turnstile: {hex(meadow_self_efc4995.dst_turnstile)}, tid: {meadow_self_efc4995.tid}, priority: {meadow_self_efc4995.priority}, link priority: {meadow_self_efc4995.thread_link_priority}'

@_name_boundary.class_contract('TurnstileAddTurnstilePromotion', {})
@meadow_dataclass
class meadow_TurnstileAddTurnstilePromotion:
    ktraces: meadow_List
    dst_turnstile: int
    src_turnstile: int
    src_ts_priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_e2d2b5f'}, '__str__')
    def __str__(meadow_self_e2d2b5f):
        return f'turnstile_add_turnstile_promotion({hex(meadow_self_e2d2b5f.dst_turnstile)}, {hex(meadow_self_e2d2b5f.src_turnstile)}), src_turnstile->ts_priority: {meadow_self_e2d2b5f.src_ts_priority}'

@_name_boundary.class_contract('TurnstileRemoveTurnstilePromotion', {})
@meadow_dataclass
class meadow_TurnstileRemoveTurnstilePromotion:
    ktraces: meadow_List
    dst_turnstile: int
    src_turnstile: int

    @_name_boundary.callable_contract({'self': 'meadow_self_e91e9d7'}, '__str__')
    def __str__(meadow_self_e91e9d7):
        return f'turnstile_remove_turnstile_promotion({hex(meadow_self_e91e9d7.dst_turnstile)}, {hex(meadow_self_e91e9d7.src_turnstile)})'

@_name_boundary.class_contract('TurnstileUpdateTurnstilePromotionLocked', {})
@meadow_dataclass
class meadow_TurnstileUpdateTurnstilePromotionLocked:
    ktraces: meadow_List
    dst_turnstile: int
    src_turnstile: int
    src_ts_priority: int
    src_turnstile_link_priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_212c90c'}, '__str__')
    def __str__(meadow_self_212c90c):
        return f'turnstile_update_turnstile_promotion_locked({hex(meadow_self_212c90c.dst_turnstile)}, {hex(meadow_self_212c90c.src_turnstile)}), src_turnstile->ts_priority: {meadow_self_212c90c.src_ts_priority}, src_turnstile_link_priority: {meadow_self_212c90c.src_turnstile_link_priority}'

@_name_boundary.class_contract('AddedFromThreadHeap', {})
@meadow_dataclass
class meadow_AddedFromThreadHeap:
    ktraces: meadow_List
    tid: int
    turnstile: int
    priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_0b6d28a'}, '__str__')
    def __str__(meadow_self_0b6d28a):
        return f'thread_add_turnstile_promotion({meadow_self_0b6d28a.tid}, {hex(meadow_self_0b6d28a.turnstile)}), priority: {meadow_self_0b6d28a.priority}'

@_name_boundary.class_contract('RemovedFromThreadHeap', {})
@meadow_dataclass
class meadow_RemovedFromThreadHeap:
    ktraces: meadow_List
    tid: int
    turnstile: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c3c0a1c'}, '__str__')
    def __str__(meadow_self_c3c0a1c):
        return f'thread_remove_turnstile_promotion({meadow_self_c3c0a1c.tid}, {hex(meadow_self_c3c0a1c.turnstile)})'

@_name_boundary.class_contract('ThreadUpdateTurnstilePromotionLocked', {})
@meadow_dataclass
class meadow_ThreadUpdateTurnstilePromotionLocked:
    ktraces: meadow_List
    tid: int
    turnstile: int
    turnstile_ts_priority: int
    turnstile_link_priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c1ac1cb'}, '__str__')
    def __str__(meadow_self_c1ac1cb):
        return f'thread_update_turnstile_promotion_locked, tid: {meadow_self_c1ac1cb.tid}, turnstile: {hex(meadow_self_c1ac1cb.turnstile)}, old_priority: {meadow_self_c1ac1cb.turnstile_ts_priority}, new_priority: {meadow_self_c1ac1cb.turnstile_link_priority}'

@_name_boundary.class_contract('ThreadNotWaitingOnTurnstile', {})
@meadow_dataclass
class meadow_ThreadNotWaitingOnTurnstile:
    ktraces: meadow_List
    tid: int
    turnstile_max_hop: int
    thread_hop: int

    @_name_boundary.callable_contract({'self': 'meadow_self_857fca8'}, '__str__')
    def __str__(meadow_self_857fca8):
        return f'thread_not_waiting_on_turnstile, tid: {meadow_self_857fca8.tid}, turnstile_max_hop: {meadow_self_857fca8.turnstile_max_hop}, thread_hop: {meadow_self_857fca8.thread_hop}'

@_name_boundary.class_contract('TurnstileRecomputePriorityLocked', {})
@meadow_dataclass
class meadow_TurnstileRecomputePriorityLocked:
    ktraces: meadow_List
    turnstile: int
    new_priority: int
    old_priority: int

    @_name_boundary.callable_contract({'self': 'meadow_self_f9302d2'}, '__str__')
    def __str__(meadow_self_f9302d2):
        return f'turnstile_recompute_priority_locked({hex(meadow_self_f9302d2.turnstile)}), new_priority: {meadow_self_f9302d2.new_priority}, old_priority: {meadow_self_f9302d2.old_priority}'

@_name_boundary.class_contract('ThreadRecomputeUserPromotionLocked', {})
@meadow_dataclass
class meadow_ThreadRecomputeUserPromotionLocked:
    ktraces: meadow_List
    tid: int
    user_promotion_basepri: int
    thread_user_promotion_basepri: int

    @_name_boundary.callable_contract({'self': 'meadow_self_75183d7'}, '__str__')
    def __str__(meadow_self_75183d7):
        return f'thread_recompute_user_promotion_locked, tid: {meadow_self_75183d7.tid}, new_priority: {meadow_self_75183d7.user_promotion_basepri}, old_priority: {meadow_self_75183d7.thread_user_promotion_basepri}'

@_name_boundary.class_contract('TurnstilePrepare', {})
@meadow_dataclass
class meadow_TurnstilePrepare:
    ktraces: meadow_List
    turnstile: int
    proprietor: int
    type_: meadow_TurnstileType

    @_name_boundary.callable_contract({'self': 'meadow_self_bff1261'}, '__str__')
    def __str__(meadow_self_bff1261):
        return f"turnstile_prepare, turnstile: {hex(meadow_self_bff1261.turnstile)}, proprietor: {hex(meadow_self_bff1261.proprietor)}, type: {_name_boundary.attributes(meadow_self_bff1261.type_)['name']}"

@_name_boundary.class_contract('TurnstileComplete', {})
@meadow_dataclass
class meadow_TurnstileComplete:
    ktraces: meadow_List
    turnstile: int
    proprietor: int
    type_: meadow_TurnstileType

    @_name_boundary.callable_contract({'self': 'meadow_self_c3f598f'}, '__str__')
    def __str__(meadow_self_c3f598f):
        return f"turnstile_complete, turnstile: {hex(meadow_self_c3f598f.turnstile)}, proprietor: {hex(meadow_self_c3f598f.proprietor)}, type: {_name_boundary.attributes(meadow_self_c3f598f.type_)['name']}"

@_name_boundary.callable_contract({'parser': 'meadow_parser_17da584', 'events': 'meadow_events_814241a'}, 'handle_turnstile_thread_added_to_turnstile_waitq')
def meadow_handle_turnstile_thread_added_to_turnstile_waitq(meadow_parser_17da584, meadow_events_814241a):
    return meadow_TurnstileWaitqAddThreadPriorityQueue(meadow_events_814241a, *meadow_events_814241a[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_57d953a', 'events': 'meadow_events_102d83a'}, 'handle_turnstile_thread_removed_from_turnstile_waitq')
def meadow_handle_turnstile_thread_removed_from_turnstile_waitq(meadow_parser_57d953a, meadow_events_102d83a):
    return meadow_ThreadRemovedFromTurnstileWaitq(meadow_events_102d83a, *meadow_events_102d83a[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_572c220', 'events': 'meadow_events_6ad0324'}, 'handle_turnstile_thread_moved_in_turnstile_waitq')
def meadow_handle_turnstile_thread_moved_in_turnstile_waitq(meadow_parser_572c220, meadow_events_6ad0324):
    return meadow_ThreadMovedInTurnstileWaitq(meadow_events_6ad0324, *meadow_events_6ad0324[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_3e1476e', 'events': 'meadow_events_a73a389'}, 'handle_turnstile_added_to_turnstile_heap')
def meadow_handle_turnstile_added_to_turnstile_heap(meadow_parser_3e1476e, meadow_events_a73a389):
    return meadow_TurnstileAddTurnstilePromotion(meadow_events_a73a389, *meadow_events_a73a389[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_4705c37', 'events': 'meadow_events_4bcac5e'}, 'handle_turnstile_removed_from_turnstile_heap')
def meadow_handle_turnstile_removed_from_turnstile_heap(meadow_parser_4705c37, meadow_events_4bcac5e):
    return meadow_TurnstileRemoveTurnstilePromotion(meadow_events_4bcac5e, *meadow_events_4bcac5e[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_139d385', 'events': 'meadow_events_b535531'}, 'handle_turnstile_moved_in_turnstile_heap')
def meadow_handle_turnstile_moved_in_turnstile_heap(meadow_parser_139d385, meadow_events_b535531):
    return meadow_TurnstileUpdateTurnstilePromotionLocked(meadow_events_b535531, *meadow_events_b535531[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_86f20cc', 'events': 'meadow_events_48aa5c5'}, 'handle_turnstile_added_from_thread_heap')
def meadow_handle_turnstile_added_from_thread_heap(meadow_parser_86f20cc, meadow_events_48aa5c5):
    return meadow_AddedFromThreadHeap(meadow_events_48aa5c5, *meadow_events_48aa5c5[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_85c34fb', 'events': 'meadow_events_bcfa0f4'}, 'handle_turnstile_removed_from_thread_heap')
def meadow_handle_turnstile_removed_from_thread_heap(meadow_parser_85c34fb, meadow_events_bcfa0f4):
    return meadow_RemovedFromThreadHeap(meadow_events_bcfa0f4, *meadow_events_bcfa0f4[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_5dcd4f6', 'events': 'meadow_events_ed0b206'}, 'handle_turnstile_moved_in_thread_heap')
def meadow_handle_turnstile_moved_in_thread_heap(meadow_parser_5dcd4f6, meadow_events_ed0b206):
    return meadow_ThreadUpdateTurnstilePromotionLocked(meadow_events_ed0b206, *meadow_events_ed0b206[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_96cc78c', 'events': 'meadow_events_f546f10'}, 'handle_thread_not_waiting_on_turnstile')
def meadow_handle_thread_not_waiting_on_turnstile(meadow_parser_96cc78c, meadow_events_f546f10):
    return meadow_ThreadNotWaitingOnTurnstile(meadow_events_f546f10, *meadow_events_f546f10[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_4c9c91b', 'events': 'meadow_events_28c7546'}, 'handle_turnstile_priority_change')
def meadow_handle_turnstile_priority_change(meadow_parser_4c9c91b, meadow_events_28c7546):
    return meadow_TurnstileRecomputePriorityLocked(meadow_events_28c7546, *meadow_events_28c7546[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_a599177', 'events': 'meadow_events_a056e07'}, 'handle_thread_user_promotion_change')
def meadow_handle_thread_user_promotion_change(meadow_parser_a599177, meadow_events_a056e07):
    return meadow_ThreadRecomputeUserPromotionLocked(meadow_events_a056e07, *meadow_events_a056e07[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_740c2a2', 'events': 'meadow_events_da91079'}, 'handle_turnstile_turnstile_prepare')
def meadow_handle_turnstile_turnstile_prepare(meadow_parser_740c2a2, meadow_events_da91079):
    return meadow_TurnstilePrepare(meadow_events_da91079, *meadow_events_da91079[0].values[:2], meadow_TurnstileType(meadow_events_da91079[0].values[2]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7076dcb', 'events': 'meadow_events_6d43d14'}, 'handle_turnstile_turnstile_complete')
def meadow_handle_turnstile_turnstile_complete(meadow_parser_7076dcb, meadow_events_6d43d14):
    return meadow_TurnstileComplete(meadow_events_6d43d14, *meadow_events_6d43d14[0].values[:2], meadow_TurnstileType(meadow_events_6d43d14[0].values[2]))
meadow_handlers = {'TURNSTILE_thread_added_to_turnstile_waitq': meadow_handle_turnstile_thread_added_to_turnstile_waitq, 'TURNSTILE_thread_removed_from_turnstile_waitq': meadow_handle_turnstile_thread_removed_from_turnstile_waitq, 'TURNSTILE_thread_moved_in_turnstile_waitq': meadow_handle_turnstile_thread_moved_in_turnstile_waitq, 'TURNSTILE_turnstile_added_to_turnstile_heap': meadow_handle_turnstile_added_to_turnstile_heap, 'TURNSTILE_turnstile_removed_from_turnstile_heap': meadow_handle_turnstile_removed_from_turnstile_heap, 'TURNSTILE_turnstile_moved_in_turnstile_heap': meadow_handle_turnstile_moved_in_turnstile_heap, 'TURNSTILE_turnstile_added_to_thread_heap': meadow_handle_turnstile_added_from_thread_heap, 'TURNSTILE_turnstile_removed_from_thread_heap': meadow_handle_turnstile_removed_from_thread_heap, 'TURNSTILE_turnstile_moved_in_thread_heap': meadow_handle_turnstile_moved_in_thread_heap, 'TURNSTILE_thread_not_waiting_on_turnstile': meadow_handle_thread_not_waiting_on_turnstile, 'TURNSTILE_turnstile_priority_change': meadow_handle_turnstile_priority_change, 'TURNSTILE_thread_user_promotion_change': meadow_handle_thread_user_promotion_change, 'TURNSTILE_turnstile_prepare': meadow_handle_turnstile_turnstile_prepare, 'TURNSTILE_turnstile_complete': meadow_handle_turnstile_turnstile_complete}
_name_boundary.module_contract(globals(), {'handle_turnstile_turnstile_prepare': 'meadow_handle_turnstile_turnstile_prepare', 'TurnstilePrepare': 'meadow_TurnstilePrepare', 'handle_turnstile_priority_change': 'meadow_handle_turnstile_priority_change', 'handle_turnstile_thread_removed_from_turnstile_waitq': 'meadow_handle_turnstile_thread_removed_from_turnstile_waitq', 'RemovedFromThreadHeap': 'meadow_RemovedFromThreadHeap', 'handle_thread_user_promotion_change': 'meadow_handle_thread_user_promotion_change', 'handlers': 'meadow_handlers', 'TurnstileRecomputePriorityLocked': 'meadow_TurnstileRecomputePriorityLocked', 'handle_turnstile_thread_moved_in_turnstile_waitq': 'meadow_handle_turnstile_thread_moved_in_turnstile_waitq', 'TurnstileAddTurnstilePromotion': 'meadow_TurnstileAddTurnstilePromotion', 'TurnstileType': 'meadow_TurnstileType', 'TurnstileUpdateTurnstilePromotionLocked': 'meadow_TurnstileUpdateTurnstilePromotionLocked', 'dataclass': 'meadow_dataclass', 'ThreadUpdateTurnstilePromotionLocked': 'meadow_ThreadUpdateTurnstilePromotionLocked', 'handle_turnstile_added_to_turnstile_heap': 'meadow_handle_turnstile_added_to_turnstile_heap', 'handle_turnstile_moved_in_thread_heap': 'meadow_handle_turnstile_moved_in_thread_heap', 'TurnstileRemoveTurnstilePromotion': 'meadow_TurnstileRemoveTurnstilePromotion', 'ThreadRecomputeUserPromotionLocked': 'meadow_ThreadRecomputeUserPromotionLocked', 'TurnstileWaitqAddThreadPriorityQueue': 'meadow_TurnstileWaitqAddThreadPriorityQueue', 'handle_turnstile_thread_added_to_turnstile_waitq': 'meadow_handle_turnstile_thread_added_to_turnstile_waitq', 'ThreadRemovedFromTurnstileWaitq': 'meadow_ThreadRemovedFromTurnstileWaitq', 'handle_turnstile_moved_in_turnstile_heap': 'meadow_handle_turnstile_moved_in_turnstile_heap', 'handle_turnstile_turnstile_complete': 'meadow_handle_turnstile_turnstile_complete', 'Enum': 'meadow_Enum', 'handle_turnstile_removed_from_turnstile_heap': 'meadow_handle_turnstile_removed_from_turnstile_heap', 'handle_turnstile_added_from_thread_heap': 'meadow_handle_turnstile_added_from_thread_heap', 'List': 'meadow_List', 'handle_turnstile_removed_from_thread_heap': 'meadow_handle_turnstile_removed_from_thread_heap', 'ThreadMovedInTurnstileWaitq': 'meadow_ThreadMovedInTurnstileWaitq', 'handle_thread_not_waiting_on_turnstile': 'meadow_handle_thread_not_waiting_on_turnstile', 'ThreadNotWaitingOnTurnstile': 'meadow_ThreadNotWaitingOnTurnstile', 'TurnstileComplete': 'meadow_TurnstileComplete', 'AddedFromThreadHeap': 'meadow_AddedFromThreadHeap'})
