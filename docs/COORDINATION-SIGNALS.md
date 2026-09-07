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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend analysis by linking joint timing, transfers, complementary work, or shared infrastructure to the exact participants and evidence intervals. Compare cooperation with trade, coercion, and coincidence as competing explanations rather than inferring shared intent from synchrony.

### Compatibility and promotion

Signals remain INFERRED research records, not world-truth cooperation labels or rewards. Analysis requires eligible permissioned evidence; independent Controller decision contexts cannot share research-derived strategy hints during a Gate B run. Adding a signal kind needs the owning schema/version review.

### Verification before adoption

Use a cooperative trace and a superficially similar adversarial or coincidental trace. Retain confounds and alternative interpretations in both exports and summaries; missing participant evidence must remain incomplete. Verify no signal projection writes the ledger or leaks private coordination into WATCH/PLAY.
