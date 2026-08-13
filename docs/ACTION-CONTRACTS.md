# Action Contracts

Each action is an exact transition.

| Catalog | Machine file |
|---------|--------------|
| v0.1 Chamber | [`specs/action-contracts.v01.json`](../specs/action-contracts.v01.json) |
| v0.2 Strategic | [`specs/action-contracts.v02.json`](../specs/action-contracts.v02.json) |

Event reducers remain authoritative in [EVENT-CATALOG.md](EVENT-CATALOG.md).

The player-facing crosswalk between these semantic contracts, human commands, contextual GUI controls, and structured agent actions is [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md). This map does not replace the exact transitions below.

## Verb scope

| Scope | Verbs / operations |
|-------|-------------------|
| **v0.1 REQUIRED** | `LOOK`, `MOVE`, `INSPECT`, `MESSAGE`, `WAIT`, `TRADE` (propose/accept/reject), `COMMIT` with `operation` ∈ `ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE`, `HARVEST`, `REPAIR` |
| **v0.1 OPTIONAL** | `QUERY` (read-only records), `ASK` (implemented as MESSAGE with ask semantics) |
| **v0.2 STRATEGIC** (`event-catalog/0.2`) | `COMMIT.CONTEST_DECLARE`, `COMMIT.CONTEST_DEFEND`, `COMMIT.AGREEMENT_FORM`, `COMMIT.AGREEMENT_TERMINATE`, `COMMIT.ACCESS_POLICY` |
| **LATER MILESTONE** | full `BUILD` construction trees — product contract [CONSTRUCTION.md](CONSTRUCTION.md); still not v0.1-required. `RESEARCH`, `DELEGATE`, `EXPERIMENT`, `MODEL`, complex `COMMIT` governance |

Wire verbs remain those in [`agent-action.schema.json`](../specs/agent-action.schema.json). Organization and harvest/repair use `COMMIT` + `parameters.operation` so the closed verb enum stays stable while semantics are exact. Every mutating action carries a required `client_action_sequence`; the server assigns the versioned `action_priority` below and sorts frozen-cycle actions by `(action_priority, agent_id, client_action_sequence, action_id)`.

This closed action vocabulary is intentionally stable. Dynamic gameplay belongs in compatible targets, parameters, preconditions, authority, resources, observation, and consequences. A new noun, content type, institution, or theme MUST NOT create a runtime verb; a genuinely new semantic transition requires a versioned Specs change.

## Canonical action priorities

Lower priority values resolve first. These values are world-rules metadata and MUST NOT be supplied by clients.

| Priority | Actions | Rationale |
|----------|---------|-----------|
| 10 | `WAIT` | no-op scheduling before contested mutations |
| 20 | `MOVE` | position and capacity establish the cycle's spatial state |
| 30 | `LOOK`, `INSPECT`, `QUERY` | local sensing after movement contention resolves |
| 40 | `MESSAGE`, `ASK` | communication observes the resolved addressability state |
| 50 | `TRADE` | consented exchange after parties and messages are resolved |
| 60 | `COMMIT.ORG_CREATE`, `COMMIT.ORG_MEMBER_ADD`, `COMMIT.ORG_MEMBER_REMOVE` | institutional mutations after exchange intent |
| 70 | `COMMIT.HARVEST`, `COMMIT.REPAIR` | resource and infrastructure changes last to make contention explicit |

---

## LOOK

| Field | Contract |
|-------|----------|
| availability | agent ACTIVE in world |
| inputs | optional target (default room) |
| preconditions | agent location known |
| reads | room, exits, visible entities |
| writes | attention budget |
| resource_cost | attention 1 |
| resource_reservation | attention 1 until complete |
| events_on_success | `LOOK`, then `OBSERVATION_GENERATED` (+ optional `NOISE_APPLIED`) |
| events_on_failure | `BUDGET_EXCEEDED` if attention insufficient |
| visibility | self observation only |
| observation_result | room projection |
| idempotency | key required; replay returns same observation_id binding |
| ordering | scheduler order key `(action_priority, agent_id, client_action_sequence, action_id)` |
| failure_codes | `BUDGET_EXCEEDED`, `FORBIDDEN` |
| spectator_projection | none (private observe) or public room activity pulse if policy allows |
| replay_behavior | same digests |

