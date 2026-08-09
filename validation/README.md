# Validation

This directory provides the merge-gate validation for NOEMA-Specs.

## Quick start

From the repository root:

```bash
pip install -r validation/requirements-validation.txt
python validation/validate_all.py
```

The command MUST exit 0 and report `PASS` for a change to be mergeable.

## What is checked

- Required root, docs, protocols, schemas, research, ADR, and example structure
- JSON Schema and example parsing (including JSONL)
- Internal Markdown relative links
- Claim-label vocabulary and consciousness-score prohibition
- `.env.example` variables documented in `docs/ENVIRONMENT.md`
- Contract quality markers (MUD, BBS, Deep Time, Unknown Ontology, Situation Genome)
- `examples/v01-seed/` integrity:
  - ≥3 rooms, infrastructure entity, resource node, budget defaults
  - trajectory envelope + payload schema validation against `event-types.json`
  - full closed 24-type catalog coverage
  - required acceptance events (LOOK, MOVE, MOVE_REJECTED, BUDGET_EXCEEDED, OBSERVATION_GENERATED, MESSAGE, ORG_CREATE)
  - digest chain continuity and equivalence-boundary fields
- `examples/negative/` rejection corpus (≥6 fixtures; schema, catalog, and semantic cases)

## Adding checks

Keep checks pure and deterministic. Prefer offline validation only (no network). New fixtures under `examples/v01-seed/` or `examples/negative/` should extend this suite rather than bypass it.
