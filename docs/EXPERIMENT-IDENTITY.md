# Experiment Identity

Experiment identity is immutable and content-addressed. `input_digest` is SHA-256 of canonical JSON of the claim-bearing identity payload, excluding digest fields. It includes `experiment_id`, `experiment_version`, `experiment_design_version`, source candidate/trajectory IDs, world ID/version/rules/catalog versions, agent ID/version, fork point, intervention/control-set digests, feature/metric versions, seed policy, equivalence boundary, consent basis, research-policy version, and authorization. The run boundary also pins source snapshot and ledger head.

Changing any claim-bearing input, variable definition, intervention semantic, comparison or analysis rule creates a new experiment identity. A correction appends a successor linked by `supersedes_experiment_id`; it never rewrites prior identity. Run IDs are deterministic derivatives of experiment identity, plan-node ID, replicate ordinal, and seed identity.
