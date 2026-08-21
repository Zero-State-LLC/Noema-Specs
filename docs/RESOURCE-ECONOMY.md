# Resource Economy (v0.1 Chamber)

Machine-readable authority: [`specs/resource-economy.v01.json`](../specs/resource-economy.v01.json).

New resource types require a distinct strategic constraint ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)). Currency, credit, wallets, and external settlement are not Chamber resources.

NOEMA v0.1 **MUST** constrain agent budgets with the five Chamber resources. Values are **non-negative integers**. Floating-point MUST NOT determine canonical balances.

Preserved seed defaults ([examples/v01-seed/world-seed.json](../examples/v01-seed/world-seed.json), [ENVIRONMENT.md](ENVIRONMENT.md)):

| Resource | Default grant | Notes |
|----------|---------------|--------|
| `attention` | 8 | Observation spend |
| `compute` | 64 | Planning / heavy verbs |
| `energy` | 80 | Movement, harvest, repair fuel |
| `influence` | 40 | Org authority, trade leverage |
| `storage` | 16 | Holding capacity for harvested lots |

## Shared rules

| Rule | Value |
|------|--------|
| Domain | agent budget accounts + resource nodes + infrastructure effects |
| Minimum | 0 |
| Maximum (agent holding) | 10_000 per resource unless study override |
| Overflow | clamp at maximum; excess production is lost and MUST emit `BUDGET_CONSUMED` or transfer with explicit loss path only if ledgered |
| Insufficient | action rejected; see failed_action_costs |
| Reservation | reserved on action accept; released on reject; charged once on success |
| Contention | scheduler order determines winner ([SCHEDULER.md](SCHEDULER.md)) |
| Retry / idempotency | same `idempotency_key` MUST NOT double-charge |
| Replay | balances fully determined by seed + ordered events |
| Study overrides | recorded in trajectory; min of study/agent/world ceilings |

## Per-resource contracts

### attention

| Field | Value |
|-------|--------|
| regeneration | +2 at start of each cycle after cycle processes, clamp max(grant, current) to max 8 default grant unless holding > grant (no regen above grant) |
| decay | none |
| transferable | no |
| tradeable | no |
| observable | yes (self full; others as coarse band only if co-located) |
| action_costs | LOOK 1; INSPECT 2; QUERY 1 |
| failed_action_costs | 0 (insufficient attention → `BUDGET_EXCEEDED`, no debit) |

### compute

| Field | Value |
|-------|--------|
| regeneration | +4 / cycle, clamp to grant default 64 |
| decay | none |
| transferable | yes (trade) |
| tradeable | yes |
| observable | self full; others no |
| action_costs | TRADE propose/accept 1; TRADE reject/cancel 0; COMMIT org ops 2; HARVEST 1; REPAIR 2 |
| failed_action_costs | 0 |

### energy

| Field | Value |
|-------|--------|
| regeneration | 0 passive; produced via infrastructure/node loop. Exception: RFC-0117 lockout WAIT rest when energy 0 and storage 0 sets energy to 2. RFC-0119: WAIT may burn 1 cargo for +2 energy (clamp 80) when occupied hold ≥ 1 and lockout rest did not apply |
| decay | none in v0.1 |
| transferable | yes |
| tradeable | yes |
| observable | self full; co-located agents see presence band only |
| action_costs | MOVE 1; HARVEST 2; REPAIR 3; WAIT 0 |
| failed_action_costs | 0 |

### influence

| Field | Value |
|-------|--------|
| regeneration | +1 / cycle if agent is ACTIVE member of ≥1 ACTIVE org, else 0; clamp to 40 default grant |
| decay | none |
| transferable | yes |
| tradeable | yes |
| observable | self full; org mates see member influence |
| action_costs | ORG_CREATE 5; ORG_MEMBER_ADD authorizer 1; TRADE when influence in offered/requested: amount transferred not “cost” |
| failed_action_costs | 0 |

### storage

| Field | Value |
|-------|--------|
| regeneration | 0 passive. Exception: RFC-0117 lockout WAIT rest when energy 0 and storage 0 sets storage to 1. RFC-0119 cargo fuel credits +1 free storage when WAIT burns cargo |
| decay | none |
| transferable | yes |
| tradeable | yes |
| observable | self full |
| action_costs | HARVEST **debits** free storage (fills hold) when free capacity ≥ amount. REPAIR / CONSTRUCT / UPGRADE / REPURPOSE / RESTORE **credit** free storage (consume cargo). RFC-0118. WAIT cargo fuel (RFC-0119) also **credits** free storage when burning cargo for energy. |
| capacity semantics | `storage` is **free capacity** (grant 16 empty, 0 full). Occupied hold = 16 − storage. Harvest fills hold; work empties it. Do not invert live Perihelion numbers. |
| failed_action_costs | 0 |

