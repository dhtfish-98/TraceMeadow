# Derived from pykdebugparser/trace_codes.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from typing import Mapping as meadow_Mapping
from pathlib import Path as meadow_Path

@_name_boundary.callable_contract({'codes_text': 'meadow_codes_text_3cfad72'}, 'from_trace_codes_text')
def meadow_from_trace_codes_text(meadow_codes_text_3cfad72: str) -> meadow_Mapping[int, str]:
    """
    Convert a trace codes text to dictionary.
    :param codes_text: Trace codes file data.
    :return: Mapping between code and event name.
    """
    return {int(meadow_s_b001910[0], 16): meadow_s_b001910[1] for meadow_s_b001910 in map(lambda meadow_l_0956f14: meadow_l_0956f14.split(), meadow_codes_text_3cfad72.splitlines())}

@_name_boundary.callable_contract({'path': 'meadow_path_942d9d9'}, 'from_trace_codes_file')
def meadow_from_trace_codes_file(meadow_path_942d9d9: str) -> meadow_Mapping[int, str]:
    """
    Read trace codes from a file.
    :param path: Trace codes file path.
    :return: Mapping between code and event name.
    """
    with open(meadow_path_942d9d9, 'r') as meadow_fd_39df7af:
        return meadow_from_trace_codes_text(meadow_fd_39df7af.read())

@_name_boundary.callable_contract({}, 'default_trace_codes')
def meadow_default_trace_codes() -> meadow_Mapping[int, str]:
    """
    Get the default trace codes mapping.
    :return: Mapping between code and event name.
    """
    with open(meadow_Path(__file__).resolve().parent.joinpath('trace.codes'), 'r') as meadow_fd_55292fe:
        return meadow_from_trace_codes_text(meadow_fd_55292fe.read())
_name_boundary.module_contract(globals(), {'default_trace_codes': 'meadow_default_trace_codes', 'from_trace_codes_text': 'meadow_from_trace_codes_text', 'Mapping': 'meadow_Mapping', 'from_trace_codes_file': 'meadow_from_trace_codes_file', 'Path': 'meadow_Path'})
