# Validation

Local validation: 2026-10-02 (Asia/Tokyo), Python 3.12.13, derivative release 1.0.2. Machine-readable runtime hashes and scope are in [CURRENT_VALIDATION.json](CURRENT_VALIDATION.json).

- Current tests: **435 passed**, including 356 new stream, metadata, resource and CLI boundary cases and the 79 retained derivative tests.
- Original upstream tests: **69 passed** against the separately downloaded fixed commit. All 43 archive source files were checked byte for byte after the upstream run.
- Comparison: **1,133 observations**, consisting of **1,073 equal observations** and **60 explicitly checked error changes**. The invalid short/random stream cases now report a truncated/unsupported trace version through `TraceFormatError` rather than an upstream `KeyError`. No other differences in this comparison were accepted.
- Twenty current runtime Python files parsed successfully. The runtime hash list is a source identity record, not proof of all possible behavior.

New cases use owned synthetic wire data: v2 zero-prefix timestamps, explicit padding, every truncation of a required v3 prefix, both retained v3 event-length conventions, continuation blocks, metadata merging, fragmented nonseekable reads, marker EOF, byte/count limits, plist duplicate keys/cycles/depth/entities/reference allocation limits, output limits, exact record counts, regular-file changes and actual CLI FIFO/link/directory rejection. The OS-log integration also uses a clearly attributed upstream fixture. No samples are executed and no system trace is collected.

## Reproduce

```sh
python -m pip install -r requirements-test.lock
python -m pip install -e .
python -m pytest -q -p no:cacheprovider
python checks/compare_upstream.py --upstream-root /path/to/pinned-upstream-checkout
python -m build
python -m venv .consumer
.consumer/bin/python -m pip install dist/*.whl
.consumer/bin/python -I checks/consume_installation.py
```

CI checks out upstream commit `9353b4f0ce1e5d86eeb78d93a500626a5385c109` separately. An installed consumer checks package origin, catalog access, packed and explicitly padded v2 records, missing-marker errors and the distribution version. CI results must be matched to the published commit. Source tests alone do not establish that an installed artifact matches it.

## Compatibility and remaining work

- v2 zero padding is explicit; the previous byte-scanning heuristic could consume event data. See README for the CLI option.
- EOF without a marker and incomplete final records fail instead of looping or silently accepting a partial trace. Malformed/over-limit metadata fails before further interpretation.
- Public event fields, enum identifiers, trace catalogs and compatibility aliases remain attributed wire/API contracts. Existing Construct builder schemas remain available; the production parser uses the new bounded reader.
- JSON wrappers for bytes, datetimes and plist UIDs are documented extensions. Partial output at an error must not be treated as a complete report.
- The large retained handler catalogs, aggregation/state logic, call-stack processing and formatters are **not fully rewritten or universally bounded**. This release completes the input/metadata/CLI phase, not every upstream algorithm.
- Continued stdin writers and caller-provided library readers can block. Byte/count caps do not enforce a wall-clock timeout.
- Live tracing, real devices, additional OS/firmware formats and universal malformed-input coverage: **OPEN**. Source comparison is not a device or service result.
- Comprehensive sensitive-data redaction and terminal escaping: **OPEN**.

`DELIVERY_VALIDATION.json`, older 79-test / 1,133-equal reports, release 1.0.0 assets and the executable-mode packaging change in 1.0.1 describe historical artifacts. They do not validate the new parser. This release retains original author attribution and does not establish CVP admission.
