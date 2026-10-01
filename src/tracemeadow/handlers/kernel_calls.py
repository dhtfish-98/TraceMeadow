# Derived from pykdebugparser/trace_handlers/mach.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import ctypes as meadow_ctypes
from dataclasses import dataclass as meadow_dataclass
from enum import Enum as meadow_Enum
from functools import partial as meadow_partial
from typing import List as meadow_List

@_name_boundary.class_contract('AsynchronousSystemTrapsReason', {})
class meadow_AsynchronousSystemTrapsReason(meadow_Enum):
    AST_NONE = 0
    AST_PREEMPT = 1
    AST_QUANTUM = 2
    AST_URGENT = 4
    AST_HANDOFF = 8
    AST_YIELD = 16
    AST_APC = 32
    AST_LEDGER = 64
    AST_BSD = 128
    AST_KPERF = 256
    AST_MACF = 512
    AST_RESET_PCS = 1024
    AST_ARCADE = 2048
    AST_GUARD = 4096
    AST_TELEMETRY_USER = 8192
    AST_TELEMETRY_KERNEL = 16384
    AST_TELEMETRY_PMI = 32768
    AST_SFI = 65536
    AST_DTRACE = 131072
    AST_TELEMETRY_IO = 262144
    AST_KEVENT = 524288
    AST_REBALANCE = 1048576
    AST_UNQUIESCE = 2097152

@_name_boundary.callable_contract({'flags': 'meadow_flags_b4fc498'}, 'to_ast_reasons')
def meadow_to_ast_reasons(meadow_flags_b4fc498: int):
    if not meadow_flags_b4fc498:
        return [meadow_AsynchronousSystemTrapsReason.AST_NONE]
    else:
        return [meadow_r_5f80015 for meadow_r_5f80015 in meadow_AsynchronousSystemTrapsReason if meadow_r_5f80015.value & meadow_flags_b4fc498]
meadow_ESR_EC_SHIFT = 26

@_name_boundary.class_contract('ExceptionSyndromeRegisterClass', {})
class meadow_ExceptionSyndromeRegisterClass(meadow_Enum):
    ESR_EC_UNCATEGORIZED = 0
    ESR_EC_WFI_WFE = 1
    ESR_EC_MCR_MRC_CP15_TRAP = 3
    ESR_EC_MCRR_MRRC_CP15_TRAP = 4
    ESR_EC_MCR_MRC_CP14_TRAP = 5
    ESR_EC_LDC_STC_CP14_TRAP = 6
    ESR_EC_TRAP_SIMD_FP = 7
    ESR_EC_PTRAUTH_INSTR_TRAP = 9
    ESR_EC_MCRR_MRRC_CP14_TRAP = 12
    ESR_EC_ILLEGAL_INSTR_SET = 14
    ESR_EC_SVC_32 = 17
    ESR_EC_SVC_64 = 21
    ESR_EC_MSR_TRAP = 24
    ESR_EC_IABORT_EL0 = 32
    ESR_EC_IABORT_EL1 = 33
    ESR_EC_PC_ALIGN = 34
    ESR_EC_DABORT_EL0 = 36
    ESR_EC_DABORT_EL1 = 37
    ESR_EC_SP_ALIGN = 38
    ESR_EC_FLOATING_POINT_32 = 40
    ESR_EC_FLOATING_POINT_64 = 44
    ESR_EC_BKPT_REG_MATCH_EL0 = 48
    ESR_EC_BKPT_REG_MATCH_EL1 = 49
    ESR_EC_SW_STEP_DEBUG_EL0 = 50
    ESR_EC_SW_STEP_DEBUG_EL1 = 51
    ESR_EC_WATCHPT_MATCH_EL0 = 52
    ESR_EC_WATCHPT_MATCH_EL1 = 53
    ESR_EC_BKPT_AARCH32 = 56
    ESR_EC_BRK_AARCH64 = 60

@_name_boundary.class_contract('ThreadState', {})
class meadow_ThreadState(meadow_Enum):
    TH_WAIT = 1
    TH_SUSP = 2
    TH_RUN = 4
    TH_UNINT = 8
    TH_TERMINATE = 16
    TH_TERMINATE2 = 32
    TH_WAIT_REPORT = 64
    TH_IDLE = 128

@_name_boundary.callable_contract({'flags': 'meadow_flags_d933e5a'}, 'to_thread_state')
def meadow_to_thread_state(meadow_flags_d933e5a: int):
    return [meadow_s_93951f5 for meadow_s_93951f5 in meadow_ThreadState if meadow_s_93951f5.value & meadow_flags_d933e5a]

@_name_boundary.class_contract('InterruptType', {})
class meadow_InterruptType(meadow_Enum):
    DBG_INTR_TYPE_UNKNOWN = 0
    DBG_INTR_TYPE_IPI = 1
    DBG_INTR_TYPE_TIMER = 2
    DBG_INTR_TYPE_OTHER = 3
    DBG_INTR_TYPE_PMI = 4

@_name_boundary.class_contract('ProcessState', {})
class meadow_ProcessState(meadow_Enum):
    PROCESSOR_OFF_LINE = 0
    PROCESSOR_SHUTDOWN = 1
    PROCESSOR_START = 2
    PROCESSOR_UNUSED = 3
    PROCESSOR_IDLE = 4
    PROCESSOR_DISPATCHING = 5
    PROCESSOR_RUNNING = 6

@_name_boundary.class_contract('DbgVmFaultType', {})
class meadow_DbgVmFaultType(meadow_Enum):
    DBG_ZERO_FILL_FAULT = 1
    DBG_PAGEIN_FAULT = 2
    DBG_COW_FAULT = 3
    DBG_CACHE_HIT_FAULT = 4
    DBG_NZF_PAGE_FAULT = 5
    DBG_GUARD_FAULT = 6
    DBG_PAGEINV_FAULT = 7
    DBG_PAGEIND_FAULT = 8
    DBG_COMPRESSOR_FAULT = 9
    DBG_COMPRESSOR_SWAPIN_FAULT = 10
    DBG_COR_FAULT = 11

@_name_boundary.class_contract('VmProtection', {})
class meadow_VmProtection(meadow_Enum):
    VM_PROT_NONE = 0
    VM_PROT_READ = 1
    VM_PROT_WRITE = 2
    VM_PROT_EXECUTE = 4
    VM_PROT_NO_CHANGE = 8
    VM_PROT_COPY = 16
    VM_PROT_TRUSTED = 32
    VM_PROT_IS_MASK = 64
    VM_PROT_STRIP_READ = 128

@_name_boundary.callable_contract({'flags': 'meadow_flags_c7ec5eb'}, 'to_vm_prot')
def meadow_to_vm_prot(meadow_flags_c7ec5eb: int):
    if not meadow_flags_c7ec5eb:
        return [meadow_VmProtection.VM_PROT_NONE]
    else:
        return [meadow_p_645c68f for meadow_p_645c68f in meadow_VmProtection if meadow_p_645c68f.value & meadow_flags_c7ec5eb]

@_name_boundary.class_contract('MachPortRight', {})
class meadow_MachPortRight(meadow_Enum):
    MACH_PORT_RIGHT_SEND = 0
    MACH_PORT_RIGHT_RECEIVE = 1
    MACH_PORT_RIGHT_SEND_ONCE = 2
    MACH_PORT_RIGHT_PORT_SET = 3
    MACH_PORT_RIGHT_DEAD_NAME = 4
    MACH_PORT_RIGHT_NUMBER = 5

@_name_boundary.class_contract('MachMsgTypeName', {})
class meadow_MachMsgTypeName(meadow_Enum):
    MACH_MSG_TYPE_MOVE_RECEIVE = 16
    MACH_MSG_TYPE_MOVE_SEND = 17
    MACH_MSG_TYPE_MOVE_SEND_ONCE = 18
    MACH_MSG_TYPE_COPY_SEND = 19
    MACH_MSG_TYPE_MAKE_SEND = 20
    MACH_MSG_TYPE_MAKE_SEND_ONCE = 21
    MACH_MSG_TYPE_COPY_RECEIVE = 22

@_name_boundary.class_contract('KernReturn', {})
class meadow_KernReturn(meadow_Enum):
    KERN_SUCCESS = 0
    KERN_INVALID_ADDRESS = 1
    KERN_PROTECTION_FAILURE = 2
    KERN_NO_SPACE = 3
    KERN_INVALID_ARGUMENT = 4
    KERN_FAILURE = 5
    KERN_RESOURCE_SHORTAGE = 6
    KERN_NOT_RECEIVER = 7
    KERN_NO_ACCESS = 8
    KERN_MEMORY_FAILURE = 9
    KERN_MEMORY_ERROR = 10
    KERN_ALREADY_IN_SET = 11
    KERN_NOT_IN_SET = 12
    KERN_NAME_EXISTS = 13
    KERN_ABORTED = 14
    KERN_INVALID_NAME = 15
    KERN_INVALID_TASK = 16
    KERN_INVALID_RIGHT = 17
    KERN_INVALID_VALUE = 18
    KERN_UREFS_OVERFLOW = 19
    KERN_INVALID_CAPABILITY = 20
    KERN_RIGHT_EXISTS = 21
    KERN_INVALID_HOST = 22
    KERN_MEMORY_PRESENT = 23
    KERN_MEMORY_DATA_MOVED = 24
    KERN_MEMORY_RESTART_COPY = 25
    KERN_INVALID_PROCESSOR_SET = 26
    KERN_POLICY_LIMIT = 27
    KERN_INVALID_POLICY = 28
    KERN_INVALID_OBJECT = 29
    KERN_ALREADY_WAITING = 30
    KERN_DEFAULT_SET = 31
    KERN_EXCEPTION_PROTECTED = 32
    KERN_INVALID_LEDGER = 33
    KERN_INVALID_MEMORY_CONTROL = 34
    KERN_INVALID_SECURITY = 35
    KERN_NOT_DEPRESSED = 36
    KERN_TERMINATED = 37
    KERN_LOCK_SET_DESTROYED = 38
    KERN_LOCK_UNSTABLE = 39
    KERN_LOCK_OWNED = 40
    KERN_LOCK_OWNED_SELF = 41
    KERN_SEMAPHORE_DESTROYED = 42
    KERN_RPC_SERVER_TERMINATED = 43
    KERN_RPC_TERMINATE_ORPHAN = 44
    KERN_RPC_CONTINUE_ORPHAN = 45
    KERN_NOT_SUPPORTED = 46
    KERN_NODE_DOWN = 47
    KERN_NOT_WAITING = 48
    KERN_OPERATION_TIMED_OUT = 49
    KERN_CODESIGN_ERROR = 50
    KERN_POLICY_STATIC = 51
    KERN_INSUFFICIENT_BUFFER_SIZE = 52
    KERN_DENIED = 53

@_name_boundary.class_contract('MachPortFlavor', {})
class meadow_MachPortFlavor(meadow_Enum):
    MACH_PORT_LIMITS_INFO = 1
    MACH_PORT_RECEIVE_STATUS = 2
    MACH_PORT_DNREQUESTS_SIZE = 3
    MACH_PORT_TEMPOWNER = 4
    MACH_PORT_IMPORTANCE_RECEIVER = 5
    MACH_PORT_DENAP_RECEIVER = 6
    MACH_PORT_INFO_EXT = 7

