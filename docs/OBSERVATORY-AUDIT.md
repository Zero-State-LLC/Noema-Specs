# Observatory Audit (v0.3)

Every claim-bearing decision MUST be reconstructable.

Schema: [`specs/observatory-audit-record.schema.json`](../specs/observatory-audit-record.schema.json).  
Analysis run: [`specs/observatory-analysis-run.schema.json`](../specs/observatory-analysis-run.schema.json).

## Audit record fields

```text
analysis_run_id
record_index
operation
input_digest
feature_result_digest?
baseline_result_digest?
detector_result
threshold_decision
candidate_action
reason_code
previous_record_digest
record_digest
claim_label
```

## Candidate lifecycle

```text
DETECTED → TRIAGED → RETAINED → READY_FOR_LAB
exits: REJECTED | INSUFFICIENT_EVIDENCE | DUPLICATE | CONFOUNDED | NOT_COMPUTABLE
```

Transitions append lineage (actor, reason, evidence, digests). No overwrite.

## Limits (versioned)

`specs/observatory-config.v03.json`: max trajectory window, feature count, baseline records, candidates per run. Exceeded ⇒ status `PARTIAL` with unprocessed range.
