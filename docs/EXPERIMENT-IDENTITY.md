# Experiment Identity

Experiment identity is immutable and content-addressed. `input_digest` is SHA-256 of canonical JSON of the claim-bearing identity payload, excluding digest fields. It includes `experiment_id`, `experiment_version`, `experiment_design_version`, `source_intent_id`, source candidate/trajectory IDs, world ID/version/rules/catalog versions, agent ID/version, fork point, intervention/control-set digests, feature/metric versions, seed policy, equivalence boundary, consent basis, research-policy version, and authorization. The run boundary also pins source snapshot and ledger head.

Changing any claim-bearing input, variable definition, intervention semantic, comparison or analysis rule creates a new experiment identity. A correction appends a successor linked by `supersedes_experiment_id`; it never rewrites prior identity. Run IDs are deterministic derivatives of experiment identity, plan-node ID, replicate ordinal, and seed identity.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend provenance comparison with an immutable successor view showing the changed claim-bearing inputs, source snapshot and ledger head, and supersedes_experiment_id. Explain identity changes separately from cosmetic display changes or repeated execution of the same plan.

### Compatibility and promotion

Preserve canonical JSON SHA-256 identity, digest-field exclusion, deterministic run derivation, and historical receipts. Research identity does not authorize an Agent Player to run Lab workflows, and translations must not modify serialized IDs. New identity semantics require the owning schema/contract version review.

### Verification before adoption

Test repeated canonical input, changed intervention/control digest, changed consent or boundary, and changed replicate ordinal/seed identity. Confirm corrections append successors rather than rewrite predecessors. Validate that source-head mismatches are surfaced and that display ordering or localized labels do not silently change claim-bearing payloads.