## MOVE

| Field | Contract |
|-------|----------|
| inputs | `exit_id` or direction resolved to exit |
| preconditions | agent at `from_room_id`; exit OPEN; conditions satisfied; energy ≥ 1 |
| reads | exit, rooms, conditions |
| writes | agent location, energy |
| resource_cost | energy 1 (plus any exit traversal_cost) |
| events_on_success | `MOVE` with `cost_paid` |
| events_on_failure | `MOVE_REJECTED` reason enum; **no** energy debit on reject |
| spectator_projection | `agent_move` |

## INSPECT

| Field | Contract |
|-------|----------|
| inputs | `entity_id` |
| preconditions | co-located; inspect permission; attention ≥ 2 |
| resource_cost | attention 2 |
| events_on_success | `INSPECT`, `OBSERVATION_GENERATED` |
| events_on_failure | `BUDGET_EXCEEDED` or reject without event if schema-invalid |
| spectator_projection | none of private inspect fields |

## MESSAGE

| Field | Contract |
|-------|----------|
| inputs | `recipient_id`, `text` (max `NOEMA_MAX_ACTION_PAYLOAD_BYTES`) |
| preconditions | sender ACTIVE; recipient addressable same world; compute ≥ 1 |
| resource_cost | compute 1; if local relay condition &lt; 25, additional compute 1 |
| events_on_success | `MESSAGE` (QUEUED), then same-cycle `MESSAGE_DELIVERED` before observation projection when recipient active |
| events_on_failure | `BUDGET_EXCEEDED` / FORBIDDEN |
| visibility | parties only for text |
| spectator_projection | `message_notice` without text |

## ASK (optional; not a separate mutation class)

`ASK` is a human/interface convenience intent. It is **not** a distinct canonical mutation.

```text
ASK
  → MESSAGE with ask semantics
  → ordinary MESSAGE privacy, cost, delivery, and ordering
```

Example: `ask Nacre "What happened at Coldline?"` normalizes to `MESSAGE` with `recipient_id` = Nacre and the question as `text`.

| Field | Contract |
|-------|----------|
| first-world | OPTIONAL. Omit from ordinary help unless the deployment advertises it. |
| canonical reducer | `MESSAGE` |
| resource_cost | Same as MESSAGE |
| events | Same as MESSAGE |
| agents | MUST use `MESSAGE`. No separate ASK verb is required. |
| answer linking | DEFERRED. Any answer is a later MESSAGE or world-visible event. Do not invent a Q&A ledger. |

## QUERY (optional / first-world deferred)

`QUERY` is a read-only information operation over **Player-known, permissioned records**. It is not required for first-world go-live.

```text
INSPECT
  → detailed observation of a visible/co-located entity

QUERY
  → read Player-accessible known records / archives / maps / ledgers
```

QUERY MUST NOT become a database query, omniscient search, hidden-history access, Admin lookup, or research query for ordinary PLAY.

| Field | Contract |
|-------|----------|
| first-world | OPTIONAL / DEFERRED as a required hosted path |
| preconditions | record is already known and permissioned to this Player |
| resource_cost | attention 1 ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)) |
| mutation | none |
| events_on_success | observation / record projection only |
| events_on_failure | permission, availability, or budget; no public WATCH |
| visibility | observation boundary applies; no hidden history |
| spectator_projection | none of the private query result |

Queryable record families beyond Player-known maps, archives, and ledgers already in world observation are DEFERRED. Do not enumerate a new catalog here.

## WAIT

| Field | Contract |
|-------|----------|
| inputs | `cycles` ≥ 1 |
| resource_cost | 0 |
| events_on_success | `WAIT` |
| effect | sets wait-until; does not advance world clock alone |

## TRADE (propose)

