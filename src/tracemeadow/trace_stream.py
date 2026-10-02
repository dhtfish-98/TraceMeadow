# Derived from pykdebugparser/traces_parser.py; original copyright and license in ORIGIN.md and LICENSE.
import tracemeadow_boundary as _name_boundary
from collections import namedtuple as meadow_namedtuple
from tracemeadow.event_records import meadow_DgbFuncQual as meadow_DgbFuncQual
from tracemeadow.handlers.unix_calls import meadow_handlers as meadow_bsd_handlers
from tracemeadow.handlers.image_events import meadow_handlers as meadow_dyld_handlers
from tracemeadow.handlers.file_events import meadow_handlers as meadow_fsystem_handlers
from tracemeadow.handlers.kernel_calls import meadow_handlers as meadow_mach_handlers
from tracemeadow.handlers.performance_events import meadow_handlers as meadow_perf_handlers
from tracemeadow.handlers.lifecycle_events import meadow_handlers as meadow_trace_handlers
from tracemeadow.handlers.priority_events import meadow_handlers as meadow_turnstile_handlers
meadow_Vnode = _name_boundary.named_record('Vnode', ['ktraces', 'vnode_id', 'path'])

from tracemeadow.bounded_stream import TraceFormatError

@_name_boundary.class_contract('TracesParser', {'feed': 'meadow_feed', 'feed_generator': 'meadow_feed_generator', 'parse_event_list': 'meadow_parse_event_list', 'vnode_generator': 'meadow_vnode_generator', 'parse_vnode': 'meadow_parse_vnode', 'parse_vnodes': 'meadow_parse_vnodes', '_feed_start_event': 'meadow__feed_start_event', '_feed_end_event': 'meadow__feed_end_event', '_feed_single_event': 'meadow__feed_single_event', 'trace_codes': 'meadow_trace_codes', 'on_going_events': 'meadow_on_going_events', 'on_going_traces': 'meadow_on_going_traces', 'global_strings': 'meadow_global_strings', 'threads_pids': 'meadow_threads_pids', 'pids_names': 'meadow_pids_names', 'tids_names': 'meadow_tids_names', 'qualifiers_actions': 'meadow_qualifiers_actions', 'last_data_newthread': 'meadow_last_data_newthread', 'last_data_exec': 'meadow_last_data_exec', 'handlers': 'meadow_handlers'})
class meadow_TracesParser:
    """Bounded event-group storage with the attributed handler dispatch contract."""
    def __init__(self, trace_codes_map, threads_pids, pids_names, *,
                 max_groups=4096, max_references=1048576,
                 max_group_events=65536, max_events=4194304):
        if any(type(v) is not int or v <= 0 for v in
               (max_groups, max_references, max_group_events, max_events)):
            raise ValueError('aggregation limits must be positive integers')
        self.trace_codes = trace_codes_map
        self.threads_pids, self.pids_names = threads_pids, pids_names
        self.on_going_events, self.on_going_traces = {}, {}
        self.global_strings, self.tids_names = {}, {}
        self.last_data_newthread = self.last_data_exec = None
        self._max_groups, self._max_references = max_groups, max_references
        self._max_group_events, self._max_events = max_group_events, max_events
        self._groups = self._references = self._fed = 0
        self.qualifiers_actions = {
            1: self.meadow__feed_start_event, 2: self.meadow__feed_end_event,
            0: self.meadow__feed_single_event, 3: self.meadow__feed_single_event}
        self.handlers = {}
        for table in (meadow_bsd_handlers, meadow_dyld_handlers, meadow_fsystem_handlers,
                      meadow_mach_handlers, meadow_perf_handlers, meadow_trace_handlers,
                      meadow_turnstile_handlers):
            self.handlers.update(table)

    def meadow_feed(self, event):
        if self._fed >= self._max_events:
            raise TraceFormatError('aggregation event limit exceeded; analysis is incomplete')
        self._fed += 1
        action = self.qualifiers_actions.get(event.func_qualifier)
        if action is None:
            raise TraceFormatError('unsupported event qualifier')
        name = self.trace_codes.get(event.eventid)
        state = self.on_going_traces if name in meadow_trace_handlers else self.on_going_events
        return action(event, state)

    def meadow_feed_generator(self, generator):
        for event in generator:
            result = self.meadow_feed(event)
            if result is not None:
                yield result

    def meadow_parse_event_list(self, events):
        if not isinstance(events, (list, tuple)):
            materialized = []
            for event in events:
                if len(materialized) >= self._max_group_events:
                    raise TraceFormatError('handler event-list limit exceeded')
                materialized.append(event)
            events = materialized
        if not events:
            return None
        if len(events) > self._max_group_events:
            raise TraceFormatError('handler event-list limit exceeded')
        handler = self.handlers.get(self.trace_codes.get(events[0].eventid))
        if handler is None:
            return None
        try:
            return handler(self, events)
        except TraceFormatError:
            raise
        except (ValueError, TypeError, KeyError, IndexError, AttributeError, OverflowError):
            raise TraceFormatError('incomplete or unsupported handler event data') from None

    @staticmethod
    def meadow_vnode_generator(events, *, max_path_bytes=1048576, max_events=65536):
        if any(type(v) is not int or v <= 0 for v in (max_path_bytes, max_events)):
            raise ValueError('vnode limits must be positive integers')
        parts, lookup_events, length, vnode_id = [], [], 0, 0
        for count, event in enumerate(events):
            if count >= max_events:
                raise TraceFormatError('vnode event limit exceeded')
            piece = event.data
            if event.func_qualifier & 1:
                vnode_id = event.values[0]
                piece = piece[8:]
            if not isinstance(piece, bytes):
                raise TraceFormatError('vnode event payload must be bytes')
            length += len(piece)
            if length > max_path_bytes:
                raise TraceFormatError('vnode path byte limit exceeded')
            parts.append(piece); lookup_events.append(event)
            if event.func_qualifier & 2:
                try:
                    path = b''.join(parts).replace(bytes([0]), b'').decode('utf-8')
                except UnicodeDecodeError:
                    raise TraceFormatError('invalid vnode path encoding') from None
                yield meadow_Vnode(lookup_events, vnode_id, path)
                parts, lookup_events, length, vnode_id = [], [], 0, 0

    def meadow_parse_vnode(self, events):
        nodes = self.meadow_parse_vnodes(events)
        return nodes[0] if nodes else meadow_Vnode([], 0, '')

    def meadow_parse_vnodes(self, events):
        selected = (event for event in events
                    if self.trace_codes.get(event.eventid) == 'VFS_LOOKUP')
        return list(self.meadow_vnode_generator(selected, max_events=self._max_group_events))

    def _append(self, groups, event, restart=None):
        old = groups.get(restart) if restart is not None else None
        added_group = restart is not None and restart not in groups
        group_count = self._groups + added_group
        removed = len(old) if old is not None else 0
        new_references = self._references - removed + len(groups) + added_group
        if group_count > self._max_groups or new_references > self._max_references:
            raise TraceFormatError('pending event-group limit exceeded; analysis is incomplete')
        if any(len(items) >= self._max_group_events for key, items in groups.items()
               if key != restart):
            raise TraceFormatError('pending group event limit exceeded; analysis is incomplete')
        # Preflight every limit before resetting a same-ID start or adding references.
        if restart is not None:
            groups[restart] = []
        for items in groups.values():
            items.append(event)
        self._groups, self._references = group_count, new_references

    def meadow__feed_start_event(self, event, state):
        groups = state.get(event.tid, {})
        self._append(groups, event, restart=event.eventid)
        state[event.tid] = groups

    def meadow__feed_end_event(self, event, state):
        groups = state.get(event.tid)
        if groups is None or event.eventid not in groups:
            return None
        self._append(groups, event)
        events = groups.pop(event.eventid)
        self._groups -= 1; self._references -= len(events)
        if not groups:
            del state[event.tid]
        return self.meadow_parse_event_list(events)

    def meadow__feed_single_event(self, event, state):
        self._append(state.get(event.tid, {}), event)
        return self.meadow_parse_event_list([event])

_name_boundary.module_contract(globals(), {'Vnode': 'meadow_Vnode', 'bsd_handlers': 'meadow_bsd_handlers', 'TracesParser': 'meadow_TracesParser', 'fsystem_handlers': 'meadow_fsystem_handlers', 'trace_handlers': 'meadow_trace_handlers', 'perf_handlers': 'meadow_perf_handlers', 'turnstile_handlers': 'meadow_turnstile_handlers', 'dyld_handlers': 'meadow_dyld_handlers', 'DgbFuncQual': 'meadow_DgbFuncQual', 'namedtuple': 'meadow_namedtuple', 'mach_handlers': 'meadow_mach_handlers'})
