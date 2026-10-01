# Derived from tests/traces/test_bsd.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_8c1bc36'}, 'test_read')
def meadow_test_read(meadow_traces_parser_8c1bc36):
    meadow_events_c8b09d7 = [meadow_Kevent(timestamp=15783429453, data=b'\x07\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xf1\x1b\x01\x00\x00\x00\xd6c\x00\x00\x00\x00\x00\x00h\xd8:m\x01\x00\x00\x00', values=(7, 4763795456, 25558, 6127540328), tid=7573, debugid=67895309, eventid=67895308, func_qualifier=1), meadow_Kevent(timestamp=15783456070, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\xd6c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x00\x00\x00\x00\x00\x00', values=(0, 25558, 0, 144), tid=7573, debugid=67895310, eventid=67895308, func_qualifier=2)]
    meadow_ret_b2aec84 = list(_name_boundary.attributes(meadow_traces_parser_8c1bc36)['feed_generator'](meadow_events_c8b09d7))
    assert str(meadow_ret_b2aec84[0]) == 'read(7, 0x11bf1c000, 25558), count: 25558'

@_name_boundary.callable_contract({'traces_parser': 'meadow_traces_parser_6bd87c3'}, 'test_csops_audittoken_16')
def meadow_test_csops_audittoken_16(meadow_traces_parser_6bd87c3):
    meadow_events_3a7ea1f = [meadow_Kevent(timestamp=1805610285184, data=b'C\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\xa0&\xa1m\x01\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00', values=(67, 16, 6134245024, 8), tid=1599, debugid=67895977, eventid=67895976, func_qualifier=1), meadow_Kevent(timestamp=1805610285735, data=b'"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00C\x00\x00\x00\x00\x00\x00\x00', values=(34, 0, 0, 67), tid=1599, debugid=67895978, eventid=67895976, func_qualifier=2)]
    meadow_ret_e50604c = list(_name_boundary.attributes(meadow_traces_parser_6bd87c3)['feed_generator'](meadow_events_3a7ea1f))
    assert str(meadow_ret_e50604c[0]) == 'csops_audittoken(67, CS_OPS_16, 0x16da126a0, 8), errno: ERANGE(34)'
_name_boundary.module_contract(globals(), {'test_read': 'meadow_test_read', 'Kevent': 'meadow_Kevent', 'test_csops_audittoken_16': 'meadow_test_csops_audittoken_16'})
