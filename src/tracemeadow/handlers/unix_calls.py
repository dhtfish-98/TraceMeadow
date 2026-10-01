# Derived from pykdebugparser/trace_handlers/bsd.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import ctypes as meadow_ctypes
import enum as meadow_enum
import errno as meadow_errno
from dataclasses import dataclass as meadow_dataclass
from functools import partial as meadow_partial
from signal import Signals as meadow_Signals
import socket as meadow_socket
from typing import List as meadow_List
meadow_IOC_REQUEST_PARAMS = {536870912: 'IOC_VOID', 1073741824: 'IOC_OUT', 2147483648: 'IOC_IN', 3221225472: 'IOC_IN | IOC_OUT', 3758096384: 'IOC_DIRMASK'}

@_name_boundary.class_contract('BscOpenFlags', {})
class meadow_BscOpenFlags(meadow_enum.Enum):
    O_RDONLY = 0
    O_WRONLY = 1
    O_RDWR = 2
    O_ACCMODE = 3
    O_NONBLOCK = 4
    O_APPEND = 8
    O_SHLOCK = 16
    O_EXLOCK = 32
    O_ASYNC = 64
    O_NOFOLLOW = 256
    O_CREAT = 512
    O_TRUNC = 1024
    O_EXCL = 2048
    O_EVTONLY = 32768
    O_SYMLINK = 2097152
    O_CLOEXEC = 16777216
meadow_S_IFMT = 61440

@_name_boundary.class_contract('StatFlags', {'S_IXOTH': 'meadow_S_IXOTH', 'S_IWOTH': 'meadow_S_IWOTH', 'S_IROTH': 'meadow_S_IROTH', 'S_IXGRP': 'meadow_S_IXGRP', 'S_IWGRP': 'meadow_S_IWGRP', 'S_IRGRP': 'meadow_S_IRGRP', 'S_IXUSR': 'meadow_S_IXUSR', 'S_IWUSR': 'meadow_S_IWUSR', 'S_IRUSR': 'meadow_S_IRUSR', 'S_ISTXT': 'meadow_S_ISTXT', 'S_ISGID': 'meadow_S_ISGID', 'S_ISUID': 'meadow_S_ISUID', 'S_IFIFO': 'meadow_S_IFIFO', 'S_IFCHR': 'meadow_S_IFCHR', 'S_IFDIR': 'meadow_S_IFDIR', 'S_IFBLK': 'meadow_S_IFBLK', 'S_IFREG': 'meadow_S_IFREG', 'S_IFLNK': 'meadow_S_IFLNK', 'S_IFSOCK': 'meadow_S_IFSOCK'})
class meadow_StatFlags(meadow_enum.Flag):
    meadow_S_IXOTH = 1
    meadow_S_IWOTH = 2
    meadow_S_IROTH = 4
    meadow_S_IXGRP = 8
    meadow_S_IWGRP = 16
    meadow_S_IRGRP = 32
    meadow_S_IXUSR = 64
    meadow_S_IWUSR = 128
    meadow_S_IRUSR = 256
    meadow_S_ISTXT = 512
    meadow_S_ISGID = 1024
    meadow_S_ISUID = 2048
    meadow_S_IFIFO = 4096
    meadow_S_IFCHR = 8192
    meadow_S_IFDIR = 16384
    meadow_S_IFBLK = 24576
    meadow_S_IFREG = 32768
    meadow_S_IFLNK = 40960
    meadow_S_IFSOCK = 49152

@_name_boundary.class_contract('SocketMsgFlags', {})
class meadow_SocketMsgFlags(meadow_enum.Enum):
    MSG_OOB = 1
    MSG_PEEK = 2
    MSG_DONTROUTE = 4
    MSG_EOR = 8
    MSG_TRUNC = 16
    MSG_CTRUNC = 32
    MSG_WAITALL = 64
    MSG_DONTWAIT = 128
    MSG_EOF = 256
    MSG_WAITSTREAM = 512
    MSG_FLUSH = 1024
    MSG_HOLD = 2048
    MSG_SEND = 4096
    MSG_HAVEMORE = 8192
    MSG_RCVMORE = 16384
    MSG_COMPAT = 32768
    MSG_NEEDSA = 65536
    MSG_NBIO = 131072
    MSG_SKIPCFIL = 262144
    MSG_USEUPCALL = 2147483648

@_name_boundary.class_contract('BscAccessFlags', {})
class meadow_BscAccessFlags(meadow_enum.Enum):
    F_OK = 0
    X_OK = 1
    W_OK = 2
    R_OK = 4

@_name_boundary.class_contract('BscChangeableFlags', {})
class meadow_BscChangeableFlags(meadow_enum.Enum):
    UF_NODUMP = 1
    UF_IMMUTABLE = 2
    UF_APPEND = 4
    UF_OPAQUE = 8
    UF_HIDDEN = 32768
    SF_ARCHIVED = 65536
    SF_IMMUTABLE = 131072
    SF_APPEND = 262144

@_name_boundary.class_contract('SigprocmaskFlags', {})
class meadow_SigprocmaskFlags(meadow_enum.Enum):
    SIG_BLOCK = 1
    SIG_UNBLOCK = 2
    SIG_SETMASK = 3

@_name_boundary.class_contract('FcntlCmd', {})
class meadow_FcntlCmd(meadow_enum.Enum):
    F_DUPFD = 0
    F_GETFD = 1
    F_SETFD = 2
    F_GETFL = 3
    F_SETFL = 4
    F_GETOWN = 5
    F_SETOWN = 6
    F_GETLK = 7
    F_SETLK = 8
    F_SETLKW = 9
    F_SETLKWTIMEOUT = 10
    F_FLUSH_DATA = 40
    F_CHKCLEAN = 41
    F_PREALLOCATE = 42
    F_SETSIZE = 43
    F_RDADVISE = 44
    F_RDAHEAD = 45
    F_NOCACHE = 48
    F_LOG2PHYS = 49
    F_GETPATH = 50
    F_FULLFSYNC = 51
    F_PATHPKG_CHECK = 52
    F_FREEZE_FS = 53
    F_THAW_FS = 54
    F_GLOBAL_NOCACHE = 55
    F_OPENFROM = 56
    F_UNLINKFROM = 57
    F_CHECK_OPENEVT = 58
    F_ADDSIGS = 59
    F_MARKDEPENDENCY = 60
    F_ADDFILESIGS = 61
    F_NODIRECT = 62
    F_GETPROTECTIONCLASS = 63
    F_SETPROTECTIONCLASS = 64
    F_LOG2PHYS_EXT = 65
    F_GETLKPID = 66
    F_DUPFD_CLOEXEC = 67
    F_SETSTATICCONTENT = 68
    F_MOVEDATAEXTENTS = 69
    F_SETBACKINGSTORE = 70
    F_GETPATH_MTMINFO = 71
    F_GETCODEDIR = 72
    F_SETNOSIGPIPE = 73
    F_GETNOSIGPIPE = 74
    F_TRANSCODEKEY = 75
    F_SINGLE_WRITER = 76
    F_GETPROTECTIONLEVEL = 77
    F_FINDSIGS = 78
    F_GETDEFAULTPROTLEVEL = 79
    F_MAKECOMPRESSED = 80
    F_SET_GREEDY_MODE = 81
    F_SETIOTYPE = 82
    F_ADDFILESIGS_FOR_DYLD_SIM = 83
    F_RECYCLE = 84
    F_BARRIERFSYNC = 85
    F_OFD_SETLK = 90
    F_OFD_SETLKW = 91
    F_OFD_GETLK = 92
    F_OFD_SETLKWTIMEOUT = 93
    F_OFD_GETLKPID = 94
    F_SETCONFINED = 95
    F_GETCONFINED = 96
    F_ADDFILESIGS_RETURN = 97
    F_CHECK_LV = 98
    F_PUNCHHOLE = 99
    F_TRIM_ACTIVE_FILE = 100
    F_SPECULATIVE_READ = 101
    F_GETPATH_NOFIRMLINK = 102
    F_ADDFILESIGS_INFO = 103
    F_ADDFILESUPPL = 104
    F_GETSIGSINFO = 105

@_name_boundary.class_contract('PriorityWhich', {})
class meadow_PriorityWhich(meadow_enum.Enum):
    PRIO_PROCESS = 0
    PRIO_PGRP = 1
    PRIO_USER = 2
    PRIO_DARWIN_THREAD = 3
    PRIO_DARWIN_PROCESS = 4
    PRIO_DARWIN_GPU = 5
    PRIO_DARWIN_ROLE = 6
    PRIO_DARWIN_GAME_MODE = 7
    PRIO_DARWIN_CARPLAY_MODE = 8

@_name_boundary.class_contract('SocketOptionName', {})
class meadow_SocketOptionName(meadow_enum.Enum):
    SO_DEBUG = 1
    SO_ACCEPTCONN = 2
    SO_REUSEADDR = 4
    SO_KEEPALIVE = 8
    SO_DONTROUTE = 16
    SO_BROADCAST = 32
    SO_USELOOPBACK = 64
    SO_LINGER = 128
    SO_OOBINLINE = 256
    SO_REUSEPORT = 512
    SO_TIMESTAMP = 1024
    SO_TIMESTAMP_MONOTONIC = 2048
    SO_ACCEPTFILTER = 4096
    SO_SNDBUF = 4097
    SO_RCVBUF = 4098
    SO_SNDLOWAT = 4099
    SO_RCVLOWAT = 4100
    SO_SNDTIMEO = 4101
    SO_RCVTIMEO = 4102
    SO_ERROR = 4103
    SO_TYPE = 4104
    SO_LABEL = 4112
    SO_PEERLABEL = 4113
    SO_NREAD = 4128
    SO_NKE = 4129
    SO_NOSIGPIPE = 4130
    SO_NOADDRERR = 4131
    SO_NWRITE = 4132
    SO_REUSESHAREUID = 4133
    SO_NOTIFYCONFLICT = 4134
    SO_UPCALLCLOSEWAIT = 4135
    SO_LINGER_SEC = 4224
    SO_RESTRICTIONS = 4225
    SO_RANDOMPORT = 4226
    SO_NP_EXTENSIONS = 4227
    SO_EXECPATH = 4229
    SO_TRAFFIC_CLASS = 4230
    SO_RECV_TRAFFIC_CLASS = 4231
    SO_TRAFFIC_CLASS_DBG = 4232
    SO_OPTION_UNUSED_0 = 4233
    SO_PRIVILEGED_TRAFFIC_CLASS = 4240
    SO_DEFUNCTIT = 4241
    SO_DEFUNCTOK = 4352
    SO_ISDEFUNCT = 4353
    SO_OPPORTUNISTIC = 4354
    SO_FLUSH = 4355
    SO_RECV_ANYIF = 4356
    SO_TRAFFIC_MGT_BACKGROUND = 4357
    SO_FLOW_DIVERT_TOKEN = 4358
    SO_DELEGATED = 4359
    SO_DELEGATED_UUID = 4360
    SO_NECP_ATTRIBUTES = 4361
    SO_CFIL_SOCK_ID = 4368
    SO_NECP_CLIENTUUID = 4369
    SO_NUMRCVPKT = 4370
    SO_AWDL_UNRESTRICTED = 4371
    SO_EXTENDED_BK_IDLE = 4372
    SO_MARK_CELLFALLBACK = 4373
    SO_NET_SERVICE_TYPE = 4374
    SO_QOSMARKING_POLICY_OVERRIDE = 4375
    SO_INTCOPROC_ALLOW = 4376
    SO_NETSVC_MARKING_LEVEL = 4377
    SO_NECP_LISTENUUID = 4384
    SO_MPKL_SEND_INFO = 4386
    SO_STATISTICS_EVENT = 4387
    SO_WANT_KEV_SOCKET_CLOSED = 4388
    SO_DONTTRUNC = 8192
    SO_WANTMORE = 16384
    SO_WANTOOBFLAG = 32768
    SO_NOWAKEFROMSLEEP = 65536
    SO_NOAPNFALLBK = 131072
    SO_TIMESTAMP_CONTINUOUS = 262144

@_name_boundary.callable_contract({'level': 'meadow_level_f212aa4', 'option_name': 'meadow_option_name_c56c3a5'}, 'sockopt_format_level_and_option')
def meadow_sockopt_format_level_and_option(meadow_level_f212aa4, meadow_option_name_c56c3a5):
    if meadow_level_f212aa4 == meadow_socket.SOL_SOCKET:
        return ('SOL_SOCKET', _name_boundary.attributes(meadow_SocketOptionName(meadow_option_name_c56c3a5))['name'])
    else:
        return (meadow_level_f212aa4, meadow_option_name_c56c3a5)

@_name_boundary.class_contract('RusageWho', {})
class meadow_RusageWho(meadow_enum.Enum):
    RUSAGE_CHILDREN = -1
    RUSAGE_SELF = 0

@_name_boundary.class_contract('FlockOperation', {})
class meadow_FlockOperation(meadow_enum.Enum):
    LOCK_SH = 1
    LOCK_EX = 2
    LOCK_NB = 4
    LOCK_UN = 8

@_name_boundary.class_contract('CsopsOps', {})
class meadow_CsopsOps(meadow_enum.Enum):
    CS_OPS_STATUS = 0
    CS_OPS_MARKINVALID = 1
    CS_OPS_MARKHARD = 2
    CS_OPS_MARKKILL = 3
    CS_OPS_PIDPATH = 4
    CS_OPS_CDHASH = 5
    CS_OPS_PIDOFFSET = 6
    CS_OPS_ENTITLEMENTS_BLOB = 7
    CS_OPS_MARKRESTRICT = 8
    CS_OPS_SET_STATUS = 9
    CS_OPS_BLOB = 10
    CS_OPS_IDENTITY = 11
    CS_OPS_CLEARINSTALLER = 12
    CS_OPS_CLEARPLATFORM = 13
    CS_OPS_TEAMID = 14
    CS_OPS_CLEAR_LV = 15
    CS_OPS_16 = 16

@_name_boundary.class_contract('ProcInfoCall', {})
class meadow_ProcInfoCall(meadow_enum.Enum):
    PROC_INFO_CALL_LISTPIDS = 1
    PROC_INFO_CALL_PIDINFO = 2
    PROC_INFO_CALL_PIDFDINFO = 3
    PROC_INFO_CALL_KERNMSGBUF = 4
    PROC_INFO_CALL_SETCONTROL = 5
    PROC_INFO_CALL_PIDFILEPORTINFO = 6
    PROC_INFO_CALL_TERMINATE = 7
    PROC_INFO_CALL_DIRTYCONTROL = 8
    PROC_INFO_CALL_PIDRUSAGE = 9
    PROC_INFO_CALL_PIDORIGINATORINFO = 10
    PROC_INFO_CALL_LISTCOALITIONS = 11
    PROC_INFO_CALL_CANUSEFGHW = 12
    PROC_INFO_CALL_PIDDYNKQUEUEINFO = 13
    PROC_INFO_CALL_UDATA_INFO = 14
    PROC_INFO_CALL_SET_DYLD_IMAGES = 15
    PROC_INFO_CALL_TERMINATE_RSR = 16
    PROC_INFO_CALL_SIGNAL_AUDITTOKEN = 17
    PROC_INFO_CALL_TERMINATE_AUDITTOKEN = 18
    PROC_INFO_CALL_DELEGATE_SIGNAL = 19
    PROC_INFO_CALL_DELEGATE_TERMINATE = 20

@_name_boundary.class_contract('FsSnapshotOp', {})
class meadow_FsSnapshotOp(meadow_enum.Enum):
    SNAPSHOT_OP_CREATE = 1
    SNAPSHOT_OP_DELETE = 2
    SNAPSHOT_OP_RENAME = 3
    SNAPSHOT_OP_MOUNT = 4
    SNAPSHOT_OP_REVERT = 5
    SNAPSHOT_OP_ROOT = 6

@_name_boundary.callable_contract({'flags': 'meadow_flags_a143db1'}, 'serialize_open_flags')
def meadow_serialize_open_flags(meadow_flags_a143db1: int) -> meadow_List[meadow_BscOpenFlags]:
    meadow_call_flags_b76cfc9 = []
    for meadow_flag_de915d6 in (meadow_BscOpenFlags.O_RDWR, meadow_BscOpenFlags.O_WRONLY):
        if meadow_flags_a143db1 & meadow_flag_de915d6.value:
            meadow_call_flags_b76cfc9.append(meadow_flag_de915d6)
            break
    else:
        meadow_call_flags_b76cfc9.append(meadow_BscOpenFlags.O_RDONLY)
    for meadow_flag_de915d6 in (meadow_BscOpenFlags.O_CREAT, meadow_BscOpenFlags.O_APPEND, meadow_BscOpenFlags.O_TRUNC, meadow_BscOpenFlags.O_EXCL, meadow_BscOpenFlags.O_NONBLOCK, meadow_BscOpenFlags.O_SHLOCK, meadow_BscOpenFlags.O_EXLOCK, meadow_BscOpenFlags.O_NOFOLLOW, meadow_BscOpenFlags.O_SYMLINK, meadow_BscOpenFlags.O_EVTONLY, meadow_BscOpenFlags.O_CLOEXEC):
        if meadow_flags_a143db1 & meadow_flag_de915d6.value:
            meadow_call_flags_b76cfc9.append(meadow_flag_de915d6)
    return meadow_call_flags_b76cfc9

@_name_boundary.callable_contract({'flags': 'meadow_flags_9972770'}, 'serialize_stat_flags')
def meadow_serialize_stat_flags(meadow_flags_9972770: int) -> meadow_List[meadow_StatFlags]:
    meadow_stat_flags_d80185a = []
    for meadow_flag_3573f35 in list(meadow_StatFlags):
        if meadow_flag_3573f35.value & meadow_S_IFMT:
            if meadow_flags_9972770 & meadow_S_IFMT == meadow_flag_3573f35.value:
                meadow_stat_flags_d80185a.append(meadow_flag_3573f35)
        elif meadow_flag_3573f35.value & meadow_flags_9972770:
            meadow_stat_flags_d80185a.append(meadow_flag_3573f35)
    return meadow_stat_flags_d80185a

@_name_boundary.callable_contract({'end_event': 'meadow_end_event_558c351', 'success_name': 'meadow_success_name_f1af12d', 'fmt': 'meadow_fmt_08a4b1b'}, 'serialize_result')
def meadow_serialize_result(meadow_end_event_558c351, meadow_success_name_f1af12d='', meadow_fmt_08a4b1b=lambda meadow_x_5de3c25: meadow_x_5de3c25) -> str:
    meadow_error_code_69247a8 = meadow_end_event_558c351.values[0]
    meadow_res_f5ab95d = meadow_end_event_558c351.values[1]
    if meadow_error_code_69247a8 in meadow_errno.errorcode:
        meadow_err_b36a37f = f'errno: {meadow_errno.errorcode[meadow_error_code_69247a8]}({meadow_error_code_69247a8})'
    else:
        meadow_err_b36a37f = f'errno: {meadow_error_code_69247a8}'
    meadow_success_f74b5a2 = f'{meadow_success_name_f1af12d}: {meadow_fmt_08a4b1b(meadow_res_f5ab95d)}' if meadow_success_name_f1af12d else ''
    return meadow_success_f74b5a2 if not meadow_error_code_69247a8 else meadow_err_b36a37f

@_name_boundary.callable_contract({'flags': 'meadow_flags_b32838b'}, 'serialize_access_flags')
def meadow_serialize_access_flags(meadow_flags_b32838b: int) -> meadow_List[meadow_BscAccessFlags]:
    meadow_amode_46a5d3f = [meadow_flag_a368242 for meadow_flag_a368242 in meadow_BscAccessFlags if meadow_flag_a368242.value & meadow_flags_b32838b]
    if not meadow_amode_46a5d3f:
        meadow_amode_46a5d3f = [meadow_BscAccessFlags.F_OK]
    return meadow_amode_46a5d3f

@_name_boundary.class_contract('BscOpen', {})
@meadow_dataclass
class meadow_BscOpen:
    ktraces: meadow_List
    path: str
    flags: meadow_List
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_f669cde'}, '__str__')
    def __str__(meadow_self_f669cde):
        meadow_no_cancel_0ae7046 = '_nocancel' if meadow_self_f669cde.no_cancel else ''
        return f'''open{meadow_no_cancel_0ae7046}("{meadow_self_f669cde.path}", {' | '.join(map(lambda meadow_f_577a685: _name_boundary.attributes(meadow_f_577a685)['name'], meadow_self_f669cde.flags))}), {meadow_self_f669cde.result}'''

@_name_boundary.class_contract('BscOpenat', {})
@meadow_dataclass
class meadow_BscOpenat:
    ktraces: meadow_List
    dirfd: int
    path: str
    flags: meadow_List
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_6361672'}, '__str__')
    def __str__(meadow_self_6361672):
        meadow_no_cancel_dbbd0dc = '_nocancel' if meadow_self_6361672.no_cancel else ''
        return f'''openat{meadow_no_cancel_dbbd0dc}({meadow_self_6361672.dirfd}, "{meadow_self_6361672.path}", {' | '.join(map(lambda meadow_f_3b4c1fe: _name_boundary.attributes(meadow_f_3b4c1fe)['name'], meadow_self_6361672.flags))}), {meadow_self_6361672.result}'''

@_name_boundary.class_contract('BscRead', {})
@meadow_dataclass
class meadow_BscRead:
    ktraces: meadow_List
    fd: int
    address: int
    size: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_f0bfbc9'}, '__str__')
    def __str__(meadow_self_f0bfbc9):
        meadow_no_cancel_73aef71 = '_nocancel' if meadow_self_f0bfbc9.no_cancel else ''
        return f'read{meadow_no_cancel_73aef71}({meadow_self_f0bfbc9.fd}, {hex(meadow_self_f0bfbc9.address)}, {meadow_self_f0bfbc9.size}), {meadow_self_f0bfbc9.result}'

@_name_boundary.class_contract('BscWrite', {})
@meadow_dataclass
class meadow_BscWrite:
    ktraces: meadow_List
    fd: int
    address: int
    size: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_29d79b0'}, '__str__')
    def __str__(meadow_self_29d79b0):
        meadow_no_cancel_32f029e = '_nocancel' if meadow_self_29d79b0.no_cancel else ''
        return f'write{meadow_no_cancel_32f029e}({meadow_self_29d79b0.fd}, {hex(meadow_self_29d79b0.address)}, {meadow_self_29d79b0.size}), {meadow_self_29d79b0.result}'

@_name_boundary.class_contract('BscPread', {})
@meadow_dataclass
class meadow_BscPread:
    ktraces: meadow_List
    fd: int
    address: int
    size: int
    offset: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_7926000'}, '__str__')
    def __str__(meadow_self_7926000):
        meadow_no_cancel_99647ea = '_nocancel' if meadow_self_7926000.no_cancel else ''
        return f'pread{meadow_no_cancel_99647ea}({meadow_self_7926000.fd}, {hex(meadow_self_7926000.address)}, {meadow_self_7926000.size}, {hex(meadow_self_7926000.offset)}), {meadow_self_7926000.result}'

@_name_boundary.class_contract('BscPwrite', {})
@meadow_dataclass
class meadow_BscPwrite:
    ktraces: meadow_List
    fd: int
    address: int
    size: int
    offset: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_603b501'}, '__str__')
    def __str__(meadow_self_603b501):
        meadow_no_cancel_ddddc40 = '_nocancel' if meadow_self_603b501.no_cancel else ''
        return f'pwrite{meadow_no_cancel_ddddc40}({meadow_self_603b501.fd}, {hex(meadow_self_603b501.address)}, {meadow_self_603b501.size}, {hex(meadow_self_603b501.offset)}), {meadow_self_603b501.result}'

@_name_boundary.class_contract('BscSysFstat64', {})
@meadow_dataclass
class meadow_BscSysFstat64:
    ktraces: meadow_List
    fd: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2f3399f'}, '__str__')
    def __str__(meadow_self_2f3399f):
        meadow_rep_cd55936 = f'fstat64({meadow_self_2f3399f.fd})'
        if meadow_self_2f3399f.result:
            meadow_rep_cd55936 += f', {meadow_self_2f3399f.result}'
        return meadow_rep_cd55936

@_name_boundary.class_contract('BscLstat64', {})
@meadow_dataclass
class meadow_BscLstat64:
    ktraces: meadow_List
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e428190'}, '__str__')
    def __str__(meadow_self_e428190):
        meadow_rep_cd22829 = f'lstat64("{meadow_self_e428190.path}")'
        if meadow_self_e428190.result:
            meadow_rep_cd22829 += f', {meadow_self_e428190.result}'
        return meadow_rep_cd22829

@_name_boundary.class_contract('BscGetdirentries64', {})
@meadow_dataclass
class meadow_BscGetdirentries64:
    ktraces: meadow_List
    fd: int
    buf: int
    bufsize: int
    position: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1dc31e1'}, '__str__')
    def __str__(meadow_self_1dc31e1):
        return f'getdirentries64({meadow_self_1dc31e1.fd}, {hex(meadow_self_1dc31e1.buf)}, {meadow_self_1dc31e1.bufsize}, {hex(meadow_self_1dc31e1.position)}), {meadow_self_1dc31e1.result}'

@_name_boundary.class_contract('BscStatfs64', {})
@meadow_dataclass
class meadow_BscStatfs64:
    ktraces: meadow_List
    path: str
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f949f20'}, '__str__')
    def __str__(meadow_self_f949f20):
        meadow_rep_a35ee22 = f'statfs64("{meadow_self_f949f20.path}", {hex(meadow_self_f949f20.buf)})'
        if meadow_self_f949f20.result:
            meadow_rep_a35ee22 += f', {meadow_self_f949f20.result}'
        return meadow_rep_a35ee22

@_name_boundary.class_contract('BscFstatfs64', {})
@meadow_dataclass
class meadow_BscFstatfs64:
    ktraces: meadow_List
    fd: int
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1cfd0f8'}, '__str__')
    def __str__(meadow_self_1cfd0f8):
        meadow_rep_1c2bc5e = f'fstatfs64({meadow_self_1cfd0f8.fd}, {hex(meadow_self_1cfd0f8.buf)})'
        if meadow_self_1cfd0f8.result:
            meadow_rep_1c2bc5e += f', {meadow_self_1cfd0f8.result}'
        return meadow_rep_1c2bc5e

@_name_boundary.class_contract('BscGetfsstat64', {})
@meadow_dataclass
class meadow_BscGetfsstat64:
    ktraces: meadow_List
    buf: int
    bufsize: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c9ea5ab'}, '__str__')
    def __str__(meadow_self_c9ea5ab):
        return f'getfsstat64({hex(meadow_self_c9ea5ab.buf)}, {meadow_self_c9ea5ab.bufsize}, {meadow_self_c9ea5ab.flags}), {meadow_self_c9ea5ab.result}'

@_name_boundary.class_contract('BscPthreadFchdir', {})
@meadow_dataclass
class meadow_BscPthreadFchdir:
    ktraces: meadow_List
    fd: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7fa4d45'}, '__str__')
    def __str__(meadow_self_7fa4d45):
        meadow_rep_f0a0dc0 = f'pthread_fchdir({meadow_self_7fa4d45.fd})'
        if meadow_self_7fa4d45.result:
            meadow_rep_f0a0dc0 += f', {meadow_self_7fa4d45.result}'
        return meadow_rep_f0a0dc0

@_name_boundary.class_contract('BscAudit', {})
@meadow_dataclass
class meadow_BscAudit:
    ktraces: meadow_List
    record: int
    length: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_982601a'}, '__str__')
    def __str__(meadow_self_982601a):
        meadow_rep_c17dae8 = f'audit({hex(meadow_self_982601a.record)}, {meadow_self_982601a.length})'
        if meadow_self_982601a.result:
            meadow_rep_c17dae8 += f', {meadow_self_982601a.result}'
        return meadow_rep_c17dae8

@_name_boundary.class_contract('BscAuditon', {})
@meadow_dataclass
class meadow_BscAuditon:
    ktraces: meadow_List
    cmd: int
    data: int
    length: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_016fdce'}, '__str__')
    def __str__(meadow_self_016fdce):
        meadow_rep_01fb56c = f'auditon({meadow_self_016fdce.cmd}, {hex(meadow_self_016fdce.data)}, {meadow_self_016fdce.length})'
        if meadow_self_016fdce.result:
            meadow_rep_01fb56c += f', {meadow_self_016fdce.result}'
        return meadow_rep_01fb56c

@_name_boundary.class_contract('BscGetauid', {})
@meadow_dataclass
class meadow_BscGetauid:
    ktraces: meadow_List
    auid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_56a0790'}, '__str__')
    def __str__(meadow_self_56a0790):
        meadow_rep_90a2f99 = f'getauid({hex(meadow_self_56a0790.auid)})'
        if meadow_self_56a0790.result:
            meadow_rep_90a2f99 += f', {meadow_self_56a0790.result}'
        return meadow_rep_90a2f99

@_name_boundary.class_contract('BscSetauid', {})
@meadow_dataclass
class meadow_BscSetauid:
    ktraces: meadow_List
    auid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b0ddeeb'}, '__str__')
    def __str__(meadow_self_b0ddeeb):
        meadow_rep_049676a = f'setauid({hex(meadow_self_b0ddeeb.auid)})'
        if meadow_self_b0ddeeb.result:
            meadow_rep_049676a += f', {meadow_self_b0ddeeb.result}'
        return meadow_rep_049676a

@_name_boundary.class_contract('BscBsdthreadCreate', {})
@meadow_dataclass
class meadow_BscBsdthreadCreate:
    ktraces: meadow_List
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_bc131cd'}, '__str__')
    def __str__(meadow_self_bc131cd):
        return 'thread_create()'

@_name_boundary.class_contract('BscKqueue', {})
@meadow_dataclass
class meadow_BscKqueue:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ea372b3'}, '__str__')
    def __str__(meadow_self_ea372b3):
        return f'kqueue(), {meadow_self_ea372b3.result}'

@_name_boundary.class_contract('BscKevent', {})
@meadow_dataclass
class meadow_BscKevent:
    ktraces: meadow_List
    kq: int
    changelist: int
    nchanges: int
    eventlist: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_714c499'}, '__str__')
    def __str__(meadow_self_714c499):
        return f'kevent({meadow_self_714c499.kq}, {hex(meadow_self_714c499.changelist)}, {meadow_self_714c499.nchanges}, {hex(meadow_self_714c499.eventlist)}), {meadow_self_714c499.result}'

@_name_boundary.class_contract('BscLchown', {})
@meadow_dataclass
class meadow_BscLchown:
    ktraces: meadow_List
    path: str
    owner: int
    group: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_13dfc4f'}, '__str__')
    def __str__(meadow_self_13dfc4f):
        meadow_rep_eb16605 = f'lchown("{meadow_self_13dfc4f.path}", {meadow_self_13dfc4f.owner}, {meadow_self_13dfc4f.group})'
        if meadow_self_13dfc4f.result:
            meadow_rep_eb16605 += f', {meadow_self_13dfc4f.result}'
        return meadow_rep_eb16605

@_name_boundary.class_contract('BscBsdthreadRegister', {})
@meadow_dataclass
class meadow_BscBsdthreadRegister:
    ktraces: meadow_List
    threadstart: int
    wqthread: int
    pthsize: int
    dummy_value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_62af601'}, '__str__')
    def __str__(meadow_self_62af601):
        meadow_rep_cd8dc92 = f'thread_register({hex(meadow_self_62af601.threadstart)}, {hex(meadow_self_62af601.wqthread)}, {meadow_self_62af601.pthsize}, {hex(meadow_self_62af601.dummy_value)})'
        if meadow_self_62af601.result:
            meadow_rep_cd8dc92 += f', {meadow_self_62af601.result}'
        return meadow_rep_cd8dc92

@_name_boundary.class_contract('BscWorkqOpen', {})
@meadow_dataclass
class meadow_BscWorkqOpen:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c217d09'}, '__str__')
    def __str__(meadow_self_c217d09):
        meadow_rep_2db4975 = 'workq_open()'
        if meadow_self_c217d09.result:
            meadow_rep_2db4975 += f', {meadow_self_c217d09.result}'
        return meadow_rep_2db4975

@_name_boundary.class_contract('BscWorkqKernreturn', {})
@meadow_dataclass
class meadow_BscWorkqKernreturn:
    ktraces: meadow_List
    options: int
    item: int
    affinity: int
    prio: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c6286c7'}, '__str__')
    def __str__(meadow_self_c6286c7):
        return f'workq_kernreturn({meadow_self_c6286c7.options}, {hex(meadow_self_c6286c7.item)}, {meadow_self_c6286c7.affinity}, {meadow_self_c6286c7.prio}), {meadow_self_c6286c7.result}'

@_name_boundary.class_contract('BscKevent64', {})
@meadow_dataclass
class meadow_BscKevent64:
    ktraces: meadow_List
    kq: int
    changelist: int
    nchanges: int
    eventlist: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2541295'}, '__str__')
    def __str__(meadow_self_2541295):
        return f'kevent64({meadow_self_2541295.kq}, {hex(meadow_self_2541295.changelist)}, {meadow_self_2541295.nchanges}, {hex(meadow_self_2541295.eventlist)}), {meadow_self_2541295.result}'

@_name_boundary.class_contract('BscThreadSelfid', {})
@meadow_dataclass
class meadow_BscThreadSelfid:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0bca739'}, '__str__')
    def __str__(meadow_self_0bca739):
        return f'thread_selfid(), {meadow_self_0bca739.result}'

@_name_boundary.class_contract('BscKeventQos', {})
@meadow_dataclass
class meadow_BscKeventQos:
    ktraces: meadow_List
    kq: int
    changelist: int
    nchanges: int
    eventlist: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a68cccd'}, '__str__')
    def __str__(meadow_self_a68cccd):
        return f'kevent_qos({meadow_self_a68cccd.kq}, {hex(meadow_self_a68cccd.changelist)}, {meadow_self_a68cccd.nchanges}, {hex(meadow_self_a68cccd.eventlist)}), {meadow_self_a68cccd.result}'

@_name_boundary.class_contract('BscKeventId', {})
@meadow_dataclass
class meadow_BscKeventId:
    ktraces: meadow_List
    kq: int
    changelist: int
    nchanges: int
    eventlist: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ef6217f'}, '__str__')
    def __str__(meadow_self_ef6217f):
        return f'kevent_id({meadow_self_ef6217f.kq}, {hex(meadow_self_ef6217f.changelist)}, {meadow_self_ef6217f.nchanges}, {hex(meadow_self_ef6217f.eventlist)}), {meadow_self_ef6217f.result}'

@_name_boundary.class_contract('BscMacSyscall', {})
@meadow_dataclass
class meadow_BscMacSyscall:
    ktraces: meadow_List
    policy: int
    call: int
    arg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8bd42aa'}, '__str__')
    def __str__(meadow_self_8bd42aa):
        meadow_rep_cce752e = f'mac_syscall({hex(meadow_self_8bd42aa.policy)}, {meadow_self_8bd42aa.call}, {hex(meadow_self_8bd42aa.arg)})'
        if meadow_self_8bd42aa.result:
            meadow_rep_cce752e += f', {meadow_self_8bd42aa.result}'
        return meadow_rep_cce752e

@_name_boundary.class_contract('BscPselect', {})
@meadow_dataclass
class meadow_BscPselect:
    ktraces: meadow_List
    nfds: int
    readfds: int
    writefds: int
    errorfds: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_6f1c91e'}, '__str__')
    def __str__(meadow_self_6f1c91e):
        meadow_no_cancel_3a65340 = '_nocancel' if meadow_self_6f1c91e.no_cancel else ''
        return f'pselect{meadow_no_cancel_3a65340}({meadow_self_6f1c91e.nfds}, {hex(meadow_self_6f1c91e.readfds)}, {hex(meadow_self_6f1c91e.writefds)}, {hex(meadow_self_6f1c91e.errorfds)}), {meadow_self_6f1c91e.result}'

@_name_boundary.class_contract('BscFsgetpath', {})
@meadow_dataclass
class meadow_BscFsgetpath:
    ktraces: meadow_List
    buf: int
    bufsize: int
    fsid: int
    objid: int
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b4f7600'}, '__str__')
    def __str__(meadow_self_b4f7600):
        meadow_rep_90b2339 = f'fsgetpath({hex(meadow_self_b4f7600.buf)}, {meadow_self_b4f7600.bufsize}, {hex(meadow_self_b4f7600.fsid)}, {meadow_self_b4f7600.objid}), {meadow_self_b4f7600.result}'
        if meadow_self_b4f7600.path:
            meadow_rep_90b2339 += f' path: "{meadow_self_b4f7600.path}"'
        return meadow_rep_90b2339

@_name_boundary.class_contract('BscSysFileportMakeport', {})
@meadow_dataclass
class meadow_BscSysFileportMakeport:
    ktraces: meadow_List
    fd: int
    portnamep: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1868962'}, '__str__')
    def __str__(meadow_self_1868962):
        meadow_rep_c8a9382 = f'fileport_makeport({meadow_self_1868962.fd}, {hex(meadow_self_1868962.portnamep)})'
        if meadow_self_1868962.result:
            meadow_rep_c8a9382 += f', {meadow_self_1868962.result}'
        return meadow_rep_c8a9382

@_name_boundary.class_contract('BscSysFileportMakefd', {})
@meadow_dataclass
class meadow_BscSysFileportMakefd:
    ktraces: meadow_List
    port: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e830864'}, '__str__')
    def __str__(meadow_self_e830864):
        return f'fileport_makefd({meadow_self_e830864.port}), {meadow_self_e830864.result}'

@_name_boundary.class_contract('BscAuditSessionPort', {})
@meadow_dataclass
class meadow_BscAuditSessionPort:
    ktraces: meadow_List
    asid: int
    portnamep: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c2862ba'}, '__str__')
    def __str__(meadow_self_c2862ba):
        meadow_rep_aef7306 = f'audit_session_port({meadow_self_c2862ba.asid}, {hex(meadow_self_c2862ba.portnamep)})'
        if meadow_self_c2862ba.result:
            meadow_rep_aef7306 += f', {meadow_self_c2862ba.result}'
        return meadow_rep_aef7306

@_name_boundary.class_contract('BscPidSuspend', {})
@meadow_dataclass
class meadow_BscPidSuspend:
    ktraces: meadow_List
    pid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d0690d2'}, '__str__')
    def __str__(meadow_self_d0690d2):
        meadow_rep_1d60fda = f'pid_suspend({meadow_self_d0690d2.pid})'
        if meadow_self_d0690d2.result:
            meadow_rep_1d60fda += f', {meadow_self_d0690d2.result}'
        return meadow_rep_1d60fda

@_name_boundary.class_contract('BscPidResume', {})
@meadow_dataclass
class meadow_BscPidResume:
    ktraces: meadow_List
    pid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_71f1a7c'}, '__str__')
    def __str__(meadow_self_71f1a7c):
        meadow_rep_5f37d62 = f'pid_resume({meadow_self_71f1a7c.pid})'
        if meadow_self_71f1a7c.result:
            meadow_rep_5f37d62 += f', {meadow_self_71f1a7c.result}'
        return meadow_rep_5f37d62

@_name_boundary.class_contract('BscPidHibernate', {})
@meadow_dataclass
class meadow_BscPidHibernate:
    ktraces: meadow_List
    pid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b6dfaf0'}, '__str__')
    def __str__(meadow_self_b6dfaf0):
        meadow_rep_babdf8d = f'pid_hibernate({meadow_self_b6dfaf0.pid})'
        if meadow_self_b6dfaf0.result:
            meadow_rep_babdf8d += f', {meadow_self_b6dfaf0.result}'
        return meadow_rep_babdf8d

@_name_boundary.class_contract('BscPidShutdownSockets', {})
@meadow_dataclass
class meadow_BscPidShutdownSockets:
    ktraces: meadow_List
    pid: int
    level: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a5b1d6d'}, '__str__')
    def __str__(meadow_self_a5b1d6d):
        meadow_rep_19879ea = f'pid_shutdown_sockets({meadow_self_a5b1d6d.pid}, {meadow_self_a5b1d6d.level})'
        if meadow_self_a5b1d6d.result:
            meadow_rep_19879ea += f', {meadow_self_a5b1d6d.result}'
        return meadow_rep_19879ea

@_name_boundary.class_contract('BscSharedRegionMapAndSlideNp', {})
@meadow_dataclass
class meadow_BscSharedRegionMapAndSlideNp:
    ktraces: meadow_List
    fd: int
    count: int
    mappings: int
    slide: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e8eaae4'}, '__str__')
    def __str__(meadow_self_e8eaae4):
        meadow_rep_3b1784c = f'shared_region_map_and_slide_np({meadow_self_e8eaae4.fd}, {meadow_self_e8eaae4.count}, {hex(meadow_self_e8eaae4.mappings)}, {meadow_self_e8eaae4.slide})'
        if meadow_self_e8eaae4.result:
            meadow_rep_3b1784c += f', {meadow_self_e8eaae4.result}'
        return meadow_rep_3b1784c

@_name_boundary.class_contract('BscKasInfo', {})
@meadow_dataclass
class meadow_BscKasInfo:
    ktraces: meadow_List
    selector: int
    value: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2f29060'}, '__str__')
    def __str__(meadow_self_2f29060):
        meadow_rep_4e8646d = f'kas_info({meadow_self_2f29060.selector}, {hex(meadow_self_2f29060.value)}, {hex(meadow_self_2f29060.size)})'
        if meadow_self_2f29060.result:
            meadow_rep_4e8646d += f', {meadow_self_2f29060.result}'
        return meadow_rep_4e8646d

@_name_boundary.class_contract('BscMemorystatusControl', {})
@meadow_dataclass
class meadow_BscMemorystatusControl:
    ktraces: meadow_List
    command: int
    pid: int
    flags: int
    buffer: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6e8b107'}, '__str__')
    def __str__(meadow_self_6e8b107):
        meadow_rep_1c91ea8 = f'memorystatus_control({meadow_self_6e8b107.command}, {meadow_self_6e8b107.pid}, {meadow_self_6e8b107.flags}, {hex(meadow_self_6e8b107.buffer)})'
        if meadow_self_6e8b107.result:
            meadow_rep_1c91ea8 += f', {meadow_self_6e8b107.result}'
        return meadow_rep_1c91ea8

@_name_boundary.class_contract('BscGuardedOpenNp', {})
@meadow_dataclass
class meadow_BscGuardedOpenNp:
    ktraces: meadow_List
    path: str
    guard: int
    guardflags: int
    flags: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ee2c826'}, '__str__')
    def __str__(meadow_self_ee2c826):
        meadow_flags_d46b64a = ' | '.join(map(lambda meadow_f_7fc895e: _name_boundary.attributes(meadow_f_7fc895e)['name'], meadow_self_ee2c826.flags))
        return f'guarded_open_np("{meadow_self_ee2c826.path}", {hex(meadow_self_ee2c826.guard)}, {meadow_self_ee2c826.guardflags}, {meadow_flags_d46b64a}), {meadow_self_ee2c826.result}'

@_name_boundary.class_contract('BscGuardedCloseNp', {})
@meadow_dataclass
class meadow_BscGuardedCloseNp:
    ktraces: meadow_List
    fd: int
    guard: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_96c2851'}, '__str__')
    def __str__(meadow_self_96c2851):
        meadow_rep_e2fe71b = f'guarded_close_np({meadow_self_96c2851.fd}, {hex(meadow_self_96c2851.guard)})'
        if meadow_self_96c2851.result:
            meadow_rep_e2fe71b += f', {meadow_self_96c2851.result}'
        return meadow_rep_e2fe71b

@_name_boundary.class_contract('BscGuardedKqueueNp', {})
@meadow_dataclass
class meadow_BscGuardedKqueueNp:
    ktraces: meadow_List
    guard: int
    guardflags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_def75dd'}, '__str__')
    def __str__(meadow_self_def75dd):
        meadow_rep_4a98243 = f'guarded_kqueue_np({hex(meadow_self_def75dd.guard)}, {meadow_self_def75dd.guardflags})'
        if meadow_self_def75dd.result:
            meadow_rep_4a98243 += f', {meadow_self_def75dd.result}'
        return meadow_rep_4a98243

@_name_boundary.class_contract('BscChangeFdguardNp', {})
@meadow_dataclass
class meadow_BscChangeFdguardNp:
    ktraces: meadow_List
    fd: int
    guard: int
    guardflags: int
    nguard: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_315fef2'}, '__str__')
    def __str__(meadow_self_315fef2):
        meadow_rep_c43a08b = f'change_fdguard_np({meadow_self_315fef2.fd}, {hex(meadow_self_315fef2.guard)}, {meadow_self_315fef2.guardflags}, {hex(meadow_self_315fef2.nguard)})'
        if meadow_self_315fef2.result:
            meadow_rep_c43a08b += f', {meadow_self_315fef2.result}'
        return meadow_rep_c43a08b

@_name_boundary.class_contract('BscUsrctl', {})
@meadow_dataclass
class meadow_BscUsrctl:
    ktraces: meadow_List
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e73ed69'}, '__str__')
    def __str__(meadow_self_e73ed69):
        meadow_rep_5ff3f2f = f'usrctl({meadow_self_e73ed69.flags})'
        if meadow_self_e73ed69.result:
            meadow_rep_5ff3f2f += f', {meadow_self_e73ed69.result}'
        return meadow_rep_5ff3f2f

@_name_boundary.class_contract('BscProcRlimitControl', {})
@meadow_dataclass
class meadow_BscProcRlimitControl:
    ktraces: meadow_List
    pid: int
    flavor: int
    arg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4ed72a3'}, '__str__')
    def __str__(meadow_self_4ed72a3):
        meadow_rep_3300bf4 = f'proc_rlimit_control({meadow_self_4ed72a3.pid}, {meadow_self_4ed72a3.flavor}, {hex(meadow_self_4ed72a3.arg)})'
        if meadow_self_4ed72a3.result:
            meadow_rep_3300bf4 += f', {meadow_self_4ed72a3.result}'
        return meadow_rep_3300bf4

@_name_boundary.class_contract('BscConnectx', {})
@meadow_dataclass
class meadow_BscConnectx:
    ktraces: meadow_List
    socket: int
    endpoints: int
    associd: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0822218'}, '__str__')
    def __str__(meadow_self_0822218):
        meadow_rep_e336691 = f'connectx({meadow_self_0822218.socket}, {hex(meadow_self_0822218.endpoints)}, {meadow_self_0822218.associd}, {meadow_self_0822218.flags})'
        if meadow_self_0822218.result:
            meadow_rep_e336691 += f', {meadow_self_0822218.result}'
        return meadow_rep_e336691

@_name_boundary.class_contract('BscDisconnectx', {})
@meadow_dataclass
class meadow_BscDisconnectx:
    ktraces: meadow_List
    s: int
    aid: int
    cid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e5b8c09'}, '__str__')
    def __str__(meadow_self_e5b8c09):
        meadow_rep_7b2ca6c = f'disconnectx({meadow_self_e5b8c09.s}, {meadow_self_e5b8c09.aid}, {meadow_self_e5b8c09.cid})'
        if meadow_self_e5b8c09.result:
            meadow_rep_7b2ca6c += f', {meadow_self_e5b8c09.result}'
        return meadow_rep_7b2ca6c

@_name_boundary.class_contract('BscPeeloff', {})
@meadow_dataclass
class meadow_BscPeeloff:
    ktraces: meadow_List
    s: int
    aid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9039e08'}, '__str__')
    def __str__(meadow_self_9039e08):
        meadow_rep_1b185a5 = f'peeloff({meadow_self_9039e08.s}, {meadow_self_9039e08.aid})'
        if meadow_self_9039e08.result:
            meadow_rep_1b185a5 += f', {meadow_self_9039e08.result}'
        return meadow_rep_1b185a5

@_name_boundary.class_contract('BscSocketDelegate', {})
@meadow_dataclass
class meadow_BscSocketDelegate:
    ktraces: meadow_List
    domain: meadow_socket.AddressFamily
    type: meadow_socket.SocketKind
    protocol: int
    epid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6ccd30b'}, '__str__')
    def __str__(meadow_self_6ccd30b):
        return f"socket_delegate({_name_boundary.attributes(meadow_self_6ccd30b.domain)['name']}, {_name_boundary.attributes(meadow_self_6ccd30b.type)['name']}, {meadow_self_6ccd30b.protocol}, {meadow_self_6ccd30b.epid}), {meadow_self_6ccd30b.result}"

@_name_boundary.class_contract('BscTelemetry', {})
@meadow_dataclass
class meadow_BscTelemetry:
    ktraces: meadow_List
    cmd: int
    deadline: int
    interval: int
    leeway: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_81ae427'}, '__str__')
    def __str__(meadow_self_81ae427):
        meadow_rep_eca7802 = f'telemetry({meadow_self_81ae427.cmd}, {meadow_self_81ae427.deadline}, {meadow_self_81ae427.interval}, {meadow_self_81ae427.leeway})'
        if meadow_self_81ae427.result:
            meadow_rep_eca7802 += f', {meadow_self_81ae427.result}'
        return meadow_rep_eca7802

@_name_boundary.class_contract('BscProcUuidPolicy', {})
@meadow_dataclass
class meadow_BscProcUuidPolicy:
    ktraces: meadow_List
    operation: int
    uuid: int
    uuidlen: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8a4cd96'}, '__str__')
    def __str__(meadow_self_8a4cd96):
        meadow_rep_9f349fd = f'proc_uuid_policy({meadow_self_8a4cd96.operation}, {meadow_self_8a4cd96.uuid}, {meadow_self_8a4cd96.uuidlen}, {meadow_self_8a4cd96.flags})'
        if meadow_self_8a4cd96.result:
            meadow_rep_9f349fd += f', {meadow_self_8a4cd96.result}'
        return meadow_rep_9f349fd

@_name_boundary.class_contract('BscMemorystatusGetLevel', {})
@meadow_dataclass
class meadow_BscMemorystatusGetLevel:
    ktraces: meadow_List
    level: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_534619c'}, '__str__')
    def __str__(meadow_self_534619c):
        meadow_rep_2fc5bb2 = f'memorystatus_get_level({hex(meadow_self_534619c.level)})'
        if meadow_self_534619c.result:
            meadow_rep_2fc5bb2 += f', {meadow_self_534619c.result}'
        return meadow_rep_2fc5bb2

@_name_boundary.class_contract('BscSystemOverride', {})
@meadow_dataclass
class meadow_BscSystemOverride:
    ktraces: meadow_List
    timeout: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_65d846a'}, '__str__')
    def __str__(meadow_self_65d846a):
        meadow_rep_0a04794 = f'system_override({meadow_self_65d846a.timeout}, {meadow_self_65d846a.flags})'
        if meadow_self_65d846a.result:
            meadow_rep_0a04794 += f', {meadow_self_65d846a.result}'
        return meadow_rep_0a04794

@_name_boundary.class_contract('BscVfsPurge', {})
@meadow_dataclass
class meadow_BscVfsPurge:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cfcb127'}, '__str__')
    def __str__(meadow_self_cfcb127):
        meadow_rep_095814e = 'vfs_purge()'
        if meadow_self_cfcb127.result:
            meadow_rep_095814e += f', {meadow_self_cfcb127.result}'
        return meadow_rep_095814e

@_name_boundary.class_contract('BscSfiCtl', {})
@meadow_dataclass
class meadow_BscSfiCtl:
    ktraces: meadow_List
    operation: int
    sfi_class: int
    time: int
    out_time: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4142ed7'}, '__str__')
    def __str__(meadow_self_4142ed7):
        meadow_rep_d27da23 = f'sfi_ctl({meadow_self_4142ed7.operation}, {meadow_self_4142ed7.sfi_class}, {meadow_self_4142ed7.time}, {hex(meadow_self_4142ed7.out_time)})'
        if meadow_self_4142ed7.result:
            meadow_rep_d27da23 += f', {meadow_self_4142ed7.result}'
        return meadow_rep_d27da23

@_name_boundary.class_contract('BscSfiPidctl', {})
@meadow_dataclass
class meadow_BscSfiPidctl:
    ktraces: meadow_List
    operation: int
    pid: int
    sfi_flags: int
    out_sfi_flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c56a916'}, '__str__')
    def __str__(meadow_self_c56a916):
        meadow_rep_d5c8273 = f'sfi_pidctl({meadow_self_c56a916.operation}, {meadow_self_c56a916.pid}, {meadow_self_c56a916.sfi_flags}, {hex(meadow_self_c56a916.out_sfi_flags)})'
        if meadow_self_c56a916.result:
            meadow_rep_d5c8273 += f', {meadow_self_c56a916.result}'
        return meadow_rep_d5c8273

@_name_boundary.class_contract('BscCoalition', {})
@meadow_dataclass
class meadow_BscCoalition:
    ktraces: meadow_List
    operation: int
    cid: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_5a3c1cd'}, '__str__')
    def __str__(meadow_self_5a3c1cd):
        meadow_rep_fd838ff = f'coalition({meadow_self_5a3c1cd.operation}, {hex(meadow_self_5a3c1cd.cid)}, {meadow_self_5a3c1cd.flags})'
        if meadow_self_5a3c1cd.result:
            meadow_rep_fd838ff += f', {meadow_self_5a3c1cd.result}'
        return meadow_rep_fd838ff

@_name_boundary.class_contract('BscCoalitionInfo', {})
@meadow_dataclass
class meadow_BscCoalitionInfo:
    ktraces: meadow_List
    flavor: int
    cid: int
    buffer: int
    bufsize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8e2ca39'}, '__str__')
    def __str__(meadow_self_8e2ca39):
        meadow_rep_8e2b33e = f'coalition_info({meadow_self_8e2ca39.flavor}, {hex(meadow_self_8e2ca39.cid)}, {hex(meadow_self_8e2ca39.buffer)}, {hex(meadow_self_8e2ca39.bufsize)})'
        if meadow_self_8e2ca39.result:
            meadow_rep_8e2b33e += f', {meadow_self_8e2ca39.result}'
        return meadow_rep_8e2b33e

@_name_boundary.class_contract('BscNecpMatchPolicy', {})
@meadow_dataclass
class meadow_BscNecpMatchPolicy:
    ktraces: meadow_List
    parameters: int
    parameters_size: int
    returned_result: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fa53069'}, '__str__')
    def __str__(meadow_self_fa53069):
        meadow_rep_8badf70 = f'necp_match_policy({hex(meadow_self_fa53069.parameters)}, {meadow_self_fa53069.parameters_size}, {hex(meadow_self_fa53069.returned_result)})'
        if meadow_self_fa53069.result:
            meadow_rep_8badf70 += f', {meadow_self_fa53069.result}'
        return meadow_rep_8badf70

@_name_boundary.class_contract('BscGetattrlistbulk', {})
@meadow_dataclass
class meadow_BscGetattrlistbulk:
    ktraces: meadow_List
    dirfd: int
    alist: int
    attributeBuffer: int
    bufferSize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_61afd77'}, '__str__')
    def __str__(meadow_self_61afd77):
        return f'getattrlistbulk({meadow_self_61afd77.dirfd}, {hex(meadow_self_61afd77.alist)}, {hex(meadow_self_61afd77.attributeBuffer)}, {meadow_self_61afd77.bufferSize}), {meadow_self_61afd77.result}'

@_name_boundary.class_contract('BscClonefileat', {})
@meadow_dataclass
class meadow_BscClonefileat:
    ktraces: meadow_List
    src_dirfd: int
    src: str
    dst_dirfd: int
    dst: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7741f7c'}, '__str__')
    def __str__(meadow_self_7741f7c):
        meadow_rep_679357b = f'clonefileat({meadow_self_7741f7c.src_dirfd}, "{meadow_self_7741f7c.src}", {meadow_self_7741f7c.dst_dirfd}, "{meadow_self_7741f7c.dst}")'
        if meadow_self_7741f7c.result:
            meadow_rep_679357b += f', {meadow_self_7741f7c.result}'
        return meadow_rep_679357b

@_name_boundary.class_contract('BscRenameat', {})
@meadow_dataclass
class meadow_BscRenameat:
    ktraces: meadow_List
    fromfd: int
    from_: str
    tofd: int
    to: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_49026f1'}, '__str__')
    def __str__(meadow_self_49026f1):
        meadow_rep_67a178b = f'renameat({meadow_self_49026f1.fromfd}, "{meadow_self_49026f1.from_}", {meadow_self_49026f1.tofd}, "{meadow_self_49026f1.to}")'
        if meadow_self_49026f1.result:
            meadow_rep_67a178b += f', {meadow_self_49026f1.result}'
        return meadow_rep_67a178b

@_name_boundary.class_contract('BscFaccessat', {})
@meadow_dataclass
class meadow_BscFaccessat:
    ktraces: meadow_List
    fd: int
    path: str
    amode: meadow_List
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6e97a9d'}, '__str__')
    def __str__(meadow_self_6e97a9d):
        meadow_amode_8372473 = ' | '.join(map(lambda meadow_f_e250f9f: _name_boundary.attributes(meadow_f_e250f9f)['name'], meadow_self_6e97a9d.amode))
        meadow_rep_620f649 = f'faccessat({meadow_self_6e97a9d.fd}, "{meadow_self_6e97a9d.path}", {meadow_amode_8372473}, {meadow_self_6e97a9d.flag})'
        if meadow_self_6e97a9d.result:
            meadow_rep_620f649 += f', {meadow_self_6e97a9d.result}'
        return meadow_rep_620f649

@_name_boundary.class_contract('BscFchmodat', {})
@meadow_dataclass
class meadow_BscFchmodat:
    ktraces: meadow_List
    fd: int
    path: str
    mode: meadow_List
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6c9470e'}, '__str__')
    def __str__(meadow_self_6c9470e):
        meadow_mode_95ce87c = ' | '.join(map(lambda meadow_f_42aac9e: _name_boundary.attributes(meadow_f_42aac9e)['name'], meadow_self_6c9470e.mode))
        meadow_rep_8401056 = f'fchmodat({meadow_self_6c9470e.fd}, "{meadow_self_6c9470e.path}", {meadow_mode_95ce87c}, {meadow_self_6c9470e.flag})'
        if meadow_self_6c9470e.result:
            meadow_rep_8401056 += f', {meadow_self_6c9470e.result}'
        return meadow_rep_8401056

@_name_boundary.class_contract('BscFchownat', {})
@meadow_dataclass
class meadow_BscFchownat:
    ktraces: meadow_List
    fd: int
    path: str
    uid: int
    gid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c32fbf7'}, '__str__')
    def __str__(meadow_self_c32fbf7):
        meadow_rep_bfb57df = f'fchownat({meadow_self_c32fbf7.fd}, "{meadow_self_c32fbf7.path}", {meadow_self_c32fbf7.uid}, {meadow_self_c32fbf7.gid})'
        if meadow_self_c32fbf7.result:
            meadow_rep_bfb57df += f', {meadow_self_c32fbf7.result}'
        return meadow_rep_bfb57df

@_name_boundary.class_contract('BscFstatat', {})
@meadow_dataclass
class meadow_BscFstatat:
    ktraces: meadow_List
    fd: int
    path: str
    ub: int
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_56bc970'}, '__str__')
    def __str__(meadow_self_56bc970):
        meadow_rep_453dffb = f'fstatat({meadow_self_56bc970.fd}, "{meadow_self_56bc970.path}", {hex(meadow_self_56bc970.ub)}, {meadow_self_56bc970.flag})'
        if meadow_self_56bc970.result:
            meadow_rep_453dffb += f', {meadow_self_56bc970.result}'
        return meadow_rep_453dffb

@_name_boundary.class_contract('BscFstatat64', {})
@meadow_dataclass
class meadow_BscFstatat64:
    ktraces: meadow_List
    fd: int
    path: str
    ub: int
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6b957c9'}, '__str__')
    def __str__(meadow_self_6b957c9):
        meadow_rep_8616cc5 = f'fstatat64({meadow_self_6b957c9.fd}, "{meadow_self_6b957c9.path}", {hex(meadow_self_6b957c9.ub)}, {meadow_self_6b957c9.flag})'
        if meadow_self_6b957c9.result:
            meadow_rep_8616cc5 += f', {meadow_self_6b957c9.result}'
        return meadow_rep_8616cc5

@_name_boundary.class_contract('BscLinkat', {})
@meadow_dataclass
class meadow_BscLinkat:
    ktraces: meadow_List
    fd1: int
    path: str
    fd2: int
    link: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_611f7e1'}, '__str__')
    def __str__(meadow_self_611f7e1):
        meadow_rep_95deab8 = f'linkat({meadow_self_611f7e1.fd1}, "{meadow_self_611f7e1.path}", {meadow_self_611f7e1.fd2}, "{meadow_self_611f7e1.link}")'
        if meadow_self_611f7e1.result:
            meadow_rep_95deab8 += f', {meadow_self_611f7e1.result}'
        return meadow_rep_95deab8

@_name_boundary.class_contract('BscUnlinkat', {})
@meadow_dataclass
class meadow_BscUnlinkat:
    ktraces: meadow_List
    fd: int
    path: str
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9d2be2c'}, '__str__')
    def __str__(meadow_self_9d2be2c):
        meadow_rep_3b37798 = f'unlinkat({meadow_self_9d2be2c.fd}, "{meadow_self_9d2be2c.path}", {meadow_self_9d2be2c.flag})'
        if meadow_self_9d2be2c.result:
            meadow_rep_3b37798 += f', {meadow_self_9d2be2c.result}'
        return meadow_rep_3b37798

@_name_boundary.class_contract('BscReadlinkat', {})
@meadow_dataclass
class meadow_BscReadlinkat:
    ktraces: meadow_List
    fd: int
    path: str
    buf: int
    bufsize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a6922c9'}, '__str__')
    def __str__(meadow_self_a6922c9):
        return f'readlinkat({meadow_self_a6922c9.fd}, "{meadow_self_a6922c9.path}", {hex(meadow_self_a6922c9.buf)}, {meadow_self_a6922c9.bufsize}), {meadow_self_a6922c9.result}'

@_name_boundary.class_contract('BscSymlinkat', {})
@meadow_dataclass
class meadow_BscSymlinkat:
    ktraces: meadow_List
    path1: str
    fd: int
    path2: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_eeab1e4'}, '__str__')
    def __str__(meadow_self_eeab1e4):
        meadow_rep_2f9191c = f'symlinkat("{meadow_self_eeab1e4.path1}", {meadow_self_eeab1e4.fd}, "{meadow_self_eeab1e4.path2}")'
        if meadow_self_eeab1e4.result:
            meadow_rep_2f9191c += f', {meadow_self_eeab1e4.result}'
        return meadow_rep_2f9191c

@_name_boundary.class_contract('BscMkdirat', {})
@meadow_dataclass
class meadow_BscMkdirat:
    ktraces: meadow_List
    fd: int
    path: str
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d90f6cd'}, '__str__')
    def __str__(meadow_self_d90f6cd):
        meadow_mode_5fd6690 = ' | '.join(map(lambda meadow_f_66ba862: _name_boundary.attributes(meadow_f_66ba862)['name'], meadow_self_d90f6cd.mode))
        meadow_rep_25651bc = f'mkdirat({meadow_self_d90f6cd.fd}, "{meadow_self_d90f6cd.path}", {meadow_mode_5fd6690})'
        if meadow_self_d90f6cd.result:
            meadow_rep_25651bc += f', {meadow_self_d90f6cd.result}'
        return meadow_rep_25651bc

@_name_boundary.class_contract('BscGetattrlistat', {})
@meadow_dataclass
class meadow_BscGetattrlistat:
    ktraces: meadow_List
    fd: int
    path: str
    alist: int
    attributeBuffer: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c920651'}, '__str__')
    def __str__(meadow_self_c920651):
        meadow_rep_0aa87f4 = f'getattrlistat({meadow_self_c920651.fd}, "{meadow_self_c920651.path}", {hex(meadow_self_c920651.alist)}, {hex(meadow_self_c920651.attributeBuffer)})'
        if meadow_self_c920651.result:
            meadow_rep_0aa87f4 += f', {meadow_self_c920651.result}'
        return meadow_rep_0aa87f4

@_name_boundary.class_contract('BscProcTraceLog', {})
@meadow_dataclass
class meadow_BscProcTraceLog:
    ktraces: meadow_List
    pid: int
    uniqueid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1eac958'}, '__str__')
    def __str__(meadow_self_1eac958):
        meadow_rep_2517878 = f'proc_trace_log({meadow_self_1eac958.pid}, {meadow_self_1eac958.uniqueid})'
        if meadow_self_1eac958.result:
            meadow_rep_2517878 += f', {meadow_self_1eac958.result}'
        return meadow_rep_2517878

@_name_boundary.class_contract('BscBsdthreadCtl', {})
@meadow_dataclass
class meadow_BscBsdthreadCtl:
    ktraces: meadow_List
    cmd: int
    arg1: int
    arg2: int
    arg3: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8e79552'}, '__str__')
    def __str__(meadow_self_8e79552):
        meadow_rep_33839af = f'bsdthread_ctl({meadow_self_8e79552.cmd}, {hex(meadow_self_8e79552.arg1)}, {hex(meadow_self_8e79552.arg2)}, {hex(meadow_self_8e79552.arg3)})'
        if meadow_self_8e79552.result:
            meadow_rep_33839af += f', {meadow_self_8e79552.result}'
        return meadow_rep_33839af

@_name_boundary.class_contract('BscOpenbyidNp', {})
@meadow_dataclass
class meadow_BscOpenbyidNp:
    ktraces: meadow_List
    fsid: int
    objid: int
    oflags: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_df700c8'}, '__str__')
    def __str__(meadow_self_df700c8):
        meadow_oflags_9ba013d = ' | '.join(map(lambda meadow_f_79a0659: _name_boundary.attributes(meadow_f_79a0659)['name'], meadow_self_df700c8.oflags))
        return f'openbyid_np({meadow_self_df700c8.fsid}, {meadow_self_df700c8.objid}, {meadow_oflags_9ba013d}), {meadow_self_df700c8.result}'

@_name_boundary.class_contract('BscRecvmsgX', {})
@meadow_dataclass
class meadow_BscRecvmsgX:
    ktraces: meadow_List
    s: int
    msgp: int
    cnt: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_33b5edd'}, '__str__')
    def __str__(meadow_self_33b5edd):
        return f'recvmsg_x({meadow_self_33b5edd.s}, {hex(meadow_self_33b5edd.msgp)}, {meadow_self_33b5edd.cnt}, {meadow_self_33b5edd.flags}), {meadow_self_33b5edd.result}'

@_name_boundary.class_contract('BscSendmsgX', {})
@meadow_dataclass
class meadow_BscSendmsgX:
    ktraces: meadow_List
    s: int
    msgp: int
    cnt: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_af58374'}, '__str__')
    def __str__(meadow_self_af58374):
        return f'sendmsg_x({meadow_self_af58374.s}, {hex(meadow_self_af58374.msgp)}, {meadow_self_af58374.cnt}, {meadow_self_af58374.flags}), {meadow_self_af58374.result}'

@_name_boundary.class_contract('BscThreadSelfusage', {})
@meadow_dataclass
class meadow_BscThreadSelfusage:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e217272'}, '__str__')
    def __str__(meadow_self_e217272):
        return f'thread_selfusage(), {meadow_self_e217272.result}'

@_name_boundary.class_contract('BscCsrctl', {})
@meadow_dataclass
class meadow_BscCsrctl:
    ktraces: meadow_List
    op: int
    useraddr: int
    usersize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9cc8e92'}, '__str__')
    def __str__(meadow_self_9cc8e92):
        meadow_rep_b07a3a8 = f'csrctl({meadow_self_9cc8e92.op}, {hex(meadow_self_9cc8e92.useraddr)}, {meadow_self_9cc8e92.usersize})'
        if meadow_self_9cc8e92.result:
            meadow_rep_b07a3a8 += f', {meadow_self_9cc8e92.result}'
        return meadow_rep_b07a3a8

@_name_boundary.class_contract('BscGuardedOpenDprotectedNp', {})
@meadow_dataclass
class meadow_BscGuardedOpenDprotectedNp:
    ktraces: meadow_List
    path: str
    guard: int
    guardflags: int
    flags: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3e1a341'}, '__str__')
    def __str__(meadow_self_3e1a341):
        meadow_oflags_21c5620 = ' | '.join(map(lambda meadow_f_e0683fc: _name_boundary.attributes(meadow_f_e0683fc)['name'], meadow_self_3e1a341.flags))
        return f'guarded_open_dprotected_np("{meadow_self_3e1a341.path}", {hex(meadow_self_3e1a341.guard)}, {meadow_self_3e1a341.guardflags}, {meadow_oflags_21c5620}), {meadow_self_3e1a341.result}'

@_name_boundary.class_contract('BscGuardedWriteNp', {})
@meadow_dataclass
class meadow_BscGuardedWriteNp:
    ktraces: meadow_List
    fd: int
    guard: int
    cbuf: int
    nbyte: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_dbe5a9a'}, '__str__')
    def __str__(meadow_self_dbe5a9a):
        return f'guarded_write_np({meadow_self_dbe5a9a.fd}, {hex(meadow_self_dbe5a9a.guard)}, {hex(meadow_self_dbe5a9a.cbuf)}, {meadow_self_dbe5a9a.nbyte}), {meadow_self_dbe5a9a.result}'

@_name_boundary.class_contract('BscGuardedPwriteNp', {})
@meadow_dataclass
class meadow_BscGuardedPwriteNp:
    ktraces: meadow_List
    fd: int
    guard: int
    buf: int
    nbyte: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f798d54'}, '__str__')
    def __str__(meadow_self_f798d54):
        return f'guarded_pwrite_np({meadow_self_f798d54.fd}, {hex(meadow_self_f798d54.guard)}, {hex(meadow_self_f798d54.buf)}, {meadow_self_f798d54.nbyte}), {meadow_self_f798d54.result}'

@_name_boundary.class_contract('BscGuardedWritevNp', {})
@meadow_dataclass
class meadow_BscGuardedWritevNp:
    ktraces: meadow_List
    fd: int
    guard: int
    iovp: int
    iovcnt: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_33b28a1'}, '__str__')
    def __str__(meadow_self_33b28a1):
        return f'guarded_writev_np({meadow_self_33b28a1.fd}, {hex(meadow_self_33b28a1.guard)}, {hex(meadow_self_33b28a1.iovp)}, {meadow_self_33b28a1.iovcnt}), {meadow_self_33b28a1.result}'

@_name_boundary.class_contract('BscRenameatxNp', {})
@meadow_dataclass
class meadow_BscRenameatxNp:
    ktraces: meadow_List
    fromfd: int
    from_: str
    tofd: int
    to: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_50cd99f'}, '__str__')
    def __str__(meadow_self_50cd99f):
        meadow_rep_768a5e2 = f'renameatx_np({meadow_self_50cd99f.fromfd}, "{meadow_self_50cd99f.from_}", {meadow_self_50cd99f.tofd}, "{meadow_self_50cd99f.to}")'
        if meadow_self_50cd99f.result:
            meadow_rep_768a5e2 += f', {meadow_self_50cd99f.result}'
        return meadow_rep_768a5e2

@_name_boundary.class_contract('BscMremapEncrypted', {})
@meadow_dataclass
class meadow_BscMremapEncrypted:
    ktraces: meadow_List
    addr: int
    len: int
    cryptid: int
    cputype: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_25e7d71'}, '__str__')
    def __str__(meadow_self_25e7d71):
        meadow_rep_aa51a30 = f'mremap_encrypted({hex(meadow_self_25e7d71.addr)}, {meadow_self_25e7d71.len}, {meadow_self_25e7d71.cryptid}, {meadow_self_25e7d71.cputype})'
        if meadow_self_25e7d71.result:
            meadow_rep_aa51a30 += f', {meadow_self_25e7d71.result}'
        return meadow_rep_aa51a30

@_name_boundary.class_contract('BscNetagentTrigger', {})
@meadow_dataclass
class meadow_BscNetagentTrigger:
    ktraces: meadow_List
    agent_uuid: int
    agent_uuidlen: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fec6054'}, '__str__')
    def __str__(meadow_self_fec6054):
        meadow_rep_0897c8b = f'netagent_trigger({meadow_self_fec6054.agent_uuid}, {meadow_self_fec6054.agent_uuidlen})'
        if meadow_self_fec6054.result:
            meadow_rep_0897c8b += f', {meadow_self_fec6054.result}'
        return meadow_rep_0897c8b

@_name_boundary.class_contract('BscStackSnapshotWithConfig', {})
@meadow_dataclass
class meadow_BscStackSnapshotWithConfig:
    ktraces: meadow_List
    stackshot_config_version: int
    stackshot_config: int
    stackshot_config_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d1d946f'}, '__str__')
    def __str__(meadow_self_d1d946f):
        meadow_rep_d6bddef = f'stack_snapshot_with_config({meadow_self_d1d946f.stackshot_config_version}, {hex(meadow_self_d1d946f.stackshot_config)}, {meadow_self_d1d946f.stackshot_config_size})'
        if meadow_self_d1d946f.result:
            meadow_rep_d6bddef += f', {meadow_self_d1d946f.result}'
        return meadow_rep_d6bddef

@_name_boundary.class_contract('BscMicrostackshot', {})
@meadow_dataclass
class meadow_BscMicrostackshot:
    ktraces: meadow_List
    tracebuf: int
    tracebuf_size: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b03d038'}, '__str__')
    def __str__(meadow_self_b03d038):
        return f'microstackshot({hex(meadow_self_b03d038.tracebuf)}, {meadow_self_b03d038.tracebuf_size}, {meadow_self_b03d038.flags}), {meadow_self_b03d038.result}'

@_name_boundary.class_contract('BscGrabPgoData', {})
@meadow_dataclass
class meadow_BscGrabPgoData:
    ktraces: meadow_List
    uuid: int
    flags: int
    buffer: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c4a0772'}, '__str__')
    def __str__(meadow_self_c4a0772):
        return f'grab_pgo_data({hex(meadow_self_c4a0772.uuid)}, {meadow_self_c4a0772.flags}, {hex(meadow_self_c4a0772.buffer)}, {meadow_self_c4a0772.size}), {meadow_self_c4a0772.result}'

@_name_boundary.class_contract('BscPersona', {})
@meadow_dataclass
class meadow_BscPersona:
    ktraces: meadow_List
    operation: int
    flags: int
    buffer: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_34aa497'}, '__str__')
    def __str__(meadow_self_34aa497):
        meadow_rep_66c190c = f'persona({meadow_self_34aa497.operation}, {meadow_self_34aa497.flags}, {hex(meadow_self_34aa497.buffer)}, {hex(meadow_self_34aa497.size)})'
        if meadow_self_34aa497.result:
            meadow_rep_66c190c += f', {meadow_self_34aa497.result}'
        return meadow_rep_66c190c

@_name_boundary.class_contract('BscMachEventlinkSignal', {})
@meadow_dataclass
class meadow_BscMachEventlinkSignal:
    ktraces: meadow_List
    eventlink_port: int
    signal_count: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7bf29e8'}, '__str__')
    def __str__(meadow_self_7bf29e8):
        meadow_rep_5dcfa9a = f'mach_eventlink_signal({meadow_self_7bf29e8.eventlink_port}, {meadow_self_7bf29e8.signal_count})'
        if meadow_self_7bf29e8.result:
            meadow_rep_5dcfa9a += f', {meadow_self_7bf29e8.result}'
        return meadow_rep_5dcfa9a

@_name_boundary.class_contract('BscMachEventlinkWaitUntil', {})
@meadow_dataclass
class meadow_BscMachEventlinkWaitUntil:
    ktraces: meadow_List
    eventlink_port: int
    wait_count: int
    deadline: int
    clock_id: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1dfdafd'}, '__str__')
    def __str__(meadow_self_1dfdafd):
        meadow_rep_66a9e0a = f'mach_eventlink_wait_until({meadow_self_1dfdafd.eventlink_port}, {hex(meadow_self_1dfdafd.wait_count)}, {meadow_self_1dfdafd.deadline}, {meadow_self_1dfdafd.clock_id})'
        if meadow_self_1dfdafd.result:
            meadow_rep_66a9e0a += f', {meadow_self_1dfdafd.result}'
        return meadow_rep_66a9e0a

@_name_boundary.class_contract('BscMachEventlinkSignalWaitUntil', {})
@meadow_dataclass
class meadow_BscMachEventlinkSignalWaitUntil:
    ktraces: meadow_List
    eventlink_port: int
    wait_count: int
    signal_count: int
    deadline: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9e854ef'}, '__str__')
    def __str__(meadow_self_9e854ef):
        meadow_rep_a22b736 = f'mach_eventlink_signal_wait_until({meadow_self_9e854ef.eventlink_port}, {hex(meadow_self_9e854ef.wait_count)}, {meadow_self_9e854ef.signal_count}, {meadow_self_9e854ef.deadline})'
        if meadow_self_9e854ef.result:
            meadow_rep_a22b736 += f', {meadow_self_9e854ef.result}'
        return meadow_rep_a22b736

@_name_boundary.class_contract('BscWorkIntervalCtl', {})
@meadow_dataclass
class meadow_BscWorkIntervalCtl:
    ktraces: meadow_List
    operation: int
    work_interval_id: int
    arg: int
    len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_800eeba'}, '__str__')
    def __str__(meadow_self_800eeba):
        meadow_rep_5726e65 = f'work_interval_ctl({meadow_self_800eeba.operation}, {meadow_self_800eeba.work_interval_id}, {hex(meadow_self_800eeba.arg)}, {meadow_self_800eeba.len})'
        if meadow_self_800eeba.result:
            meadow_rep_5726e65 += f', {meadow_self_800eeba.result}'
        return meadow_rep_5726e65

@_name_boundary.class_contract('BscGetentropy', {})
@meadow_dataclass
class meadow_BscGetentropy:
    ktraces: meadow_List
    buffer: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_97f57af'}, '__str__')
    def __str__(meadow_self_97f57af):
        meadow_rep_4b61ff4 = f'getentropy({hex(meadow_self_97f57af.buffer)}, {meadow_self_97f57af.size})'
        if meadow_self_97f57af.result:
            meadow_rep_4b61ff4 += f', {meadow_self_97f57af.result}'
        return meadow_rep_4b61ff4

@_name_boundary.class_contract('BscNecpOpen', {})
@meadow_dataclass
class meadow_BscNecpOpen:
    ktraces: meadow_List
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a3306f9'}, '__str__')
    def __str__(meadow_self_a3306f9):
        return f'necp_open({meadow_self_a3306f9.flags}), {meadow_self_a3306f9.result}'

@_name_boundary.class_contract('BscNecpClientAction', {})
@meadow_dataclass
class meadow_BscNecpClientAction:
    ktraces: meadow_List
    necp_fd: int
    action: int
    client_id: int
    client_id_len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_24ac853'}, '__str__')
    def __str__(meadow_self_24ac853):
        return f'necp_client_action({meadow_self_24ac853.necp_fd}, {meadow_self_24ac853.action}, {hex(meadow_self_24ac853.client_id)}, {meadow_self_24ac853.client_id_len}), {meadow_self_24ac853.result}'

@_name_boundary.class_contract('BscNexusOpen', {})
@meadow_dataclass
class meadow_BscNexusOpen:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_dc52f6e'}, '__str__')
    def __str__(meadow_self_dc52f6e):
        return f'nexus_open(), {meadow_self_dc52f6e.result}'

@_name_boundary.class_contract('BscNexusRegister', {})
@meadow_dataclass
class meadow_BscNexusRegister:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_852417c'}, '__str__')
    def __str__(meadow_self_852417c):
        meadow_rep_2e8a1a0 = 'nexus_register()'
        if meadow_self_852417c.result:
            meadow_rep_2e8a1a0 += f', {meadow_self_852417c.result}'
        return meadow_rep_2e8a1a0

@_name_boundary.class_contract('BscNexusDeregister', {})
@meadow_dataclass
class meadow_BscNexusDeregister:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c75a965'}, '__str__')
    def __str__(meadow_self_c75a965):
        meadow_rep_f110a8d = 'nexus_deregister()'
        if meadow_self_c75a965.result:
            meadow_rep_f110a8d += f', {meadow_self_c75a965.result}'
        return meadow_rep_f110a8d

@_name_boundary.class_contract('BscNexusCreate', {})
@meadow_dataclass
class meadow_BscNexusCreate:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_66badc8'}, '__str__')
    def __str__(meadow_self_66badc8):
        meadow_rep_6fb0755 = 'nexus_create()'
        if meadow_self_66badc8.result:
            meadow_rep_6fb0755 += f', {meadow_self_66badc8.result}'
        return meadow_rep_6fb0755

@_name_boundary.class_contract('BscNexusDestroy', {})
@meadow_dataclass
class meadow_BscNexusDestroy:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_69e87f1'}, '__str__')
    def __str__(meadow_self_69e87f1):
        meadow_rep_9e1aeac = 'nexus_destroy()'
        if meadow_self_69e87f1.result:
            meadow_rep_9e1aeac += f', {meadow_self_69e87f1.result}'
        return meadow_rep_9e1aeac

@_name_boundary.class_contract('BscNexusGetOpt', {})
@meadow_dataclass
class meadow_BscNexusGetOpt:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1d3356f'}, '__str__')
    def __str__(meadow_self_1d3356f):
        meadow_rep_612d769 = 'nexus_get_opt()'
        if meadow_self_1d3356f.result:
            meadow_rep_612d769 += f', {meadow_self_1d3356f.result}'
        return meadow_rep_612d769

@_name_boundary.class_contract('BscNexusSetOpt', {})
@meadow_dataclass
class meadow_BscNexusSetOpt:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_af2daf1'}, '__str__')
    def __str__(meadow_self_af2daf1):
        meadow_rep_f18d90c = 'nexus_set_opt()'
        if meadow_self_af2daf1.result:
            meadow_rep_f18d90c += f', {meadow_self_af2daf1.result}'
        return meadow_rep_f18d90c

@_name_boundary.class_contract('BscChannelOpen', {})
@meadow_dataclass
class meadow_BscChannelOpen:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8c5e5ff'}, '__str__')
    def __str__(meadow_self_8c5e5ff):
        meadow_rep_d734988 = 'channel_open()'
        if meadow_self_8c5e5ff.result:
            meadow_rep_d734988 += f', {meadow_self_8c5e5ff.result}'
        return meadow_rep_d734988

@_name_boundary.class_contract('BscChannelGetInfo', {})
@meadow_dataclass
class meadow_BscChannelGetInfo:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9b10d07'}, '__str__')
    def __str__(meadow_self_9b10d07):
        meadow_rep_ae498ff = 'channel_get_info()'
        if meadow_self_9b10d07.result:
            meadow_rep_ae498ff += f', {meadow_self_9b10d07.result}'
        return meadow_rep_ae498ff

@_name_boundary.class_contract('BscChannelSync', {})
@meadow_dataclass
class meadow_BscChannelSync:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0c6ecca'}, '__str__')
    def __str__(meadow_self_0c6ecca):
        meadow_rep_204b281 = 'channel_sync()'
        if meadow_self_0c6ecca.result:
            meadow_rep_204b281 += f', {meadow_self_0c6ecca.result}'
        return meadow_rep_204b281

@_name_boundary.class_contract('BscChannelGetOpt', {})
@meadow_dataclass
class meadow_BscChannelGetOpt:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_613eafc'}, '__str__')
    def __str__(meadow_self_613eafc):
        meadow_rep_c289c74 = 'channel_get_opt()'
        if meadow_self_613eafc.result:
            meadow_rep_c289c74 += f', {meadow_self_613eafc.result}'
        return meadow_rep_c289c74

@_name_boundary.class_contract('BscChannelSetOpt', {})
@meadow_dataclass
class meadow_BscChannelSetOpt:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_35c5a0a'}, '__str__')
    def __str__(meadow_self_35c5a0a):
        meadow_rep_58b4a5c = 'channel_set_opt()'
        if meadow_self_35c5a0a.result:
            meadow_rep_58b4a5c += f', {meadow_self_35c5a0a.result}'
        return meadow_rep_58b4a5c

@_name_boundary.class_contract('BscUlockWait', {})
@meadow_dataclass
class meadow_BscUlockWait:
    ktraces: meadow_List
    operation: int
    addr: int
    value: int
    timeout: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_bf12fa8'}, '__str__')
    def __str__(meadow_self_bf12fa8):
        return f'ulock_wait({meadow_self_bf12fa8.operation}, {hex(meadow_self_bf12fa8.addr)}, {meadow_self_bf12fa8.value}, {meadow_self_bf12fa8.timeout}), {meadow_self_bf12fa8.result}'

@_name_boundary.class_contract('BscUlockWake', {})
@meadow_dataclass
class meadow_BscUlockWake:
    ktraces: meadow_List
    operation: int
    addr: int
    wake_value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3d7939a'}, '__str__')
    def __str__(meadow_self_3d7939a):
        return f'ulock_wake({meadow_self_3d7939a.operation}, {hex(meadow_self_3d7939a.addr)}, {meadow_self_3d7939a.wake_value}), {meadow_self_3d7939a.result}'

@_name_boundary.class_contract('BscFclonefileat', {})
@meadow_dataclass
class meadow_BscFclonefileat:
    ktraces: meadow_List
    src_fd: int
    dst_dirfd: int
    dst: str
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6b8c7ae'}, '__str__')
    def __str__(meadow_self_6b8c7ae):
        meadow_rep_eaa34d5 = f'fclonefileat({meadow_self_6b8c7ae.src_fd}, {meadow_self_6b8c7ae.dst_dirfd}, "{meadow_self_6b8c7ae.dst}", {meadow_self_6b8c7ae.flags})'
        if meadow_self_6b8c7ae.result:
            meadow_rep_eaa34d5 += f', {meadow_self_6b8c7ae.result}'
        return meadow_rep_eaa34d5

@_name_boundary.class_contract('BscFsSnapshot', {})
@meadow_dataclass
class meadow_BscFsSnapshot:
    ktraces: meadow_List
    op: meadow_FsSnapshotOp
    dirfd: int
    name1: str
    name2: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0c63188'}, '__str__')
    def __str__(meadow_self_0c63188):
        meadow_rep_b49a9ae = f'''fs_snapshot({_name_boundary.attributes(meadow_self_0c63188.op)['name']}, {meadow_self_0c63188.dirfd}, "{meadow_self_0c63188.name1}", "{meadow_self_0c63188.name2}")'''
        if meadow_self_0c63188.result:
            meadow_rep_b49a9ae += f', {meadow_self_0c63188.result}'
        return meadow_rep_b49a9ae

@_name_boundary.class_contract('BscTerminateWithPayload', {})
@meadow_dataclass
class meadow_BscTerminateWithPayload:
    ktraces: meadow_List
    pid: int
    reason_namespace: int
    reason_code: int
    payload: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_354f35e'}, '__str__')
    def __str__(meadow_self_354f35e):
        meadow_rep_1221148 = f'terminate_with_payload({meadow_self_354f35e.pid}, {meadow_self_354f35e.reason_namespace}, {hex(meadow_self_354f35e.reason_code)}, {hex(meadow_self_354f35e.payload)})'
        if meadow_self_354f35e.result:
            meadow_rep_1221148 += f', {meadow_self_354f35e.result}'
        return meadow_rep_1221148

@_name_boundary.class_contract('BscAbortWithPayload', {})
@meadow_dataclass
class meadow_BscAbortWithPayload:
    ktraces: meadow_List
    reason_namespace: int
    reason_code: int
    payload: int
    payload_size: int

    @_name_boundary.callable_contract({'self': 'meadow_self_da5a914'}, '__str__')
    def __str__(meadow_self_da5a914):
        return f'abort_with_payload({meadow_self_da5a914.reason_namespace}, {hex(meadow_self_da5a914.reason_code)}, {hex(meadow_self_da5a914.payload)}, {meadow_self_da5a914.payload_size})'

@_name_boundary.class_contract('BscNecpSessionOpen', {})
@meadow_dataclass
class meadow_BscNecpSessionOpen:
    ktraces: meadow_List
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_13de4b3'}, '__str__')
    def __str__(meadow_self_13de4b3):
        return f'necp_session_open({meadow_self_13de4b3.flags}), {meadow_self_13de4b3.result}'

@_name_boundary.class_contract('BscNecpSessionAction', {})
@meadow_dataclass
class meadow_BscNecpSessionAction:
    ktraces: meadow_List
    necp_fd: int
    action: int
    in_buffer: int
    in_buffer_length: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6d6464d'}, '__str__')
    def __str__(meadow_self_6d6464d):
        meadow_rep_4d06dcc = f'necp_session_action({meadow_self_6d6464d.necp_fd}, {meadow_self_6d6464d.action}, {hex(meadow_self_6d6464d.in_buffer)}, {meadow_self_6d6464d.in_buffer_length})'
        if meadow_self_6d6464d.result:
            meadow_rep_4d06dcc += f', {meadow_self_6d6464d.result}'
        return meadow_rep_4d06dcc

@_name_boundary.class_contract('BscSetattrlistat', {})
@meadow_dataclass
class meadow_BscSetattrlistat:
    ktraces: meadow_List
    fd: int
    path: str
    alist: int
    attributeBuffer: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_093a37c'}, '__str__')
    def __str__(meadow_self_093a37c):
        meadow_rep_3e1c490 = f'setattrlistat({meadow_self_093a37c.fd}, "{meadow_self_093a37c.path}", {hex(meadow_self_093a37c.alist)}, {hex(meadow_self_093a37c.attributeBuffer)})'
        if meadow_self_093a37c.result:
            meadow_rep_3e1c490 += f', {meadow_self_093a37c.result}'
        return meadow_rep_3e1c490

@_name_boundary.class_contract('BscNetQosGuideline', {})
@meadow_dataclass
class meadow_BscNetQosGuideline:
    ktraces: meadow_List
    param: int
    param_len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6f81a82'}, '__str__')
    def __str__(meadow_self_6f81a82):
        return f'net_qos_guideline({hex(meadow_self_6f81a82.param)}, {meadow_self_6f81a82.param_len}), {meadow_self_6f81a82.result}'

@_name_boundary.class_contract('BscFmount', {})
@meadow_dataclass
class meadow_BscFmount:
    ktraces: meadow_List
    type: int
    fd: int
    flags: int
    data: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fdee4e0'}, '__str__')
    def __str__(meadow_self_fdee4e0):
        meadow_rep_ad835dd = f'fmount({hex(meadow_self_fdee4e0.type)}, {meadow_self_fdee4e0.fd}, {meadow_self_fdee4e0.flags}, {hex(meadow_self_fdee4e0.data)})'
        if meadow_self_fdee4e0.result:
            meadow_rep_ad835dd += f', {meadow_self_fdee4e0.result}'
        return meadow_rep_ad835dd

@_name_boundary.class_contract('BscNtpAdjtime', {})
@meadow_dataclass
class meadow_BscNtpAdjtime:
    ktraces: meadow_List
    tp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_75aeffb'}, '__str__')
    def __str__(meadow_self_75aeffb):
        return f'ntp_adjtime({hex(meadow_self_75aeffb.tp)}), {meadow_self_75aeffb.result}'

@_name_boundary.class_contract('BscNtpGettime', {})
@meadow_dataclass
class meadow_BscNtpGettime:
    ktraces: meadow_List
    ntvp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6d0603a'}, '__str__')
    def __str__(meadow_self_6d0603a):
        meadow_rep_89613f9 = f'ntp_gettime({hex(meadow_self_6d0603a.ntvp)})'
        if meadow_self_6d0603a.result:
            meadow_rep_89613f9 += f', {meadow_self_6d0603a.result}'
        return meadow_rep_89613f9

@_name_boundary.class_contract('BscOsFaultWithPayload', {})
@meadow_dataclass
class meadow_BscOsFaultWithPayload:
    ktraces: meadow_List
    reason_namespace: int
    reason_code: int
    payload: int
    payload_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0807c5b'}, '__str__')
    def __str__(meadow_self_0807c5b):
        meadow_rep_bd36522 = f'os_fault_with_payload({meadow_self_0807c5b.reason_namespace}, {hex(meadow_self_0807c5b.reason_code)}, {hex(meadow_self_0807c5b.payload)}, {meadow_self_0807c5b.payload_size})'
        if meadow_self_0807c5b.result:
            meadow_rep_bd36522 += f', {meadow_self_0807c5b.result}'
        return meadow_rep_bd36522

@_name_boundary.class_contract('BscKqueueWorkloopCtl', {})
@meadow_dataclass
class meadow_BscKqueueWorkloopCtl:
    ktraces: meadow_List
    cmd: int
    options: int
    addr: int
    sz: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_bd5836a'}, '__str__')
    def __str__(meadow_self_bd5836a):
        meadow_rep_4ed8d24 = f'kqueue_workloop_ctl({meadow_self_bd5836a.cmd}, {meadow_self_bd5836a.options}, {hex(meadow_self_bd5836a.addr)}, {meadow_self_bd5836a.sz})'
        if meadow_self_bd5836a.result:
            meadow_rep_4ed8d24 += f', {meadow_self_bd5836a.result}'
        return meadow_rep_4ed8d24

@_name_boundary.class_contract('BscMachBridgeRemoteTime', {})
@meadow_dataclass
class meadow_BscMachBridgeRemoteTime:
    ktraces: meadow_List
    local_timestamp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_783fe8e'}, '__str__')
    def __str__(meadow_self_783fe8e):
        meadow_rep_1f4a2bc = f'mach_bridge_remote_time({meadow_self_783fe8e.local_timestamp})'
        if meadow_self_783fe8e.result:
            meadow_rep_1f4a2bc += f', {meadow_self_783fe8e.result}'
        return meadow_rep_1f4a2bc

@_name_boundary.class_contract('BscCoalitionLedger', {})
@meadow_dataclass
class meadow_BscCoalitionLedger:
    ktraces: meadow_List
    operation: int
    cid: int
    buffer: int
    bufsize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7be905c'}, '__str__')
    def __str__(meadow_self_7be905c):
        meadow_rep_87e78b0 = f'coalition_ledger({meadow_self_7be905c.operation}, {hex(meadow_self_7be905c.cid)}, {hex(meadow_self_7be905c.buffer)}, {hex(meadow_self_7be905c.bufsize)})'
        if meadow_self_7be905c.result:
            meadow_rep_87e78b0 += f', {meadow_self_7be905c.result}'
        return meadow_rep_87e78b0

@_name_boundary.class_contract('BscLogData', {})
@meadow_dataclass
class meadow_BscLogData:
    ktraces: meadow_List
    tag: int
    flags: int
    buffer: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cf679ba'}, '__str__')
    def __str__(meadow_self_cf679ba):
        meadow_rep_28de66b = f'log_data({meadow_self_cf679ba.tag}, {meadow_self_cf679ba.flags}, {hex(meadow_self_cf679ba.buffer)}, {meadow_self_cf679ba.size})'
        if meadow_self_cf679ba.result:
            meadow_rep_28de66b += f', {meadow_self_cf679ba.result}'
        return meadow_rep_28de66b

@_name_boundary.class_contract('BscMemorystatusAvailableMemory', {})
@meadow_dataclass
class meadow_BscMemorystatusAvailableMemory:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b4a29d6'}, '__str__')
    def __str__(meadow_self_b4a29d6):
        return f'memorystatus_available_memory(), {meadow_self_b4a29d6.result}'

@_name_boundary.class_contract('BscSharedRegionMapAndSlide2Np', {})
@meadow_dataclass
class meadow_BscSharedRegionMapAndSlide2Np:
    ktraces: meadow_List
    files_count: int
    shared_file_np: int
    mappings_count: int
    mappings: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4d6fb5e'}, '__str__')
    def __str__(meadow_self_4d6fb5e):
        meadow_rep_f97ffa7 = f'shared_region_map_and_slide_2_np({meadow_self_4d6fb5e.files_count}, {hex(meadow_self_4d6fb5e.shared_file_np)}, {hex(meadow_self_4d6fb5e.mappings_count)}, {hex(meadow_self_4d6fb5e.mappings)})'
        if meadow_self_4d6fb5e.result:
            meadow_rep_f97ffa7 += f', {meadow_self_4d6fb5e.result}'
        return meadow_rep_f97ffa7

@_name_boundary.class_contract('BscPivotRoot', {})
@meadow_dataclass
class meadow_BscPivotRoot:
    ktraces: meadow_List
    new_rootfs_path_before: str
    old_rootfs_path_after: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e88a5df'}, '__str__')
    def __str__(meadow_self_e88a5df):
        meadow_rep_dc80809 = f'pivot_root("{meadow_self_e88a5df.new_rootfs_path_before}", "{meadow_self_e88a5df.old_rootfs_path_after}")'
        if meadow_self_e88a5df.result:
            meadow_rep_dc80809 += f', {meadow_self_e88a5df.result}'
        return meadow_rep_dc80809

@_name_boundary.class_contract('BscTaskInspectForPid', {})
@meadow_dataclass
class meadow_BscTaskInspectForPid:
    ktraces: meadow_List
    target_tport: int
    pid: int
    t: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_35f079c'}, '__str__')
    def __str__(meadow_self_35f079c):
        meadow_rep_8ccefe4 = f'task_inspect_for_pid({meadow_self_35f079c.target_tport}, {meadow_self_35f079c.pid}, {meadow_self_35f079c.t})'
        if meadow_self_35f079c.result:
            meadow_rep_8ccefe4 += f', {meadow_self_35f079c.result}'
        return meadow_rep_8ccefe4

@_name_boundary.class_contract('BscTaskReadForPid', {})
@meadow_dataclass
class meadow_BscTaskReadForPid:
    ktraces: meadow_List
    target_tport: int
    pid: int
    t: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b475ddb'}, '__str__')
    def __str__(meadow_self_b475ddb):
        meadow_rep_9aa726b = f'task_read_for_pid({meadow_self_b475ddb.target_tport}, {meadow_self_b475ddb.pid}, {meadow_self_b475ddb.t})'
        if meadow_self_b475ddb.result:
            meadow_rep_9aa726b += f', {meadow_self_b475ddb.result}'
        return meadow_rep_9aa726b

@_name_boundary.class_contract('BscSysPreadv', {})
@meadow_dataclass
class meadow_BscSysPreadv:
    ktraces: meadow_List
    fd: int
    iovp: int
    iovcnt: int
    offset: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_3fcc6d8'}, '__str__')
    def __str__(meadow_self_3fcc6d8):
        meadow_no_cancel_3f677ba = '_nocancel' if meadow_self_3fcc6d8.no_cancel else ''
        return f'preadv{meadow_no_cancel_3f677ba}({meadow_self_3fcc6d8.fd}, {hex(meadow_self_3fcc6d8.iovp)}, {meadow_self_3fcc6d8.iovcnt}, {meadow_self_3fcc6d8.offset}), {meadow_self_3fcc6d8.result}'

@_name_boundary.class_contract('BscSysPwritev', {})
@meadow_dataclass
class meadow_BscSysPwritev:
    ktraces: meadow_List
    fd: int
    iovp: int
    iovcnt: int
    offset: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_098a260'}, '__str__')
    def __str__(meadow_self_098a260):
        meadow_no_cancel_cc148ee = '_nocancel' if meadow_self_098a260.no_cancel else ''
        return f'pwritev{meadow_no_cancel_cc148ee}({meadow_self_098a260.fd}, {hex(meadow_self_098a260.iovp)}, {meadow_self_098a260.iovcnt}, {meadow_self_098a260.offset}), {meadow_self_098a260.result}'

@_name_boundary.class_contract('BscUlockWait2', {})
@meadow_dataclass
class meadow_BscUlockWait2:
    ktraces: meadow_List
    operation: int
    addr: int
    value: int
    timeout: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1cdbaec'}, '__str__')
    def __str__(meadow_self_1cdbaec):
        return f'ulock_wait2({meadow_self_1cdbaec.operation}, {hex(meadow_self_1cdbaec.addr)}, {meadow_self_1cdbaec.value}, {meadow_self_1cdbaec.timeout}), {meadow_self_1cdbaec.result}'

@_name_boundary.class_contract('BscProcInfoExtendedId', {})
@meadow_dataclass
class meadow_BscProcInfoExtendedId:
    ktraces: meadow_List
    callnum: int
    pid: int
    flavor: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0f07922'}, '__str__')
    def __str__(meadow_self_0f07922):
        meadow_rep_ed1dc50 = f'proc_info_extended_id({meadow_self_0f07922.callnum}, {meadow_self_0f07922.pid}, {meadow_self_0f07922.flavor}, {meadow_self_0f07922.flags})'
        if meadow_self_0f07922.result:
            meadow_rep_ed1dc50 += f', {meadow_self_0f07922.result}'
        return meadow_rep_ed1dc50

@_name_boundary.class_contract('BscSysClose', {})
@meadow_dataclass
class meadow_BscSysClose:
    ktraces: meadow_List
    fd: str
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_8ef2902'}, '__str__')
    def __str__(meadow_self_8ef2902):
        meadow_no_cancel_31a2853 = '_nocancel' if meadow_self_8ef2902.no_cancel else ''
        meadow_rep_9469037 = f'close{meadow_no_cancel_31a2853}({meadow_self_8ef2902.fd})'
        if meadow_self_8ef2902.result:
            meadow_rep_9469037 += f', {meadow_self_8ef2902.result}'
        return meadow_rep_9469037

@_name_boundary.class_contract('BscLink', {})
@meadow_dataclass
class meadow_BscLink:
    ktraces: meadow_List
    oldpath: str
    newpath: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e5f3fd7'}, '__str__')
    def __str__(meadow_self_e5f3fd7):
        meadow_rep_a5db4af = f'link("{meadow_self_e5f3fd7.oldpath}", "{meadow_self_e5f3fd7.newpath}")'
        if meadow_self_e5f3fd7.result:
            meadow_rep_a5db4af += f', {meadow_self_e5f3fd7.result}'
        return meadow_rep_a5db4af

@_name_boundary.class_contract('BscUnlink', {})
@meadow_dataclass
class meadow_BscUnlink:
    ktraces: meadow_List
    pathname: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_96ad4d0'}, '__str__')
    def __str__(meadow_self_96ad4d0):
        meadow_rep_598e97e = f'unlink("{meadow_self_96ad4d0.pathname}")'
        if meadow_self_96ad4d0.result:
            meadow_rep_598e97e += f', {meadow_self_96ad4d0.result}'
        return meadow_rep_598e97e

@_name_boundary.class_contract('BscChdir', {})
@meadow_dataclass
class meadow_BscChdir:
    ktraces: meadow_List
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c80c4a6'}, '__str__')
    def __str__(meadow_self_c80c4a6):
        meadow_rep_ecb6c24 = f'chdir("{meadow_self_c80c4a6.path}")'
        if meadow_self_c80c4a6.result:
            meadow_rep_ecb6c24 += f', {meadow_self_c80c4a6.result}'
        return meadow_rep_ecb6c24

@_name_boundary.class_contract('BscFchdir', {})
@meadow_dataclass
class meadow_BscFchdir:
    ktraces: meadow_List
    fd: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2ea09c9'}, '__str__')
    def __str__(meadow_self_2ea09c9):
        meadow_rep_07e101c = f'fchdir({meadow_self_2ea09c9.fd})'
        if meadow_self_2ea09c9.result:
            meadow_rep_07e101c += f', {meadow_self_2ea09c9.result}'
        return meadow_rep_07e101c

@_name_boundary.class_contract('BscMknod', {})
@meadow_dataclass
class meadow_BscMknod:
    ktraces: meadow_List
    pathname: str
    mode: int
    dev: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_08cb090'}, '__str__')
    def __str__(meadow_self_08cb090):
        meadow_rep_87293a5 = f'mknod("{meadow_self_08cb090.pathname}", {meadow_self_08cb090.mode}, {meadow_self_08cb090.dev})'
        if meadow_self_08cb090.result:
            meadow_rep_87293a5 += f', {meadow_self_08cb090.result}'
        return meadow_rep_87293a5

@_name_boundary.class_contract('BscChmod', {})
@meadow_dataclass
class meadow_BscChmod:
    ktraces: meadow_List
    pathname: str
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6a4bbff'}, '__str__')
    def __str__(meadow_self_6a4bbff):
        meadow_rep_5e6a1bb = f'''chmod("{meadow_self_6a4bbff.pathname}", {' | '.join(map(lambda meadow_f_3562290: _name_boundary.attributes(meadow_f_3562290)['name'], meadow_self_6a4bbff.mode))})'''
        if meadow_self_6a4bbff.result:
            meadow_rep_5e6a1bb += f', {meadow_self_6a4bbff.result}'
        return meadow_rep_5e6a1bb

@_name_boundary.class_contract('BscChown', {})
@meadow_dataclass
class meadow_BscChown:
    ktraces: meadow_List
    pathname: str
    owner: int
    group: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_796d03a'}, '__str__')
    def __str__(meadow_self_796d03a):
        meadow_rep_3114811 = f'chown("{meadow_self_796d03a.pathname}", {meadow_self_796d03a.owner}, {meadow_self_796d03a.group})'
        if meadow_self_796d03a.result:
            meadow_rep_3114811 += f', {meadow_self_796d03a.result}'
        return meadow_rep_3114811

@_name_boundary.class_contract('BscGetpid', {})
@meadow_dataclass
class meadow_BscGetpid:
    ktraces: meadow_List
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_b9eaa5c'}, '__str__')
    def __str__(meadow_self_b9eaa5c):
        return f'getpid(), pid: {meadow_self_b9eaa5c.pid}'

@_name_boundary.class_contract('BscSetuid', {})
@meadow_dataclass
class meadow_BscSetuid:
    ktraces: meadow_List
    uid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c3fcdc1'}, '__str__')
    def __str__(meadow_self_c3fcdc1):
        meadow_rep_829150e = f'setuid({meadow_self_c3fcdc1.uid})'
        if meadow_self_c3fcdc1.result:
            meadow_rep_829150e += f', {meadow_self_c3fcdc1.result}'
        return meadow_rep_829150e

@_name_boundary.class_contract('BscGetuid', {})
@meadow_dataclass
class meadow_BscGetuid:
    ktraces: meadow_List
    uid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_652e270'}, '__str__')
    def __str__(meadow_self_652e270):
        return f'getuid(), uid: {meadow_self_652e270.uid}'

@_name_boundary.class_contract('BscGeteuid', {})
@meadow_dataclass
class meadow_BscGeteuid:
    ktraces: meadow_List
    uid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_64089b1'}, '__str__')
    def __str__(meadow_self_64089b1):
        return f'geteuid(), uid: {meadow_self_64089b1.uid}'

@_name_boundary.class_contract('BscWait4', {})
@meadow_dataclass
class meadow_BscWait4:
    ktraces: meadow_List
    pid: int
    status: int
    options: int
    rusage: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_0ecbbc8'}, '__str__')
    def __str__(meadow_self_0ecbbc8):
        meadow_no_cancel_9f0b1d9 = '_nocancel' if meadow_self_0ecbbc8.no_cancel else ''
        return f'wait4{meadow_no_cancel_9f0b1d9}({meadow_self_0ecbbc8.pid}, {hex(meadow_self_0ecbbc8.status)}, {meadow_self_0ecbbc8.options}, {hex(meadow_self_0ecbbc8.rusage)}), {meadow_self_0ecbbc8.result}'

@_name_boundary.class_contract('BscRecvmsg', {})
@meadow_dataclass
class meadow_BscRecvmsg:
    ktraces: meadow_List
    socket: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_e086938'}, '__str__')
    def __str__(meadow_self_e086938):
        meadow_no_cancel_ec3f7e2 = '_nocancel' if meadow_self_e086938.no_cancel else ''
        return f'recvmsg{meadow_no_cancel_ec3f7e2}({meadow_self_e086938.socket}), {meadow_self_e086938.result}'

@_name_boundary.class_contract('BscSendmsg', {})
@meadow_dataclass
class meadow_BscSendmsg:
    ktraces: meadow_List
    socket: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_d237ed9'}, '__str__')
    def __str__(meadow_self_d237ed9):
        meadow_no_cancel_33853d1 = '_nocancel' if meadow_self_d237ed9.no_cancel else ''
        return f'sendmsg{meadow_no_cancel_33853d1}({meadow_self_d237ed9.socket}), {meadow_self_d237ed9.result}'

@_name_boundary.class_contract('BscRecvfrom', {})
@meadow_dataclass
class meadow_BscRecvfrom:
    ktraces: meadow_List
    socket: int
    buffer: int
    length: int
    flags: meadow_List
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_7da49f1'}, '__str__')
    def __str__(meadow_self_7da49f1):
        meadow_no_cancel_705150a = '_nocancel' if meadow_self_7da49f1.no_cancel else ''
        return f"recvfrom{meadow_no_cancel_705150a}({meadow_self_7da49f1.socket}, {hex(meadow_self_7da49f1.buffer)}, {meadow_self_7da49f1.length}, {(' | '.join(map(lambda meadow_f_9218d71: _name_boundary.attributes(meadow_f_9218d71)['name'], meadow_self_7da49f1.flags)) if meadow_self_7da49f1.flags else '0')}), {meadow_self_7da49f1.result}"

@_name_boundary.class_contract('BscAccept', {})
@meadow_dataclass
class meadow_BscAccept:
    ktraces: meadow_List
    socket: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_41bd103'}, '__str__')
    def __str__(meadow_self_41bd103):
        meadow_no_cancel_0ce9d7b = '_nocancel' if meadow_self_41bd103.no_cancel else ''
        return f'accept{meadow_no_cancel_0ce9d7b}({meadow_self_41bd103.socket}), {meadow_self_41bd103.result}'

@_name_boundary.class_contract('BscGetpeername', {})
@meadow_dataclass
class meadow_BscGetpeername:
    ktraces: meadow_List
    socket: int
    address: int
    address_len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7cc42df'}, '__str__')
    def __str__(meadow_self_7cc42df):
        meadow_rep_bd5a481 = f'getpeername({meadow_self_7cc42df.socket}, {hex(meadow_self_7cc42df.address)}, {hex(meadow_self_7cc42df.address_len)})'
        if meadow_self_7cc42df.result:
            meadow_rep_bd5a481 += f', {meadow_self_7cc42df.result}'
        return meadow_rep_bd5a481

@_name_boundary.class_contract('BscGetsockname', {})
@meadow_dataclass
class meadow_BscGetsockname:
    ktraces: meadow_List
    socket: int
    address: int
    address_len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2eed62b'}, '__str__')
    def __str__(meadow_self_2eed62b):
        meadow_rep_c821e7c = f'getsockname({meadow_self_2eed62b.socket}, {hex(meadow_self_2eed62b.address)}, {hex(meadow_self_2eed62b.address_len)})'
        if meadow_self_2eed62b.result:
            meadow_rep_c821e7c += f', {meadow_self_2eed62b.result}'
        return meadow_rep_c821e7c

@_name_boundary.class_contract('BscAccess', {})
@meadow_dataclass
class meadow_BscAccess:
    ktraces: meadow_List
    path: str
    amode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0a217f1'}, '__str__')
    def __str__(meadow_self_0a217f1):
        meadow_rep_8cd74a2 = f'''access("{meadow_self_0a217f1.path}", {' | '.join(map(lambda meadow_f_65193eb: _name_boundary.attributes(meadow_f_65193eb)['name'], meadow_self_0a217f1.amode))})'''
        if meadow_self_0a217f1.result:
            meadow_rep_8cd74a2 += f', {meadow_self_0a217f1.result}'
        return meadow_rep_8cd74a2

@_name_boundary.class_contract('BscChflags', {})
@meadow_dataclass
class meadow_BscChflags:
    ktraces: meadow_List
    path: str
    flags: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d24050d'}, '__str__')
    def __str__(meadow_self_d24050d):
        meadow_rep_74d8187 = f'''chflags("{meadow_self_d24050d.path}", {' | '.join(map(lambda meadow_f_8d3f7c1: _name_boundary.attributes(meadow_f_8d3f7c1)['name'], meadow_self_d24050d.flags))})'''
        if meadow_self_d24050d.result:
            meadow_rep_74d8187 += f', {meadow_self_d24050d.result}'
        return meadow_rep_74d8187

@_name_boundary.class_contract('BscFchflags', {})
@meadow_dataclass
class meadow_BscFchflags:
    ktraces: meadow_List
    fd: int
    flags: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1264ef8'}, '__str__')
    def __str__(meadow_self_1264ef8):
        meadow_rep_ced312c = f"fchflags({meadow_self_1264ef8.fd}, {' | '.join(map(lambda meadow_f_9670195: _name_boundary.attributes(meadow_f_9670195)['name'], meadow_self_1264ef8.flags))})"
        if meadow_self_1264ef8.result:
            meadow_rep_ced312c += f', {meadow_self_1264ef8.result}'
        return meadow_rep_ced312c

@_name_boundary.class_contract('BscSync', {})
@meadow_dataclass
class meadow_BscSync:
    ktraces: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_d724ce7'}, '__str__')
    def __str__(meadow_self_d724ce7):
        return 'sync()'

@_name_boundary.class_contract('BscKill', {})
@meadow_dataclass
class meadow_BscKill:
    ktraces: meadow_List
    pid: int
    sig: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a1585bf'}, '__str__')
    def __str__(meadow_self_a1585bf):
        meadow_rep_ec7f089 = f'kill({meadow_self_a1585bf.pid}, {meadow_self_a1585bf.sig})'
        if meadow_self_a1585bf.result:
            meadow_rep_ec7f089 += f', {meadow_self_a1585bf.result}'
        return meadow_rep_ec7f089

@_name_boundary.class_contract('BscGetppid', {})
@meadow_dataclass
class meadow_BscGetppid:
    ktraces: meadow_List
    pid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_adcba4a'}, '__str__')
    def __str__(meadow_self_adcba4a):
        return f'getppid(), pid: {meadow_self_adcba4a.pid}'

@_name_boundary.class_contract('BscSysDup', {})
@meadow_dataclass
class meadow_BscSysDup:
    ktraces: meadow_List
    fildes: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d0a16b6'}, '__str__')
    def __str__(meadow_self_d0a16b6):
        return f'dup({meadow_self_d0a16b6.fildes}), {meadow_self_d0a16b6.result}'

@_name_boundary.class_contract('BscPipe', {})
@meadow_dataclass
class meadow_BscPipe:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_703f278'}, '__str__')
    def __str__(meadow_self_703f278):
        return f'pipe(), {meadow_self_703f278.result}'

@_name_boundary.class_contract('BscGetegid', {})
@meadow_dataclass
class meadow_BscGetegid:
    ktraces: meadow_List
    gid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_29d425f'}, '__str__')
    def __str__(meadow_self_29d425f):
        return f'getegid(), gid: {meadow_self_29d425f.gid}'

@_name_boundary.class_contract('BscSigaction', {})
@meadow_dataclass
class meadow_BscSigaction:
    ktraces: meadow_List
    sig: meadow_Signals
    act: int
    oact: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9d8e44f'}, '__str__')
    def __str__(meadow_self_9d8e44f):
        meadow_rep_724578e = f"sigaction({_name_boundary.attributes(meadow_self_9d8e44f.sig)['name']}, {hex(meadow_self_9d8e44f.act)}, {hex(meadow_self_9d8e44f.oact)})"
        if meadow_self_9d8e44f.result:
            meadow_rep_724578e += f', {meadow_self_9d8e44f.result}'
        return meadow_rep_724578e

@_name_boundary.class_contract('BscGetgid', {})
@meadow_dataclass
class meadow_BscGetgid:
    ktraces: meadow_List
    gid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_44f1100'}, '__str__')
    def __str__(meadow_self_44f1100):
        return f'getgid(), gid: {meadow_self_44f1100.gid}'

@_name_boundary.class_contract('BscSigprocmap', {})
@meadow_dataclass
class meadow_BscSigprocmap:
    ktraces: meadow_List
    how: meadow_SigprocmaskFlags
    set: int
    oset: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9f021c2'}, '__str__')
    def __str__(meadow_self_9f021c2):
        meadow_rep_91151a1 = f"sigprocmask({_name_boundary.attributes(meadow_self_9f021c2.how)['name']}, {hex(meadow_self_9f021c2.set)}, {hex(meadow_self_9f021c2.oset)})"
        if meadow_self_9f021c2.result:
            meadow_rep_91151a1 += f', {meadow_self_9f021c2.result}'
        return meadow_rep_91151a1

@_name_boundary.class_contract('BscGetlogin', {})
@meadow_dataclass
class meadow_BscGetlogin:
    ktraces: meadow_List
    address: int

    @_name_boundary.callable_contract({'self': 'meadow_self_18f5463'}, '__str__')
    def __str__(meadow_self_18f5463):
        return f'getlogin(), address: {hex(meadow_self_18f5463.address)}'

@_name_boundary.class_contract('BscSetlogin', {})
@meadow_dataclass
class meadow_BscSetlogin:
    ktraces: meadow_List
    address: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9dc914f'}, '__str__')
    def __str__(meadow_self_9dc914f):
        meadow_rep_1b0ab9b = f'setlogin({hex(meadow_self_9dc914f.address)})'
        if meadow_self_9dc914f.result:
            meadow_rep_1b0ab9b += f', {meadow_self_9dc914f.result}'
        return meadow_rep_1b0ab9b

@_name_boundary.class_contract('BscAcct', {})
@meadow_dataclass
class meadow_BscAcct:
    ktraces: meadow_List
    file: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_41d99a3'}, '__str__')
    def __str__(meadow_self_41d99a3):
        meadow_rep_a4fb431 = f'acct("{meadow_self_41d99a3.file}")'
        if meadow_self_41d99a3.result:
            meadow_rep_a4fb431 += f', {meadow_self_41d99a3.result}'
        return meadow_rep_a4fb431

@_name_boundary.class_contract('BscSigpending', {})
@meadow_dataclass
class meadow_BscSigpending:
    ktraces: meadow_List
    set: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2b30ce7'}, '__str__')
    def __str__(meadow_self_2b30ce7):
        meadow_rep_b7d9bfa = f'sigpending({hex(meadow_self_2b30ce7.set)})'
        if meadow_self_2b30ce7.result:
            meadow_rep_b7d9bfa += f', {meadow_self_2b30ce7.result}'
        return meadow_rep_b7d9bfa

@_name_boundary.class_contract('BscSigaltstack', {})
@meadow_dataclass
class meadow_BscSigaltstack:
    ktraces: meadow_List
    ss_address: int
    oss_address: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fcca18f'}, '__str__')
    def __str__(meadow_self_fcca18f):
        meadow_rep_b9c9659 = f'sigaltstack({hex(meadow_self_fcca18f.ss_address)}, {hex(meadow_self_fcca18f.oss_address)})'
        if meadow_self_fcca18f.result:
            meadow_rep_b9c9659 += f', {meadow_self_fcca18f.result}'
        return meadow_rep_b9c9659

@_name_boundary.class_contract('BscIoctl', {})
@meadow_dataclass
class meadow_BscIoctl:
    ktraces: meadow_List
    fildes: int
    request: int
    arg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cf71778'}, '__str__')
    def __str__(meadow_self_cf71778):
        meadow_params_a2b7e6a = meadow_IOC_REQUEST_PARAMS[meadow_self_cf71778.request & 4026531840]
        meadow_group_1cb5c1a = chr(meadow_self_cf71778.request >> 8 & 255)
        meadow_number_a39f529 = meadow_self_cf71778.request & 255
        meadow_length_4db578d = meadow_self_cf71778.request >> 16 & 8191
        meadow_ioc_833c904 = f"_IOC({meadow_params_a2b7e6a}, '{meadow_group_1cb5c1a}', {meadow_number_a39f529}, {meadow_length_4db578d})"
        meadow_rep_7e30cdc = f'ioctl({meadow_self_cf71778.fildes}, {hex(meadow_self_cf71778.request)} /* {meadow_ioc_833c904} */, {hex(meadow_self_cf71778.arg)})'
        if meadow_self_cf71778.result:
            meadow_rep_7e30cdc += f', {meadow_self_cf71778.result}'
        return meadow_rep_7e30cdc

@_name_boundary.class_contract('BscReboot', {})
@meadow_dataclass
class meadow_BscReboot:
    ktraces: meadow_List
    howto: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ff12dac'}, '__str__')
    def __str__(meadow_self_ff12dac):
        meadow_rep_73d07e3 = f'reboot({meadow_self_ff12dac.howto})'
        if meadow_self_ff12dac.result:
            meadow_rep_73d07e3 += f', {meadow_self_ff12dac.result}'
        return meadow_rep_73d07e3

@_name_boundary.class_contract('BscRevoke', {})
@meadow_dataclass
class meadow_BscRevoke:
    ktraces: meadow_List
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8cc780b'}, '__str__')
    def __str__(meadow_self_8cc780b):
        meadow_rep_31cf489 = f'revoke("{meadow_self_8cc780b.path}")'
        if meadow_self_8cc780b.result:
            meadow_rep_31cf489 += f', {meadow_self_8cc780b.result}'
        return meadow_rep_31cf489

@_name_boundary.class_contract('BscSymlink', {})
@meadow_dataclass
class meadow_BscSymlink:
    ktraces: meadow_List
    vnode1: int
    path2: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9159826'}, '__str__')
    def __str__(meadow_self_9159826):
        meadow_rep_3937ee8 = f'symlink({meadow_self_9159826.vnode1}, "{meadow_self_9159826.path2}")'
        if meadow_self_9159826.result:
            meadow_rep_3937ee8 += f', {meadow_self_9159826.result}'
        return meadow_rep_3937ee8

@_name_boundary.class_contract('BscReadlink', {})
@meadow_dataclass
class meadow_BscReadlink:
    ktraces: meadow_List
    path: str
    buf: int
    bufsize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cda4358'}, '__str__')
    def __str__(meadow_self_cda4358):
        return f'readlink("{meadow_self_cda4358.path}", {hex(meadow_self_cda4358.buf)}, {meadow_self_cda4358.bufsize}), {meadow_self_cda4358.result}'

@_name_boundary.class_contract('BscExecve', {})
@meadow_dataclass
class meadow_BscExecve:
    ktraces: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_1b2aee6'}, '__str__')
    def __str__(meadow_self_1b2aee6):
        return 'execve()'

@_name_boundary.class_contract('BscUmask', {})
@meadow_dataclass
class meadow_BscUmask:
    ktraces: meadow_List
    cmask: int
    prev_mask: int

    @_name_boundary.callable_contract({'self': 'meadow_self_b59b538'}, '__str__')
    def __str__(meadow_self_b59b538):
        return f'umask({meadow_self_b59b538.cmask}), previous mask: {meadow_self_b59b538.prev_mask}'

@_name_boundary.class_contract('BscChroot', {})
@meadow_dataclass
class meadow_BscChroot:
    ktraces: meadow_List
    dirname: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c243535'}, '__str__')
    def __str__(meadow_self_c243535):
        meadow_rep_b8bf15d = f'chroot("{meadow_self_c243535.dirname}")'
        if meadow_self_c243535.result:
            meadow_rep_b8bf15d += f', {meadow_self_c243535.result}'
        return meadow_rep_b8bf15d

@_name_boundary.class_contract('BscMsync', {})
@meadow_dataclass
class meadow_BscMsync:
    ktraces: meadow_List
    addr: int
    len_: int
    flags: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_774fb0e'}, '__str__')
    def __str__(meadow_self_774fb0e):
        meadow_no_cancel_d3ed386 = '_nocancel' if meadow_self_774fb0e.no_cancel else ''
        meadow_rep_7562770 = f'msync{meadow_no_cancel_d3ed386}({hex(meadow_self_774fb0e.addr)}, {meadow_self_774fb0e.len_}, {meadow_self_774fb0e.flags})'
        if meadow_self_774fb0e.result:
            meadow_rep_7562770 += f', {meadow_self_774fb0e.result}'
        return meadow_rep_7562770

@_name_boundary.class_contract('BscVfork', {})
@meadow_dataclass
class meadow_BscVfork:
    ktraces: meadow_List

    @_name_boundary.callable_contract({'self': 'meadow_self_e351f4a'}, '__str__')
    def __str__(meadow_self_e351f4a):
        return 'vfork()'

@_name_boundary.class_contract('BscMunmap', {})
@meadow_dataclass
class meadow_BscMunmap:
    ktraces: meadow_List
    addr: int
    len_: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f307f59'}, '__str__')
    def __str__(meadow_self_f307f59):
        meadow_rep_ec2f70b = f'munmap({hex(meadow_self_f307f59.addr)}, {meadow_self_f307f59.len_})'
        if meadow_self_f307f59.result:
            meadow_rep_ec2f70b += f', {meadow_self_f307f59.result}'
        return meadow_rep_ec2f70b

@_name_boundary.class_contract('BscMprotect', {})
@meadow_dataclass
class meadow_BscMprotect:
    ktraces: meadow_List
    addr: int
    len_: int
    prot: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_965d2da'}, '__str__')
    def __str__(meadow_self_965d2da):
        meadow_rep_2f2a144 = f'mprotect({hex(meadow_self_965d2da.addr)}, {meadow_self_965d2da.len_}, {meadow_self_965d2da.prot})'
        if meadow_self_965d2da.result:
            meadow_rep_2f2a144 += f', {meadow_self_965d2da.result}'
        return meadow_rep_2f2a144

@_name_boundary.class_contract('BscMadvise', {})
@meadow_dataclass
class meadow_BscMadvise:
    ktraces: meadow_List
    addr: int
    len_: int
    advice: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e70be89'}, '__str__')
    def __str__(meadow_self_e70be89):
        meadow_rep_ec43e98 = f'madvise({hex(meadow_self_e70be89.addr)}, {meadow_self_e70be89.len_}, {meadow_self_e70be89.advice})'
        if meadow_self_e70be89.result:
            meadow_rep_ec43e98 += f', {meadow_self_e70be89.result}'
        return meadow_rep_ec43e98

@_name_boundary.class_contract('BscMincore', {})
@meadow_dataclass
class meadow_BscMincore:
    ktraces: meadow_List
    addr: int
    len_: int
    vec: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3f61f15'}, '__str__')
    def __str__(meadow_self_3f61f15):
        meadow_rep_abef5bf = f'mincore({hex(meadow_self_3f61f15.addr)}, {meadow_self_3f61f15.len_}, {hex(meadow_self_3f61f15.vec)})'
        if meadow_self_3f61f15.result:
            meadow_rep_abef5bf += f', {meadow_self_3f61f15.result}'
        return meadow_rep_abef5bf

@_name_boundary.class_contract('BscGetgroups', {})
@meadow_dataclass
class meadow_BscGetgroups:
    ktraces: meadow_List
    gidsetsize: int
    grouplist: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e6fdee2'}, '__str__')
    def __str__(meadow_self_e6fdee2):
        return f'getgroups({meadow_self_e6fdee2.gidsetsize}, {hex(meadow_self_e6fdee2.grouplist)}), {meadow_self_e6fdee2.result}'

@_name_boundary.class_contract('BscSetgroups', {})
@meadow_dataclass
class meadow_BscSetgroups:
    ktraces: meadow_List
    ngroups: int
    gidset: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_db06c86'}, '__str__')
    def __str__(meadow_self_db06c86):
        meadow_rep_fa94250 = f'setgroups({meadow_self_db06c86.ngroups}, {hex(meadow_self_db06c86.gidset)})'
        if meadow_self_db06c86.result:
            meadow_rep_fa94250 += f', {meadow_self_db06c86.result}'
        return meadow_rep_fa94250

@_name_boundary.class_contract('BscGetpgrp', {})
@meadow_dataclass
class meadow_BscGetpgrp:
    ktraces: meadow_List
    pgid: int

    @_name_boundary.callable_contract({'self': 'meadow_self_57eaeba'}, '__str__')
    def __str__(meadow_self_57eaeba):
        return f'getpgrp(), pgid: {meadow_self_57eaeba.pgid}'

@_name_boundary.class_contract('BscSetpgid', {})
@meadow_dataclass
class meadow_BscSetpgid:
    ktraces: meadow_List
    pid: int
    pgid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6f84527'}, '__str__')
    def __str__(meadow_self_6f84527):
        meadow_rep_2d0daa9 = f'setpgid({meadow_self_6f84527.pid}, {meadow_self_6f84527.pgid})'
        if meadow_self_6f84527.result:
            meadow_rep_2d0daa9 += f', {meadow_self_6f84527.result}'
        return meadow_rep_2d0daa9

@_name_boundary.class_contract('BscSetitimer', {})
@meadow_dataclass
class meadow_BscSetitimer:
    ktraces: meadow_List
    which: int
    value: int
    ovalue: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_274c3e0'}, '__str__')
    def __str__(meadow_self_274c3e0):
        meadow_rep_9424e9f = f'setitimer({meadow_self_274c3e0.which}, {hex(meadow_self_274c3e0.value)}, {hex(meadow_self_274c3e0.ovalue)})'
        if meadow_self_274c3e0.result:
            meadow_rep_9424e9f += f', {meadow_self_274c3e0.result}'
        return meadow_rep_9424e9f

@_name_boundary.class_contract('BscSwapon', {})
@meadow_dataclass
class meadow_BscSwapon:
    ktraces: meadow_List
    path: int
    swapflags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b505c46'}, '__str__')
    def __str__(meadow_self_b505c46):
        meadow_rep_940178f = f'swapon({meadow_self_b505c46.path}, {meadow_self_b505c46.swapflags})'
        if meadow_self_b505c46.result:
            meadow_rep_940178f += f', {meadow_self_b505c46.result}'
        return meadow_rep_940178f

@_name_boundary.class_contract('BscGetitimer', {})
@meadow_dataclass
class meadow_BscGetitimer:
    ktraces: meadow_List
    which: int
    value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_724338f'}, '__str__')
    def __str__(meadow_self_724338f):
        meadow_rep_516ebe2 = f'getitimer({meadow_self_724338f.which}, {hex(meadow_self_724338f.value)})'
        if meadow_self_724338f.result:
            meadow_rep_516ebe2 += f', {meadow_self_724338f.result}'
        return meadow_rep_516ebe2

@_name_boundary.class_contract('BscSysGetdtablesize', {})
@meadow_dataclass
class meadow_BscSysGetdtablesize:
    ktraces: meadow_List
    table_size: int

    @_name_boundary.callable_contract({'self': 'meadow_self_17df248'}, '__str__')
    def __str__(meadow_self_17df248):
        return f'getdtablesize(), size: {meadow_self_17df248.table_size}'

@_name_boundary.class_contract('BscSysDup2', {})
@meadow_dataclass
class meadow_BscSysDup2:
    ktraces: meadow_List
    fildes: int
    fildes2: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_177c1ca'}, '__str__')
    def __str__(meadow_self_177c1ca):
        meadow_rep_ca3bbc6 = f'dup2({meadow_self_177c1ca.fildes}, {meadow_self_177c1ca.fildes2})'
        if meadow_self_177c1ca.result:
            meadow_rep_ca3bbc6 += f', {meadow_self_177c1ca.result}'
        return meadow_rep_ca3bbc6

@_name_boundary.class_contract('BscSysFcntl', {})
@meadow_dataclass
class meadow_BscSysFcntl:
    ktraces: meadow_List
    fildes: int
    cmd: meadow_FcntlCmd
    buf: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_d9576df'}, '__str__')
    def __str__(meadow_self_d9576df):
        meadow_no_cancel_11dbbe6 = '_nocancel' if meadow_self_d9576df.no_cancel else ''
        return f"fcntl{meadow_no_cancel_11dbbe6}({meadow_self_d9576df.fildes}, {_name_boundary.attributes(meadow_self_d9576df.cmd)['name']}, {hex(meadow_self_d9576df.buf)}), {meadow_self_d9576df.result}"

@_name_boundary.class_contract('BscSelect', {})
@meadow_dataclass
class meadow_BscSelect:
    ktraces: meadow_List
    nfds: int
    readfds: int
    writefds: int
    errorfds: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_ab5874f'}, '__str__')
    def __str__(meadow_self_ab5874f):
        meadow_no_cancel_021a2d2 = '_nocancel' if meadow_self_ab5874f.no_cancel else ''
        return f'select{meadow_no_cancel_021a2d2}({meadow_self_ab5874f.nfds}, {hex(meadow_self_ab5874f.readfds)}, {hex(meadow_self_ab5874f.writefds)}, {hex(meadow_self_ab5874f.errorfds)}), {meadow_self_ab5874f.result}'

@_name_boundary.class_contract('BscFsync', {})
@meadow_dataclass
class meadow_BscFsync:
    ktraces: meadow_List
    fildes: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_b4fcdc9'}, '__str__')
    def __str__(meadow_self_b4fcdc9):
        meadow_no_cancel_190f57e = '_nocancel' if meadow_self_b4fcdc9.no_cancel else ''
        meadow_rep_aef0b67 = f'fsync{meadow_no_cancel_190f57e}({meadow_self_b4fcdc9.fildes})'
        if meadow_self_b4fcdc9.result:
            meadow_rep_aef0b67 += f', {meadow_self_b4fcdc9.result}'
        return meadow_rep_aef0b67

@_name_boundary.class_contract('BscSetpriority', {})
@meadow_dataclass
class meadow_BscSetpriority:
    ktraces: meadow_List
    which: meadow_PriorityWhich
    who: int
    prio: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4af8301'}, '__str__')
    def __str__(meadow_self_4af8301):
        meadow_rep_162df19 = f"setpriority({_name_boundary.attributes(meadow_self_4af8301.which)['name']}, {meadow_self_4af8301.who}, {meadow_self_4af8301.prio})"
        if meadow_self_4af8301.result:
            meadow_rep_162df19 += f', {meadow_self_4af8301.result}'
        return meadow_rep_162df19

@_name_boundary.class_contract('BscSocket', {})
@meadow_dataclass
class meadow_BscSocket:
    ktraces: meadow_List
    domain: meadow_socket.AddressFamily
    type: meadow_socket.SocketKind
    protocol: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2278d6e'}, '__str__')
    def __str__(meadow_self_2278d6e):
        return f"socket({_name_boundary.attributes(meadow_self_2278d6e.domain)['name']}, {_name_boundary.attributes(meadow_self_2278d6e.type)['name']}, {meadow_self_2278d6e.protocol}), {meadow_self_2278d6e.result}"

@_name_boundary.class_contract('BscConnect', {})
@meadow_dataclass
class meadow_BscConnect:
    ktraces: meadow_List
    socket: int
    address: int
    address_len: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_3bb8995'}, '__str__')
    def __str__(meadow_self_3bb8995):
        meadow_no_cancel_913a0a9 = '_nocancel' if meadow_self_3bb8995.no_cancel else ''
        meadow_rep_be0c77c = f'connect{meadow_no_cancel_913a0a9}({meadow_self_3bb8995.socket}, {hex(meadow_self_3bb8995.address)}, {meadow_self_3bb8995.address_len})'
        if meadow_self_3bb8995.result:
            meadow_rep_be0c77c += f', {meadow_self_3bb8995.result}'
        return meadow_rep_be0c77c

@_name_boundary.class_contract('BscGetpriority', {})
@meadow_dataclass
class meadow_BscGetpriority:
    ktraces: meadow_List
    which: meadow_PriorityWhich
    who: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fc293bb'}, '__str__')
    def __str__(meadow_self_fc293bb):
        return f"getpriority({_name_boundary.attributes(meadow_self_fc293bb.which)['name']}, {meadow_self_fc293bb.who}), {meadow_self_fc293bb.result}"

@_name_boundary.class_contract('BscBind', {})
@meadow_dataclass
class meadow_BscBind:
    ktraces: meadow_List
    socket: int
    address: int
    address_len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0fff696'}, '__str__')
    def __str__(meadow_self_0fff696):
        meadow_rep_31aa6e8 = f'bind({meadow_self_0fff696.socket}, {hex(meadow_self_0fff696.address)}, {meadow_self_0fff696.address_len})'
        if meadow_self_0fff696.result:
            meadow_rep_31aa6e8 += f', {meadow_self_0fff696.result}'
        return meadow_rep_31aa6e8

@_name_boundary.class_contract('BscSetsockopt', {})
@meadow_dataclass
class meadow_BscSetsockopt:
    ktraces: meadow_List
    socket: int
    level: int
    option_name: int
    option_value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4dc4356'}, '__str__')
    def __str__(meadow_self_4dc4356):
        meadow_level_51486ca, meadow_option_8333db8 = meadow_sockopt_format_level_and_option(meadow_self_4dc4356.level, meadow_self_4dc4356.option_name)
        meadow_rep_301213c = f'setsockopt({meadow_self_4dc4356.socket}, {meadow_level_51486ca}, {meadow_option_8333db8}, {hex(meadow_self_4dc4356.option_value)})'
        if meadow_self_4dc4356.result:
            meadow_rep_301213c += f', {meadow_self_4dc4356.result}'
        return meadow_rep_301213c

@_name_boundary.class_contract('BscListen', {})
@meadow_dataclass
class meadow_BscListen:
    ktraces: meadow_List
    socket: int
    backlog: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1853690'}, '__str__')
    def __str__(meadow_self_1853690):
        meadow_rep_cc839fc = f'listen({meadow_self_1853690.socket}, {meadow_self_1853690.backlog})'
        if meadow_self_1853690.result:
            meadow_rep_cc839fc += f', {meadow_self_1853690.result}'
        return meadow_rep_cc839fc

@_name_boundary.class_contract('BscSigsuspend', {})
@meadow_dataclass
class meadow_BscSigsuspend:
    ktraces: meadow_List
    sigmask: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_cf6f862'}, '__str__')
    def __str__(meadow_self_cf6f862):
        meadow_no_cancel_bad5003 = '_nocancel' if meadow_self_cf6f862.no_cancel else ''
        meadow_rep_9aac86a = f'sigsuspend{meadow_no_cancel_bad5003}({hex(meadow_self_cf6f862.sigmask)})'
        if meadow_self_cf6f862.result:
            meadow_rep_9aac86a += f', {meadow_self_cf6f862.result}'
        return meadow_rep_9aac86a

@_name_boundary.class_contract('BscGettimeofday', {})
@meadow_dataclass
class meadow_BscGettimeofday:
    ktraces: meadow_List
    tv: int
    tz: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_73ed2a7'}, '__str__')
    def __str__(meadow_self_73ed2a7):
        meadow_rep_2f0d415 = f'gettimeofday({hex(meadow_self_73ed2a7.tv)}, {hex(meadow_self_73ed2a7.tz)})'
        if meadow_self_73ed2a7.result:
            meadow_rep_2f0d415 += f', {meadow_self_73ed2a7.result}'
        return meadow_rep_2f0d415

@_name_boundary.class_contract('BscGetrusage', {})
@meadow_dataclass
class meadow_BscGetrusage:
    ktraces: meadow_List
    who: meadow_RusageWho
    r_usage: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ca745f4'}, '__str__')
    def __str__(meadow_self_ca745f4):
        meadow_rep_a17a6c6 = f"getrusage({_name_boundary.attributes(meadow_self_ca745f4.who)['name']}, {meadow_self_ca745f4.r_usage})"
        if meadow_self_ca745f4.result:
            meadow_rep_a17a6c6 += f', {meadow_self_ca745f4.result}'
        return meadow_rep_a17a6c6

@_name_boundary.class_contract('BscGetsockopt', {})
@meadow_dataclass
class meadow_BscGetsockopt:
    ktraces: meadow_List
    socket: int
    level: int
    option_name: int
    option_value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_36d1840'}, '__str__')
    def __str__(meadow_self_36d1840):
        meadow_level_22090a9, meadow_option_b2e1237 = meadow_sockopt_format_level_and_option(meadow_self_36d1840.level, meadow_self_36d1840.option_name)
        meadow_rep_2201458 = f'getsockopt({meadow_self_36d1840.socket}, {meadow_level_22090a9}, {meadow_option_b2e1237}, {hex(meadow_self_36d1840.option_value)})'
        if meadow_self_36d1840.result:
            meadow_rep_2201458 += f', {meadow_self_36d1840.result}'
        return meadow_rep_2201458

@_name_boundary.class_contract('BscReadv', {})
@meadow_dataclass
class meadow_BscReadv:
    ktraces: meadow_List
    d: int
    iov: int
    iovcnt: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_c7fbf64'}, '__str__')
    def __str__(meadow_self_c7fbf64):
        meadow_no_cancel_35ed7b6 = '_nocancel' if meadow_self_c7fbf64.no_cancel else ''
        return f'readv{meadow_no_cancel_35ed7b6}({meadow_self_c7fbf64.d}, {hex(meadow_self_c7fbf64.iov)}, {meadow_self_c7fbf64.iovcnt}), {meadow_self_c7fbf64.result}'

@_name_boundary.class_contract('BscWritev', {})
@meadow_dataclass
class meadow_BscWritev:
    ktraces: meadow_List
    fildes: int
    iov: int
    iovcnt: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_e518f2b'}, '__str__')
    def __str__(meadow_self_e518f2b):
        meadow_no_cancel_50a35bf = '_nocancel' if meadow_self_e518f2b.no_cancel else ''
        return f'writev{meadow_no_cancel_50a35bf}({meadow_self_e518f2b.fildes}, {hex(meadow_self_e518f2b.iov)}, {meadow_self_e518f2b.iovcnt}), {meadow_self_e518f2b.result}'

@_name_boundary.class_contract('BscSettimeofday', {})
@meadow_dataclass
class meadow_BscSettimeofday:
    ktraces: meadow_List
    tp: int
    tzp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9a1dc69'}, '__str__')
    def __str__(meadow_self_9a1dc69):
        meadow_rep_f2f529c = f'settimeofday({hex(meadow_self_9a1dc69.tp)}, {hex(meadow_self_9a1dc69.tzp)})'
        if meadow_self_9a1dc69.result:
            meadow_rep_f2f529c += f', {meadow_self_9a1dc69.result}'
        return meadow_rep_f2f529c

@_name_boundary.class_contract('BscFchown', {})
@meadow_dataclass
class meadow_BscFchown:
    ktraces: meadow_List
    fildes: int
    owner: int
    group: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b71ae19'}, '__str__')
    def __str__(meadow_self_b71ae19):
        meadow_rep_67d9e01 = f'fchown({meadow_self_b71ae19.fildes}, {meadow_self_b71ae19.owner}, {meadow_self_b71ae19.group})'
        if meadow_self_b71ae19.result:
            meadow_rep_67d9e01 += f', {meadow_self_b71ae19.result}'
        return meadow_rep_67d9e01

@_name_boundary.class_contract('BscFchmod', {})
@meadow_dataclass
class meadow_BscFchmod:
    ktraces: meadow_List
    fildes: str
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2c0e7e1'}, '__str__')
    def __str__(meadow_self_2c0e7e1):
        meadow_rep_55695fd = f"fchmod({meadow_self_2c0e7e1.fildes}, {' | '.join(map(lambda meadow_f_dc6d6e3: _name_boundary.attributes(meadow_f_dc6d6e3)['name'], meadow_self_2c0e7e1.mode))})"
        if meadow_self_2c0e7e1.result:
            meadow_rep_55695fd += f', {meadow_self_2c0e7e1.result}'
        return meadow_rep_55695fd

@_name_boundary.class_contract('BscSetreuid', {})
@meadow_dataclass
class meadow_BscSetreuid:
    ktraces: meadow_List
    ruid: int
    euid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_35a691c'}, '__str__')
    def __str__(meadow_self_35a691c):
        meadow_rep_f8bd41a = f'setreuid({meadow_self_35a691c.ruid}, {meadow_self_35a691c.euid})'
        if meadow_self_35a691c.result:
            meadow_rep_f8bd41a += f', {meadow_self_35a691c.result}'
        return meadow_rep_f8bd41a

@_name_boundary.class_contract('BscSetregid', {})
@meadow_dataclass
class meadow_BscSetregid:
    ktraces: meadow_List
    rgid: int
    egid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_016d8a9'}, '__str__')
    def __str__(meadow_self_016d8a9):
        meadow_rep_7c5aca9 = f'setregid({meadow_self_016d8a9.rgid}, {meadow_self_016d8a9.egid})'
        if meadow_self_016d8a9.result:
            meadow_rep_7c5aca9 += f', {meadow_self_016d8a9.result}'
        return meadow_rep_7c5aca9

@_name_boundary.class_contract('BscRename', {})
@meadow_dataclass
class meadow_BscRename:
    ktraces: meadow_List
    old: str
    new: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_37b7c25'}, '__str__')
    def __str__(meadow_self_37b7c25):
        meadow_rep_fe5ca85 = f'rename("{meadow_self_37b7c25.old}", "{meadow_self_37b7c25.new}")'
        if meadow_self_37b7c25.result:
            meadow_rep_fe5ca85 += f', {meadow_self_37b7c25.result}'
        return meadow_rep_fe5ca85

@_name_boundary.class_contract('BscSysFlock', {})
@meadow_dataclass
class meadow_BscSysFlock:
    ktraces: meadow_List
    fd: int
    operation: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_377c14f'}, '__str__')
    def __str__(meadow_self_377c14f):
        meadow_rep_3eb7568 = f"flock({meadow_self_377c14f.fd}, {' | '.join(map(lambda meadow_o_56523d7: _name_boundary.attributes(meadow_o_56523d7)['name'], meadow_self_377c14f.operation))})"
        if meadow_self_377c14f.result:
            meadow_rep_3eb7568 += f', {meadow_self_377c14f.result}'
        return meadow_rep_3eb7568

@_name_boundary.class_contract('BscMkfifo', {})
@meadow_dataclass
class meadow_BscMkfifo:
    ktraces: meadow_List
    path: str
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2ddb8dc'}, '__str__')
    def __str__(meadow_self_2ddb8dc):
        meadow_rep_475705f = f'''mkfifo("{meadow_self_2ddb8dc.path}", {' | '.join(map(lambda meadow_f_5480418: _name_boundary.attributes(meadow_f_5480418)['name'], meadow_self_2ddb8dc.mode))})'''
        if meadow_self_2ddb8dc.result:
            meadow_rep_475705f += f', {meadow_self_2ddb8dc.result}'
        return meadow_rep_475705f

@_name_boundary.class_contract('BscSendto', {})
@meadow_dataclass
class meadow_BscSendto:
    ktraces: meadow_List
    socket: int
    buffer: int
    length: int
    flags: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_b326ea0'}, '__str__')
    def __str__(meadow_self_b326ea0):
        meadow_no_cancel_435a5e7 = '_nocancel' if meadow_self_b326ea0.no_cancel else ''
        return f'sendto{meadow_no_cancel_435a5e7}({meadow_self_b326ea0.socket}, {hex(meadow_self_b326ea0.buffer)}, {meadow_self_b326ea0.length}, {meadow_self_b326ea0.flags}), {meadow_self_b326ea0.result}'

@_name_boundary.class_contract('BscShutdown', {})
@meadow_dataclass
class meadow_BscShutdown:
    ktraces: meadow_List
    socket: int
    how: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_19d6983'}, '__str__')
    def __str__(meadow_self_19d6983):
        meadow_rep_c7a8278 = f'shutdown({meadow_self_19d6983.socket}, {meadow_self_19d6983.how})'
        if meadow_self_19d6983.result:
            meadow_rep_c7a8278 += f', {meadow_self_19d6983.result}'
        return meadow_rep_c7a8278

@_name_boundary.class_contract('BscSocketpair', {})
@meadow_dataclass
class meadow_BscSocketpair:
    ktraces: meadow_List
    domain: meadow_socket.AddressFamily
    type: meadow_socket.SocketKind
    protocol: int
    socket_vector: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_288fed4'}, '__str__')
    def __str__(meadow_self_288fed4):
        meadow_rep_c709634 = f"socketpair({_name_boundary.attributes(meadow_self_288fed4.domain)['name']}, {_name_boundary.attributes(meadow_self_288fed4.type)['name']}, {meadow_self_288fed4.protocol}, {hex(meadow_self_288fed4.socket_vector)})"
        if meadow_self_288fed4.result:
            meadow_rep_c709634 += f', {meadow_self_288fed4.result}'
        return meadow_rep_c709634

@_name_boundary.class_contract('BscMkdir', {})
@meadow_dataclass
class meadow_BscMkdir:
    ktraces: meadow_List
    path: str
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_140c6a7'}, '__str__')
    def __str__(meadow_self_140c6a7):
        meadow_rep_fcee434 = f'''mkdir("{meadow_self_140c6a7.path}", {' | '.join(map(lambda meadow_f_e6455db: _name_boundary.attributes(meadow_f_e6455db)['name'], meadow_self_140c6a7.mode))})'''
        if meadow_self_140c6a7.result:
            meadow_rep_fcee434 += f', {meadow_self_140c6a7.result}'
        return meadow_rep_fcee434

@_name_boundary.class_contract('BscRmdir', {})
@meadow_dataclass
class meadow_BscRmdir:
    ktraces: meadow_List
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d011982'}, '__str__')
    def __str__(meadow_self_d011982):
        meadow_rep_915e082 = f'rmdir("{meadow_self_d011982.path}")'
        if meadow_self_d011982.result:
            meadow_rep_915e082 += f', {meadow_self_d011982.result}'
        return meadow_rep_915e082

@_name_boundary.class_contract('BscUtimes', {})
@meadow_dataclass
class meadow_BscUtimes:
    ktraces: meadow_List
    path: str
    times: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e570cfc'}, '__str__')
    def __str__(meadow_self_e570cfc):
        meadow_rep_26963fa = f'utimes("{meadow_self_e570cfc.path}", {hex(meadow_self_e570cfc.times)})'
        if meadow_self_e570cfc.result:
            meadow_rep_26963fa += f', {meadow_self_e570cfc.result}'
        return meadow_rep_26963fa

@_name_boundary.class_contract('BscFutimes', {})
@meadow_dataclass
class meadow_BscFutimes:
    ktraces: meadow_List
    fildes: int
    times: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_029b7fd'}, '__str__')
    def __str__(meadow_self_029b7fd):
        meadow_rep_ed9489b = f'futimes({meadow_self_029b7fd.fildes}, {hex(meadow_self_029b7fd.times)})'
        if meadow_self_029b7fd.result:
            meadow_rep_ed9489b += f', {meadow_self_029b7fd.result}'
        return meadow_rep_ed9489b

@_name_boundary.class_contract('BscAdjtime', {})
@meadow_dataclass
class meadow_BscAdjtime:
    ktraces: meadow_List
    delta: int
    olddelta: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9a890aa'}, '__str__')
    def __str__(meadow_self_9a890aa):
        meadow_rep_4202ac6 = f'adjtime({hex(meadow_self_9a890aa.delta)}, {hex(meadow_self_9a890aa.olddelta)})'
        if meadow_self_9a890aa.result:
            meadow_rep_4202ac6 += f', {meadow_self_9a890aa.result}'
        return meadow_rep_4202ac6

@_name_boundary.class_contract('BscGethostuuid', {})
@meadow_dataclass
class meadow_BscGethostuuid:
    ktraces: meadow_List
    uuid: int
    timeout: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3cd3771'}, '__str__')
    def __str__(meadow_self_3cd3771):
        meadow_rep_a3ac0c6 = f'gethostuuid({hex(meadow_self_3cd3771.uuid)}, {hex(meadow_self_3cd3771.timeout)})'
        if meadow_self_3cd3771.result:
            meadow_rep_a3ac0c6 += f', {meadow_self_3cd3771.result}'
        return meadow_rep_a3ac0c6

@_name_boundary.class_contract('BscObsKillpg', {})
@meadow_dataclass
class meadow_BscObsKillpg:
    ktraces: meadow_List
    pgrp: int
    sig: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c7bc508'}, '__str__')
    def __str__(meadow_self_c7bc508):
        meadow_rep_575ccb1 = f'killpg({meadow_self_c7bc508.pgrp}, {meadow_self_c7bc508.sig})'
        if meadow_self_c7bc508.result:
            meadow_rep_575ccb1 += f', {meadow_self_c7bc508.result}'
        return meadow_rep_575ccb1

@_name_boundary.class_contract('BscSetsid', {})
@meadow_dataclass
class meadow_BscSetsid:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_82a6c63'}, '__str__')
    def __str__(meadow_self_82a6c63):
        return f'setsid(), {meadow_self_82a6c63.result}'

@_name_boundary.class_contract('BscGetpgid', {})
@meadow_dataclass
class meadow_BscGetpgid:
    ktraces: meadow_List
    pid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_74ff377'}, '__str__')
    def __str__(meadow_self_74ff377):
        return f'getpgid({meadow_self_74ff377.pid}), {meadow_self_74ff377.result}'

@_name_boundary.class_contract('BscSetprivexec', {})
@meadow_dataclass
class meadow_BscSetprivexec:
    ktraces: meadow_List
    flag: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8b9a319'}, '__str__')
    def __str__(meadow_self_8b9a319):
        return f'setprivexec({meadow_self_8b9a319.flag}), {meadow_self_8b9a319.result}'

@_name_boundary.class_contract('BscNfssvc', {})
@meadow_dataclass
class meadow_BscNfssvc:
    ktraces: meadow_List
    flags: int
    argstructp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_78035fa'}, '__str__')
    def __str__(meadow_self_78035fa):
        meadow_rep_605f2c5 = f'nfssvc({meadow_self_78035fa.flags}, {hex(meadow_self_78035fa.argstructp)})'
        if meadow_self_78035fa.result:
            meadow_rep_605f2c5 += f', {meadow_self_78035fa.result}'
        return meadow_rep_605f2c5

@_name_boundary.class_contract('BscStatfs', {})
@meadow_dataclass
class meadow_BscStatfs:
    ktraces: meadow_List
    path: str
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_75926d8'}, '__str__')
    def __str__(meadow_self_75926d8):
        meadow_rep_7e26321 = f'statfs("{meadow_self_75926d8.path}", {hex(meadow_self_75926d8.buf)})'
        if meadow_self_75926d8.result:
            meadow_rep_7e26321 += f', {meadow_self_75926d8.result}'
        return meadow_rep_7e26321

@_name_boundary.class_contract('BscFstatfs', {})
@meadow_dataclass
class meadow_BscFstatfs:
    ktraces: meadow_List
    fd: int
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_018a8a0'}, '__str__')
    def __str__(meadow_self_018a8a0):
        meadow_rep_be497c5 = f'fstatfs({meadow_self_018a8a0.fd}, {hex(meadow_self_018a8a0.buf)})'
        if meadow_self_018a8a0.result:
            meadow_rep_be497c5 += f', {meadow_self_018a8a0.result}'
        return meadow_rep_be497c5

@_name_boundary.class_contract('BscUnmount', {})
@meadow_dataclass
class meadow_BscUnmount:
    ktraces: meadow_List
    dir: str
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4fb439c'}, '__str__')
    def __str__(meadow_self_4fb439c):
        meadow_rep_35d3b2b = f'unmount("{meadow_self_4fb439c.dir}", {meadow_self_4fb439c.flags})'
        if meadow_self_4fb439c.result:
            meadow_rep_35d3b2b += f', {meadow_self_4fb439c.result}'
        return meadow_rep_35d3b2b

@_name_boundary.class_contract('BscGetfh', {})
@meadow_dataclass
class meadow_BscGetfh:
    ktraces: meadow_List
    path: str
    fhp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_788ddca'}, '__str__')
    def __str__(meadow_self_788ddca):
        meadow_rep_a9b75b4 = f'getfh("{meadow_self_788ddca.path}", {hex(meadow_self_788ddca.fhp)})'
        if meadow_self_788ddca.result:
            meadow_rep_a9b75b4 += f', {meadow_self_788ddca.result}'
        return meadow_rep_a9b75b4

@_name_boundary.class_contract('BscQuotactl', {})
@meadow_dataclass
class meadow_BscQuotactl:
    ktraces: meadow_List
    path: str
    cmd: int
    id: int
    addr: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9bd0d79'}, '__str__')
    def __str__(meadow_self_9bd0d79):
        meadow_rep_9fef970 = f'quotactl("{meadow_self_9bd0d79.path}", {meadow_self_9bd0d79.cmd}, {meadow_self_9bd0d79.id}, {hex(meadow_self_9bd0d79.addr)})'
        if meadow_self_9bd0d79.result:
            meadow_rep_9fef970 += f', {meadow_self_9bd0d79.result}'
        return meadow_rep_9fef970

@_name_boundary.class_contract('BscMount', {})
@meadow_dataclass
class meadow_BscMount:
    ktraces: meadow_List
    source: str
    dest: str
    flags: int
    data: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f1f7a18'}, '__str__')
    def __str__(meadow_self_f1f7a18):
        meadow_rep_b315eec = f'mount("{meadow_self_f1f7a18.source}", "{meadow_self_f1f7a18.dest}", {meadow_self_f1f7a18.flags}, {hex(meadow_self_f1f7a18.data)})'
        if meadow_self_f1f7a18.result:
            meadow_rep_b315eec += f', {meadow_self_f1f7a18.result}'
        return meadow_rep_b315eec

@_name_boundary.class_contract('BscCsops', {})
@meadow_dataclass
class meadow_BscCsops:
    ktraces: meadow_List
    pid: int
    ops: meadow_CsopsOps
    useraddr: int
    usersize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_de085e9'}, '__str__')
    def __str__(meadow_self_de085e9):
        meadow_rep_0bb96f8 = f"csops({meadow_self_de085e9.pid}, {_name_boundary.attributes(meadow_self_de085e9.ops)['name']}, {hex(meadow_self_de085e9.useraddr)}, {meadow_self_de085e9.usersize})"
        if meadow_self_de085e9.result:
            meadow_rep_0bb96f8 += f', {meadow_self_de085e9.result}'
        return meadow_rep_0bb96f8

@_name_boundary.class_contract('BscCsopsAudittoken', {})
@meadow_dataclass
class meadow_BscCsopsAudittoken:
    ktraces: meadow_List
    pid: int
    ops: meadow_CsopsOps
    useraddr: int
    usersize: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_af5f321'}, '__str__')
    def __str__(meadow_self_af5f321):
        meadow_rep_c673b71 = f"csops_audittoken({meadow_self_af5f321.pid}, {_name_boundary.attributes(meadow_self_af5f321.ops)['name']}, {hex(meadow_self_af5f321.useraddr)}, {meadow_self_af5f321.usersize})"
        if meadow_self_af5f321.result:
            meadow_rep_c673b71 += f', {meadow_self_af5f321.result}'
        return meadow_rep_c673b71

@_name_boundary.class_contract('BscWaitid', {})
@meadow_dataclass
class meadow_BscWaitid:
    ktraces: meadow_List
    idtype: int
    id: int
    infop: int
    options: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_be94413'}, '__str__')
    def __str__(meadow_self_be94413):
        meadow_no_cancel_2064396 = '_nocancel' if meadow_self_be94413.no_cancel else ''
        meadow_rep_6334e49 = f'waitid{meadow_no_cancel_2064396}({meadow_self_be94413.idtype}, {meadow_self_be94413.id}, {hex(meadow_self_be94413.infop)}, {meadow_self_be94413.options})'
        if meadow_self_be94413.result:
            meadow_rep_6334e49 += f', {meadow_self_be94413.result}'
        return meadow_rep_6334e49

@_name_boundary.class_contract('BscKdebugTypefilter', {})
@meadow_dataclass
class meadow_BscKdebugTypefilter:
    ktraces: meadow_List
    addr: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b3217ef'}, '__str__')
    def __str__(meadow_self_b3217ef):
        meadow_rep_51a8084 = f'kdebug_typefilter({hex(meadow_self_b3217ef.addr)}, {hex(meadow_self_b3217ef.size)})'
        if meadow_self_b3217ef.result:
            meadow_rep_51a8084 += f', {meadow_self_b3217ef.result}'
        return meadow_rep_51a8084

@_name_boundary.class_contract('BscSetgid', {})
@meadow_dataclass
class meadow_BscSetgid:
    ktraces: meadow_List
    gid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f217d91'}, '__str__')
    def __str__(meadow_self_f217d91):
        meadow_rep_2437998 = f'setgid({meadow_self_f217d91.gid})'
        if meadow_self_f217d91.result:
            meadow_rep_2437998 += f', {meadow_self_f217d91.result}'
        return meadow_rep_2437998

@_name_boundary.class_contract('BscSetegid', {})
@meadow_dataclass
class meadow_BscSetegid:
    ktraces: meadow_List
    egid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e919f85'}, '__str__')
    def __str__(meadow_self_e919f85):
        meadow_rep_d7ee7c2 = f'setegid({meadow_self_e919f85.egid})'
        if meadow_self_e919f85.result:
            meadow_rep_d7ee7c2 += f', {meadow_self_e919f85.result}'
        return meadow_rep_d7ee7c2

@_name_boundary.class_contract('BscSeteuid', {})
@meadow_dataclass
class meadow_BscSeteuid:
    ktraces: meadow_List
    euid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_c6fa0c9'}, '__str__')
    def __str__(meadow_self_c6fa0c9):
        meadow_rep_d7ff4b5 = f'seteuid({meadow_self_c6fa0c9.euid})'
        if meadow_self_c6fa0c9.result:
            meadow_rep_d7ff4b5 += f', {meadow_self_c6fa0c9.result}'
        return meadow_rep_d7ff4b5

@_name_boundary.class_contract('BscThreadSelfcounts', {})
@meadow_dataclass
class meadow_BscThreadSelfcounts:
    ktraces: meadow_List
    type: int
    buf: int
    nbytes: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_16c2c08'}, '__str__')
    def __str__(meadow_self_16c2c08):
        meadow_rep_97b068d = f'thread_selfcounts({meadow_self_16c2c08.type}, {hex(meadow_self_16c2c08.buf)}, {meadow_self_16c2c08.nbytes})'
        if meadow_self_16c2c08.result:
            meadow_rep_97b068d += f', {meadow_self_16c2c08.result}'
        return meadow_rep_97b068d

@_name_boundary.class_contract('BscFdatasync', {})
@meadow_dataclass
class meadow_BscFdatasync:
    ktraces: meadow_List
    fd: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_eac0f0c'}, '__str__')
    def __str__(meadow_self_eac0f0c):
        meadow_rep_f0d7101 = f'fdatasync({meadow_self_eac0f0c.fd})'
        if meadow_self_eac0f0c.result:
            meadow_rep_f0d7101 += f', {meadow_self_eac0f0c.result}'
        return meadow_rep_f0d7101

@_name_boundary.class_contract('BscPathconf', {})
@meadow_dataclass
class meadow_BscPathconf:
    ktraces: meadow_List
    path: str
    name: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a87cbcd'}, '__str__')
    def __str__(meadow_self_a87cbcd):
        return f'''pathconf("{meadow_self_a87cbcd.path}", {_name_boundary.attributes(meadow_self_a87cbcd)['name']}), {meadow_self_a87cbcd.result}'''

@_name_boundary.class_contract('BscSysFpathconf', {})
@meadow_dataclass
class meadow_BscSysFpathconf:
    ktraces: meadow_List
    fildes: int
    name: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_04cb882'}, '__str__')
    def __str__(meadow_self_04cb882):
        return f"fpathconf({meadow_self_04cb882.fildes}, {_name_boundary.attributes(meadow_self_04cb882)['name']}), {meadow_self_04cb882.result}"

@_name_boundary.class_contract('BscGetrlimit', {})
@meadow_dataclass
class meadow_BscGetrlimit:
    ktraces: meadow_List
    resource: int
    rlp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_19d2fc3'}, '__str__')
    def __str__(meadow_self_19d2fc3):
        meadow_rep_7688e59 = f'getrlimit({meadow_self_19d2fc3.resource}, {hex(meadow_self_19d2fc3.rlp)})'
        if meadow_self_19d2fc3.result:
            meadow_rep_7688e59 += f', {meadow_self_19d2fc3.result}'
        return meadow_rep_7688e59

@_name_boundary.class_contract('BscSetrlimit', {})
@meadow_dataclass
class meadow_BscSetrlimit:
    ktraces: meadow_List
    resource: int
    rlp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_beb3e5e'}, '__str__')
    def __str__(meadow_self_beb3e5e):
        meadow_rep_8d579fc = f'setrlimit({meadow_self_beb3e5e.resource}, {hex(meadow_self_beb3e5e.rlp)})'
        if meadow_self_beb3e5e.result:
            meadow_rep_8d579fc += f', {meadow_self_beb3e5e.result}'
        return meadow_rep_8d579fc

@_name_boundary.class_contract('BscGetdirentries', {})
@meadow_dataclass
class meadow_BscGetdirentries:
    ktraces: meadow_List
    fd: int
    buf: int
    nbytes: int
    basep: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6587d6e'}, '__str__')
    def __str__(meadow_self_6587d6e):
        return f'getdirentries({meadow_self_6587d6e.fd}, {hex(meadow_self_6587d6e.buf)}, {meadow_self_6587d6e.nbytes}, {hex(meadow_self_6587d6e.basep)}), {meadow_self_6587d6e.result}'

@_name_boundary.class_contract('BscMmap', {})
@meadow_dataclass
class meadow_BscMmap:
    ktraces: meadow_List
    addr: int
    len: int
    prot: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_deeae5a'}, '__str__')
    def __str__(meadow_self_deeae5a):
        return f'mmap({hex(meadow_self_deeae5a.addr)}, {meadow_self_deeae5a.len}, {meadow_self_deeae5a.prot}, {meadow_self_deeae5a.flags}), {meadow_self_deeae5a.result}'

@_name_boundary.class_contract('BscLseek', {})
@meadow_dataclass
class meadow_BscLseek:
    ktraces: meadow_List
    fildes: int
    offset: int
    whence: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_74e5cad'}, '__str__')
    def __str__(meadow_self_74e5cad):
        return f'lseek({meadow_self_74e5cad.fildes}, {meadow_self_74e5cad.offset}, {meadow_self_74e5cad.whence}), {meadow_self_74e5cad.result}'

@_name_boundary.class_contract('BscTruncate', {})
@meadow_dataclass
class meadow_BscTruncate:
    ktraces: meadow_List
    path: str
    length: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b89de44'}, '__str__')
    def __str__(meadow_self_b89de44):
        meadow_rep_44dd168 = f'truncate("{meadow_self_b89de44.path}", {meadow_self_b89de44.length})'
        if meadow_self_b89de44.result:
            meadow_rep_44dd168 += f', {meadow_self_b89de44.result}'
        return meadow_rep_44dd168

@_name_boundary.class_contract('BscFtruncate', {})
@meadow_dataclass
class meadow_BscFtruncate:
    ktraces: meadow_List
    fildes: int
    length: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4d97988'}, '__str__')
    def __str__(meadow_self_4d97988):
        meadow_rep_ec09e6e = f'ftruncate({meadow_self_4d97988.fildes}, {meadow_self_4d97988.length})'
        if meadow_self_4d97988.result:
            meadow_rep_ec09e6e += f', {meadow_self_4d97988.result}'
        return meadow_rep_ec09e6e

@_name_boundary.class_contract('BscSysctl', {})
@meadow_dataclass
class meadow_BscSysctl:
    ktraces: meadow_List
    name: int
    namelen: int
    oldp: int
    oldlenp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6a32397'}, '__str__')
    def __str__(meadow_self_6a32397):
        meadow_rep_86c8bcb = f"sysctl({hex(_name_boundary.attributes(meadow_self_6a32397)['name'])}, {meadow_self_6a32397.namelen}, {hex(meadow_self_6a32397.oldp)}, {hex(meadow_self_6a32397.oldlenp)})"
        if meadow_self_6a32397.result:
            meadow_rep_86c8bcb += f', {meadow_self_6a32397.result}'
        return meadow_rep_86c8bcb

@_name_boundary.class_contract('BscMlock', {})
@meadow_dataclass
class meadow_BscMlock:
    ktraces: meadow_List
    addr: int
    len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fb8222b'}, '__str__')
    def __str__(meadow_self_fb8222b):
        meadow_rep_cd8f86d = f'mlock({hex(meadow_self_fb8222b.addr)}, {meadow_self_fb8222b.len})'
        if meadow_self_fb8222b.result:
            meadow_rep_cd8f86d += f', {meadow_self_fb8222b.result}'
        return meadow_rep_cd8f86d

@_name_boundary.class_contract('BscMunlock', {})
@meadow_dataclass
class meadow_BscMunlock:
    ktraces: meadow_List
    addr: int
    len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fd87342'}, '__str__')
    def __str__(meadow_self_fd87342):
        meadow_rep_f56063a = f'munlock({hex(meadow_self_fd87342.addr)}, {meadow_self_fd87342.len})'
        if meadow_self_fd87342.result:
            meadow_rep_f56063a += f', {meadow_self_fd87342.result}'
        return meadow_rep_f56063a

@_name_boundary.class_contract('BscUndelete', {})
@meadow_dataclass
class meadow_BscUndelete:
    ktraces: meadow_List
    path: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d25acb8'}, '__str__')
    def __str__(meadow_self_d25acb8):
        meadow_rep_ec65fa8 = f'undelete("{meadow_self_d25acb8.path}")'
        if meadow_self_d25acb8.result:
            meadow_rep_ec65fa8 += f', {meadow_self_d25acb8.result}'
        return meadow_rep_ec65fa8

@_name_boundary.class_contract('BscOpenDprotectedNp', {})
@meadow_dataclass
class meadow_BscOpenDprotectedNp:
    ktraces: meadow_List
    path: str
    flags: meadow_List
    class_: str
    dpflags: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_09df6e7'}, '__str__')
    def __str__(meadow_self_09df6e7):
        meadow_flags_d53d3c9 = ' | '.join(map(lambda meadow_f_7deee25: _name_boundary.attributes(meadow_f_7deee25)['name'], meadow_self_09df6e7.flags))
        return f'open_dprotected_np("{meadow_self_09df6e7.path}", {meadow_flags_d53d3c9}, {meadow_self_09df6e7.class_}, {meadow_self_09df6e7.dpflags}), {meadow_self_09df6e7.result}'

@_name_boundary.class_contract('BscGetattrlist', {})
@meadow_dataclass
class meadow_BscGetattrlist:
    ktraces: meadow_List
    path: str
    attr_list: int
    attr_buf: int
    attr_buf_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4face89'}, '__str__')
    def __str__(meadow_self_4face89):
        meadow_rep_74c0afb = f'getattrlist("{meadow_self_4face89.path}", {hex(meadow_self_4face89.attr_list)}, {hex(meadow_self_4face89.attr_buf)}, {meadow_self_4face89.attr_buf_size})'
        if meadow_self_4face89.result:
            meadow_rep_74c0afb += f', {meadow_self_4face89.result}'
        return meadow_rep_74c0afb

@_name_boundary.class_contract('BscSetattrlist', {})
@meadow_dataclass
class meadow_BscSetattrlist:
    ktraces: meadow_List
    path: str
    attr_list: int
    attr_buf: int
    attr_buf_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9cb7055'}, '__str__')
    def __str__(meadow_self_9cb7055):
        meadow_rep_597263c = f'setattrlist("{meadow_self_9cb7055.path}", {hex(meadow_self_9cb7055.attr_list)}, {hex(meadow_self_9cb7055.attr_buf)}, {meadow_self_9cb7055.attr_buf_size})'
        if meadow_self_9cb7055.result:
            meadow_rep_597263c += f', {meadow_self_9cb7055.result}'
        return meadow_rep_597263c

@_name_boundary.class_contract('BscGetdirentriesattr', {})
@meadow_dataclass
class meadow_BscGetdirentriesattr:
    ktraces: meadow_List
    fd: str
    attr_list: int
    attr_buf: int
    attr_buf_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8736380'}, '__str__')
    def __str__(meadow_self_8736380):
        return f'getdirentriesattr({meadow_self_8736380.fd}, {hex(meadow_self_8736380.attr_list)}, {hex(meadow_self_8736380.attr_buf)}, {meadow_self_8736380.attr_buf_size}), {meadow_self_8736380.result}'

@_name_boundary.class_contract('BscExchangedata', {})
@meadow_dataclass
class meadow_BscExchangedata:
    ktraces: meadow_List
    path1: str
    path2: str
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d5eb9f0'}, '__str__')
    def __str__(meadow_self_d5eb9f0):
        meadow_rep_c152d60 = f'exchangedata("{meadow_self_d5eb9f0.path1}", "{meadow_self_d5eb9f0.path2}", {meadow_self_d5eb9f0.options})'
        if meadow_self_d5eb9f0.result:
            meadow_rep_c152d60 += f', {meadow_self_d5eb9f0.result}'
        return meadow_rep_c152d60

@_name_boundary.class_contract('BscSearchfs', {})
@meadow_dataclass
class meadow_BscSearchfs:
    ktraces: meadow_List
    path: str
    search_block: int
    num_matches: int
    script_code: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_da60975'}, '__str__')
    def __str__(meadow_self_da60975):
        meadow_rep_0197bc4 = f'searchfs("{meadow_self_da60975.path}", {hex(meadow_self_da60975.search_block)}, {hex(meadow_self_da60975.num_matches)}, {meadow_self_da60975.script_code})'
        if meadow_self_da60975.result:
            meadow_rep_0197bc4 += f', {meadow_self_da60975.result}'
        return meadow_rep_0197bc4

@_name_boundary.class_contract('BscFgetattrlist', {})
@meadow_dataclass
class meadow_BscFgetattrlist:
    ktraces: meadow_List
    fd: int
    attr_list: int
    attr_buf: int
    attr_buf_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_37f3985'}, '__str__')
    def __str__(meadow_self_37f3985):
        meadow_rep_976a218 = f'fgetattrlist({meadow_self_37f3985.fd}, {hex(meadow_self_37f3985.attr_list)}, {hex(meadow_self_37f3985.attr_buf)}, {meadow_self_37f3985.attr_buf_size})'
        if meadow_self_37f3985.result:
            meadow_rep_976a218 += f', {meadow_self_37f3985.result}'
        return meadow_rep_976a218

@_name_boundary.class_contract('BscFsetattrlist', {})
@meadow_dataclass
class meadow_BscFsetattrlist:
    ktraces: meadow_List
    fd: int
    attr_list: int
    attr_buf: int
    attr_buf_size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_569a9c6'}, '__str__')
    def __str__(meadow_self_569a9c6):
        meadow_rep_278ecfc = f'fsetattrlist({meadow_self_569a9c6.fd}, {hex(meadow_self_569a9c6.attr_list)}, {hex(meadow_self_569a9c6.attr_buf)}, {meadow_self_569a9c6.attr_buf_size})'
        if meadow_self_569a9c6.result:
            meadow_rep_278ecfc += f', {meadow_self_569a9c6.result}'
        return meadow_rep_278ecfc

@_name_boundary.class_contract('BscPoll', {})
@meadow_dataclass
class meadow_BscPoll:
    ktraces: meadow_List
    fds: int
    nfds: int
    timeout: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_60dd29a'}, '__str__')
    def __str__(meadow_self_60dd29a):
        meadow_no_cancel_310b852 = '_nocancel' if meadow_self_60dd29a.no_cancel else ''
        return f'poll{meadow_no_cancel_310b852}({hex(meadow_self_60dd29a.fds)}, {meadow_self_60dd29a.nfds}, {meadow_self_60dd29a.timeout}), {meadow_self_60dd29a.result}'

@_name_boundary.class_contract('BscGetxattr', {})
@meadow_dataclass
class meadow_BscGetxattr:
    ktraces: meadow_List
    path: str
    name: int
    value: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_244aa00'}, '__str__')
    def __str__(meadow_self_244aa00):
        return f'''getxattr("{meadow_self_244aa00.path}", {hex(_name_boundary.attributes(meadow_self_244aa00)['name'])}, {hex(meadow_self_244aa00.value)}, {meadow_self_244aa00.size}), {meadow_self_244aa00.result}'''

@_name_boundary.class_contract('BscFgetxattr', {})
@meadow_dataclass
class meadow_BscFgetxattr:
    ktraces: meadow_List
    fd: int
    name: int
    value: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_acb0e13'}, '__str__')
    def __str__(meadow_self_acb0e13):
        return f"fgetxattr({meadow_self_acb0e13.fd}, {hex(_name_boundary.attributes(meadow_self_acb0e13)['name'])}, {hex(meadow_self_acb0e13.value)}, {meadow_self_acb0e13.size}), {meadow_self_acb0e13.result}"

@_name_boundary.class_contract('BscSetxattr', {})
@meadow_dataclass
class meadow_BscSetxattr:
    ktraces: meadow_List
    path: str
    name: int
    value: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_48d2f13'}, '__str__')
    def __str__(meadow_self_48d2f13):
        meadow_rep_0ce019b = f'''setxattr("{meadow_self_48d2f13.path}", {hex(_name_boundary.attributes(meadow_self_48d2f13)['name'])}, {hex(meadow_self_48d2f13.value)}, {meadow_self_48d2f13.size})'''
        if meadow_self_48d2f13.result:
            meadow_rep_0ce019b += f', {meadow_self_48d2f13.result}'
        return meadow_rep_0ce019b

@_name_boundary.class_contract('BscFsetxattr', {})
@meadow_dataclass
class meadow_BscFsetxattr:
    ktraces: meadow_List
    fd: int
    name: int
    value: int
    size: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_74628ca'}, '__str__')
    def __str__(meadow_self_74628ca):
        meadow_rep_5479f33 = f"fsetxattr({meadow_self_74628ca.fd}, {hex(_name_boundary.attributes(meadow_self_74628ca)['name'])}, {hex(meadow_self_74628ca.value)}, {meadow_self_74628ca.size})"
        if meadow_self_74628ca.result:
            meadow_rep_5479f33 += f', {meadow_self_74628ca.result}'
        return meadow_rep_5479f33

@_name_boundary.class_contract('BscRemovexattr', {})
@meadow_dataclass
class meadow_BscRemovexattr:
    ktraces: meadow_List
    path: str
    name: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0a96065'}, '__str__')
    def __str__(meadow_self_0a96065):
        meadow_rep_1ad7096 = f'''removexattr("{meadow_self_0a96065.path}", {hex(_name_boundary.attributes(meadow_self_0a96065)['name'])}, {meadow_self_0a96065.options})'''
        if meadow_self_0a96065.result:
            meadow_rep_1ad7096 += f', {meadow_self_0a96065.result}'
        return meadow_rep_1ad7096

@_name_boundary.class_contract('BscFremovexattr', {})
@meadow_dataclass
class meadow_BscFremovexattr:
    ktraces: meadow_List
    fd: int
    name: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_bb12baf'}, '__str__')
    def __str__(meadow_self_bb12baf):
        meadow_rep_238bc09 = f"fremovexattr({meadow_self_bb12baf.fd}, {hex(_name_boundary.attributes(meadow_self_bb12baf)['name'])}, {meadow_self_bb12baf.options})"
        if meadow_self_bb12baf.result:
            meadow_rep_238bc09 += f', {meadow_self_bb12baf.result}'
        return meadow_rep_238bc09

@_name_boundary.class_contract('BscListxattr', {})
@meadow_dataclass
class meadow_BscListxattr:
    ktraces: meadow_List
    path: str
    namebuf: int
    size: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e91ce54'}, '__str__')
    def __str__(meadow_self_e91ce54):
        return f'listxattr("{meadow_self_e91ce54.path}", {hex(meadow_self_e91ce54.namebuf)}, {meadow_self_e91ce54.size}, {meadow_self_e91ce54.options}), {meadow_self_e91ce54.result}'

@_name_boundary.class_contract('BscFlistxattr', {})
@meadow_dataclass
class meadow_BscFlistxattr:
    ktraces: meadow_List
    fd: int
    namebuf: int
    size: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b096a6b'}, '__str__')
    def __str__(meadow_self_b096a6b):
        return f'flistxattr({meadow_self_b096a6b.fd}, {hex(meadow_self_b096a6b.namebuf)}, {meadow_self_b096a6b.size}, {meadow_self_b096a6b.options}), {meadow_self_b096a6b.result}'

@_name_boundary.class_contract('BscFsctl', {})
@meadow_dataclass
class meadow_BscFsctl:
    ktraces: meadow_List
    path: str
    request: int
    data: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9a17c09'}, '__str__')
    def __str__(meadow_self_9a17c09):
        meadow_rep_3559e04 = f'fsctl("{meadow_self_9a17c09.path}", {meadow_self_9a17c09.request}, {hex(meadow_self_9a17c09.data)}, {meadow_self_9a17c09.options})'
        if meadow_self_9a17c09.result:
            meadow_rep_3559e04 += f', {meadow_self_9a17c09.result}'
        return meadow_rep_3559e04

@_name_boundary.class_contract('BscInitgroups', {})
@meadow_dataclass
class meadow_BscInitgroups:
    ktraces: meadow_List
    name: int
    basegid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8485383'}, '__str__')
    def __str__(meadow_self_8485383):
        meadow_rep_dc8e998 = f"initgroups({hex(_name_boundary.attributes(meadow_self_8485383)['name'])}, {meadow_self_8485383.basegid})"
        if meadow_self_8485383.result:
            meadow_rep_dc8e998 += f', {meadow_self_8485383.result}'
        return meadow_rep_dc8e998

@_name_boundary.class_contract('BscPosixSpawn', {})
@meadow_dataclass
class meadow_BscPosixSpawn:
    ktraces: meadow_List
    pid: int
    path: str
    file_actions: int
    attrp: int
    stdin: str
    stdout: str
    stderr: str
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_5a63102'}, '__str__')
    def __str__(meadow_self_5a63102):
        meadow_rep_7cf4289 = f'posix_spawn({hex(meadow_self_5a63102.pid)}, "{meadow_self_5a63102.path}", {hex(meadow_self_5a63102.file_actions)}, {hex(meadow_self_5a63102.attrp)})'
        if meadow_self_5a63102.result:
            meadow_rep_7cf4289 += f', {meadow_self_5a63102.result}'
        return meadow_rep_7cf4289

@_name_boundary.class_contract('BscFfsctl', {})
@meadow_dataclass
class meadow_BscFfsctl:
    ktraces: meadow_List
    fd: int
    request: int
    data: int
    options: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6a582bd'}, '__str__')
    def __str__(meadow_self_6a582bd):
        meadow_rep_ef429de = f'ffsctl({meadow_self_6a582bd.fd}, {meadow_self_6a582bd.request}, {hex(meadow_self_6a582bd.data)}, {meadow_self_6a582bd.options})'
        if meadow_self_6a582bd.result:
            meadow_rep_ef429de += f', {meadow_self_6a582bd.result}'
        return meadow_rep_ef429de

@_name_boundary.class_contract('BscNfsclnt', {})
@meadow_dataclass
class meadow_BscNfsclnt:
    ktraces: meadow_List
    flags: int
    argstructp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7b5095d'}, '__str__')
    def __str__(meadow_self_7b5095d):
        meadow_rep_3e051a2 = f'nfsclnt({meadow_self_7b5095d.flags}, {hex(meadow_self_7b5095d.argstructp)})'
        if meadow_self_7b5095d.result:
            meadow_rep_3e051a2 += f', {meadow_self_7b5095d.result}'
        return meadow_rep_3e051a2

@_name_boundary.class_contract('BscFhopen', {})
@meadow_dataclass
class meadow_BscFhopen:
    ktraces: meadow_List
    fhp: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f17b3fe'}, '__str__')
    def __str__(meadow_self_f17b3fe):
        meadow_rep_02fdcef = f'fhopen({hex(meadow_self_f17b3fe.fhp)}, {meadow_self_f17b3fe.flags})'
        if meadow_self_f17b3fe.result:
            meadow_rep_02fdcef += f', {meadow_self_f17b3fe.result}'
        return meadow_rep_02fdcef

@_name_boundary.class_contract('BscMinherit', {})
@meadow_dataclass
class meadow_BscMinherit:
    ktraces: meadow_List
    addr: int
    len: int
    inherit: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0ef29bf'}, '__str__')
    def __str__(meadow_self_0ef29bf):
        meadow_rep_6c17bcf = f'minherit({hex(meadow_self_0ef29bf.addr)}, {meadow_self_0ef29bf.len}, {meadow_self_0ef29bf.inherit})'
        if meadow_self_0ef29bf.result:
            meadow_rep_6c17bcf += f', {meadow_self_0ef29bf.result}'
        return meadow_rep_6c17bcf

@_name_boundary.class_contract('BscSemsys', {})
@meadow_dataclass
class meadow_BscSemsys:
    ktraces: meadow_List
    which: int
    a2: int
    a3: int
    a4: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_7faaca7'}, '__str__')
    def __str__(meadow_self_7faaca7):
        meadow_rep_06c5d52 = f'semsys({meadow_self_7faaca7.which}, {meadow_self_7faaca7.a2}, {meadow_self_7faaca7.a3}, {meadow_self_7faaca7.a4})'
        if meadow_self_7faaca7.result:
            meadow_rep_06c5d52 += f', {meadow_self_7faaca7.result}'
        return meadow_rep_06c5d52

@_name_boundary.class_contract('BscMsgsys', {})
@meadow_dataclass
class meadow_BscMsgsys:
    ktraces: meadow_List
    which: int
    a2: int
    a3: int
    a4: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2b2248b'}, '__str__')
    def __str__(meadow_self_2b2248b):
        meadow_rep_b301100 = f'msgsys({meadow_self_2b2248b.which}, {meadow_self_2b2248b.a2}, {meadow_self_2b2248b.a3}, {meadow_self_2b2248b.a4})'
        if meadow_self_2b2248b.result:
            meadow_rep_b301100 += f', {meadow_self_2b2248b.result}'
        return meadow_rep_b301100

@_name_boundary.class_contract('BscShmsys', {})
@meadow_dataclass
class meadow_BscShmsys:
    ktraces: meadow_List
    which: int
    a2: int
    a3: int
    a4: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_d43dfa6'}, '__str__')
    def __str__(meadow_self_d43dfa6):
        meadow_rep_747a2ba = f'shmsys({meadow_self_d43dfa6.which}, {meadow_self_d43dfa6.a2}, {meadow_self_d43dfa6.a3}, {meadow_self_d43dfa6.a4})'
        if meadow_self_d43dfa6.result:
            meadow_rep_747a2ba += f', {meadow_self_d43dfa6.result}'
        return meadow_rep_747a2ba

@_name_boundary.class_contract('BscSemctl', {})
@meadow_dataclass
class meadow_BscSemctl:
    ktraces: meadow_List
    semid: int
    semnum: int
    cmd: int
    semun: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8926242'}, '__str__')
    def __str__(meadow_self_8926242):
        return f'semctl({meadow_self_8926242.semid}, {meadow_self_8926242.semnum}, {meadow_self_8926242.cmd}, {hex(meadow_self_8926242.semun)}), {meadow_self_8926242.result}'

@_name_boundary.class_contract('BscSemget', {})
@meadow_dataclass
class meadow_BscSemget:
    ktraces: meadow_List
    key: int
    nsems: int
    semflg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e7d0ebf'}, '__str__')
    def __str__(meadow_self_e7d0ebf):
        return f'semget({meadow_self_e7d0ebf.key}, {meadow_self_e7d0ebf.nsems}, {meadow_self_e7d0ebf.semflg}), {meadow_self_e7d0ebf.result}'

@_name_boundary.class_contract('BscSemop', {})
@meadow_dataclass
class meadow_BscSemop:
    ktraces: meadow_List
    semid: int
    sops: int
    nsops: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_81c73cb'}, '__str__')
    def __str__(meadow_self_81c73cb):
        meadow_rep_e683b9c = f'semop({meadow_self_81c73cb.semid}, {hex(meadow_self_81c73cb.sops)}, {meadow_self_81c73cb.nsops})'
        if meadow_self_81c73cb.result:
            meadow_rep_e683b9c += f', {meadow_self_81c73cb.result}'
        return meadow_rep_e683b9c

@_name_boundary.class_contract('BscMsgctl', {})
@meadow_dataclass
class meadow_BscMsgctl:
    ktraces: meadow_List
    msqid: int
    cmd: int
    ds: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_1b9400d'}, '__str__')
    def __str__(meadow_self_1b9400d):
        return f'msgctl({meadow_self_1b9400d.msqid}, {meadow_self_1b9400d.cmd}, {meadow_self_1b9400d.ds}), {meadow_self_1b9400d.result}'

@_name_boundary.class_contract('BscMsgget', {})
@meadow_dataclass
class meadow_BscMsgget:
    ktraces: meadow_List
    key: int
    msgflg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e25b21c'}, '__str__')
    def __str__(meadow_self_e25b21c):
        return f'msgget({meadow_self_e25b21c.key}, {meadow_self_e25b21c.msgflg}), {meadow_self_e25b21c.result}'

@_name_boundary.class_contract('BscMsgsnd', {})
@meadow_dataclass
class meadow_BscMsgsnd:
    ktraces: meadow_List
    msqid: int
    msgp: int
    msgsz: int
    msgflg: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_ea06c09'}, '__str__')
    def __str__(meadow_self_ea06c09):
        meadow_no_cancel_0e6eac9 = '_nocancel' if meadow_self_ea06c09.no_cancel else ''
        return f'msgsnd{meadow_no_cancel_0e6eac9}({meadow_self_ea06c09.msqid}, {hex(meadow_self_ea06c09.msgp)}, {meadow_self_ea06c09.msgsz}, {meadow_self_ea06c09.msgflg}), {meadow_self_ea06c09.result}'

@_name_boundary.class_contract('BscMsgrcv', {})
@meadow_dataclass
class meadow_BscMsgrcv:
    ktraces: meadow_List
    msqid: int
    msgp: int
    msgsz: int
    msgtyp: int
    result: str
    no_cancel: bool

    @_name_boundary.callable_contract({'self': 'meadow_self_5064aad'}, '__str__')
    def __str__(meadow_self_5064aad):
        meadow_no_cancel_3f27666 = '_nocancel' if meadow_self_5064aad.no_cancel else ''
        return f'msgrcv{meadow_no_cancel_3f27666}({meadow_self_5064aad.msqid}, {hex(meadow_self_5064aad.msgp)}, {meadow_self_5064aad.msgsz}, {meadow_self_5064aad.msgtyp}), {meadow_self_5064aad.result}'

@_name_boundary.class_contract('BscShmat', {})
@meadow_dataclass
class meadow_BscShmat:
    ktraces: meadow_List
    shmid: int
    shmaddr: int
    shmflg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a287e42'}, '__str__')
    def __str__(meadow_self_a287e42):
        return f'shmat({meadow_self_a287e42.shmid}, {hex(meadow_self_a287e42.shmaddr)}, {meadow_self_a287e42.shmflg}), {meadow_self_a287e42.result}'

@_name_boundary.class_contract('BscShmctl', {})
@meadow_dataclass
class meadow_BscShmctl:
    ktraces: meadow_List
    shmid: int
    cmd: int
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_af34ab7'}, '__str__')
    def __str__(meadow_self_af34ab7):
        meadow_rep_ccaf0c6 = f'shmctl({meadow_self_af34ab7.shmid}, {meadow_self_af34ab7.cmd}, {hex(meadow_self_af34ab7.buf)})'
        if meadow_self_af34ab7.result:
            meadow_rep_ccaf0c6 += f', {meadow_self_af34ab7.result}'
        return meadow_rep_ccaf0c6

@_name_boundary.class_contract('BscShmdt', {})
@meadow_dataclass
class meadow_BscShmdt:
    ktraces: meadow_List
    shmaddr: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_87715e2'}, '__str__')
    def __str__(meadow_self_87715e2):
        meadow_rep_314953c = f'shmdt({hex(meadow_self_87715e2.shmaddr)})'
        if meadow_self_87715e2.result:
            meadow_rep_314953c += f', {meadow_self_87715e2.result}'
        return meadow_rep_314953c

@_name_boundary.class_contract('BscShmget', {})
@meadow_dataclass
class meadow_BscShmget:
    ktraces: meadow_List
    key: int
    size: int
    shmflg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b88a751'}, '__str__')
    def __str__(meadow_self_b88a751):
        return f'shmget({meadow_self_b88a751.key}, {meadow_self_b88a751.size}, {meadow_self_b88a751.shmflg}), {meadow_self_b88a751.result}'

@_name_boundary.class_contract('BscShmOpen', {})
@meadow_dataclass
class meadow_BscShmOpen:
    ktraces: meadow_List
    name: int
    oflag: meadow_List
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_6ab1135'}, '__str__')
    def __str__(meadow_self_6ab1135):
        meadow_oflags_6eb5725 = ' | '.join(map(lambda meadow_f_d6202fc: _name_boundary.attributes(meadow_f_d6202fc)['name'], meadow_self_6ab1135.oflag))
        meadow_mode_74a2168 = ', ' + ' | '.join(map(lambda meadow_f_a1e0df9: _name_boundary.attributes(meadow_f_a1e0df9)['name'], meadow_self_6ab1135.mode)) if meadow_BscOpenFlags.O_CREAT in meadow_self_6ab1135.oflag else ''
        return f"shm_open({hex(_name_boundary.attributes(meadow_self_6ab1135)['name'])}, {meadow_oflags_6eb5725}{meadow_mode_74a2168}), {meadow_self_6ab1135.result}"

@_name_boundary.class_contract('BscShmUnlink', {})
@meadow_dataclass
class meadow_BscShmUnlink:
    ktraces: meadow_List
    name: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e0847d0'}, '__str__')
    def __str__(meadow_self_e0847d0):
        meadow_rep_5a0e610 = f"shm_unlink({hex(_name_boundary.attributes(meadow_self_e0847d0)['name'])})"
        if meadow_self_e0847d0.result:
            meadow_rep_5a0e610 += f', {meadow_self_e0847d0.result}'
        return meadow_rep_5a0e610

@_name_boundary.class_contract('BscSemOpen', {})
@meadow_dataclass
class meadow_BscSemOpen:
    ktraces: meadow_List
    name: int
    oflag: meadow_List
    mode: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_2231f22'}, '__str__')
    def __str__(meadow_self_2231f22):
        meadow_oflags_493a956 = ' | '.join(map(lambda meadow_f_272d29d: _name_boundary.attributes(meadow_f_272d29d)['name'], meadow_self_2231f22.oflag))
        meadow_mode_2f0be8d = ', ' + ' | '.join(map(lambda meadow_f_0d94e97: _name_boundary.attributes(meadow_f_0d94e97)['name'], meadow_self_2231f22.mode)) if meadow_BscOpenFlags.O_CREAT in meadow_self_2231f22.oflag else ''
        return f"sem_open({hex(_name_boundary.attributes(meadow_self_2231f22)['name'])}, {meadow_oflags_493a956}{meadow_mode_2f0be8d}), {meadow_self_2231f22.result}"

@_name_boundary.class_contract('BscSemClose', {})
@meadow_dataclass
class meadow_BscSemClose:
    ktraces: meadow_List
    sem: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cf87356'}, '__str__')
    def __str__(meadow_self_cf87356):
        meadow_rep_3a2daa4 = f'sem_close({meadow_self_cf87356.sem})'
        if meadow_self_cf87356.result:
            meadow_rep_3a2daa4 += f', {meadow_self_cf87356.result}'
        return meadow_rep_3a2daa4

@_name_boundary.class_contract('BscSemUnlink', {})
@meadow_dataclass
class meadow_BscSemUnlink:
    ktraces: meadow_List
    name: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_02df6ee'}, '__str__')
    def __str__(meadow_self_02df6ee):
        meadow_rep_04f3538 = f"sem_unlink({hex(_name_boundary.attributes(meadow_self_02df6ee)['name'])})"
        if meadow_self_02df6ee.result:
            meadow_rep_04f3538 += f', {meadow_self_02df6ee.result}'
        return meadow_rep_04f3538

@_name_boundary.class_contract('BscSemWait', {})
@meadow_dataclass
class meadow_BscSemWait:
    ktraces: meadow_List
    sem: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_069ca98'}, '__str__')
    def __str__(meadow_self_069ca98):
        meadow_no_cancel_11e794f = '_nocancel' if meadow_self_069ca98.no_cancel else ''
        meadow_rep_1e0a0ca = f'sem_wait{meadow_no_cancel_11e794f}({hex(meadow_self_069ca98.sem)})'
        if meadow_self_069ca98.result:
            meadow_rep_1e0a0ca += f', {meadow_self_069ca98.result}'
        return meadow_rep_1e0a0ca

@_name_boundary.class_contract('BscSemTrywait', {})
@meadow_dataclass
class meadow_BscSemTrywait:
    ktraces: meadow_List
    sem: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b4643e6'}, '__str__')
    def __str__(meadow_self_b4643e6):
        meadow_rep_56a5005 = f'sem_trywait({hex(meadow_self_b4643e6.sem)})'
        if meadow_self_b4643e6.result:
            meadow_rep_56a5005 += f', {meadow_self_b4643e6.result}'
        return meadow_rep_56a5005

@_name_boundary.class_contract('BscSemPost', {})
@meadow_dataclass
class meadow_BscSemPost:
    ktraces: meadow_List
    sem: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_26927b4'}, '__str__')
    def __str__(meadow_self_26927b4):
        meadow_rep_54ead69 = f'sem_post({hex(meadow_self_26927b4.sem)})'
        if meadow_self_26927b4.result:
            meadow_rep_54ead69 += f', {meadow_self_26927b4.result}'
        return meadow_rep_54ead69

@_name_boundary.class_contract('BscSysctlbyname', {})
@meadow_dataclass
class meadow_BscSysctlbyname:
    ktraces: meadow_List
    name: int
    oldp: int
    oldlenp: int
    newp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a0d0408'}, '__str__')
    def __str__(meadow_self_a0d0408):
        meadow_rep_88f52c0 = f"sysctlbyname({hex(_name_boundary.attributes(meadow_self_a0d0408)['name'])}, {hex(meadow_self_a0d0408.oldp)}, {hex(meadow_self_a0d0408.oldlenp)}, {hex(meadow_self_a0d0408.newp)})"
        if meadow_self_a0d0408.result:
            meadow_rep_88f52c0 += f', {meadow_self_a0d0408.result}'
        return meadow_rep_88f52c0

@_name_boundary.class_contract('BscAccessExtended', {})
@meadow_dataclass
class meadow_BscAccessExtended:
    ktraces: meadow_List
    entries: int
    size: int
    results: int
    uid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e7af299'}, '__str__')
    def __str__(meadow_self_e7af299):
        meadow_rep_1eedf9c = f'access_extended({hex(meadow_self_e7af299.entries)}, {meadow_self_e7af299.size}, {hex(meadow_self_e7af299.results)}, {meadow_self_e7af299.uid})'
        if meadow_self_e7af299.result:
            meadow_rep_1eedf9c += f', {meadow_self_e7af299.result}'
        return meadow_rep_1eedf9c

@_name_boundary.class_contract('BscGettid', {})
@meadow_dataclass
class meadow_BscGettid:
    ktraces: meadow_List
    uidp: int
    gidp: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_e5f59bd'}, '__str__')
    def __str__(meadow_self_e5f59bd):
        meadow_rep_e3f4f34 = f'gettid({hex(meadow_self_e5f59bd.uidp)}, {hex(meadow_self_e5f59bd.gidp)})'
        if meadow_self_e5f59bd.result:
            meadow_rep_e3f4f34 += f', {meadow_self_e5f59bd.result}'
        return meadow_rep_e3f4f34

@_name_boundary.class_contract('BscSharedRegionCheckNp', {})
@meadow_dataclass
class meadow_BscSharedRegionCheckNp:
    ktraces: meadow_List
    startaddress: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_92390d4'}, '__str__')
    def __str__(meadow_self_92390d4):
        meadow_rep_40eb4ff = f'shared_region_check_np({hex(meadow_self_92390d4.startaddress)})'
        if meadow_self_92390d4.result:
            meadow_rep_40eb4ff += f', {meadow_self_92390d4.result}'
        return meadow_rep_40eb4ff

@_name_boundary.class_contract('BscPsynchMutexwait', {})
@meadow_dataclass
class meadow_BscPsynchMutexwait:
    ktraces: meadow_List
    mutex: int
    mgen: int
    ugen: int
    tid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_cbce4d8'}, '__str__')
    def __str__(meadow_self_cbce4d8):
        meadow_rep_286e63f = f'psynch_mutexwait({hex(meadow_self_cbce4d8.mutex)}, {meadow_self_cbce4d8.mgen}, {meadow_self_cbce4d8.ugen}, {meadow_self_cbce4d8.tid})'
        if meadow_self_cbce4d8.result:
            meadow_rep_286e63f += f', {meadow_self_cbce4d8.result}'
        return meadow_rep_286e63f

@_name_boundary.class_contract('BscPsynchMutexdrop', {})
@meadow_dataclass
class meadow_BscPsynchMutexdrop:
    ktraces: meadow_List
    mutex: int
    mgen: int
    ugen: int
    tid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_26fde72'}, '__str__')
    def __str__(meadow_self_26fde72):
        meadow_rep_65429cc = f'psynch_mutexdrop({hex(meadow_self_26fde72.mutex)}, {meadow_self_26fde72.mgen}, {meadow_self_26fde72.ugen}, {meadow_self_26fde72.tid})'
        if meadow_self_26fde72.result:
            meadow_rep_65429cc += f', {meadow_self_26fde72.result}'
        return meadow_rep_65429cc

@_name_boundary.class_contract('BscPsynchCvbroad', {})
@meadow_dataclass
class meadow_BscPsynchCvbroad:
    ktraces: meadow_List
    cv: int
    cvlsgen: int
    cvudgen: int
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b00e884'}, '__str__')
    def __str__(meadow_self_b00e884):
        meadow_rep_6164972 = f'psynch_cvbroad({hex(meadow_self_b00e884.cv)}, {meadow_self_b00e884.cvlsgen}, {meadow_self_b00e884.cvudgen}, {meadow_self_b00e884.flags})'
        if meadow_self_b00e884.result:
            meadow_rep_6164972 += f', {meadow_self_b00e884.result}'
        return meadow_rep_6164972

@_name_boundary.class_contract('BscPsynchCvsignal', {})
@meadow_dataclass
class meadow_BscPsynchCvsignal:
    ktraces: meadow_List
    cv: int
    cvlsgen: int
    cvugen: int
    thread_port: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_f2781a4'}, '__str__')
    def __str__(meadow_self_f2781a4):
        meadow_rep_2b71e65 = f'psynch_cvsignal({hex(meadow_self_f2781a4.cv)}, {meadow_self_f2781a4.cvlsgen}, {meadow_self_f2781a4.cvugen}, {meadow_self_f2781a4.thread_port})'
        if meadow_self_f2781a4.result:
            meadow_rep_2b71e65 += f', {meadow_self_f2781a4.result}'
        return meadow_rep_2b71e65

@_name_boundary.class_contract('BscPsynchCvwait', {})
@meadow_dataclass
class meadow_BscPsynchCvwait:
    ktraces: meadow_List
    cv: int
    cvlsgen: int
    cvugen: int
    mutex: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_93233d9'}, '__str__')
    def __str__(meadow_self_93233d9):
        meadow_rep_28e5c8c = f'psynch_cvwait({hex(meadow_self_93233d9.cv)}, {meadow_self_93233d9.cvlsgen}, {meadow_self_93233d9.cvugen}, {hex(meadow_self_93233d9.mutex)})'
        if meadow_self_93233d9.result:
            meadow_rep_28e5c8c += f', {meadow_self_93233d9.result}'
        return meadow_rep_28e5c8c

@_name_boundary.class_contract('BscGetsid', {})
@meadow_dataclass
class meadow_BscGetsid:
    ktraces: meadow_List
    pid: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_fe1ccde'}, '__str__')
    def __str__(meadow_self_fe1ccde):
        return f'getsid({meadow_self_fe1ccde.pid}), {meadow_self_fe1ccde.result}'

@_name_boundary.class_contract('BscPsynchCvclrprepost', {})
@meadow_dataclass
class meadow_BscPsynchCvclrprepost:
    ktraces: meadow_List
    cv: int
    cvgen: int
    cvugen: int
    cvsgen: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_a3eda1d'}, '__str__')
    def __str__(meadow_self_a3eda1d):
        meadow_rep_d03a1ad = f'psynch_cvclrprepost({hex(meadow_self_a3eda1d.cv)}, {meadow_self_a3eda1d.cvgen}, {meadow_self_a3eda1d.cvugen}, {meadow_self_a3eda1d.cvsgen})'
        if meadow_self_a3eda1d.result:
            meadow_rep_d03a1ad += f', {meadow_self_a3eda1d.result}'
        return meadow_rep_d03a1ad

@_name_boundary.class_contract('BscIopolicysys', {})
@meadow_dataclass
class meadow_BscIopolicysys:
    ktraces: meadow_List
    cmd: int
    arg: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_4d0a625'}, '__str__')
    def __str__(meadow_self_4d0a625):
        return f'iopolicysys({meadow_self_4d0a625.cmd}, {hex(meadow_self_4d0a625.arg)}), {meadow_self_4d0a625.result}'

@_name_boundary.class_contract('BscProcessPolicy', {})
@meadow_dataclass
class meadow_BscProcessPolicy:
    ktraces: meadow_List
    scope: int
    action: int
    policy: int
    policy_subtype: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_3d7611f'}, '__str__')
    def __str__(meadow_self_3d7611f):
        meadow_rep_d8a9acf = f'process_policy({meadow_self_3d7611f.scope}, {meadow_self_3d7611f.action}, {meadow_self_3d7611f.policy}, {meadow_self_3d7611f.policy_subtype})'
        if meadow_self_3d7611f.result:
            meadow_rep_d8a9acf += f', {meadow_self_3d7611f.result}'
        return meadow_rep_d8a9acf

@_name_boundary.class_contract('BscMlockall', {})
@meadow_dataclass
class meadow_BscMlockall:
    ktraces: meadow_List
    flags: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_0ee4172'}, '__str__')
    def __str__(meadow_self_0ee4172):
        meadow_rep_1533de7 = f'mlockall({meadow_self_0ee4172.flags})'
        if meadow_self_0ee4172.result:
            meadow_rep_1533de7 += f', {meadow_self_0ee4172.result}'
        return meadow_rep_1533de7

@_name_boundary.class_contract('BscMunlockall', {})
@meadow_dataclass
class meadow_BscMunlockall:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_ca82ad1'}, '__str__')
    def __str__(meadow_self_ca82ad1):
        meadow_rep_32ce751 = 'munlockall()'
        if meadow_self_ca82ad1.result:
            meadow_rep_32ce751 += f', {meadow_self_ca82ad1.result}'
        return meadow_rep_32ce751

@_name_boundary.class_contract('BscIssetugid', {})
@meadow_dataclass
class meadow_BscIssetugid:
    ktraces: meadow_List
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8a6e986'}, '__str__')
    def __str__(meadow_self_8a6e986):
        return f'issetugid(), {meadow_self_8a6e986.result}'

@_name_boundary.class_contract('BscPthreadSigmask', {})
@meadow_dataclass
class meadow_BscPthreadSigmask:
    ktraces: meadow_List
    how: int
    set: int
    oset: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_9422372'}, '__str__')
    def __str__(meadow_self_9422372):
        meadow_rep_6ba3f14 = f'pthread_sigmask({meadow_self_9422372.how}, {hex(meadow_self_9422372.set)}, {hex(meadow_self_9422372.oset)})'
        if meadow_self_9422372.result:
            meadow_rep_6ba3f14 += f', {meadow_self_9422372.result}'
        return meadow_rep_6ba3f14

@_name_boundary.class_contract('BscDisableThreadsignal', {})
@meadow_dataclass
class meadow_BscDisableThreadsignal:
    ktraces: meadow_List
    value: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_8ca91f6'}, '__str__')
    def __str__(meadow_self_8ca91f6):
        meadow_rep_82716a4 = f'disable_threadsignal({meadow_self_8ca91f6.value})'
        if meadow_self_8ca91f6.result:
            meadow_rep_82716a4 += f', {meadow_self_8ca91f6.result}'
        return meadow_rep_82716a4

@_name_boundary.class_contract('BscSemwaitSignal', {})
@meadow_dataclass
class meadow_BscSemwaitSignal:
    ktraces: meadow_List
    cond_sem: int
    mutex_sem: int
    timeout: int
    relative: int
    result: str
    no_cancel: bool = False

    @_name_boundary.callable_contract({'self': 'meadow_self_14402b5'}, '__str__')
    def __str__(meadow_self_14402b5):
        meadow_no_cancel_a7898af = '_nocancel' if meadow_self_14402b5.no_cancel else ''
        meadow_rep_d7e233d = f'semwait_signal{meadow_no_cancel_a7898af}({meadow_self_14402b5.cond_sem}, {meadow_self_14402b5.mutex_sem}, {meadow_self_14402b5.timeout}, {meadow_self_14402b5.relative})'
        if meadow_self_14402b5.result:
            meadow_rep_d7e233d += f', {meadow_self_14402b5.result}'
        return meadow_rep_d7e233d

@_name_boundary.class_contract('BscProcInfo', {})
@meadow_dataclass
class meadow_BscProcInfo:
    ktraces: meadow_List
    callnum: meadow_ProcInfoCall
    pid: int
    flags: int
    ext_id: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_b6eb898'}, '__str__')
    def __str__(meadow_self_b6eb898):
        meadow_rep_9f65f88 = f"proc_info({_name_boundary.attributes(meadow_self_b6eb898.callnum)['name']}, {meadow_self_b6eb898.pid}, {meadow_self_b6eb898.flags}, {meadow_self_b6eb898.ext_id})"
        if meadow_self_b6eb898.result:
            meadow_rep_9f65f88 += f', {meadow_self_b6eb898.result}'
        return meadow_rep_9f65f88

@_name_boundary.class_contract('BscSendfile', {})
@meadow_dataclass
class meadow_BscSendfile:
    ktraces: meadow_List
    fd: int
    s: int
    offset: int
    len: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_84d5448'}, '__str__')
    def __str__(meadow_self_84d5448):
        meadow_rep_bfc834d = f'sendfile({meadow_self_84d5448.fd}, {meadow_self_84d5448.s}, {meadow_self_84d5448.offset}, {hex(meadow_self_84d5448.len)})'
        if meadow_self_84d5448.result:
            meadow_rep_bfc834d += f', {meadow_self_84d5448.result}'
        return meadow_rep_bfc834d

@_name_boundary.class_contract('BscStat64', {})
@meadow_dataclass
class meadow_BscStat64:
    ktraces: meadow_List
    path: str
    buf: int
    result: str

    @_name_boundary.callable_contract({'self': 'meadow_self_da5a8f2'}, '__str__')
    def __str__(meadow_self_da5a8f2):
        meadow_rep_4665321 = f'stat64("{meadow_self_da5a8f2.path}", {hex(meadow_self_da5a8f2.buf)})'
        if meadow_self_da5a8f2.result:
            meadow_rep_4665321 += f', {meadow_self_da5a8f2.result}'
        return meadow_rep_4665321

@_name_boundary.callable_contract({'parser': 'meadow_parser_f550da0', 'events': 'meadow_events_d354f06', 'no_cancel': 'meadow_no_cancel_53e63a8'}, 'handle_read')
def meadow_handle_read(meadow_parser_f550da0, meadow_events_d354f06, meadow_no_cancel_53e63a8=False):
    meadow_result_f0ebbad = meadow_serialize_result(meadow_events_d354f06[-1], 'count')
    meadow_args_5eb48a1 = meadow_events_d354f06[0].values
    return meadow_BscRead(meadow_events_d354f06, meadow_args_5eb48a1[0], meadow_args_5eb48a1[1], meadow_args_5eb48a1[2], meadow_result_f0ebbad, meadow_no_cancel_53e63a8)

@_name_boundary.callable_contract({'parser': 'meadow_parser_eff0143', 'events': 'meadow_events_5e21462', 'no_cancel': 'meadow_no_cancel_5bcaa68'}, 'handle_write')
def meadow_handle_write(meadow_parser_eff0143, meadow_events_5e21462, meadow_no_cancel_5bcaa68=False):
    meadow_result_6284302 = meadow_serialize_result(meadow_events_5e21462[-1], 'count')
    meadow_args_fb6eedc = meadow_events_5e21462[0].values
    return meadow_BscWrite(meadow_events_5e21462, meadow_args_fb6eedc[0], meadow_args_fb6eedc[1], meadow_args_fb6eedc[2], meadow_result_6284302, meadow_no_cancel_5bcaa68)

@_name_boundary.callable_contract({'parser': 'meadow_parser_f69b3e4', 'events': 'meadow_events_de7de01', 'no_cancel': 'meadow_no_cancel_08f1195'}, 'handle_open')
def meadow_handle_open(meadow_parser_f69b3e4, meadow_events_de7de01, meadow_no_cancel_08f1195=False):
    meadow_vnode_a4414a8 = _name_boundary.attributes(meadow_parser_f69b3e4)['parse_vnode'](meadow_events_de7de01)
    meadow_call_flags_0adde2c = meadow_serialize_open_flags(meadow_events_de7de01[0].values[1])
    return meadow_BscOpen(meadow_events_de7de01, meadow_vnode_a4414a8.path, meadow_call_flags_0adde2c, meadow_serialize_result(meadow_events_de7de01[-1], 'fd'), meadow_no_cancel_08f1195)

@_name_boundary.callable_contract({'parser': 'meadow_parser_c9cde7e', 'events': 'meadow_events_5dbeea3', 'no_cancel': 'meadow_no_cancel_b3fc92e'}, 'handle_sys_close')
def meadow_handle_sys_close(meadow_parser_c9cde7e, meadow_events_5dbeea3, meadow_no_cancel_b3fc92e=False):
    return meadow_BscSysClose(meadow_events_5dbeea3, meadow_events_5dbeea3[0].values[0], meadow_serialize_result(meadow_events_5dbeea3[-1]), meadow_no_cancel_b3fc92e)

@_name_boundary.callable_contract({'parser': 'meadow_parser_4a9ec40', 'events': 'meadow_events_e28dd6d'}, 'handle_link')
def meadow_handle_link(meadow_parser_4a9ec40, meadow_events_e28dd6d):
    meadow_old_vnode_eec80f1 = _name_boundary.attributes(meadow_parser_4a9ec40)['parse_vnode'](meadow_events_e28dd6d)
    meadow_new_vnode_81a81a2 = _name_boundary.attributes(meadow_parser_4a9ec40)['parse_vnode']([meadow_e_a04fec9 for meadow_e_a04fec9 in meadow_events_e28dd6d if meadow_e_a04fec9 not in meadow_old_vnode_eec80f1.ktraces])
    return meadow_BscLink(meadow_events_e28dd6d, meadow_old_vnode_eec80f1.path, meadow_new_vnode_81a81a2.path, meadow_serialize_result(meadow_events_e28dd6d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_95c84f8', 'events': 'meadow_events_b69d189'}, 'handle_unlink')
def meadow_handle_unlink(meadow_parser_95c84f8, meadow_events_b69d189):
    meadow_vnode_263ec6b = _name_boundary.attributes(meadow_parser_95c84f8)['parse_vnode'](meadow_events_b69d189)
    return meadow_BscUnlink(meadow_events_b69d189, meadow_vnode_263ec6b.path, meadow_serialize_result(meadow_events_b69d189[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_80cc4cb', 'events': 'meadow_events_3bd0fd3'}, 'handle_chdir')
def meadow_handle_chdir(meadow_parser_80cc4cb, meadow_events_3bd0fd3):
    meadow_vnode_82ed1ff = _name_boundary.attributes(meadow_parser_80cc4cb)['parse_vnode'](meadow_events_3bd0fd3)
    return meadow_BscChdir(meadow_events_3bd0fd3, meadow_vnode_82ed1ff.path, meadow_serialize_result(meadow_events_3bd0fd3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e1934a6', 'events': 'meadow_events_280cbad'}, 'handle_fchdir')
def meadow_handle_fchdir(meadow_parser_e1934a6, meadow_events_280cbad):
    return meadow_BscFchdir(meadow_events_280cbad, meadow_events_280cbad[0].values[0], meadow_serialize_result(meadow_events_280cbad[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_87e5243', 'events': 'meadow_events_6e78b5c'}, 'handle_mknod')
def meadow_handle_mknod(meadow_parser_87e5243, meadow_events_6e78b5c):
    meadow_vnode_591069e = _name_boundary.attributes(meadow_parser_87e5243)['parse_vnode'](meadow_events_6e78b5c)
    return meadow_BscMknod(meadow_events_6e78b5c, meadow_vnode_591069e.path, meadow_events_6e78b5c[0].values[1], meadow_events_6e78b5c[0].values[2], meadow_serialize_result(meadow_events_6e78b5c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5018774', 'events': 'meadow_events_aece7bd'}, 'handle_chmod')
def meadow_handle_chmod(meadow_parser_5018774, meadow_events_aece7bd):
    meadow_vnode_73292a6 = _name_boundary.attributes(meadow_parser_5018774)['parse_vnode'](meadow_events_aece7bd)
    return meadow_BscChmod(meadow_events_aece7bd, meadow_vnode_73292a6.path, meadow_serialize_stat_flags(meadow_events_aece7bd[0].values[1]), meadow_serialize_result(meadow_events_aece7bd[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_982ba0b', 'events': 'meadow_events_768e290'}, 'handle_chown')
def meadow_handle_chown(meadow_parser_982ba0b, meadow_events_768e290):
    meadow_vnode_754d193 = _name_boundary.attributes(meadow_parser_982ba0b)['parse_vnode'](meadow_events_768e290)
    return meadow_BscChown(meadow_events_768e290, meadow_vnode_754d193.path, meadow_events_768e290[0].values[1], meadow_events_768e290[0].values[2], meadow_serialize_result(meadow_events_768e290[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_3c846f5', 'events': 'meadow_events_a8d30a5'}, 'handle_getpid')
def meadow_handle_getpid(meadow_parser_3c846f5, meadow_events_a8d30a5):
    return meadow_BscGetpid(meadow_events_a8d30a5, meadow_events_a8d30a5[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_52b630a', 'events': 'meadow_events_82607b1'}, 'handle_setuid')
def meadow_handle_setuid(meadow_parser_52b630a, meadow_events_82607b1):
    return meadow_BscSetuid(meadow_events_82607b1, meadow_events_82607b1[0].values[0], meadow_serialize_result(meadow_events_82607b1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9441193', 'events': 'meadow_events_95a4879'}, 'handle_getuid')
def meadow_handle_getuid(meadow_parser_9441193, meadow_events_95a4879):
    return meadow_BscGetuid(meadow_events_95a4879, meadow_events_95a4879[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_4c9492f', 'events': 'meadow_events_4dbe089'}, 'handle_geteuid')
def meadow_handle_geteuid(meadow_parser_4c9492f, meadow_events_4dbe089):
    return meadow_BscGeteuid(meadow_events_4dbe089, meadow_events_4dbe089[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_dba0538', 'events': 'meadow_events_9f1fb65', 'no_cancel': 'meadow_no_cancel_8426184'}, 'handle_wait4')
def meadow_handle_wait4(meadow_parser_dba0538, meadow_events_9f1fb65, meadow_no_cancel_8426184=False):
    meadow_args_d599723 = meadow_events_9f1fb65[0].values
    return meadow_BscWait4(meadow_events_9f1fb65, meadow_args_d599723[0], meadow_args_d599723[1], meadow_args_d599723[2], meadow_args_d599723[3], meadow_serialize_result(meadow_events_9f1fb65[-1], 'pid'), meadow_no_cancel_8426184)

@_name_boundary.callable_contract({'parser': 'meadow_parser_bf20410', 'events': 'meadow_events_dad1af3', 'no_cancel': 'meadow_no_cancel_0074205'}, 'handle_recvmsg')
def meadow_handle_recvmsg(meadow_parser_bf20410, meadow_events_dad1af3, meadow_no_cancel_0074205=False):
    return meadow_BscRecvmsg(meadow_events_dad1af3, meadow_events_dad1af3[0].values[0], meadow_serialize_result(meadow_events_dad1af3[-1], 'count'), meadow_no_cancel_0074205)

@_name_boundary.callable_contract({'parser': 'meadow_parser_bdfec0f', 'events': 'meadow_events_a6e5335', 'no_cancel': 'meadow_no_cancel_04511aa'}, 'handle_sendmsg')
def meadow_handle_sendmsg(meadow_parser_bdfec0f, meadow_events_a6e5335, meadow_no_cancel_04511aa=False):
    return meadow_BscSendmsg(meadow_events_a6e5335, meadow_events_a6e5335[0].values[0], meadow_serialize_result(meadow_events_a6e5335[-1], 'count'), meadow_no_cancel_04511aa)

@_name_boundary.callable_contract({'parser': 'meadow_parser_3328e49', 'events': 'meadow_events_86bfb90', 'no_cancel': 'meadow_no_cancel_339a467'}, 'handle_recvfrom')
def meadow_handle_recvfrom(meadow_parser_3328e49, meadow_events_86bfb90, meadow_no_cancel_339a467=False):
    meadow_args_6ef1c68 = meadow_events_86bfb90[0].values
    meadow_flags_2a3d25f = [meadow_flag_2e4dd3d for meadow_flag_2e4dd3d in meadow_SocketMsgFlags if meadow_flag_2e4dd3d.value & meadow_args_6ef1c68[3]]
    return meadow_BscRecvfrom(meadow_events_86bfb90, meadow_args_6ef1c68[0], meadow_args_6ef1c68[1], meadow_args_6ef1c68[2], meadow_flags_2a3d25f, meadow_serialize_result(meadow_events_86bfb90[-1], 'count'), meadow_no_cancel_339a467)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a20eba7', 'events': 'meadow_events_dae6f7e', 'no_cancel': 'meadow_no_cancel_34d0091'}, 'handle_accept')
def meadow_handle_accept(meadow_parser_a20eba7, meadow_events_dae6f7e, meadow_no_cancel_34d0091=False):
    return meadow_BscAccept(meadow_events_dae6f7e, meadow_events_dae6f7e[0].values[0], meadow_serialize_result(meadow_events_dae6f7e[-1], 'fd'), meadow_no_cancel_34d0091)

@_name_boundary.callable_contract({'parser': 'meadow_parser_52a9e32', 'events': 'meadow_events_50b11ac'}, 'handle_getpeername')
def meadow_handle_getpeername(meadow_parser_52a9e32, meadow_events_50b11ac):
    meadow_args_5f2cb0a = meadow_events_50b11ac[0].values
    return meadow_BscGetpeername(meadow_events_50b11ac, meadow_args_5f2cb0a[0], meadow_args_5f2cb0a[1], meadow_args_5f2cb0a[2], meadow_serialize_result(meadow_events_50b11ac[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0159f39', 'events': 'meadow_events_21b0428'}, 'handle_getsockname')
def meadow_handle_getsockname(meadow_parser_0159f39, meadow_events_21b0428):
    meadow_args_842fa30 = meadow_events_21b0428[0].values
    return meadow_BscGetsockname(meadow_events_21b0428, meadow_args_842fa30[0], meadow_args_842fa30[1], meadow_args_842fa30[2], meadow_serialize_result(meadow_events_21b0428[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_63334cb', 'events': 'meadow_events_b363451'}, 'handle_access')
def meadow_handle_access(meadow_parser_63334cb, meadow_events_b363451):
    meadow_vnode_addaaf2 = _name_boundary.attributes(meadow_parser_63334cb)['parse_vnode'](meadow_events_b363451)
    meadow_amode_29bea97 = meadow_serialize_access_flags(meadow_events_b363451[0].values[1])
    return meadow_BscAccess(meadow_events_b363451, meadow_vnode_addaaf2.path, meadow_amode_29bea97, meadow_serialize_result(meadow_events_b363451[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e5239a2', 'events': 'meadow_events_9bea1ad'}, 'handle_chflags')
def meadow_handle_chflags(meadow_parser_e5239a2, meadow_events_9bea1ad):
    meadow_vnode_2b50a22 = _name_boundary.attributes(meadow_parser_e5239a2)['parse_vnode'](meadow_events_9bea1ad)
    meadow_flags_9073082 = [meadow_flag_6a56feb for meadow_flag_6a56feb in meadow_BscChangeableFlags if meadow_flag_6a56feb.value & meadow_events_9bea1ad[0].values[1]]
    return meadow_BscChflags(meadow_events_9bea1ad, meadow_vnode_2b50a22.path, meadow_flags_9073082, meadow_serialize_result(meadow_events_9bea1ad[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4d4347d', 'events': 'meadow_events_5087043'}, 'handle_fchflags')
def meadow_handle_fchflags(meadow_parser_4d4347d, meadow_events_5087043):
    meadow_flags_1e136a2 = [meadow_flag_365edbf for meadow_flag_365edbf in meadow_BscChangeableFlags if meadow_flag_365edbf.value & meadow_events_5087043[0].values[1]]
    return meadow_BscFchflags(meadow_events_5087043, meadow_events_5087043[0].values[0], meadow_flags_1e136a2, meadow_serialize_result(meadow_events_5087043[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b9d1938', 'events': 'meadow_events_13f7439'}, 'handle_sync')
def meadow_handle_sync(meadow_parser_b9d1938, meadow_events_13f7439):
    return meadow_BscSync(meadow_events_13f7439)

@_name_boundary.callable_contract({'parser': 'meadow_parser_1f1e3c2', 'events': 'meadow_events_7120057'}, 'handle_kill')
def meadow_handle_kill(meadow_parser_1f1e3c2, meadow_events_7120057):
    return meadow_BscKill(meadow_events_7120057, meadow_events_7120057[0].values[0], meadow_events_7120057[0].values[1], meadow_serialize_result(meadow_events_7120057[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7f9745d', 'events': 'meadow_events_98a4184'}, 'handle_getppid')
def meadow_handle_getppid(meadow_parser_7f9745d, meadow_events_98a4184):
    return meadow_BscGetppid(meadow_events_98a4184, meadow_events_98a4184[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_b28f192', 'events': 'meadow_events_3ac8747'}, 'handle_sys_dup')
def meadow_handle_sys_dup(meadow_parser_b28f192, meadow_events_3ac8747):
    return meadow_BscSysDup(meadow_events_3ac8747, meadow_events_3ac8747[0].values[0], meadow_serialize_result(meadow_events_3ac8747[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_693d8af', 'events': 'meadow_events_8dd60be'}, 'handle_pipe')
def meadow_handle_pipe(meadow_parser_693d8af, meadow_events_8dd60be):
    meadow_error_code_ce9a43a = meadow_events_8dd60be[-1].values[0]
    if meadow_error_code_ce9a43a:
        if meadow_error_code_ce9a43a in meadow_errno.errorcode:
            meadow_result_a2adf60 = f'errno: {meadow_errno.errorcode[meadow_error_code_ce9a43a]}({meadow_error_code_ce9a43a})'
        else:
            meadow_result_a2adf60 = f'errno: {meadow_error_code_ce9a43a}'
    else:
        meadow_result_a2adf60 = f'read_fd: {meadow_events_8dd60be[-1].values[1]}, write_fd: {meadow_events_8dd60be[-1].values[2]}'
    return meadow_BscPipe(meadow_events_8dd60be, meadow_result_a2adf60)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a3aea2f', 'events': 'meadow_events_cbf0288'}, 'handle_getegid')
def meadow_handle_getegid(meadow_parser_a3aea2f, meadow_events_cbf0288):
    return meadow_BscGetegid(meadow_events_cbf0288, meadow_events_cbf0288[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_c85495c', 'events': 'meadow_events_7dd21f2'}, 'handle_sigaction')
def meadow_handle_sigaction(meadow_parser_c85495c, meadow_events_7dd21f2):
    meadow_args_eb1c2f0 = meadow_events_7dd21f2[0].values
    return meadow_BscSigaction(meadow_events_7dd21f2, meadow_Signals(meadow_args_eb1c2f0[0]), meadow_args_eb1c2f0[1], meadow_args_eb1c2f0[2], meadow_serialize_result(meadow_events_7dd21f2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_83f784b', 'events': 'meadow_events_68654f3'}, 'handle_getgid')
def meadow_handle_getgid(meadow_parser_83f784b, meadow_events_68654f3):
    return meadow_BscGetgid(meadow_events_68654f3, meadow_events_68654f3[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_6304575', 'events': 'meadow_events_f73a217'}, 'handle_sigprocmask')
def meadow_handle_sigprocmask(meadow_parser_6304575, meadow_events_f73a217):
    meadow_args_6a258e2 = meadow_events_f73a217[0].values
    return meadow_BscSigprocmap(meadow_events_f73a217, meadow_SigprocmaskFlags(meadow_args_6a258e2[0]), meadow_args_6a258e2[1], meadow_args_6a258e2[2], meadow_serialize_result(meadow_events_f73a217[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ce4539b', 'events': 'meadow_events_a3ec2c6'}, 'handle_getlogin')
def meadow_handle_getlogin(meadow_parser_ce4539b, meadow_events_a3ec2c6):
    return meadow_BscGetlogin(meadow_events_a3ec2c6, meadow_events_a3ec2c6[0].values[0])

@_name_boundary.callable_contract({'parser': 'meadow_parser_2d8684e', 'events': 'meadow_events_7c43c1a'}, 'handle_setlogin')
def meadow_handle_setlogin(meadow_parser_2d8684e, meadow_events_7c43c1a):
    return meadow_BscSetlogin(meadow_events_7c43c1a, meadow_events_7c43c1a[0].values[0], meadow_serialize_result(meadow_events_7c43c1a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b8c860f', 'events': 'meadow_events_e534822'}, 'handle_acct')
def meadow_handle_acct(meadow_parser_b8c860f, meadow_events_e534822):
    return meadow_BscAcct(meadow_events_e534822, _name_boundary.attributes(meadow_parser_b8c860f)['parse_vnode'](meadow_events_e534822).path, meadow_serialize_result(meadow_events_e534822[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cfb585f', 'events': 'meadow_events_b9eb68b'}, 'handle_sigpending')
def meadow_handle_sigpending(meadow_parser_cfb585f, meadow_events_b9eb68b):
    return meadow_BscSigpending(meadow_events_b9eb68b, meadow_events_b9eb68b[0].values[0], meadow_serialize_result(meadow_events_b9eb68b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f9b7014', 'events': 'meadow_events_9435741'}, 'handle_sigaltstack')
def meadow_handle_sigaltstack(meadow_parser_f9b7014, meadow_events_9435741):
    return meadow_BscSigaltstack(meadow_events_9435741, meadow_events_9435741[0].values[0], meadow_events_9435741[0].values[1], meadow_serialize_result(meadow_events_9435741[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_51113e1', 'events': 'meadow_events_86ef9bd'}, 'handle_ioctl')
def meadow_handle_ioctl(meadow_parser_51113e1, meadow_events_86ef9bd):
    meadow_args_05cf7ed = meadow_events_86ef9bd[0].values
    return meadow_BscIoctl(meadow_events_86ef9bd, meadow_args_05cf7ed[0], meadow_args_05cf7ed[1], meadow_args_05cf7ed[2], meadow_serialize_result(meadow_events_86ef9bd[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6c245fc', 'events': 'meadow_events_8523bd9'}, 'handle_reboot')
def meadow_handle_reboot(meadow_parser_6c245fc, meadow_events_8523bd9):
    return meadow_BscReboot(meadow_events_8523bd9, meadow_events_8523bd9[0].values[0], meadow_serialize_result(meadow_events_8523bd9[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bb051bc', 'events': 'meadow_events_4becdcd'}, 'handle_revoke')
def meadow_handle_revoke(meadow_parser_bb051bc, meadow_events_4becdcd):
    return meadow_BscRevoke(meadow_events_4becdcd, _name_boundary.attributes(meadow_parser_bb051bc)['parse_vnode'](meadow_events_4becdcd).path, meadow_serialize_result(meadow_events_4becdcd[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_3744f1e', 'events': 'meadow_events_0fbff07'}, 'handle_symlink')
def meadow_handle_symlink(meadow_parser_3744f1e, meadow_events_0fbff07):
    return meadow_BscSymlink(meadow_events_0fbff07, meadow_events_0fbff07[0].values[0], _name_boundary.attributes(meadow_parser_3744f1e)['parse_vnode'](meadow_events_0fbff07).path, meadow_serialize_result(meadow_events_0fbff07[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_323142b', 'events': 'meadow_events_f3b5225'}, 'handle_readlink')
def meadow_handle_readlink(meadow_parser_323142b, meadow_events_f3b5225):
    meadow_args_e41c37a = meadow_events_f3b5225[0].values
    return meadow_BscReadlink(meadow_events_f3b5225, _name_boundary.attributes(meadow_parser_323142b)['parse_vnode'](meadow_events_f3b5225).path, meadow_args_e41c37a[1], meadow_args_e41c37a[2], meadow_serialize_result(meadow_events_f3b5225[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0a4b1fa', 'events': 'meadow_events_442d328'}, 'handle_execve')
def meadow_handle_execve(meadow_parser_0a4b1fa, meadow_events_442d328):
    return meadow_BscExecve(meadow_events_442d328)

@_name_boundary.callable_contract({'parser': 'meadow_parser_c6792d9', 'events': 'meadow_events_f72046d'}, 'handle_umask')
def meadow_handle_umask(meadow_parser_c6792d9, meadow_events_f72046d):
    return meadow_BscUmask(meadow_events_f72046d, meadow_events_f72046d[0].values[0], meadow_events_f72046d[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_900922f', 'events': 'meadow_events_761f308'}, 'handle_chroot')
def meadow_handle_chroot(meadow_parser_900922f, meadow_events_761f308):
    return meadow_BscChroot(meadow_events_761f308, _name_boundary.attributes(meadow_parser_900922f)['parse_vnode'](meadow_events_761f308).path, meadow_serialize_result(meadow_events_761f308[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_592ba6e', 'events': 'meadow_events_aa3c556', 'no_cancel': 'meadow_no_cancel_3cd27aa'}, 'handle_msync')
def meadow_handle_msync(meadow_parser_592ba6e, meadow_events_aa3c556, meadow_no_cancel_3cd27aa=False):
    meadow_args_a4d8b02 = meadow_events_aa3c556[0].values
    return meadow_BscMsync(meadow_events_aa3c556, meadow_args_a4d8b02[0], meadow_args_a4d8b02[1], meadow_args_a4d8b02[2], meadow_serialize_result(meadow_events_aa3c556[-1]), meadow_no_cancel_3cd27aa)

@_name_boundary.callable_contract({'parser': 'meadow_parser_dc65fd2', 'events': 'meadow_events_27b4a35'}, 'handle_vfork')
def meadow_handle_vfork(meadow_parser_dc65fd2, meadow_events_27b4a35):
    return meadow_BscVfork(meadow_events_27b4a35)

@_name_boundary.callable_contract({'parser': 'meadow_parser_eda798d', 'events': 'meadow_events_19dcaaf'}, 'handle_munmap')
def meadow_handle_munmap(meadow_parser_eda798d, meadow_events_19dcaaf):
    meadow_args_7fa409a = meadow_events_19dcaaf[0].values
    return meadow_BscMunmap(meadow_events_19dcaaf, meadow_args_7fa409a[0], meadow_args_7fa409a[1], meadow_serialize_result(meadow_events_19dcaaf[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_12928e9', 'events': 'meadow_events_785e85e'}, 'handle_mprotect')
def meadow_handle_mprotect(meadow_parser_12928e9, meadow_events_785e85e):
    meadow_args_543d694 = meadow_events_785e85e[0].values
    return meadow_BscMprotect(meadow_events_785e85e, meadow_args_543d694[0], meadow_args_543d694[1], meadow_args_543d694[2], meadow_serialize_result(meadow_events_785e85e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c5e4efa', 'events': 'meadow_events_700ea1d'}, 'handle_madvise')
def meadow_handle_madvise(meadow_parser_c5e4efa, meadow_events_700ea1d):
    meadow_args_aad8aa3 = meadow_events_700ea1d[0].values
    return meadow_BscMadvise(meadow_events_700ea1d, meadow_args_aad8aa3[0], meadow_args_aad8aa3[1], meadow_args_aad8aa3[2], meadow_serialize_result(meadow_events_700ea1d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_47bd048', 'events': 'meadow_events_f1ce6e9'}, 'handle_mincore')
def meadow_handle_mincore(meadow_parser_47bd048, meadow_events_f1ce6e9):
    meadow_args_1b8383c = meadow_events_f1ce6e9[0].values
    return meadow_BscMincore(meadow_events_f1ce6e9, meadow_args_1b8383c[0], meadow_args_1b8383c[1], meadow_args_1b8383c[2], meadow_serialize_result(meadow_events_f1ce6e9[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_27846af', 'events': 'meadow_events_1542be0'}, 'handle_getgroups')
def meadow_handle_getgroups(meadow_parser_27846af, meadow_events_1542be0):
    meadow_args_35a36f5 = meadow_events_1542be0[0].values
    return meadow_BscGetgroups(meadow_events_1542be0, meadow_args_35a36f5[0], meadow_args_35a36f5[1], meadow_serialize_result(meadow_events_1542be0[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_49f9ba0', 'events': 'meadow_events_b83ec47'}, 'handle_setgroups')
def meadow_handle_setgroups(meadow_parser_49f9ba0, meadow_events_b83ec47):
    meadow_args_141a3a1 = meadow_events_b83ec47[0].values
    return meadow_BscSetgroups(meadow_events_b83ec47, meadow_args_141a3a1[0], meadow_args_141a3a1[1], meadow_serialize_result(meadow_events_b83ec47[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b3541d6', 'events': 'meadow_events_f99ba71'}, 'handle_getpgrp')
def meadow_handle_getpgrp(meadow_parser_b3541d6, meadow_events_f99ba71):
    return meadow_BscGetpgrp(meadow_events_f99ba71, meadow_events_f99ba71[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_92fd2d9', 'events': 'meadow_events_df17bc5'}, 'handle_setpgid')
def meadow_handle_setpgid(meadow_parser_92fd2d9, meadow_events_df17bc5):
    return meadow_BscSetpgid(meadow_events_df17bc5, meadow_events_df17bc5[0].values[0], meadow_events_df17bc5[0].values[1], meadow_serialize_result(meadow_events_df17bc5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8a83a6c', 'events': 'meadow_events_38cf7f6'}, 'handle_setitimer')
def meadow_handle_setitimer(meadow_parser_8a83a6c, meadow_events_38cf7f6):
    meadow_args_0ae7059 = meadow_events_38cf7f6[0].values
    return meadow_BscSetitimer(meadow_events_38cf7f6, meadow_args_0ae7059[0], meadow_args_0ae7059[1], meadow_args_0ae7059[2], meadow_serialize_result(meadow_events_38cf7f6[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9aad32f', 'events': 'meadow_events_373401e'}, 'handle_swapon')
def meadow_handle_swapon(meadow_parser_9aad32f, meadow_events_373401e):
    meadow_args_9ba9ff0 = meadow_events_373401e[0].values
    return meadow_BscSwapon(meadow_events_373401e, meadow_args_9ba9ff0[0], meadow_args_9ba9ff0[1], meadow_serialize_result(meadow_events_373401e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f8d2025', 'events': 'meadow_events_c2abaa2'}, 'handle_getitimer')
def meadow_handle_getitimer(meadow_parser_f8d2025, meadow_events_c2abaa2):
    meadow_args_d15ccc1 = meadow_events_c2abaa2[0].values
    return meadow_BscGetitimer(meadow_events_c2abaa2, meadow_args_d15ccc1[0], meadow_args_d15ccc1[1], meadow_serialize_result(meadow_events_c2abaa2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f4ed38e', 'events': 'meadow_events_a744cde'}, 'handle_sys_getdtablesize')
def meadow_handle_sys_getdtablesize(meadow_parser_f4ed38e, meadow_events_a744cde):
    return meadow_BscSysGetdtablesize(meadow_events_a744cde, meadow_events_a744cde[-1].values[1])

@_name_boundary.callable_contract({'parser': 'meadow_parser_fb33c34', 'events': 'meadow_events_2a5fc77'}, 'handle_sys_dup2')
def meadow_handle_sys_dup2(meadow_parser_fb33c34, meadow_events_2a5fc77):
    meadow_args_3271637 = meadow_events_2a5fc77[0].values
    return meadow_BscSysDup2(meadow_events_2a5fc77, meadow_args_3271637[0], meadow_args_3271637[1], meadow_serialize_result(meadow_events_2a5fc77[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d688b36', 'events': 'meadow_events_dbab9ce', 'no_cancel': 'meadow_no_cancel_b67ca1d'}, 'handle_sys_fcntl')
def meadow_handle_sys_fcntl(meadow_parser_d688b36, meadow_events_dbab9ce, meadow_no_cancel_b67ca1d=False):
    meadow_args_05ba13b = meadow_events_dbab9ce[0].values
    return meadow_BscSysFcntl(meadow_events_dbab9ce, meadow_args_05ba13b[0], meadow_FcntlCmd(meadow_args_05ba13b[1]), meadow_args_05ba13b[2], meadow_serialize_result(meadow_events_dbab9ce[-1], 'return'), meadow_no_cancel_b67ca1d)

@_name_boundary.callable_contract({'parser': 'meadow_parser_acf7d96', 'events': 'meadow_events_799810b', 'no_cancel': 'meadow_no_cancel_c15f801'}, 'handle_select')
def meadow_handle_select(meadow_parser_acf7d96, meadow_events_799810b, meadow_no_cancel_c15f801=False):
    meadow_args_080b07d = meadow_events_799810b[0].values
    return meadow_BscSelect(meadow_events_799810b, meadow_args_080b07d[0], meadow_args_080b07d[1], meadow_args_080b07d[2], meadow_args_080b07d[3], meadow_serialize_result(meadow_events_799810b[-1], 'count'), meadow_no_cancel_c15f801)

@_name_boundary.callable_contract({'parser': 'meadow_parser_6d1a909', 'events': 'meadow_events_8e42318', 'no_cancel': 'meadow_no_cancel_09084da'}, 'handle_fsync')
def meadow_handle_fsync(meadow_parser_6d1a909, meadow_events_8e42318, meadow_no_cancel_09084da=False):
    return meadow_BscFsync(meadow_events_8e42318, meadow_events_8e42318[0].values[0], meadow_serialize_result(meadow_events_8e42318[-1]), meadow_no_cancel_09084da)

@_name_boundary.callable_contract({'parser': 'meadow_parser_9aeeffb', 'events': 'meadow_events_b57345a'}, 'handle_setpriority')
def meadow_handle_setpriority(meadow_parser_9aeeffb, meadow_events_b57345a):
    meadow_args_0746506 = meadow_events_b57345a[0].values
    return meadow_BscSetpriority(meadow_events_b57345a, meadow_PriorityWhich(meadow_args_0746506[0]), meadow_args_0746506[1], meadow_args_0746506[2], meadow_serialize_result(meadow_events_b57345a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_de6b0b5', 'events': 'meadow_events_96cb5fa'}, 'handle_socket')
def meadow_handle_socket(meadow_parser_de6b0b5, meadow_events_96cb5fa):
    meadow_args_3e4ec55 = meadow_events_96cb5fa[0].values
    return meadow_BscSocket(meadow_events_96cb5fa, meadow_socket.AddressFamily(meadow_args_3e4ec55[0]), meadow_socket.SocketKind(meadow_args_3e4ec55[1]), meadow_args_3e4ec55[2], meadow_serialize_result(meadow_events_96cb5fa[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2a0cd0d', 'events': 'meadow_events_2b7b380', 'no_cancel': 'meadow_no_cancel_99f0935'}, 'handle_connect')
def meadow_handle_connect(meadow_parser_2a0cd0d, meadow_events_2b7b380, meadow_no_cancel_99f0935=False):
    meadow_args_8a83a4a = meadow_events_2b7b380[0].values
    return meadow_BscConnect(meadow_events_2b7b380, meadow_args_8a83a4a[0], meadow_args_8a83a4a[1], meadow_args_8a83a4a[2], meadow_serialize_result(meadow_events_2b7b380[-1]), meadow_no_cancel_99f0935)

@_name_boundary.callable_contract({'parser': 'meadow_parser_1c8960e', 'events': 'meadow_events_df203cd'}, 'handle_getpriority')
def meadow_handle_getpriority(meadow_parser_1c8960e, meadow_events_df203cd):
    meadow_args_37ef0a9 = meadow_events_df203cd[0].values
    return meadow_BscGetpriority(meadow_events_df203cd, meadow_PriorityWhich(meadow_args_37ef0a9[0]), meadow_args_37ef0a9[1], meadow_serialize_result(meadow_events_df203cd[-1], 'priority'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e0d772e', 'events': 'meadow_events_1866306'}, 'handle_bind')
def meadow_handle_bind(meadow_parser_e0d772e, meadow_events_1866306):
    meadow_args_6425d32 = meadow_events_1866306[0].values
    return meadow_BscBind(meadow_events_1866306, meadow_args_6425d32[0], meadow_args_6425d32[1], meadow_args_6425d32[2], meadow_serialize_result(meadow_events_1866306[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2fb3d0f', 'events': 'meadow_events_d460ecc'}, 'handle_setsockopt')
def meadow_handle_setsockopt(meadow_parser_2fb3d0f, meadow_events_d460ecc):
    meadow_args_3b31c9d = meadow_events_d460ecc[0].values
    return meadow_BscSetsockopt(meadow_events_d460ecc, meadow_args_3b31c9d[0], meadow_args_3b31c9d[1], meadow_args_3b31c9d[2], meadow_args_3b31c9d[3], meadow_serialize_result(meadow_events_d460ecc[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f83dec6', 'events': 'meadow_events_0dfe928'}, 'handle_listen')
def meadow_handle_listen(meadow_parser_f83dec6, meadow_events_0dfe928):
    meadow_args_f3b4cc7 = meadow_events_0dfe928[0].values
    return meadow_BscListen(meadow_events_0dfe928, meadow_args_f3b4cc7[0], meadow_args_f3b4cc7[1], meadow_serialize_result(meadow_events_0dfe928[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a0f6b49', 'events': 'meadow_events_d3ee165', 'no_cancel': 'meadow_no_cancel_43eb9a0'}, 'handle_sigsuspend')
def meadow_handle_sigsuspend(meadow_parser_a0f6b49, meadow_events_d3ee165, meadow_no_cancel_43eb9a0=False):
    return meadow_BscSigsuspend(meadow_events_d3ee165, meadow_events_d3ee165[0].values[0], meadow_serialize_result(meadow_events_d3ee165[-1]), meadow_no_cancel_43eb9a0)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a315c8c', 'events': 'meadow_events_1b379f8'}, 'handle_gettimeofday')
def meadow_handle_gettimeofday(meadow_parser_a315c8c, meadow_events_1b379f8):
    meadow_args_f24b8c2 = meadow_events_1b379f8[0].values
    return meadow_BscGettimeofday(meadow_events_1b379f8, meadow_args_f24b8c2[0], meadow_args_f24b8c2[1], meadow_serialize_result(meadow_events_1b379f8[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_dbe746e', 'events': 'meadow_events_3b32185'}, 'handle_getrusage')
def meadow_handle_getrusage(meadow_parser_dbe746e, meadow_events_3b32185):
    meadow_args_24d0bba = meadow_events_3b32185[0].values
    return meadow_BscGetrusage(meadow_events_3b32185, meadow_RusageWho(meadow_ctypes.c_int32(meadow_args_24d0bba[0]).value), meadow_args_24d0bba[1], meadow_serialize_result(meadow_events_3b32185[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_54e7e89', 'events': 'meadow_events_94e0598'}, 'handle_getsockopt')
def meadow_handle_getsockopt(meadow_parser_54e7e89, meadow_events_94e0598):
    meadow_args_3a18957 = meadow_events_94e0598[0].values
    return meadow_BscGetsockopt(meadow_events_94e0598, meadow_args_3a18957[0], meadow_args_3a18957[1], meadow_args_3a18957[2], meadow_args_3a18957[3], meadow_serialize_result(meadow_events_94e0598[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_498ed21', 'events': 'meadow_events_865201f', 'no_cancel': 'meadow_no_cancel_69d500e'}, 'handle_readv')
def meadow_handle_readv(meadow_parser_498ed21, meadow_events_865201f, meadow_no_cancel_69d500e=False):
    meadow_args_149b135 = meadow_events_865201f[0].values
    return meadow_BscReadv(meadow_events_865201f, meadow_args_149b135[0], meadow_args_149b135[1], meadow_args_149b135[2], meadow_serialize_result(meadow_events_865201f[-1], 'count'), meadow_no_cancel_69d500e)

@_name_boundary.callable_contract({'parser': 'meadow_parser_dc816ac', 'events': 'meadow_events_a3019c1', 'no_cancel': 'meadow_no_cancel_42ae175'}, 'handle_writev')
def meadow_handle_writev(meadow_parser_dc816ac, meadow_events_a3019c1, meadow_no_cancel_42ae175=False):
    meadow_args_4858306 = meadow_events_a3019c1[0].values
    return meadow_BscWritev(meadow_events_a3019c1, meadow_args_4858306[0], meadow_args_4858306[1], meadow_args_4858306[2], meadow_serialize_result(meadow_events_a3019c1[-1], 'count'), meadow_no_cancel_42ae175)

@_name_boundary.callable_contract({'parser': 'meadow_parser_fd994bf', 'events': 'meadow_events_4382c0e'}, 'handle_settimeofday')
def meadow_handle_settimeofday(meadow_parser_fd994bf, meadow_events_4382c0e):
    meadow_args_5acc0b3 = meadow_events_4382c0e[0].values
    return meadow_BscSettimeofday(meadow_events_4382c0e, meadow_args_5acc0b3[0], meadow_args_5acc0b3[1], meadow_serialize_result(meadow_events_4382c0e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_98a1592', 'events': 'meadow_events_219d780'}, 'handle_fchown')
def meadow_handle_fchown(meadow_parser_98a1592, meadow_events_219d780):
    meadow_args_deb55ef = meadow_events_219d780[0].values
    return meadow_BscFchown(meadow_events_219d780, meadow_args_deb55ef[0], meadow_args_deb55ef[1], meadow_args_deb55ef[2], meadow_serialize_result(meadow_events_219d780[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c24451a', 'events': 'meadow_events_a078a8b'}, 'handle_fchmod')
def meadow_handle_fchmod(meadow_parser_c24451a, meadow_events_a078a8b):
    meadow_args_8349d53 = meadow_events_a078a8b[0].values
    return meadow_BscFchmod(meadow_events_a078a8b, meadow_args_8349d53[0], meadow_serialize_stat_flags(meadow_args_8349d53[1]), meadow_serialize_result(meadow_events_a078a8b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_96f08da', 'events': 'meadow_events_93103ed'}, 'handle_setreuid')
def meadow_handle_setreuid(meadow_parser_96f08da, meadow_events_93103ed):
    meadow_args_d957c0d = meadow_events_93103ed[0].values
    return meadow_BscSetreuid(meadow_events_93103ed, meadow_args_d957c0d[0], meadow_args_d957c0d[1], meadow_serialize_result(meadow_events_93103ed[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_54934bc', 'events': 'meadow_events_45faeff'}, 'handle_setregid')
def meadow_handle_setregid(meadow_parser_54934bc, meadow_events_45faeff):
    meadow_args_22ca108 = meadow_events_45faeff[0].values
    return meadow_BscSetregid(meadow_events_45faeff, meadow_args_22ca108[0], meadow_args_22ca108[1], meadow_serialize_result(meadow_events_45faeff[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1e3ca2b', 'events': 'meadow_events_d66f648'}, 'handle_rename')
def meadow_handle_rename(meadow_parser_1e3ca2b, meadow_events_d66f648):
    meadow_old_vnode_aa18a9c = _name_boundary.attributes(meadow_parser_1e3ca2b)['parse_vnode'](meadow_events_d66f648)
    meadow_new_vnode_4f27cfd = _name_boundary.attributes(meadow_parser_1e3ca2b)['parse_vnode']([meadow_e_4708eb3 for meadow_e_4708eb3 in meadow_events_d66f648 if meadow_e_4708eb3 not in meadow_old_vnode_aa18a9c.ktraces])
    return meadow_BscRename(meadow_events_d66f648, meadow_old_vnode_aa18a9c.path, meadow_new_vnode_4f27cfd.path, meadow_serialize_result(meadow_events_d66f648[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9e5964b', 'events': 'meadow_events_5403cad'}, 'handle_sys_flock')
def meadow_handle_sys_flock(meadow_parser_9e5964b, meadow_events_5403cad):
    meadow_args_69837a6 = meadow_events_5403cad[0].values
    meadow_operations_d3148cc = [meadow_op_e8bc8c3 for meadow_op_e8bc8c3 in list(meadow_FlockOperation) if meadow_args_69837a6[1] & meadow_op_e8bc8c3.value]
    return meadow_BscSysFlock(meadow_events_5403cad, meadow_args_69837a6[0], meadow_operations_d3148cc, meadow_serialize_result(meadow_events_5403cad[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_eab38c3', 'events': 'meadow_events_7d487ba'}, 'handle_mkfifo')
def meadow_handle_mkfifo(meadow_parser_eab38c3, meadow_events_7d487ba):
    meadow_args_67e4c9b = meadow_events_7d487ba[0].values
    return meadow_BscMkfifo(meadow_events_7d487ba, _name_boundary.attributes(meadow_parser_eab38c3)['parse_vnode'](meadow_events_7d487ba).path, meadow_serialize_stat_flags(meadow_args_67e4c9b[1]), meadow_serialize_result(meadow_events_7d487ba[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_03cdab8', 'events': 'meadow_events_8e6e4f8', 'no_cancel': 'meadow_no_cancel_2696702'}, 'handle_sendto')
def meadow_handle_sendto(meadow_parser_03cdab8, meadow_events_8e6e4f8, meadow_no_cancel_2696702=False):
    meadow_args_6b6347f = meadow_events_8e6e4f8[0].values
    return meadow_BscSendto(meadow_events_8e6e4f8, meadow_args_6b6347f[0], meadow_args_6b6347f[1], meadow_args_6b6347f[2], meadow_args_6b6347f[3], meadow_serialize_result(meadow_events_8e6e4f8[-1], 'count'), meadow_no_cancel_2696702)

@_name_boundary.callable_contract({'parser': 'meadow_parser_d33455b', 'events': 'meadow_events_fc53c3f'}, 'handle_shutdown')
def meadow_handle_shutdown(meadow_parser_d33455b, meadow_events_fc53c3f):
    meadow_args_00d605d = meadow_events_fc53c3f[0].values
    return meadow_BscShutdown(meadow_events_fc53c3f, meadow_args_00d605d[0], meadow_args_00d605d[1], meadow_serialize_result(meadow_events_fc53c3f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_263e992', 'events': 'meadow_events_740b0f3'}, 'handle_socketpair')
def meadow_handle_socketpair(meadow_parser_263e992, meadow_events_740b0f3):
    meadow_args_e99682e = meadow_events_740b0f3[0].values
    return meadow_BscSocketpair(meadow_events_740b0f3, meadow_socket.AddressFamily(meadow_args_e99682e[0]), meadow_socket.SocketKind(meadow_args_e99682e[1]), meadow_args_e99682e[2], meadow_args_e99682e[3], meadow_serialize_result(meadow_events_740b0f3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cda5f6b', 'events': 'meadow_events_82e1d98'}, 'handle_mkdir')
def meadow_handle_mkdir(meadow_parser_cda5f6b, meadow_events_82e1d98):
    meadow_args_4a80f7d = meadow_events_82e1d98[0].values
    return meadow_BscMkdir(meadow_events_82e1d98, _name_boundary.attributes(meadow_parser_cda5f6b)['parse_vnode'](meadow_events_82e1d98).path, meadow_serialize_stat_flags(meadow_args_4a80f7d[1]), meadow_serialize_result(meadow_events_82e1d98[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c4e6071', 'events': 'meadow_events_cd4c6a3'}, 'handle_rmdir')
def meadow_handle_rmdir(meadow_parser_c4e6071, meadow_events_cd4c6a3):
    return meadow_BscRmdir(meadow_events_cd4c6a3, _name_boundary.attributes(meadow_parser_c4e6071)['parse_vnode'](meadow_events_cd4c6a3).path, meadow_serialize_result(meadow_events_cd4c6a3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9653853', 'events': 'meadow_events_d7f9418'}, 'handle_utimes')
def meadow_handle_utimes(meadow_parser_9653853, meadow_events_d7f9418):
    meadow_args_dd57080 = meadow_events_d7f9418[0].values
    return meadow_BscUtimes(meadow_events_d7f9418, _name_boundary.attributes(meadow_parser_9653853)['parse_vnode'](meadow_events_d7f9418).path, meadow_args_dd57080[1], meadow_serialize_result(meadow_events_d7f9418[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9f9d909', 'events': 'meadow_events_173269d'}, 'handle_futimes')
def meadow_handle_futimes(meadow_parser_9f9d909, meadow_events_173269d):
    meadow_args_ae38c12 = meadow_events_173269d[0].values
    return meadow_BscFutimes(meadow_events_173269d, meadow_args_ae38c12[0], meadow_args_ae38c12[1], meadow_serialize_result(meadow_events_173269d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d521a39', 'events': 'meadow_events_9aebbb7'}, 'handle_adjtime')
def meadow_handle_adjtime(meadow_parser_d521a39, meadow_events_9aebbb7):
    meadow_args_2a13824 = meadow_events_9aebbb7[0].values
    return meadow_BscAdjtime(meadow_events_9aebbb7, meadow_args_2a13824[0], meadow_args_2a13824[1], meadow_serialize_result(meadow_events_9aebbb7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e8a8e87', 'events': 'meadow_events_547cd05'}, 'handle_gethostuuid')
def meadow_handle_gethostuuid(meadow_parser_e8a8e87, meadow_events_547cd05):
    meadow_args_f3228e6 = meadow_events_547cd05[0].values
    return meadow_BscGethostuuid(meadow_events_547cd05, meadow_args_f3228e6[0], meadow_args_f3228e6[1], meadow_serialize_result(meadow_events_547cd05[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5ae8946', 'events': 'meadow_events_d5a1d6d'}, 'handle_obs_killpg')
def meadow_handle_obs_killpg(meadow_parser_5ae8946, meadow_events_d5a1d6d):
    return meadow_BscObsKillpg(meadow_events_d5a1d6d, meadow_events_d5a1d6d[0].values[0], meadow_events_d5a1d6d[0].values[1], meadow_serialize_result(meadow_events_d5a1d6d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d217a13', 'events': 'meadow_events_34c1e75'}, 'handle_setsid')
def meadow_handle_setsid(meadow_parser_d217a13, meadow_events_34c1e75):
    return meadow_BscSetsid(meadow_events_34c1e75, meadow_serialize_result(meadow_events_34c1e75[-1], 'gid'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f9c44ee', 'events': 'meadow_events_06dc8fe'}, 'handle_getpgid')
def meadow_handle_getpgid(meadow_parser_f9c44ee, meadow_events_06dc8fe):
    return meadow_BscGetpgid(meadow_events_06dc8fe, meadow_events_06dc8fe[0].values[0], meadow_serialize_result(meadow_events_06dc8fe[-1], 'gid'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c93876b', 'events': 'meadow_events_89334a1'}, 'handle_setprivexec')
def meadow_handle_setprivexec(meadow_parser_c93876b, meadow_events_89334a1):
    return meadow_BscSetprivexec(meadow_events_89334a1, meadow_events_89334a1[0].values[0], meadow_serialize_result(meadow_events_89334a1[-1], 'previous'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cb92481', 'events': 'meadow_events_82d549b', 'no_cancel': 'meadow_no_cancel_dc76d8a'}, 'handle_pread')
def meadow_handle_pread(meadow_parser_cb92481, meadow_events_82d549b, meadow_no_cancel_dc76d8a=False):
    meadow_result_85fe6b6 = meadow_serialize_result(meadow_events_82d549b[-1], 'count')
    meadow_args_1116637 = meadow_events_82d549b[0].values
    return meadow_BscPread(meadow_events_82d549b, meadow_args_1116637[0], meadow_args_1116637[1], meadow_args_1116637[2], meadow_args_1116637[3], meadow_result_85fe6b6, meadow_no_cancel_dc76d8a)

@_name_boundary.callable_contract({'parser': 'meadow_parser_68e0cca', 'events': 'meadow_events_51d78f2', 'no_cancel': 'meadow_no_cancel_62f7bf1'}, 'handle_pwrite')
def meadow_handle_pwrite(meadow_parser_68e0cca, meadow_events_51d78f2, meadow_no_cancel_62f7bf1=False):
    meadow_result_5a5a4e1 = meadow_serialize_result(meadow_events_51d78f2[-1], 'count')
    meadow_args_f15f6f7 = meadow_events_51d78f2[0].values
    return meadow_BscPwrite(meadow_events_51d78f2, meadow_args_f15f6f7[0], meadow_args_f15f6f7[1], meadow_args_f15f6f7[2], meadow_args_f15f6f7[3], meadow_result_5a5a4e1, meadow_no_cancel_62f7bf1)

@_name_boundary.callable_contract({'parser': 'meadow_parser_65a9796', 'events': 'meadow_events_6bc9b50'}, 'handle_nfssvc')
def meadow_handle_nfssvc(meadow_parser_65a9796, meadow_events_6bc9b50):
    meadow_args_12b01bc = meadow_events_6bc9b50[0].values
    return meadow_BscNfssvc(meadow_events_6bc9b50, meadow_args_12b01bc[0], meadow_args_12b01bc[1], meadow_serialize_result(meadow_events_6bc9b50[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a578271', 'events': 'meadow_events_ccdd551'}, 'handle_statfs')
def meadow_handle_statfs(meadow_parser_a578271, meadow_events_ccdd551):
    meadow_args_9c63599 = meadow_events_ccdd551[0].values
    return meadow_BscStatfs(meadow_events_ccdd551, _name_boundary.attributes(meadow_parser_a578271)['parse_vnode'](meadow_events_ccdd551).path, meadow_args_9c63599[1], meadow_serialize_result(meadow_events_ccdd551[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d1a7b55', 'events': 'meadow_events_79f5eb2'}, 'handle_fstatfs')
def meadow_handle_fstatfs(meadow_parser_d1a7b55, meadow_events_79f5eb2):
    meadow_args_78a630e = meadow_events_79f5eb2[0].values
    return meadow_BscFstatfs(meadow_events_79f5eb2, meadow_args_78a630e[0], meadow_args_78a630e[1], meadow_serialize_result(meadow_events_79f5eb2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0f70616', 'events': 'meadow_events_718585b'}, 'handle_unmount')
def meadow_handle_unmount(meadow_parser_0f70616, meadow_events_718585b):
    meadow_args_9149542 = meadow_events_718585b[0].values
    return meadow_BscUnmount(meadow_events_718585b, _name_boundary.attributes(meadow_parser_0f70616)['parse_vnode'](meadow_events_718585b).path, meadow_args_9149542[1], meadow_serialize_result(meadow_events_718585b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_991c6b9', 'events': 'meadow_events_bfca4ac'}, 'handle_getfh')
def meadow_handle_getfh(meadow_parser_991c6b9, meadow_events_bfca4ac):
    meadow_args_ab1bc3e = meadow_events_bfca4ac[0].values
    return meadow_BscGetfh(meadow_events_bfca4ac, _name_boundary.attributes(meadow_parser_991c6b9)['parse_vnode'](meadow_events_bfca4ac).path, meadow_args_ab1bc3e[1], meadow_serialize_result(meadow_events_bfca4ac[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bae68bc', 'events': 'meadow_events_c2c2d76'}, 'handle_quotactl')
def meadow_handle_quotactl(meadow_parser_bae68bc, meadow_events_c2c2d76):
    meadow_args_6a0bacc = meadow_events_c2c2d76[0].values
    return meadow_BscQuotactl(meadow_events_c2c2d76, _name_boundary.attributes(meadow_parser_bae68bc)['parse_vnode'](meadow_events_c2c2d76).path, meadow_args_6a0bacc[1], meadow_args_6a0bacc[2], meadow_args_6a0bacc[3], meadow_serialize_result(meadow_events_c2c2d76[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2ec7cd3', 'events': 'meadow_events_b390900'}, 'handle_mount')
def meadow_handle_mount(meadow_parser_2ec7cd3, meadow_events_b390900):
    meadow_src_vnode_41d5757 = _name_boundary.attributes(meadow_parser_2ec7cd3)['parse_vnode'](meadow_events_b390900)
    meadow_dst_vnode_ca9af93 = _name_boundary.attributes(meadow_parser_2ec7cd3)['parse_vnode']([meadow_e_a461738 for meadow_e_a461738 in meadow_events_b390900 if meadow_e_a461738 not in meadow_src_vnode_41d5757.ktraces])
    meadow_args_e6bfeb2 = meadow_events_b390900[0].values
    return meadow_BscMount(meadow_events_b390900, meadow_src_vnode_41d5757.path, meadow_dst_vnode_ca9af93.path, meadow_args_e6bfeb2[2], meadow_args_e6bfeb2[3], meadow_serialize_result(meadow_events_b390900[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_73c4651', 'events': 'meadow_events_3ac7096'}, 'handle_csops')
def meadow_handle_csops(meadow_parser_73c4651, meadow_events_3ac7096):
    meadow_args_ad88431 = meadow_events_3ac7096[0].values
    return meadow_BscCsops(meadow_events_3ac7096, meadow_args_ad88431[0], meadow_CsopsOps(meadow_args_ad88431[1]), meadow_args_ad88431[2], meadow_args_ad88431[3], meadow_serialize_result(meadow_events_3ac7096[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_09582d7', 'events': 'meadow_events_aa3da00'}, 'handle_csops_audittoken')
def meadow_handle_csops_audittoken(meadow_parser_09582d7, meadow_events_aa3da00):
    meadow_args_82e5465 = meadow_events_aa3da00[0].values
    return meadow_BscCsopsAudittoken(meadow_events_aa3da00, meadow_args_82e5465[0], meadow_CsopsOps(meadow_args_82e5465[1]), meadow_args_82e5465[2], meadow_args_82e5465[3], meadow_serialize_result(meadow_events_aa3da00[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2039729', 'events': 'meadow_events_1eb3a95', 'no_cancel': 'meadow_no_cancel_bdf2c0f'}, 'handle_waitid')
def meadow_handle_waitid(meadow_parser_2039729, meadow_events_1eb3a95, meadow_no_cancel_bdf2c0f=False):
    meadow_args_c23379b = meadow_events_1eb3a95[0].values
    return meadow_BscWaitid(meadow_events_1eb3a95, meadow_args_c23379b[0], meadow_args_c23379b[1], meadow_args_c23379b[2], meadow_args_c23379b[3], meadow_serialize_result(meadow_events_1eb3a95[-1]), meadow_no_cancel_bdf2c0f)

@_name_boundary.callable_contract({'parser': 'meadow_parser_f350d1b', 'events': 'meadow_events_a000eb9'}, 'handle_kdebug_typefilter')
def meadow_handle_kdebug_typefilter(meadow_parser_f350d1b, meadow_events_a000eb9):
    meadow_args_9f59e53 = meadow_events_a000eb9[0].values
    return meadow_BscKdebugTypefilter(meadow_events_a000eb9, meadow_args_9f59e53[0], meadow_args_9f59e53[1], meadow_serialize_result(meadow_events_a000eb9[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_eec2811', 'events': 'meadow_events_b4c8ccb'}, 'handle_setgid')
def meadow_handle_setgid(meadow_parser_eec2811, meadow_events_b4c8ccb):
    meadow_args_248944a = meadow_events_b4c8ccb[0].values
    return meadow_BscSetgid(meadow_events_b4c8ccb, meadow_args_248944a[0], meadow_serialize_result(meadow_events_b4c8ccb[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4cf7d12', 'events': 'meadow_events_9789e4b'}, 'handle_setegid')
def meadow_handle_setegid(meadow_parser_4cf7d12, meadow_events_9789e4b):
    meadow_args_5c8fcf7 = meadow_events_9789e4b[0].values
    return meadow_BscSetegid(meadow_events_9789e4b, meadow_args_5c8fcf7[0], meadow_serialize_result(meadow_events_9789e4b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8e295ab', 'events': 'meadow_events_199f8a7'}, 'handle_seteuid')
def meadow_handle_seteuid(meadow_parser_8e295ab, meadow_events_199f8a7):
    meadow_args_b50e6f7 = meadow_events_199f8a7[0].values
    return meadow_BscSeteuid(meadow_events_199f8a7, meadow_args_b50e6f7[0], meadow_serialize_result(meadow_events_199f8a7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_111e9b6', 'events': 'meadow_events_2cbc3e9'}, 'handle_thread_selfcounts')
def meadow_handle_thread_selfcounts(meadow_parser_111e9b6, meadow_events_2cbc3e9):
    meadow_args_2a3b9b7 = meadow_events_2cbc3e9[0].values
    return meadow_BscThreadSelfcounts(meadow_events_2cbc3e9, meadow_args_2a3b9b7[0], meadow_args_2a3b9b7[1], meadow_args_2a3b9b7[2], meadow_serialize_result(meadow_events_2cbc3e9[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e799618', 'events': 'meadow_events_355ce1f'}, 'handle_fdatasync')
def meadow_handle_fdatasync(meadow_parser_e799618, meadow_events_355ce1f):
    meadow_args_4164efa = meadow_events_355ce1f[0].values
    return meadow_BscFdatasync(meadow_events_355ce1f, meadow_args_4164efa[0], meadow_serialize_result(meadow_events_355ce1f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5c8523c', 'events': 'meadow_events_3831f8f'}, 'handle_pathconf')
def meadow_handle_pathconf(meadow_parser_5c8523c, meadow_events_3831f8f):
    meadow_args_1ebbd0d = meadow_events_3831f8f[0].values
    return meadow_BscPathconf(meadow_events_3831f8f, _name_boundary.attributes(meadow_parser_5c8523c)['parse_vnode'](meadow_events_3831f8f).path, meadow_args_1ebbd0d[1], meadow_serialize_result(meadow_events_3831f8f[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_695ce55', 'events': 'meadow_events_e40deb4'}, 'handle_sys_fpathconf')
def meadow_handle_sys_fpathconf(meadow_parser_695ce55, meadow_events_e40deb4):
    meadow_args_eb5de03 = meadow_events_e40deb4[0].values
    return meadow_BscSysFpathconf(meadow_events_e40deb4, meadow_args_eb5de03[0], meadow_args_eb5de03[1], meadow_serialize_result(meadow_events_e40deb4[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_63e2601', 'events': 'meadow_events_3b9aad7'}, 'handle_getrlimit')
def meadow_handle_getrlimit(meadow_parser_63e2601, meadow_events_3b9aad7):
    meadow_args_1576130 = meadow_events_3b9aad7[0].values
    return meadow_BscGetrlimit(meadow_events_3b9aad7, meadow_args_1576130[0], meadow_args_1576130[1], meadow_serialize_result(meadow_events_3b9aad7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_349fed7', 'events': 'meadow_events_e4ce20a'}, 'handle_setrlimit')
def meadow_handle_setrlimit(meadow_parser_349fed7, meadow_events_e4ce20a):
    meadow_args_b3ea8d7 = meadow_events_e4ce20a[0].values
    return meadow_BscSetrlimit(meadow_events_e4ce20a, meadow_args_b3ea8d7[0], meadow_args_b3ea8d7[1], meadow_serialize_result(meadow_events_e4ce20a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_11f8af3', 'events': 'meadow_events_fbc9018'}, 'handle_getdirentries')
def meadow_handle_getdirentries(meadow_parser_11f8af3, meadow_events_fbc9018):
    meadow_args_ea116fd = meadow_events_fbc9018[0].values
    return meadow_BscGetdirentries(meadow_events_fbc9018, meadow_args_ea116fd[0], meadow_args_ea116fd[1], meadow_args_ea116fd[2], meadow_args_ea116fd[3], meadow_serialize_result(meadow_events_fbc9018[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_72f752b', 'events': 'meadow_events_50c979e'}, 'handle_mmap')
def meadow_handle_mmap(meadow_parser_72f752b, meadow_events_50c979e):
    meadow_args_fffc216 = meadow_events_50c979e[0].values
    return meadow_BscMmap(meadow_events_50c979e, meadow_args_fffc216[0], meadow_args_fffc216[1], meadow_args_fffc216[2], meadow_args_fffc216[3], meadow_serialize_result(meadow_events_50c979e[-1], 'count', hex))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7ffcc4a', 'events': 'meadow_events_4eea0f8'}, 'handle_lseek')
def meadow_handle_lseek(meadow_parser_7ffcc4a, meadow_events_4eea0f8):
    meadow_args_f05be00 = meadow_events_4eea0f8[0].values
    return meadow_BscLseek(meadow_events_4eea0f8, meadow_args_f05be00[0], meadow_ctypes.c_int64(meadow_args_f05be00[1]).value, meadow_args_f05be00[2], meadow_serialize_result(meadow_events_4eea0f8[-1], 'count', lambda meadow_x_8bff8f0: meadow_ctypes.c_int64(meadow_x_8bff8f0).value))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d784890', 'events': 'meadow_events_b66f6af'}, 'handle_truncate')
def meadow_handle_truncate(meadow_parser_d784890, meadow_events_b66f6af):
    meadow_args_e8540e8 = meadow_events_b66f6af[0].values
    return meadow_BscTruncate(meadow_events_b66f6af, _name_boundary.attributes(meadow_parser_d784890)['parse_vnode'](meadow_events_b66f6af).path, meadow_args_e8540e8[1], meadow_serialize_result(meadow_events_b66f6af[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_dc24745', 'events': 'meadow_events_a28e541'}, 'handle_ftruncate')
def meadow_handle_ftruncate(meadow_parser_dc24745, meadow_events_a28e541):
    meadow_args_f80c3c5 = meadow_events_a28e541[0].values
    return meadow_BscFtruncate(meadow_events_a28e541, meadow_args_f80c3c5[0], meadow_args_f80c3c5[1], meadow_serialize_result(meadow_events_a28e541[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1624a9f', 'events': 'meadow_events_a0053fa'}, 'handle_sysctl')
def meadow_handle_sysctl(meadow_parser_1624a9f, meadow_events_a0053fa):
    meadow_args_e54f34d = meadow_events_a0053fa[0].values
    return meadow_BscSysctl(meadow_events_a0053fa, meadow_args_e54f34d[0], meadow_args_e54f34d[1], meadow_args_e54f34d[2], meadow_args_e54f34d[3], meadow_serialize_result(meadow_events_a0053fa[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_fa451cf', 'events': 'meadow_events_edd1fa5'}, 'handle_mlock')
def meadow_handle_mlock(meadow_parser_fa451cf, meadow_events_edd1fa5):
    meadow_args_bfa5ab7 = meadow_events_edd1fa5[0].values
    return meadow_BscMlock(meadow_events_edd1fa5, meadow_args_bfa5ab7[0], meadow_args_bfa5ab7[1], meadow_serialize_result(meadow_events_edd1fa5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d5c0d0f', 'events': 'meadow_events_e5a43a2'}, 'handle_munlock')
def meadow_handle_munlock(meadow_parser_d5c0d0f, meadow_events_e5a43a2):
    meadow_args_80b5314 = meadow_events_e5a43a2[0].values
    return meadow_BscMunlock(meadow_events_e5a43a2, meadow_args_80b5314[0], meadow_args_80b5314[1], meadow_serialize_result(meadow_events_e5a43a2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_111da10', 'events': 'meadow_events_503aee2'}, 'handle_undelete')
def meadow_handle_undelete(meadow_parser_111da10, meadow_events_503aee2):
    return meadow_BscUndelete(meadow_events_503aee2, _name_boundary.attributes(meadow_parser_111da10)['parse_vnode'](meadow_events_503aee2).path, meadow_serialize_result(meadow_events_503aee2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9ec6d98', 'events': 'meadow_events_b11f754'}, 'handle_open_dprotected_np')
def meadow_handle_open_dprotected_np(meadow_parser_9ec6d98, meadow_events_b11f754):
    meadow_args_1ece096 = meadow_events_b11f754[0].values
    return meadow_BscOpenDprotectedNp(meadow_events_b11f754, _name_boundary.attributes(meadow_parser_9ec6d98)['parse_vnode'](meadow_events_b11f754).path, meadow_serialize_open_flags(meadow_args_1ece096[1]), meadow_args_1ece096[2], meadow_args_1ece096[3], meadow_serialize_result(meadow_events_b11f754[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_de69fec', 'events': 'meadow_events_4878cfa'}, 'handle_getattrlist')
def meadow_handle_getattrlist(meadow_parser_de69fec, meadow_events_4878cfa):
    meadow_args_bede8fe = meadow_events_4878cfa[0].values
    return meadow_BscGetattrlist(meadow_events_4878cfa, _name_boundary.attributes(meadow_parser_de69fec)['parse_vnode'](meadow_events_4878cfa).path, meadow_args_bede8fe[1], meadow_args_bede8fe[2], meadow_args_bede8fe[3], meadow_serialize_result(meadow_events_4878cfa[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_fad2bf9', 'events': 'meadow_events_f03a386'}, 'handle_setattrlist')
def meadow_handle_setattrlist(meadow_parser_fad2bf9, meadow_events_f03a386):
    meadow_args_213823d = meadow_events_f03a386[0].values
    return meadow_BscSetattrlist(meadow_events_f03a386, _name_boundary.attributes(meadow_parser_fad2bf9)['parse_vnode'](meadow_events_f03a386).path, meadow_args_213823d[1], meadow_args_213823d[2], meadow_args_213823d[3], meadow_serialize_result(meadow_events_f03a386[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_87b791b', 'events': 'meadow_events_2978637'}, 'handle_getdirentriesattr')
def meadow_handle_getdirentriesattr(meadow_parser_87b791b, meadow_events_2978637):
    meadow_args_62b5246 = meadow_events_2978637[0].values
    return meadow_BscGetdirentriesattr(meadow_events_2978637, meadow_args_62b5246[0], meadow_args_62b5246[1], meadow_args_62b5246[2], meadow_args_62b5246[3], meadow_serialize_result(meadow_events_2978637[-1], 'last entry'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_10167c5', 'events': 'meadow_events_ba8bade'}, 'handle_exchangedata')
def meadow_handle_exchangedata(meadow_parser_10167c5, meadow_events_ba8bade):
    meadow_vnode1_89fff29 = _name_boundary.attributes(meadow_parser_10167c5)['parse_vnode'](meadow_events_ba8bade)
    meadow_vnode2_eeb3ac2 = _name_boundary.attributes(meadow_parser_10167c5)['parse_vnode']([meadow_e_2b0668f for meadow_e_2b0668f in meadow_events_ba8bade if meadow_e_2b0668f not in meadow_vnode1_89fff29.ktraces])
    meadow_args_6fe4f75 = meadow_events_ba8bade[0].values
    return meadow_BscExchangedata(meadow_events_ba8bade, meadow_vnode1_89fff29.path, meadow_vnode2_eeb3ac2.path, meadow_args_6fe4f75[2], meadow_serialize_result(meadow_events_ba8bade[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a5f0db7', 'events': 'meadow_events_e38b502'}, 'handle_searchfs')
def meadow_handle_searchfs(meadow_parser_a5f0db7, meadow_events_e38b502):
    meadow_vnode_fd87140 = _name_boundary.attributes(meadow_parser_a5f0db7)['parse_vnode'](meadow_events_e38b502)
    meadow_args_2cef032 = meadow_events_e38b502[0].values
    return meadow_BscSearchfs(meadow_events_e38b502, meadow_vnode_fd87140.path, meadow_args_2cef032[1], meadow_args_2cef032[2], meadow_args_2cef032[3], meadow_serialize_result(meadow_events_e38b502[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a86d98a', 'events': 'meadow_events_9787f51'}, 'handle_fgetattrlist')
def meadow_handle_fgetattrlist(meadow_parser_a86d98a, meadow_events_9787f51):
    meadow_args_4269aba = meadow_events_9787f51[0].values
    return meadow_BscFgetattrlist(meadow_events_9787f51, meadow_args_4269aba[0], meadow_args_4269aba[1], meadow_args_4269aba[2], meadow_args_4269aba[3], meadow_serialize_result(meadow_events_9787f51[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_eccd3cd', 'events': 'meadow_events_406dd45'}, 'handle_fsetattrlist')
def meadow_handle_fsetattrlist(meadow_parser_eccd3cd, meadow_events_406dd45):
    meadow_args_3238e4f = meadow_events_406dd45[0].values
    return meadow_BscFsetattrlist(meadow_events_406dd45, meadow_args_3238e4f[0], meadow_args_3238e4f[1], meadow_args_3238e4f[2], meadow_args_3238e4f[3], meadow_serialize_result(meadow_events_406dd45[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6549db9', 'events': 'meadow_events_d7b8db9', 'no_cancel': 'meadow_no_cancel_f59dea9'}, 'handle_poll')
def meadow_handle_poll(meadow_parser_6549db9, meadow_events_d7b8db9, meadow_no_cancel_f59dea9=False):
    meadow_args_4c560de = meadow_events_d7b8db9[0].values
    return meadow_BscPoll(meadow_events_d7b8db9, meadow_args_4c560de[0], meadow_args_4c560de[1], meadow_args_4c560de[2], meadow_serialize_result(meadow_events_d7b8db9[-1], 'count'), meadow_no_cancel_f59dea9)

@_name_boundary.callable_contract({'parser': 'meadow_parser_14aa18d', 'events': 'meadow_events_1448c0d'}, 'handle_getxattr')
def meadow_handle_getxattr(meadow_parser_14aa18d, meadow_events_1448c0d):
    meadow_args_0d68891 = meadow_events_1448c0d[0].values
    return meadow_BscGetxattr(meadow_events_1448c0d, _name_boundary.attributes(meadow_parser_14aa18d)['parse_vnode'](meadow_events_1448c0d).path, meadow_args_0d68891[1], meadow_args_0d68891[2], meadow_args_0d68891[3], meadow_serialize_result(meadow_events_1448c0d[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ce5d134', 'events': 'meadow_events_ea7bc3d'}, 'handle_fgetxattr')
def meadow_handle_fgetxattr(meadow_parser_ce5d134, meadow_events_ea7bc3d):
    meadow_args_4554485 = meadow_events_ea7bc3d[0].values
    return meadow_BscFgetxattr(meadow_events_ea7bc3d, meadow_args_4554485[0], meadow_args_4554485[1], meadow_args_4554485[2], meadow_args_4554485[3], meadow_serialize_result(meadow_events_ea7bc3d[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_55c86b4', 'events': 'meadow_events_a53fb63'}, 'handle_setxattr')
def meadow_handle_setxattr(meadow_parser_55c86b4, meadow_events_a53fb63):
    meadow_args_44f698a = meadow_events_a53fb63[0].values
    return meadow_BscSetxattr(meadow_events_a53fb63, _name_boundary.attributes(meadow_parser_55c86b4)['parse_vnode'](meadow_events_a53fb63).path, meadow_args_44f698a[1], meadow_args_44f698a[2], meadow_args_44f698a[3], meadow_serialize_result(meadow_events_a53fb63[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_78017e4', 'events': 'meadow_events_f2ea5b1'}, 'handle_fsetxattr')
def meadow_handle_fsetxattr(meadow_parser_78017e4, meadow_events_f2ea5b1):
    meadow_args_56b8e2d = meadow_events_f2ea5b1[0].values
    return meadow_BscFsetxattr(meadow_events_f2ea5b1, meadow_args_56b8e2d[0], meadow_args_56b8e2d[1], meadow_args_56b8e2d[2], meadow_args_56b8e2d[3], meadow_serialize_result(meadow_events_f2ea5b1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b570c22', 'events': 'meadow_events_aba3f1e'}, 'handle_removexattr')
def meadow_handle_removexattr(meadow_parser_b570c22, meadow_events_aba3f1e):
    meadow_args_69011eb = meadow_events_aba3f1e[0].values
    return meadow_BscRemovexattr(meadow_events_aba3f1e, _name_boundary.attributes(meadow_parser_b570c22)['parse_vnode'](meadow_events_aba3f1e).path, meadow_args_69011eb[1], meadow_args_69011eb[2], meadow_serialize_result(meadow_events_aba3f1e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4d3a24d', 'events': 'meadow_events_6292ba6'}, 'handle_fremovexattr')
def meadow_handle_fremovexattr(meadow_parser_4d3a24d, meadow_events_6292ba6):
    meadow_args_90957ee = meadow_events_6292ba6[0].values
    return meadow_BscFremovexattr(meadow_events_6292ba6, meadow_args_90957ee[0], meadow_args_90957ee[1], meadow_args_90957ee[2], meadow_serialize_result(meadow_events_6292ba6[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6b72e1d', 'events': 'meadow_events_f519dfc'}, 'handle_listxattr')
def meadow_handle_listxattr(meadow_parser_6b72e1d, meadow_events_f519dfc):
    meadow_args_7f29878 = meadow_events_f519dfc[0].values
    return meadow_BscListxattr(meadow_events_f519dfc, _name_boundary.attributes(meadow_parser_6b72e1d)['parse_vnode'](meadow_events_f519dfc).path, meadow_args_7f29878[1], meadow_args_7f29878[2], meadow_args_7f29878[3], meadow_serialize_result(meadow_events_f519dfc[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4a7f7af', 'events': 'meadow_events_52605c9'}, 'handle_flistxattr')
def meadow_handle_flistxattr(meadow_parser_4a7f7af, meadow_events_52605c9):
    meadow_args_eadd82f = meadow_events_52605c9[0].values
    return meadow_BscFlistxattr(meadow_events_52605c9, meadow_args_eadd82f[0], meadow_args_eadd82f[1], meadow_args_eadd82f[2], meadow_args_eadd82f[3], meadow_serialize_result(meadow_events_52605c9[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_32dff90', 'events': 'meadow_events_ec7da11'}, 'handle_fsctl')
def meadow_handle_fsctl(meadow_parser_32dff90, meadow_events_ec7da11):
    meadow_args_141f9b4 = meadow_events_ec7da11[0].values
    return meadow_BscFsctl(meadow_events_ec7da11, _name_boundary.attributes(meadow_parser_32dff90)['parse_vnode'](meadow_events_ec7da11).path, meadow_args_141f9b4[1], meadow_args_141f9b4[2], meadow_args_141f9b4[3], meadow_serialize_result(meadow_events_ec7da11[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2d202d6', 'events': 'meadow_events_a6f7686'}, 'handle_initgroups')
def meadow_handle_initgroups(meadow_parser_2d202d6, meadow_events_a6f7686):
    meadow_args_377f527 = meadow_events_a6f7686[0].values
    return meadow_BscInitgroups(meadow_events_a6f7686, meadow_args_377f527[0], meadow_args_377f527[1], meadow_serialize_result(meadow_events_a6f7686[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_3cdb765', 'events': 'meadow_events_74f33ff'}, 'handle_posix_spawn')
def meadow_handle_posix_spawn(meadow_parser_3cdb765, meadow_events_74f33ff):
    meadow_vnodes_ae68e20 = _name_boundary.attributes(meadow_parser_3cdb765)['parse_vnodes'](meadow_events_74f33ff)
    if len(meadow_vnodes_ae68e20) >= 6:
        meadow_stdin_57be813, meadow_stdout_ce7b9bc, meadow_stderr_20aca0d = (meadow_vnodes_ae68e20[0].path, meadow_vnodes_ae68e20[1].path, meadow_vnodes_ae68e20[2].path)
        meadow_path_30f8efc = meadow_vnodes_ae68e20[3].path
    else:
        meadow_stdin_57be813, meadow_stdout_ce7b9bc, meadow_stderr_20aca0d = (None, None, None)
        meadow_path_30f8efc = meadow_vnodes_ae68e20[0].path
    meadow_args_29bcd24 = meadow_events_74f33ff[0].values
    return meadow_BscPosixSpawn(meadow_events_74f33ff, meadow_args_29bcd24[0], meadow_path_30f8efc, meadow_args_29bcd24[2], meadow_args_29bcd24[3], meadow_stdin_57be813, meadow_stdout_ce7b9bc, meadow_stderr_20aca0d, meadow_serialize_result(meadow_events_74f33ff[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bdc5fe6', 'events': 'meadow_events_c1b0218'}, 'handle_ffsctl')
def meadow_handle_ffsctl(meadow_parser_bdc5fe6, meadow_events_c1b0218):
    meadow_args_860d473 = meadow_events_c1b0218[0].values
    return meadow_BscFfsctl(meadow_events_c1b0218, meadow_args_860d473[0], meadow_args_860d473[1], meadow_args_860d473[2], meadow_args_860d473[3], meadow_serialize_result(meadow_events_c1b0218[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_02bd2da', 'events': 'meadow_events_7783fc1'}, 'handle_nfsclnt')
def meadow_handle_nfsclnt(meadow_parser_02bd2da, meadow_events_7783fc1):
    meadow_args_8b79629 = meadow_events_7783fc1[0].values
    return meadow_BscNfsclnt(meadow_events_7783fc1, meadow_args_8b79629[0], meadow_args_8b79629[1], meadow_serialize_result(meadow_events_7783fc1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9168edc', 'events': 'meadow_events_7349a3c'}, 'handle_fhopen')
def meadow_handle_fhopen(meadow_parser_9168edc, meadow_events_7349a3c):
    meadow_args_9752248 = meadow_events_7349a3c[0].values
    return meadow_BscFhopen(meadow_events_7349a3c, meadow_args_9752248[0], meadow_args_9752248[1], meadow_serialize_result(meadow_events_7349a3c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d21fe66', 'events': 'meadow_events_b564d03'}, 'handle_minherit')
def meadow_handle_minherit(meadow_parser_d21fe66, meadow_events_b564d03):
    meadow_args_83006ff = meadow_events_b564d03[0].values
    return meadow_BscMinherit(meadow_events_b564d03, meadow_args_83006ff[0], meadow_args_83006ff[1], meadow_args_83006ff[2], meadow_serialize_result(meadow_events_b564d03[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_3e260d9', 'events': 'meadow_events_aadde98'}, 'handle_semsys')
def meadow_handle_semsys(meadow_parser_3e260d9, meadow_events_aadde98):
    meadow_args_a8392b7 = meadow_events_aadde98[0].values
    return meadow_BscSemsys(meadow_events_aadde98, meadow_args_a8392b7[0], meadow_args_a8392b7[1], meadow_args_a8392b7[2], meadow_args_a8392b7[3], meadow_serialize_result(meadow_events_aadde98[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ef04b84', 'events': 'meadow_events_b7f1104'}, 'handle_msgsys')
def meadow_handle_msgsys(meadow_parser_ef04b84, meadow_events_b7f1104):
    meadow_args_fb01b57 = meadow_events_b7f1104[0].values
    return meadow_BscMsgsys(meadow_events_b7f1104, meadow_args_fb01b57[0], meadow_args_fb01b57[1], meadow_args_fb01b57[2], meadow_args_fb01b57[3], meadow_serialize_result(meadow_events_b7f1104[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_26a6ec5', 'events': 'meadow_events_9674dcb'}, 'handle_shmsys')
def meadow_handle_shmsys(meadow_parser_26a6ec5, meadow_events_9674dcb):
    meadow_args_80616b7 = meadow_events_9674dcb[0].values
    return meadow_BscShmsys(meadow_events_9674dcb, meadow_args_80616b7[0], meadow_args_80616b7[1], meadow_args_80616b7[2], meadow_args_80616b7[3], meadow_serialize_result(meadow_events_9674dcb[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d89afe3', 'events': 'meadow_events_67655c2'}, 'handle_semctl')
def meadow_handle_semctl(meadow_parser_d89afe3, meadow_events_67655c2):
    meadow_args_07df5bb = meadow_events_67655c2[0].values
    return meadow_BscSemctl(meadow_events_67655c2, meadow_args_07df5bb[0], meadow_args_07df5bb[1], meadow_args_07df5bb[2], meadow_args_07df5bb[3], meadow_serialize_result(meadow_events_67655c2[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_96bbc2b', 'events': 'meadow_events_8cc8b4f'}, 'handle_semget')
def meadow_handle_semget(meadow_parser_96bbc2b, meadow_events_8cc8b4f):
    meadow_args_caa96e2 = meadow_events_8cc8b4f[0].values
    return meadow_BscSemget(meadow_events_8cc8b4f, meadow_args_caa96e2[0], meadow_args_caa96e2[1], meadow_args_caa96e2[2], meadow_serialize_result(meadow_events_8cc8b4f[-1], 'id'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a6a4e50', 'events': 'meadow_events_efe1c12'}, 'handle_semop')
def meadow_handle_semop(meadow_parser_a6a4e50, meadow_events_efe1c12):
    meadow_args_ad47db6 = meadow_events_efe1c12[0].values
    return meadow_BscSemop(meadow_events_efe1c12, meadow_args_ad47db6[0], meadow_args_ad47db6[1], meadow_args_ad47db6[2], meadow_serialize_result(meadow_events_efe1c12[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cf9ad42', 'events': 'meadow_events_596f34b'}, 'handle_msgctl')
def meadow_handle_msgctl(meadow_parser_cf9ad42, meadow_events_596f34b):
    meadow_args_ec682b1 = meadow_events_596f34b[0].values
    return meadow_BscMsgctl(meadow_events_596f34b, meadow_args_ec682b1[0], meadow_args_ec682b1[1], meadow_args_ec682b1[2], meadow_serialize_result(meadow_events_596f34b[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f654ef0', 'events': 'meadow_events_930a096'}, 'handle_msgget')
def meadow_handle_msgget(meadow_parser_f654ef0, meadow_events_930a096):
    meadow_args_f9a0340 = meadow_events_930a096[0].values
    return meadow_BscMsgget(meadow_events_930a096, meadow_args_f9a0340[0], meadow_args_f9a0340[1], meadow_serialize_result(meadow_events_930a096[-1], 'id'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b9a9c63', 'events': 'meadow_events_ace2d3a', 'no_cancel': 'meadow_no_cancel_f5d47b6'}, 'handle_msgsnd')
def meadow_handle_msgsnd(meadow_parser_b9a9c63, meadow_events_ace2d3a, meadow_no_cancel_f5d47b6=False):
    meadow_args_81b163f = meadow_events_ace2d3a[0].values
    return meadow_BscMsgsnd(meadow_events_ace2d3a, meadow_args_81b163f[0], meadow_args_81b163f[1], meadow_args_81b163f[2], meadow_args_81b163f[3], meadow_serialize_result(meadow_events_ace2d3a[-1], 'count'), meadow_no_cancel_f5d47b6)

@_name_boundary.callable_contract({'parser': 'meadow_parser_d4c0cf5', 'events': 'meadow_events_75c7367', 'no_cancel': 'meadow_no_cancel_133f4d4'}, 'handle_msgrcv')
def meadow_handle_msgrcv(meadow_parser_d4c0cf5, meadow_events_75c7367, meadow_no_cancel_133f4d4=False):
    meadow_args_a9660b0 = meadow_events_75c7367[0].values
    return meadow_BscMsgrcv(meadow_events_75c7367, meadow_args_a9660b0[0], meadow_args_a9660b0[1], meadow_args_a9660b0[2], meadow_args_a9660b0[3], meadow_serialize_result(meadow_events_75c7367[-1], 'count'), meadow_no_cancel_133f4d4)

@_name_boundary.callable_contract({'parser': 'meadow_parser_60d4049', 'events': 'meadow_events_487db70'}, 'handle_shmat')
def meadow_handle_shmat(meadow_parser_60d4049, meadow_events_487db70):
    meadow_args_80fd99c = meadow_events_487db70[0].values
    return meadow_BscShmat(meadow_events_487db70, meadow_args_80fd99c[0], meadow_args_80fd99c[1], meadow_args_80fd99c[2], meadow_serialize_result(meadow_events_487db70[-1], 'address'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_70e6b4e', 'events': 'meadow_events_1524f3c'}, 'handle_shmctl')
def meadow_handle_shmctl(meadow_parser_70e6b4e, meadow_events_1524f3c):
    meadow_args_729bc61 = meadow_events_1524f3c[0].values
    return meadow_BscShmctl(meadow_events_1524f3c, meadow_args_729bc61[0], meadow_args_729bc61[1], meadow_args_729bc61[2], meadow_serialize_result(meadow_events_1524f3c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6155d64', 'events': 'meadow_events_9166945'}, 'handle_shmdt')
def meadow_handle_shmdt(meadow_parser_6155d64, meadow_events_9166945):
    meadow_args_e3dbf3c = meadow_events_9166945[0].values
    return meadow_BscShmdt(meadow_events_9166945, meadow_args_e3dbf3c[0], meadow_serialize_result(meadow_events_9166945[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8ef72cb', 'events': 'meadow_events_794fbf5'}, 'handle_shmget')
def meadow_handle_shmget(meadow_parser_8ef72cb, meadow_events_794fbf5):
    meadow_args_8289e31 = meadow_events_794fbf5[0].values
    return meadow_BscShmget(meadow_events_794fbf5, meadow_args_8289e31[0], meadow_args_8289e31[1], meadow_args_8289e31[2], meadow_serialize_result(meadow_events_794fbf5[-1], 'id'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cde9ea3', 'events': 'meadow_events_0296c5a'}, 'handle_shm_open')
def meadow_handle_shm_open(meadow_parser_cde9ea3, meadow_events_0296c5a):
    meadow_args_90bd77d = meadow_events_0296c5a[0].values
    meadow_oflags_0914af9 = meadow_serialize_open_flags(meadow_args_90bd77d[1])
    meadow_sflags_808e6a2 = meadow_serialize_stat_flags(meadow_args_90bd77d[2]) if meadow_BscOpenFlags.O_CREAT in meadow_oflags_0914af9 else []
    return meadow_BscShmOpen(meadow_events_0296c5a, meadow_args_90bd77d[0], meadow_oflags_0914af9, meadow_sflags_808e6a2, meadow_serialize_result(meadow_events_0296c5a[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a1370e0', 'events': 'meadow_events_e8ec0c1'}, 'handle_shm_unlink')
def meadow_handle_shm_unlink(meadow_parser_a1370e0, meadow_events_e8ec0c1):
    return meadow_BscShmUnlink(meadow_events_e8ec0c1, meadow_events_e8ec0c1[0].values[0], meadow_serialize_result(meadow_events_e8ec0c1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_44a247c', 'events': 'meadow_events_875f9d5'}, 'handle_sem_open')
def meadow_handle_sem_open(meadow_parser_44a247c, meadow_events_875f9d5):
    meadow_args_37dbaf8 = meadow_events_875f9d5[0].values
    meadow_oflags_4715e8c = meadow_serialize_open_flags(meadow_args_37dbaf8[1])
    meadow_sflags_6a5b77f = meadow_serialize_stat_flags(meadow_args_37dbaf8[2]) if meadow_BscOpenFlags.O_CREAT in meadow_oflags_4715e8c else []
    return meadow_BscSemOpen(meadow_events_875f9d5, meadow_args_37dbaf8[0], meadow_oflags_4715e8c, meadow_sflags_6a5b77f, meadow_serialize_result(meadow_events_875f9d5[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_dc2813d', 'events': 'meadow_events_b5bf0c5'}, 'handle_sem_close')
def meadow_handle_sem_close(meadow_parser_dc2813d, meadow_events_b5bf0c5):
    meadow_args_c81622f = meadow_events_b5bf0c5[0].values
    return meadow_BscSemClose(meadow_events_b5bf0c5, meadow_args_c81622f[0], meadow_serialize_result(meadow_events_b5bf0c5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0d24c7c', 'events': 'meadow_events_fa8c176'}, 'handle_sem_unlink')
def meadow_handle_sem_unlink(meadow_parser_0d24c7c, meadow_events_fa8c176):
    meadow_args_a2c6f4a = meadow_events_fa8c176[0].values
    return meadow_BscSemUnlink(meadow_events_fa8c176, meadow_args_a2c6f4a[0], meadow_serialize_result(meadow_events_fa8c176[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_92ca57c', 'events': 'meadow_events_26341f9', 'no_cancel': 'meadow_no_cancel_5c1b57c'}, 'handle_sem_wait')
def meadow_handle_sem_wait(meadow_parser_92ca57c, meadow_events_26341f9, meadow_no_cancel_5c1b57c=False):
    meadow_args_6d0407a = meadow_events_26341f9[0].values
    return meadow_BscSemWait(meadow_events_26341f9, meadow_args_6d0407a[0], meadow_serialize_result(meadow_events_26341f9[-1]), meadow_no_cancel_5c1b57c)

@_name_boundary.callable_contract({'parser': 'meadow_parser_1b07192', 'events': 'meadow_events_e1cd9aa'}, 'handle_sem_trywait')
def meadow_handle_sem_trywait(meadow_parser_1b07192, meadow_events_e1cd9aa):
    meadow_args_bde78c0 = meadow_events_e1cd9aa[0].values
    return meadow_BscSemTrywait(meadow_events_e1cd9aa, meadow_args_bde78c0[0], meadow_serialize_result(meadow_events_e1cd9aa[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9879592', 'events': 'meadow_events_fcd7991'}, 'handle_sem_post')
def meadow_handle_sem_post(meadow_parser_9879592, meadow_events_fcd7991):
    meadow_args_5984ba0 = meadow_events_fcd7991[0].values
    return meadow_BscSemPost(meadow_events_fcd7991, meadow_args_5984ba0[0], meadow_serialize_result(meadow_events_fcd7991[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ab06895', 'events': 'meadow_events_4dd3aa5'}, 'handle_sys_sysctlbyname')
def meadow_handle_sys_sysctlbyname(meadow_parser_ab06895, meadow_events_4dd3aa5):
    meadow_args_c9d9bf4 = meadow_events_4dd3aa5[0].values
    return meadow_BscSysctlbyname(meadow_events_4dd3aa5, meadow_args_c9d9bf4[0], meadow_args_c9d9bf4[1], meadow_args_c9d9bf4[2], meadow_args_c9d9bf4[3], meadow_serialize_result(meadow_events_4dd3aa5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_339a8db', 'events': 'meadow_events_50e394a'}, 'handle_access_extended')
def meadow_handle_access_extended(meadow_parser_339a8db, meadow_events_50e394a):
    meadow_args_d1f9e35 = meadow_events_50e394a[0].values
    return meadow_BscAccessExtended(meadow_events_50e394a, meadow_args_d1f9e35[0], meadow_args_d1f9e35[1], meadow_args_d1f9e35[2], meadow_args_d1f9e35[3], meadow_serialize_result(meadow_events_50e394a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1e14127', 'events': 'meadow_events_5e82cf0'}, 'handle_gettid')
def meadow_handle_gettid(meadow_parser_1e14127, meadow_events_5e82cf0):
    meadow_args_76bdcc7 = meadow_events_5e82cf0[0].values
    return meadow_BscGettid(meadow_events_5e82cf0, meadow_args_76bdcc7[0], meadow_args_76bdcc7[1], meadow_serialize_result(meadow_events_5e82cf0[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b287eb4', 'events': 'meadow_events_816f0af'}, 'handle_shared_region_check_np')
def meadow_handle_shared_region_check_np(meadow_parser_b287eb4, meadow_events_816f0af):
    meadow_args_83615be = meadow_events_816f0af[0].values
    return meadow_BscSharedRegionCheckNp(meadow_events_816f0af, meadow_args_83615be[0], meadow_serialize_result(meadow_events_816f0af[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8ec63db', 'events': 'meadow_events_9c8d950'}, 'handle_psynch_mutexwait')
def meadow_handle_psynch_mutexwait(meadow_parser_8ec63db, meadow_events_9c8d950):
    meadow_args_9e02fde = meadow_events_9c8d950[0].values
    return meadow_BscPsynchMutexwait(meadow_events_9c8d950, meadow_args_9e02fde[0], meadow_args_9e02fde[1], meadow_args_9e02fde[2], meadow_args_9e02fde[3], meadow_serialize_result(meadow_events_9c8d950[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e0f6422', 'events': 'meadow_events_4bb8b51'}, 'handle_psynch_mutexdrop')
def meadow_handle_psynch_mutexdrop(meadow_parser_e0f6422, meadow_events_4bb8b51):
    meadow_args_5feb4e6 = meadow_events_4bb8b51[0].values
    return meadow_BscPsynchMutexdrop(meadow_events_4bb8b51, meadow_args_5feb4e6[0], meadow_args_5feb4e6[1], meadow_args_5feb4e6[2], meadow_args_5feb4e6[3], meadow_serialize_result(meadow_events_4bb8b51[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6d72b51', 'events': 'meadow_events_ff3a90f'}, 'handle_psynch_cvbroad')
def meadow_handle_psynch_cvbroad(meadow_parser_6d72b51, meadow_events_ff3a90f):
    meadow_args_d5e2ede = meadow_events_ff3a90f[0].values
    return meadow_BscPsynchCvbroad(meadow_events_ff3a90f, meadow_args_d5e2ede[0], meadow_args_d5e2ede[1], meadow_args_d5e2ede[2], meadow_args_d5e2ede[3], meadow_serialize_result(meadow_events_ff3a90f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a849a3d', 'events': 'meadow_events_cc39444'}, 'handle_psynch_cvsignal')
def meadow_handle_psynch_cvsignal(meadow_parser_a849a3d, meadow_events_cc39444):
    meadow_args_632b79e = meadow_events_cc39444[0].values
    return meadow_BscPsynchCvsignal(meadow_events_cc39444, meadow_args_632b79e[0], meadow_args_632b79e[1], meadow_args_632b79e[2], meadow_args_632b79e[3], meadow_serialize_result(meadow_events_cc39444[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c88a9a8', 'events': 'meadow_events_2d72336'}, 'handle_psynch_cvwait')
def meadow_handle_psynch_cvwait(meadow_parser_c88a9a8, meadow_events_2d72336):
    meadow_args_0dfc040 = meadow_events_2d72336[0].values
    return meadow_BscPsynchCvwait(meadow_events_2d72336, meadow_args_0dfc040[0], meadow_args_0dfc040[1], meadow_args_0dfc040[2], meadow_args_0dfc040[3], meadow_serialize_result(meadow_events_2d72336[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_35c69a7', 'events': 'meadow_events_cb9a987'}, 'handle_getsid')
def meadow_handle_getsid(meadow_parser_35c69a7, meadow_events_cb9a987):
    meadow_args_8a95360 = meadow_events_cb9a987[0].values
    return meadow_BscGetsid(meadow_events_cb9a987, meadow_args_8a95360[0], meadow_serialize_result(meadow_events_cb9a987[-1], 'sid'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f1d1666', 'events': 'meadow_events_c55e132'}, 'handle_psynch_cvclrprepost')
def meadow_handle_psynch_cvclrprepost(meadow_parser_f1d1666, meadow_events_c55e132):
    meadow_args_b4167a6 = meadow_events_c55e132[0].values
    return meadow_BscPsynchCvclrprepost(meadow_events_c55e132, meadow_args_b4167a6[0], meadow_args_b4167a6[1], meadow_args_b4167a6[2], meadow_args_b4167a6[3], meadow_serialize_result(meadow_events_c55e132[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_87ae956', 'events': 'meadow_events_109768b'}, 'handle_iopolicysys')
def meadow_handle_iopolicysys(meadow_parser_87ae956, meadow_events_109768b):
    meadow_args_297b04c = meadow_events_109768b[0].values
    return meadow_BscIopolicysys(meadow_events_109768b, meadow_args_297b04c[0], meadow_args_297b04c[1], meadow_serialize_result(meadow_events_109768b[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_abdca7b', 'events': 'meadow_events_0edb72d'}, 'handle_process_policy')
def meadow_handle_process_policy(meadow_parser_abdca7b, meadow_events_0edb72d):
    meadow_args_1e1f9da = meadow_events_0edb72d[0].values
    return meadow_BscProcessPolicy(meadow_events_0edb72d, meadow_args_1e1f9da[0], meadow_args_1e1f9da[1], meadow_args_1e1f9da[2], meadow_args_1e1f9da[3], meadow_serialize_result(meadow_events_0edb72d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8d96d33', 'events': 'meadow_events_6651cb3'}, 'handle_mlockall')
def meadow_handle_mlockall(meadow_parser_8d96d33, meadow_events_6651cb3):
    return meadow_BscMlockall(meadow_events_6651cb3, meadow_events_6651cb3[0].values[0], meadow_serialize_result(meadow_events_6651cb3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_30b79a1', 'events': 'meadow_events_c885873'}, 'handle_munlockall')
def meadow_handle_munlockall(meadow_parser_30b79a1, meadow_events_c885873):
    return meadow_BscMunlockall(meadow_events_c885873, meadow_serialize_result(meadow_events_c885873[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d9c72ce', 'events': 'meadow_events_6576f77'}, 'handle_issetugid')
def meadow_handle_issetugid(meadow_parser_d9c72ce, meadow_events_6576f77):
    return meadow_BscIssetugid(meadow_events_6576f77, meadow_serialize_result(meadow_events_6576f77[-1], 'return', bool))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b54de63', 'events': 'meadow_events_3b0fd66'}, 'handle_pthread_sigmask')
def meadow_handle_pthread_sigmask(meadow_parser_b54de63, meadow_events_3b0fd66):
    meadow_args_fcf6171 = meadow_events_3b0fd66[0].values
    return meadow_BscPthreadSigmask(meadow_events_3b0fd66, meadow_args_fcf6171[0], meadow_args_fcf6171[1], meadow_args_fcf6171[2], meadow_serialize_result(meadow_events_3b0fd66[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_625b8e5', 'events': 'meadow_events_64199a1'}, 'handle_disable_threadsignal')
def meadow_handle_disable_threadsignal(meadow_parser_625b8e5, meadow_events_64199a1):
    return meadow_BscDisableThreadsignal(meadow_events_64199a1, meadow_events_64199a1[0].values[0], meadow_serialize_result(meadow_events_64199a1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ac84de3', 'events': 'meadow_events_b46eb8e', 'no_cancel': 'meadow_no_cancel_08a6be2'}, 'handle_semwait_signal')
def meadow_handle_semwait_signal(meadow_parser_ac84de3, meadow_events_b46eb8e, meadow_no_cancel_08a6be2=False):
    meadow_args_9863435 = meadow_events_b46eb8e[0].values
    return meadow_BscSemwaitSignal(meadow_events_b46eb8e, meadow_args_9863435[0], meadow_args_9863435[1], meadow_args_9863435[2], meadow_args_9863435[3], meadow_serialize_result(meadow_events_b46eb8e[-1]), meadow_no_cancel_08a6be2)

@_name_boundary.callable_contract({'parser': 'meadow_parser_bef4a1d', 'events': 'meadow_events_caeeead'}, 'handle_proc_info')
def meadow_handle_proc_info(meadow_parser_bef4a1d, meadow_events_caeeead):
    meadow_args_3a1aa63 = meadow_events_caeeead[0].values
    return meadow_BscProcInfo(meadow_events_caeeead, meadow_ProcInfoCall(meadow_args_3a1aa63[0]), meadow_args_3a1aa63[1], meadow_args_3a1aa63[2], meadow_args_3a1aa63[3], meadow_serialize_result(meadow_events_caeeead[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9a04d65', 'events': 'meadow_events_cdef76e'}, 'handle_sendfile')
def meadow_handle_sendfile(meadow_parser_9a04d65, meadow_events_cdef76e):
    meadow_args_dd6968e = meadow_events_cdef76e[0].values
    return meadow_BscSendfile(meadow_events_cdef76e, meadow_args_dd6968e[0], meadow_args_dd6968e[1], meadow_args_dd6968e[2], meadow_args_dd6968e[3], meadow_serialize_result(meadow_events_cdef76e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4a7c71b', 'events': 'meadow_events_c9762ce'}, 'handle_stat64')
def meadow_handle_stat64(meadow_parser_4a7c71b, meadow_events_c9762ce):
    return meadow_BscStat64(meadow_events_c9762ce, _name_boundary.attributes(meadow_parser_4a7c71b)['parse_vnode'](meadow_events_c9762ce).path, meadow_events_c9762ce[0].values[1], meadow_serialize_result(meadow_events_c9762ce[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_78c5e72', 'events': 'meadow_events_1cce091'}, 'handle_sys_fstat64')
def meadow_handle_sys_fstat64(meadow_parser_78c5e72, meadow_events_1cce091):
    return meadow_BscSysFstat64(meadow_events_1cce091, meadow_events_1cce091[0].values[0], meadow_serialize_result(meadow_events_1cce091[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_242dc10', 'events': 'meadow_events_ff89326'}, 'handle_lstat64')
def meadow_handle_lstat64(meadow_parser_242dc10, meadow_events_ff89326):
    return meadow_BscLstat64(meadow_events_ff89326, _name_boundary.attributes(meadow_parser_242dc10)['parse_vnode'](meadow_events_ff89326).path, meadow_serialize_result(meadow_events_ff89326[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bd96631', 'events': 'meadow_events_ad13bec'}, 'handle_getdirentries64')
def meadow_handle_getdirentries64(meadow_parser_bd96631, meadow_events_ad13bec):
    meadow_args_ade1a6e = meadow_events_ad13bec[0].values
    return meadow_BscGetdirentries64(meadow_events_ad13bec, meadow_args_ade1a6e[0], meadow_args_ade1a6e[1], meadow_args_ade1a6e[2], meadow_args_ade1a6e[3], meadow_serialize_result(meadow_events_ad13bec[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_add2283', 'events': 'meadow_events_15593b5'}, 'handle_statfs64')
def meadow_handle_statfs64(meadow_parser_add2283, meadow_events_15593b5):
    meadow_args_94f4c4c = meadow_events_15593b5[0].values
    return meadow_BscStatfs64(meadow_events_15593b5, _name_boundary.attributes(meadow_parser_add2283)['parse_vnode'](meadow_events_15593b5).path, meadow_args_94f4c4c[1], meadow_serialize_result(meadow_events_15593b5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e972eff', 'events': 'meadow_events_47183b0'}, 'handle_fstatfs64')
def meadow_handle_fstatfs64(meadow_parser_e972eff, meadow_events_47183b0):
    meadow_args_6256e81 = meadow_events_47183b0[0].values
    return meadow_BscFstatfs64(meadow_events_47183b0, meadow_args_6256e81[0], meadow_args_6256e81[1], meadow_serialize_result(meadow_events_47183b0[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_16dd228', 'events': 'meadow_events_e454023'}, 'handle_getfsstat64')
def meadow_handle_getfsstat64(meadow_parser_16dd228, meadow_events_e454023):
    meadow_args_eaaa5b0 = meadow_events_e454023[0].values
    return meadow_BscGetfsstat64(meadow_events_e454023, meadow_args_eaaa5b0[0], meadow_args_eaaa5b0[1], meadow_args_eaaa5b0[2], meadow_serialize_result(meadow_events_e454023[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_70f344f', 'events': 'meadow_events_6ccb18b'}, 'handle_pthread_fchdir')
def meadow_handle_pthread_fchdir(meadow_parser_70f344f, meadow_events_6ccb18b):
    meadow_args_a61af22 = meadow_events_6ccb18b[0].values
    return meadow_BscPthreadFchdir(meadow_events_6ccb18b, meadow_args_a61af22[0], meadow_serialize_result(meadow_events_6ccb18b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f043258', 'events': 'meadow_events_083310f'}, 'handle_audit')
def meadow_handle_audit(meadow_parser_f043258, meadow_events_083310f):
    meadow_args_4efd453 = meadow_events_083310f[0].values
    return meadow_BscAudit(meadow_events_083310f, meadow_args_4efd453[0], meadow_args_4efd453[1], meadow_serialize_result(meadow_events_083310f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_faf6a67', 'events': 'meadow_events_b3fc607'}, 'handle_auditon')
def meadow_handle_auditon(meadow_parser_faf6a67, meadow_events_b3fc607):
    meadow_args_36210ef = meadow_events_b3fc607[0].values
    return meadow_BscAuditon(meadow_events_b3fc607, meadow_args_36210ef[0], meadow_args_36210ef[1], meadow_args_36210ef[2], meadow_serialize_result(meadow_events_b3fc607[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_af5fdd0', 'events': 'meadow_events_a120573'}, 'handle_getauid')
def meadow_handle_getauid(meadow_parser_af5fdd0, meadow_events_a120573):
    meadow_args_6fb2e41 = meadow_events_a120573[0].values
    return meadow_BscGetauid(meadow_events_a120573, meadow_args_6fb2e41[0], meadow_serialize_result(meadow_events_a120573[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a839c12', 'events': 'meadow_events_2775f52'}, 'handle_setauid')
def meadow_handle_setauid(meadow_parser_a839c12, meadow_events_2775f52):
    meadow_args_198f260 = meadow_events_2775f52[0].values
    return meadow_BscSetauid(meadow_events_2775f52, meadow_args_198f260[0], meadow_serialize_result(meadow_events_2775f52[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_003f54e', 'events': 'meadow_events_aa917b5'}, 'handle_bsdthread_create')
def meadow_handle_bsdthread_create(meadow_parser_003f54e, meadow_events_aa917b5):
    return meadow_BscBsdthreadCreate(meadow_events_aa917b5, meadow_events_aa917b5[-1].values[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_d5187d5', 'events': 'meadow_events_80d33f3'}, 'handle_kqueue')
def meadow_handle_kqueue(meadow_parser_d5187d5, meadow_events_80d33f3):
    return meadow_BscKqueue(meadow_events_80d33f3, meadow_serialize_result(meadow_events_80d33f3[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c9bbaa7', 'events': 'meadow_events_1ad5965'}, 'handle_kevent')
def meadow_handle_kevent(meadow_parser_c9bbaa7, meadow_events_1ad5965):
    meadow_args_b90d358 = meadow_events_1ad5965[0].values
    return meadow_BscKevent(meadow_events_1ad5965, meadow_args_b90d358[0], meadow_args_b90d358[1], meadow_args_b90d358[2], meadow_args_b90d358[3], meadow_serialize_result(meadow_events_1ad5965[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1c3558d', 'events': 'meadow_events_657ab16'}, 'handle_lchown')
def meadow_handle_lchown(meadow_parser_1c3558d, meadow_events_657ab16):
    meadow_args_e8eb28f = meadow_events_657ab16[0].values
    return meadow_BscLchown(meadow_events_657ab16, _name_boundary.attributes(meadow_parser_1c3558d)['parse_vnode'](meadow_events_657ab16).path, meadow_args_e8eb28f[1], meadow_args_e8eb28f[2], meadow_serialize_result(meadow_events_657ab16[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7e75533', 'events': 'meadow_events_e1d97bd'}, 'handle_bsdthread_register')
def meadow_handle_bsdthread_register(meadow_parser_7e75533, meadow_events_e1d97bd):
    meadow_args_e5e2d21 = meadow_events_e1d97bd[0].values
    return meadow_BscBsdthreadRegister(meadow_events_e1d97bd, meadow_args_e5e2d21[0], meadow_args_e5e2d21[1], meadow_args_e5e2d21[2], meadow_args_e5e2d21[3], meadow_serialize_result(meadow_events_e1d97bd[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_dd0187f', 'events': 'meadow_events_d0b8eb7'}, 'handle_workq_open')
def meadow_handle_workq_open(meadow_parser_dd0187f, meadow_events_d0b8eb7):
    return meadow_BscWorkqOpen(meadow_events_d0b8eb7, meadow_serialize_result(meadow_events_d0b8eb7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8c142ce', 'events': 'meadow_events_82aacf5'}, 'handle_workq_kernreturn')
def meadow_handle_workq_kernreturn(meadow_parser_8c142ce, meadow_events_82aacf5):
    meadow_args_06c0849 = meadow_events_82aacf5[0].values
    return meadow_BscWorkqKernreturn(meadow_events_82aacf5, meadow_args_06c0849[0], meadow_args_06c0849[1], meadow_args_06c0849[2], meadow_args_06c0849[3], meadow_serialize_result(meadow_events_82aacf5[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_3d1bfc7', 'events': 'meadow_events_4bd3d23'}, 'handle_kevent64')
def meadow_handle_kevent64(meadow_parser_3d1bfc7, meadow_events_4bd3d23):
    meadow_args_f9c083a = meadow_events_4bd3d23[0].values
    return meadow_BscKevent64(meadow_events_4bd3d23, meadow_args_f9c083a[0], meadow_args_f9c083a[1], meadow_args_f9c083a[2], meadow_args_f9c083a[3], meadow_serialize_result(meadow_events_4bd3d23[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e33f814', 'events': 'meadow_events_9942576'}, 'handle_thread_selfid')
def meadow_handle_thread_selfid(meadow_parser_e33f814, meadow_events_9942576):
    return meadow_BscThreadSelfid(meadow_events_9942576, meadow_serialize_result(meadow_events_9942576[-1], 'tid'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7c78e5b', 'events': 'meadow_events_a5e9dfa'}, 'handle_kevent_qos')
def meadow_handle_kevent_qos(meadow_parser_7c78e5b, meadow_events_a5e9dfa):
    meadow_args_6e810cd = meadow_events_a5e9dfa[0].values
    return meadow_BscKeventQos(meadow_events_a5e9dfa, meadow_args_6e810cd[0], meadow_args_6e810cd[1], meadow_args_6e810cd[2], meadow_args_6e810cd[3], meadow_serialize_result(meadow_events_a5e9dfa[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_341923d', 'events': 'meadow_events_9d2eed9'}, 'handle_kevent_id')
def meadow_handle_kevent_id(meadow_parser_341923d, meadow_events_9d2eed9):
    meadow_args_93ee0e9 = meadow_events_9d2eed9[0].values
    return meadow_BscKeventId(meadow_events_9d2eed9, meadow_args_93ee0e9[0], meadow_args_93ee0e9[1], meadow_args_93ee0e9[2], meadow_args_93ee0e9[3], meadow_serialize_result(meadow_events_9d2eed9[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a5a16f6', 'events': 'meadow_events_4c73e20'}, 'handle_mac_syscall')
def meadow_handle_mac_syscall(meadow_parser_a5a16f6, meadow_events_4c73e20):
    meadow_args_008baaf = meadow_events_4c73e20[0].values
    return meadow_BscMacSyscall(meadow_events_4c73e20, meadow_args_008baaf[0], meadow_args_008baaf[1], meadow_args_008baaf[2], meadow_serialize_result(meadow_events_4c73e20[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f3077a6', 'events': 'meadow_events_f5e8a1e', 'no_cancel': 'meadow_no_cancel_2c6e981'}, 'handle_pselect')
def meadow_handle_pselect(meadow_parser_f3077a6, meadow_events_f5e8a1e, meadow_no_cancel_2c6e981=False):
    meadow_args_5d3ba2a = meadow_events_f5e8a1e[0].values
    return meadow_BscPselect(meadow_events_f5e8a1e, meadow_args_5d3ba2a[0], meadow_args_5d3ba2a[1], meadow_args_5d3ba2a[2], meadow_args_5d3ba2a[3], meadow_serialize_result(meadow_events_f5e8a1e[-1], 'count'), meadow_no_cancel_2c6e981)

@_name_boundary.callable_contract({'parser': 'meadow_parser_9e7258c', 'events': 'meadow_events_29b5d37'}, 'handle_fsgetpath')
def meadow_handle_fsgetpath(meadow_parser_9e7258c, meadow_events_29b5d37):
    meadow_args_2b1da4f = meadow_events_29b5d37[0].values
    return meadow_BscFsgetpath(meadow_events_29b5d37, meadow_args_2b1da4f[0], meadow_args_2b1da4f[1], meadow_args_2b1da4f[2], meadow_args_2b1da4f[3], _name_boundary.attributes(meadow_parser_9e7258c)['parse_vnode'](meadow_events_29b5d37).path, meadow_serialize_result(meadow_events_29b5d37[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0dad19c', 'events': 'meadow_events_d554b6b'}, 'handle_sys_fileport_makeport')
def meadow_handle_sys_fileport_makeport(meadow_parser_0dad19c, meadow_events_d554b6b):
    meadow_args_2fe2454 = meadow_events_d554b6b[0].values
    return meadow_BscSysFileportMakeport(meadow_events_d554b6b, meadow_args_2fe2454[0], meadow_args_2fe2454[1], meadow_serialize_result(meadow_events_d554b6b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2ebf24b', 'events': 'meadow_events_bb5185f'}, 'handle_sys_fileport_makefd')
def meadow_handle_sys_fileport_makefd(meadow_parser_2ebf24b, meadow_events_bb5185f):
    meadow_args_38f71aa = meadow_events_bb5185f[0].values
    return meadow_BscSysFileportMakefd(meadow_events_bb5185f, meadow_args_38f71aa[0], meadow_serialize_result(meadow_events_bb5185f[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c04bb39', 'events': 'meadow_events_026a1c7'}, 'handle_audit_session_port')
def meadow_handle_audit_session_port(meadow_parser_c04bb39, meadow_events_026a1c7):
    meadow_args_b579bd4 = meadow_events_026a1c7[0].values
    return meadow_BscAuditSessionPort(meadow_events_026a1c7, meadow_args_b579bd4[0], meadow_args_b579bd4[1], meadow_serialize_result(meadow_events_026a1c7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_03aaa45', 'events': 'meadow_events_9c06cc3'}, 'handle_pid_suspend')
def meadow_handle_pid_suspend(meadow_parser_03aaa45, meadow_events_9c06cc3):
    meadow_args_e1f7dcd = meadow_events_9c06cc3[0].values
    return meadow_BscPidSuspend(meadow_events_9c06cc3, meadow_args_e1f7dcd[0], meadow_serialize_result(meadow_events_9c06cc3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0c2cfae', 'events': 'meadow_events_b31034b'}, 'handle_pid_resume')
def meadow_handle_pid_resume(meadow_parser_0c2cfae, meadow_events_b31034b):
    meadow_args_073ef37 = meadow_events_b31034b[0].values
    return meadow_BscPidResume(meadow_events_b31034b, meadow_args_073ef37[0], meadow_serialize_result(meadow_events_b31034b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5fa31b6', 'events': 'meadow_events_20d1164'}, 'handle_pid_hibernate')
def meadow_handle_pid_hibernate(meadow_parser_5fa31b6, meadow_events_20d1164):
    meadow_args_c186d36 = meadow_events_20d1164[0].values
    return meadow_BscPidHibernate(meadow_events_20d1164, meadow_args_c186d36[0], meadow_serialize_result(meadow_events_20d1164[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_addea11', 'events': 'meadow_events_a48a79d'}, 'handle_pid_shutdown_sockets')
def meadow_handle_pid_shutdown_sockets(meadow_parser_addea11, meadow_events_a48a79d):
    meadow_args_04739bc = meadow_events_a48a79d[0].values
    return meadow_BscPidShutdownSockets(meadow_events_a48a79d, meadow_args_04739bc[0], meadow_args_04739bc[1], meadow_serialize_result(meadow_events_a48a79d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7ede32a', 'events': 'meadow_events_b654600'}, 'handle_shared_region_map_and_slide_np')
def meadow_handle_shared_region_map_and_slide_np(meadow_parser_7ede32a, meadow_events_b654600):
    meadow_args_7085c80 = meadow_events_b654600[0].values
    return meadow_BscSharedRegionMapAndSlideNp(meadow_events_b654600, meadow_args_7085c80[0], meadow_args_7085c80[1], meadow_args_7085c80[2], meadow_args_7085c80[3], meadow_serialize_result(meadow_events_b654600[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_eba53ef', 'events': 'meadow_events_6d1600e'}, 'handle_kas_info')
def meadow_handle_kas_info(meadow_parser_eba53ef, meadow_events_6d1600e):
    meadow_args_c277a08 = meadow_events_6d1600e[0].values
    return meadow_BscKasInfo(meadow_events_6d1600e, meadow_args_c277a08[0], meadow_args_c277a08[1], meadow_args_c277a08[2], meadow_serialize_result(meadow_events_6d1600e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bd654f8', 'events': 'meadow_events_8d7bdff'}, 'handle_memorystatus_control')
def meadow_handle_memorystatus_control(meadow_parser_bd654f8, meadow_events_8d7bdff):
    meadow_args_c652e16 = meadow_events_8d7bdff[0].values
    return meadow_BscMemorystatusControl(meadow_events_8d7bdff, meadow_args_c652e16[0], meadow_args_c652e16[1], meadow_args_c652e16[2], meadow_args_c652e16[3], meadow_serialize_result(meadow_events_8d7bdff[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_74667e3', 'events': 'meadow_events_397f464'}, 'handle_guarded_open_np')
def meadow_handle_guarded_open_np(meadow_parser_74667e3, meadow_events_397f464):
    meadow_args_e5fa2a2 = meadow_events_397f464[0].values
    return meadow_BscGuardedOpenNp(meadow_events_397f464, _name_boundary.attributes(meadow_parser_74667e3)['parse_vnode'](meadow_events_397f464).path, meadow_args_e5fa2a2[1], meadow_args_e5fa2a2[2], meadow_serialize_open_flags(meadow_args_e5fa2a2[3]), meadow_serialize_result(meadow_events_397f464[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_48a89ee', 'events': 'meadow_events_697d444'}, 'handle_guarded_close_np')
def meadow_handle_guarded_close_np(meadow_parser_48a89ee, meadow_events_697d444):
    meadow_args_790a5e4 = meadow_events_697d444[0].values
    return meadow_BscGuardedCloseNp(meadow_events_697d444, meadow_args_790a5e4[0], meadow_args_790a5e4[1], meadow_serialize_result(meadow_events_697d444[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_de0c1c9', 'events': 'meadow_events_310ce14'}, 'handle_guarded_kqueue_np')
def meadow_handle_guarded_kqueue_np(meadow_parser_de0c1c9, meadow_events_310ce14):
    meadow_args_154e354 = meadow_events_310ce14[0].values
    return meadow_BscGuardedKqueueNp(meadow_events_310ce14, meadow_args_154e354[0], meadow_args_154e354[1], meadow_serialize_result(meadow_events_310ce14[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_81f8c9c', 'events': 'meadow_events_485db75'}, 'handle_change_fdguard_np')
def meadow_handle_change_fdguard_np(meadow_parser_81f8c9c, meadow_events_485db75):
    meadow_args_a1b771a = meadow_events_485db75[0].values
    return meadow_BscChangeFdguardNp(meadow_events_485db75, meadow_args_a1b771a[0], meadow_args_a1b771a[1], meadow_args_a1b771a[2], meadow_args_a1b771a[3], meadow_serialize_result(meadow_events_485db75[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d545f45', 'events': 'meadow_events_757ec12'}, 'handle_usrctl')
def meadow_handle_usrctl(meadow_parser_d545f45, meadow_events_757ec12):
    meadow_args_de55879 = meadow_events_757ec12[0].values
    return meadow_BscUsrctl(meadow_events_757ec12, meadow_args_de55879[0], meadow_serialize_result(meadow_events_757ec12[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e35afce', 'events': 'meadow_events_943c922'}, 'handle_proc_rlimit_control')
def meadow_handle_proc_rlimit_control(meadow_parser_e35afce, meadow_events_943c922):
    meadow_args_331e19c = meadow_events_943c922[0].values
    return meadow_BscProcRlimitControl(meadow_events_943c922, meadow_args_331e19c[0], meadow_args_331e19c[1], meadow_args_331e19c[2], meadow_serialize_result(meadow_events_943c922[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_776c564', 'events': 'meadow_events_9fbcbea'}, 'handle_connectx')
def meadow_handle_connectx(meadow_parser_776c564, meadow_events_9fbcbea):
    meadow_args_0c4e90d = meadow_events_9fbcbea[0].values
    return meadow_BscConnectx(meadow_events_9fbcbea, meadow_args_0c4e90d[0], meadow_args_0c4e90d[1], meadow_args_0c4e90d[2], meadow_args_0c4e90d[3], meadow_serialize_result(meadow_events_9fbcbea[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_19b3d70', 'events': 'meadow_events_037ea19'}, 'handle_disconnectx')
def meadow_handle_disconnectx(meadow_parser_19b3d70, meadow_events_037ea19):
    meadow_args_bf2b647 = meadow_events_037ea19[0].values
    return meadow_BscDisconnectx(meadow_events_037ea19, meadow_args_bf2b647[0], meadow_args_bf2b647[1], meadow_args_bf2b647[2], meadow_serialize_result(meadow_events_037ea19[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_869d3ab', 'events': 'meadow_events_41e714a'}, 'handle_peeloff')
def meadow_handle_peeloff(meadow_parser_869d3ab, meadow_events_41e714a):
    meadow_args_bb8e4c2 = meadow_events_41e714a[0].values
    return meadow_BscPeeloff(meadow_events_41e714a, meadow_args_bb8e4c2[0], meadow_args_bb8e4c2[1], meadow_serialize_result(meadow_events_41e714a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_864528b', 'events': 'meadow_events_7c317c6'}, 'handle_socket_delegate')
def meadow_handle_socket_delegate(meadow_parser_864528b, meadow_events_7c317c6):
    meadow_args_49ae5a1 = meadow_events_7c317c6[0].values
    return meadow_BscSocketDelegate(meadow_events_7c317c6, meadow_socket.AddressFamily(meadow_args_49ae5a1[0]), meadow_socket.SocketKind(meadow_args_49ae5a1[1]), meadow_args_49ae5a1[2], meadow_args_49ae5a1[3], meadow_serialize_result(meadow_events_7c317c6[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cf2dbe0', 'events': 'meadow_events_a65d9f3'}, 'handle_telemetry')
def meadow_handle_telemetry(meadow_parser_cf2dbe0, meadow_events_a65d9f3):
    meadow_args_d3c7184 = meadow_events_a65d9f3[0].values
    return meadow_BscTelemetry(meadow_events_a65d9f3, meadow_args_d3c7184[0], meadow_args_d3c7184[1], meadow_args_d3c7184[2], meadow_args_d3c7184[3], meadow_serialize_result(meadow_events_a65d9f3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_70c69a7', 'events': 'meadow_events_36f824d'}, 'handle_proc_uuid_policy')
def meadow_handle_proc_uuid_policy(meadow_parser_70c69a7, meadow_events_36f824d):
    meadow_args_262c67c = meadow_events_36f824d[0].values
    return meadow_BscProcUuidPolicy(meadow_events_36f824d, meadow_args_262c67c[0], meadow_args_262c67c[1], meadow_args_262c67c[2], meadow_args_262c67c[3], meadow_serialize_result(meadow_events_36f824d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e635655', 'events': 'meadow_events_d3ff8f0'}, 'handle_memorystatus_get_level')
def meadow_handle_memorystatus_get_level(meadow_parser_e635655, meadow_events_d3ff8f0):
    return meadow_BscMemorystatusGetLevel(meadow_events_d3ff8f0, meadow_events_d3ff8f0[0].values[0], meadow_serialize_result(meadow_events_d3ff8f0[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6a15f1d', 'events': 'meadow_events_8ed3a6c'}, 'handle_system_override')
def meadow_handle_system_override(meadow_parser_6a15f1d, meadow_events_8ed3a6c):
    meadow_args_325b367 = meadow_events_8ed3a6c[0].values
    return meadow_BscSystemOverride(meadow_events_8ed3a6c, meadow_args_325b367[0], meadow_args_325b367[1], meadow_serialize_result(meadow_events_8ed3a6c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7a5f10d', 'events': 'meadow_events_1e87b81'}, 'handle_vfs_purge')
def meadow_handle_vfs_purge(meadow_parser_7a5f10d, meadow_events_1e87b81):
    return meadow_BscVfsPurge(meadow_events_1e87b81, meadow_serialize_result(meadow_events_1e87b81[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_421ba4d', 'events': 'meadow_events_ed4bd0a'}, 'handle_sfi_ctl')
def meadow_handle_sfi_ctl(meadow_parser_421ba4d, meadow_events_ed4bd0a):
    meadow_args_66aec98 = meadow_events_ed4bd0a[0].values
    return meadow_BscSfiCtl(meadow_events_ed4bd0a, meadow_args_66aec98[0], meadow_args_66aec98[1], meadow_args_66aec98[2], meadow_args_66aec98[3], meadow_serialize_result(meadow_events_ed4bd0a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b4b70b5', 'events': 'meadow_events_16daf13'}, 'handle_sfi_pidctl')
def meadow_handle_sfi_pidctl(meadow_parser_b4b70b5, meadow_events_16daf13):
    meadow_args_860e9ce = meadow_events_16daf13[0].values
    return meadow_BscSfiPidctl(meadow_events_16daf13, meadow_args_860e9ce[0], meadow_args_860e9ce[1], meadow_args_860e9ce[2], meadow_args_860e9ce[3], meadow_serialize_result(meadow_events_16daf13[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8382db0', 'events': 'meadow_events_35dbe82'}, 'handle_coalition')
def meadow_handle_coalition(meadow_parser_8382db0, meadow_events_35dbe82):
    meadow_args_53f8558 = meadow_events_35dbe82[0].values
    return meadow_BscCoalition(meadow_events_35dbe82, meadow_args_53f8558[0], meadow_args_53f8558[1], meadow_args_53f8558[2], meadow_serialize_result(meadow_events_35dbe82[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b39c3cc', 'events': 'meadow_events_b63df0e'}, 'handle_coalition_info')
def meadow_handle_coalition_info(meadow_parser_b39c3cc, meadow_events_b63df0e):
    meadow_args_e54e3ef = meadow_events_b63df0e[0].values
    return meadow_BscCoalitionInfo(meadow_events_b63df0e, meadow_args_e54e3ef[0], meadow_args_e54e3ef[1], meadow_args_e54e3ef[2], meadow_args_e54e3ef[3], meadow_serialize_result(meadow_events_b63df0e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b1a4875', 'events': 'meadow_events_e55c14b'}, 'handle_necp_match_policy')
def meadow_handle_necp_match_policy(meadow_parser_b1a4875, meadow_events_e55c14b):
    meadow_args_0011dd9 = meadow_events_e55c14b[0].values
    return meadow_BscNecpMatchPolicy(meadow_events_e55c14b, meadow_args_0011dd9[0], meadow_args_0011dd9[1], meadow_args_0011dd9[2], meadow_serialize_result(meadow_events_e55c14b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5b620ea', 'events': 'meadow_events_83aa8a2'}, 'handle_getattrlistbulk')
def meadow_handle_getattrlistbulk(meadow_parser_5b620ea, meadow_events_83aa8a2):
    meadow_args_3ec99b2 = meadow_events_83aa8a2[0].values
    return meadow_BscGetattrlistbulk(meadow_events_83aa8a2, meadow_args_3ec99b2[0], meadow_args_3ec99b2[1], meadow_args_3ec99b2[2], meadow_args_3ec99b2[3], meadow_serialize_result(meadow_events_83aa8a2[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_38a666a', 'events': 'meadow_events_41a8d57'}, 'handle_clonefileat')
def meadow_handle_clonefileat(meadow_parser_38a666a, meadow_events_41a8d57):
    meadow_src_b69abed = _name_boundary.attributes(meadow_parser_38a666a)['parse_vnode'](meadow_events_41a8d57)
    meadow_dst_09b232d = _name_boundary.attributes(meadow_parser_38a666a)['parse_vnode']([meadow_e_8442cf5 for meadow_e_8442cf5 in meadow_events_41a8d57 if meadow_e_8442cf5 not in meadow_src_b69abed.ktraces])
    meadow_args_c4c4ce2 = meadow_events_41a8d57[0].values
    return meadow_BscClonefileat(meadow_events_41a8d57, meadow_args_c4c4ce2[0], meadow_src_b69abed.path, meadow_args_c4c4ce2[2], meadow_dst_09b232d.path, meadow_serialize_result(meadow_events_41a8d57[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c9bfe16', 'events': 'meadow_events_1ba8bce', 'no_cancel': 'meadow_no_cancel_98c264d'}, 'handle_openat')
def meadow_handle_openat(meadow_parser_c9bfe16, meadow_events_1ba8bce, meadow_no_cancel_98c264d=False):
    meadow_vnode_00c5f03 = _name_boundary.attributes(meadow_parser_c9bfe16)['parse_vnode'](meadow_events_1ba8bce)
    meadow_call_flags_72addf6 = meadow_serialize_open_flags(meadow_events_1ba8bce[0].values[2])
    return meadow_BscOpenat(meadow_events_1ba8bce, meadow_events_1ba8bce[0].values[0], meadow_vnode_00c5f03.path, meadow_call_flags_72addf6, meadow_serialize_result(meadow_events_1ba8bce[-1], 'fd'), meadow_no_cancel_98c264d)

@_name_boundary.callable_contract({'parser': 'meadow_parser_4d042a1', 'events': 'meadow_events_a812be1'}, 'handle_renameat')
def meadow_handle_renameat(meadow_parser_4d042a1, meadow_events_a812be1):
    meadow_nodes_0ff3376 = _name_boundary.attributes(meadow_parser_4d042a1)['parse_vnodes'](meadow_events_a812be1)
    meadow_args_388185c = meadow_events_a812be1[0].values
    return meadow_BscRenameat(meadow_events_a812be1, meadow_args_388185c[0], meadow_nodes_0ff3376[0].path, meadow_args_388185c[2], meadow_nodes_0ff3376[1].path, meadow_serialize_result(meadow_events_a812be1[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d250276', 'events': 'meadow_events_375dbea'}, 'handle_faccessat')
def meadow_handle_faccessat(meadow_parser_d250276, meadow_events_375dbea):
    meadow_vnode_7abb421 = _name_boundary.attributes(meadow_parser_d250276)['parse_vnode'](meadow_events_375dbea)
    meadow_args_1df9bdf = meadow_events_375dbea[0].values
    meadow_amode_d75ec23 = meadow_serialize_access_flags(meadow_args_1df9bdf[2])
    return meadow_BscFaccessat(meadow_events_375dbea, meadow_args_1df9bdf[0], meadow_vnode_7abb421.path, meadow_amode_d75ec23, meadow_args_1df9bdf[3], meadow_serialize_result(meadow_events_375dbea[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4f58ea1', 'events': 'meadow_events_394950c'}, 'handle_fchmodat')
def meadow_handle_fchmodat(meadow_parser_4f58ea1, meadow_events_394950c):
    meadow_vnode_d8aa33b = _name_boundary.attributes(meadow_parser_4f58ea1)['parse_vnode'](meadow_events_394950c)
    meadow_args_211c635 = meadow_events_394950c[0].values
    meadow_mode_cd321e5 = meadow_serialize_stat_flags(meadow_args_211c635[2])
    return meadow_BscFchmodat(meadow_events_394950c, meadow_args_211c635[0], meadow_vnode_d8aa33b.path, meadow_mode_cd321e5, meadow_args_211c635[3], meadow_serialize_result(meadow_events_394950c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d763553', 'events': 'meadow_events_d0f72e0'}, 'handle_fchownat')
def meadow_handle_fchownat(meadow_parser_d763553, meadow_events_d0f72e0):
    meadow_vnode_27b34ab = _name_boundary.attributes(meadow_parser_d763553)['parse_vnode'](meadow_events_d0f72e0)
    meadow_args_1104d04 = meadow_events_d0f72e0[0].values
    return meadow_BscFchownat(meadow_events_d0f72e0, meadow_args_1104d04[0], meadow_vnode_27b34ab.path, meadow_args_1104d04[2], meadow_args_1104d04[3], meadow_serialize_result(meadow_events_d0f72e0[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1bd7536', 'events': 'meadow_events_47249d8'}, 'handle_fstatat')
def meadow_handle_fstatat(meadow_parser_1bd7536, meadow_events_47249d8):
    meadow_vnode_9dd9753 = _name_boundary.attributes(meadow_parser_1bd7536)['parse_vnode'](meadow_events_47249d8)
    meadow_args_039dbdb = meadow_events_47249d8[0].values
    return meadow_BscFstatat(meadow_events_47249d8, meadow_args_039dbdb[0], meadow_vnode_9dd9753.path, meadow_args_039dbdb[2], meadow_args_039dbdb[3], meadow_serialize_result(meadow_events_47249d8[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_28e7d61', 'events': 'meadow_events_1a7a33b'}, 'handle_fstatat64')
def meadow_handle_fstatat64(meadow_parser_28e7d61, meadow_events_1a7a33b):
    meadow_vnode_57c189d = _name_boundary.attributes(meadow_parser_28e7d61)['parse_vnode'](meadow_events_1a7a33b)
    meadow_args_e955108 = meadow_events_1a7a33b[0].values
    return meadow_BscFstatat64(meadow_events_1a7a33b, meadow_args_e955108[0], meadow_vnode_57c189d.path, meadow_args_e955108[2], meadow_args_e955108[3], meadow_serialize_result(meadow_events_1a7a33b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bc26153', 'events': 'meadow_events_349101a'}, 'handle_linkat')
def meadow_handle_linkat(meadow_parser_bc26153, meadow_events_349101a):
    meadow_nodes_ca546c2 = _name_boundary.attributes(meadow_parser_bc26153)['parse_vnodes'](meadow_events_349101a)
    meadow_path1_9f19923, meadow_path2_32ba179 = (meadow_nodes_ca546c2[0].path, meadow_nodes_ca546c2[1].path) if meadow_nodes_ca546c2 else ('', '')
    meadow_args_c2cee1b = meadow_events_349101a[0].values
    return meadow_BscLinkat(meadow_events_349101a, meadow_args_c2cee1b[0], meadow_path1_9f19923, meadow_args_c2cee1b[2], meadow_path2_32ba179, meadow_serialize_result(meadow_events_349101a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_88a7afd', 'events': 'meadow_events_4883b59'}, 'handle_unlinkat')
def meadow_handle_unlinkat(meadow_parser_88a7afd, meadow_events_4883b59):
    meadow_vnode_a957d41 = _name_boundary.attributes(meadow_parser_88a7afd)['parse_vnode'](meadow_events_4883b59)
    meadow_args_c076614 = meadow_events_4883b59[0].values
    return meadow_BscUnlinkat(meadow_events_4883b59, meadow_args_c076614[0], meadow_vnode_a957d41.path, meadow_args_c076614[2], meadow_serialize_result(meadow_events_4883b59[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_10faf2c', 'events': 'meadow_events_3605243'}, 'handle_readlinkat')
def meadow_handle_readlinkat(meadow_parser_10faf2c, meadow_events_3605243):
    meadow_vnode_6901754 = _name_boundary.attributes(meadow_parser_10faf2c)['parse_vnode'](meadow_events_3605243)
    meadow_args_94c888a = meadow_events_3605243[0].values
    return meadow_BscReadlinkat(meadow_events_3605243, meadow_args_94c888a[0], meadow_vnode_6901754.path, meadow_args_94c888a[2], meadow_args_94c888a[3], meadow_serialize_result(meadow_events_3605243[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b95a436', 'events': 'meadow_events_f5200ef'}, 'handle_symlinkat')
def meadow_handle_symlinkat(meadow_parser_b95a436, meadow_events_f5200ef):
    meadow_nodes_c054295 = _name_boundary.attributes(meadow_parser_b95a436)['parse_vnodes'](meadow_events_f5200ef)
    meadow_oldpath_901fc81 = meadow_nodes_c054295[0].path if len(meadow_nodes_c054295) > 1 else ''
    meadow_args_e633dba = meadow_events_f5200ef[0].values
    return meadow_BscSymlinkat(meadow_events_f5200ef, meadow_oldpath_901fc81, meadow_args_e633dba[1], meadow_nodes_c054295[-1].path, meadow_serialize_result(meadow_events_f5200ef[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5c58a8c', 'events': 'meadow_events_87756d8'}, 'handle_mkdirat')
def meadow_handle_mkdirat(meadow_parser_5c58a8c, meadow_events_87756d8):
    meadow_vnode_9299be3 = _name_boundary.attributes(meadow_parser_5c58a8c)['parse_vnode'](meadow_events_87756d8)
    meadow_args_e564750 = meadow_events_87756d8[0].values
    return meadow_BscMkdirat(meadow_events_87756d8, meadow_args_e564750[0], meadow_vnode_9299be3.path, meadow_serialize_stat_flags(meadow_args_e564750[2]), meadow_serialize_result(meadow_events_87756d8[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1bdb1f0', 'events': 'meadow_events_13856bb'}, 'handle_getattrlistat')
def meadow_handle_getattrlistat(meadow_parser_1bdb1f0, meadow_events_13856bb):
    meadow_vnode_7030004 = _name_boundary.attributes(meadow_parser_1bdb1f0)['parse_vnode'](meadow_events_13856bb)
    meadow_args_6a8557d = meadow_events_13856bb[0].values
    return meadow_BscGetattrlistat(meadow_events_13856bb, meadow_args_6a8557d[0], meadow_vnode_7030004.path, meadow_args_6a8557d[2], meadow_args_6a8557d[3], meadow_serialize_result(meadow_events_13856bb[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6749810', 'events': 'meadow_events_5b70e64'}, 'handle_proc_trace_log')
def meadow_handle_proc_trace_log(meadow_parser_6749810, meadow_events_5b70e64):
    meadow_args_7c5ff20 = meadow_events_5b70e64[0].values
    return meadow_BscProcTraceLog(meadow_events_5b70e64, meadow_args_7c5ff20[0], meadow_args_7c5ff20[1], meadow_serialize_result(meadow_events_5b70e64[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ea35949', 'events': 'meadow_events_8dfebc3'}, 'handle_bsdthread_ctl')
def meadow_handle_bsdthread_ctl(meadow_parser_ea35949, meadow_events_8dfebc3):
    meadow_args_6b3afbe = meadow_events_8dfebc3[0].values
    return meadow_BscBsdthreadCtl(meadow_events_8dfebc3, meadow_args_6b3afbe[0], meadow_args_6b3afbe[1], meadow_args_6b3afbe[2], meadow_args_6b3afbe[3], meadow_serialize_result(meadow_events_8dfebc3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_7487f62', 'events': 'meadow_events_b487ef3'}, 'handle_openbyid_np')
def meadow_handle_openbyid_np(meadow_parser_7487f62, meadow_events_b487ef3):
    meadow_args_a29678c = meadow_events_b487ef3[0].values
    return meadow_BscOpenbyidNp(meadow_events_b487ef3, meadow_args_a29678c[0], meadow_args_a29678c[1], meadow_serialize_open_flags(meadow_args_a29678c[2]), meadow_serialize_result(meadow_events_b487ef3[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1d538a4', 'events': 'meadow_events_0d519aa'}, 'handle_recvmsg_x')
def meadow_handle_recvmsg_x(meadow_parser_1d538a4, meadow_events_0d519aa):
    meadow_args_8bc691e = meadow_events_0d519aa[0].values
    return meadow_BscRecvmsgX(meadow_events_0d519aa, meadow_args_8bc691e[0], meadow_args_8bc691e[1], meadow_args_8bc691e[2], meadow_args_8bc691e[3], meadow_serialize_result(meadow_events_0d519aa[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_0ece529', 'events': 'meadow_events_98b670b'}, 'handle_sendmsg_x')
def meadow_handle_sendmsg_x(meadow_parser_0ece529, meadow_events_98b670b):
    meadow_args_981c18a = meadow_events_98b670b[0].values
    return meadow_BscSendmsgX(meadow_events_98b670b, meadow_args_981c18a[0], meadow_args_981c18a[1], meadow_args_981c18a[2], meadow_args_981c18a[3], meadow_serialize_result(meadow_events_98b670b[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f8975c0', 'events': 'meadow_events_0677b8c'}, 'handle_thread_selfusage')
def meadow_handle_thread_selfusage(meadow_parser_f8975c0, meadow_events_0677b8c):
    return meadow_BscThreadSelfusage(meadow_events_0677b8c, meadow_serialize_result(meadow_events_0677b8c[-1], 'runtime'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ee37565', 'events': 'meadow_events_9811855'}, 'handle_csrctl')
def meadow_handle_csrctl(meadow_parser_ee37565, meadow_events_9811855):
    meadow_args_d5aa18f = meadow_events_9811855[0].values
    return meadow_BscCsrctl(meadow_events_9811855, meadow_args_d5aa18f[0], meadow_args_d5aa18f[1], meadow_args_d5aa18f[2], meadow_serialize_result(meadow_events_9811855[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9187ae2', 'events': 'meadow_events_d595d30'}, 'handle_guarded_open_dprotected_np')
def meadow_handle_guarded_open_dprotected_np(meadow_parser_9187ae2, meadow_events_d595d30):
    meadow_vnode_c686a8f = _name_boundary.attributes(meadow_parser_9187ae2)['parse_vnode'](meadow_events_d595d30)
    meadow_args_314cbb0 = meadow_events_d595d30[0].values
    return meadow_BscGuardedOpenDprotectedNp(meadow_events_d595d30, meadow_vnode_c686a8f.path, meadow_args_314cbb0[1], meadow_args_314cbb0[2], meadow_serialize_open_flags(meadow_args_314cbb0[3]), meadow_serialize_result(meadow_events_d595d30[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_37b199b', 'events': 'meadow_events_1d404ae'}, 'handle_guarded_write_np')
def meadow_handle_guarded_write_np(meadow_parser_37b199b, meadow_events_1d404ae):
    meadow_args_919a9c2 = meadow_events_1d404ae[0].values
    return meadow_BscGuardedWriteNp(meadow_events_1d404ae, meadow_args_919a9c2[0], meadow_args_919a9c2[1], meadow_args_919a9c2[2], meadow_args_919a9c2[3], meadow_serialize_result(meadow_events_1d404ae[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e9f5cd5', 'events': 'meadow_events_17fefa7'}, 'handle_guarded_pwrite_np')
def meadow_handle_guarded_pwrite_np(meadow_parser_e9f5cd5, meadow_events_17fefa7):
    meadow_args_1a59492 = meadow_events_17fefa7[0].values
    return meadow_BscGuardedPwriteNp(meadow_events_17fefa7, meadow_args_1a59492[0], meadow_args_1a59492[1], meadow_args_1a59492[2], meadow_args_1a59492[3], meadow_serialize_result(meadow_events_17fefa7[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c087e1c', 'events': 'meadow_events_e0630b1'}, 'handle_guarded_writev_np')
def meadow_handle_guarded_writev_np(meadow_parser_c087e1c, meadow_events_e0630b1):
    meadow_args_dcf97df = meadow_events_e0630b1[0].values
    return meadow_BscGuardedWritevNp(meadow_events_e0630b1, meadow_args_dcf97df[0], meadow_args_dcf97df[1], meadow_args_dcf97df[2], meadow_args_dcf97df[3], meadow_serialize_result(meadow_events_e0630b1[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8bb2268', 'events': 'meadow_events_b5f3161'}, 'handle_renameatx_np')
def meadow_handle_renameatx_np(meadow_parser_8bb2268, meadow_events_b5f3161):
    meadow_nodes_10b89fe = _name_boundary.attributes(meadow_parser_8bb2268)['parse_vnodes'](meadow_events_b5f3161)
    meadow_path1_ed027cd, meadow_path2_6a67f20 = (meadow_nodes_10b89fe[0].path, meadow_nodes_10b89fe[1].path) if meadow_nodes_10b89fe else ('', '')
    meadow_args_481f6ab = meadow_events_b5f3161[0].values
    return meadow_BscRenameatxNp(meadow_events_b5f3161, meadow_args_481f6ab[0], meadow_path1_ed027cd, meadow_args_481f6ab[2], meadow_path2_6a67f20, meadow_serialize_result(meadow_events_b5f3161[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bc22c48', 'events': 'meadow_events_cee5d59'}, 'handle_mremap_encrypted')
def meadow_handle_mremap_encrypted(meadow_parser_bc22c48, meadow_events_cee5d59):
    meadow_args_e462c16 = meadow_events_cee5d59[0].values
    return meadow_BscMremapEncrypted(meadow_events_cee5d59, meadow_args_e462c16[0], meadow_args_e462c16[1], meadow_args_e462c16[2], meadow_args_e462c16[3], meadow_serialize_result(meadow_events_cee5d59[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_abd8613', 'events': 'meadow_events_75bd4f2'}, 'handle_netagent_trigger')
def meadow_handle_netagent_trigger(meadow_parser_abd8613, meadow_events_75bd4f2):
    meadow_args_0882732 = meadow_events_75bd4f2[0].values
    return meadow_BscNetagentTrigger(meadow_events_75bd4f2, meadow_args_0882732[0], meadow_args_0882732[1], meadow_serialize_result(meadow_events_75bd4f2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_67d306c', 'events': 'meadow_events_d15ae8a'}, 'handle_stack_snapshot_with_config')
def meadow_handle_stack_snapshot_with_config(meadow_parser_67d306c, meadow_events_d15ae8a):
    meadow_args_a814573 = meadow_events_d15ae8a[0].values
    return meadow_BscStackSnapshotWithConfig(meadow_events_d15ae8a, meadow_args_a814573[0], meadow_args_a814573[1], meadow_args_a814573[2], meadow_serialize_result(meadow_events_d15ae8a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b6ac038', 'events': 'meadow_events_56e0563'}, 'handle_microstackshot')
def meadow_handle_microstackshot(meadow_parser_b6ac038, meadow_events_56e0563):
    meadow_args_d56b290 = meadow_events_56e0563[0].values
    return meadow_BscMicrostackshot(meadow_events_56e0563, meadow_args_d56b290[0], meadow_args_d56b290[1], meadow_args_d56b290[2], meadow_serialize_result(meadow_events_56e0563[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_03d416d', 'events': 'meadow_events_a345521'}, 'handle_grab_pgo_data')
def meadow_handle_grab_pgo_data(meadow_parser_03d416d, meadow_events_a345521):
    meadow_args_9d8dded = meadow_events_a345521[0].values
    return meadow_BscGrabPgoData(meadow_events_a345521, meadow_args_9d8dded[0], meadow_args_9d8dded[1], meadow_args_9d8dded[2], meadow_args_9d8dded[3], meadow_serialize_result(meadow_events_a345521[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_c469885', 'events': 'meadow_events_b90482b'}, 'handle_persona')
def meadow_handle_persona(meadow_parser_c469885, meadow_events_b90482b):
    meadow_args_0391e0d = meadow_events_b90482b[0].values
    return meadow_BscPersona(meadow_events_b90482b, meadow_args_0391e0d[0], meadow_args_0391e0d[1], meadow_args_0391e0d[2], meadow_args_0391e0d[3], meadow_serialize_result(meadow_events_b90482b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_6be247a', 'events': 'meadow_events_1773fda'}, 'handle_mach_eventlink_signal')
def meadow_handle_mach_eventlink_signal(meadow_parser_6be247a, meadow_events_1773fda):
    meadow_args_9fda1e2 = meadow_events_1773fda[0].values
    return meadow_BscMachEventlinkSignal(meadow_events_1773fda, meadow_args_9fda1e2[0], meadow_args_9fda1e2[1], meadow_serialize_result(meadow_events_1773fda[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_145ab23', 'events': 'meadow_events_007a1c0'}, 'handle_mach_eventlink_wait_until')
def meadow_handle_mach_eventlink_wait_until(meadow_parser_145ab23, meadow_events_007a1c0):
    meadow_args_bdd89b9 = meadow_events_007a1c0[0].values
    return meadow_BscMachEventlinkWaitUntil(meadow_events_007a1c0, meadow_args_bdd89b9[0], meadow_args_bdd89b9[1], meadow_args_bdd89b9[2], meadow_args_bdd89b9[3], meadow_serialize_result(meadow_events_007a1c0[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_691dbd2', 'events': 'meadow_events_436303a'}, 'handle_mach_eventlink_signal_wait_until')
def meadow_handle_mach_eventlink_signal_wait_until(meadow_parser_691dbd2, meadow_events_436303a):
    meadow_args_1d7193f = meadow_events_436303a[0].values
    return meadow_BscMachEventlinkSignalWaitUntil(meadow_events_436303a, meadow_args_1d7193f[0], meadow_args_1d7193f[1], meadow_args_1d7193f[2], meadow_args_1d7193f[3], meadow_serialize_result(meadow_events_436303a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bd8d0b2', 'events': 'meadow_events_a114d5c'}, 'handle_work_interval_ctl')
def meadow_handle_work_interval_ctl(meadow_parser_bd8d0b2, meadow_events_a114d5c):
    meadow_args_af7907b = meadow_events_a114d5c[0].values
    return meadow_BscWorkIntervalCtl(meadow_events_a114d5c, meadow_args_af7907b[0], meadow_args_af7907b[1], meadow_args_af7907b[2], meadow_args_af7907b[3], meadow_serialize_result(meadow_events_a114d5c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5b22404', 'events': 'meadow_events_9d4f170'}, 'handle_getentropy')
def meadow_handle_getentropy(meadow_parser_5b22404, meadow_events_9d4f170):
    meadow_args_a3a9c40 = meadow_events_9d4f170[0].values
    return meadow_BscGetentropy(meadow_events_9d4f170, meadow_args_a3a9c40[0], meadow_args_a3a9c40[1], meadow_serialize_result(meadow_events_9d4f170[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f7d83d4', 'events': 'meadow_events_646f8c9'}, 'handle_necp_open')
def meadow_handle_necp_open(meadow_parser_f7d83d4, meadow_events_646f8c9):
    meadow_args_1b13a3d = meadow_events_646f8c9[0].values
    return meadow_BscNecpOpen(meadow_events_646f8c9, meadow_args_1b13a3d[0], meadow_serialize_result(meadow_events_646f8c9[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9e2800e', 'events': 'meadow_events_7603487'}, 'handle_necp_client_action')
def meadow_handle_necp_client_action(meadow_parser_9e2800e, meadow_events_7603487):
    meadow_args_79b1ad4 = meadow_events_7603487[0].values
    return meadow_BscNecpClientAction(meadow_events_7603487, meadow_args_79b1ad4[0], meadow_args_79b1ad4[1], meadow_args_79b1ad4[2], meadow_args_79b1ad4[3], meadow_serialize_result(meadow_events_7603487[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_5463f72', 'events': 'meadow_events_b6e2bb6'}, 'handle_nexus_open')
def meadow_handle_nexus_open(meadow_parser_5463f72, meadow_events_b6e2bb6):
    return meadow_BscNexusOpen(meadow_events_b6e2bb6, meadow_serialize_result(meadow_events_b6e2bb6[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_79134fc', 'events': 'meadow_events_22808a5'}, 'handle_nexus_register')
def meadow_handle_nexus_register(meadow_parser_79134fc, meadow_events_22808a5):
    return meadow_BscNexusRegister(meadow_events_22808a5, meadow_serialize_result(meadow_events_22808a5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_140adbb', 'events': 'meadow_events_d7cf371'}, 'handle_nexus_deregister')
def meadow_handle_nexus_deregister(meadow_parser_140adbb, meadow_events_d7cf371):
    return meadow_BscNexusDeregister(meadow_events_d7cf371, meadow_serialize_result(meadow_events_d7cf371[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2a85a0e', 'events': 'meadow_events_d79f5f7'}, 'handle_nexus_create')
def meadow_handle_nexus_create(meadow_parser_2a85a0e, meadow_events_d79f5f7):
    return meadow_BscNexusCreate(meadow_events_d79f5f7, meadow_serialize_result(meadow_events_d79f5f7[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_600c588', 'events': 'meadow_events_f5ef06e'}, 'handle_nexus_destroy')
def meadow_handle_nexus_destroy(meadow_parser_600c588, meadow_events_f5ef06e):
    return meadow_BscNexusDestroy(meadow_events_f5ef06e, meadow_serialize_result(meadow_events_f5ef06e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8a21537', 'events': 'meadow_events_1dacc71'}, 'handle_nexus_get_opt')
def meadow_handle_nexus_get_opt(meadow_parser_8a21537, meadow_events_1dacc71):
    return meadow_BscNexusGetOpt(meadow_events_1dacc71, meadow_serialize_result(meadow_events_1dacc71[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_f517d21', 'events': 'meadow_events_b83caac'}, 'handle_nexus_set_opt')
def meadow_handle_nexus_set_opt(meadow_parser_f517d21, meadow_events_b83caac):
    return meadow_BscNexusSetOpt(meadow_events_b83caac, meadow_serialize_result(meadow_events_b83caac[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_72bdc65', 'events': 'meadow_events_c5878c2'}, 'handle_channel_open')
def meadow_handle_channel_open(meadow_parser_72bdc65, meadow_events_c5878c2):
    return meadow_BscChannelOpen(meadow_events_c5878c2, meadow_serialize_result(meadow_events_c5878c2[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d7a54d9', 'events': 'meadow_events_87cd2a5'}, 'handle_channel_get_info')
def meadow_handle_channel_get_info(meadow_parser_d7a54d9, meadow_events_87cd2a5):
    return meadow_BscChannelGetInfo(meadow_events_87cd2a5, meadow_serialize_result(meadow_events_87cd2a5[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9cc3ab2', 'events': 'meadow_events_e163069'}, 'handle_channel_sync')
def meadow_handle_channel_sync(meadow_parser_9cc3ab2, meadow_events_e163069):
    return meadow_BscChannelSync(meadow_events_e163069, meadow_serialize_result(meadow_events_e163069[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_cfd093d', 'events': 'meadow_events_312245a'}, 'handle_channel_get_opt')
def meadow_handle_channel_get_opt(meadow_parser_cfd093d, meadow_events_312245a):
    return meadow_BscChannelGetOpt(meadow_events_312245a, meadow_serialize_result(meadow_events_312245a[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_70ee2be', 'events': 'meadow_events_0b6d23b'}, 'handle_channel_set_opt')
def meadow_handle_channel_set_opt(meadow_parser_70ee2be, meadow_events_0b6d23b):
    return meadow_BscChannelSetOpt(meadow_events_0b6d23b, meadow_serialize_result(meadow_events_0b6d23b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_89a2332', 'events': 'meadow_events_e9077ed'}, 'handle_ulock_wait')
def meadow_handle_ulock_wait(meadow_parser_89a2332, meadow_events_e9077ed):
    meadow_args_0337a54 = meadow_events_e9077ed[0].values
    return meadow_BscUlockWait(meadow_events_e9077ed, meadow_args_0337a54[0], meadow_args_0337a54[1], meadow_args_0337a54[2], meadow_args_0337a54[3], meadow_serialize_result(meadow_events_e9077ed[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4805d5e', 'events': 'meadow_events_22914e5'}, 'handle_ulock_wake')
def meadow_handle_ulock_wake(meadow_parser_4805d5e, meadow_events_22914e5):
    meadow_args_d6c88bb = meadow_events_22914e5[0].values
    return meadow_BscUlockWake(meadow_events_22914e5, meadow_args_d6c88bb[0], meadow_args_d6c88bb[1], meadow_args_d6c88bb[2], meadow_serialize_result(meadow_events_22914e5[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_b4a320c', 'events': 'meadow_events_634e98c'}, 'handle_fclonefileat')
def meadow_handle_fclonefileat(meadow_parser_b4a320c, meadow_events_634e98c):
    meadow_args_397122f = meadow_events_634e98c[0].values
    return meadow_BscFclonefileat(meadow_events_634e98c, meadow_args_397122f[0], meadow_args_397122f[1], _name_boundary.attributes(meadow_parser_b4a320c)['parse_vnode'](meadow_events_634e98c).path, meadow_args_397122f[3], meadow_serialize_result(meadow_events_634e98c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_ee2aa14', 'events': 'meadow_events_ea31ccf'}, 'handle_fs_snapshot')
def meadow_handle_fs_snapshot(meadow_parser_ee2aa14, meadow_events_ea31ccf):
    meadow_nodes_ab95076 = _name_boundary.attributes(meadow_parser_ee2aa14)['parse_vnodes'](meadow_events_ea31ccf)
    meadow_name2_2f4578c = meadow_nodes_ab95076[1].path if len(meadow_nodes_ab95076) > 1 else ''
    meadow_args_2d30d1e = meadow_events_ea31ccf[0].values
    return meadow_BscFsSnapshot(meadow_events_ea31ccf, meadow_FsSnapshotOp(meadow_args_2d30d1e[0]), meadow_args_2d30d1e[1], meadow_nodes_ab95076[0].path, meadow_name2_2f4578c, meadow_serialize_result(meadow_events_ea31ccf[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4e45a8d', 'events': 'meadow_events_f042d4f'}, 'handle_terminate_with_payload')
def meadow_handle_terminate_with_payload(meadow_parser_4e45a8d, meadow_events_f042d4f):
    meadow_args_a5a0f80 = meadow_events_f042d4f[0].values
    return meadow_BscTerminateWithPayload(meadow_events_f042d4f, meadow_args_a5a0f80[0], meadow_args_a5a0f80[1], meadow_args_a5a0f80[2], meadow_args_a5a0f80[3], meadow_serialize_result(meadow_events_f042d4f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_e9d7e12', 'events': 'meadow_events_ce1e066'}, 'handle_abort_with_payload')
def meadow_handle_abort_with_payload(meadow_parser_e9d7e12, meadow_events_ce1e066):
    meadow_args_b5edd48 = meadow_events_ce1e066[0].values
    return meadow_BscAbortWithPayload(meadow_events_ce1e066, meadow_args_b5edd48[0], meadow_args_b5edd48[1], meadow_args_b5edd48[2], meadow_args_b5edd48[3])

@_name_boundary.callable_contract({'parser': 'meadow_parser_a4fc7ce', 'events': 'meadow_events_bc75f34'}, 'handle_necp_session_open')
def meadow_handle_necp_session_open(meadow_parser_a4fc7ce, meadow_events_bc75f34):
    meadow_args_c4aff20 = meadow_events_bc75f34[0].values
    return meadow_BscNecpSessionOpen(meadow_events_bc75f34, meadow_args_c4aff20[0], meadow_serialize_result(meadow_events_bc75f34[-1], 'fd'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2e6ed2f', 'events': 'meadow_events_2a49599'}, 'handle_necp_session_action')
def meadow_handle_necp_session_action(meadow_parser_2e6ed2f, meadow_events_2a49599):
    meadow_args_99f3fdb = meadow_events_2a49599[0].values
    return meadow_BscNecpSessionAction(meadow_events_2a49599, meadow_args_99f3fdb[0], meadow_args_99f3fdb[1], meadow_args_99f3fdb[2], meadow_args_99f3fdb[3], meadow_serialize_result(meadow_events_2a49599[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_31bea0c', 'events': 'meadow_events_443763c'}, 'handle_setattrlistat')
def meadow_handle_setattrlistat(meadow_parser_31bea0c, meadow_events_443763c):
    meadow_args_f01b801 = meadow_events_443763c[0].values
    return meadow_BscSetattrlistat(meadow_events_443763c, meadow_args_f01b801[0], _name_boundary.attributes(meadow_parser_31bea0c)['parse_vnode'](meadow_events_443763c).path, meadow_args_f01b801[2], meadow_args_f01b801[3], meadow_serialize_result(meadow_events_443763c[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_9991a87', 'events': 'meadow_events_f6170be'}, 'handle_net_qos_guideline')
def meadow_handle_net_qos_guideline(meadow_parser_9991a87, meadow_events_f6170be):
    meadow_args_84c1b0d = meadow_events_f6170be[0].values
    return meadow_BscNetQosGuideline(meadow_events_f6170be, meadow_args_84c1b0d[0], meadow_args_84c1b0d[1], meadow_serialize_result(meadow_events_f6170be[-1], 'background'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_2a954b4', 'events': 'meadow_events_2827033'}, 'handle_fmount')
def meadow_handle_fmount(meadow_parser_2a954b4, meadow_events_2827033):
    meadow_args_aef06ce = meadow_events_2827033[0].values
    return meadow_BscFmount(meadow_events_2827033, meadow_args_aef06ce[0], meadow_args_aef06ce[1], meadow_args_aef06ce[2], meadow_args_aef06ce[3], meadow_serialize_result(meadow_events_2827033[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d9bd9c7', 'events': 'meadow_events_b3ac3dc'}, 'handle_ntp_adjtime')
def meadow_handle_ntp_adjtime(meadow_parser_d9bd9c7, meadow_events_b3ac3dc):
    meadow_args_99f241a = meadow_events_b3ac3dc[0].values
    return meadow_BscNtpAdjtime(meadow_events_b3ac3dc, meadow_args_99f241a[0], meadow_serialize_result(meadow_events_b3ac3dc[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_63790ee', 'events': 'meadow_events_29ed22e'}, 'handle_ntp_gettime')
def meadow_handle_ntp_gettime(meadow_parser_63790ee, meadow_events_29ed22e):
    meadow_args_8cfd572 = meadow_events_29ed22e[0].values
    return meadow_BscNtpGettime(meadow_events_29ed22e, meadow_args_8cfd572[0], meadow_serialize_result(meadow_events_29ed22e[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_d08d532', 'events': 'meadow_events_5d6c689'}, 'handle_os_fault_with_payload')
def meadow_handle_os_fault_with_payload(meadow_parser_d08d532, meadow_events_5d6c689):
    meadow_args_dab2c0b = meadow_events_5d6c689[0].values
    return meadow_BscOsFaultWithPayload(meadow_events_5d6c689, meadow_args_dab2c0b[0], meadow_args_dab2c0b[1], meadow_args_dab2c0b[2], meadow_args_dab2c0b[3], meadow_serialize_result(meadow_events_5d6c689[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_aa18ee7', 'events': 'meadow_events_e243a2b'}, 'handle_kqueue_workloop_ctl')
def meadow_handle_kqueue_workloop_ctl(meadow_parser_aa18ee7, meadow_events_e243a2b):
    meadow_args_517a942 = meadow_events_e243a2b[0].values
    return meadow_BscKqueueWorkloopCtl(meadow_events_e243a2b, meadow_args_517a942[0], meadow_args_517a942[1], meadow_args_517a942[2], meadow_args_517a942[3], meadow_serialize_result(meadow_events_e243a2b[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_a8dfd5b', 'events': 'meadow_events_c4b120d'}, 'handle_mach_bridge_remote_time')
def meadow_handle_mach_bridge_remote_time(meadow_parser_a8dfd5b, meadow_events_c4b120d):
    meadow_args_ab46210 = meadow_events_c4b120d[0].values
    return meadow_BscMachBridgeRemoteTime(meadow_events_c4b120d, meadow_args_ab46210[0], meadow_serialize_result(meadow_events_c4b120d[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_29094ee', 'events': 'meadow_events_d500040'}, 'handle_coalition_ledger')
def meadow_handle_coalition_ledger(meadow_parser_29094ee, meadow_events_d500040):
    meadow_args_3b3d31b = meadow_events_d500040[0].values
    return meadow_BscCoalitionLedger(meadow_events_d500040, meadow_args_3b3d31b[0], meadow_args_3b3d31b[1], meadow_args_3b3d31b[2], meadow_args_3b3d31b[3], meadow_serialize_result(meadow_events_d500040[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_8a04d89', 'events': 'meadow_events_12cc993'}, 'handle_log_data')
def meadow_handle_log_data(meadow_parser_8a04d89, meadow_events_12cc993):
    meadow_args_5a9d733 = meadow_events_12cc993[0].values
    return meadow_BscLogData(meadow_events_12cc993, meadow_args_5a9d733[0], meadow_args_5a9d733[1], meadow_args_5a9d733[2], meadow_args_5a9d733[3], meadow_serialize_result(meadow_events_12cc993[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_4adb58c', 'events': 'meadow_events_1028dd9'}, 'handle_memorystatus_available_memory')
def meadow_handle_memorystatus_available_memory(meadow_parser_4adb58c, meadow_events_1028dd9):
    return meadow_BscMemorystatusAvailableMemory(meadow_events_1028dd9, meadow_serialize_result(meadow_events_1028dd9[-1], 'count'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_693ab6b', 'events': 'meadow_events_98610ba'}, 'handle_shared_region_map_and_slide_2_np')
def meadow_handle_shared_region_map_and_slide_2_np(meadow_parser_693ab6b, meadow_events_98610ba):
    meadow_args_7e515e8 = meadow_events_98610ba[0].values
    return meadow_BscSharedRegionMapAndSlide2Np(meadow_events_98610ba, meadow_args_7e515e8[0], meadow_args_7e515e8[1], meadow_args_7e515e8[2], meadow_args_7e515e8[3], meadow_serialize_result(meadow_events_98610ba[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_14c2537', 'events': 'meadow_events_b0103a4'}, 'handle_pivot_root')
def meadow_handle_pivot_root(meadow_parser_14c2537, meadow_events_b0103a4):
    meadow_nodes_d0ca49d = _name_boundary.attributes(meadow_parser_14c2537)['parse_vnodes'](meadow_events_b0103a4)
    meadow_path1_75efb57, meadow_path2_9bd546a = (meadow_nodes_d0ca49d[0].path, meadow_nodes_d0ca49d[1].path) if meadow_nodes_d0ca49d else ('', '')
    return meadow_BscPivotRoot(meadow_events_b0103a4, meadow_path1_75efb57, meadow_path2_9bd546a, meadow_serialize_result(meadow_events_b0103a4[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_60c8bd7', 'events': 'meadow_events_f2a167f'}, 'handle_task_inspect_for_pid')
def meadow_handle_task_inspect_for_pid(meadow_parser_60c8bd7, meadow_events_f2a167f):
    meadow_args_5d1b2f5 = meadow_events_f2a167f[0].values
    return meadow_BscTaskInspectForPid(meadow_events_f2a167f, meadow_args_5d1b2f5[0], meadow_args_5d1b2f5[1], meadow_args_5d1b2f5[2], meadow_serialize_result(meadow_events_f2a167f[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_bed9f21', 'events': 'meadow_events_e4972b3'}, 'handle_task_read_for_pid')
def meadow_handle_task_read_for_pid(meadow_parser_bed9f21, meadow_events_e4972b3):
    meadow_args_b454d57 = meadow_events_e4972b3[0].values
    return meadow_BscTaskReadForPid(meadow_events_e4972b3, meadow_args_b454d57[0], meadow_args_b454d57[1], meadow_args_b454d57[2], meadow_serialize_result(meadow_events_e4972b3[-1]))

@_name_boundary.callable_contract({'parser': 'meadow_parser_1bd473d', 'events': 'meadow_events_e144310', 'no_cancel': 'meadow_no_cancel_d9920a9'}, 'handle_sys_preadv')
def meadow_handle_sys_preadv(meadow_parser_1bd473d, meadow_events_e144310, meadow_no_cancel_d9920a9=False):
    meadow_args_629ffdb = meadow_events_e144310[0].values
    return meadow_BscSysPreadv(meadow_events_e144310, meadow_args_629ffdb[0], meadow_args_629ffdb[1], meadow_args_629ffdb[2], meadow_ctypes.c_int64(meadow_args_629ffdb[0]).value, meadow_serialize_result(meadow_events_e144310[-1], 'count'), meadow_no_cancel_d9920a9)

@_name_boundary.callable_contract({'parser': 'meadow_parser_a5982b5', 'events': 'meadow_events_f9094c5', 'no_cancel': 'meadow_no_cancel_2dd7aae'}, 'handle_sys_pwritev')
def meadow_handle_sys_pwritev(meadow_parser_a5982b5, meadow_events_f9094c5, meadow_no_cancel_2dd7aae=False):
    meadow_args_37f2559 = meadow_events_f9094c5[0].values
    return meadow_BscSysPwritev(meadow_events_f9094c5, meadow_args_37f2559[0], meadow_args_37f2559[1], meadow_args_37f2559[2], meadow_ctypes.c_int64(meadow_args_37f2559[0]).value, meadow_serialize_result(meadow_events_f9094c5[-1], 'count'), meadow_no_cancel_2dd7aae)

@_name_boundary.callable_contract({'parser': 'meadow_parser_c168f39', 'events': 'meadow_events_cc8fa8b'}, 'handle_ulock_wait2')
def meadow_handle_ulock_wait2(meadow_parser_c168f39, meadow_events_cc8fa8b):
    meadow_args_d349331 = meadow_events_cc8fa8b[0].values
    return meadow_BscUlockWait2(meadow_events_cc8fa8b, meadow_args_d349331[0], meadow_args_d349331[1], meadow_args_d349331[2], meadow_args_d349331[3], meadow_serialize_result(meadow_events_cc8fa8b[-1], 'return'))

@_name_boundary.callable_contract({'parser': 'meadow_parser_fb5fc29', 'events': 'meadow_events_57d6408'}, 'handle_proc_info_extended_id')
def meadow_handle_proc_info_extended_id(meadow_parser_fb5fc29, meadow_events_57d6408):
    meadow_args_2f52c8d = meadow_events_57d6408[0].values
    return meadow_BscProcInfoExtendedId(meadow_events_57d6408, meadow_args_2f52c8d[0], meadow_args_2f52c8d[1], meadow_args_2f52c8d[2], meadow_args_2f52c8d[3], meadow_serialize_result(meadow_events_57d6408[-1]))
meadow_handlers = {'BSC_read': meadow_handle_read, 'BSC_write': meadow_handle_write, 'BSC_open': meadow_handle_open, 'BSC_sys_close': meadow_handle_sys_close, 'BSC_link': meadow_handle_link, 'BSC_unlink': meadow_handle_unlink, 'BSC_chdir': meadow_handle_chdir, 'BSC_fchdir': meadow_handle_fchdir, 'BSC_mknod': meadow_handle_mknod, 'BSC_chmod': meadow_handle_chmod, 'BSC_chown': meadow_handle_chown, 'BSC_getpid': meadow_handle_getpid, 'BSC_setuid': meadow_handle_setuid, 'BSC_getuid': meadow_handle_getuid, 'BSC_geteuid': meadow_handle_geteuid, 'BSC_recvmsg': meadow_handle_recvmsg, 'BSC_sendmsg': meadow_handle_sendmsg, 'BSC_recvfrom': meadow_handle_recvfrom, 'BSC_accept': meadow_handle_accept, 'BSC_getpeername': meadow_handle_getpeername, 'BSC_getsockname': meadow_handle_getsockname, 'BSC_access': meadow_handle_access, 'BSC_chflags': meadow_handle_chflags, 'BSC_fchflags': meadow_handle_fchflags, 'BSC_sync': meadow_handle_sync, 'BSC_kill': meadow_handle_kill, 'BSC_getppid': meadow_handle_getppid, 'BSC_sys_dup': meadow_handle_sys_dup, 'BSC_pipe': meadow_handle_pipe, 'BSC_getegid': meadow_handle_getegid, 'BSC_sigaction': meadow_handle_sigaction, 'BSC_getgid': meadow_handle_getgid, 'BSC_sigprocmask': meadow_handle_sigprocmask, 'BSC_getlogin': meadow_handle_getlogin, 'BSC_setlogin': meadow_handle_setlogin, 'BSC_acct': meadow_handle_acct, 'BSC_sigpending': meadow_handle_sigpending, 'BSC_sigaltstack': meadow_handle_sigaltstack, 'BSC_ioctl': meadow_handle_ioctl, 'BSC_reboot': meadow_handle_reboot, 'BSC_revoke': meadow_handle_revoke, 'BSC_symlink': meadow_handle_symlink, 'BSC_readlink': meadow_handle_readlink, 'BSC_execve': meadow_handle_execve, 'BSC_umask': meadow_handle_umask, 'BSC_chroot': meadow_handle_chroot, 'BSC_msync': meadow_handle_msync, 'BSC_vfork': meadow_handle_vfork, 'BSC_munmap': meadow_handle_munmap, 'BSC_mprotect': meadow_handle_mprotect, 'BSC_madvise': meadow_handle_madvise, 'BSC_mincore': meadow_handle_mincore, 'BSC_getgroups': meadow_handle_getgroups, 'BSC_setgroups': meadow_handle_setgroups, 'BSC_getpgrp': meadow_handle_getpgrp, 'BSC_setpgid': meadow_handle_setpgid, 'BSC_setitimer': meadow_handle_setitimer, 'BSC_swapon': meadow_handle_swapon, 'BSC_getitimer': meadow_handle_getitimer, 'BSC_sys_getdtablesize': meadow_handle_sys_getdtablesize, 'BSC_sys_dup2': meadow_handle_sys_dup2, 'BSC_sys_fcntl': meadow_handle_sys_fcntl, 'BSC_select': meadow_handle_select, 'BSC_fsync': meadow_handle_fsync, 'BSC_setpriority': meadow_handle_setpriority, 'BSC_socket': meadow_handle_socket, 'BSC_connect': meadow_handle_connect, 'BSC_getpriority': meadow_handle_getpriority, 'BSC_bind': meadow_handle_bind, 'BSC_setsockopt': meadow_handle_setsockopt, 'BSC_listen': meadow_handle_listen, 'BSC_sigsuspend': meadow_handle_sigsuspend, 'BSC_gettimeofday': meadow_handle_gettimeofday, 'BSC_getrusage': meadow_handle_getrusage, 'BSC_getsockopt': meadow_handle_getsockopt, 'BSC_readv': meadow_handle_readv, 'BSC_writev': meadow_handle_writev, 'BSC_settimeofday': meadow_handle_settimeofday, 'BSC_fchown': meadow_handle_fchown, 'BSC_fchmod': meadow_handle_fchmod, 'BSC_setreuid': meadow_handle_setreuid, 'BSC_setregid': meadow_handle_setregid, 'BSC_rename': meadow_handle_rename, 'BSC_sys_flock': meadow_handle_sys_flock, 'BSC_mkfifo': meadow_handle_mkfifo, 'BSC_sendto': meadow_handle_sendto, 'BSC_shutdown': meadow_handle_shutdown, 'BSC_socketpair': meadow_handle_socketpair, 'BSC_mkdir': meadow_handle_mkdir, 'BSC_rmdir': meadow_handle_rmdir, 'BSC_utimes': meadow_handle_utimes, 'BSC_futimes': meadow_handle_futimes, 'BSC_adjtime': meadow_handle_adjtime, 'BSC_gethostuuid': meadow_handle_gethostuuid, 'BSC_obs_killpg': meadow_handle_obs_killpg, 'BSC_setsid': meadow_handle_setsid, 'BSC_getpgid': meadow_handle_getpgid, 'BSC_setprivexec': meadow_handle_setprivexec, 'BSC_pread': meadow_handle_pread, 'BSC_pwrite': meadow_handle_pwrite, 'BSC_nfssvc': meadow_handle_nfssvc, 'BSC_statfs': meadow_handle_statfs, 'BSC_fstatfs': meadow_handle_fstatfs, 'BSC_unmount': meadow_handle_unmount, 'BSC_getfh': meadow_handle_getfh, 'BSC_quotactl': meadow_handle_quotactl, 'BSC_mount': meadow_handle_mount, 'BSC_csops': meadow_handle_csops, 'BSC_csops_audittoken': meadow_handle_csops_audittoken, 'BSC_waitid': meadow_handle_waitid, 'BSC_kdebug_typefilter': meadow_handle_kdebug_typefilter, 'BSC_setgid': meadow_handle_setgid, 'BSC_setegid': meadow_handle_setegid, 'BSC_seteuid': meadow_handle_seteuid, 'BSC_thread_selfcounts': meadow_handle_thread_selfcounts, 'BSC_fdatasync': meadow_handle_fdatasync, 'BSC_pathconf': meadow_handle_pathconf, 'BSC_sys_fpathconf': meadow_handle_sys_fpathconf, 'BSC_getrlimit': meadow_handle_getrlimit, 'BSC_setrlimit': meadow_handle_setrlimit, 'BSC_getdirentries': meadow_handle_getdirentries, 'BSC_mmap': meadow_handle_mmap, 'BSC_lseek': meadow_handle_lseek, 'BSC_truncate': meadow_handle_truncate, 'BSC_ftruncate': meadow_handle_ftruncate, 'BSC_sysctl': meadow_handle_sysctl, 'BSC_mlock': meadow_handle_mlock, 'BSC_munlock': meadow_handle_munlock, 'BSC_undelete': meadow_handle_undelete, 'BSC_open_dprotected_np': meadow_handle_open_dprotected_np, 'BSC_getattrlist': meadow_handle_getattrlist, 'BSC_setattrlist': meadow_handle_setattrlist, 'BSC_getdirentriesattr': meadow_handle_getdirentriesattr, 'BSC_exchangedata': meadow_handle_exchangedata, 'BSC_searchfs': meadow_handle_searchfs, 'BSC_fgetattrlist': meadow_handle_fgetattrlist, 'BSC_fsetattrlist': meadow_handle_fsetattrlist, 'BSC_poll': meadow_handle_poll, 'BSC_getxattr': meadow_handle_getxattr, 'BSC_fgetxattr': meadow_handle_fgetxattr, 'BSC_setxattr': meadow_handle_setxattr, 'BSC_fsetxattr': meadow_handle_fsetxattr, 'BSC_removexattr': meadow_handle_removexattr, 'BSC_fremovexattr': meadow_handle_fremovexattr, 'BSC_listxattr': meadow_handle_listxattr, 'BSC_flistxattr': meadow_handle_flistxattr, 'BSC_fsctl': meadow_handle_fsctl, 'BSC_initgroups': meadow_handle_initgroups, 'BSC_posix_spawn': meadow_handle_posix_spawn, 'BSC_ffsctl': meadow_handle_ffsctl, 'BSC_nfsclnt': meadow_handle_nfsclnt, 'BSC_fhopen': meadow_handle_fhopen, 'BSC_minherit': meadow_handle_minherit, 'BSC_semsys': meadow_handle_semsys, 'BSC_msgsys': meadow_handle_msgsys, 'BSC_shmsys': meadow_handle_shmsys, 'BSC_semctl': meadow_handle_semctl, 'BSC_semget': meadow_handle_semget, 'BSC_semop': meadow_handle_semop, 'BSC_msgctl': meadow_handle_msgctl, 'BSC_msgget': meadow_handle_msgget, 'BSC_msgsnd': meadow_handle_msgsnd, 'BSC_msgrcv': meadow_handle_msgrcv, 'BSC_shmat': meadow_handle_shmat, 'BSC_shmctl': meadow_handle_shmctl, 'BSC_shmdt': meadow_handle_shmdt, 'BSC_shmget': meadow_handle_shmget, 'BSC_shm_open': meadow_handle_shm_open, 'BSC_shm_unlink': meadow_handle_shm_unlink, 'BSC_sem_open': meadow_handle_sem_open, 'BSC_sem_close': meadow_handle_sem_close, 'BSC_sem_unlink': meadow_handle_sem_unlink, 'BSC_sem_wait': meadow_handle_sem_wait, 'BSC_sem_trywait': meadow_handle_sem_trywait, 'BSC_sem_post': meadow_handle_sem_post, 'BSC_sys_sysctlbyname': meadow_handle_sys_sysctlbyname, 'BSC_access_extended': meadow_handle_access_extended, 'BSC_gettid': meadow_handle_gettid, 'BSC_shared_region_check_np': meadow_handle_shared_region_check_np, 'BSC_psynch_mutexwait': meadow_handle_psynch_mutexwait, 'BSC_psynch_mutexdrop': meadow_handle_psynch_mutexdrop, 'BSC_psynch_cvbroad': meadow_handle_psynch_cvbroad, 'BSC_psynch_cvsignal': meadow_handle_psynch_cvsignal, 'BSC_psynch_cvwait': meadow_handle_psynch_cvwait, 'BSC_getsid': meadow_handle_getsid, 'BSC_psynch_cvclrprepost': meadow_handle_psynch_cvclrprepost, 'BSC_iopolicysys': meadow_handle_iopolicysys, 'BSC_process_policy': meadow_handle_process_policy, 'BSC_mlockall': meadow_handle_mlockall, 'BSC_munlockall': meadow_handle_munlockall, 'BSC_issetugid': meadow_handle_issetugid, 'BSC_pthread_sigmask': meadow_handle_pthread_sigmask, 'BSC_disable_threadsignal': meadow_handle_disable_threadsignal, 'BSC_semwait_signal': meadow_handle_semwait_signal, 'BSC_proc_info': meadow_handle_proc_info, 'BSC_sendfile': meadow_handle_sendfile, 'BSC_stat64': meadow_handle_stat64, 'BSC_sys_fstat64': meadow_handle_sys_fstat64, 'BSC_lstat64': meadow_handle_lstat64, 'BSC_getdirentries64': meadow_handle_getdirentries64, 'BSC_statfs64': meadow_handle_statfs64, 'BSC_fstatfs64': meadow_handle_fstatfs64, 'BSC_getfsstat64': meadow_handle_getfsstat64, 'BSC_pthread_fchdir': meadow_handle_pthread_fchdir, 'BSC_audit': meadow_handle_audit, 'BSC_auditon': meadow_handle_auditon, 'BSC_getauid': meadow_handle_getauid, 'BSC_setauid': meadow_handle_setauid, 'BSC_bsdthread_create': meadow_handle_bsdthread_create, 'BSC_kqueue': meadow_handle_kqueue, 'BSC_kevent': meadow_handle_kevent, 'BSC_lchown': meadow_handle_lchown, 'BSC_bsdthread_register': meadow_handle_bsdthread_register, 'BSC_workq_open': meadow_handle_workq_open, 'BSC_workq_kernreturn': meadow_handle_workq_kernreturn, 'BSC_kevent64': meadow_handle_kevent64, 'BSC_thread_selfid': meadow_handle_thread_selfid, 'BSC_kevent_qos': meadow_handle_kevent_qos, 'BSC_kevent_id': meadow_handle_kevent_id, 'BSC_mac_syscall': meadow_handle_mac_syscall, 'BSC_pselect': meadow_handle_pselect, 'BSC_pselect_nocancel': meadow_partial(meadow_handle_pselect, no_cancel=True), 'BSC_read_nocancel': meadow_partial(meadow_handle_read, no_cancel=True), 'BSC_write_nocancel': meadow_partial(meadow_handle_write, no_cancel=True), 'BSC_open_nocancel': meadow_partial(meadow_handle_open, no_cancel=True), 'BSC_sys_close_nocancel': meadow_partial(meadow_handle_sys_close, no_cancel=True), 'BSC_wait4_nocancel': meadow_partial(meadow_handle_wait4, no_cancel=True), 'BSC_recvmsg_nocancel': meadow_partial(meadow_handle_recvmsg, no_cancel=True), 'BSC_sendmsg_nocancel': meadow_partial(meadow_handle_sendmsg, no_cancel=True), 'BSC_recvfrom_nocancel': meadow_partial(meadow_handle_recvfrom, no_cancel=True), 'BSC_accept_nocancel': meadow_partial(meadow_handle_accept, no_cancel=True), 'BSC_msync_nocancel': meadow_partial(meadow_handle_msync, no_cancel=True), 'BSC_sys_fcntl_nocancel': meadow_partial(meadow_handle_sys_fcntl, no_cancel=True), 'BSC_select_nocancel': meadow_partial(meadow_handle_select, no_cancel=True), 'BSC_fsync_nocancel': meadow_partial(meadow_handle_fsync, no_cancel=True), 'BSC_connect_nocancel': meadow_partial(meadow_handle_connect, no_cancel=True), 'BSC_sigsuspend_nocancel': meadow_partial(meadow_handle_sigsuspend, no_cancel=True), 'BSC_readv_nocancel': meadow_partial(meadow_handle_readv, no_cancel=True), 'BSC_writev_nocancel': meadow_partial(meadow_handle_writev, no_cancel=True), 'BSC_sendto_nocancel': meadow_partial(meadow_handle_sendto, no_cancel=True), 'BSC_pread_nocancel': meadow_partial(meadow_handle_pread, no_cancel=True), 'BSC_pwrite_nocancel': meadow_partial(meadow_handle_pwrite, no_cancel=True), 'BSC_waitid_nocancel': meadow_partial(meadow_handle_waitid, no_cancel=True), 'BSC_poll_nocancel': meadow_partial(meadow_handle_poll, no_cancel=True), 'BSC_msgsnd_nocancel': meadow_partial(meadow_handle_msgsnd, no_cancel=True), 'BSC_msgrcv_nocancel': meadow_partial(meadow_handle_msgrcv, no_cancel=True), 'BSC_sem_wait_nocancel': meadow_partial(meadow_handle_sem_wait, no_cancel=True), 'BSC_semwait_signal_nocancel': meadow_partial(meadow_handle_semwait_signal, no_cancel=True), 'BSC_fsgetpath': meadow_handle_fsgetpath, 'BSC_sys_fileport_makeport': meadow_handle_sys_fileport_makeport, 'BSC_sys_fileport_makefd': meadow_handle_sys_fileport_makefd, 'BSC_audit_session_port': meadow_handle_audit_session_port, 'BSC_pid_suspend': meadow_handle_pid_suspend, 'BSC_pid_resume': meadow_handle_pid_resume, 'BSC_pid_hibernate': meadow_handle_pid_hibernate, 'BSC_pid_shutdown_sockets': meadow_handle_pid_shutdown_sockets, 'BSC_shared_region_map_and_slide_np': meadow_handle_shared_region_map_and_slide_np, 'BSC_kas_info': meadow_handle_kas_info, 'BSC_memorystatus_control': meadow_handle_memorystatus_control, 'BSC_guarded_open_np': meadow_handle_guarded_open_np, 'BSC_guarded_close_np': meadow_handle_guarded_close_np, 'BSC_guarded_kqueue_np': meadow_handle_guarded_kqueue_np, 'BSC_change_fdguard_np': meadow_handle_change_fdguard_np, 'BSC_usrctl': meadow_handle_usrctl, 'BSC_proc_rlimit_control': meadow_handle_proc_rlimit_control, 'BSC_connectx': meadow_handle_connectx, 'BSC_disconnectx': meadow_handle_disconnectx, 'BSC_peeloff': meadow_handle_peeloff, 'BSC_socket_delegate': meadow_handle_socket_delegate, 'BSC_telemetry': meadow_handle_telemetry, 'BSC_proc_uuid_policy': meadow_handle_proc_uuid_policy, 'BSC_memorystatus_get_level': meadow_handle_memorystatus_get_level, 'BSC_system_override': meadow_handle_system_override, 'BSC_vfs_purge': meadow_handle_vfs_purge, 'BSC_sfi_ctl': meadow_handle_sfi_ctl, 'BSC_sfi_pidctl': meadow_handle_sfi_pidctl, 'BSC_coalition': meadow_handle_coalition, 'BSC_coalition_info': meadow_handle_coalition_info, 'BSC_necp_match_policy': meadow_handle_necp_match_policy, 'BSC_getattrlistbulk': meadow_handle_getattrlistbulk, 'BSC_clonefileat': meadow_handle_clonefileat, 'BSC_openat': meadow_handle_openat, 'BSC_openat_nocancel': meadow_partial(meadow_handle_openat, no_cancel=True), 'BSC_renameat': meadow_handle_renameat, 'BSC_faccessat': meadow_handle_faccessat, 'BSC_fchmodat': meadow_handle_fchmodat, 'BSC_fchownat': meadow_handle_fchownat, 'BSC_fstatat': meadow_handle_fstatat, 'BSC_fstatat64': meadow_handle_fstatat64, 'BSC_linkat': meadow_handle_linkat, 'BSC_unlinkat': meadow_handle_unlinkat, 'BSC_readlinkat': meadow_handle_readlinkat, 'BSC_symlinkat': meadow_handle_symlinkat, 'BSC_mkdirat': meadow_handle_mkdirat, 'BSC_getattrlistat': meadow_handle_getattrlistat, 'BSC_proc_trace_log': meadow_handle_proc_trace_log, 'BSC_bsdthread_ctl': meadow_handle_bsdthread_ctl, 'BSC_openbyid_np': meadow_handle_openbyid_np, 'BSC_recvmsg_x': meadow_handle_recvmsg_x, 'BSC_sendmsg_x': meadow_handle_sendmsg_x, 'BSC_thread_selfusage': meadow_handle_thread_selfusage, 'BSC_csrctl': meadow_handle_csrctl, 'BSC_guarded_open_dprotected_np': meadow_handle_guarded_open_dprotected_np, 'BSC_guarded_write_np': meadow_handle_guarded_write_np, 'BSC_guarded_pwrite_np': meadow_handle_guarded_pwrite_np, 'BSC_guarded_writev_np': meadow_handle_guarded_writev_np, 'BSC_renameatx_np': meadow_handle_renameatx_np, 'BSC_mremap_encrypted': meadow_handle_mremap_encrypted, 'BSC_netagent_trigger': meadow_handle_netagent_trigger, 'BSC_stack_snapshot_with_config': meadow_handle_stack_snapshot_with_config, 'BSC_microstackshot': meadow_handle_microstackshot, 'BSC_grab_pgo_data': meadow_handle_grab_pgo_data, 'BSC_persona': meadow_handle_persona, 'BSC_mach_eventlink_signal': meadow_handle_mach_eventlink_signal, 'BSC_mach_eventlink_wait_until': meadow_handle_mach_eventlink_wait_until, 'BSC_mach_eventlink_signal_wait_until': meadow_handle_mach_eventlink_signal_wait_until, 'BSC_work_interval_ctl': meadow_handle_work_interval_ctl, 'BSC_getentropy': meadow_handle_getentropy, 'BSC_necp_open': meadow_handle_necp_open, 'BSC_necp_client_action': meadow_handle_necp_client_action, 'BSC_nexus_open': meadow_handle_nexus_open, 'BSC_nexus_register': meadow_handle_nexus_register, 'BSC_nexus_deregister': meadow_handle_nexus_deregister, 'BSC_nexus_create': meadow_handle_nexus_create, 'BSC_nexus_destroy': meadow_handle_nexus_destroy, 'BSC_nexus_get_opt': meadow_handle_nexus_get_opt, 'BSC_nexus_set_opt': meadow_handle_nexus_set_opt, 'BSC_channel_open': meadow_handle_channel_open, 'BSC_channel_get_info': meadow_handle_channel_get_info, 'BSC_channel_sync': meadow_handle_channel_sync, 'BSC_channel_get_opt': meadow_handle_channel_get_opt, 'BSC_channel_set_opt': meadow_handle_channel_set_opt, 'BSC_ulock_wait': meadow_handle_ulock_wait, 'BSC_ulock_wake': meadow_handle_ulock_wake, 'BSC_fclonefileat': meadow_handle_fclonefileat, 'BSC_fs_snapshot': meadow_handle_fs_snapshot, 'BSC_terminate_with_payload': meadow_handle_terminate_with_payload, 'BSC_abort_with_payload': meadow_handle_abort_with_payload, 'BSC_necp_session_open': meadow_handle_necp_session_open, 'BSC_necp_session_action': meadow_handle_necp_session_action, 'BSC_setattrlistat': meadow_handle_setattrlistat, 'BSC_net_qos_guideline': meadow_handle_net_qos_guideline, 'BSC_fmount': meadow_handle_fmount, 'BSC_ntp_adjtime': meadow_handle_ntp_adjtime, 'BSC_ntp_gettime': meadow_handle_ntp_gettime, 'BSC_os_fault_with_payload': meadow_handle_os_fault_with_payload, 'BSC_kqueue_workloop_ctl': meadow_handle_kqueue_workloop_ctl, 'BSC_mach_bridge_remote_time': meadow_handle_mach_bridge_remote_time, 'BSC_coalition_ledger': meadow_handle_coalition_ledger, 'BSC_log_data': meadow_handle_log_data, 'BSC_memorystatus_available_memory': meadow_handle_memorystatus_available_memory, 'BSC_shared_region_map_and_slide_2_np': meadow_handle_shared_region_map_and_slide_2_np, 'BSC_pivot_root': meadow_handle_pivot_root, 'BSC_task_inspect_for_pid': meadow_handle_task_inspect_for_pid, 'BSC_task_read_for_pid': meadow_handle_task_read_for_pid, 'BSC_sys_preadv': meadow_handle_sys_preadv, 'BSC_sys_pwritev': meadow_handle_sys_pwritev, 'BSC_sys_preadv_nocancel': meadow_partial(meadow_handle_sys_preadv, no_cancel=True), 'BSC_sys_pwritev_nocancel': meadow_partial(meadow_handle_sys_pwritev, no_cancel=True), 'BSC_ulock_wait2': meadow_handle_ulock_wait2, 'BSC_proc_info_extended_id': meadow_handle_proc_info_extended_id}
_name_boundary.module_contract(globals(), {'handle_sendmsg_x': 'meadow_handle_sendmsg_x', 'BscGettid': 'meadow_BscGettid', 'handle_chown': 'meadow_handle_chown', 'BscSemUnlink': 'meadow_BscSemUnlink', 'handle_gettimeofday': 'meadow_handle_gettimeofday', 'BscSemwaitSignal': 'meadow_BscSemwaitSignal', 'BscChannelGetInfo': 'meadow_BscChannelGetInfo', 'handle_renameatx_np': 'meadow_handle_renameatx_np', 'serialize_result': 'meadow_serialize_result', 'BscSync': 'meadow_BscSync', 'handle_faccessat': 'meadow_handle_faccessat', 'BscGetattrlistbulk': 'meadow_BscGetattrlistbulk', 'handle_necp_session_open': 'meadow_handle_necp_session_open', 'BscGetattrlistat': 'meadow_BscGetattrlistat', 'handle_recvfrom': 'meadow_handle_recvfrom', 'handle_setsockopt': 'meadow_handle_setsockopt', 'BscAdjtime': 'meadow_BscAdjtime', 'BscGuardedWritevNp': 'meadow_BscGuardedWritevNp', 'BscThreadSelfusage': 'meadow_BscThreadSelfusage', 'handle_pread': 'meadow_handle_pread', 'handle_fstatfs': 'meadow_handle_fstatfs', 'handle_psynch_cvwait': 'meadow_handle_psynch_cvwait', 'handle_unlinkat': 'meadow_handle_unlinkat', 'handle_nexus_register': 'meadow_handle_nexus_register', 'BscSetattrlistat': 'meadow_BscSetattrlistat', 'handle_channel_open': 'meadow_handle_channel_open', 'handle_kas_info': 'meadow_handle_kas_info', 'BscShutdown': 'meadow_BscShutdown', 'handle_semctl': 'meadow_handle_semctl', 'handle_sem_unlink': 'meadow_handle_sem_unlink', 'BscNexusGetOpt': 'meadow_BscNexusGetOpt', 'BscIoctl': 'meadow_BscIoctl', 'BscGetlogin': 'meadow_BscGetlogin', 'BscFsync': 'meadow_BscFsync', 'BscGuardedPwriteNp': 'meadow_BscGuardedPwriteNp', 'BscAccessExtended': 'meadow_BscAccessExtended', 'handle_futimes': 'meadow_handle_futimes', 'BscSendto': 'meadow_BscSendto', 'handle_pid_shutdown_sockets': 'meadow_handle_pid_shutdown_sockets', 'handle_workq_open': 'meadow_handle_workq_open', 'FsSnapshotOp': 'meadow_FsSnapshotOp', 'BscFstatat64': 'meadow_BscFstatat64', 'handle_writev': 'meadow_handle_writev', 'BscRmdir': 'meadow_BscRmdir', 'BscMinherit': 'meadow_BscMinherit', 'BscSysPreadv': 'meadow_BscSysPreadv', 'BscFfsctl': 'meadow_BscFfsctl', 'handle_access': 'meadow_handle_access', 'BscWrite': 'meadow_BscWrite', 'BscSetregid': 'meadow_BscSetregid', 'handle_sem_trywait': 'meadow_handle_sem_trywait', 'handle_fchmod': 'meadow_handle_fchmod', 'handle_nexus_destroy': 'meadow_handle_nexus_destroy', 'BscInitgroups': 'meadow_BscInitgroups', 'BscSetegid': 'meadow_BscSetegid', 'handle_coalition_info': 'meadow_handle_coalition_info', 'BscSysctl': 'meadow_BscSysctl', 'handle_getpriority': 'meadow_handle_getpriority', 'BscGetgid': 'meadow_BscGetgid', 'BscUsrctl': 'meadow_BscUsrctl', 'handle_shmat': 'meadow_handle_shmat', 'handle_msgctl': 'meadow_handle_msgctl', 'BscBsdthreadCtl': 'meadow_BscBsdthreadCtl', 'handle_searchfs': 'meadow_handle_searchfs', 'handle_mlock': 'meadow_handle_mlock', 'BscUnlinkat': 'meadow_BscUnlinkat', 'BscChannelOpen': 'meadow_BscChannelOpen', 'BscShmctl': 'meadow_BscShmctl', 'BscDisconnectx': 'meadow_BscDisconnectx', 'BscOpenDprotectedNp': 'meadow_BscOpenDprotectedNp', 'handle_setattrlist': 'meadow_handle_setattrlist', 'BscGetpeername': 'meadow_BscGetpeername', 'BscBsdthreadCreate': 'meadow_BscBsdthreadCreate', 'BscMremapEncrypted': 'meadow_BscMremapEncrypted', 'BscCoalition': 'meadow_BscCoalition', 'handle_mach_eventlink_signal_wait_until': 'meadow_handle_mach_eventlink_signal_wait_until', 'handle_channel_sync': 'meadow_handle_channel_sync', 'BscAccessFlags': 'meadow_BscAccessFlags', 'handle_bsdthread_register': 'meadow_handle_bsdthread_register', 'handle_fs_snapshot': 'meadow_handle_fs_snapshot', 'handle_pivot_root': 'meadow_handle_pivot_root', 'BscConnect': 'meadow_BscConnect', 'handle_peeloff': 'meadow_handle_peeloff', 'BscFsSnapshot': 'meadow_BscFsSnapshot', 'BscMsgget': 'meadow_BscMsgget', 'handle_fsetxattr': 'meadow_handle_fsetxattr', 'BscPivotRoot': 'meadow_BscPivotRoot', 'BscSystemOverride': 'meadow_BscSystemOverride', 'BscGetitimer': 'meadow_BscGetitimer', 'handle_necp_open': 'meadow_handle_necp_open', 'handle_msgrcv': 'meadow_handle_msgrcv', 'BscNfssvc': 'meadow_BscNfssvc', 'BscMkdirat': 'meadow_BscMkdirat', 'handle_memorystatus_control': 'meadow_handle_memorystatus_control', 'handle_sendto': 'meadow_handle_sendto', 'BscUndelete': 'meadow_BscUndelete', 'handle_proc_info': 'meadow_handle_proc_info', 'BscIopolicysys': 'meadow_BscIopolicysys', 'handle_thread_selfcounts': 'meadow_handle_thread_selfcounts', 'BscRenameatxNp': 'meadow_BscRenameatxNp', 'BscTerminateWithPayload': 'meadow_BscTerminateWithPayload', 'BscFchown': 'meadow_BscFchown', 'handle_sfi_pidctl': 'meadow_handle_sfi_pidctl', 'handle_setgroups': 'meadow_handle_setgroups', 'BscGuardedCloseNp': 'meadow_BscGuardedCloseNp', 'handle_guarded_writev_np': 'meadow_handle_guarded_writev_np', 'handle_log_data': 'meadow_handle_log_data', 'handle_link': 'meadow_handle_link', 'BscFgetattrlist': 'meadow_BscFgetattrlist', 'BscLchown': 'meadow_BscLchown', 'BscChannelGetOpt': 'meadow_BscChannelGetOpt', 'handle_setxattr': 'meadow_handle_setxattr', 'BscVfork': 'meadow_BscVfork', 'handle_shutdown': 'meadow_handle_shutdown', 'handle_stat64': 'meadow_handle_stat64', 'BscPsynchMutexwait': 'meadow_BscPsynchMutexwait', 'handle_terminate_with_payload': 'meadow_handle_terminate_with_payload', 'BscSemsys': 'meadow_BscSemsys', 'handle_socket_delegate': 'meadow_handle_socket_delegate', 'BscGetgroups': 'meadow_BscGetgroups', 'BscRename': 'meadow_BscRename', 'BscShmdt': 'meadow_BscShmdt', 'handle_clonefileat': 'meadow_handle_clonefileat', 'BscBsdthreadRegister': 'meadow_BscBsdthreadRegister', 'handle_umask': 'meadow_handle_umask', 'BscSemOpen': 'meadow_BscSemOpen', 'serialize_access_flags': 'meadow_serialize_access_flags', 'handle_necp_client_action': 'meadow_handle_necp_client_action', 'handle_connect': 'meadow_handle_connect', 'BscFchmod': 'meadow_BscFchmod', 'BscGetxattr': 'meadow_BscGetxattr', 'SigprocmaskFlags': 'meadow_SigprocmaskFlags', 'handle_sigaction': 'meadow_handle_sigaction', 'handle_nexus_create': 'meadow_handle_nexus_create', 'BscSysctlbyname': 'meadow_BscSysctlbyname', 'handle_pipe': 'meadow_handle_pipe', 'handle_statfs64': 'meadow_handle_statfs64', 'BscProcRlimitControl': 'meadow_BscProcRlimitControl', 'dataclass': 'meadow_dataclass', 'BscOsFaultWithPayload': 'meadow_BscOsFaultWithPayload', 'handle_shared_region_check_np': 'meadow_handle_shared_region_check_np', 'handle_sfi_ctl': 'meadow_handle_sfi_ctl', 'BscFmount': 'meadow_BscFmount', 'BscLinkat': 'meadow_BscLinkat', 'FcntlCmd': 'meadow_FcntlCmd', 'handle_pthread_fchdir': 'meadow_handle_pthread_fchdir', 'handle_setitimer': 'meadow_handle_setitimer', 'handle_getattrlistbulk': 'meadow_handle_getattrlistbulk', 'handle_getdirentries': 'meadow_handle_getdirentries', 'handle_undelete': 'meadow_handle_undelete', 'BscMemorystatusControl': 'meadow_BscMemorystatusControl', 'handle_nfsclnt': 'meadow_handle_nfsclnt', 'handle_sem_post': 'meadow_handle_sem_post', 'BscMachBridgeRemoteTime': 'meadow_BscMachBridgeRemoteTime', 'handle_ntp_gettime': 'meadow_handle_ntp_gettime', 'BscChangeFdguardNp': 'meadow_BscChangeFdguardNp', 'BscNecpClientAction': 'meadow_BscNecpClientAction', 'handle_setpriority': 'meadow_handle_setpriority', 'handle_wait4': 'meadow_handle_wait4', 'handle_guarded_pwrite_np': 'meadow_handle_guarded_pwrite_np', 'BscSemTrywait': 'meadow_BscSemTrywait', 'BscSysGetdtablesize': 'meadow_BscSysGetdtablesize', 'handle_initgroups': 'meadow_handle_initgroups', 'BscPsynchCvwait': 'meadow_BscPsynchCvwait', 'handle_fgetxattr': 'meadow_handle_fgetxattr', 'handle_setauid': 'meadow_handle_setauid', 'BscSharedRegionCheckNp': 'meadow_BscSharedRegionCheckNp', 'handle_chroot': 'meadow_handle_chroot', 'handle_necp_match_policy': 'meadow_handle_necp_match_policy', 'BscNexusOpen': 'meadow_BscNexusOpen', 'BscRevoke': 'meadow_BscRevoke', 'handle_getauid': 'meadow_handle_getauid', 'BscSysPwritev': 'meadow_BscSysPwritev', 'BscSharedRegionMapAndSlideNp': 'meadow_BscSharedRegionMapAndSlideNp', 'ctypes': 'meadow_ctypes', 'handle_getdirentries64': 'meadow_handle_getdirentries64', 'BscPthreadFchdir': 'meadow_BscPthreadFchdir', 'BscFchflags': 'meadow_BscFchflags', 'BscFchdir': 'meadow_BscFchdir', 'handle_sys_dup2': 'meadow_handle_sys_dup2', 'BscCsopsAudittoken': 'meadow_BscCsopsAudittoken', 'handle_psynch_mutexdrop': 'meadow_handle_psynch_mutexdrop', 'handle_getxattr': 'meadow_handle_getxattr', 'handle_necp_session_action': 'meadow_handle_necp_session_action', 'BscGuardedWriteNp': 'meadow_BscGuardedWriteNp', 'BscSemPost': 'meadow_BscSemPost', 'handle_getppid': 'meadow_handle_getppid', 'handle_kqueue_workloop_ctl': 'meadow_handle_kqueue_workloop_ctl', 'handle_reboot': 'meadow_handle_reboot', 'BscMicrostackshot': 'meadow_BscMicrostackshot', 'BscSendmsgX': 'meadow_BscSendmsgX', 'BscMemorystatusGetLevel': 'meadow_BscMemorystatusGetLevel', 'BscAccess': 'meadow_BscAccess', 'BscSetpgid': 'meadow_BscSetpgid', 'BscCsops': 'meadow_BscCsops', 'handle_chdir': 'meadow_handle_chdir', 'handle_memorystatus_available_memory': 'meadow_handle_memorystatus_available_memory', 'BscGrabPgoData': 'meadow_BscGrabPgoData', 'handle_bsdthread_create': 'meadow_handle_bsdthread_create', 'BscVfsPurge': 'meadow_BscVfsPurge', 'handle_getdirentriesattr': 'meadow_handle_getdirentriesattr', 'handle_ftruncate': 'meadow_handle_ftruncate', 'handle_telemetry': 'meadow_handle_telemetry', 'handle_abort_with_payload': 'meadow_handle_abort_with_payload', 'BscOpen': 'meadow_BscOpen', 'handle_mremap_encrypted': 'meadow_handle_mremap_encrypted', 'handle_fchmodat': 'meadow_handle_fchmodat', 'BscKasInfo': 'meadow_BscKasInfo', 'handle_audit': 'meadow_handle_audit', 'handle_sys_dup': 'meadow_handle_sys_dup', 'handle_psynch_cvsignal': 'meadow_handle_psynch_cvsignal', 'BscChflags': 'meadow_BscChflags', 'handle_sendmsg': 'meadow_handle_sendmsg', 'handle_ulock_wait': 'meadow_handle_ulock_wait', 'handle_sigsuspend': 'meadow_handle_sigsuspend', 'handle_rmdir': 'meadow_handle_rmdir', 'handle_accept': 'meadow_handle_accept', 'handle_shared_region_map_and_slide_np': 'meadow_handle_shared_region_map_and_slide_np', 'BscMadvise': 'meadow_BscMadvise', 'handle_csops_audittoken': 'meadow_handle_csops_audittoken', 'BscGetuid': 'meadow_BscGetuid', 'BscExchangedata': 'meadow_BscExchangedata', 'handle_chmod': 'meadow_handle_chmod', 'BscSetgroups': 'meadow_BscSetgroups', 'handle_renameat': 'meadow_handle_renameat', 'handle_pathconf': 'meadow_handle_pathconf', 'handle_getgroups': 'meadow_handle_getgroups', 'handle_guarded_kqueue_np': 'meadow_handle_guarded_kqueue_np', 'handle_munlockall': 'meadow_handle_munlockall', 'handle_revoke': 'meadow_handle_revoke', 'handle_mkdirat': 'meadow_handle_mkdirat', 'handle_ntp_adjtime': 'meadow_handle_ntp_adjtime', 'handle_connectx': 'meadow_handle_connectx', 'BscPeeloff': 'meadow_BscPeeloff', 'BscNecpOpen': 'meadow_BscNecpOpen', 'handle_getfh': 'meadow_handle_getfh', 'BscSfiPidctl': 'meadow_BscSfiPidctl', 'BscSemop': 'meadow_BscSemop', 'handle_usrctl': 'meadow_handle_usrctl', 'handle_proc_uuid_policy': 'meadow_handle_proc_uuid_policy', 'handle_kevent': 'meadow_handle_kevent', 'BscChangeableFlags': 'meadow_BscChangeableFlags', 'handle_sigprocmask': 'meadow_handle_sigprocmask', 'handle_mincore': 'meadow_handle_mincore', 'SocketOptionName': 'meadow_SocketOptionName', 'handle_sys_close': 'meadow_handle_sys_close', 'handle_gettid': 'meadow_handle_gettid', 'handle_proc_trace_log': 'meadow_handle_proc_trace_log', 'handle_workq_kernreturn': 'meadow_handle_workq_kernreturn', 'BscAcct': 'meadow_BscAcct', 'BscRecvmsgX': 'meadow_BscRecvmsgX', 'BscPsynchCvclrprepost': 'meadow_BscPsynchCvclrprepost', 'handle_thread_selfusage': 'meadow_handle_thread_selfusage', 'BscSeteuid': 'meadow_BscSeteuid', 'handle_disable_threadsignal': 'meadow_handle_disable_threadsignal', 'handle_semwait_signal': 'meadow_handle_semwait_signal', 'BscNtpAdjtime': 'meadow_BscNtpAdjtime', 'BscSetattrlist': 'meadow_BscSetattrlist', 'handle_lchown': 'meadow_handle_lchown', 'BscConnectx': 'meadow_BscConnectx', 'handle_truncate': 'meadow_handle_truncate', 'BscSetrlimit': 'meadow_BscSetrlimit', 'S_IFMT': 'meadow_S_IFMT', 'BscGuardedOpenDprotectedNp': 'meadow_BscGuardedOpenDprotectedNp', 'handle_gethostuuid': 'meadow_handle_gethostuuid', 'handle_msgsnd': 'meadow_handle_msgsnd', 'BscFhopen': 'meadow_BscFhopen', 'BscPosixSpawn': 'meadow_BscPosixSpawn', 'BscFsetxattr': 'meadow_BscFsetxattr', 'handle_rename': 'meadow_handle_rename', 'handle_open_dprotected_np': 'meadow_handle_open_dprotected_np', 'BscGetrusage': 'meadow_BscGetrusage', 'BscMount': 'meadow_BscMount', 'handle_vfork': 'meadow_handle_vfork', 'BscPathconf': 'meadow_BscPathconf', 'BscReadlink': 'meadow_BscReadlink', 'handle_fsync': 'meadow_handle_fsync', 'BscNexusDestroy': 'meadow_BscNexusDestroy', 'handle_ulock_wake': 'meadow_handle_ulock_wake', 'BscSocketpair': 'meadow_BscSocketpair', 'BscSettimeofday': 'meadow_BscSettimeofday', 'BscSigsuspend': 'meadow_BscSigsuspend', 'handle_listxattr': 'meadow_handle_listxattr', 'handle_openat': 'meadow_handle_openat', 'handle_execve': 'meadow_handle_execve', 'handle_proc_rlimit_control': 'meadow_handle_proc_rlimit_control', 'BscSendmsg': 'meadow_BscSendmsg', 'handle_task_inspect_for_pid': 'meadow_handle_task_inspect_for_pid', 'BscTelemetry': 'meadow_BscTelemetry', 'BscMlockall': 'meadow_BscMlockall', 'BscSysFcntl': 'meadow_BscSysFcntl', 'handle_getsockname': 'meadow_handle_getsockname', 'handle_swapon': 'meadow_handle_swapon', 'handle_issetugid': 'meadow_handle_issetugid', 'BscPidResume': 'meadow_BscPidResume', 'handle_sys_sysctlbyname': 'meadow_handle_sys_sysctlbyname', 'BscGetpgrp': 'meadow_BscGetpgrp', 'handle_munlock': 'meadow_handle_munlock', 'BscMunlock': 'meadow_BscMunlock', 'handle_shmctl': 'meadow_handle_shmctl', 'handle_getattrlistat': 'meadow_handle_getattrlistat', 'BscFstatfs': 'meadow_BscFstatfs', 'BscOpenat': 'meadow_BscOpenat', 'BscSearchfs': 'meadow_BscSearchfs', 'BscSharedRegionMapAndSlide2Np': 'meadow_BscSharedRegionMapAndSlide2Np', 'handle_select': 'meadow_handle_select', 'handle_proc_info_extended_id': 'meadow_handle_proc_info_extended_id', 'handle_fgetattrlist': 'meadow_handle_fgetattrlist', 'BscIssetugid': 'meadow_BscIssetugid', 'BscKqueueWorkloopCtl': 'meadow_BscKqueueWorkloopCtl', 'BscChdir': 'meadow_BscChdir', 'handle_msgget': 'meadow_handle_msgget', 'socket': 'meadow_socket', 'handle_guarded_open_np': 'meadow_handle_guarded_open_np', 'handle_sys_preadv': 'meadow_handle_sys_preadv', 'BscGuardedKqueueNp': 'meadow_BscGuardedKqueueNp', 'handle_microstackshot': 'meadow_handle_microstackshot', 'handle_setattrlistat': 'meadow_handle_setattrlistat', 'handle_getsockopt': 'meadow_handle_getsockopt', 'handle_shmsys': 'meadow_handle_shmsys', 'BscStackSnapshotWithConfig': 'meadow_BscStackSnapshotWithConfig', 'BscOpenFlags': 'meadow_BscOpenFlags', 'BscMachEventlinkSignal': 'meadow_BscMachEventlinkSignal', 'handle_setprivexec': 'meadow_handle_setprivexec', 'handle_work_interval_ctl': 'meadow_handle_work_interval_ctl', 'handle_channel_get_opt': 'meadow_handle_channel_get_opt', 'handle_msync': 'meadow_handle_msync', 'handle_utimes': 'meadow_handle_utimes', 'handle_grab_pgo_data': 'meadow_handle_grab_pgo_data', 'BscKdebugTypefilter': 'meadow_BscKdebugTypefilter', 'BscChmod': 'meadow_BscChmod', 'BscDisableThreadsignal': 'meadow_BscDisableThreadsignal', 'BscNetQosGuideline': 'meadow_BscNetQosGuideline', 'handle_sys_getdtablesize': 'meadow_handle_sys_getdtablesize', 'BscSelect': 'meadow_BscSelect', 'handle_audit_session_port': 'meadow_handle_audit_session_port', 'handle_getpeername': 'meadow_handle_getpeername', 'BscRecvmsg': 'meadow_BscRecvmsg', 'handle_mach_eventlink_signal': 'meadow_handle_mach_eventlink_signal', 'handle_mount': 'meadow_handle_mount', 'handle_getgid': 'meadow_handle_getgid', 'BscFsetattrlist': 'meadow_BscFsetattrlist', 'BscGetsockname': 'meadow_BscGetsockname', 'BscPidHibernate': 'meadow_BscPidHibernate', 'handle_iopolicysys': 'meadow_handle_iopolicysys', 'handle_mach_bridge_remote_time': 'meadow_handle_mach_bridge_remote_time', 'BscUtimes': 'meadow_BscUtimes', 'BscWorkqOpen': 'meadow_BscWorkqOpen', 'BscPidShutdownSockets': 'meadow_BscPidShutdownSockets', 'enum': 'meadow_enum', 'handle_nexus_open': 'meadow_handle_nexus_open', 'handle_stack_snapshot_with_config': 'meadow_handle_stack_snapshot_with_config', 'BscShmget': 'meadow_BscShmget', 'BscProcTraceLog': 'meadow_BscProcTraceLog', 'handle_settimeofday': 'meadow_handle_settimeofday', 'handle_access_extended': 'meadow_handle_access_extended', 'BscSwapon': 'meadow_BscSwapon', 'BscGetsockopt': 'meadow_BscGetsockopt', 'BscMsgsnd': 'meadow_BscMsgsnd', 'BscPsynchCvsignal': 'meadow_BscPsynchCvsignal', 'handle_fsctl': 'meadow_handle_fsctl', 'BscWritev': 'meadow_BscWritev', 'BscChown': 'meadow_BscChown', 'BscClonefileat': 'meadow_BscClonefileat', 'handle_auditon': 'meadow_handle_auditon', 'handle_mkfifo': 'meadow_handle_mkfifo', 'BscMsgctl': 'meadow_BscMsgctl', 'handle_read': 'meadow_handle_read', 'BscShmOpen': 'meadow_BscShmOpen', 'handle_psynch_cvclrprepost': 'meadow_handle_psynch_cvclrprepost', 'handle_symlinkat': 'meadow_handle_symlinkat', 'BscMachEventlinkSignalWaitUntil': 'meadow_BscMachEventlinkSignalWaitUntil', 'BscPwrite': 'meadow_BscPwrite', 'BscMkfifo': 'meadow_BscMkfifo', 'BscGuardedOpenNp': 'meadow_BscGuardedOpenNp', 'handle_lstat64': 'meadow_handle_lstat64', 'handle_fremovexattr': 'meadow_handle_fremovexattr', 'BscTruncate': 'meadow_BscTruncate', 'BscSetprivexec': 'meadow_BscSetprivexec', 'BscRenameat': 'meadow_BscRenameat', 'BscReadlinkat': 'meadow_BscReadlinkat', 'BscLseek': 'meadow_BscLseek', 'BscRemovexattr': 'meadow_BscRemovexattr', 'BscMunlockall': 'meadow_BscMunlockall', 'handle_munmap': 'meadow_handle_munmap', 'BscCoalitionLedger': 'meadow_BscCoalitionLedger', 'BscMprotect': 'meadow_BscMprotect', 'handle_msgsys': 'meadow_handle_msgsys', 'handle_ioctl': 'meadow_handle_ioctl', 'BscNecpMatchPolicy': 'meadow_BscNecpMatchPolicy', 'handle_pthread_sigmask': 'meadow_handle_pthread_sigmask', 'BscSocketDelegate': 'meadow_BscSocketDelegate', 'BscFchmodat': 'meadow_BscFchmodat', 'FlockOperation': 'meadow_FlockOperation', 'BscKevent64': 'meadow_BscKevent64', 'handle_exchangedata': 'meadow_handle_exchangedata', 'BscMsync': 'meadow_BscMsync', 'StatFlags': 'meadow_StatFlags', 'handle_linkat': 'meadow_handle_linkat', 'BscLstat64': 'meadow_BscLstat64', 'BscPsynchMutexdrop': 'meadow_BscPsynchMutexdrop', 'handle_sync': 'meadow_handle_sync', 'sockopt_format_level_and_option': 'meadow_sockopt_format_level_and_option', 'handle_shm_unlink': 'meadow_handle_shm_unlink', 'handle_fstatfs64': 'meadow_handle_fstatfs64', 'handle_csrctl': 'meadow_handle_csrctl', 'handle_sysctl': 'meadow_handle_sysctl', 'handle_socket': 'meadow_handle_socket', 'handle_sys_flock': 'meadow_handle_sys_flock', 'handle_mkdir': 'meadow_handle_mkdir', 'handle_bsdthread_ctl': 'meadow_handle_bsdthread_ctl', 'handle_obs_killpg': 'meadow_handle_obs_killpg', 'handle_mach_eventlink_wait_until': 'meadow_handle_mach_eventlink_wait_until', 'handle_ulock_wait2': 'meadow_handle_ulock_wait2', 'BscSemClose': 'meadow_BscSemClose', 'handle_guarded_close_np': 'meadow_handle_guarded_close_np', 'BscSetsockopt': 'meadow_BscSetsockopt', 'BscMlock': 'meadow_BscMlock', 'handle_readv': 'meadow_handle_readv', 'handle_chflags': 'meadow_handle_chflags', 'handle_unmount': 'meadow_handle_unmount', 'handle_sys_fpathconf': 'meadow_handle_sys_fpathconf', 'BscNecpSessionAction': 'meadow_BscNecpSessionAction', 'handle_getattrlist': 'meadow_handle_getattrlist', 'handle_sem_open': 'meadow_handle_sem_open', 'handle_sem_wait': 'meadow_handle_sem_wait', 'ProcInfoCall': 'meadow_ProcInfoCall', 'BscSigprocmap': 'meadow_BscSigprocmap', 'BscSysClose': 'meadow_BscSysClose', 'BscListxattr': 'meadow_BscListxattr', 'BscMsgsys': 'meadow_BscMsgsys', 'BscSysFileportMakeport': 'meadow_BscSysFileportMakeport', 'serialize_stat_flags': 'meadow_serialize_stat_flags', 'handle_readlink': 'meadow_handle_readlink', 'handle_disconnectx': 'meadow_handle_disconnectx', 'BscTaskReadForPid': 'meadow_BscTaskReadForPid', 'handle_psynch_mutexwait': 'meadow_handle_psynch_mutexwait', 'BscShmat': 'meadow_BscShmat', 'handle_fchflags': 'meadow_handle_fchflags', 'PriorityWhich': 'meadow_PriorityWhich', 'BscGetegid': 'meadow_BscGetegid', 'BscSetauid': 'meadow_BscSetauid', 'BscFsgetpath': 'meadow_BscFsgetpath', 'BscFtruncate': 'meadow_BscFtruncate', 'handle_adjtime': 'meadow_handle_adjtime', 'handle_openbyid_np': 'meadow_handle_openbyid_np', 'BscPread': 'meadow_BscPread', 'BscGetrlimit': 'meadow_BscGetrlimit', 'handle_channel_set_opt': 'meadow_handle_channel_set_opt', 'handle_getlogin': 'meadow_handle_getlogin', 'handle_fsetattrlist': 'meadow_handle_fsetattrlist', 'handle_fchown': 'meadow_handle_fchown', 'BscRecvfrom': 'meadow_BscRecvfrom', 'BscKill': 'meadow_BscKill', 'handle_getpgrp': 'meadow_handle_getpgrp', 'BscSysFileportMakefd': 'meadow_BscSysFileportMakefd', 'handle_shared_region_map_and_slide_2_np': 'meadow_handle_shared_region_map_and_slide_2_np', 'BscPipe': 'meadow_BscPipe', 'handle_symlink': 'meadow_handle_symlink', 'handle_setreuid': 'meadow_handle_setreuid', 'handle_setrlimit': 'meadow_handle_setrlimit', 'handle_coalition': 'meadow_handle_coalition', 'handle_nexus_get_opt': 'meadow_handle_nexus_get_opt', 'BscMknod': 'meadow_BscMknod', 'BscUnlink': 'meadow_BscUnlink', 'BscCoalitionInfo': 'meadow_BscCoalitionInfo', 'handle_pid_resume': 'meadow_handle_pid_resume', 'BscSetreuid': 'meadow_BscSetreuid', 'handle_mlockall': 'meadow_handle_mlockall', 'BscGettimeofday': 'meadow_BscGettimeofday', 'handle_csops': 'meadow_handle_csops', 'handle_pid_suspend': 'meadow_handle_pid_suspend', 'RusageWho': 'meadow_RusageWho', 'handle_geteuid': 'meadow_handle_geteuid', 'BscWorkIntervalCtl': 'meadow_BscWorkIntervalCtl', 'handle_posix_spawn': 'meadow_handle_posix_spawn', 'BscGetppid': 'meadow_BscGetppid', 'BscSetpriority': 'meadow_BscSetpriority', 'BscMemorystatusAvailableMemory': 'meadow_BscMemorystatusAvailableMemory', 'BscNetagentTrigger': 'meadow_BscNetagentTrigger', 'handle_kdebug_typefilter': 'meadow_handle_kdebug_typefilter', 'BscSemget': 'meadow_BscSemget', 'BscReadv': 'meadow_BscReadv', 'BscSemctl': 'meadow_BscSemctl', 'handle_setregid': 'meadow_handle_setregid', 'BscGetfh': 'meadow_BscGetfh', 'handle_getentropy': 'meadow_handle_getentropy', 'handle_setgid': 'meadow_handle_setgid', 'handle_fmount': 'meadow_handle_fmount', 'BscUmask': 'meadow_BscUmask', 'BscWaitid': 'meadow_BscWaitid', 'handle_getrusage': 'meadow_handle_getrusage', 'BscSymlinkat': 'meadow_BscSymlinkat', 'BscThreadSelfid': 'meadow_BscThreadSelfid', 'handle_fsgetpath': 'meadow_handle_fsgetpath', 'handle_getegid': 'meadow_handle_getegid', 'handle_waitid': 'meadow_handle_waitid', 'handle_sys_fileport_makefd': 'meadow_handle_sys_fileport_makefd', 'handle_setegid': 'meadow_handle_setegid', 'BscListen': 'meadow_BscListen', 'BscSysDup2': 'meadow_BscSysDup2', 'BscMsgrcv': 'meadow_BscMsgrcv', 'handle_nexus_deregister': 'meadow_handle_nexus_deregister', 'handle_bind': 'meadow_handle_bind', 'handle_getuid': 'meadow_handle_getuid', 'handle_sigpending': 'meadow_handle_sigpending', 'BscSetsid': 'meadow_BscSetsid', 'BscExecve': 'meadow_BscExecve', 'handle_kevent64': 'meadow_handle_kevent64', 'BscPersona': 'meadow_BscPersona', 'handle_setsid': 'meadow_handle_setsid', 'BscNfsclnt': 'meadow_BscNfsclnt', 'handle_sys_pwritev': 'meadow_handle_sys_pwritev', 'BscChannelSync': 'meadow_BscChannelSync', 'handle_memorystatus_get_level': 'meadow_handle_memorystatus_get_level', 'handle_mprotect': 'meadow_handle_mprotect', 'BscSysDup': 'meadow_BscSysDup', 'handle_fstatat64': 'meadow_handle_fstatat64', 'handle_sendfile': 'meadow_handle_sendfile', 'handle_thread_selfid': 'meadow_handle_thread_selfid', 'handle_task_read_for_pid': 'meadow_handle_task_read_for_pid', 'handle_fdatasync': 'meadow_handle_fdatasync', 'handle_system_override': 'meadow_handle_system_override', 'SocketMsgFlags': 'meadow_SocketMsgFlags', 'BscAudit': 'meadow_BscAudit', 'handle_kqueue': 'meadow_handle_kqueue', 'handle_net_qos_guideline': 'meadow_handle_net_qos_guideline', 'handle_getsid': 'meadow_handle_getsid', 'handle_setpgid': 'meadow_handle_setpgid', 'handle_shmdt': 'meadow_handle_shmdt', 'handle_setlogin': 'meadow_handle_setlogin', 'handle_mac_syscall': 'meadow_handle_mac_syscall', 'handle_guarded_open_dprotected_np': 'meadow_handle_guarded_open_dprotected_np', 'CsopsOps': 'meadow_CsopsOps', 'BscGethostuuid': 'meadow_BscGethostuuid', 'BscNexusDeregister': 'meadow_BscNexusDeregister', 'handle_pid_hibernate': 'meadow_handle_pid_hibernate', 'handle_unlink': 'meadow_handle_unlink', 'handle_pwrite': 'meadow_handle_pwrite', 'BscFstatat': 'meadow_BscFstatat', 'BscGetpgid': 'meadow_BscGetpgid', 'handle_change_fdguard_np': 'meadow_handle_change_fdguard_np', 'IOC_REQUEST_PARAMS': 'meadow_IOC_REQUEST_PARAMS', 'BscPoll': 'meadow_BscPoll', 'BscProcUuidPolicy': 'meadow_BscProcUuidPolicy', 'BscStat64': 'meadow_BscStat64', 'BscMincore': 'meadow_BscMincore', 'BscMkdir': 'meadow_BscMkdir', 'BscPidSuspend': 'meadow_BscPidSuspend', 'BscFsctl': 'meadow_BscFsctl', 'handle_quotactl': 'meadow_handle_quotactl', 'BscWait4': 'meadow_BscWait4', 'handle_sigaltstack': 'meadow_handle_sigaltstack', 'handle_pselect': 'meadow_handle_pselect', 'handle_fchownat': 'meadow_handle_fchownat', 'BscUlockWake': 'meadow_BscUlockWake', 'BscGetattrlist': 'meadow_BscGetattrlist', 'BscSysFlock': 'meadow_BscSysFlock', 'BscKeventQos': 'meadow_BscKeventQos', 'BscFstatfs64': 'meadow_BscFstatfs64', 'BscKeventId': 'meadow_BscKeventId', 'BscGeteuid': 'meadow_BscGeteuid', 'handle_getrlimit': 'meadow_handle_getrlimit', 'handle_socketpair': 'meadow_handle_socketpair', 'BscSocket': 'meadow_BscSocket', 'BscGetentropy': 'meadow_BscGetentropy', 'handle_fhopen': 'meadow_handle_fhopen', 'handle_getpgid': 'meadow_handle_getpgid', 'handle_nexus_set_opt': 'meadow_handle_nexus_set_opt', 'handle_mmap': 'meadow_handle_mmap', 'BscAuditSessionPort': 'meadow_BscAuditSessionPort', 'BscSetuid': 'meadow_BscSetuid', 'handle_removexattr': 'meadow_handle_removexattr', 'partial': 'meadow_partial', 'handle_kevent_id': 'meadow_handle_kevent_id', 'handle_minherit': 'meadow_handle_minherit', 'BscSetitimer': 'meadow_BscSetitimer', 'handle_netagent_trigger': 'meadow_handle_netagent_trigger', 'BscUlockWait': 'meadow_BscUlockWait', 'BscGetpid': 'meadow_BscGetpid', 'BscAbortWithPayload': 'meadow_BscAbortWithPayload', 'handlers': 'meadow_handlers', 'BscGetdirentriesattr': 'meadow_BscGetdirentriesattr', 'BscKevent': 'meadow_BscKevent', 'handle_fstatat': 'meadow_handle_fstatat', 'BscFaccessat': 'meadow_BscFaccessat', 'handle_process_policy': 'meadow_handle_process_policy', 'handle_psynch_cvbroad': 'meadow_handle_psynch_cvbroad', 'BscMachEventlinkWaitUntil': 'meadow_BscMachEventlinkWaitUntil', 'handle_channel_get_info': 'meadow_handle_channel_get_info', 'handle_getpid': 'meadow_handle_getpid', 'handle_fclonefileat': 'meadow_handle_fclonefileat', 'BscReboot': 'meadow_BscReboot', 'Signals': 'meadow_Signals', 'BscShmUnlink': 'meadow_BscShmUnlink', 'handle_readlinkat': 'meadow_handle_readlinkat', 'BscGetpriority': 'meadow_BscGetpriority', 'BscStatfs': 'meadow_BscStatfs', 'handle_acct': 'meadow_handle_acct', 'BscSigaction': 'meadow_BscSigaction', 'handle_ffsctl': 'meadow_handle_ffsctl', 'BscProcInfo': 'meadow_BscProcInfo', 'List': 'meadow_List', 'handle_sys_fstat64': 'meadow_handle_sys_fstat64', 'BscNexusSetOpt': 'meadow_BscNexusSetOpt', 'BscProcessPolicy': 'meadow_BscProcessPolicy', 'BscSysFpathconf': 'meadow_BscSysFpathconf', 'BscChroot': 'meadow_BscChroot', 'BscChannelSetOpt': 'meadow_BscChannelSetOpt', 'BscSetlogin': 'meadow_BscSetlogin', 'handle_sys_fcntl': 'meadow_handle_sys_fcntl', 'BscFlistxattr': 'meadow_BscFlistxattr', 'handle_shmget': 'meadow_handle_shmget', 'BscFdatasync': 'meadow_BscFdatasync', 'BscSysFstat64': 'meadow_BscSysFstat64', 'BscFutimes': 'meadow_BscFutimes', 'BscKqueue': 'meadow_BscKqueue', 'BscSendfile': 'meadow_BscSendfile', 'handle_semop': 'meadow_handle_semop', 'BscSigaltstack': 'meadow_BscSigaltstack', 'BscThreadSelfcounts': 'meadow_BscThreadSelfcounts', 'handle_setuid': 'meadow_handle_setuid', 'serialize_open_flags': 'meadow_serialize_open_flags', 'BscGetsid': 'meadow_BscGetsid', 'BscMacSyscall': 'meadow_BscMacSyscall', 'handle_semget': 'meadow_handle_semget', 'BscUlockWait2': 'meadow_BscUlockWait2', 'handle_persona': 'meadow_handle_persona', 'errno': 'meadow_errno', 'handle_sys_fileport_makeport': 'meadow_handle_sys_fileport_makeport', 'BscFchownat': 'meadow_BscFchownat', 'BscObsKillpg': 'meadow_BscObsKillpg', 'handle_semsys': 'meadow_handle_semsys', 'BscNexusRegister': 'meadow_BscNexusRegister', 'BscGetdirentries': 'meadow_BscGetdirentries', 'handle_kill': 'meadow_handle_kill', 'BscFclonefileat': 'meadow_BscFclonefileat', 'BscTaskInspectForPid': 'meadow_BscTaskInspectForPid', 'BscWorkqKernreturn': 'meadow_BscWorkqKernreturn', 'BscCsrctl': 'meadow_BscCsrctl', 'handle_fchdir': 'meadow_handle_fchdir', 'BscPselect': 'meadow_BscPselect', 'handle_vfs_purge': 'meadow_handle_vfs_purge', 'handle_madvise': 'meadow_handle_madvise', 'BscFgetxattr': 'meadow_BscFgetxattr', 'BscUnmount': 'meadow_BscUnmount', 'BscMunmap': 'meadow_BscMunmap', 'BscPsynchCvbroad': 'meadow_BscPsynchCvbroad', 'BscMmap': 'meadow_BscMmap', 'handle_flistxattr': 'meadow_handle_flistxattr', 'handle_guarded_write_np': 'meadow_handle_guarded_write_np', 'BscGetauid': 'meadow_BscGetauid', 'handle_getitimer': 'meadow_handle_getitimer', 'handle_seteuid': 'meadow_handle_seteuid', 'BscGetdirentries64': 'meadow_BscGetdirentries64', 'BscSemWait': 'meadow_BscSemWait', 'BscSetgid': 'meadow_BscSetgid', 'BscNtpGettime': 'meadow_BscNtpGettime', 'handle_listen': 'meadow_handle_listen', 'handle_mknod': 'meadow_handle_mknod', 'BscSfiCtl': 'meadow_BscSfiCtl', 'handle_statfs': 'meadow_handle_statfs', 'handle_recvmsg': 'meadow_handle_recvmsg', 'handle_kevent_qos': 'meadow_handle_kevent_qos', 'BscProcInfoExtendedId': 'meadow_BscProcInfoExtendedId', 'handle_getfsstat64': 'meadow_handle_getfsstat64', 'handle_os_fault_with_payload': 'meadow_handle_os_fault_with_payload', 'BscSymlink': 'meadow_BscSymlink', 'handle_nfssvc': 'meadow_handle_nfssvc', 'handle_coalition_ledger': 'meadow_handle_coalition_ledger', 'handle_lseek': 'meadow_handle_lseek', 'handle_sem_close': 'meadow_handle_sem_close', 'BscOpenbyidNp': 'meadow_BscOpenbyidNp', 'BscSetxattr': 'meadow_BscSetxattr', 'BscRead': 'meadow_BscRead', 'BscSigpending': 'meadow_BscSigpending', 'BscBind': 'meadow_BscBind', 'handle_open': 'meadow_handle_open', 'BscStatfs64': 'meadow_BscStatfs64', 'BscAccept': 'meadow_BscAccept', 'BscFremovexattr': 'meadow_BscFremovexattr', 'BscShmsys': 'meadow_BscShmsys', 'handle_write': 'meadow_handle_write', 'BscGetfsstat64': 'meadow_BscGetfsstat64', 'BscQuotactl': 'meadow_BscQuotactl', 'BscAuditon': 'meadow_BscAuditon', 'BscLogData': 'meadow_BscLogData', 'BscLink': 'meadow_BscLink', 'BscPthreadSigmask': 'meadow_BscPthreadSigmask', 'handle_shm_open': 'meadow_handle_shm_open', 'BscNecpSessionOpen': 'meadow_BscNecpSessionOpen', 'handle_poll': 'meadow_handle_poll', 'BscNexusCreate': 'meadow_BscNexusCreate', 'handle_recvmsg_x': 'meadow_handle_recvmsg_x'})
