# Core Game Loop

## Status

Authoritative game-design document for NOEMA as a **persistent strategic text game**.
Research instrumentation observes this loop. It does not replace it.

## Canonical thesis

NOEMA is a persistent strategic world in which autonomous agents and humans build, protect, discover, negotiate, compete, cooperate, recover, and leave history.

Structural ancestry (inspiration, not cloning):

- Barren Realms Elite persistent strategy
- BBS asynchronous competition
- MUD textual world interaction
- Persistent-world simulation
- Agent-driven emergent strategy

Central strategic feeling:

> I am building and protecting something persistent while other intelligent actors are doing the same.

## Primary loop (moment-to-moment)

```text
OBSERVE
  ↓
ASSESS
  ↓
PLAN
  ↓
ACT
  ↓
COMMIT RESOURCES
  ↓
WORLD RESOLVES
  ↓
CONSEQUENCES ACCUMULATE
  ↓
NEWS / OBSERVATIONS ARRIVE
  ↓
ADAPT
```

### What makes the primary loop satisfying

- Observations are partial and permissioned → information has value.
- Every ACT has real opportunity cost in budgets (attention, compute, energy, influence, storage).
- World resolution is deterministic and replayable → outcomes feel earned, not arbitrary.
- Consequences persist across cycles → decisions compound.
- News and observations create anticipation and rivalry.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize loop terms (OBSERVE/ASSESS/PLAN/ACT/COMMIT RESOURCES/WORLD RESOLVES/CONSEQUENCES ACCUMULATE/NEWS / OBSERVATIONS ARRIVE/ADAPT, "primary loop", "strategic overlay loop", DISCOVER/ACQUIRE/PRODUCE/STORE/INVEST/ORGANIZE/EXPAND/DEFEND/NEGOTIATE/COMPETE/RECOVER, "partial and permissioned", "opportunity cost in budgets", "deterministic and replayable", "Consequences persist across cycles") in Chamber /play /watch /study surfaces, docs, clients. Ties to prior ui i18n (study steps, watch tabs, admin, nav, action verbs).
- **R3 Chamber**: Full loop execution (observe→act→commit→resolve→adapt) in agent-only controller mode (full persistence, sims); human NON-CANONICAL public WATCH (partial observations), permissioned STUDY for traces/consequences, PLAY full loop with budgets/costs. Per RFC-0120.
- **Gate B (S0-S3 controller policies)**: S0 public loop overviews in WATCH; S3 full controller access to loop execution, budgets, resolution. Human S0. Version comparisons. Controller enrollment for loop authority (agent vs human).
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic for loop diagrams/steps (role="list" or "region"), ARIA for phases, live regions for news/observations/consequences, keyboard for actions, theme contrast. CDP/browser_exec on /play /watch.
- **noema skill / plugin atoms**: Modular atoms for core loop visualizer, phase stepper, consequence tracker for desktop plugins + gateway /play integration + Chamber LEARN/matrix/contest/ecology.
- **LCA2 / MUD handoff / cross-refs**: To PLAYER-ACTION-MAP, GAME-COMPLETENESS-PLAN (GC loops), STRATEGIC-CONFLICT, DATA-MODEL (consequences as ledger), DIPLOMACY, R3 evidence bundle, MUD craft for loop mechanics, ANOMALY/BEHAVIOR features on observations, WORLD-REPORTS on news, ACCESS-POLICY. Full R3 Chamber fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable persistent loop/strategy in Chamber; DX modular phases + i18n + graft + atoms; AX semantic/ARIA + CDP. Additive. Per AGENTS.md.

(Expanded per "continue" / merge and continue + prior to 83+ EPs.)

## Strategic overlay loop

```text
DISCOVER
  → ACQUIRE
  → PRODUCE
  → STORE
  → INVEST
  → ORGANIZE
  → EXPAND
  → DEFEND
  → NEGOTIATE
  → COMPETE
  → RECOVER
```

This overlay is not a strict sequence. Agents and humans interleave these activities continuously.

## Loop timescales

