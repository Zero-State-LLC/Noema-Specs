# Captured Test Format

## Package layout

```text
captured-tests/<id>/
├── manifest.json      # captured-test/0.5 record
├── fixture/
├── oracle.json
├── provenance.json
├── evidence.json
├── expected.json
├── controls.json
└── README.md
```

Reference package: [`examples/v05-compiler/captured-test/`](../examples/v05-compiler/captured-test/).

Align with [REPRODUCIBILITY.md](REPRODUCIBILITY.md). Prefer content-addressed refs over duplicating canonical Lab/Observatory data.

## Simple view budget

Show only: what was captured, required, removed, validation summary, important limitations, next action.

Hide by default: digests, schema versions, audit roots, unit manifests, dependency IDs, oracle cache keys.
