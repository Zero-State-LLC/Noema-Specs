# intent/ — SDLC intent records

**Kind:** process. Not a specification. Not implementation authority. Does not authorize an RFC, runtime change, or Worker publish.

Non-trivial RFCs and features start here. Copy [`_TEMPLATE.md`](_TEMPLATE.md) to a dated file (`YYYY-MM-DD-short-slug.md`). Fill every section. Label claims `OBSERVED`, `INFERRED`, `SPECULATIVE`, or `NOT_COMPUTABLE`.

## Sequence

`intent.md` → `specify/spec.md` (must include `## Workflows`) → plan → implement.

The next stage after a filled intent is `specify/spec.md`: a new draft spec or a proposed patch to existing contracts. That spec must include a `## Workflows` section. See [SKILLS.md](../SKILLS.md). Plan and implement live in runtime repositories (`Zero-State-LLC/Noema` and related clients), not in this specifications repository.

Clarifications, adapters, and docs-only hygiene that do not change contracts may skip this sequence.

## Holds

- An intent is not a spec, not a plan, not an RFC, and not a release. It does not authorize implementation or production.
- Do not invent intent records for existing RFCs.
- Do not invent protocol fields, verbs, events, or canonical behavior here.
- This directory is a template surface only until a non-trivial RFC or feature is authorized.
