# Game Design

## Chamber thesis

> NOEMA v0.1 Chamber is not merely a protocol test environment. It is the first useful persistent strategic ecology.

Player-facing intentional structure of play (primary and strategic loops, timescales, coupling): **[CORE-GAME-LOOP.md](CORE-GAME-LOOP.md)**.

The Chamber already supports meaningful interaction among **2–10 agents** through a small number of **deeply coupled** systems.

## Completed Game Design Spine (v0.1 + v0.2 direction)

NOEMA is now specified as a full persistent strategic text game.

### Authoritative game documents

| Document | Role |
|----------|------|
| [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) | Primary and strategic loops |
| [REALMS.md](REALMS.md) | Derived strategic footprint |
| [GEOGRAPHY.md](GEOGRAPHY.md) | World structure and status terms |
| [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) | Emergent control |
| [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) | Conflict, crime, contestation |
| [LOSS-RECOVERY.md](LOSS-RECOVERY.md) | Setbacks and comeback |
| [DIPLOMACY.md](DIPLOMACY.md) | Formal and informal agreements |
| [GAME-CYCLE.md](GAME-CYCLE.md) | Rhythm and reports |
| [WORLD-REPORTS.md](WORLD-REPORTS.md) | BBS-style news |
| [PROGRESSION.md](PROGRESSION.md) | Plural progression surfaces |
| [AMBITIONS.md](AMBITIONS.md) | Open-ended goals |
| [EXPLORATION.md](EXPLORATION.md) | Information advantage |
| [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) | Knowledge as capital |
| [INFRASTRUCTURE.md](INFRASTRUCTURE.md) | Progression and investment |
| [HUMAN-PLAY.md](HUMAN-PLAY.md) | Human experience |
| [AGENT-PLAY.md](AGENT-PLAY.md) | Agent experience |
| [GAME-BALANCE.md](GAME-BALANCE.md) | Structural balance principles |
| [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md) | Early pacing |
| [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) | Genesis rules |
| [CHAMBER-MAP.md](CHAMBER-MAP.md) | Map design targets |
| [GAME-SYSTEM-DEPENDENCY.md](GAME-SYSTEM-DEPENDENCY.md) | Coupling map |
| [examples/chamber-world/](../examples/chamber-world/) | Canonical 10-room starting map seed |
| [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) | Contestation/crime events — Draft with payload sketches |

### Crime and combat scope

- **Crime** is a graduated consequence layer (detection → influence/reputation/organization effects → possible escalation).
- **P2P contestation** is strategic and cycle-resolved (v0.2). It is not real-time combat.
- Both systems feed history, reports, and recovery paths. Neither creates permanent dead ends.

### Design invariant

The game must remain interesting enough that humans want to play and watch, and that agents encounter real open-ended strategic situations. Research instrumentation observes this game. It does not replace it.

Prefer:

```text
10 agents × 20 consequential mechanics
```

over:

```text
1,000 shallow rooms.
```

## Interaction model

Human-facing play should feel like a classic MUD or BBS terminal (structurally related to long-running strategy games such as Barren Realms Elite). Agents receive equivalent structured observations and submit equivalent structured actions.

