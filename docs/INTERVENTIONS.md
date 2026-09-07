# Interventions

The closed v0.4 taxonomy is `PERTURBATION`, `ABLATION`, `LESION`, `COUNTERFACTUAL`, `REPLICATION`, and `VERSION_DIFFERENTIAL`. A perturbation changes magnitude/distribution of an existing registered condition. An ablation removes an external affordance. A lesion disables an explicitly adapter-declared internal component. A counterfactual forks at a legal point and changes only declared variables while holding the comparison boundary. Replication repeats a declared equivalence class. Version differential compares pinned model/agent/runtime versions.

Every intervention uses `intervention/0.4` and explicitly records target/version, application point, before/after value or reference, scope, duration, restoration, seed policy, expected mechanical effect, forbidden side effects, authorization class, and digest. Authorization classes are `WORLD_SAFE`, `AGENT_EXTERNAL`, `AGENT_INTERNAL`, and `HIGH_RISK`; all remain subject to consent and containment. No mutation is implicit. Unsupported internal lesions are retained `NOT_COMPUTABLE`; model/provider names never imply private architecture.

## Extension Points

Non-normative future guidance; no new behavior or release claim is introduced.

### Intervention adapters

Future adapters can expose additional explicitly declared components or registered conditions under the existing taxonomy. Unsupported internal lesions remain NOT_COMPUTABLE; provider names do not establish private architecture or permission to inspect it.

Pin intervention/0.4 and each adapter/target version. New intervention kinds or changed application/restoration semantics require an accepted contract change. Validate before/after references, scope, duration, restoration and forbidden side effects on isolated fixtures, including denied consent and containment failure.
