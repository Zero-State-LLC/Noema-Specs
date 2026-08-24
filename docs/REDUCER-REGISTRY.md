# Reducer Registry and Mutation Ownership

**Status:** Architecture authority for *who may write which world field*. First slice of the post-reconciliation frontier.  
**Does not replace:** [EVENT-CATALOG.md](EVENT-CATALOG.md) (reducer semantics) · [WORLD-ENGINE.md](WORLD-ENGINE.md) (cycle / fence / transaction) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) (command preconditions)  
**Hosted split:** [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md) · [PLATFORM.md](PLATFORM.md)

This document **registers existing reducers** and names the **sole mutation owner** for each invariant-sensitive field family. It does not add verbs, event types, or a second World Engine.

```text
COMMAND RESOLUTION  →  emits World Events
EVENT REDUCER       →  mutates named fields only
PROJECTION          →  reads; never writes WorldState
RESEARCH            →  never writes WorldState
```

---

## Layers

| Layer | Job | Must not |
|-------|-----|----------|
| Worker / Gateway | Authenticate, normalize, route | Embed reducers or write Postgres world rows |
| World DO (`NoemaWorldDO`) | Serialize / order live commands; hold the writer fence | Be the sole copy of a durable commitment |
| Command resolution | Validate action, reserve, emit events | Mutate fields except via those events |
| Event reducer | Apply one cataloged type to WorldState | I/O, wall-clock, second implicit event |
| Postgres transaction | Persist event batch + settled state + fence | Accept a second writer |
| Projection (PLAY / WATCH / GC derived) | Rebuild views from committed events | Authorize mutations |
| Scheduler / queue / alarm | Wake settlement | Be the only record of a future obligation |

One active fenced writer per `world_id` ([MODULE-CONTRACTS.md](MODULE-CONTRACTS.md), [WORLD-ENGINE.md](WORLD-ENGINE.md)).

---

## Event reducer registry

Authoritative payload and reject rules remain [EVENT-CATALOG.md](EVENT-CATALOG.md). This table is the **ownership index**.

### `event-catalog/0.1` (24)

| Event | May mutate | Must not mutate |
|-------|------------|-----------------|
| `AGENT_ENTERED_WORLD` | Presence, start location, initial budgets | Other Players; rooms except occupancy |
| `AGENT_LEFT_WORLD` | Presence, live location | History, holdings (except as already ledgered) |
| `MOVE` | Actor location, both rooms' occupancy, paid budgets | Other entities' owners |
| `MOVE_REJECTED` | Bounded audit ref only | Location, occupancy, budgets |
| `LOOK` | Attention spend, observation request metadata | Room contents, other Players |
| `INSPECT` | Attention spend, observation request metadata | Target entity fields |
| `MESSAGE` | Sender cost, `QUEUED` message record | Recipient holdings; delivery |
| `MESSAGE_DELIVERED` | Message status, inbox index | Text, third-party knowledge |
| `TRADE_PROPOSED` | Open trade + offered reservation | Transfer of holdings |
| `TRADE_ACCEPTED` | Trade status `ACCEPTED_PENDING_TRANSFER` | Balances (next `RESOURCE_TRANSFER`) |
| `TRADE_REJECTED` | Trade closed; release reservation | Other trades; inventories |
| `RESOURCE_TRANSFER` | Two holders' balances; matching reservation | Unrelated accounts |
| `ORG_CREATE` | New org + initial memberships | Dissolution of others |
| `ORG_MEMBER_ADD` | One membership row | Roles of existing members except as specified |
| `ORG_MEMBER_REMOVE` | End that membership | Implicit resource move |
| `ENTITY_CREATE` | New live entity + room index | Existing entity identity |
| `ENTITY_DESTROY` | Lifecycle to archived/dead; drop live indexes | Hard-delete; implicit inventory transfer |
| `ENTITY_UPDATE` | Allowlisted property/state keys | Identity, owner, location, inventory, lifecycle |
| `WAIT` | Actor wait-until cycle | World `cycle` |
| `BUDGET_CONSUMED` | Named resource on one Player | Other Players' budgets |
| `BUDGET_EXCEEDED` | Bounded audit ref only | Budgets |
| `SITUATION_INJECTED` | Active situation + room refs | Concrete entities (need later events). **Not** a WED id ([GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md)) |
| `NOISE_APPLIED` | Observation noise metadata | Canonical room/entity state |
| `OBSERVATION_GENERATED` | Observation record / digest index | Canonical room/entity state |

### `event-catalog/0.2` (eight additional)

| Event | May mutate | Must not mutate |
|-------|------------|-----------------|
| `CONTEST_DECLARED` | Open contest + stake reservation | Condition, transfers |
| `CONTEST_RESOLVED` | Close contest; spend/release stakes | Infra condition (use `INFRASTRUCTURE_DISRUPTED`) |
| `CRIME_DETECTED` | Immutable crime record; influence debit (floor 0) | Remove Player |
| `ACCESS_RESTRICTED` | Exit/room restriction consulted by `MOVE` | Geography graph |
| `INFRASTRUCTURE_DISRUPTED` | Named entity `condition` | Destroy; identity |
| `AGREEMENT_FORMED` | New ACTIVE agreement; formation cost | Third-party bindings |
| `AGREEMENT_BROKEN` | Mark BROKEN; influence; optional commitment release | Delete history |
| `TRADE_CANCELLED` | Trade closed (`CANCELLED`); release reservation | Other trades; inventories |

