# TraceMeadow

An attributed derivative of **pykdebugparser**, retaining the upstream behavior while reorganizing Python modules and implementation bindings. See [ORIGIN.md](ORIGIN.md) for source, copyright and licensing.

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
