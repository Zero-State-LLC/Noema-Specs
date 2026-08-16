# Construction and World Modification (GC2)

**Status:** Product authority that **closes the generalized `BUILD` deferral at specification level**. P0. Phase GC-A.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [INFRASTRUCTURE.md](INFRASTRUCTURE.md) · [GEOGRAPHY.md](GEOGRAPHY.md) · [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**Does not add `BUILD` to frozen v0.1 required help or the Chamber acceptance verb set.**  
**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) — one `BUILD` + operations, not a crafting industry.

This document is the construction contract the existing LATER notes pointed at. It is **not** an executable action-catalog increment. Runtime MUST NOT accept generalized `BUILD` until an RFC pins operations, events, fixtures, and conformance.

---

## Thesis

Construction is how Players leave **persistent, attributable structure** in geography, infrastructure, and routes.

Required product property:

> The state of the world at Cycle 500 can visibly contain consequences of Players who acted at Cycle 50.

Short-session PLAY still needs one such consequence: see the minimal durable trace pin in [DEEP-TIME.md](DEEP-TIME.md).

An isolated crafting minigame is a **defect**. Construction operates on resources, assets, locations, ownership, infrastructure, and history. It MUST couple to:

```text
GEOGRAPHY
RESOURCES
PRODUCTION
INFRASTRUCTURE
TRADE
ORGANIZATIONS
TERRITORY
CONFLICT
DEEP TIME
```

---

## Verb strategy

Do **not** create a verb per noun (`BUILD_RELAY`, `BUILD_WALL`, `BUILD_ARCHIVE`).

Settled wire shape for the later increment:

```text
one later verb BUILD
  + parameters.operation ∈ closed set
  + target / location / blueprint class
```

Existing `COMMIT.REPAIR` remains the repair transition ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)). Construction MUST reuse `REPAIR` rather than invent `BUILD.REPAIR`.

Closed **operation** set (product intent, not yet a schema enum):

| Operation | Intent | Distinct transition? |
|-----------|--------|----------------------|
| `CONSTRUCT` | Create a constructible entity in a valid location | Yes |
| `UPGRADE` | Increase a dimension of an existing constructible | Yes |
| `REPURPOSE` | Change function class within a legal conversion table | Yes |
| `CONNECT` | Create or alter a route/link between valid endpoints | Yes |
| `FORTIFY` | Increase defensibility / contest resistance | Yes (or UPGRADE of defensibility — RFC may collapse) |
| `DISMANTLE` | Remove function; leave salvage and a scar | Yes |
| `RESTORE` | Recover a ruined/abandoned constructible toward a prior class | Yes |
| `REPAIR` | Restore condition | **No new verb** — use existing `COMMIT.REPAIR` |

Human adapters may say `build`, `upgrade`, `fortify`. They normalize to `BUILD` + operation, except `repair` which stays `COMMIT.REPAIR`.

v0.1 Chamber help MUST continue to omit generalized construction ([PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md)).

---

## Constructible entity classes

Start from the v0.1 closed infrastructure set and add only classes that change strategic coupling.

| Class | Already exists? | Strategic effect |
|-------|-----------------|------------------|
| `relay` | Yes | Communication quality ([COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)) |
| `generator` | Yes | Node regeneration |
| `storage_bay` | Yes | Holding capacity |
| `production_node` | Yes | Harvest enablement / throughput |
| `route_link` | New (bounded) | Movement / trade cost or new exit |
| `defensive_work` | New (bounded) | Contest resistance / access |
| `archive_annex` | New (bounded) | Record capacity / access |
| `workshop` | New (bounded) | Construction/repair throughput, not a crafting minigame |

The constructible catalog is **closed** per version. A new class requires a catalog RFC. World Services, institutions, and artifacts are not implicitly constructible.

---

## Valid locations

A construct attempt is legal only when **all** hold:

1. Actor is co-located with the target room (or both endpoints for `CONNECT`).
2. Room geography permits the class (not every room accepts a generator or defensive work).
3. Local capacity / crowding rules are satisfied (versioned).
4. Required resources, budgets, and any proficiency/authority gates are satisfied.
5. Territory / access policy does not forbid the actor ([TERRITORY-CONTROL.md](TERRITORY-CONTROL.md), v0.2 `ACCESS_POLICY`).
6. The operation is idempotent-safe (see below).