| Field | Contract |
|-------|----------|
| inputs | `counterparty_id`, `offered{}`, `requested{}`, optional `expires_cycle` |
| preconditions | both ACTIVE; offered positive; proposer unreserved balance sufficient; compute ≥ 1 |
| resource_cost | compute 1 |
| events_on_success | `TRADE_PROPOSED` (reserves offered) |
| events_on_failure | no proposal; possible `BUDGET_EXCEEDED` |
| atomicity | reservation atomic |
| spectator_projection | `trade` |

## TRADE (accept)

| Field | Contract |
|-------|----------|
| inputs | `trade_id` |
| preconditions | open unexpired trade; actor is counterparty; holds requested |
| resource_cost | compute 1 ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) `TRADE propose/accept 1`). No second proposal tax. |
| events_on_success | `TRADE_ACCEPTED`, then `RESOURCE_TRANSFER` offered, then `RESOURCE_TRANSFER` requested |
| failure | `TRADE_REJECTED` with reason; release reservation |
| reservation | Offered reservation is **consumed** by the transfer legs, not left open |
| atomicity | both transfers commit or neither (single action reduction) |

## TRADE (reject / cancel)

| Field | Contract |
|-------|----------|
| resource_cost | **0**. Rejecting or cancelling MUST NOT trap a Player behind resource scarcity. |
| events_on_success | `TRADE_REJECTED`; release reservation |
| reasons | `DECLINED`, `EXPIRED`, `INSUFFICIENT_RESOURCE`, `INVALID_TERMS`, `CANCELLED` |

### Trade reservation release

The proposer's offered reservation MUST be released or consumed on every closure. No stuck reservations.

| Closure | Reservation |
|---|---|
| accepted | Consumed by the atomic transfer legs |
| rejected (`DECLINED`) | Released |
| cancelled (`CANCELLED`) | Released |
| expired (`EXPIRED`) | Released |
| invalidated (`INVALID_TERMS` / `INSUFFICIENT_RESOURCE` / other reject reasons) | Released |

### Trade design rationale

Two-phase offer/accept is the **smallest** mechanism that permits negotiation and strategic exchange without a full market order book. Direct transfer without consent is **not** v0.1 default (prevents silent theft). Fees: none.

## COMMIT / ORG_CREATE

| Field | Contract |
|-------|----------|
| parameters | `operation=ORG_CREATE`, `org_id`, `name`, `charter`, `initial_members` |
| preconditions | creator ACTIVE; org_id fresh; creator in members; influence ≥ 5; compute ≥ 2 |
| resource_cost | influence 5, compute 2 |
| events_on_success | `BUDGET_CONSUMED`×, `ORG_CREATE` |
| spectator_projection | `organization` |

## COMMIT / ORG_MEMBER_ADD

| Field | Contract |
|-------|----------|
| parameters | `operation=ORG_MEMBER_ADD`, `org_id`, `agent_id`, `role` |
| preconditions | org ACTIVE; authorizer role ∈ {founder, officer}; target not member; compute ≥ 2; influence ≥ 1 on authorizer |
| resource_cost | compute 2, influence 1 (authorizer) |
| events_on_success | `ORG_MEMBER_ADD` |

## COMMIT / ORG_MEMBER_REMOVE

| Field | Contract |
|-------|----------|
| parameters | `operation=ORG_MEMBER_REMOVE`, `org_id`, `agent_id`, `reason` |
| preconditions | membership exists; authorizer permitted or self-leave |
| events_on_success | `ORG_MEMBER_REMOVE` |
| note | org resources not moved implicitly |

### Organization v0.1 scope

Roles: `founder`, `officer`, `member`, `advisor`. No elections, laws, or multi-step governance. Dissolution: not automated; status may become `DISSOLVED` only via future RFC or operator injection ledgered as `ENTITY_UPDATE`/`ORG_*` extension — **v0.1 agents cannot dissolve** (record as LATER). Self-leave via ORG_MEMBER_REMOVE with self as agent_id is REQUIRED.

## COMMIT / HARVEST

