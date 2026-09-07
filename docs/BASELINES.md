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

## Extension Points

Non-normative baseline-construction and inspection seams.

- Extend construction algorithms or cohort selectors within the existing baseline schema, recording inclusion/exclusion rules, context constraints, population window and minimum evidence. A selector may propose a candidate baseline; it cannot silently replace a claim-bearing run's pinned digest.
- Preserve feature_version compatibility and the freeze rule: newer data or different rules produce a new baseline_id. Keep control, peer and self-history populations distinguishable instead of pooling incompatible regimes for a convenient result.
- Compatibility/promotion: require schema-valid provenance and a reproducible digest before attaching a candidate to a new analysis; leave prior claims attached to their original baseline. Research access, not Controller enrollment or a UI filter, governs cohort visibility.
- Verification proposal: reproduce a digest from frozen inputs, alter one inclusion rule and expect a new identity, reject insufficient evidence, and test incompatible feature versions. A comparison view should expose pinned versus candidate baseline and excluded-population reasons accessibly; translate captions, not baseline_type tokens or identifiers.
