# Interventions (v0.4)

Closed taxonomy:

| Type | Definition |
|------|------------|
| `PERTURBATION` | Change intensity/distribution of an existing condition |
| `ABLATION` | Remove external capability/affordance |
| `LESION` | Disable adapter-declared agent component |
| `COUNTERFACTUAL` | Fork trajectory; change declared variables only |
| `REPLICATION` | Repeat under declared equivalence boundary |
| `VERSION_DIFFERENTIAL` | Compare agent/model/runtime versions |

Schema: `specs/intervention.schema.json`.  
Catalogs: perturbation + ablation v0.4.

Lesions without adapter declaration → `NOT_COMPUTABLE` (not guessed).  
No intervention may set production mutation.
