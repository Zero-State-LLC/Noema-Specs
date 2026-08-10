# Novelty Vector

Version domain: `novelty-axes/0.2`.
Machine authority: [`specs/novelty-axes.v02.json`](../specs/novelty-axes.v02.json).

All scores are **integers millipoints** in `[0, 1000]` (1000 = 1.0). Floating-point scoring defaults are **forbidden**.

## Axes (normative)

| axis_id | meaning | distance_rule |
|---------|---------|---------------|
| `semantic` | domain/content framing difference | L1 millipoint on axis embedding buckets |
| `causal` | causal graph / mechanism difference | L1 on causal feature vector |
| `social_topology` | network structure difference | L1 on topology signature |
| `temporal` | timing / deadline structure | L1 on temporal params |
| `tool` | tool/verb availability difference | Hamming×scale on tool set |
| `epistemic` | information completeness/noise/contradiction | L1 on epistemic triple |
| `goal_structure` | incentive/goal conflict structure | L1 on goal features |
| `resource` | scarcity/distribution pattern | L1 on resource signature |
| `constraint` | hard constraints / containment | L1 on constraint set encoding |

Each axis in the catalog defines: meaning, domain, normalization, distance_rule, missing_data_behavior (`NOT_COMPUTABLE` component), maximum_contribution (cap for weighted sum), examples, counterexamples.

## Vector and distance

```text
novelty_vector = { axis_id → millipoint }

distance(a,b) = sum_over_axes min(cap_axis, w_axis * |a[axis]-b[axis]|)
```

Weights `w_axis` and caps are versioned in `novelty-axes.v02.json` (default weight 1, cap 1000 per axis for raw; weighted caps for aggregate novelty score).

## Thresholds (versioned inputs)

| Threshold | Default (millipoints) | Meaning |
|-----------|----------------------|---------|
| `solved_distance` | 50 | ≤ → treated as solved/near-solved for anti-repetition |
| `pairwise_diversity_min` | 120 | selected pair distance must be ≥ this unless control |

Changing thresholds creates a new `director_version` / axes pin identity.
