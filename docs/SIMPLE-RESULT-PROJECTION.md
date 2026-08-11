# Simple Result Projection

A simple STUDY result is a deterministic, non-authoritative projection of one [`Lab Result`](../specs/lab-result.schema.json). It is not a new experiment and cannot strengthen the underlying interpretation or claim label.

The projection copies `experiment_id`, `lab_result_id`, `source_intent_id`, `interpretation`, `claim_label`, `compiler_readiness`, evidence references, counterevidence, confounds, and limits. Its display maps outcome classes as follows:

| Outcome | Plain-language display |
|---|---|
| `PERSISTED` | Behavior still occurred. |
| `DEGRADED` | Behavior occurred less reliably or less strongly. |
| `DISAPPEARED` | Behavior was not observed under the changed condition. |
| `CHANGED_FORM` | Behavior continued in a materially different form. |
| `NOT_COMPARABLE` | These tests differed too much to compare reliably. |
| `NOT_COMPUTABLE` | NOEMA cannot determine this from the available evidence. |

Every projection says “within the tested conditions” unless it is `NOT_COMPARABLE` or `NOT_COMPUTABLE`. It MUST expose limitations and link advanced drill-down to the same evidence record. A `CAPTURE_AS_TEST` action is valid only when `compiler_readiness` is `READY`; otherwise the allowed next action is bounded to further testing, confound resolution, or rejection review.
