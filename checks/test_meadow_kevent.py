# Derived from tests/test_kevent.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import pytest as meadow_pytest
from tracemeadow.event_records import meadow_from_kd_buf as meadow_from_kd_buf, meadow_Kevent as meadow_Kevent

@meadow_pytest.mark.parametrize('raw, parsed', [(b'\x8b\xf3\x8f1\x13\xeb\x03\x00ework_BusinessChat-7.0.1-py2.py3\xdeJ\x88\x00\x00\x00\x00\x00\x90\x00\x01\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', meadow_Kevent(timestamp=1102892598555531, data=b'ework_BusinessChat-7.0.1-py2.py3', values=(8449420765986518885, 7512975542844287347, 3543822931839513697, 3709119111833940013), tid=8932062, debugid=50397328, eventid=50397328, func_qualifier=0)), (b'\x00' * 64, meadow_Kevent(timestamp=0, data=b'\x00' * 32, values=(0, 0, 0, 0), tid=0, debugid=0, eventid=0, func_qualifier=0)), (b'\xff' * 64, meadow_Kevent(timestamp=18446744073709551615, data=b'\xff' * 32, values=(18446744073709551615, 18446744073709551615, 18446744073709551615, 18446744073709551615), tid=18446744073709551615, debugid=4294967295, eventid=4294967292, func_qualifier=3))])
@_name_boundary.callable_contract({'raw': 'meadow_raw_24b4aae', 'parsed': 'meadow_parsed_1ba4e7a'}, 'test_from_kd_buf')
def meadow_test_from_kd_buf(meadow_raw_24b4aae, meadow_parsed_1ba4e7a):
    assert meadow_from_kd_buf(meadow_raw_24b4aae) == meadow_parsed_1ba4e7a
_name_boundary.module_contract(globals(), {'Kevent': 'meadow_Kevent', 'pytest': 'meadow_pytest', 'from_kd_buf': 'meadow_from_kd_buf', 'test_from_kd_buf': 'meadow_test_from_kd_buf'})
