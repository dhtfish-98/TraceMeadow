# Validation

Local validation date: 2026-10-02 (Asia/Tokyo). Python 3.12.13.

- Upstream tests: 69 passed.
- Derivative tests: 79 passed.
- Independent upstream/derivative observations: 1133; zero differences. Return values, serialized keys/display labels, binary output and observed exception types/messages are checked.
- Scope-resolved source/module mappings are in SYMBOL_MAP.json and FILE_MAP.json. Python protocol hooks, framework callbacks, serialized field labels, enum identifiers, public compatibility aliases and fixed fixture bytes are explicit exceptions. Obsolete upstream packaging and Sphinx build configuration were replaced by the current build/CI configuration.

## Reproduce

```sh
python -m pip install -r requirements-test.lock
python -m pip install -e .
python -m pytest -q
python checks/compare_upstream.py --upstream-root /path/to/pinned-upstream-checkout
python -m build
python -m pip install dist/*.whl
python -I checks/consume_installation.py
```

The GitHub workflow checks out upstream commit `9353b4f0ce1e5d86eeb78d93a500626a5385c109` separately. Package builds, independent consumer installation and final package/source hash checks are recorded in DELIVERY_VALIDATION.json when completed. Source comparison does not establish device or external-service behavior.

## Limits

- Real-device live tracing and additional OS/firmware versions: OPEN.
- Public dataclass/namedtuple event fields, enum identifiers and trace catalog names intentionally remain wire labels.
