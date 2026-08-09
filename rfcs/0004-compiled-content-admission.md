# RFC 0004: Compiled Content Admission

- Status: Accepted
- Date: 2026-08-09

## Context

Procedural and model-assisted generation can expand a discovery world, but runtime generation without gates can create unsolvable, unsafe, duplicated, rights-unclear, or truth-leaking content.

## Decision

Runtime sessions consume only immutable promoted artifacts emitted by the Phenomenon Compiler. All authored and generated sources pass schema, dependency, determinism, invariant, solvability, safety, accessibility, performance, leakage, duplication, provenance, and rights gates. Required human review cannot be self-approved by a generator or its operator where separation of duties applies.

Artifacts separate canonical and player-safe partitions. Promotion, quarantine, revocation, and migration are auditable state transitions. Revocation blocks new sessions while preserving explicitly supported replay or migration paths.

## Consequences

Content cannot appear instantly from an unconstrained live model. The release pipeline carries additional latency and review cost. The benefit is a testable world whose mysteries remain fair and whose failures can be rolled back.

## Alternatives

Live generation with post-hoc moderation was rejected because damage occurs before detection. Schema-only validation was rejected because structurally valid phenomena can be impossible or unsafe.

## Validation

A hostile fixture suite covers truth leakage, impossible evidence paths, runaway simulation, unsafe sensory metadata, duplicate content, missing license, and self-approval.
