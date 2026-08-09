# Validation

This directory provides the merge-gate validation for NOEMA-Specs.

## Quick start

```bash
pip install -r requirements-validation.txt
python validation/validate_all.py
```

The command MUST exit 0 and report `PASS` for a change to be mergeable.

## What is checked

- Required root and directory structure (aligned with SPEC-CHECKLIST.md)
- JSON Schema and example parsing (Draft 2020-12)
- Internal Markdown relative links
- Claim-label vocabulary and consciousness-score prohibition
- Presence of ADR index and RFC template
- Basic structure for future env-var and schema cross-checks

## Adding checks

Extend pure functions under `validation/lib/` (to be expanded). Keep side effects in `validate_all.py`. All checks must be deterministic and offline.
