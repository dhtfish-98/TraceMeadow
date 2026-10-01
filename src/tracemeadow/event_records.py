# Derived from pykdebugparser/kevent.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from collections import namedtuple as meadow_namedtuple
import enum as meadow_enum
import struct as meadow_struct
meadow_KDBG_EVENTID_MASK = 4294967292
meadow_KDBG_FUNC_MASK = 3
meadow_KD_BUF_FORMAT = '<Q32sQIIQ'
meadow_Kevent = _name_boundary.named_record('Kevent', ['timestamp', 'data', 'values', 'tid', 'debugid', 'eventid', 'func_qualifier'])

@_name_boundary.class_contract('DgbFuncQual', {})
class meadow_DgbFuncQual(meadow_enum.Enum):
    """
    Event's role in the trace.
    """
    DBG_FUNC_NONE = 0
    DBG_FUNC_START = 1
    DBG_FUNC_END = 2
    DBG_FUNC_ALL = 3

@_name_boundary.callable_contract({'kd_buf': 'meadow_kd_buf_bad8ae3'}, 'from_kd_buf')
def meadow_from_kd_buf(meadow_kd_buf_bad8ae3: bytes) -> meadow_Kevent:
    """
    Create a Kevent object from a kd_buf kevent's struct.
    :param kd_buf: Buffer of kd_buf kevent's struct.
    :return: Parsed kevent.
    """
    meadow_timestamp_a72bffd, meadow_args_buf_284e55c, meadow_tid_b0d56e2, meadow_debugid_d5ea2dd, meadow_cpuid_e55becf, meadow_unused_d43e200 = meadow_struct.unpack(meadow_KD_BUF_FORMAT, meadow_kd_buf_bad8ae3)
    meadow_eventid_149b163 = meadow_debugid_d5ea2dd & meadow_KDBG_EVENTID_MASK
    meadow_qual_77c3ea9 = meadow_debugid_d5ea2dd & meadow_KDBG_FUNC_MASK
    meadow_args_b9093b0 = meadow_struct.unpack('<QQQQ', meadow_args_buf_284e55c)
    return meadow_Kevent(meadow_timestamp_a72bffd, meadow_args_buf_284e55c, meadow_args_b9093b0, meadow_tid_b0d56e2, meadow_debugid_d5ea2dd, meadow_eventid_149b163, meadow_qual_77c3ea9)
_name_boundary.module_contract(globals(), {'from_kd_buf': 'meadow_from_kd_buf', 'struct': 'meadow_struct', 'KDBG_EVENTID_MASK': 'meadow_KDBG_EVENTID_MASK', 'KD_BUF_FORMAT': 'meadow_KD_BUF_FORMAT', 'Kevent': 'meadow_Kevent', 'DgbFuncQual': 'meadow_DgbFuncQual', 'namedtuple': 'meadow_namedtuple', 'KDBG_FUNC_MASK': 'meadow_KDBG_FUNC_MASK', 'enum': 'meadow_enum'})
