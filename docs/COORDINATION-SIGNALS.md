# Coordination Signals (v0.3)

Deterministic multi-agent signals:

joint timing · resource transfers · complementary roles · shared infrastructure use · organization-level actions

## Representation

```text
coordination_signal_id
signal_type
participants[]
evidence_refs[]
possible_interpretations[]   # e.g. cooperation, trade, coercion, coincidence
confounds[]
claim_label: INFERRED
```

Do **not** auto-label as “cooperation” when adversarial/transactional explanations remain plausible.