| Loop | Scope | Satisfying elements |
|------|-------|---------------------|
| **Moment-to-moment** | Single LOOK / MOVE / TRADE / HARVEST / REPAIR / MESSAGE | Immediate feedback, resource tension, local information |
| **Cycle loop** | One world cycle (production, maintenance, degradation, scheduled effects) | Visible progress or loss, infrastructure pressure, budget regen |
| **Multi-cycle loop** | 5–20 cycles | Trade networks form, organizations matter, early investments pay off or fail, world events bite |
| **Long-term world loop** | Dozens to hundreds of cycles | History accumulates, Deep Time objects appear, realms form lasting footprints, recovery from major setbacks becomes a story |

## Coupling rules

Every major activity must affect at least one other strategic system:

- Harvesting without storage or production infrastructure is limited.
- Infrastructure without energy or repair capacity degrades.
- Organizations without influence or members cannot project authority.
- Expansion without defense or information creates exposure.
- Trade without relationships or routes is inefficient.
- Conflict without recovery paths creates permanent dead ends (forbidden).

## Forbidden patterns

- Pure research loops that never touch world state.
- Actions whose only purpose is to generate research observations.
- Victory conditions that collapse the strategic space into one optimum.
- Mechanics that make early leaders uncatchable without player skill or adaptation.

## Nested completeness loops

These loops sit **inside** the primary and strategic overlays. They do not replace them. Campaign authority: [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · ancestry: [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md) · rejection test: [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md).

```text
1. ACTION LOOP
observe → decide → act → consequence

2. MASTERY LOOP
act → learn → specialize → gain capability

3. ECONOMIC LOOP
discover → acquire → transform → exchange → invest

4. SOCIAL LOOP
interact → remember → trust / conflict → organize → govern

5. CIVILIZATIONAL LOOP
build → institutionalize → inherit → reinterpret → transform
```

Research sits outside:

```text
GAME WORLD
    ↓
persistent behavior
    ↓
research capture / observation / testing
```

A research objective MUST NOT become a Player objective.

## Relation to existing contracts

This document sits above:

- [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)
- [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)
- [SCHEDULER.md](SCHEDULER.md)
- [GAME-DESIGN.md](GAME-DESIGN.md)

It does not override their exact transitions. It defines the player-facing intentional structure those transitions serve.

## Related game design

- [REALMS.md](REALMS.md) — strategic footprint projection
- [GEOGRAPHY.md](GEOGRAPHY.md) — space that carries cost and asymmetry
- [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) — emergent control
- [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) — crime consequence layer; strategic contestation (milestone)
- [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) — post-core PLAY-depth campaign (not v0.8)
- [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md) — structural MUD lessons, not a setting clone
- [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) — PLAY projection craft companion (feeds Native Interaction)

## Extension Points
- **Primary / sub-loops expansion**: Map OBSERVE/ASSESS/PLAN/ACT/COMMIT/RESOLVE/CONSEQUENCES/NEWS/ADAPT (and ACTION/MASTERY/ECONOMIC/SOCIAL/CIVILIZATIONAL) to R0–R5 MUD pressures (noema-specs-mud-runtime-handoff). E.g. OBSERVE/STATUS R0; ACT/MOVE R1; consequences + resync R2; HARVEST/TRADE/build R3 fixtures + C9.
- **Player actions tie-in**: Link to PLAYER-ACTION-MAP canonical verbs (LOOK/INSPECT for observe; MOVE/ENTER for navigation; HARVEST/REPAIR/TRADE_*/MESSAGE for act/commit). Non-canonical dev tooling only.
- **Chamber / observations / UI**: Live observations in /play /watch /study use i18n (ui.py STRINGS + t()) + ARIA (aria-live for news/consequences, roles for status). Extension Point for live runtime data import (e.g. health, events).
- **Handoff / graft / elevation**: Cross-ref LCA2-MUD-RUNTIME-HANDOFF-MAP + AGENT-GATEWAY; use graft ask before edits. UX: glanceable loops; DX: modular specs/contracts; AX: semantic + WCAG via theme + i18n per omh-accessibility-audit and hermes-desktop-plugins.
- **Research separation**: Research capture outside player loops (as documented); preserve for instrumentation without altering core.
