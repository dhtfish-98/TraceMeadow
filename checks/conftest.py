# Derived from tests/conftest.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
import pytest as meadow_pytest
from tracemeadow.stack_stream import meadow_CallstacksParser as meadow_CallstacksParser
from tracemeadow.code_index import meadow_default_trace_codes as meadow_default_trace_codes
from tracemeadow.trace_stream import meadow_TracesParser as meadow_TracesParser

@meadow_pytest.fixture(scope='function')
@_name_boundary.callable_contract({}, 'traces_parser')
def meadow_traces_parser():
    return meadow_TracesParser(meadow_default_trace_codes(), {}, {})

@meadow_pytest.fixture(scope='function')
@_name_boundary.callable_contract({}, 'callstacks_parser')
def meadow_callstacks_parser():
    return meadow_CallstacksParser([], [])
_name_boundary.module_contract(globals(), {'CallstacksParser': 'meadow_CallstacksParser', 'default_trace_codes': 'meadow_default_trace_codes', 'pytest': 'meadow_pytest', 'TracesParser': 'meadow_TracesParser', 'callstacks_parser': 'meadow_callstacks_parser', 'traces_parser': 'meadow_traces_parser'})
