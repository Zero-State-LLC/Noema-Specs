# GC2 First Slice — Construct and Dismantle Existing Infrastructure

**Status:** Shipped as hosted `BUILD` CONSTRUCT/DISMANTLE (RFC-0006 Accepted; reference runtime PR #79). Chamber help still omits `BUILD`.  
**Parent:** [CONSTRUCTION.md](CONSTRUCTION.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0006](../rfcs/RFC-0006-construction-existing-events.md)  
**Does not open:** `event-catalog/0.3` · new infrastructure classes · crafting · multi-cycle projects

This is the smallest construction increment that still satisfies scenario C’s *shape* (persistent, attributable structure) without a construction industry.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Nine `STRUCTURE_*` events | **REJECT.** Reuse `ENTITY_CREATE`, `ENTITY_UPDATE`, `ENTITY_DESTROY`, `BUDGET_CONSUMED` |
| `BUILD_RELAY` / crafting tree | **REJECT.** One `BUILD` + `operation` |
| New classes (`route_link`, `workshop`, …) | **DEFER** to a later slice. First cut only mutates the v0.1 four |
| `FORTIFY` as its own operation | **DEFER** / collapse into later `UPGRADE` |
| `UPGRADE` / `REPURPOSE` / `CONNECT` / `RESTORE` | **DEFER** |
| Multi-cycle ghost projects | **DEFER.** S0 is single-cycle, all-or-nothing |
| Repair via `BUILD` | **REJECT.** Keep `COMMIT.REPAIR` |
| Level-based cheaper builds | **REJECT.** No mastery discount in S0 |

Pressures: **scarcity** (budget + storage materials), **distance** (must be co-located), **dependency** (someone must maintain what is built), **uncertainty** (remote Players do not auto-see the new asset).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s0` |
| Catalog | `construction-catalog/gc2-s0` |
| Wire verb | `BUILD` (later; not v0.1 required help) |
| Operations | `CONSTRUCT`, `DISMANTLE` |
| Classes | `relay`, `generator`, `storage_bay`, `production_node` |
| Events | Existing `event-catalog/0.1` types only |
| Owner | Constructing Player; owner = steward |

### CONSTRUCT

| Field | Contract |
|-------|----------|
| parameters | `operation=CONSTRUCT`, `class`, `room_id` (default current) |
| preconditions | Actor ACTIVE and co-located; `class` in catalog; room has no live asset of that class; budgets ≥ cost; not a hidden room |
| resource_cost | Catalog table below |
| events_on_success | `BUDGET_CONSUMED`×, then `ENTITY_CREATE` (`entity_type=INFRASTRUCTURE`, `owner_id` = actor, `location` = room, `properties.infra_type` = class, `state.condition` = 100) |
| events_on_failure | none (typed API/command failure) |
| failure_codes | `NOT_COLOCATED`, `CLASS_FORBIDDEN`, `SLOT_OCCUPIED`, `BUDGET_EXCEEDED`, `NOT_OBSERVABLE`, `FORBIDDEN` |

### DISMANTLE

| Field | Contract |
|-------|----------|
| parameters | `operation=DISMANTLE`, `entity_id` |
| preconditions | Actor co-located; entity is live constructible infrastructure; actor is owner |
| resource_cost | energy 4, compute 2 |
| salvage | storage + catalog `salvage_storage` (clamped by actor storage capacity; overflow lost and ledgered as `BUDGET_CONSUMED` if a loss event is already legal — otherwise clamp only) |
| events_on_success | `BUDGET_CONSUMED`×, `ENTITY_DESTROY` (`reason=DISMANTLED`), optional existing Deep Time scar record if v0.6 indexes are live |
| failure_codes | `NOT_COLOCATED`, `NOT_OWNER`, `NOT_FOUND`, `BUDGET_EXCEEDED` |

`COMMIT.REPAIR` is unchanged: energy 3, compute 2, storage 1, condition +15 cap 100.

### Costs (pinned)

| Class | CONSTRUCT energy | compute | storage | influence | salvage_storage |
|-------|------------------|---------|---------|-----------|-----------------|
| `relay` | 8 | 4 | 4 | 2 | 2 |
| `generator` | 8 | 3 | 5 | 0 | 2 |
| `storage_bay` | 5 | 2 | 6 | 0 | 3 |
| `production_node` | 7 | 3 | 4 | 0 | 2 |

One action, decision scale. Do not require repeated construct clicks.

### Crowding

At most **one live asset of each class per room**. That is the S0 room-permission table. Hidden rooms never appear as construct targets.

---

## A–J (this slice)

| Test | Result |
|------|--------|
| A Primitive reuse | Asset + location + resource + player. `ENTITY_*` already exist |
| B Pressures | Scarcity, distance, dependency, uncertainty |
| C Decision density | One CONSTRUCT / DISMANTLE per commitment |
| D Coupling | Relay → communication; generator → production; storage → trade buffer; node → harvest |
| E Verb stability | One later `BUILD`; repair stays `REPAIR` |
| F Emergence | A maintenance order or freight habit can form around built assets without a company engine |
| G Deep Time | `ENTITY_CREATE` / `DESTROY` remain attributable |
| H Parity | Same action for human and agent Controllers |
| I Research isolation | Meaningful with STUDY hidden |
| J Removal | Without this, Players cannot add persistent infrastructure after genesis |

---

## Explicitly out of S0

```text
route_link (closed in GC2-S1)
defensive_work, archive_annex, workshop
UPGRADE, REPURPOSE, CONNECT, FORTIFY, RESTORE
shared / institution ownership
abandonment timers
mastery cost discounts
event-catalog/0.3
first-world PLAY help advertising BUILD
```

---

## Runtime rule

Hosted Chamber accepts `BUILD` CONSTRUCT/DISMANTLE (human `construct` / `build` / `dismantle`). Help and `AVAILABLE HERE` still omit `BUILD`. Repair stays `COMMIT.REPAIR`. Contest and WED later shipped on their own slices; this document does not authorize help text for them.
