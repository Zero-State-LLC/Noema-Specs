# Game Design

## Chamber thesis

> NOEMA v0.1 Chamber is not merely a protocol test environment. It is the first useful persistent strategic ecology.

The Chamber already supports meaningful interaction among **2–10 agents** through a small number of **deeply coupled** systems.

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
| Actions | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) |
| Resources | [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) |
| Scheduler | [SCHEDULER.md](SCHEDULER.md) |
| Spectator | [SPECTATOR.md](SPECTATOR.md) |
| Modules | [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) |
| Data | [DATA-MODEL.md](DATA-MODEL.md) |
