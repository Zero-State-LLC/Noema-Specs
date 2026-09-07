# Experiment Lifecycle

Execution states are `DRAFT → VALIDATED → READY → RUNNING → COMPLETE`, with exits `INVALID`, `ABORTED`, `PARTIAL`, `NOT_COMPUTABLE`, and `QUARANTINED`. Interpretation is separately `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_SUPPORTED`, or `INCONCLUSIVE`. Claim provenance is separately `OBSERVED`, `INFERRED`, `SPECULATIVE`, or `NOT_COMPUTABLE`. `PROVEN` is forbidden.

`VALIDATED` means contract validity, not support. `READY` additionally requires resolved fork, authorization, consent, a frozen plan DAG, registered variables, and pinned metrics. Each transition appends an audit record: `previous_state`, `new_state`, `reason_code`, `actor_or_system`, `evidence_refs`, `cycle_or_time`, `previous_digest`, and `digest`. Corrections append lineage rather than rewriting it. Budget exhaustion is `PARTIAL` with every unexecuted node identified.

## STUDY projection

The technical lifecycle projects deterministically to `Preparing test` for `DRAFT`/`VALIDATED`, `Ready` for `READY`, `Testing` for `RUNNING`, `Result available` for `COMPLETE`, `Incomplete result` for `PARTIAL`, and `Cannot determine` for `NOT_COMPUTABLE`. `INVALID`, `ABORTED`, and `QUARANTINED` display that the test cannot be interpreted. The projection never hides the canonical execution state, interpretation, claim label, confounds, or audit record from an authorized advanced view.

## Extension Points

Non-normative future guidance; this section does not authorize new behavior.

- Lifecycle audit consumers and STUDY status projections can be extended without conflating execution, interpretation, and claim provenance. Preserve append-only correction lineage, the READY prerequisites, and the prohibition on PROVEN.
- Version any transition or projection mapping change through the owning contract before promotion; old audit chains remain interpretable. Validate budget exhaustion with every unexecuted node recorded, quarantine without interpretation, and corrections linked to the previous digest.
