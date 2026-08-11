# Experiment Lifecycle

Execution states are `DRAFT → VALIDATED → READY → RUNNING → COMPLETE`, with exits `INVALID`, `ABORTED`, `PARTIAL`, `NOT_COMPUTABLE`, and `QUARANTINED`. Interpretation is separately `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_SUPPORTED`, or `INCONCLUSIVE`. Claim provenance is separately `OBSERVED`, `INFERRED`, `SPECULATIVE`, or `NOT_COMPUTABLE`. `PROVEN` is forbidden.

`VALIDATED` means contract validity, not support. `READY` additionally requires resolved fork, authorization, consent, a frozen plan DAG, registered variables, and pinned metrics. Each transition appends an audit record: `previous_state`, `new_state`, `reason_code`, `actor_or_system`, `evidence_refs`, `cycle_or_time`, `previous_digest`, and `digest`. Corrections append lineage rather than rewriting it. Budget exhaustion is `PARTIAL` with every unexecuted node identified.
