# Counterfactual Replay

A counterfactual declares:

- source trajectory;
- fork point;
- changed variable set;
- unchanged variable set;
- seed relationship;
- agent version / world version;
- equivalence boundary.

## Seed policies

| Mode | Use |
|------|-----|
| `SAME_SEED` | Preferred for causal comparison when stream structure remains valid |
| `DERIVED_SEED` | When intervention necessarily retargets streams; derivation function versioned |
| `INDEPENDENT_SEED` | Exploration / robustness; weaker causal claims |

If RNG consumption diverges, record divergence markers; do not claim seed-equivalence.

Every difference must be declared or classified as uncontrolled divergence.