@_name_boundary.class_contract('SwitchOption', {})
class meadow_SwitchOption(meadow_Enum):
    SWITCH_OPTION_NONE = 0
    SWITCH_OPTION_DEPRESS = 1
    SWITCH_OPTION_WAIT = 2
    SWITCH_OPTION_DISPATCH_CONTENTION = 3
    SWITCH_OPTION_OSLOCK_DEPRESS = 4
    SWITCH_OPTION_OSLOCK_WAIT = 5

@_name_boundary.class_contract('MkTimerFlags', {})
class meadow_MkTimerFlags(meadow_Enum):
    MK_TIMER_NORMAL = 0
    MK_TIMER_CRITICAL = 1

@_name_boundary.class_contract('KernelUncategorizedExcArm', {})
@meadow_dataclass
class meadow_KernelUncategorizedExcArm:
    ktraces: meadow_List
    esr: int
    far: int
    pc: int

    @_name_boundary.callable_contract({'self': 'meadow_self_2b3d87b'}, '__str__')
    def __str__(meadow_self_2b3d87b):
        meadow_esr_class_0f8b5b5 = meadow_self_2b3d87b.esr >> 26
        try:
            meadow_esr_class_0f8b5b5 = _name_boundary.attributes(meadow_ExceptionSyndromeRegisterClass(meadow_esr_class_0f8b5b5))['name']
        except ValueError:
            pass
        return f'KernelUncategorizedExcArm, class: {meadow_esr_class_0f8b5b5}, far: {hex(meadow_self_2b3d87b.far)}, pc: {hex(meadow_self_2b3d87b.pc)}'

@_name_boundary.class_contract('KernelDataAbortSameElExcArm', {})
@meadow_dataclass
class meadow_KernelDataAbortSameElExcArm:
    ktraces: meadow_List
    esr: int
    far: int
    pc: int

    @_name_boundary.callable_contract({'self': 'meadow_self_4674ba5'}, '__str__')
    def __str__(meadow_self_4674ba5):
        meadow_esr_class_8218796 = meadow_self_4674ba5.esr >> 26
        try:
            meadow_esr_class_8218796 = _name_boundary.attributes(meadow_ExceptionSyndromeRegisterClass(meadow_esr_class_8218796))['name']
        except ValueError:
            pass
        return f'Kernel_Data_Abort_Same_EL_Exc_ARM, class: {meadow_esr_class_8218796}, far: {hex(meadow_self_4674ba5.far)}, pc: {hex(meadow_self_4674ba5.pc)}'

@_name_boundary.class_contract('UserSvc64ExcArm', {})
@meadow_dataclass
class meadow_UserSvc64ExcArm:
    ktraces: meadow_List
    esr: int
    far: int
    pc: int

    @_name_boundary.callable_contract({'self': 'meadow_self_17f0e3a'}, '__str__')
    def __str__(meadow_self_17f0e3a):
        meadow_esr_class_e03076f = meadow_self_17f0e3a.esr >> 26
        try:
            meadow_esr_class_e03076f = _name_boundary.attributes(meadow_ExceptionSyndromeRegisterClass(meadow_esr_class_e03076f))['name']
        except ValueError:
            pass
        return f'User_SVC64_Exc_ARM, class: {meadow_esr_class_e03076f}, far: {hex(meadow_self_17f0e3a.far)}, pc: {hex(meadow_self_17f0e3a.pc)}'

@_name_boundary.class_contract('Interrupt', {})
@meadow_dataclass
class meadow_Interrupt:
    ktraces: meadow_List
    pc: int
    is_user: bool
    type: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ab9be4c'}, '__str__')
    def __str__(meadow_self_ab9be4c):
        return f"INTERRUPT, pc: {hex(meadow_self_ab9be4c.pc)}, is_user: {meadow_self_ab9be4c.is_user}, type: {_name_boundary.attributes(meadow_InterruptType(meadow_self_ab9be4c.type))['name']}"

@_name_boundary.class_contract('UserInstrAbortLowerElExcArm', {})
@meadow_dataclass
class meadow_UserInstrAbortLowerElExcArm:
    ktraces: meadow_List
    esr: int
    far: int
    pc: int

    @_name_boundary.callable_contract({'self': 'meadow_self_943cb0b'}, '__str__')
    def __str__(meadow_self_943cb0b):
        meadow_esr_class_4eccbbe = meadow_self_943cb0b.esr >> 26
        try:
            meadow_esr_class_4eccbbe = _name_boundary.attributes(meadow_ExceptionSyndromeRegisterClass(meadow_esr_class_4eccbbe))['name']
        except ValueError:
            pass
        return f'User_Instr_Abort_Lower_EL_Exc_ARM, class: {meadow_esr_class_4eccbbe}, far: {hex(meadow_self_943cb0b.far)}, pc: {hex(meadow_self_943cb0b.pc)}'

@_name_boundary.class_contract('UserDataAbortLowerElExcArm', {})
@meadow_dataclass
class meadow_UserDataAbortLowerElExcArm:
    ktraces: meadow_List
    esr: int
    far: int
    pc: int

    @_name_boundary.callable_contract({'self': 'meadow_self_de8f095'}, '__str__')
    def __str__(meadow_self_de8f095):
        meadow_esr_class_ec5dbb0 = meadow_self_de8f095.esr >> 26
        try:
            meadow_esr_class_ec5dbb0 = _name_boundary.attributes(meadow_ExceptionSyndromeRegisterClass(meadow_esr_class_ec5dbb0))['name']
        except ValueError:
            pass
        return f'User_Data_Abort_Lower_EL_Exc_ARM, class: {meadow_esr_class_ec5dbb0}, far: {hex(meadow_self_de8f095.far)}, pc: {hex(meadow_self_de8f095.pc)}'

@_name_boundary.class_contract('DecrTrap', {})
@meadow_dataclass
class meadow_DecrTrap:
    ktraces: meadow_List
    latency: int
    pc: int
    user_mode: bool

    @_name_boundary.callable_contract({'self': 'meadow_self_ec649b8'}, '__str__')
    def __str__(meadow_self_ec649b8):
        return f'DecrTrap, latency: {meadow_self_ec649b8.latency}, pc: {hex(meadow_self_ec649b8.pc)}, user_mode: {meadow_self_ec649b8.user_mode}'

@_name_boundary.class_contract('DecrSet', {})
@meadow_dataclass
class meadow_DecrSet:
    ktraces: meadow_List
    decr: int
    deadline: int
    queue_count: int

    @_name_boundary.callable_contract({'self': 'meadow_self_bcc2607'}, '__str__')
    def __str__(meadow_self_bcc2607):
        return f'DecrSet, decr: {meadow_self_bcc2607.decr}'

@_name_boundary.class_contract('MachVmAllocate', {})
@meadow_dataclass
class meadow_MachVmAllocate:
    ktraces: meadow_List
    target: int
    address: int
    size: int
    flags: int

    @_name_boundary.callable_contract({'self': 'meadow_self_a0d2013'}, '__str__')
    def __str__(meadow_self_a0d2013):
        return f'mach_vm_allocate({meadow_self_a0d2013.target}, {hex(meadow_self_a0d2013.address)}, {hex(meadow_self_a0d2013.size)}, {hex(meadow_self_a0d2013.flags)})'

@_name_boundary.class_contract('MachVmPurgableControl', {})
@meadow_dataclass
class meadow_MachVmPurgableControl:
    ktraces: meadow_List
    target: int
    address: int
    control: int
    state: int

    @_name_boundary.callable_contract({'self': 'meadow_self_850fdb8'}, '__str__')
    def __str__(meadow_self_850fdb8):
        return f'mach_vm_purgable_control({meadow_self_850fdb8.target}, {hex(meadow_self_850fdb8.address)}, {meadow_self_850fdb8.control}, {hex(meadow_self_850fdb8.state)})'

@_name_boundary.class_contract('MachVmDeallocate', {})
@meadow_dataclass
class meadow_MachVmDeallocate:
    ktraces: meadow_List
    target: int
    address: int
    size: int

    @_name_boundary.callable_contract({'self': 'meadow_self_7df4851'}, '__str__')
    def __str__(meadow_self_7df4851):
        return f'mach_vm_deallocate({meadow_self_7df4851.target}, {hex(meadow_self_7df4851.address)}, {hex(meadow_self_7df4851.size)})'

@_name_boundary.class_contract('MachVmProtect', {})
@meadow_dataclass
class meadow_MachVmProtect:
    ktraces: meadow_List
    target: int
    address: int
    size: int
    set_maximum: bool

    @_name_boundary.callable_contract({'self': 'meadow_self_f5fc9e8'}, '__str__')
    def __str__(meadow_self_f5fc9e8):
        return f'mach_vm_protect({meadow_self_f5fc9e8.target}, {hex(meadow_self_f5fc9e8.address)}, {hex(meadow_self_f5fc9e8.size)}, {str(meadow_self_f5fc9e8.set_maximum).lower()})'

@_name_boundary.class_contract('MachVmMap', {})
@meadow_dataclass
class meadow_MachVmMap:
    ktraces: meadow_List
    target: int
    address: int
    size: int
    mask: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ccd6a59'}, '__str__')
    def __str__(meadow_self_ccd6a59):
        return f'mach_vm_map({meadow_self_ccd6a59.target}, {hex(meadow_self_ccd6a59.address)}, {hex(meadow_self_ccd6a59.size)}, {hex(meadow_self_ccd6a59.mask)})'

@_name_boundary.class_contract('MachPortAllocate', {})
@meadow_dataclass
class meadow_MachPortAllocate:
    ktraces: meadow_List
    target: int
    right: meadow_MachPortRight
    name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_53ed572'}, '__str__')
    def __str__(meadow_self_53ed572):
        return f"mach_port_allocate({meadow_self_53ed572.target}, {_name_boundary.attributes(meadow_self_53ed572.right)['name']}, {hex(_name_boundary.attributes(meadow_self_53ed572)['name'])})"

@_name_boundary.class_contract('MachPortDeallocate', {})
@meadow_dataclass
class meadow_MachPortDeallocate:
    ktraces: meadow_List
    target: int
    name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_67ef559'}, '__str__')
    def __str__(meadow_self_67ef559):
        return f"mach_port_deallocate({meadow_self_67ef559.target}, {hex(_name_boundary.attributes(meadow_self_67ef559)['name'])})"

@_name_boundary.class_contract('MachPortModRefs', {})
@meadow_dataclass
class meadow_MachPortModRefs:
    ktraces: meadow_List
    target: int
    name: int
    right: meadow_MachPortRight
    delta: int

    @_name_boundary.callable_contract({'self': 'meadow_self_20e92a5'}, '__str__')
    def __str__(meadow_self_20e92a5):
        return f"mach_port_mod_refs({meadow_self_20e92a5.target}, {hex(_name_boundary.attributes(meadow_self_20e92a5)['name'])}, {_name_boundary.attributes(meadow_self_20e92a5.right)['name']}, {hex(meadow_self_20e92a5.delta)})"

@_name_boundary.class_contract('MachPortInsertRight', {})
@meadow_dataclass
class meadow_MachPortInsertRight:
    ktraces: meadow_List
    target: int
    name: int
    poly: int
    poly_poly: meadow_MachMsgTypeName

    @_name_boundary.callable_contract({'self': 'meadow_self_c65943c'}, '__str__')
    def __str__(meadow_self_c65943c):
        return f"mach_port_insert_right({meadow_self_c65943c.target}, {hex(_name_boundary.attributes(meadow_self_c65943c)['name'])}, {hex(meadow_self_c65943c.poly)}, {_name_boundary.attributes(meadow_self_c65943c.poly_poly)['name']})"

