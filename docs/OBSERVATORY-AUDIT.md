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


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Audit examples can cover candidate rejection, duplication, confounding, and partial processing as carefully as READY_FOR_LAB. Preserve append-only transition lineage and the distinction between detector results, threshold decisions, and claim-bearing promotion.

- Additional operations, lifecycle transitions, or digest inputs need audit-schema and analysis-run compatibility review. Retain original configuration limits and chain inputs for prior runs; increasing a later processing bound must not silently turn an old PARTIAL run into a complete one.

- Validate record-index order, previous_record_digest continuity, input/result digests, and actor/reason evidence for each transition. Exercise limit exhaustion with an explicit unprocessed range, and verify a failed or NOT_COMPUTABLE candidate remains queryable without being promoted by a missing audit link.