Worlds pinned to `0.1` MUST NOT apply 0.2 reducers.

---

## Mutation ownership map

Sole writer for each family. “Writer” means the **event reducer** (or named command step) that may change the field. Everything else reads.

| Field family | Sole writer(s) | Persistence |
|--------------|----------------|-------------|
| `World.cycle` / `World.status` | Cycle commit / world-ops path in WORLD-ENGINE · WORLD-OPERATIONS | Postgres world row |
| Writer fence / revision | WORLD-ENGINE fence | Postgres + DO coordination |
| Player presence / `room_id` | `AGENT_*`, `MOVE` | Postgres + DO live index |
| Player budgets / reservations | `BUDGET_*`, `RESOURCE_TRANSFER`, `TRADE_*`, contest stake events | Postgres (durable); DO may hold in-flight reservation only until settled |
| Entity identity / lifecycle | `ENTITY_CREATE`, `ENTITY_DESTROY` | Postgres |
| Entity `state.condition` | `ENTITY_UPDATE` (allowlist) or `INFRASTRUCTURE_DISRUPTED` | Postgres |
| Entity owner / location / inventory | Only events that name those fields (not `ENTITY_UPDATE`) | Postgres |
| Organization / membership | `ORG_*` | Postgres |
| Institution office / holder / lifecycle / profile | `ENTITY_CREATE` / `ENTITY_UPDATE` (allowlisted office keys on `office.*`) | WorldRuntime / world head |
| Player reconstruction record | `ENTITY_CREATE` / `ENTITY_UPDATE` (allowlisted reconstruction keys on `recon.*`) | WorldRuntime / world head |
| Trade object | `TRADE_*` + following transfers | Postgres |
| Message queue / delivery | `MESSAGE`, `MESSAGE_DELIVERED` | Postgres |
| Agreement | `AGREEMENT_*` | Postgres |
| Contest | `CONTEST_*` | Postgres; DO serializes declare/defend/resolve |
| Access restriction | `ACCESS_RESTRICTED` | Postgres (MOVE consults) |
| Observation / noise records | `LOOK` / `INSPECT` metadata, `NOISE_APPLIED`, `OBSERVATION_GENERATED` | Postgres research/observation tables; **not** WorldState geography |
| GC1 / GC3 / GC6 / GC9 projections | **None.** Rebuild from committed events | Optional cache; must be reconstructable |
| Research scores / claim labels | **None** on WorldState | Research store only |
| Admin Live views | **None** on WorldState | Control-plane projection |

If two rows would write the same field in one cycle, command resolution must emit a legal ordered event pair; the second reducer sees the first's state. Conflicting exclusive grants fail closed ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)).

---

## Derived projections are not writers

| Projection | Evidence | Writes WorldState? |
|------------|----------|--------------------|
| GC1 practice / recognition | Existing LOOK / INSPECT / TRADE / ENTITY_UPDATE | No |
| GC3 trade memory | `TRADE_ACCEPTED` | No |
| GC5-S2 claim / transmission | `MESSAGE` / `MESSAGE_DELIVERED` (+ existing notice `ENTITY_UPDATE`) | No |
| GC6 archive vs inspect | Accessible archive + INSPECT | No |
| GC9 maintenance custom | Distinct repair `ENTITY_UPDATE`s | No |
| WATCH / World Reports / Admin Live | Settled public events | No |

A cache of these lines MAY exist in the DO or Postgres. Losing the cache MUST NOT lose world truth.

---

## Command vs event (REJECTED / FAILED)

Command resolution may **reject** before any event (no WorldState mutation, normally no spend). That is the forward `REJECTED` distinction in [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md).

Catalog types `MOVE_REJECTED`, `TRADE_REJECTED`, `BUDGET_EXCEEDED` remain the frozen names for already-decided command outcomes. Replaying them does not invent a second rejection ([EVENT-CATALOG.md](EVENT-CATALOG.md)).

---

## Hosted execution

```text
Worker
  → NoemaWorldDO   (order, fence, in-flight)
  → event reducers (meaning)
  → Postgres event sink + world head (RFC-0016)
```

Hosted first resume: upsert `noema_world_heads` after mutating PLAY; restore that head if DO storage has no world; retry `unsettled` idempotently. Live DO state is not clobbered by an older head. Full `SERIALIZABLE` cycle-fence remains later.

Simple paths that already settle in one Postgres transaction without extra DO hops remain legal if they keep the same protocol, fence, receipts, and determinism. Do not add a DO for doctrine purity. Do not bypass the World DO where the current runtime already centralizes mutations.

---

## Out of this slice

```text
new event types / event-catalog/0.3
machine-readable reducer-registry schema
per-field JSON Pointer map
changing WORLD-ENGINE cycle order
runtime refactor
```

Those wait for an explicit RFC if a later implementation cannot execute this table.

## Acceptance

1. Every cataloged event type appears in the registry.
2. No field family has two sole writers.
3. GC derived lines are listed as non-writers.
4. `SITUATION_INJECTED` is not a WED id.
5. Frozen event names are unchanged.
