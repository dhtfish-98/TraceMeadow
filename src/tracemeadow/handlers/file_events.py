# Derived from pykdebugparser/trace_handlers/fsystem.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from dataclasses import dataclass as meadow_dataclass
from typing import List as meadow_List

@_name_boundary.class_contract('VfsLookup', {})
@meadow_dataclass
class meadow_VfsLookup:
    ktraces: meadow_List
    path: str
    vnode_id: int

    @_name_boundary.callable_contract({'self': 'meadow_self_ec08e19'}, '__str__')
    def __str__(meadow_self_ec08e19):
        return f'lookup("{meadow_self_ec08e19.path}"), vnode id: {meadow_self_ec08e19.vnode_id}'

@_name_boundary.callable_contract({'parser': 'meadow_parser_c607bd4', 'events': 'meadow_events_f171e6f'}, 'handle_vfs_lookup')
def meadow_handle_vfs_lookup(meadow_parser_c607bd4, meadow_events_f171e6f):
    meadow_node_15a9204 = _name_boundary.attributes(meadow_parser_c607bd4)['parse_vnode'](meadow_events_f171e6f)
    return meadow_VfsLookup(meadow_events_f171e6f, meadow_node_15a9204.path, meadow_node_15a9204.vnode_id)
meadow_handlers = {'VFS_LOOKUP': meadow_handle_vfs_lookup}
_name_boundary.module_contract(globals(), {'handlers': 'meadow_handlers', 'VfsLookup': 'meadow_VfsLookup', 'dataclass': 'meadow_dataclass', 'handle_vfs_lookup': 'meadow_handle_vfs_lookup', 'List': 'meadow_List'})
