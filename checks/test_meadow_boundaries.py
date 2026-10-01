"""Binary event boundaries, independent of handler dispatch implementation."""
import struct as meadow_struct
import pytest as meadow_pytest
from tracemeadow.event_records import meadow_from_kd_buf
from tracemeadow.log_records import meadow_OsLogType


@meadow_pytest.mark.parametrize('meadow_length',[0,1,7,31,32,63,65,127])
def test_meadow_event_requires_exact_wire_size(meadow_length):
    with meadow_pytest.raises(meadow_struct.error):
        meadow_from_kd_buf(b'\0'*meadow_length)


def test_meadow_event_wire_masks_and_tuple_fields():
    meadow_event=meadow_from_kd_buf(b'\xff'*64)
    assert meadow_event.timestamp==2**64-1
    assert meadow_event.eventid==0xfffffffc
    assert meadow_event.func_qualifier==3
    assert tuple(meadow_event._asdict())==('timestamp','data','values','tid','debugid','eventid','func_qualifier')
    assert repr(meadow_event).startswith('Kevent(')


def test_meadow_enum_error_uses_wire_type_label():
    with meadow_pytest.raises(ValueError,match='is not a valid OsLogType'):
        meadow_OsLogType(2**40)
