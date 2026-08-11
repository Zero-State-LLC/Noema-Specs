# Behavioral Regression

Captured tests answer:

- Does this version reproduce the behavior?
- Did the behavior disappear?
- Did it change form?
- Did a previously absent behavior appear?

## Outcomes

| Outcome | Simple language |
|---|---|
| PASS | Behavior reproduced. |
| PARTIAL | Behavior reproduced only partly. |
| FAIL | Behavior did not reproduce in this test. |
| NOT_COMPARABLE | Conditions differ too much to compare. |
| NOT_COMPUTABLE | NOEMA cannot determine this from available evidence. |

## Non-claims

A regression **FAIL** means only: this behavior did not satisfy this captured test under this boundary.

It MUST NOT become a global model ranking or scalar score. Schema field `not_a_global_ranking` is required `true`.
