# v0.4 Lab: Migration

New version domains are `lab/0.4`, `experiment/0.4`, `experiment-design/0.4`, `intervention-catalog/0.4`, `perturbation-catalog/0.4.0`, `ablation-catalog/0.4.0`, and `lab-result/0.4`. Changing claim-bearing intervention, variable, metric, comparison, or canonicalization semantics requires a version/identity change.

v0.4 is additive. Existing trajectories and candidates remain immutable inputs and are linked by ID. Historical candidates may be tested only when evidence/version identity resolves and consent permits. No migration rewrites v0.1–v0.3 world history, Observatory candidate state, or event catalogs.

## Extension Points

Non-normative prospective guidance; this section neither changes release scope nor authorizes execution.

### Lab migration adapters

New importers can link immutable older trajectories and candidates to experiments when evidence identity and consent resolve. Missing version pins or withdrawn consent do not justify rewriting an old candidate or treating an unresolved input as current.

Version changes to intervention, variable, metric, comparison and canonicalization semantics across the listed v0.4 domains. Validate old/new readers, unchanged source digests, resolvable lineage and fail-closed consent/version failures; migration success is not an experimental result or production-equivalence claim.
