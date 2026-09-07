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

## Extension Points

Non-normative captured-test and result-rendering seams.

- Extend a behavior-specific oracle with its boundary, conditions, expected behavior and evidence references. Distinguish disappearance, changed form and newly observed behavior without converting a local result into a model ranking.
- Preserve all five outcomes: unavailable evidence is NOT_COMPUTABLE, incompatible conditions are NOT_COMPARABLE, and partial reproduction is not silently PASS or FAIL. Keep not_a_global_ranking true in serialized and displayed results.
- Compatibility/promotion: pin fixture, oracle and relevant baseline versions for comparisons; new oracle semantics create a new comparison boundary rather than rewriting old verdicts. Permissioned STUDY interpretation cannot change Player status or world state.
- Verification proposal: exercise a reproduced behavior, partial case, absent behavior, incompatible context and missing evidence; assert each yields the appropriate outcome and attached non-claim. Localize explanations while retaining exact outcome tokens, and expose uncertainty/boundary alongside keyboard-readable result rows rather than hiding them in color or tooltips.
