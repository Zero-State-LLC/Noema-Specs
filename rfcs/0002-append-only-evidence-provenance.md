# RFC 0002: Append-Only Evidence Provenance

- Status: Accepted
- Date: 2026-08-09

## Context

Progress depends on evidence. Mutable measurements or opaque scoring would make unlocks impossible to audit and collaboration impossible to trust.

## Decision

Observations, preregistrations, trial results, assessments, and evidence relationships are immutable records with stable IDs, integrity digests, versions, conditions, actors, and parent references. Corrections, exclusions, and invalidations append status records or derived successors. They never overwrite history.

Every unlock-relevant predicate MUST cite exact eligible evidence IDs and an evaluator version. Imported evidence remains untrusted until integrity, permission, compatibility, and provenance validation succeeds.

## Consequences

Storage grows and erasure workflows require separating personal attribution from scientific lineage. In return, decisions are explainable, assessments are reproducible, and historical conclusions can be recomputed after invalidation.

## Alternatives

Mutable notebook rows were rejected because edits destroy lineage. A single numeric “knowledge score” was rejected because it hides why progression occurred.

## Privacy

Personal identity SHOULD be referenced through revocable or pseudonymous actor records. Privacy deletion may remove identity linkage while preserving a non-identifying integrity tombstone where legally permitted.

## Validation

Tests attempt mutation, duplicate retry, recalibration, evidence invalidation, import, and identity redaction and verify that lineage remains coherent.