@_name_boundary.class_contract('MachPortInsertMember', {})
@meadow_dataclass
class meadow_MachPortInsertMember:
    ktraces: meadow_List
    target: int
    name: int
    pset: int

    @_name_boundary.callable_contract({'self': 'meadow_self_314560d'}, '__str__')
    def __str__(meadow_self_314560d):
        return f"mach_port_insert_member({meadow_self_314560d.target}, {hex(_name_boundary.attributes(meadow_self_314560d)['name'])}, {hex(meadow_self_314560d.pset)})"

@_name_boundary.class_contract('MachPortExtractMember', {})
@meadow_dataclass
class meadow_MachPortExtractMember:
    ktraces: meadow_List
    target: int
    name: int
    pset: int

    @_name_boundary.callable_contract({'self': 'meadow_self_a277095'}, '__str__')
    def __str__(meadow_self_a277095):
        return f"mach_port_extract_member({meadow_self_a277095.target}, {hex(_name_boundary.attributes(meadow_self_a277095)['name'])}, {hex(meadow_self_a277095.pset)})"

@_name_boundary.class_contract('MachPortConstruct', {})
@meadow_dataclass
class meadow_MachPortConstruct:
    ktraces: meadow_List
    target: int
    options: int
    context: int
    name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_92a4fdc'}, '__str__')
    def __str__(meadow_self_92a4fdc):
        return f"mach_port_construct({meadow_self_92a4fdc.target}, {hex(meadow_self_92a4fdc.options)}, {hex(meadow_self_92a4fdc.context)}, {hex(_name_boundary.attributes(meadow_self_92a4fdc)['name'])})"

@_name_boundary.class_contract('MachPortDestruct', {})
@meadow_dataclass
class meadow_MachPortDestruct:
    ktraces: meadow_List
    target: int
    name: int
    srdelta: int
    guard: int

    @_name_boundary.callable_contract({'self': 'meadow_self_3044dce'}, '__str__')
    def __str__(meadow_self_3044dce):
        return f"mach_port_destruct({meadow_self_3044dce.target}, {hex(_name_boundary.attributes(meadow_self_3044dce)['name'])}, {hex(meadow_self_3044dce.srdelta)}, {hex(meadow_self_3044dce.guard)})"

@_name_boundary.class_contract('MachReplyPort', {})
@meadow_dataclass
class meadow_MachReplyPort:
    ktraces: meadow_List
    result: int

    @_name_boundary.callable_contract({'self': 'meadow_self_60d0871'}, '__str__')
    def __str__(meadow_self_60d0871):
        return f'mach_reply_port(), result: {hex(meadow_self_60d0871.result)}'

@_name_boundary.class_contract('MachThreadSelf', {})
@meadow_dataclass
class meadow_MachThreadSelf:
    ktraces: meadow_List
    result: int

    @_name_boundary.callable_contract({'self': 'meadow_self_3a1e789'}, '__str__')
    def __str__(meadow_self_3a1e789):
        return f'mach_thread_self(), result: {hex(meadow_self_3a1e789.result)}'

@_name_boundary.class_contract('TaskSelf', {})
@meadow_dataclass
class meadow_TaskSelf:
    ktraces: meadow_List
    result: int

    @_name_boundary.callable_contract({'self': 'meadow_self_8cd10c2'}, '__str__')
    def __str__(meadow_self_8cd10c2):
        return f'task_self(), result: {meadow_self_8cd10c2.result}'

@_name_boundary.class_contract('HostSelf', {})
@meadow_dataclass
class meadow_HostSelf:
    ktraces: meadow_List
    result: int

    @_name_boundary.callable_contract({'self': 'meadow_self_4d48404'}, '__str__')
    def __str__(meadow_self_4d48404):
        return f'host_self(), result: {hex(meadow_self_4d48404.result)}'

@_name_boundary.class_contract('SemaphoreSignal', {})
@meadow_dataclass
class meadow_SemaphoreSignal:
    ktraces: meadow_List
    signal_name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_d669ba5'}, '__str__')
    def __str__(meadow_self_d669ba5):
        return f'semaphore_signal({hex(meadow_self_d669ba5.signal_name)})'

@_name_boundary.class_contract('SemaphoreWait', {})
@meadow_dataclass
class meadow_SemaphoreWait:
    ktraces: meadow_List
    wait_name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_cf57713'}, '__str__')
    def __str__(meadow_self_cf57713):
        return f'semaphore_wait({hex(meadow_self_cf57713.wait_name)})'

@_name_boundary.class_contract('SemaphoreTimedwait', {})
@meadow_dataclass
class meadow_SemaphoreTimedwait:
    ktraces: meadow_List
    wait_name: int
    sec: int
    nsec: int
    result: meadow_KernReturn

    @_name_boundary.callable_contract({'self': 'meadow_self_d202c5a'}, '__str__')
    def __str__(meadow_self_d202c5a):
        return f"semaphore_timedwait({hex(meadow_self_d202c5a.wait_name)}, {meadow_self_d202c5a.sec}, {meadow_self_d202c5a.nsec}), result: {_name_boundary.attributes(meadow_self_d202c5a.result)['name']}"

@_name_boundary.class_contract('MachPortGetAttributes', {})
@meadow_dataclass
class meadow_MachPortGetAttributes:
    ktraces: meadow_List
    target: int
    name: int
    flavor: meadow_MachPortFlavor
    port_info_out: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ca1a183'}, '__str__')
    def __str__(meadow_self_ca1a183):
        return f"mach_port_get_attributes({meadow_self_ca1a183.target}, {hex(_name_boundary.attributes(meadow_self_ca1a183)['name'])}, {_name_boundary.attributes(meadow_self_ca1a183.flavor)['name']}, {hex(meadow_self_ca1a183.port_info_out)})"

@_name_boundary.class_contract('MachPortGuard', {})
@meadow_dataclass
class meadow_MachPortGuard:
    ktraces: meadow_List
    target: int
    name: int
    guard: int
    strict: bool

    @_name_boundary.callable_contract({'self': 'meadow_self_266d7b5'}, '__str__')
    def __str__(meadow_self_266d7b5):
        return f"mach_port_guard({meadow_self_266d7b5.target}, {hex(_name_boundary.attributes(meadow_self_266d7b5)['name'])}, {hex(meadow_self_266d7b5.guard)}, {str(meadow_self_266d7b5.strict).lower()})"

@_name_boundary.class_contract('MachPortUnguard', {})
@meadow_dataclass
class meadow_MachPortUnguard:
    ktraces: meadow_List
    target: int
    name: int
    guard: int

    @_name_boundary.callable_contract({'self': 'meadow_self_129975e'}, '__str__')
    def __str__(meadow_self_129975e):
        return f"mach_port_unguard({meadow_self_129975e.target}, {hex(_name_boundary.attributes(meadow_self_129975e)['name'])}, {hex(meadow_self_129975e.guard)})"

@_name_boundary.class_contract('MachGenerateActivityId', {})
@meadow_dataclass
class meadow_MachGenerateActivityId:
    ktraces: meadow_List
    target: int
    count: int
    activity_id: int

    @_name_boundary.callable_contract({'self': 'meadow_self_4ec0fb9'}, '__str__')
    def __str__(meadow_self_4ec0fb9):
        return f'mach_generate_activity_id({meadow_self_4ec0fb9.target}, {meadow_self_4ec0fb9.count}, {hex(meadow_self_4ec0fb9.activity_id)})'

@_name_boundary.class_contract('MachMsg2', {})
@meadow_dataclass
class meadow_MachMsg2:
    ktraces: meadow_List
    data: int
    option64: int
    header: int
    send_size: int

    @_name_boundary.callable_contract({'self': 'meadow_self_046e7b6'}, '__str__')
    def __str__(meadow_self_046e7b6):
        return f'mach_msg2({hex(meadow_self_046e7b6.data)}, {hex(meadow_self_046e7b6.option64)}, {hex(meadow_self_046e7b6.header)}, {hex(meadow_self_046e7b6.send_size)})'

@_name_boundary.class_contract('ThreadGetSpecialReplyPort', {})
@meadow_dataclass
class meadow_ThreadGetSpecialReplyPort:
    ktraces: meadow_List
    result: int

    @_name_boundary.callable_contract({'self': 'meadow_self_5288c02'}, '__str__')
    def __str__(meadow_self_5288c02):
        return f'thread_get_special_reply_port(), result {hex(meadow_self_5288c02.result)}'

@_name_boundary.class_contract('ThreadSwitch', {})
@meadow_dataclass
class meadow_ThreadSwitch:
    ktraces: meadow_List
    thread_name: int
    option: meadow_SwitchOption
    option_time: int

    @_name_boundary.callable_contract({'self': 'meadow_self_391cac5'}, '__str__')
    def __str__(meadow_self_391cac5):
        return f"thread_switch({hex(meadow_self_391cac5.thread_name)}, {_name_boundary.attributes(meadow_self_391cac5.option)['name']}, {meadow_self_391cac5.option_time})"

@_name_boundary.class_contract('HostCreateMachVoucher', {})
@meadow_dataclass
class meadow_HostCreateMachVoucher:
    ktraces: meadow_List
    host: int
    recipes: int
    recipes_size: int
    voucher: int

    @_name_boundary.callable_contract({'self': 'meadow_self_76b9091'}, '__str__')
    def __str__(meadow_self_76b9091):
        return f'host_create_mach_voucher({hex(meadow_self_76b9091.host)}, {hex(meadow_self_76b9091.recipes)}, {meadow_self_76b9091.recipes_size}, {hex(meadow_self_76b9091.voucher)})'

@_name_boundary.class_contract('MachPortType', {})
@meadow_dataclass
class meadow_MachPortType:
    ktraces: meadow_List
    task: int
    name: int
    ptype: int

    @_name_boundary.callable_contract({'self': 'meadow_self_36bfe1b'}, '__str__')
    def __str__(meadow_self_36bfe1b):
        return f"mach_port_type({meadow_self_36bfe1b.task}, {hex(_name_boundary.attributes(meadow_self_36bfe1b)['name'])}, {hex(meadow_self_36bfe1b.ptype)})"

@_name_boundary.class_contract('MachPortRequestNotification', {})
@meadow_dataclass
class meadow_MachPortRequestNotification:
    ktraces: meadow_List
    task: int
    name: int
    msgid: int
    sync: int

    @_name_boundary.callable_contract({'self': 'meadow_self_2bfef5c'}, '__str__')
    def __str__(meadow_self_2bfef5c):
        return f"mach_port_request_notification({meadow_self_2bfef5c.task}, {hex(_name_boundary.attributes(meadow_self_2bfef5c)['name'])}, {hex(meadow_self_2bfef5c.msgid)}, {meadow_self_2bfef5c.sync})"

@_name_boundary.class_contract('MachTimebaseInfo', {})
@meadow_dataclass
class meadow_MachTimebaseInfo:
    ktraces: meadow_List
    info: int

    @_name_boundary.callable_contract({'self': 'meadow_self_b270738'}, '__str__')
    def __str__(meadow_self_b270738):
        return f'mach_timebase_info({hex(meadow_self_b270738.info)})'

@_name_boundary.class_contract('MachWaitUntil', {})
@meadow_dataclass
class meadow_MachWaitUntil:
    ktraces: meadow_List
    deadline: int

    @_name_boundary.callable_contract({'self': 'meadow_self_701d9cc'}, '__str__')
    def __str__(meadow_self_701d9cc):
        return f'mach_wait_until({meadow_self_701d9cc.deadline})'

