# Agent Instructions

## Mission

Maintain the canonical NOEMA specification surface for a persistent science-fiction world that is instrumented for research. Player-facing presentation is game-first ([docs/PLAYER-BRAND.md](docs/PLAYER-BRAND.md)). Prefer durable contracts, machine-readable protocols, reproducible evidence, and implementation-neutral requirements. Do not implement runtime code in this repository.

For deterministic procedures for recurring specification work, see [SKILLS.md](SKILLS.md). This file remains the behavioral constraint surface.

Non-trivial RFCs and features are intent-first: start from [intent/README.md](intent/README.md) before `specify/spec.md` or an RFC draft.

## Required first actions

1. Read `CONTEXT.md` before editing.
2. Read `GLOSSARY.md` and every affected subsystem document.
3. Inspect related protocols, schemas, examples, research files, and RFCs.
4. Check `git status` and avoid overwriting another contributor's work.

## Editing rules

- Use canonical terminology exactly.
- Do not invent protocol fields without a spec change and version review.
- Do not modify public schemas silently.
- Do not conflate OBSERVED, INFERRED, SPECULATIVE, or NOT_COMPUTABLE claims.
- Do not make unsupported consciousness or AGI claims.
- Do not create a scalar consciousness score.
- Reproducibility-critical changes require validation evidence.
- Protocol, schema, ontology semantics, reproducibility boundary, claims policy, and security boundary changes require the RFC process.
- Maintain backward compatibility where required.
- Avoid hidden coupling between subsystems.
- Prefer deterministic state transitions and explicit seeded nondeterminism.
- Preserve event provenance and lineage.
- Never commit real secrets, private prompts, or proprietary architecture details in fixtures.
- Update roadmap and versioning docs when changing milestones or version domains.
- Do not implement runtime code in this repository.

## SDLC

Non-trivial RFCs and features start here:

1. `intent.md` — copy [intent/_TEMPLATE.md](intent/_TEMPLATE.md); see [intent/README.md](intent/README.md).
2. `specify/spec.md` — include `## Workflows` (see [SKILLS.md](SKILLS.md)).
3. plan
4. implement (runtime repositories; not this specifications repository)

Clarifications, adapters, and docs-only hygiene that do not change contracts may skip this sequence. Do not invent intent records for existing RFCs.

## Escalation

If CI or validation looks wrong, open a labeled defect (`bug` or `type:bug`). Do not patch tests, fixtures, or validators to obtain a green result.

## Validation

Before finishing, run available repository validation, validate JSON syntax, inspect Markdown links, run `git diff --check`, and ensure the final tree still contains every required path.

## Agent skills

Pocock engineering skills ([mattpocock/skills](https://github.com/mattpocock/skills)) read this configuration. Repo-specific `SKILL.*` procedures stay in [SKILLS.md](SKILLS.md).

### Issue tracker

GitHub Issues on `Zero-State-LLC/Noema-Specs`, via `gh`. See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical roles under their default names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `GLOSSARY.md` plus `docs/adr/`. `CONTEXT.md` is authority, not a glossary. See `docs/agents/domain.md`.

<!-- graft:start -->
## Graft — repo context graph

`graft/` indexes the code (`validation/*.py`), not the Markdown specs. Start with `graft map`; ask with `graft ask "<question>" --source`; use `graft grep "<literal>"` for every occurrence and `graft callers <symbol>` for call edges. Entry point: `graft/INDEX.md`. Rebuild with `GRAFT_NO_GITIGNORE=1 graft build` after editing validators. See [CONTRIBUTING.md](CONTRIBUTING.md#graft-context-index).
<!-- graft:end -->
