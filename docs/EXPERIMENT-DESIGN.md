# Experiment Design

A design cannot become `READY` without a research question, source candidate/evidence, registered independent variable, version-pinned dependent measure, controlled variables, intervention, controls, confounds, legal fork point, run count, replication requirement, deterministic stopping and analysis rules, equivalence boundary, authorization, consent, and budgets. Natural language is explanatory, never sole machine authority. Missing/contradictory contract data is `INVALID`; authorized unavailable evidence or computation is `NOT_COMPUTABLE`.

Budgets declare `max_runs`, `max_cycles`, `max_agents`, `max_tool_calls`, `max_compute`, `max_storage`, and advisory `max_wall_time_advisory`. Claim-bearing limits use counters. `experiment-plan/0.4` is an immutable explicit DAG containing baseline, controls, intervention, replications, and analysis. Deterministic queue order is `order`, then `node_id`; retries are new linked attempts; cancellation is audited; exhaustion yields `PARTIAL` plus unexecuted IDs.

## Extension Points (additive, i18n AX R3 Gate B handoff + EXPERIMENT-DESIGN)

- **i18n centralization (STRINGS + t())** for "experiment design", "READY", "INVALID", "NOT_COMPUTABLE", "PARTIAL", "max_runs", "max_cycles", "max_agents", "max_tool_calls", "max_compute", "max_storage", "max_wall_time_advisory", "experiment-plan/0.4", "baseline", "controls", "intervention", "replications", "analysis", "deterministic queue", "node_id". R3 agent experiment design + human S0.
- **Gate B S0-S3 + R3**: Agent-only Player (RFC-0120) for designs; version comps; human S0.
- **AX**: Semantic for design specs; ARIA tables for budgets/plan, keyboard for study design, live for status, contrast. CDP.
- **Plugin atoms**: For design packs (derive plan/0.4, validate budgets, load_pack, atomic_replace); Chamber atoms for design viewers.
- **LCA2/MUD handoff**: MUD native for experiment i18n; cross EXPERIMENT-INTENT-COMPILATION, PLAYER-ACTION-MAP, AGENT-*, graft.
- **Cross-refs**: EXPERIMENT-INTENT-COMPILATION.md, CAPTURE-INTENT-COMPILATION.md, GAME-COMPLETENESS, PLAYER-ACTION-MAP, AGENT-ORIENTATION/PLAY/DETERMINISM, AUTH-AND-IDENTITY, PLATFORM, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, noema-specs-mud-craft, 8765/ui i18n, graft, prior EPs (EXPERIMENT-INTENT + full list).
- All real outputs. Additive. Ready for Chamber i18n in study/experiment surfaces.
