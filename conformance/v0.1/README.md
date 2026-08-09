# Conformance Suite — v0.1 The Chamber

Machine-readable cases for the ten acceptance tests in `docs/v0.1-ACCEPTANCE.md`.

See **[docs/v0.1-CONFORMANCE.md](../../docs/v0.1-CONFORMANCE.md)** for the normative runner contract.

```text
conformance/v0.1/
  manifest.json
  cases/C01-...json … C10-...json
```

Validate cases:

```bash
# via repository merge gate
python validation/validate_all.py
```