## Production / consumption loop

```text
resource node (stock)
  → infrastructure (condition × capacity modifiers)
  → cycle production tick
  → storage holdings
  → consumption (action costs, repair)
  → trade / investment
```

### Resource nodes

Canonical entity property markers (from seed):

```json
{ "resource_node": true, "resource": "storage" }
```

State fields (integers):

| Field | Meaning |
|-------|---------|
| `available` | extractable stock |
| `capacity` | max stock (default 24 if omitted) |
| `regen_per_cycle` | base regen (default 1) |

### Infrastructure types (v0.1 closed set)

| Type | Effect |
|------|--------|
| `relay` | if `condition >= 50`, room communication normal; else MESSAGE cost +1 energy equivalent via extra `compute` 0 and attention unaffected — MESSAGE still succeeds but delivery may queue (see SPECTATOR). Power stability on relay affects production modifier. |
| `generator` | multiplies node `regen_per_cycle` in same room by `1 + floor(condition/50)` (0 if condition &lt; 25) |
| `storage_bay` | increases agent effective storage capacity by `floor(capacity * condition / 100)` for agents in room (not transferred) |
| `production_node` | enables HARVEST in room when condition ≥ 25 |

Seed `entity.relay-7` is type `relay` with `function: power-relay`.

### Cycle production formula

At scheduler phase **apply scheduled infrastructure / resource processes** (after agent actions):

```text
for each resource_node in world:
  infra = controlling or same-room generator/production infrastructure
  mod = production_modifier(infra)  # integer 0..3
  if mod == 0: skip regen
  else:
    gain = node.regen_per_cycle * mod
    node.available = min(node.capacity, node.available + gain)
```

`production_modifier(infra)`:

```text
if no production-capable infra in room: 1  # bare node still regens slowly
if any infra.condition < 25: 0
else: 1 + floor(min(infra.condition for production-capable) / 50)
```

Ledger representation: production tick MAY be pure state in snapshot-derived processes **or** emit `ENTITY_UPDATE` per changed node. Strategic fixtures MUST ledger `ENTITY_UPDATE` when stock changes so replay is event-complete.

### Harvest (agent)

Verb path: `COMMIT` with `parameters.operation = "HARVEST"`.

```text
pre: agent in node room; production_node or resource_node accessible; node.available >= amount; agent.storage capacity allows
cost: energy 2, compute 1
effect: node.available -= amount; agent.storage += amount
events: BUDGET_CONSUMED (energy), BUDGET_CONSUMED (compute), ENTITY_UPDATE (node), BUDGET_CONSUMED or RESOURCE_TRANSFER-style holding update via BUDGET_CONSUMED for storage gain is FORBIDDEN
```

Storage gain MUST be ledgered as `RESOURCE_TRANSFER` with `from_id = node.entity_id` and `to_id = agent_id` (node is a holder).

### Repair (agent)

`COMMIT` / `parameters.operation = "REPAIR"`:

```text
pre: co-located with INFRASTRUCTURE; agent energy >= 3; storage >= 1
cost: energy 3, compute 2, storage 1
effect: infrastructure.condition = min(100, condition + 15)
events: BUDGET_CONSUMED × resources, ENTITY_UPDATE on infrastructure
```

### Degradation (World Event Director)

Deterministic schedule from world seed stream `world_event_director.v1`:

```text
if cycle > 0 and cycle % 5 == 0:
  for each infrastructure with condition > 0:
    condition = max(0, condition - 5)
    ledger ENTITY_UPDATE
```

## Trade

Two-phase offer/accept ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)):

1. `TRADE_PROPOSED` reserves offered amounts on proposer.
2. `TRADE_ACCEPTED` marks pending.
3. Two `RESOURCE_TRANSFER` events move offered then requested (or reject).
4. `TRADE_REJECTED` releases reservation.

Fees: **none** in v0.1. Expiration: `expires_cycle` if set; else open until reject/world close.

## Status surfaces (player-visible, not research scores)

Grounded only in canonical state:

- resource holdings
- production capacity (sum of node.available × modifiers)
- infrastructure control/condition
- organization membership/size
- influence
- discoveries (entity ARTIFACT/DOCUMENT known via OBSERVE history — observational, not a score)

**MUST NOT** expose anomaly score, capability confidence, epistemic restraint, or phenomenon classification on player surfaces.
