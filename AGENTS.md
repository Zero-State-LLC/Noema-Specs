# Agent Instructions

## Mission

Maintain the canonical NOEMA specification surface for a persistent science-fiction world that is instrumented for research. Player-facing presentation is game-first ([docs/PLAYER-BRAND.md](docs/PLAYER-BRAND.md)). Prefer durable contracts, machine-readable protocols, reproducible evidence, and implementation-neutral requirements. Do not implement runtime code in this repository.

For deterministic procedures for recurring specification work, see [SKILLS.md](SKILLS.md). This file remains the behavioral constraint surface.

## Required first actions

1. Read `CONTEXT.md` before editing.
2. Read `docs/TERMINOLOGY.md` and every affected subsystem document.
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

## Escalation

If CI or validation looks wrong, open a labeled defect (`bug` or `type:bug`). Do not patch tests, fixtures, or validators to obtain a green result.

## Validation

Before finishing, run available repository validation, validate JSON syntax, inspect Markdown links, run `git diff --check`, and ensure the final tree still contains every required path.
