# Derived from tests/traces/test_mach.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent
from tracemeadow.handlers.kernel_calls import meadow_AsynchronousSystemTrapsReason as meadow_AsynchronousSystemTrapsReason, meadow_ThreadState as meadow_ThreadState, meadow_ProcessState as meadow_ProcessState, meadow_DbgVmFaultType as meadow_DbgVmFaultType, meadow_VmProtection as meadow_VmProtection

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_52b7280'}, 'test_kernel_data_abort_same_el_exc_arm')
def meadow_test_kernel_data_abort_same_el_exc_arm(meadow_traces_parser_52b7280):
    meadow_events_c529b24 = [meadow_Kevent(timestamp=4188336568757, data=b'K\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00HH\x13\x07\xf0\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00', values=(2516582475, 0, 18446744005108779080, 0), tid=690, debugid=16973973, eventid=16973972, func_qualifier=1), meadow_Kevent(timestamp=4188336568849, data=b'K\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00HH\x13\x07\xf0\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00', values=(2516582475, 0, 18446744005108779080, 0), tid=690, debugid=16973974, eventid=16973972, func_qualifier=2)]
    meadow_ret_62143f3 = list(_name_boundary.attributes(meadow_traces_parser_52b7280)['feed_generator'](meadow_events_c529b24))
    meadow_abort_28c0149 = meadow_ret_62143f3[0]
    assert meadow_abort_28c0149.esr == 2516582475
    assert meadow_abort_28c0149.far == 0
    assert meadow_abort_28c0149.pc == 18446744005108779080

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_6b7db1a'}, 'test_interrupt')
def meadow_test_interrupt(meadow_traces_parser_6b7db1a):
    meadow_events_07f8406 = [meadow_Kevent(timestamp=9999124593098, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\xb0\x07p\x94\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00', values=(0, 6785337264, 1, 3), tid=825504, debugid=17104897, eventid=17104896, func_qualifier=1), meadow_Kevent(timestamp=9999124593219, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=825504, debugid=17104898, eventid=17104896, func_qualifier=2)]
    meadow_ret_03ae3f8 = list(_name_boundary.attributes(meadow_traces_parser_6b7db1a)['feed_generator'](meadow_events_07f8406))
    meadow_interrupt_ce8d730 = meadow_ret_03ae3f8[0]
    assert meadow_interrupt_ce8d730.pc == 6785337264
    assert meadow_interrupt_ce8d730.is_user
    assert meadow_interrupt_ce8d730.type == 3

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_2fbb0d5'}, 'test_user_data_abort_lower_el_exc_arm')
def meadow_test_user_data_abort_lower_el_exc_arm(meadow_traces_parser_2fbb0d5):
    meadow_events_642ab03 = [meadow_Kevent(timestamp=10170262586161, data=b'K\x00\x00\x92\x00\x00\x00\x00\xc0bEm\x01\x00\x00\x00$]\x14\x93\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(2449473611, 6128231104, 6762552612, 0), tid=840790, debugid=16974993, eventid=16974992, func_qualifier=1), meadow_Kevent(timestamp=10170262586221, data=b'K\x00\x00\x92\x00\x00\x00\x00\xc0bEm\x01\x00\x00\x00$]\x14\x93\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(2449473611, 6128231104, 6762552612, 0), tid=840790, debugid=16974994, eventid=16974992, func_qualifier=2)]
    meadow_ret_b94abea = list(_name_boundary.attributes(meadow_traces_parser_2fbb0d5)['feed_generator'](meadow_events_642ab03))
    meadow_abort_aa025cd = meadow_ret_b94abea[0]
    assert meadow_abort_aa025cd.esr == 2449473611
    assert meadow_abort_aa025cd.far == 6128231104
    assert meadow_abort_aa025cd.pc == 6762552612

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_6482bc0'}, 'test_decr_trap')
def meadow_test_decr_trap(meadow_traces_parser_6482bc0):
    meadow_events_b2922df = [meadow_Kevent(timestamp=5453855881172, data=b'\xe3\xff\xff\xff\xff\xff\xff\xff\xc4\x9dt\xac\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(18446744073709551587, 7188291012, 1, 0), tid=941745, debugid=17367040, eventid=17367040, func_qualifier=0)]
    meadow_ret_cc6d279 = list(_name_boundary.attributes(meadow_traces_parser_6482bc0)['feed_generator'](meadow_events_b2922df))
    meadow_trace_513fda0 = meadow_ret_cc6d279[0]
    assert meadow_trace_513fda0.latency == -29
    assert meadow_trace_513fda0.pc == 7188291012
    assert meadow_trace_513fda0.user_mode

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_5accb03'}, 'test_decr_set')
def meadow_test_decr_set(meadow_traces_parser_5accb03):
    meadow_events_7609bf2 = [meadow_Kevent(timestamp=10041923525014, data=b'\xb7\xa8\x03\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(239799, 2, 0, 0), tid=267, debugid=17367044, eventid=17367044, func_qualifier=0)]
    meadow_ret_27b81d7 = list(_name_boundary.attributes(meadow_traces_parser_5accb03)['feed_generator'](meadow_events_7609bf2))
    meadow_decr_set_05f50cf = meadow_ret_27b81d7[0]
    assert meadow_decr_set_05f50cf.decr == 239799
    assert meadow_decr_set_05f50cf.deadline == 0
    assert meadow_decr_set_05f50cf.queue_count == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_00afa1e'}, 'test_msc_mach_vm_allocate_trap')
def meadow_test_msc_mach_vm_allocate_trap(meadow_traces_parser_00afa1e):
    meadow_events_6ffdb54 = [meadow_Kevent(timestamp=7476363431, data=b'\x03\x02\x00\x00\x00\x00\x00\x00\x08#\xc0k\x01\x00\x00\x00\xa0o\n\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00', values=(515, 6102721288, 683936, 1), tid=6740, debugid=17563689, eventid=17563688, func_qualifier=1), meadow_Kevent(timestamp=7476363521, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=6740, debugid=17563690, eventid=17563688, func_qualifier=2)]
    meadow_ret_882b45c = list(_name_boundary.attributes(meadow_traces_parser_00afa1e)['feed_generator'](meadow_events_6ffdb54))
    meadow_vm_allocate_trap_432f3b2 = meadow_ret_882b45c[0]
    assert meadow_vm_allocate_trap_432f3b2.target == 515
    assert meadow_vm_allocate_trap_432f3b2.address == 6102721288
    assert meadow_vm_allocate_trap_432f3b2.size == 683936
    assert meadow_vm_allocate_trap_432f3b2.flags == 1

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_9df8c86'}, 'test_msc_kern_mach_vm_purgable_control_trap')
def meadow_test_msc_kern_mach_vm_purgable_control_trap(meadow_traces_parser_9df8c86):
    meadow_events_91cc7d6 = [meadow_Kevent(timestamp=7498028542, data=b'\x03\x02\x00\x00\x00\x00\x00\x00\x00@d\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\xd9\x9do\x01\x00\x00\x00', values=(515, 4335091712, 0, 6167583140), tid=7649, debugid=17563693, eventid=17563692, func_qualifier=1), meadow_Kevent(timestamp=7498028620, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=7649, debugid=17563694, eventid=17563692, func_qualifier=2)]
    meadow_ret_e837260 = list(_name_boundary.attributes(meadow_traces_parser_9df8c86)['feed_generator'](meadow_events_91cc7d6))
    meadow_mach_9820391 = meadow_ret_e837260[0]
    assert meadow_mach_9820391.target == 515
    assert meadow_mach_9820391.address == 4335091712
    assert meadow_mach_9820391.control == 0
    assert meadow_mach_9820391.state == 6167583140

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_905a95b'}, 'test_msc_mach_vm_protect_trap')
def meadow_test_msc_mach_vm_protect_trap(meadow_traces_parser_905a95b):
    meadow_events_56c556f = [meadow_Kevent(timestamp=319993982901, data=b'\x03\x02\x00\x00\x00\x00\x00\x00\x00\xc0@k\x01\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(515, 6094372864, 16384, 0), tid=57703, debugid=17563705, eventid=17563704, func_qualifier=1), meadow_Kevent(timestamp=319993982995, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=57703, debugid=17563706, eventid=17563704, func_qualifier=2)]
    meadow_ret_69b44bf = list(_name_boundary.attributes(meadow_traces_parser_905a95b)['feed_generator'](meadow_events_56c556f))
    meadow_mach_d2e8b36 = meadow_ret_69b44bf[0]
    assert meadow_mach_d2e8b36.target == 515
    assert meadow_mach_d2e8b36.address == 6094372864
    assert meadow_mach_d2e8b36.size == 16384
    assert not meadow_mach_d2e8b36.set_maximum

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_c71e182'}, 'test_msc_mach_vm_map_trap')
def meadow_test_msc_mach_vm_map_trap(meadow_traces_parser_c71e182):
    meadow_events_3dda5e7 = [meadow_Kevent(timestamp=319987780136, data=b'\x03\x02\x00\x00\x00\x00\x00\x00hf\xdbm\x01\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(515, 6138062440, 32768, 0), tid=57808, debugid=17563709, eventid=17563708, func_qualifier=1), meadow_Kevent(timestamp=319987780148, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=57808, debugid=17563710, eventid=17563708, func_qualifier=2)]
    meadow_ret_68ed18c = list(_name_boundary.attributes(meadow_traces_parser_c71e182)['feed_generator'](meadow_events_3dda5e7))
    meadow_mach_36989c6 = meadow_ret_68ed18c[0]
    assert meadow_mach_36989c6.target == 515
    assert meadow_mach_36989c6.address == 6138062440
    assert meadow_mach_36989c6.size == 32768
    assert meadow_mach_36989c6.mask == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_0dd3ba9'}, 'test_msc_mach_reply_port')
def meadow_test_msc_mach_reply_port(meadow_traces_parser_0dd3ba9):
    meadow_events_66a431a = [meadow_Kevent(timestamp=5453890497755, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=941818, debugid=17563753, eventid=17563752, func_qualifier=1), meadow_Kevent(timestamp=5453890497771, data=b'\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(771, 0, 0, 0), tid=941818, debugid=17563754, eventid=17563752, func_qualifier=2)]
    meadow_ret_12142bc = list(_name_boundary.attributes(meadow_traces_parser_0dd3ba9)['feed_generator'](meadow_events_66a431a))
    meadow_mach_3c0de1f = meadow_ret_12142bc[0]
    assert meadow_mach_3c0de1f.result == 771

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_c2d0ed5'}, 'test_msc_thread_self_trap')
def meadow_test_msc_thread_self_trap(meadow_traces_parser_c2d0ed5):
    meadow_events_10df422 = [meadow_Kevent(timestamp=5453890560892, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=941536, debugid=17563757, eventid=17563756, func_qualifier=1), meadow_Kevent(timestamp=5453890560912, data=b'\x0b\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(42507, 0, 0, 0), tid=941536, debugid=17563758, eventid=17563756, func_qualifier=2)]
    meadow_ret_e8c2f11 = list(_name_boundary.attributes(meadow_traces_parser_c2d0ed5)['feed_generator'](meadow_events_10df422))
    meadow_mach_9547d20 = meadow_ret_e8c2f11[0]
    assert meadow_mach_9547d20.result == 42507

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_0e9573e'}, 'test_msc_task_self_trap')
def meadow_test_msc_task_self_trap(meadow_traces_parser_0e9573e):
    meadow_events_16a85fb = [meadow_Kevent(timestamp=5453890600244, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=941827, debugid=17563761, eventid=17563760, func_qualifier=1), meadow_Kevent(timestamp=5453890600265, data=b'\x03\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(515, 0, 0, 0), tid=941827, debugid=17563762, eventid=17563760, func_qualifier=2)]
    meadow_ret_34934e2 = list(_name_boundary.attributes(meadow_traces_parser_0e9573e)['feed_generator'](meadow_events_16a85fb))
    meadow_mach_590ba47 = meadow_ret_34934e2[0]
    assert meadow_mach_590ba47.result == 515

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_07f66a8'}, 'test_msc_mach_port_unguard_trap')
def meadow_test_msc_mach_port_unguard_trap(meadow_traces_parser_07f66a8):
    meadow_events_e14d1e0 = [meadow_Kevent(timestamp=5453890742696, data=b'\x03\x02\x00\x00\x00\x00\x00\x00\x03\x8e\n\x00\x00\x00\x00\x000j\xd2G\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(515, 691715, 5499939376, 0), tid=941734, debugid=17563817, eventid=17563816, func_qualifier=1), meadow_Kevent(timestamp=5453890742704, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=941734, debugid=17563818, eventid=17563816, func_qualifier=2)]
    meadow_ret_5bdc73d = list(_name_boundary.attributes(meadow_traces_parser_07f66a8)['feed_generator'](meadow_events_e14d1e0))
    meadow_mach_3433233 = meadow_ret_5bdc73d[0]
    assert meadow_mach_3433233.target == 515
    assert _name_boundary.attributes(meadow_mach_3433233)['name'] == 691715
    assert meadow_mach_3433233.guard == 5499939376

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_276cf9e'}, 'test_msc_mach_timebase_info')
def meadow_test_msc_mach_timebase_info(meadow_traces_parser_276cf9e):
    meadow_events_b106a2c = [meadow_Kevent(timestamp=5453890643526, data=b'\xc4F\n\x0e\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(8825489092, 0, 0, 0), tid=941827, debugid=17564005, eventid=17564004, func_qualifier=1), meadow_Kevent(timestamp=5453890643529, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=941827, debugid=17564006, eventid=17564004, func_qualifier=2)]
    meadow_ret_45a4348 = list(_name_boundary.attributes(meadow_traces_parser_276cf9e)['feed_generator'](meadow_events_b106a2c))
    meadow_mach_64163b9 = meadow_ret_45a4348[0]
    assert meadow_mach_64163b9.info == 8825489092

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_df27362'}, 'test_mach_vmfault')
def meadow_test_mach_vmfault(meadow_traces_parser_df27362):
    meadow_events_91c15b5 = [meadow_Kevent(timestamp=10533581994269, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x99k\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(1, 6100205568, 0, 0), tid=876421, debugid=19922953, eventid=19922952, func_qualifier=1), meadow_Kevent(timestamp=10533581994584, data=b'\x00\xc0\x99k\x01\x00\x00\x00\x01\x03\x1e\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x00\x00\x00', values=(6100205568, 1966849, 524288, 95), tid=876421, debugid=20054024, eventid=20054024, func_qualifier=0), meadow_Kevent(timestamp=10533581994616, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x99k\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00', values=(1, 6100205568, 0, 1), tid=876421, debugid=19922954, eventid=19922952, func_qualifier=2)]
    meadow_ret_2e205fd = list(_name_boundary.attributes(meadow_traces_parser_df27362)['feed_generator'](meadow_events_91c15b5))
    meadow_fault_906d431 = meadow_ret_2e205fd[1]
    assert meadow_fault_906d431.addr == 6100205568
    assert not meadow_fault_906d431.is_kernel
    assert meadow_fault_906d431.result == 0
    assert meadow_fault_906d431.fault_type == meadow_DbgVmFaultType.DBG_ZERO_FILL_FAULT
    assert meadow_fault_906d431.pid == 95
    assert meadow_fault_906d431.caller_prot == [meadow_VmProtection.VM_PROT_READ, meadow_VmProtection.VM_PROT_WRITE]

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_cb4789d'}, 'test_mach_vmfault_no_real_address')
def meadow_test_mach_vmfault_no_real_address(meadow_traces_parser_cb4789d):
    meadow_events_1ec50e7 = [meadow_Kevent(timestamp=10533581994269, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x99k\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(1, 6100205568, 0, 0), tid=876421, debugid=19922953, eventid=19922952, func_qualifier=1), meadow_Kevent(timestamp=10533581994616, data=b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x99k\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00', values=(1, 6100205568, 0, 1), tid=876421, debugid=19922954, eventid=19922952, func_qualifier=2)]
    meadow_ret_7068383 = list(_name_boundary.attributes(meadow_traces_parser_cb4789d)['feed_generator'](meadow_events_1ec50e7))
    meadow_fault_d583056 = meadow_ret_7068383[0]
    assert meadow_fault_d583056.addr == 6100205568
    assert not meadow_fault_d583056.is_kernel
    assert meadow_fault_d583056.result == 0
    assert meadow_fault_d583056.fault_type == meadow_DbgVmFaultType.DBG_ZERO_FILL_FAULT
    assert meadow_fault_d583056.pid is None
    assert meadow_fault_d583056.caller_prot is None

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_d8dc8ae'}, 'test_mach_sched')
def meadow_test_mach_sched(meadow_traces_parser_d8dc8ae):
    meadow_events_77fbd43 = [meadow_Kevent(timestamp=4580000449861, data=b'\x01\x00\x00\x00\x00\x00\x00\x00o\x02\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00\x00\x00\x00\x00', values=(1, 623, 4, 81), tid=387391, debugid=20971520, eventid=20971520, func_qualifier=0)]
    meadow_ret_7b9ad4f = list(_name_boundary.attributes(meadow_traces_parser_d8dc8ae)['feed_generator'](meadow_events_77fbd43))
    meadow_sched_ad76b94 = meadow_ret_7b9ad4f[0]
    assert meadow_sched_ad76b94.reason == [meadow_AsynchronousSystemTrapsReason.AST_PREEMPT]
    assert meadow_sched_ad76b94.to == 623
    assert meadow_sched_ad76b94.from_sched_pri == 4
    assert meadow_sched_ad76b94.to_sched_pri == 81

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_ed0a4b2'}, 'test_mach_stkhandoff')
def meadow_test_mach_stkhandoff(meadow_traces_parser_ed0a4b2):
    meadow_events_1a483ea = [meadow_Kevent(timestamp=3897242679331, data=b'\x05\x00\x00\x00\x00\x00\x00\x00w\xf5\x04\x00\x00\x00\x00\x007\x00\x00\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x00', values=(5, 324983, 55, 63), tid=2761, debugid=20971528, eventid=20971528, func_qualifier=0)]
    meadow_ret_fd200e6 = list(_name_boundary.attributes(meadow_traces_parser_ed0a4b2)['feed_generator'](meadow_events_1a483ea))
    meadow_handoff_f8d73ec = meadow_ret_fd200e6[0]
    assert meadow_handoff_f8d73ec.from_ == 2761
    assert meadow_handoff_f8d73ec.to == 324983
    assert meadow_handoff_f8d73ec.reason == [meadow_AsynchronousSystemTrapsReason.AST_PREEMPT, meadow_AsynchronousSystemTrapsReason.AST_URGENT]
    assert meadow_handoff_f8d73ec.from_sched_pri == 55
    assert meadow_handoff_f8d73ec.to_sched_pri == 63

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_fea722a'}, 'test_mach_mkrunnable')
def meadow_test_mach_mkrunnable(meadow_traces_parser_fea722a):
    meadow_events_b426d23 = [meadow_Kevent(timestamp=9982171649633, data=b'\xb7\x01\x00\x00\x00\x00\x00\x00Q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00', values=(439, 81, 0, 8), tid=261, debugid=20971544, eventid=20971544, func_qualifier=0)]
    meadow_ret_56f308c = list(_name_boundary.attributes(meadow_traces_parser_fea722a)['feed_generator'](meadow_events_b426d23))
    meadow_mkrunnable_0abc867 = meadow_ret_56f308c[0]
    assert meadow_mkrunnable_0abc867.tid == 439
    assert meadow_mkrunnable_0abc867.sched_pri == 81
    assert meadow_mkrunnable_0abc867.wait_result == 0
    assert meadow_mkrunnable_0abc867.runnable_threads == 8

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_f08f313'}, 'test_mach_idle')
def meadow_test_mach_idle(meadow_traces_parser_f08f313):
    meadow_events_a6df8d8 = [meadow_Kevent(timestamp=10071358928388, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 0), tid=332, debugid=20971557, eventid=20971556, func_qualifier=1), meadow_Kevent(timestamp=10071358928416, data=b'\xa4\xb1\x0c\x00\x00\x00\x00\x00\xf1\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(831908, 241, 3, 0), tid=332, debugid=27852808, eventid=27852808, func_qualifier=0), meadow_Kevent(timestamp=10071358928432, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\xa4\xb1\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 6, 831908, 0), tid=332, debugid=20971558, eventid=20971556, func_qualifier=2)]
    meadow_ret_5052645 = list(_name_boundary.attributes(meadow_traces_parser_f08f313)['feed_generator'](meadow_events_a6df8d8))
    meadow_idle_d964b3b = meadow_ret_5052645[1]
    assert meadow_idle_d964b3b.from_ == 0
    assert meadow_idle_d964b3b.process_state == meadow_ProcessState.PROCESSOR_RUNNING
    assert meadow_idle_d964b3b.to == 831908
    assert meadow_idle_d964b3b.reason == [meadow_AsynchronousSystemTrapsReason.AST_NONE]

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_fa65e1b'}, 'test_mach_block')
def meadow_test_mach_block(meadow_traces_parser_fa65e1b):
    meadow_events_97fe99b = [meadow_Kevent(timestamp=4643561352579, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x98\x92n\x07\xf0\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(0, 18446744005114761880, 0, 0), tid=883, debugid=20971580, eventid=20971580, func_qualifier=0)]
    meadow_ret_575ceb0 = list(_name_boundary.attributes(meadow_traces_parser_fa65e1b)['feed_generator'](meadow_events_97fe99b))
    meadow_block_f54bcc1 = meadow_ret_575ceb0[0]
    assert meadow_block_f54bcc1.reason == [meadow_AsynchronousSystemTrapsReason.AST_NONE]
    assert meadow_block_f54bcc1.continuation == 18446744005114761880

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_f2c10e9'}, 'test_mach_wait')
def meadow_test_mach_wait(meadow_traces_parser_f2c10e9):
    meadow_events_418baf0 = [meadow_Kevent(timestamp=4365975502717, data=b'\x19\x99\xe5<\xfb\xd5\xa0u\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(8476009773746460953, 0, 0, 0), tid=884, debugid=20971584, eventid=20971584, func_qualifier=0)]
    meadow_ret_29dff3c = list(_name_boundary.attributes(meadow_traces_parser_f2c10e9)['feed_generator'](meadow_events_418baf0))
    meadow_wait_a78280d = meadow_ret_29dff3c[0]
    assert meadow_wait_a78280d.event == 8476009773746460953

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_a1695dd'}, 'test_mach_dispatch')
def meadow_test_mach_dispatch(meadow_traces_parser_a1695dd):
    meadow_events_5864cb6 = [meadow_Kevent(timestamp=4440978834382, data=b'L\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00', values=(332, 0, 132, 3), tid=261, debugid=20971648, eventid=20971648, func_qualifier=0)]
    meadow_ret_af5b154 = list(_name_boundary.attributes(meadow_traces_parser_a1695dd)['feed_generator'](meadow_events_5864cb6))
    meadow_dispatch_b1f1b8c = meadow_ret_af5b154[0]
    assert meadow_dispatch_b1f1b8c.tid == 332
    assert meadow_dispatch_b1f1b8c.reason == [meadow_AsynchronousSystemTrapsReason.AST_NONE]
    assert meadow_dispatch_b1f1b8c.state == [meadow_ThreadState.TH_RUN, meadow_ThreadState.TH_IDLE]
    assert meadow_dispatch_b1f1b8c.runnable_threads == 3

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_87fdba8'}, 'test_thread_group_set')
def meadow_test_thread_group_set(meadow_traces_parser_87fdba8):
    meadow_events_de35829 = [meadow_Kevent(timestamp=10566859835989, data=b'\xff\xff\xff\xff\xff\xff\xff\xff>\x00\x00\x00\x00\x00\x00\x00\xf6l\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(18446744073709551615, 62, 879862, 0), tid=879802, debugid=27656200, eventid=27656200, func_qualifier=0)]
    meadow_ret_93c434a = list(_name_boundary.attributes(meadow_traces_parser_87fdba8)['feed_generator'](meadow_events_de35829))
    meadow_group_set_3b833de = meadow_ret_93c434a[0]
    assert meadow_group_set_3b833de.current_tgid == -1
    assert meadow_group_set_3b833de.target_tgid == 62
    assert meadow_group_set_3b833de.tid == 879862
    assert meadow_group_set_3b833de.home_tgid == 0

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_d16885b'}, 'test_sched_clutch_cpu_thread_select')
def meadow_test_sched_clutch_cpu_thread_select(meadow_traces_parser_d16885b):
    meadow_events_1cf37eb = [meadow_Kevent(timestamp=4387224443080, data=b'\xa7\xa7\x05\x00\x00\x00\x00\x00\xf1\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', values=(370599, 241, 1, 0), tid=597, debugid=27852808, eventid=27852808, func_qualifier=0)]
    meadow_ret_e2c7736 = list(_name_boundary.attributes(meadow_traces_parser_d16885b)['feed_generator'](meadow_events_1cf37eb))
    meadow_select_0e1c7dd = meadow_ret_e2c7736[0]
    assert meadow_select_0e1c7dd.tid == 370599
    assert meadow_select_0e1c7dd.tgid == 241
    assert meadow_select_0e1c7dd.scb_bucket == 1

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_9c4ddec'}, 'test_sched_clutch_tg_bucket_pri')
def meadow_test_sched_clutch_tg_bucket_pri(meadow_traces_parser_9c4ddec):
    meadow_events_583d807 = [meadow_Kevent(timestamp=4517075147289, data=b'/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00C\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00', values=(47, 0, 67, 16), tid=261, debugid=27852816, eventid=27852816, func_qualifier=0)]
    meadow_ret_85256cc = list(_name_boundary.attributes(meadow_traces_parser_9c4ddec)['feed_generator'](meadow_events_583d807))
    meadow_pri_5c3f67e = meadow_ret_85256cc[0]
    assert meadow_pri_5c3f67e.tgid == 47
    assert meadow_pri_5c3f67e.scb_bucket == 0
    assert meadow_pri_5c3f67e.priority == 67
    assert meadow_pri_5c3f67e.interactive_score == 16
_name_boundary.module_contract(globals(), {'test_mach_idle': 'meadow_test_mach_idle', 'test_decr_set': 'meadow_test_decr_set', 'test_msc_mach_vm_allocate_trap': 'meadow_test_msc_mach_vm_allocate_trap', 'test_sched_clutch_tg_bucket_pri': 'meadow_test_sched_clutch_tg_bucket_pri', 'test_mach_wait': 'meadow_test_mach_wait', 'test_msc_thread_self_trap': 'meadow_test_msc_thread_self_trap', 'test_kernel_data_abort_same_el_exc_arm': 'meadow_test_kernel_data_abort_same_el_exc_arm', 'test_thread_group_set': 'meadow_test_thread_group_set', 'test_mach_dispatch': 'meadow_test_mach_dispatch', 'test_msc_kern_mach_vm_purgable_control_trap': 'meadow_test_msc_kern_mach_vm_purgable_control_trap', 'test_msc_mach_reply_port': 'meadow_test_msc_mach_reply_port', 'test_mach_vmfault': 'meadow_test_mach_vmfault', 'ThreadState': 'meadow_ThreadState', 'Kevent': 'meadow_Kevent', 'test_msc_mach_timebase_info': 'meadow_test_msc_mach_timebase_info', 'ProcessState': 'meadow_ProcessState', 'test_msc_task_self_trap': 'meadow_test_msc_task_self_trap', 'AsynchronousSystemTrapsReason': 'meadow_AsynchronousSystemTrapsReason', 'DbgVmFaultType': 'meadow_DbgVmFaultType', 'test_mach_sched': 'meadow_test_mach_sched', 'test_mach_block': 'meadow_test_mach_block', 'test_mach_mkrunnable': 'meadow_test_mach_mkrunnable', 'test_msc_mach_vm_map_trap': 'meadow_test_msc_mach_vm_map_trap', 'test_user_data_abort_lower_el_exc_arm': 'meadow_test_user_data_abort_lower_el_exc_arm', 'test_sched_clutch_cpu_thread_select': 'meadow_test_sched_clutch_cpu_thread_select', 'test_mach_vmfault_no_real_address': 'meadow_test_mach_vmfault_no_real_address', 'test_msc_mach_port_unguard_trap': 'meadow_test_msc_mach_port_unguard_trap', 'VmProtection': 'meadow_VmProtection', 'test_decr_trap': 'meadow_test_decr_trap', 'test_interrupt': 'meadow_test_interrupt', 'test_mach_stkhandoff': 'meadow_test_mach_stkhandoff', 'test_msc_mach_vm_protect_trap': 'meadow_test_msc_mach_vm_protect_trap'})
