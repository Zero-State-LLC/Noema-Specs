# Baselines (v0.3)

Schema: [`specs/baseline.schema.json`](../specs/baseline.schema.json).

## Types

| baseline_type | Population |
|---------------|------------|
| `self_history` | same agent earlier windows |
| `agent_version` | same agent_version cohort |
| `peer` | other agents same regime |
| `scenario` | same Situation Genome / scenario class |
| `control` | declared control trajectories |
| `world_regime` | same world pressure band |

## Required fields

```text
baseline_id, baseline_type, population_window,
inclusion_rules, exclusion_rules, context_constraints,
minimum_evidence, feature_version, construction_algorithm,
feature_summary, digest
```

## Freeze rule

A claim-bearing analysis run MUST pin baseline digests. Rebuilding with newer data creates a **new** baseline_id. Silent rebuild is forbidden.
