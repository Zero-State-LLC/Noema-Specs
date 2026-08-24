# Validation

This directory provides the merge-gate validation for NOEMA-Specs.

## Quick start

From the repository root:

```bash
pip install -r validation/requirements-validation.txt
python validation/validate_all.py
python validation/validate_direction.py
```

Both commands MUST exit 0. The main validator reports `PASS`; the direction validator confirms that planning remains implementation-aware and status-disciplined.

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
- Schema validation of seed, state, snapshot, boundary, protocol, and observation fixtures
- `conformance/v0.1/` suite: 26 cases, fixture linkage, acceptance item coverage 1–26
- Deployment/runtime-manifest and strategic/module/spectator fixtures and related negatives
- Direction package presence, current-state evidence pins, implementation-plane status vocabulary, active integration campaign markers, and stale live-guidance rejection

## Adding checks

Keep checks pure and deterministic. Prefer offline validation only (no network). New fixtures under `examples/v01-seed/` or `examples/negative/` should extend this suite rather than bypass it.