@_name_boundary.class_contract('MkTimerCreate', {})
@meadow_dataclass
class meadow_MkTimerCreate:
    ktraces: meadow_List
    timer_port: int

    @_name_boundary.callable_contract({'self': 'meadow_self_41d1e4c'}, '__str__')
    def __str__(meadow_self_41d1e4c):
        return f'mk_timer_create(), timer: {hex(meadow_self_41d1e4c.timer_port)}'

@_name_boundary.class_contract('MkTimerDestroy', {})
@meadow_dataclass
class meadow_MkTimerDestroy:
    ktraces: meadow_List
    name: int

    @_name_boundary.callable_contract({'self': 'meadow_self_1202032'}, '__str__')
    def __str__(meadow_self_1202032):
        return f"mk_timer_destroy({hex(_name_boundary.attributes(meadow_self_1202032)['name'])})"

@_name_boundary.class_contract('MkTimerArm', {})
@meadow_dataclass
class meadow_MkTimerArm:
    ktraces: meadow_List
    name: int
    expire_time: int

    @_name_boundary.callable_contract({'self': 'meadow_self_1233979'}, '__str__')
    def __str__(meadow_self_1233979):
        return f"mk_timer_arm({hex(_name_boundary.attributes(meadow_self_1233979)['name'])}, {meadow_self_1233979.expire_time})"

@_name_boundary.class_contract('MkTimerCancel', {})
@meadow_dataclass
class meadow_MkTimerCancel:
    ktraces: meadow_List
    name: int
    result_time: int

    @_name_boundary.callable_contract({'self': 'meadow_self_4177a27'}, '__str__')
    def __str__(meadow_self_4177a27):
        return f"mk_timer_cancel({hex(_name_boundary.attributes(meadow_self_4177a27)['name'])}, {meadow_self_4177a27.result_time})"

@_name_boundary.class_contract('MkTimerArmLeeway', {})
@meadow_dataclass
class meadow_MkTimerArmLeeway:
    ktraces: meadow_List
    name: int
    mk_timer_flags: meadow_MkTimerFlags
    mk_timer_expire_time: int
    mk_timer_leeway: int

    @_name_boundary.callable_contract({'self': 'meadow_self_f743124'}, '__str__')
    def __str__(meadow_self_f743124):
        return f"mk_timer_arm_leeway({hex(_name_boundary.attributes(meadow_self_f743124)['name'])}, {_name_boundary.attributes(meadow_self_f743124.mk_timer_flags)['name']}, {meadow_self_f743124.mk_timer_expire_time}, {meadow_self_f743124.mk_timer_leeway})"

@_name_boundary.class_contract('IokitUserClient', {})
@meadow_dataclass
class meadow_IokitUserClient:
    ktraces: meadow_List
    user_client_ref: int
    index: int
    p1: int
    p2: int

    @_name_boundary.callable_contract({'self': 'meadow_self_1830481'}, '__str__')
    def __str__(meadow_self_1830481):
        return f'iokit_user_client({hex(meadow_self_1830481.user_client_ref)}, {meadow_self_1830481.index}, {hex(meadow_self_1830481.p1)}, {hex(meadow_self_1830481.p2)})'

@_name_boundary.class_contract('ThreadSetVoucher', {})
@meadow_dataclass
class meadow_ThreadSetVoucher:
    ktraces: meadow_List
    tid: int
    port: int
    voucher: int
    persona_id: int

    @_name_boundary.callable_contract({'self': 'meadow_self_b4ac0ad'}, '__str__')
    def __str__(meadow_self_b4ac0ad):
        return f'thread_set_voucher, tid: {meadow_self_b4ac0ad.tid}, port: {hex(meadow_self_b4ac0ad.port)}, voucher: {hex(meadow_self_b4ac0ad.voucher)}, persona_id: {meadow_self_b4ac0ad.persona_id}'

@_name_boundary.class_contract('MachPageout', {})
@meadow_dataclass
class meadow_MachPageout:
    ktraces: meadow_List
    size: int

    @_name_boundary.callable_contract({'self': 'meadow_self_5b0587b'}, '__str__')
    def __str__(meadow_self_5b0587b):
        return f'MACH_Pageout, size: {hex(meadow_self_5b0587b.size)}'

@_name_boundary.class_contract('MachVmfault', {})
@meadow_dataclass
class meadow_MachVmfault:
    ktraces: meadow_List
    addr: int
    is_kernel: bool
    result: int
    fault_type: meadow_DbgVmFaultType = None
    pid: int = None
    caller_prot: meadow_List = None

    @_name_boundary.callable_contract({'self': 'meadow_self_ef4c239'}, '__str__')
    def __str__(meadow_self_ef4c239):
        meadow_ret_e113d8e = f'MachVmfault, addr: {hex(meadow_self_ef4c239.addr)}, is_kernel: {meadow_self_ef4c239.is_kernel}, result: {meadow_self_ef4c239.result}'
        if meadow_self_ef4c239.result == 0:
            meadow_ret_e113d8e += f", type: {_name_boundary.attributes(meadow_self_ef4c239.fault_type)['name']}"
            if meadow_self_ef4c239.pid is not None and meadow_self_ef4c239.caller_prot is not None:
                meadow_prot_d78ba68 = ' | '.join(map(lambda meadow_p_5c5b5a4: _name_boundary.attributes(meadow_p_5c5b5a4)['name'], meadow_self_ef4c239.caller_prot))
                meadow_ret_e113d8e += f', vm_prot: {meadow_prot_d78ba68}, pid: {meadow_self_ef4c239.pid}'
        return meadow_ret_e113d8e

@_name_boundary.class_contract('RealFaultAddressInternal', {})
@meadow_dataclass
class meadow_RealFaultAddressInternal:
    ktraces: meadow_List
    vaddr: int
    user_tag: int
    caller_prot: meadow_List
    fault_type: meadow_DbgVmFaultType
    offset: int
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_00db346'}, '__str__')
    def __str__(meadow_self_00db346):
        meadow_prot_824ef35 = ' | '.join(map(lambda meadow_p_e17e0ff: _name_boundary.attributes(meadow_p_e17e0ff)['name'], meadow_self_00db346.caller_prot))
        return f"RealFaultAddressInternal, vaddr: {hex(meadow_self_00db346.vaddr)}, vm_prot: {meadow_prot_824ef35}, type: {_name_boundary.attributes(meadow_self_00db346.fault_type)['name']}, pid: {meadow_self_00db346.pid}"

@_name_boundary.class_contract('RealFaultAddressExternal', {})
@meadow_dataclass
class meadow_RealFaultAddressExternal:
    ktraces: meadow_List
    vaddr: int
    user_tag: int
    caller_prot: meadow_List
    fault_type: meadow_DbgVmFaultType
    offset: int
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_cb9d464'}, '__str__')
    def __str__(meadow_self_cb9d464):
        meadow_prot_970c4d0 = ' | '.join(map(lambda meadow_p_d57f3fa: _name_boundary.attributes(meadow_p_d57f3fa)['name'], meadow_self_cb9d464.caller_prot))
        return f"RealFaultAddressExternal, vaddr: {hex(meadow_self_cb9d464.vaddr)}, vm_prot: {meadow_prot_970c4d0}, type: {_name_boundary.attributes(meadow_self_cb9d464.fault_type)['name']}, pid: {meadow_self_cb9d464.pid}"

@_name_boundary.class_contract('RealFaultAddressSharedCache', {})
@meadow_dataclass
class meadow_RealFaultAddressSharedCache:
    ktraces: meadow_List
    vaddr: int
    user_tag: int
    caller_prot: meadow_List
    fault_type: meadow_DbgVmFaultType
    offset: int
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_7d82bcb'}, '__str__')
    def __str__(meadow_self_7d82bcb):
        meadow_prot_81863af = ' | '.join(map(lambda meadow_p_2881ee5: _name_boundary.attributes(meadow_p_2881ee5)['name'], meadow_self_7d82bcb.caller_prot))
        return f"RealFaultAddressSharedCache, vaddr: {hex(meadow_self_7d82bcb.vaddr)}, vm_prot: {meadow_prot_81863af}, type: {_name_boundary.attributes(meadow_self_7d82bcb.fault_type)['name']}, pid: {meadow_self_7d82bcb.pid}"

@_name_boundary.class_contract('MachSched', {})
@meadow_dataclass
class meadow_MachSched:
    ktraces: meadow_List
    reason: meadow_List[meadow_AsynchronousSystemTrapsReason]
    to: int
    from_sched_pri: int
    to_sched_pri: int

    @_name_boundary.callable_contract({'self': 'meadow_self_40c9021'}, '__str__')
    def __str__(meadow_self_40c9021):
        meadow_reason_a2e3b80 = ' | '.join(map(lambda meadow_r_4e0d878: _name_boundary.attributes(meadow_r_4e0d878)['name'], meadow_self_40c9021.reason))
        return f'MACH_SCHED, to: {meadow_self_40c9021.to}, reason: {meadow_reason_a2e3b80}'

@_name_boundary.class_contract('MachStkhandoff', {})
@meadow_dataclass
class meadow_MachStkhandoff:
    ktraces: meadow_List
    from_: int
    to: int
    reason: meadow_List[meadow_AsynchronousSystemTrapsReason]
    from_sched_pri: int
    to_sched_pri: int

    @_name_boundary.callable_contract({'self': 'meadow_self_6544dd2'}, '__str__')
    def __str__(meadow_self_6544dd2):
        return f'stack_handoff({meadow_self_6544dd2.from_}, {meadow_self_6544dd2.to})'

@_name_boundary.class_contract('MachMkrunnable', {})
@meadow_dataclass
class meadow_MachMkrunnable:
    ktraces: meadow_List
    tid: int
    sched_pri: int
    wait_result: int
    runnable_threads: int

    @_name_boundary.callable_contract({'self': 'meadow_self_9cd7ed5'}, '__str__')
    def __str__(meadow_self_9cd7ed5):
        return f'MACH_MKRUNNABLE, tid: {meadow_self_9cd7ed5.tid}, wait_result: {meadow_self_9cd7ed5.wait_result}'

@_name_boundary.class_contract('MachIdle', {})
@meadow_dataclass
class meadow_MachIdle:
    ktraces: meadow_List
    from_: int
    process_state: meadow_ProcessState
    to: int
    reason: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_c05cd53'}, '__str__')
    def __str__(meadow_self_c05cd53):
        meadow_reason_626732b = ' | '.join(map(lambda meadow_r_bce6a17: _name_boundary.attributes(meadow_r_bce6a17)['name'], meadow_self_c05cd53.reason))
        return f"MACH_IDLE, from: {meadow_self_c05cd53.from_}, to: {meadow_self_c05cd53.to}, reason: {meadow_reason_626732b}, state: {_name_boundary.attributes(meadow_self_c05cd53.process_state)['name']}"

@_name_boundary.class_contract('MachBlock', {})
@meadow_dataclass
class meadow_MachBlock:
    ktraces: meadow_List
    reason: meadow_List[meadow_AsynchronousSystemTrapsReason]
    continuation: int

    @_name_boundary.callable_contract({'self': 'meadow_self_eb8b997'}, '__str__')
    def __str__(meadow_self_eb8b997):
        meadow_reason_17c2e0c = ' | '.join(map(lambda meadow_r_7b801a2: _name_boundary.attributes(meadow_r_7b801a2)['name'], meadow_self_eb8b997.reason))
        return f'MACH_BLOCK, reason: {meadow_reason_17c2e0c}, continuation: {hex(meadow_self_eb8b997.continuation)}'

