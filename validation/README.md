# Validation

This directory provides the merge-gate validation for NOEMA-Specs.

## Quick start

From the repository root:

```bash
bash validation/run.sh
```

The shared local/CI entrypoint installs the declared validation dependencies, runs the native unit tests, then runs the main validator, direction validator, offline freshness checker, and Gate B traceability checker. Every required check MUST exit 0; failures stop the entrypoint before later checks.

An already-qualified environment can be selected explicitly:

```bash
NOEMA_VALIDATION_VENV="/path/to/qualified/.venv" bash validation/run.sh
```

The default freshness check is metadata-only and offline. A separate live comparison can be requested explicitly with `python validation/validate_freshness.py`; it is not part of the default merge gate.

## Entrypoint recording fixture

`test_validation_entrypoint.py` exercises the real Bash entrypoint against a temporary recording interpreter. It preserves the install/check order, repository-root working directory for checks, exact injected exit status 37, no later checks after each failure, and the existing 30-second subprocess bound.

The recorder is executable shell text without a shebang. It uses [Bash's documented executable-format fallback](https://www.gnu.org/software/bash/manual/html_node/Command-Search-and-Execution.html) to invoke the real interpreter with `shlex.quote` and forward arguments with `"$@"`. This avoids putting an unquotable interpreter path in a kernel shebang and avoids the observed macOS shebang-startup stall. A regression exercises a host interpreter path containing spaces, in addition to the already-spaced fixture repository and virtual-environment paths. This is a test-double repair, not a change to the validation commands or CI policy.

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