Hidden rooms, hidden exits, and unobserved nodes MUST NOT become advertised build targets.

---

## Costs and production dependencies

Construction spends the same five Chamber resources plus held lots where the catalog requires them.

| Channel | Role |
|---------|------|
| `energy` | Physical work |
| `compute` | Planning / upgrade / connect design |
| `attention` | Supervision (if versioned) |
| `influence` | Territorial or institutional permission |
| `storage` / lots | Materials taken from holdings or local nodes |
| Time / cycles | Multi-cycle projects are allowed; partial state must be ledgered |

Exact quantities are **SPEC GAP**. Failed attempts MUST NOT consume materials reserved only on success, matching existing reservation rules ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)).

Production dependency: some classes MAY require a nearby `workshop` or sufficient `production_node` condition. That is coupling, not a second skill minigame.

Proficiency MAY improve quality or cost bands ([MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)). Proficiency MUST NOT waive authority or geography gates.

---

## Ownership, stewardship, sharing

| Mode | Meaning |
|------|---------|
| `PLAYER` | Creating Player is owner |
| `SHARED` | Explicit co-owners; all named on the record |
| `INSTITUTION` | Institution owns; office-holders act under [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) |
| `UNCLAIMED` | After abandonment threshold; salvageable |

Stewardship is the right to `REPAIR`, `UPGRADE`, and set access. It MAY be separated from economic ownership only by a later RFC. First construction increment SHOULD keep owner = steward.

Transfer uses existing org/institution/succession machinery where possible. Do not invent a second property law.

---

## Maintenance, decay, damage, repair, abandonment, salvage

| Process | Rule |
|---------|------|
| Maintenance | Neglect is a choice. World Event Director and ordinary degradation continue ([INFRASTRUCTURE.md](INFRASTRUCTURE.md)) |
| Decay | Condition 0–100 remains the health model |
| Damage | Contest, disruption, and pressure events lower condition ([STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)) |
| Repair | Existing `COMMIT.REPAIR` |
| Abandonment | No qualifying steward for a versioned window → `UNCLAIMED` or ruined subclass; history retained |
| Salvage | `DISMANTLE` or salvage of `UNCLAIMED` returns a versioned fraction of materials and leaves a scar |
| Repurposing | Legal only via a closed conversion table (e.g. workshop → storage_bay). Illegal conversions fail closed |

A ruined constructible remains a **historical object**. It is not deleted.

---

## Territorial, route, trade, and conflict effects

Construction is illegal as flavor. Each class MUST change at least one of:

- movement cost or available exits;
- harvest / production / storage;
- communication quality or addressability;
- contest defensibility or access;
- trade friction;
- institutional archive capacity.

`CONNECT` that creates an exit is a geography mutation and MUST be replay-visible. `FORTIFY` MUST change contest modifiers, not only description. Relays MUST change [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md) when that package is live.

---

## Deep Time, naming, scars, visibility

| Concern | Rule |
|---------|------|
| Lineage | Construct, upgrade, repurpose, dismantle, restore are historical events |
| Historical naming | Display names MAY accrue ([DEEP-TIME.md](DEEP-TIME.md)); IDs MUST NOT change |
| World scars | Dismantle, ruin, and major damage leave scars as historical evidence |
| Visibility | New structure is locally observable; remote Players learn through movement, reports, messages, or authorized records |
| Partial observability | Construction MUST NOT reveal hidden rooms or hidden ownership to unauthorized observers |
| Attribution | After builders leave, WATCH/PLAY history MUST still be able to attribute “who built this” from public events |

Cycle 50 work remaining at Cycle 500 is the acceptance test (scenario C).

---

## Events, replay, idempotency, failure, recovery

Candidate later events (RFC required; no silent catalog expansion):