@_name_boundary.class_contract('MachWait', {})
@meadow_dataclass
class meadow_MachWait:
    ktraces: meadow_List
    event: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c96a89f'}, '__str__')
    def __str__(meadow_self_c96a89f):
        return f'MACH_WAIT, event: {hex(meadow_self_c96a89f.event)}'

@_name_boundary.class_contract('MachDispatch', {})
@meadow_dataclass
class meadow_MachDispatch:
    ktraces: meadow_List
    tid: int
    reason: meadow_List
    state: meadow_List
    runnable_threads: int

    @_name_boundary.callable_contract({'self': 'meadow_self_24efffa'}, '__str__')
    def __str__(meadow_self_24efffa):
        meadow_reason_d26ec86 = ' | '.join(map(lambda meadow_r_3b096f4: _name_boundary.attributes(meadow_r_3b096f4)['name'], meadow_self_24efffa.reason))
        meadow_state_49a394a = ' | '.join(map(lambda meadow_s_90daebf: _name_boundary.attributes(meadow_s_90daebf)['name'], meadow_self_24efffa.state))
        return f'MACH_DISPATCH, tid: {meadow_self_24efffa.tid}, reason: {meadow_reason_d26ec86}, state: {meadow_state_49a394a}'

@_name_boundary.class_contract('ThreadGroupSet', {})
@meadow_dataclass
class meadow_ThreadGroupSet:
    ktraces: meadow_List
    current_tgid: int
    target_tgid: int
    tid: int
    home_tgid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_afa05c5'}, '__str__')
    def __str__(meadow_self_afa05c5):
        return f'THREAD_GROUP_SET, from: {meadow_self_afa05c5.current_tgid}, to: {meadow_self_afa05c5.target_tgid}, tid: {meadow_self_afa05c5.tid}, home: {meadow_self_afa05c5.home_tgid}'

@_name_boundary.class_contract('SchedClutchCpuThreadSelect', {})
@meadow_dataclass
class meadow_SchedClutchCpuThreadSelect:
    ktraces: meadow_List
    tid: int
    tgid: int
    scb_bucket: int

    @_name_boundary.callable_contract({'self': 'meadow_self_c31bda7'}, '__str__')
    def __str__(meadow_self_c31bda7):
        return f'SCHED_CLUTCH_CPU_THREAD_SELECT, tid: {meadow_self_c31bda7.tid}'

@_name_boundary.class_contract('SchedClutchTgBucketPri', {})
@meadow_dataclass
class meadow_SchedClutchTgBucketPri:
    ktraces: meadow_List
    tgid: int
    scb_bucket: int
    priority: int
    interactive_score: int

    @_name_boundary.callable_contract({'self': 'meadow_self_59b1e94'}, '__str__')
    def __str__(meadow_self_59b1e94):
        return f'SCHED_CLUTCH_TG_BUCKET_PRI, tgid: {meadow_self_59b1e94.tgid}, bucket: {meadow_self_59b1e94.scb_bucket}, priority: {meadow_self_59b1e94.priority}'

