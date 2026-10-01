# Derived from tests/test_pykdebugparser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from io import BytesIO as meadow_BytesIO
from tracemeadow.binary_stream import meadow_RAW_VERSION2_BYTES as meadow_RAW_VERSION2_BYTES
from tracemeadow.event_records import meadow_Kevent as meadow_Kevent
from tracemeadow.event_stream import meadow_PyKdebugParser as meadow_PyKdebugParser

@_name_boundary.callable_contract({}, 'test_kevents')
def meadow_test_kevents():
    meadow_events_buf_7c39c1e = meadow_RAW_VERSION2_BYTES + b'\x00' * 284
    meadow_events_buf_7c39c1e += b'\xa50\x147_\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x01\x00\x00\x00\x00\x00\x00y\xd8\t\x00\x00\x00\x00\x00*\x03\x0c\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    meadow_parser_6c17198 = meadow_PyKdebugParser()
    meadow_events_8e07c46 = list(_name_boundary.attributes(meadow_parser_6c17198)['kevents'](meadow_BytesIO(meadow_events_buf_7c39c1e)))
    assert meadow_events_8e07c46 == [meadow_Kevent(timestamp=7006015729829, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x01\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 454), tid=645241, debugid=67896106, eventid=67896104, func_qualifier=2)]

@_name_boundary.callable_contract({}, 'test_kevents_filter_tid')
def meadow_test_kevents_filter_tid():
    meadow_events_buf_da07946 = meadow_RAW_VERSION2_BYTES + b'\x00' * 284
    meadow_events_buf_da07946 += b'\xa50\x147_\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x01\x00\x00\x00\x00\x00\x00y\xd8\t\x00\x00\x00\x00\x00*\x03\x0c\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    meadow_parser_61b24c1 = meadow_PyKdebugParser()
    _name_boundary.attributes(meadow_parser_61b24c1)['filter_tid'] = 645241
    meadow_events_6b165d8 = list(_name_boundary.attributes(meadow_parser_61b24c1)['kevents'](meadow_BytesIO(meadow_events_buf_da07946)))
    assert meadow_events_6b165d8 == [meadow_Kevent(timestamp=7006015729829, data=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc6\x01\x00\x00\x00\x00\x00\x00', values=(0, 0, 0, 454), tid=645241, debugid=67896106, eventid=67896104, func_qualifier=2)]
    _name_boundary.attributes(meadow_parser_61b24c1)['filter_tid'] = 3
    meadow_events_6b165d8 = list(_name_boundary.attributes(meadow_parser_61b24c1)['kevents'](meadow_BytesIO(meadow_events_buf_da07946)))
    assert meadow_events_6b165d8 == []
_name_boundary.module_contract(globals(), {'RAW_VERSION2_BYTES': 'meadow_RAW_VERSION2_BYTES', 'Kevent': 'meadow_Kevent', 'test_kevents_filter_tid': 'meadow_test_kevents_filter_tid', 'PyKdebugParser': 'meadow_PyKdebugParser', 'test_kevents': 'meadow_test_kevents', 'BytesIO': 'meadow_BytesIO'})