| Field | Contract |
|-------|----------|
| parameters | `operation=HARVEST`, `entity_id` (node), `amount` ≥ 1 |
| preconditions | co-located; node.available ≥ amount; agent can hold storage |
| resource_cost | energy 2, compute 1 |
| events_on_success | `BUDGET_CONSUMED`×, `RESOURCE_TRANSFER` node→agent, `ENTITY_UPDATE` node.available |
| events_on_failure | insufficient → no debit, no public event |
| spectator_projection | public harvest notice: Player public identity harvested from public node; **no** amounts, inventory, or hidden node capacity ([SPECTATOR.md](SPECTATOR.md)) |

## COMMIT / REPAIR

| Field | Contract |
|-------|----------|
| parameters | `operation=REPAIR`, `entity_id` (infrastructure) |
| preconditions | co-located INFRASTRUCTURE; energy ≥ 3; storage ≥ 1; compute ≥ 2 |
| resource_cost | energy 3, compute 2, storage 1 |
| events_on_success | `BUDGET_CONSUMED`×, `ENTITY_UPDATE` condition +15 (cap 100) |
| spectator_projection | `infrastructure` |

---

## v0.2 Strategic COMMIT operations

Require `catalog_version = event-catalog/0.2`. Details: [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md), [STRATEGIC-EVENT-COUPLING.md](STRATEGIC-EVENT-COUPLING.md).

### COMMIT / CONTEST_DECLARE

| Field | Contract |
|-------|----------|
| parameters | `operation=CONTEST_DECLARE`, `contest_form`, `target`, `stake`, `expires_cycle`, `seed_stream_id`, optional `defender_id`/`notes` |
| preconditions | ACTIVE; co-located; form/target match; stake ≥ form minimums; open-contest limits |
| resource_cost | compute 2, influence 1 (+ stake reserved) |
| events_on_success | `CONTEST_DECLARED` |
| events_on_failure | insufficient stake/budget; invalid target |
| spectator_projection | `contest_declared` (banded stakes) |
| idempotency | key required |

### COMMIT / CONTEST_DEFEND

| Field | Contract |
|-------|----------|
| parameters | `operation=CONTEST_DEFEND`, `contest_id`, `stake` |
| preconditions | contest OPEN; defender authorized; before `expires_cycle` |
| resource_cost | compute 1 (+ stake reserved) |
| events_on_success | **none** (reservation only; settlement on `CONTEST_RESOLVED`) |
| notes | Passive defense also from infra condition + mutual-defense agreements |

### World / CONTEST_RESOLVE (scheduler or authorized world actor)

| Field | Contract |
|-------|----------|
| preconditions | OPEN contest; stakes reserved; deterministic score computed |
| events_on_success | `CONTEST_RESOLVED` then ordered follow-ons per coupling doc |
| atomicity | entire batch validated before append |

### COMMIT / AGREEMENT_FORM

| Field | Contract |
|-------|----------|
| parameters | `operation=AGREEMENT_FORM`, type, parties, machine terms, signatories, costs |
| preconditions | ≥2 active parties; consent pre-validated; machine terms valid for type |
| resource_cost | compute 2, influence 1 (payer) |
| events_on_success | `AGREEMENT_FORMED` |
| spectator_projection | `agreement_formed` if PUBLIC |

### COMMIT / AGREEMENT_TERMINATE

| Field | Contract |
|-------|----------|
| parameters | `operation=AGREEMENT_TERMINATE`, `agreement_id`, `reason` |
| events_on_success | `AGREEMENT_BROKEN` |
| spectator_projection | `agreement_broken` if PUBLIC |

### COMMIT / ACCESS_POLICY

| Field | Contract |
|-------|----------|
| parameters | `operation=ACCESS_POLICY`, scope, mode, applies_to, expires_cycle |
| preconditions | authorized_by WORLD policy or contest/crime follow-on authority |
| events_on_success | `ACCESS_RESTRICTED` |
| spectator_projection | `access_changed` |

---

## Idempotency (all mutating)

Mutating ACT requires `idempotency_key`. Duplicate MUST return original accept/reject outcome and MUST NOT double-charge or double-append success events.

## Operator path

Operator-initiated world mutations MUST enter through Action Router as authenticated principal actions or declared external inputs (`SITUATION_INJECTED`), never by direct WorldState writes.