@_name_boundary.callable_contract({'parser': 'meadow_parser_4d6cf10', 'events': 'meadow_events_b62104f'}, 'handle_kernel_uncategorized_exc_arm')
def meadow_handle_kernel_uncategorized_exc_arm(meadow_parser_4d6cf10, meadow_events_b62104f):
    return meadow_KernelUncategorizedExcArm(meadow_events_b62104f, *meadow_events_b62104f[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_b09b295', 'events': 'meadow_events_2e4395c'}, 'handle_kernel_data_abort_same_el_exc_arm')
def meadow_handle_kernel_data_abort_same_el_exc_arm(meadow_parser_b09b295, meadow_events_2e4395c):
    return meadow_KernelDataAbortSameElExcArm(meadow_events_2e4395c, *meadow_events_2e4395c[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_27ddd4c', 'events': 'meadow_events_e0f49d8'}, 'handle_user_svc64_exc_arm')
def meadow_handle_user_svc64_exc_arm(meadow_parser_27ddd4c, meadow_events_e0f49d8):
    return meadow_UserSvc64ExcArm(meadow_events_e0f49d8, *meadow_events_e0f49d8[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_09fa9c6', 'events': 'meadow_events_8127f61'}, 'handle_user_instr_abort_lower_el_exc_arm')
def meadow_handle_user_instr_abort_lower_el_exc_arm(meadow_parser_09fa9c6, meadow_events_8127f61):
    return meadow_UserInstrAbortLowerElExcArm(meadow_events_8127f61, *meadow_events_8127f61[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_3cd1b19', 'events': 'meadow_events_f57cd16'}, 'handle_user_data_abort_lower_el_exc_arm')
def meadow_handle_user_data_abort_lower_el_exc_arm(meadow_parser_3cd1b19, meadow_events_f57cd16):
    meadow_args_4732069 = meadow_events_f57cd16[0].values
    return meadow_UserDataAbortLowerElExcArm(meadow_events_f57cd16, meadow_args_4732069[0], meadow_args_4732069[1], meadow_args_4732069[2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_17876df', 'events': 'meadow_events_8043df6'}, 'handle_interrupt')
def meadow_handle_interrupt(meadow_parser_17876df, meadow_events_8043df6):
    meadow_args_fc59f5a = meadow_events_8043df6[0].values
    return meadow_Interrupt(meadow_events_8043df6, meadow_args_fc59f5a[1], bool(meadow_args_fc59f5a[2]), meadow_args_fc59f5a[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_0a0024e', 'events': 'meadow_events_5260da9'}, 'handle_decr_trap')
def meadow_handle_decr_trap(meadow_parser_0a0024e, meadow_events_5260da9):
    meadow_args_d3d6662 = meadow_events_5260da9[0].values
    return meadow_DecrTrap(meadow_events_5260da9, meadow_ctypes.c_int64(meadow_args_d3d6662[0]).value, meadow_args_d3d6662[1], bool(meadow_args_d3d6662[2]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_506d196', 'events': 'meadow_events_a0cd5c1'}, 'handle_decr_set')
def meadow_handle_decr_set(meadow_parser_506d196, meadow_events_a0cd5c1):
    meadow_args_ba90a95 = meadow_events_a0cd5c1[0].values
    return meadow_DecrSet(meadow_events_a0cd5c1, meadow_args_ba90a95[0], meadow_args_ba90a95[2], meadow_args_ba90a95[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_61e6fdc', 'events': 'meadow_events_96f9b53'}, 'handle_msc_mach_vm_allocate_trap')
def meadow_handle_msc_mach_vm_allocate_trap(meadow_parser_61e6fdc, meadow_events_96f9b53):
    return meadow_MachVmAllocate(meadow_events_96f9b53, *meadow_events_96f9b53[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_6dcb002', 'events': 'meadow_events_be3fc8a'}, 'handle_msc_kern_mach_vm_purgable_control_trap')
def meadow_handle_msc_kern_mach_vm_purgable_control_trap(meadow_parser_6dcb002, meadow_events_be3fc8a):
    return meadow_MachVmPurgableControl(meadow_events_be3fc8a, *meadow_events_be3fc8a[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_c43a50b', 'events': 'meadow_events_e04257d'}, 'handle_msc_mach_vm_deallocate_trap')
def meadow_handle_msc_mach_vm_deallocate_trap(meadow_parser_c43a50b, meadow_events_e04257d):
    return meadow_MachVmDeallocate(meadow_events_e04257d, *meadow_events_e04257d[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_f13b887', 'events': 'meadow_events_10be037'}, 'handle_msc_mach_vm_protect_trap')
def meadow_handle_msc_mach_vm_protect_trap(meadow_parser_f13b887, meadow_events_10be037):
    return meadow_MachVmProtect(meadow_events_10be037, *meadow_events_10be037[0].values[:3], bool(meadow_events_10be037[0].values[3]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8df4d15', 'events': 'meadow_events_3160772'}, 'handle_msc_mach_vm_map_trap')
def meadow_handle_msc_mach_vm_map_trap(meadow_parser_8df4d15, meadow_events_3160772):
    return meadow_MachVmMap(meadow_events_3160772, *meadow_events_3160772[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_000b83b', 'events': 'meadow_events_c7b5d45'}, 'handle_msc_mach_port_allocate_trap')
def meadow_handle_msc_mach_port_allocate_trap(meadow_parser_000b83b, meadow_events_c7b5d45):
    meadow_args_c601968 = meadow_events_c7b5d45[0].values
    return meadow_MachPortAllocate(meadow_events_c7b5d45, meadow_args_c601968[0], meadow_MachPortRight(meadow_args_c601968[1]), meadow_args_c601968[2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_76f9d94', 'events': 'meadow_events_8cdeb3d'}, 'handle_msc_mach_port_deallocate_trap')
def meadow_handle_msc_mach_port_deallocate_trap(meadow_parser_76f9d94, meadow_events_8cdeb3d):
    return meadow_MachPortDeallocate(meadow_events_8cdeb3d, *meadow_events_8cdeb3d[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_3a38171', 'events': 'meadow_events_9a95fc2'}, 'handle_msc_mach_port_mod_refs_trap')
def meadow_handle_msc_mach_port_mod_refs_trap(meadow_parser_3a38171, meadow_events_9a95fc2):
    meadow_args_d8c1cfc = meadow_events_9a95fc2[0].values
    return meadow_MachPortModRefs(meadow_events_9a95fc2, meadow_args_d8c1cfc[0], meadow_args_d8c1cfc[1], meadow_MachPortRight(meadow_args_d8c1cfc[2]), meadow_args_d8c1cfc[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_c396cf7', 'events': 'meadow_events_71d1876'}, 'handle_msc_mach_port_insert_right_trap')
def meadow_handle_msc_mach_port_insert_right_trap(meadow_parser_c396cf7, meadow_events_71d1876):
    return meadow_MachPortInsertRight(meadow_events_71d1876, *meadow_events_71d1876[0].values[:3], meadow_MachMsgTypeName(meadow_events_71d1876[0].values[3]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c1b29f4', 'events': 'meadow_events_c9155c7'}, 'handle_msc_mach_port_insert_member_trap')
def meadow_handle_msc_mach_port_insert_member_trap(meadow_parser_c1b29f4, meadow_events_c9155c7):
    return meadow_MachPortInsertMember(meadow_events_c9155c7, *meadow_events_c9155c7[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_cdaf180', 'events': 'meadow_events_c4b3ab5'}, 'handle_msc_mach_port_extract_member_trap')
def meadow_handle_msc_mach_port_extract_member_trap(meadow_parser_cdaf180, meadow_events_c4b3ab5):
    return meadow_MachPortExtractMember(meadow_events_c4b3ab5, *meadow_events_c4b3ab5[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_ac45067', 'events': 'meadow_events_47c5b42'}, 'handle_msc_mach_port_construct_trap')
def meadow_handle_msc_mach_port_construct_trap(meadow_parser_ac45067, meadow_events_47c5b42):
    return meadow_MachPortConstruct(meadow_events_47c5b42, *meadow_events_47c5b42[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a2ea041', 'events': 'meadow_events_f453a25'}, 'handle_msc_mach_port_destruct_trap')
def meadow_handle_msc_mach_port_destruct_trap(meadow_parser_a2ea041, meadow_events_f453a25):
    return meadow_MachPortDestruct(meadow_events_f453a25, *meadow_events_f453a25[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_45a35ca', 'events': 'meadow_events_47b9173'}, 'handle_msc_mach_reply_port')
def meadow_handle_msc_mach_reply_port(meadow_parser_45a35ca, meadow_events_47b9173):
    return meadow_MachReplyPort(meadow_events_47b9173, meadow_events_47b9173[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_8d93983', 'events': 'meadow_events_9d6a024'}, 'handle_msc_thread_self_trap')
def meadow_handle_msc_thread_self_trap(meadow_parser_8d93983, meadow_events_9d6a024):
    return meadow_MachThreadSelf(meadow_events_9d6a024, meadow_events_9d6a024[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_53a0473', 'events': 'meadow_events_1b088af'}, 'handle_msc_task_self_port')
def meadow_handle_msc_task_self_port(meadow_parser_53a0473, meadow_events_1b088af):
    return meadow_TaskSelf(meadow_events_1b088af, meadow_events_1b088af[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_cdb8e0e', 'events': 'meadow_events_95915e6'}, 'handle_msc_host_self_port')
def meadow_handle_msc_host_self_port(meadow_parser_cdb8e0e, meadow_events_95915e6):
    return meadow_HostSelf(meadow_events_95915e6, meadow_events_95915e6[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_7fbbaf7', 'events': 'meadow_events_9b33209'}, 'handle_msc_semaphore_signal_trap')
def meadow_handle_msc_semaphore_signal_trap(meadow_parser_7fbbaf7, meadow_events_9b33209):
    return meadow_SemaphoreSignal(meadow_events_9b33209, meadow_events_9b33209[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_4a7a350', 'events': 'meadow_events_21cd1cc'}, 'handle_msc_semaphore_wait_trap')
def meadow_handle_msc_semaphore_wait_trap(meadow_parser_4a7a350, meadow_events_21cd1cc):
    return meadow_SemaphoreWait(meadow_events_21cd1cc, meadow_events_21cd1cc[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_bee96dc', 'events': 'meadow_events_2599e48'}, 'handle_msc_semaphore_timedwait_trap')
def meadow_handle_msc_semaphore_timedwait_trap(meadow_parser_bee96dc, meadow_events_2599e48):
    meadow_args_136830a = meadow_events_2599e48[0].values
    return meadow_SemaphoreTimedwait(meadow_events_2599e48, meadow_args_136830a[0], meadow_args_136830a[1] & 4294967295, meadow_args_136830a[2], meadow_KernReturn(meadow_events_2599e48[-1].values[0]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_fd53eb1', 'events': 'meadow_events_317cda7'}, 'handle_msc_mach_port_get_attributes_trap')
def meadow_handle_msc_mach_port_get_attributes_trap(meadow_parser_fd53eb1, meadow_events_317cda7):
    meadow_args_3554c2d = meadow_events_317cda7[0].values
    return meadow_MachPortGetAttributes(meadow_events_317cda7, *meadow_args_3554c2d[:2], meadow_MachPortFlavor(meadow_args_3554c2d[2]), meadow_args_3554c2d[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_f60f3da', 'events': 'meadow_events_c73ac04'}, 'handle_msc_mach_port_guard_trap')
def meadow_handle_msc_mach_port_guard_trap(meadow_parser_f60f3da, meadow_events_c73ac04):
    return meadow_MachPortGuard(meadow_events_c73ac04, *meadow_events_c73ac04[0].values[:3], bool(meadow_events_c73ac04[0].values[3]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_53b2bed', 'events': 'meadow_events_9c61f58'}, 'handle_msc_mach_port_unguard_trap')
def meadow_handle_msc_mach_port_unguard_trap(meadow_parser_53b2bed, meadow_events_9c61f58):
    return meadow_MachPortUnguard(meadow_events_9c61f58, *meadow_events_9c61f58[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_78d1dc1', 'events': 'meadow_events_4a49101'}, 'handle_msc_mach_generate_activity_id')
def meadow_handle_msc_mach_generate_activity_id(meadow_parser_78d1dc1, meadow_events_4a49101):
    return meadow_MachGenerateActivityId(meadow_events_4a49101, *meadow_events_4a49101[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_496ddf2', 'events': 'meadow_events_7b4c58a'}, 'handle_msc_mach_msg2_trap')
def meadow_handle_msc_mach_msg2_trap(meadow_parser_496ddf2, meadow_events_7b4c58a):
    return meadow_MachMsg2(meadow_events_7b4c58a, *meadow_events_7b4c58a[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_fd1e3a9', 'events': 'meadow_events_5d9d98b'}, 'handle_msc_thread_get_special_reply_port')
def meadow_handle_msc_thread_get_special_reply_port(meadow_parser_fd1e3a9, meadow_events_5d9d98b):
    return meadow_ThreadGetSpecialReplyPort(meadow_events_5d9d98b, meadow_events_5d9d98b[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_f0311f0', 'events': 'meadow_events_831ce80'}, 'handle_msc_thread_switch')
def meadow_handle_msc_thread_switch(meadow_parser_f0311f0, meadow_events_831ce80):
    meadow_args_7b5e0d7 = meadow_events_831ce80[0].values
    return meadow_ThreadSwitch(meadow_events_831ce80, meadow_args_7b5e0d7[0], meadow_SwitchOption(meadow_args_7b5e0d7[1]), meadow_args_7b5e0d7[2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_3035d78', 'events': 'meadow_events_0ba031b'}, 'handle_msc_host_create_mach_voucher_trap')
def meadow_handle_msc_host_create_mach_voucher_trap(meadow_parser_3035d78, meadow_events_0ba031b):
    return meadow_HostCreateMachVoucher(meadow_events_0ba031b, *meadow_events_0ba031b[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_159c47b', 'events': 'meadow_events_cc7d407'}, 'handle_msc_mach_port_type_trap')
def meadow_handle_msc_mach_port_type_trap(meadow_parser_159c47b, meadow_events_cc7d407):
    return meadow_MachPortType(meadow_events_cc7d407, *meadow_events_cc7d407[0].values[:3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_1947f9e', 'events': 'meadow_events_e221605'}, 'handle_msc_mach_port_request_notification_trap')
def meadow_handle_msc_mach_port_request_notification_trap(meadow_parser_1947f9e, meadow_events_e221605):
    return meadow_MachPortRequestNotification(meadow_events_e221605, *meadow_events_e221605[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_1031765', 'events': 'meadow_events_0009794'}, 'handle_msc_mach_timebase_info')
def meadow_handle_msc_mach_timebase_info(meadow_parser_1031765, meadow_events_0009794):
    return meadow_MachTimebaseInfo(meadow_events_0009794, meadow_events_0009794[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_3804d81', 'events': 'meadow_events_68b3425'}, 'handle_msc_mach_wait_until')
def meadow_handle_msc_mach_wait_until(meadow_parser_3804d81, meadow_events_68b3425):
    return meadow_MachWaitUntil(meadow_events_68b3425, meadow_events_68b3425[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_fc2502b', 'events': 'meadow_events_c93a332'}, 'handle_msc_mk_timer_create')
def meadow_handle_msc_mk_timer_create(meadow_parser_fc2502b, meadow_events_c93a332):
    return meadow_MkTimerCreate(meadow_events_c93a332, meadow_events_c93a332[-1].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_650940b', 'events': 'meadow_events_a05de3f'}, 'handle_msc_mk_timer_destroy')
def meadow_handle_msc_mk_timer_destroy(meadow_parser_650940b, meadow_events_a05de3f):
    return meadow_MkTimerDestroy(meadow_events_a05de3f, meadow_events_a05de3f[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_e704ec1', 'events': 'meadow_events_fb56cb4'}, 'handle_msc_mk_timer_arm')
def meadow_handle_msc_mk_timer_arm(meadow_parser_e704ec1, meadow_events_fb56cb4):
    return meadow_MkTimerArm(meadow_events_fb56cb4, *meadow_events_fb56cb4[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_c150bf6', 'events': 'meadow_events_e1d4b66'}, 'handle_msc_mk_timer_cancel')
def meadow_handle_msc_mk_timer_cancel(meadow_parser_c150bf6, meadow_events_e1d4b66):
    return meadow_MkTimerCancel(meadow_events_e1d4b66, *meadow_events_e1d4b66[0].values[:2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_23c76f8', 'events': 'meadow_events_4789e93'}, 'handle_msc_mk_timer_arm_leeway')
def meadow_handle_msc_mk_timer_arm_leeway(meadow_parser_23c76f8, meadow_events_4789e93):
    meadow_args_7ac3f1c = meadow_events_4789e93[0].values
    return meadow_MkTimerArmLeeway(meadow_events_4789e93, meadow_args_7ac3f1c[0], meadow_MkTimerFlags(meadow_args_7ac3f1c[1]), meadow_args_7ac3f1c[2], meadow_args_7ac3f1c[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_aa9960a', 'events': 'meadow_events_abbd5a3'}, 'handle_msc_iokit_user_client')
def meadow_handle_msc_iokit_user_client(meadow_parser_aa9960a, meadow_events_abbd5a3):
    return meadow_IokitUserClient(meadow_events_abbd5a3, *meadow_events_abbd5a3[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_117f419', 'events': 'meadow_events_46e4239'}, 'handle_mach_thread_set_voucher')
def meadow_handle_mach_thread_set_voucher(meadow_parser_117f419, meadow_events_46e4239):
    return meadow_ThreadSetVoucher(meadow_events_46e4239, *meadow_events_46e4239[0].values)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a4516b4', 'events': 'meadow_events_a1d8c30'}, 'handle_mach_pageout')
def meadow_handle_mach_pageout(meadow_parser_a4516b4, meadow_events_a1d8c30):
    return meadow_MachPageout(meadow_events_a1d8c30, meadow_events_a1d8c30[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_d168337', 'events': 'meadow_events_5f1da60'}, 'handle_mach_vmfault')
def meadow_handle_mach_vmfault(meadow_parser_d168337, meadow_events_5f1da60):
    meadow_args_af88354 = meadow_events_5f1da60[0].values
    meadow_is_kernel_ded4516 = bool(meadow_args_af88354[2])
    meadow_rets_46501e8 = meadow_events_5f1da60[-1].values
    meadow_result_3884f46 = meadow_rets_46501e8[2]
    meadow_fault_type_188dd80 = None
    meadow_pid_d85eefc = None
    meadow_caller_prot_10a6b93 = None
    if meadow_result_3884f46 == 0:
        meadow_fault_type_188dd80 = meadow_DbgVmFaultType(meadow_rets_46501e8[3])
        meadow_real_events_b3f7ce7 = [meadow_e_6152983 for meadow_e_6152983 in meadow_events_5f1da60[1:-1] if 20054024 <= meadow_e_6152983.eventid <= 20054036]
        if meadow_real_events_b3f7ce7:
            meadow_vm_fault_real_2f34e8e = _name_boundary.attributes(meadow_parser_d168337)['parse_event_list'](meadow_real_events_b3f7ce7)
            meadow_pid_d85eefc = meadow_vm_fault_real_2f34e8e.pid
            meadow_caller_prot_10a6b93 = meadow_vm_fault_real_2f34e8e.caller_prot
    return meadow_MachVmfault(meadow_events_5f1da60, meadow_args_af88354[1], meadow_is_kernel_ded4516, meadow_result_3884f46, meadow_fault_type_188dd80, meadow_pid_d85eefc, meadow_caller_prot_10a6b93)

@_name_boundary.callable_contract({'addr_type': 'meadow_addr_type_971b5d1', 'parser': 'meadow_parser_b71054e', 'events': 'meadow_events_fd230b4'}, 'handle_real_fault_address')
def meadow_handle_real_fault_address(meadow_addr_type_971b5d1, meadow_parser_b71054e, meadow_events_fd230b4):
    meadow_args_a4b5e01 = meadow_events_fd230b4[0].values
    meadow_caller_prot_0483559 = meadow_to_vm_prot(meadow_args_a4b5e01[1] >> 8 & 255)
    meadow_fault_type_42fafba = meadow_DbgVmFaultType(meadow_args_a4b5e01[1] & 255)
    return meadow_addr_type_971b5d1(meadow_events_fd230b4, meadow_args_a4b5e01[0], meadow_args_a4b5e01[1] >> 16, meadow_caller_prot_0483559, meadow_fault_type_42fafba, meadow_args_a4b5e01[2], meadow_args_a4b5e01[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_ec592e5', 'events': 'meadow_events_f3f622e'}, 'handle_mach_sched')
def meadow_handle_mach_sched(meadow_parser_ec592e5, meadow_events_f3f622e):
    meadow_args_e0b4650 = meadow_events_f3f622e[0].values
    return meadow_MachSched(meadow_events_f3f622e, meadow_to_ast_reasons(meadow_args_e0b4650[0]), meadow_args_e0b4650[1], meadow_args_e0b4650[2], meadow_args_e0b4650[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_b413d11', 'events': 'meadow_events_cb09fe6'}, 'handle_mach_stkhandoff')
def meadow_handle_mach_stkhandoff(meadow_parser_b413d11, meadow_events_cb09fe6):
    meadow_args_4ac51c7 = meadow_events_cb09fe6[0].values
    return meadow_MachStkhandoff(meadow_events_cb09fe6, meadow_events_cb09fe6[0].tid, meadow_args_4ac51c7[1], meadow_to_ast_reasons(meadow_args_4ac51c7[0]), meadow_args_4ac51c7[2], meadow_args_4ac51c7[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_0a30e32', 'events': 'meadow_events_ce935a3'}, 'handle_mach_mkrunnable')
def meadow_handle_mach_mkrunnable(meadow_parser_0a30e32, meadow_events_ce935a3):
    meadow_args_7f6cdb8 = meadow_events_ce935a3[0].values
    return meadow_MachMkrunnable(meadow_events_ce935a3, meadow_args_7f6cdb8[0], meadow_args_7f6cdb8[1], meadow_args_7f6cdb8[2], meadow_args_7f6cdb8[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_b2c6f00', 'events': 'meadow_events_257c78e'}, 'handle_mach_idle')
def meadow_handle_mach_idle(meadow_parser_b2c6f00, meadow_events_257c78e):
    meadow_args_65d7e1e = meadow_events_257c78e[-1].values
    return meadow_MachIdle(meadow_events_257c78e, meadow_args_65d7e1e[0], meadow_ProcessState(meadow_args_65d7e1e[1]), meadow_args_65d7e1e[2], meadow_to_ast_reasons(meadow_args_65d7e1e[3]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7b432f7', 'events': 'meadow_events_37b667d'}, 'handle_mach_block')
def meadow_handle_mach_block(meadow_parser_7b432f7, meadow_events_37b667d):
    meadow_args_f3b3b96 = meadow_events_37b667d[0].values
    return meadow_MachBlock(meadow_events_37b667d, meadow_to_ast_reasons(meadow_args_f3b3b96[0]), meadow_args_f3b3b96[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_537f0f2', 'events': 'meadow_events_27f797b'}, 'handle_mach_wait')
def meadow_handle_mach_wait(meadow_parser_537f0f2, meadow_events_27f797b):
    return meadow_MachWait(meadow_events_27f797b, meadow_events_27f797b[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_838a20f', 'events': 'meadow_events_381ab4c'}, 'handle_mach_dispatch')
def meadow_handle_mach_dispatch(meadow_parser_838a20f, meadow_events_381ab4c):
    meadow_args_5ab6788 = meadow_events_381ab4c[0].values
    return meadow_MachDispatch(meadow_events_381ab4c, meadow_args_5ab6788[0], meadow_to_ast_reasons(meadow_args_5ab6788[1]), meadow_to_thread_state(meadow_args_5ab6788[2]), meadow_args_5ab6788[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_43337e8', 'events': 'meadow_events_ee0d0b4'}, 'handle_thread_group_set')
def meadow_handle_thread_group_set(meadow_parser_43337e8, meadow_events_ee0d0b4):
    meadow_args_693aa90 = meadow_events_ee0d0b4[0].values
    return meadow_ThreadGroupSet(meadow_events_ee0d0b4, meadow_ctypes.c_int64(meadow_args_693aa90[0]).value, meadow_args_693aa90[1], meadow_args_693aa90[2], meadow_args_693aa90[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_c3665d0', 'events': 'meadow_events_33e7952'}, 'handle_sched_clutch_cpu_thread_select')
def meadow_handle_sched_clutch_cpu_thread_select(meadow_parser_c3665d0, meadow_events_33e7952):
    meadow_args_abcebf9 = meadow_events_33e7952[0].values
    return meadow_SchedClutchCpuThreadSelect(meadow_events_33e7952, meadow_args_abcebf9[0], meadow_args_abcebf9[1], meadow_args_abcebf9[2])

@_name_boundary.callable_contract({'parser': 'meadow_parser_3fdf6e3', 'events': 'meadow_events_ea5b186'}, 'handle_sched_clutch_tg_bucket_pri')
def meadow_handle_sched_clutch_tg_bucket_pri(meadow_parser_3fdf6e3, meadow_events_ea5b186):
    meadow_args_998da99 = meadow_events_ea5b186[0].values
    return meadow_SchedClutchTgBucketPri(meadow_events_ea5b186, meadow_args_998da99[0], meadow_args_998da99[1], meadow_args_998da99[2], meadow_args_998da99[3])
meadow_handlers = {'Kernel_Uncategorized_Exc_ARM': meadow_handle_kernel_uncategorized_exc_arm, 'Kernel_Data_Abort_Same_EL_Exc_ARM': meadow_handle_kernel_data_abort_same_el_exc_arm, 'User_SVC64_Exc_ARM': meadow_handle_user_svc64_exc_arm, 'User_Instr_Abort_Lower_EL_Exc_ARM': meadow_handle_user_instr_abort_lower_el_exc_arm, 'User_Data_Abort_Lower_EL_Exc_ARM': meadow_handle_user_data_abort_lower_el_exc_arm, 'INTERRUPT': meadow_handle_interrupt, 'DecrTrap': meadow_handle_decr_trap, 'DecrSet': meadow_handle_decr_set, 'MSC_mach_vm_allocate_trap': meadow_handle_msc_mach_vm_allocate_trap, 'MSC_kern_mach_vm_purgable_control_trap': meadow_handle_msc_kern_mach_vm_purgable_control_trap, 'MSC_mach_vm_deallocate_trap': meadow_handle_msc_mach_vm_deallocate_trap, 'MSC_mach_vm_protect_trap': meadow_handle_msc_mach_vm_protect_trap, 'MSC_mach_vm_map_trap': meadow_handle_msc_mach_vm_map_trap, 'MSC_mach_port_allocate_trap': meadow_handle_msc_mach_port_allocate_trap, 'MSC_mach_port_deallocate_trap': meadow_handle_msc_mach_port_deallocate_trap, 'MSC_mach_port_mod_refs_trap': meadow_handle_msc_mach_port_mod_refs_trap, 'MSC_mach_port_insert_right_trap': meadow_handle_msc_mach_port_insert_right_trap, 'MSC_mach_port_insert_member_trap': meadow_handle_msc_mach_port_insert_member_trap, 'MSC_mach_port_extract_member_trap': meadow_handle_msc_mach_port_extract_member_trap, 'MSC_mach_port_construct_trap': meadow_handle_msc_mach_port_construct_trap, 'MSC_mach_port_destruct_trap': meadow_handle_msc_mach_port_destruct_trap, 'MSC_mach_reply_port': meadow_handle_msc_mach_reply_port, 'MSC_thread_self_trap': meadow_handle_msc_thread_self_trap, 'MSC_task_self_trap': meadow_handle_msc_task_self_port, 'MSC_host_self_trap': meadow_handle_msc_host_self_port, 'MSC_semaphore_signal_trap': meadow_handle_msc_semaphore_signal_trap, 'MSC_semaphore_wait_trap': meadow_handle_msc_semaphore_wait_trap, 'MSC_semaphore_timedwait_trap': meadow_handle_msc_semaphore_timedwait_trap, 'MSC_mach_port_get_attributes_trap': meadow_handle_msc_mach_port_get_attributes_trap, 'MSC_mach_port_guard_trap': meadow_handle_msc_mach_port_guard_trap, 'MSC_mach_port_unguard_trap': meadow_handle_msc_mach_port_unguard_trap, 'MSC_mach_generate_activity_id': meadow_handle_msc_mach_generate_activity_id, 'MSC_mach_msg2_trap': meadow_handle_msc_mach_msg2_trap, 'MSC_thread_get_special_reply_port': meadow_handle_msc_thread_get_special_reply_port, 'MSC_thread_switch': meadow_handle_msc_thread_switch, 'MSC_host_create_mach_voucher_trap': meadow_handle_msc_host_create_mach_voucher_trap, 'MSC_mach_port_type_trap': meadow_handle_msc_mach_port_type_trap, 'MSC_mach_port_request_notification_trap': meadow_handle_msc_mach_port_request_notification_trap, 'MSC_mach_timebase_info': meadow_handle_msc_mach_timebase_info, 'MSC_mach_wait_until': meadow_handle_msc_mach_wait_until, 'MSC_mk_timer_create': meadow_handle_msc_mk_timer_create, 'MSC_mk_timer_destroy': meadow_handle_msc_mk_timer_destroy, 'MSC_mk_timer_arm': meadow_handle_msc_mk_timer_arm, 'MSC_mk_timer_cancel': meadow_handle_msc_mk_timer_cancel, 'MSC_mk_timer_arm_leeway': meadow_handle_msc_mk_timer_arm_leeway, 'MSC_iokit_user_client': meadow_handle_msc_iokit_user_client, 'MACH_thread_set_voucher': meadow_handle_mach_thread_set_voucher, 'MACH_Pageout': meadow_handle_mach_pageout, 'MACH_vmfault': meadow_handle_mach_vmfault, 'RealFaultAddressInternal': meadow_partial(meadow_handle_real_fault_address, meadow_RealFaultAddressInternal), 'RealFaultAddressExternal': meadow_partial(meadow_handle_real_fault_address, meadow_RealFaultAddressExternal), 'RealFaultAddressSharedCache': meadow_partial(meadow_handle_real_fault_address, meadow_RealFaultAddressSharedCache), 'MACH_SCHED': meadow_handle_mach_sched, 'MACH_STKHANDOFF': meadow_handle_mach_stkhandoff, 'MACH_MKRUNNABLE': meadow_handle_mach_mkrunnable, 'MACH_IDLE': meadow_handle_mach_idle, 'MACH_BLOCK': meadow_handle_mach_block, 'MACH_WAIT': meadow_handle_mach_wait, 'MACH_DISPATCH': meadow_handle_mach_dispatch, 'THREAD_GROUP_SET': meadow_handle_thread_group_set, 'SCHED_CLUTCH_CPU_THREAD_SELECT': meadow_handle_sched_clutch_cpu_thread_select, 'SCHED_CLUTCH_TG_BUCKET_PRI': meadow_handle_sched_clutch_tg_bucket_pri}
_name_boundary.module_contract(globals(), {'SemaphoreTimedwait': 'meadow_SemaphoreTimedwait', 'handle_mach_pageout': 'meadow_handle_mach_pageout', 'ctypes': 'meadow_ctypes', 'MachVmfault': 'meadow_MachVmfault', 'handle_user_data_abort_lower_el_exc_arm': 'meadow_handle_user_data_abort_lower_el_exc_arm', 'handle_mach_wait': 'meadow_handle_mach_wait', 'MachPortGuard': 'meadow_MachPortGuard', 'handle_msc_mach_port_get_attributes_trap': 'meadow_handle_msc_mach_port_get_attributes_trap', 'handle_msc_thread_self_trap': 'meadow_handle_msc_thread_self_trap', 'handle_thread_group_set': 'meadow_handle_thread_group_set', 'UserSvc64ExcArm': 'meadow_UserSvc64ExcArm', 'handle_decr_set': 'meadow_handle_decr_set', 'ThreadGroupSet': 'meadow_ThreadGroupSet', 'handle_msc_mk_timer_create': 'meadow_handle_msc_mk_timer_create', 'handle_msc_mach_port_extract_member_trap': 'meadow_handle_msc_mach_port_extract_member_trap', 'ThreadState': 'meadow_ThreadState', 'InterruptType': 'meadow_InterruptType', 'handle_msc_mach_vm_allocate_trap': 'meadow_handle_msc_mach_vm_allocate_trap', 'handle_kernel_data_abort_same_el_exc_arm': 'meadow_handle_kernel_data_abort_same_el_exc_arm', 'ThreadSwitch': 'meadow_ThreadSwitch', 'AsynchronousSystemTrapsReason': 'meadow_AsynchronousSystemTrapsReason', 'handle_msc_semaphore_timedwait_trap': 'meadow_handle_msc_semaphore_timedwait_trap', 'handle_mach_thread_set_voucher': 'meadow_handle_mach_thread_set_voucher', 'MachDispatch': 'meadow_MachDispatch', 'MachMsg2': 'meadow_MachMsg2', 'DbgVmFaultType': 'meadow_DbgVmFaultType', 'ThreadSetVoucher': 'meadow_ThreadSetVoucher', 'handle_msc_kern_mach_vm_purgable_control_trap': 'meadow_handle_msc_kern_mach_vm_purgable_control_trap', 'RealFaultAddressSharedCache': 'meadow_RealFaultAddressSharedCache', 'ExceptionSyndromeRegisterClass': 'meadow_ExceptionSyndromeRegisterClass', 'handle_msc_mach_vm_protect_trap': 'meadow_handle_msc_mach_vm_protect_trap', 'handle_mach_dispatch': 'meadow_handle_mach_dispatch', 'partial': 'meadow_partial', 'handle_msc_mk_timer_cancel': 'meadow_handle_msc_mk_timer_cancel', 'MachMsgTypeName': 'meadow_MachMsgTypeName', 'handle_mach_idle': 'meadow_handle_mach_idle', 'DecrTrap': 'meadow_DecrTrap', 'handlers': 'meadow_handlers', 'handle_user_instr_abort_lower_el_exc_arm': 'meadow_handle_user_instr_abort_lower_el_exc_arm', 'handle_msc_mach_wait_until': 'meadow_handle_msc_mach_wait_until', 'MachPortRight': 'meadow_MachPortRight', 'RealFaultAddressExternal': 'meadow_RealFaultAddressExternal', 'MachSched': 'meadow_MachSched', 'handle_msc_iokit_user_client': 'meadow_handle_msc_iokit_user_client', 'MachBlock': 'meadow_MachBlock', 'handle_interrupt': 'meadow_handle_interrupt', 'handle_msc_mach_port_guard_trap': 'meadow_handle_msc_mach_port_guard_trap', 'handle_msc_mk_timer_destroy': 'meadow_handle_msc_mk_timer_destroy', 'ThreadGetSpecialReplyPort': 'meadow_ThreadGetSpecialReplyPort', 'to_ast_reasons': 'meadow_to_ast_reasons', 'handle_msc_mach_port_destruct_trap': 'meadow_handle_msc_mach_port_destruct_trap', 'MachVmProtect': 'meadow_MachVmProtect', 'handle_msc_mach_vm_deallocate_trap': 'meadow_handle_msc_mach_vm_deallocate_trap', 'handle_kernel_uncategorized_exc_arm': 'meadow_handle_kernel_uncategorized_exc_arm', 'MkTimerCancel': 'meadow_MkTimerCancel', 'SchedClutchCpuThreadSelect': 'meadow_SchedClutchCpuThreadSelect', 'List': 'meadow_List', 'MachPortUnguard': 'meadow_MachPortUnguard', 'MachWaitUntil': 'meadow_MachWaitUntil', 'handle_mach_stkhandoff': 'meadow_handle_mach_stkhandoff', 'MachPortGetAttributes': 'meadow_MachPortGetAttributes', 'handle_msc_mach_port_deallocate_trap': 'meadow_handle_msc_mach_port_deallocate_trap', 'handle_msc_mach_port_insert_member_trap': 'meadow_handle_msc_mach_port_insert_member_trap', 'DecrSet': 'meadow_DecrSet', 'SemaphoreSignal': 'meadow_SemaphoreSignal', 'handle_sched_clutch_tg_bucket_pri': 'meadow_handle_sched_clutch_tg_bucket_pri', 'handle_msc_thread_get_special_reply_port': 'meadow_handle_msc_thread_get_special_reply_port', 'handle_mach_mkrunnable': 'meadow_handle_mach_mkrunnable', 'handle_real_fault_address': 'meadow_handle_real_fault_address', 'SemaphoreWait': 'meadow_SemaphoreWait', 'UserInstrAbortLowerElExcArm': 'meadow_UserInstrAbortLowerElExcArm', 'MachVmDeallocate': 'meadow_MachVmDeallocate', 'handle_msc_mach_timebase_info': 'meadow_handle_msc_mach_timebase_info', 'RealFaultAddressInternal': 'meadow_RealFaultAddressInternal', 'handle_msc_host_self_port': 'meadow_handle_msc_host_self_port', 'MachPortType': 'meadow_MachPortType', 'ESR_EC_SHIFT': 'meadow_ESR_EC_SHIFT', 'MachTimebaseInfo': 'meadow_MachTimebaseInfo', 'MkTimerCreate': 'meadow_MkTimerCreate', 'handle_msc_mach_vm_map_trap': 'meadow_handle_msc_mach_vm_map_trap', 'MachStkhandoff': 'meadow_MachStkhandoff', 'MachPageout': 'meadow_MachPageout', 'handle_msc_semaphore_wait_trap': 'meadow_handle_msc_semaphore_wait_trap', 'UserDataAbortLowerElExcArm': 'meadow_UserDataAbortLowerElExcArm', 'MkTimerDestroy': 'meadow_MkTimerDestroy', 'ProcessState': 'meadow_ProcessState', 'to_thread_state': 'meadow_to_thread_state', 'MkTimerArmLeeway': 'meadow_MkTimerArmLeeway', 'handle_msc_mk_timer_arm': 'meadow_handle_msc_mk_timer_arm', 'MkTimerFlags': 'meadow_MkTimerFlags', 'MachWait': 'meadow_MachWait', 'MachPortInsertMember': 'meadow_MachPortInsertMember', 'handle_msc_mach_port_allocate_trap': 'meadow_handle_msc_mach_port_allocate_trap', 'handle_msc_mach_reply_port': 'meadow_handle_msc_mach_reply_port', 'handle_msc_task_self_port': 'meadow_handle_msc_task_self_port', 'handle_msc_mk_timer_arm_leeway': 'meadow_handle_msc_mk_timer_arm_leeway', 'MachPortExtractMember': 'meadow_MachPortExtractMember', 'to_vm_prot': 'meadow_to_vm_prot', 'MachPortDestruct': 'meadow_MachPortDestruct', 'SchedClutchTgBucketPri': 'meadow_SchedClutchTgBucketPri', 'handle_decr_trap': 'meadow_handle_decr_trap', 'VmProtection': 'meadow_VmProtection', 'MkTimerArm': 'meadow_MkTimerArm', 'handle_msc_mach_port_insert_right_trap': 'meadow_handle_msc_mach_port_insert_right_trap', 'handle_mach_vmfault': 'meadow_handle_mach_vmfault', 'handle_sched_clutch_cpu_thread_select': 'meadow_handle_sched_clutch_cpu_thread_select', 'TaskSelf': 'meadow_TaskSelf', 'handle_msc_mach_generate_activity_id': 'meadow_handle_msc_mach_generate_activity_id', 'handle_mach_block': 'meadow_handle_mach_block', 'MachThreadSelf': 'meadow_MachThreadSelf', 'MachPortAllocate': 'meadow_MachPortAllocate', 'handle_msc_thread_switch': 'meadow_handle_msc_thread_switch', 'Interrupt': 'meadow_Interrupt', 'handle_user_svc64_exc_arm': 'meadow_handle_user_svc64_exc_arm', 'HostSelf': 'meadow_HostSelf', 'MachReplyPort': 'meadow_MachReplyPort', 'MachVmMap': 'meadow_MachVmMap', 'MachPortDeallocate': 'meadow_MachPortDeallocate', 'dataclass': 'meadow_dataclass', 'HostCreateMachVoucher': 'meadow_HostCreateMachVoucher', 'IokitUserClient': 'meadow_IokitUserClient', 'MachPortFlavor': 'meadow_MachPortFlavor', 'handle_msc_host_create_mach_voucher_trap': 'meadow_handle_msc_host_create_mach_voucher_trap', 'handle_msc_mach_port_unguard_trap': 'meadow_handle_msc_mach_port_unguard_trap', 'handle_msc_mach_port_request_notification_trap': 'meadow_handle_msc_mach_port_request_notification_trap', 'MachVmPurgableControl': 'meadow_MachVmPurgableControl', 'handle_msc_mach_port_construct_trap': 'meadow_handle_msc_mach_port_construct_trap', 'KernelUncategorizedExcArm': 'meadow_KernelUncategorizedExcArm', 'MachPortRequestNotification': 'meadow_MachPortRequestNotification', 'handle_msc_semaphore_signal_trap': 'meadow_handle_msc_semaphore_signal_trap', 'SwitchOption': 'meadow_SwitchOption', 'MachVmAllocate': 'meadow_MachVmAllocate', 'MachGenerateActivityId': 'meadow_MachGenerateActivityId', 'MachIdle': 'meadow_MachIdle', 'MachPortInsertRight': 'meadow_MachPortInsertRight', 'MachPortConstruct': 'meadow_MachPortConstruct', 'Enum': 'meadow_Enum', 'handle_msc_mach_port_type_trap': 'meadow_handle_msc_mach_port_type_trap', 'MachMkrunnable': 'meadow_MachMkrunnable', 'handle_mach_sched': 'meadow_handle_mach_sched', 'handle_msc_mach_port_mod_refs_trap': 'meadow_handle_msc_mach_port_mod_refs_trap', 'KernelDataAbortSameElExcArm': 'meadow_KernelDataAbortSameElExcArm', 'MachPortModRefs': 'meadow_MachPortModRefs', 'handle_msc_mach_msg2_trap': 'meadow_handle_msc_mach_msg2_trap', 'KernReturn': 'meadow_KernReturn'})
