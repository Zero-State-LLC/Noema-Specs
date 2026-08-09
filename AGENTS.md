# Agent Instructions

## Mission

Maintain a coherent, testable specification for Noema. Prefer durable contracts over implementation detail and player-observable acceptance criteria over vague intent.

## Before editing

1. Read `CONTEXT.md`, `docs/TERMINOLOGY.md`, and the affected subsystem documents.
2. Inspect schemas, protocols, examples, and accepted RFCs for adjacent contracts.
3. Check `git status`. Other agents may be editing unrelated files.

## Editing rules

- Preserve the separation between world truth, observations, evidence, beliefs, and unlock state.
- Use the canonical terms exactly. Add new domain language to `docs/TERMINOLOGY.md`.
- State requirements with MUST, SHOULD, or MAY and give each critical behavior an observable check.
- Define ownership, inputs, outputs, invariants, failure modes, and versioning for every subsystem.
- Use stable IDs rather than display names as references.
- Never invent scientific authority. Label fictional, simplified, inferred, and sourced material.
- Do not weaken provenance, consent, accessibility, safety, determinism, or replay guarantees for convenience.
- Contract-breaking changes require an RFC and migration plan.

## Validation

Before finishing:

- run repository validation scripts when present;
- check internal Markdown links and required headings;
- validate JSON/YAML examples against their schemas;
- inspect `git diff --check` and ensure only intended files changed;
- update `CHANGELOG.md` for user-visible or contract-visible changes.

## Commit discipline

Make focused commits. Do not rewrite, reset, or discard another contributor's work. Never commit secrets, personal data, copyrighted source corpora, or generated assets without documented provenance and rights.
