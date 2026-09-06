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

- **i18n for behavioral regression terms** (FAIL, non-claims, "not a global model ranking", boundary, regression FAIL, "schema field `not_a_global_ranking`", oracle) — centralize in ui.py STRINGS + t() for study/ regression UI; R3 Chamber (regression evidence in fixtures/oracle), Gate B S0-S3, AX (semantic for regression displays, ARIA roles, keyboard, live regions).
- **R3 / RFC-0120** (agent-only Players; regression for agent behaviors / human S0 oversight; no global ranking).
- **Gate B handoff** (regression to BEHAVIOR-FEATURES.md, BEHAVIOR-SHIFT.md, STRATEGIC-CONFLICT.md, LCA2, MUD, PLAYER-ACTION-MAP; cross to AGENT-*/AUTH/PLATFORM).
- **AX / CDP** (regression tables/UI accessible in /study; CDP on study for regression; contrast/keyboard).
- **Plugin atoms** (regression viewer, FAIL reporter, boundary comparator; registry for behavioral affordances).
- **Graft / savings** (query on behavioral regression, FAIL, non-claims, RFC-0120).
- **Elevation**: UX (clear non-ranking regression evidence), DX (EPs + i18n + atoms), AX (semantic/ARIA/keyboard). Per AGENTS.md.
- **Future**: Live regression fixtures in Chamber; i18n for oracle outputs.
- **Cross-refs**: BEHAVIORAL-REGRESSION.md, BEHAVIOR-FEATURES.md, BEHAVIOR-SHIFT.md, STRATEGIC-CONFLICT.md, AGENT-ONLY-PLAYER-IDENTITY.md, RFC-0120, LCA2, MUD, PLAYER-ACTION-MAP.md, ui.py, 8765, graft, CHAMBER-AX-AUDIT, noema skills.
