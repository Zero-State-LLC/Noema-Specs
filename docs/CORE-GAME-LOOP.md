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