```text
STRUCTURE_CONSTRUCTED
STRUCTURE_UPGRADED
STRUCTURE_REPURPOSED
STRUCTURE_CONNECTED
STRUCTURE_FORTIFIED
STRUCTURE_DISMANTLED
STRUCTURE_RESTORED
STRUCTURE_ABANDONED
STRUCTURE_SALVAGED
```

Condition changes may continue to use existing infrastructure / `ENTITY_UPDATE` / `INFRASTRUCTURE_DISRUPTED` patterns where they already apply.

| Concern | Rule |
|---------|------|
| Idempotency | Same `idempotency_key` MUST NOT double-place a structure |
| Failure | Illegal location, insufficient resources, forbidden access → typed failure; no partial ghost entity unless a multi-cycle project record is the cataloged partial state |
| Multi-cycle projects | Partial projects are first-class entities with owner, progress, and salvage path |
| Recovery | Destroyed or ruined structures have `RESTORE` or rebuild-at-scar paths. No irreversible dead map |
| Replay | Seed + events determine structure set, owners, condition, and scars |

---

## PLAY / WATCH / research / security

| Surface | Rule |
|---------|------|
| PLAY | Local structures, own projects, public attribution |
| WATCH | Public construction, ruin, and route changes; no hidden stockpiles |
| STUDY | May capture construction trajectories; MUST NOT inject build quests |
| Security | GUI MUST NOT advertise illegal or hidden build targets |

---

## SPEC GAP

### Closed for GC2-S0 ([GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md), RFC-0006)

```text
CONSTRUCT + DISMANTLE only
four v0.1 infrastructure classes
pinned costs and salvage
one live asset per class per room
owner = steward
reuse ENTITY_CREATE / ENTITY_DESTROY / BUDGET_CONSUMED
attempt fixtures
```

### Still open (later slices)

```text
GC2-S1 closed: route_link waives cargo MOVE extra; no new exit
GC2-S2 closed: workshop saves 1 storage on in-room CONSTRUCT/REPAIR
GC2-S3 closed: defensive_work adds 50 contest defense millipoints in-room
GC2-S4 closed: archive_annex saves 1 attention on in-room INSPECT/ATTEST
GC2-S5 closed: BUILD.UPGRADE owned public workshop; storage save 2; once
GC2-S6 closed: BUILD.REPURPOSE owned public workshop → storage_bay; same entity_id
GC2-S7 closed: 12 idle committed cycles → UNCLAIMED; anyone may DISMANTLE
GC2-S8 closed: BUILD.RESTORE owned public UNCLAIMED; condition cap 50; scars stay dead
GC2-S9 closed: public relay CONSTRUCT is IN_PROGRESS; live after 1 committed cycle
GC2-S10 closed: BUILD.VEST personal public constructible to occupied OPERATE_NAMED_ASSET; same entity_id
GC2-S11 closed: BUILD.SHARE one entered Player as co-owner; same entity_id; once
GC2-S12 closed: BUILD.CONNECT dest pin on public route_link; existing two-way public neighbor; no new exit
GC2-S13 closed: public workshop CONSTRUCT is IN_PROGRESS; live after 1 committed cycle
GC2-S14 closed: public generator CONSTRUCT is IN_PROGRESS; live after 1 committed cycle
GC2-S15 closed: public storage_bay CONSTRUCT is IN_PROGRESS; live after 1 committed cycle
GC2-S16 closed: public production_node CONSTRUCT is IN_PROGRESS; live after 1 committed cycle
GC2-S17 closed: public defensive_work CONSTRUCT is IN_PROGRESS; live after 1 committed cycle; contest bonus live-only
GC2-S18 closed: public archive_annex CONSTRUCT is IN_PROGRESS; live after 1 committed cycle; attention discount live-only
remaining-class multi-cycle
third-and-later co-owners
first-world PLAY advertising BUILD
runtime implementation
```

`BUILD` remains **UNSUPPORTED** in ordinary Chamber PLAY until a separate implementation pass.

---

## Acceptance (scenario C)

A Player or institution constructs a `route_link` or upgrades a `relay` / `production_node` so that movement, trade, production, or communication changes; the original actors leave; later Players still observe the structure and can attribute it from history.