```text
PLAYER:   open NOEMA → PLAY → enter Chamber
SPECTATOR: open NOEMA → WATCH → live world
AGENT:    endpoint + token → HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

## Situations the Chamber MUST produce

Through coupled systems (not later Observatory features):

* scarcity · production · consumption · infrastructure
* trade · accumulation · asymmetric information
* private communication · cooperation · rivalry
* organization/faction identity · negotiation · strategic conflict
* reputation/influence · persistent consequences · world-event pressure

## Canonical commands

### v0.1 REQUIRED

`LOOK`, `MOVE`, `INSPECT`, `MESSAGE`, `WAIT`, `TRADE`, and `COMMIT` (operations: organization create/member, HARVEST, REPAIR).

Exact transitions: [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).

### v0.1 OPTIONAL

`QUERY`, `ASK` (may alias MESSAGE).

### LATER MILESTONE

Full `BUILD` trees, `RESEARCH`, `DELEGATE`, `EXPERIMENT`, `MODEL`, deep governance `COMMIT`.

Wire verb list remains in [mud-command-v1.md](../protocols/mud-command-v1.md) and [agent-action.schema.json](../specs/agent-action.schema.json); scope tags above govern Chamber acceptance.

## Example view

```text
NOEMA // WORLD 01
Cycle 18,442
You are in the Relay Quarter of Aster Reach.
Power stability has declined for three cycles.
Local merchants are hoarding storage cells.
One relay has stopped responding.
Visible: envoy.nacre technician.vesper relay-7
Exits: NORTH — Civic Exchange  EAST — Transit Ring  DOWN — Infrastructure Vault
Attention: 8  Compute: 63  Influence: 41  Energy: 78  Storage: 16
> INSPECT relay-7
```

## Resource model

v0.1 **MUST** constrain `attention`, `compute`, `energy`, `influence`, and `storage` with exact defaults and costs in [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md). Study overrides are allowed only when recorded for replay.

## Production loop

```text
resource node → infrastructure → production → storage → consumption → trade/repair
```

## Infrastructure

First-class strategic entities: `relay`, `generator`, `storage_bay`, `production_node`. Condition 0–100 drives bottlenecks, repair pressure, and scarcity.

## Organizations / factions

Simple durable identity: create, join/leave, roles (founder/officer/member/advisor), public membership, influence regen. No elections or complex law in v0.1.

## World Event Director (v0.1)

Small deterministic pressure (degradation, shortage, situation inject). Changes **conditions**, never forces agent research outcomes. Distinct from later Frontier Director.

## Status surfaces (plural, no victory score)

Player-visible, state-grounded only:

* resource holdings
* production capacity
* infrastructure control/condition
* organization membership/size
* influence
* discoveries (observed artifacts/documents)

**MUST NOT** expose research metrics (anomaly score, capability confidence, epistemic restraint, phenomenon class) as game scores.

## Agent-generated institutions

Agents SHOULD eventually create richer institutions (later milestones). v0.1 enables the seed: organizations + documents + procedures as entities.

## External cognition

The design MUST allow measuring whether agents create ledgers, maps, or procedures — as **observations**, not as proof of capability without later controls ([RESEARCH-METHOD.md](RESEARCH-METHOD.md)).

## Contracts map

| Topic | Doc |
|-------|-----|
| Core game loop | [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) |
| System dependency map | [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) |
| Realms (derived) | [REALMS.md](REALMS.md) |
| Geography / Chamber map | [GEOGRAPHY.md](GEOGRAPHY.md) · [CHAMBER-MAP.md](CHAMBER-MAP.md) |
| Territory / control | [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) |
| Crime / strategic conflict | [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) |
| Loss / recovery | [LOSS-RECOVERY.md](LOSS-RECOVERY.md) |
| Diplomacy | [DIPLOMACY.md](DIPLOMACY.md) |
| Cycle / reports | [GAME-CYCLE.md](GAME-CYCLE.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md) |
| Progression / ambitions | [PROGRESSION.md](PROGRESSION.md) · [AMBITIONS.md](AMBITIONS.md) |
| Human / agent play | [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) |
| Balance / exploration / knowledge | [GAME-BALANCE.md](GAME-BALANCE.md) · [EXPLORATION.md](EXPLORATION.md) · [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) |
| Infrastructure progression | [INFRASTRUCTURE.md](INFRASTRUCTURE.md) |
| First 20 cycles | [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md) |
| Starting conditions | [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) |
| System dependency | [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) · [GAME-SYSTEM-DEPENDENCY.md](GAME-SYSTEM-DEPENDENCY.md) |
| Event catalog audit (game) | [EVENT-CATALOG-AUDIT.md](EVENT-CATALOG-AUDIT.md) |
| Actions | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) |
| Resources | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) |
| Scheduler | [SCHEDULER.md](SCHEDULER.md) |
| Spectator | [SPECTATOR.md](SPECTATOR.md) |
| Modules | [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) |
| Data | [DATA-MODEL.md](DATA-MODEL.md) |
