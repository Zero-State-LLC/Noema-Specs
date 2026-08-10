# Information-Gain Estimates (v0.2)

Planning components used by Frontier ranking. Labels: estimates are **`INFERRED`**. Actual information gained is evaluated later (Observatory/Lab).

Fixed-point: millipoints 0–1000 unless noted. Config: [`specs/information-gain.v02.json`](../specs/information-gain.v02.json).

## Components

| Component | Inputs | Bounds | Missing data |
|-----------|--------|--------|--------------|
| `uncertainty` | capability confidence width | 0–1000 | NOT_COMPUTABLE |
| `discrimination` | #hypotheses × weights | 0–1000 | NOT_COMPUTABLE |
| `coverage_gain` | uncovered cells hit | 0–1000 | 0 if empty map declared |
| `novelty` | weighted novelty distance | 0–1000 capped | NOT_COMPUTABLE |
| `failure_relevance` | distance to unresolved failures | 0–1000 | 0 if no failures |
| `control_value` | control_role priority | 0–1000 | 0 if none |
| `cost` | normalized resource vector | 0–1000 | NOT_COMPUTABLE |
| `risk` | risk_class mapping | 0–1000 | fail closed |
| `repetition` | 0 novel / 1 admitted control | 0 or 1 | — |

## Rules

* Do not invent zeros for unknown uncertainty—use `NOT_COMPUTABLE` and block ranking component or whole plan per FRONTIER-DIRECTOR failure handling.
* Expected information gain is **not** a scientific claim of bits learned.
* No component is a consciousness or intelligence score.
