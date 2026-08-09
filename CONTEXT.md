# Repository Context

## Purpose

This repository is the source of truth for Noema's product behavior and cross-system contracts. It exists so design, engineering, content, research, QA, and safety work can proceed against the same model.

## Authority order

When documents disagree, use this precedence:

1. Accepted RFCs for the contract they explicitly change.
2. Versioned schemas and protocols.
3. Named subsystem specifications in `docs/`.
4. `docs/ARCHITECTURE.md` and `docs/GAME-DESIGN.md`.
5. `docs/VISION.md`.
6. Examples and non-normative commentary.

A conflict is a defect. Resolve it rather than relying permanently on precedence.

## Scope

In scope:

- the observation, hypothesis, experiment, inference, and capability loop;
- deterministic world truth and controlled uncertainty;
- provenance, replay, versioning, content compilation, validation, and migration;
- player-facing concepts and system boundaries;
- accessibility, safety, and ethical constraints that affect the product contract.

Out of scope unless introduced by RFC:

- engine choice, cloud vendor, programming language, monetization, final narrative, and platform-specific UI;
- claims that Noema is a scientifically accurate simulator of the real world;
- automated generation that bypasses review or validation.

## Canonical loop

`encounter → observe → record → hypothesize → predict → experiment → compare → revise → reproduce → unlock → reach frontier`

The world produces outcomes from hidden canonical rules. The player notebook stores interpretations separately. Instruments mediate observation. The Experiment Lab compares preregistered predictions with results. Reproducible evidence can satisfy Capability Graph requirements. The Frontier Director chooses an appropriate next opportunity without changing truth to protect a hypothesis.

## Non-negotiable invariants

- World truth and player belief MUST be separate data domains.
- A seed, content version, initial state, and ordered action log MUST support deterministic replay.
- Generated content MUST pass schema, solvability, safety, performance, and duplication gates before release.
- Unlock decisions MUST be explainable from cited evidence.
- Telemetry MUST NOT silently become canonical scientific evidence.
- Content updates MUST preserve or explicitly migrate saved provenance.

## Working conventions

Use stable identifiers, explicit units, UTC timestamps, semantic versions, and additive evolution where practical. Examples are illustrative unless marked as conformance fixtures. Unresolved decisions belong in an RFC, not hidden in implementation details.
