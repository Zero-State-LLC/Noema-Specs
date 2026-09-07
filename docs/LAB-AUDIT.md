# Lab Audit

`lab-audit-record/0.4` hash-chains design validation, plan generation, fork creation, intervention application, control execution, run start/completion, divergence detection, feature/metric calculation, replication comparison, result classification, lifecycle transition, and Compiler handoff. It records sequence, previous digest, canonical input/output references, actor/system, cycle/time, reason code, and digest. Replay reconstructs the research-layer history and never emits a world event.

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Additional Lab lifecycle audit coverage can link new research derivations to their canonical input/output references and existing Compiler handoff.

**Preserved invariants.** Preserve append-only sequence and previous-digest lineage; replay reconstructs research history only and never emits world events.

**Compatibility and promotion.** Changes to the closed lab-audit-record/0.4 shape or canonical hashing require a versioned schema and compatibility fixtures; an audit entry is not itself a promotion decision.

**Validation expectations.** Check replay of a complete chain, missing and reordered records, altered inputs, and superseding corrections; confirm failures remain visible and research records cannot enter the world ledger.
