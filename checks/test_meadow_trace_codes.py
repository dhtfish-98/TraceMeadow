# Derived from tests/test_trace_codes.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from tracemeadow.code_index import meadow_from_trace_codes_text as meadow_from_trace_codes_text
import pytest as meadow_pytest

@meadow_pytest.mark.parametrize('text, out', [('0x40c0548\tBSC_stat64', {67896648: 'BSC_stat64'}), ('0x80010068 ASPCORE_PUSH_PAGES                                          \t\t#Params: flow band page size\t\t#Matchby: Arg1', {2147549288: 'ASPCORE_PUSH_PAGES'}), ('0x40c0548\tBSC_stat64\n0x40c054c\tBSC_sys_fstat64', {67896648: 'BSC_stat64', 67896652: 'BSC_sys_fstat64'})])
@_name_boundary.callable_contract({'text': 'meadow_text_03a0e1c', 'out': 'meadow_out_42860a8'}, 'test_from_trace_codes_text')
def meadow_test_from_trace_codes_text(meadow_text_03a0e1c, meadow_out_42860a8):
    assert meadow_from_trace_codes_text(meadow_text_03a0e1c) == meadow_out_42860a8
_name_boundary.module_contract(globals(), {'test_from_trace_codes_text': 'meadow_test_from_trace_codes_text', 'pytest': 'meadow_pytest', 'from_trace_codes_text': 'meadow_from_trace_codes_text'})
