# v0.2 Frontier — Migration

## Goal

Enable Frontier on a durable v0.1 world **without rewriting history**.

```text
v0.1 world (ledger + state + runtime manifest)
  → deploy product 0.2.0 modules (frontier_director enabled)
  → preserve world_id, ledger, digests, world_rules for past events
  → append Frontier-originated events prospectively only
```

## Rules

1. Pre-v0.2 history MUST replay under original rules/version pins (ADR-005 for Chamber fixtures).
2. Do **not** retroactively invent Frontier metadata for historical events unless marked as **derived analysis** (research partition, not ledger rewrite).
3. `world_rules_version` may remain `world/v1` if only research modules are added; if world observation rules change, bump rules/version and require explicit migration.
4. Runtime manifest MUST add/pin: `frontier_director_version`, `situation_genome` schema pin, `novelty_axes` pin, `mutation_catalog` pin, `noise_model` pin when Frontier is enabled.
5. Feature flag `NOEMA_FEATURE_FRONTIER_DIRECTOR=true` enables the module; default remains false for pure v0.1 deploys ([ENVIRONMENT.md](../../ENVIRONMENT.md)).

## Fail-closed

If Frontier config is incomplete (missing director_version constants, axes, or seed), requests yield `NOT_COMPUTABLE` and no plan execution.
