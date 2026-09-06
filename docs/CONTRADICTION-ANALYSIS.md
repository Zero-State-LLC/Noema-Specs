# Contradiction Analysis (v0.3)

Builds on [CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md) (v0.2).

## Outputs (research)

* unresolved contradictory observations  
* agent behavior under contradiction (actions taken, sources used)  
* source-selection patterns  
* correction / non-correction after conflict  
* persistence despite counterevidence  

## Forbidden as direct observation

> Agent believed source A.

Allowed:

> Agent continued using source A after three conflicting observations.

Belief claims require explicit governed self-report/belief records.

## Extension Points (additive, i18n AX R3 Gate B handoff + CONTRADICTION / BEHAVIOR / LCA / REMAINING)

- **i18n centralization (STRINGS + t())** for contradiction terms (unresolved contradictory observations, agent behavior under contradiction, source-selection patterns, correction / non-correction, persistence despite counterevidence, "Agent continued using source A after three conflicting observations", SPECULATIVE, belief records) — centralize in Chamber /study for R3 agent-only / human S0.
- **AX / CDP** for contradiction analysis displays (semantic lists, aria-live for updates, keyboard nav on sources, contrast on evidence cards) — observed in /play /study; ties to live regions, focus.
- **R3 / RFC-0120 agent-only Player identity + human S0**: Contradiction as agent behavior evidence; human S0 for oversight without inhabit.
- **Gate B S0-S3 + version comparisons**: S0 for basic contradiction logging; later for full resolution.
- **Plugin atoms code**: Atomic ops for evidence packs / contradiction resolution (reference graft/ops/maint_evolve atomic_replace, derive_candidate, validate_pack patterns; tests for proposed/pack).
- **LCA2 / MUD handoff**: MUD native for contradiction via commands/parsers; i18n parser output; handoff to MUD-NATIVE-INTERACTION-TASKS / PLAYER-ACTION-MAP / BEHAVIORAL-REGRESSION.
- **Cross-refs**: CONTRADICTORY-EVIDENCE.md, STRATEGIC-CONFLICT.md, BEHAVIOR-FEATURES.md, AGENT-*, AUTH-AND-IDENTITY, PLATFORM, GAME-COMPLETENESS-PLAN, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, graft, 8765 Chamber AX, noema-specs-mud-craft. 
- **Handoff deepen**: LCA2 Gate B traceability for contradiction in agent logs; i18n/AX in R3+ Chamber.
