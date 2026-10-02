# Origin and attribution

TraceMeadow is a derived, reorganized version of pykdebugparser.

- Source: https://github.com/matan1008/pykdebugparser.git
- Baseline commit: `9353b4f0ce1e5d86eeb78d93a500626a5385c109`
- Baseline tree: `b291e46563de1d261d54ee9cc4d6364830f2426b`
- License: MIT; the original license and copyright are retained.

The original algorithms and project history belong to their upstream authors. This derivative introduces renamed implementation bindings resolved by lexical scope, renamed modules, and explicit adapters separating public data labels from internal implementation names. It does not claim independent authorship of upstream code or approval by any verification program.

Release 1.0.2 adds a new bounded stream/metadata reader and rewrites production v2/v3 framing, trace-code text/file loading and CLI file/record/output consumption. The new implementation was developed with Codex assistance and checked against owned synthetic wire fixtures and the pinned upstream behavior. Existing event models, handler catalogs, aggregation and formatting remain upstream-derived; they have not all been substantively rewritten. Original public Construct schemas and compatibility labels are retained. Invalid-input errors and explicit v2 padding intentionally differ as documented in VALIDATION.md.

Public CLI flags, structured data keys, enum identifiers, Python framework hooks, legacy external API aliases, resource formats and compatibility labels are deliberate naming exceptions. The compatibility module provides separate wire/display labels; it is not a hidden copy of the old implementation.
