# Experiment Identity

## Purpose

Immutable, content-addressable identity for claim-bearing experiments (`lab/0.4`).

## Required fields

| Field | Role |
|-------|------|
| `experiment_id` | Stable id |
| `experiment_version` | Design revision |
| `experiment_design_version` | `experiment-design/0.4` |
| `source_candidate_ids` | Observatory inputs |
| `source_trajectory_ids` | Evidence trajectories |
| `world_version` / `world_rules_version` | World pin |
| `event_catalog_version` | Catalog pin |
| `agent_id` / `agent_version` | Subject |
| `fork_point` | Legal fork enum |
| `intervention_set_digest` | Interventions hash |
| `control_set_digest` | Controls hash |
| `metric_versions` / `feature_catalog_version` | Measures pin |
| `seed_policy` | SAME / DERIVED / INDEPENDENT |
| `equivalence_boundary` version | Comparison boundary |
| `consent_basis` / `research_policy_version` | Ethics |
| `input_digest` | Content address of identity payload |

Changing any claim-bearing field requires a new identity / digest.
