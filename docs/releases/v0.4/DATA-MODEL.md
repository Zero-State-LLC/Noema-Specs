# v0.4 Lab: Data Model Delta

| Record | Machine authority |
|---|---|
| immutable design | `experiment/0.4` |
| intervention | `intervention/0.4` |
| execution DAG | `experiment-plan/0.4` |
| isolated fork | `experiment-fork/0.4` |
| immutable run | `experiment-run/0.4` |
| result | `lab-result/0.4` |
| audit chain | `lab-audit-record/0.4` |
| variable/catalog pins | v0.4 registries and catalogs |

All are derived research records linked to v0.1–v0.3 evidence. They do not alter historical canonical data. Identity pins candidates, trajectories, world and agent versions, forks, interventions, controls, metrics, seed policy, equivalence boundary, consent, policy, and digest.

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** The delta table can gain provenance cross-references and examples linking experiment designs, DAGs, forks, runs, results, and audit records.
- **Unchanged invariants:** All Lab records remain derived research artifacts; identity retains consent, policy, seed, equivalence, intervention, and version pins without mutating canonical history.
- **Compatibility, promotion, and verification:** Additional record fields or types belong in versioned schema changes with migration rules. Verify schema validity and end-to-end lineage, including rejection of missing consent or digest linkage.
