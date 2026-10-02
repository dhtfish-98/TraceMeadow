# TraceMeadow

防御用途、实际能力及本轮验证范围见 [DEFENSIVE_SCOPE.md](DEFENSIVE_SCOPE.md)。

An attributed derivative of **pykdebugparser** for authorized, offline trace analysis. Release 1.0.2 rewrites the input reader, v2/v3 record framing, metadata validation, trace-code loading and CLI consumption. See [ORIGIN.md](ORIGIN.md) for source, copyright and licensing.

TraceMeadow parses Darwin kdebug event buffers, trace headers, system-call traces, loaded-image events, sampled call stacks and OS log records. It provides the existing kevents, traces, callstacks, images, kexts, logs and processes commands. Binary streaming, event records, code catalogs and trace handlers are separate modules.

Public event keys, namedtuple/dataclass field names and event identifier catalogs are stable data contracts. Renamed implementation classes and lexical bindings are listed separately from these wire labels in SYMBOL_MAP.json.

## Install

```sh
python -m pip install .
tracemeadow --help
```

## Development

```sh
python -m pip install '.[test]'
python -m pytest
python -m build
```

New implementation names are listed in `SYMBOL_MAP.json`, and module/file mappings in `FILE_MAP.json`. External data labels and public compatibility aliases are kept at an explicit adapter boundary. The `guides` directory contains clearly attributed historical upstream documentation; its original commands refer to the upstream project.

See [VALIDATION.md](VALIDATION.md) for measured checks and remaining environmental limits.

## Compare with upstream

```sh
python checks/compare_upstream.py --upstream-root /path/to/pinned-upstream-checkout
```

The source checkout is supplied explicitly; no developer machine paths are embedded. The public CI pins the original upstream commit and repeats tests, comparison, build and installed consumption.

## Input and output behavior in 1.0.2

- CLI files must be nonempty regular files of at most 1 GiB. Final-component symlinks, directories and FIFOs are rejected. `-` reads caller-provided stdin; a writer that stays open can still make a read wait.
- Packed v2 streams use zero padding by default. If the capture has known zero-filled header padding, specify its exact byte count before the command: `tracemeadow --v2-padding 3808 kevents capture.bin`. The parser no longer guesses padding by skipping zero bytes, which could consume a legitimate event timestamp.
- Missing markers, truncated records, unsupported versions, ambiguous duplicate metadata keys and exceeded input limits raise `TraceFormatError`; CLI input/output failures return status 2. Reports printed before a failure are incomplete.
- Defaults also bound each block and cumulative metadata to 64 MiB, marker searches to 16 MiB, thread maps to 65,536 entries, events to 4,194,304, chunks to 4,096 and metadata graphs to 1,048,576 nodes / 128 levels. These are finite work limits, not wall-clock timeouts or bounds on all retained handler state.
- CLI output is limited to 16 MiB of UTF-8. Metadata JSON encodes bytes as `{"$bytes_hex":"..."}`, datetime values as `{"$datetime":"..."}` and plist UIDs as `{"$plist_uid":n}`. These wrappers do not define an automatic reverse decoder.
- A positive command count selects only that many records; it does not validate the rest of the stream. Metadata commands consume the whole stream without collecting every event into a list.

The supported v3 framing is the existing upstream dialect, including its two event-size conventions. This does not establish support for every Darwin capture format. Other retained handler state, syscall interpretation and formatting algorithms still require further rewriting and validation. Logs can contain sensitive values and terminal control characters; output does not provide comprehensive redaction or terminal escaping.

## Aggregation and call-stack behavior in 1.0.3

The event-group state machine and call-stack/image attribution are now substantively rewritten. Defaults limit active groups to 4,096, stored event references to 1,048,576, each group to 65,536 events and processed records to 4,194,304. Group insertion/replacement is checked before mutation; completed empty thread groups are removed. Vnode path assembly uses bounded chunks (1 MiB / 65,536 events) instead of repeated whole-path concatenation. Invalid handler data produces TraceFormatError.

Call-stack defaults limit each sample to 65,536 frames, image tables to 65,536 entries and consumed traces to 4,194,304. Image tables must initially be aligned and sorted; addresses are unsigned 64-bit. Same-address insertions retain the first registered identifier. Attribution still chooses the nearest preceding image base without a proven image extent; these offsets are heuristic candidates.

These limits bound the new group storage and call-stack operations. They do not fully bound other handler-owned maps, caller mutations, all formatting operations or unmatched groups at EOF. Unmatched ends and replacement of an existing same-ID start retain the documented upstream convention. A stream can still contain unresolved groups; successfully exhausting the group iterator is not proof of a complete capture.

Call-stack formatting checks its 16 MiB UTF-8 budget before allocating each indented frame line. This prevents large bounded samples from materializing quadratic-size indentation before the CLI can check output. Other formatters remain within the stated unfinished scope.
