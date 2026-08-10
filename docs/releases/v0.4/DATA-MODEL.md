# v0.4 Lab — Data Model Delta

## Core objects

| Object | Schema |
|--------|--------|
| Experiment | `specs/experiment.schema.json` |
| Intervention | `specs/intervention.schema.json` |
| Experiment plan | `specs/experiment-plan.schema.json` |
| Experiment run | `specs/experiment-run.schema.json` |
| Experiment fork | `specs/experiment-fork.schema.json` |
| Lab result | `specs/lab-result.schema.json` |
| Lab audit | `specs/lab-audit-record.schema.json` |

## Catalogs

- `specs/perturbation-catalog.v04.json`
- `specs/ablation-catalog.v04.json`
- `specs/experiment-variable-registry.v04.json`

## Identity digests

Claim-bearing experiments MUST pin `input_digest` over identity fields. Changing a claim-bearing variable creates a new experiment identity.
