# Action Contracts (v0.1 Chamber)

Each v0.1 action is an exact transition. Machine-readable catalog: [`specs/action-contracts.v01.json`](../specs/action-contracts.v01.json).

Event reducers remain authoritative in [EVENT-CATALOG.md](EVENT-CATALOG.md) / [`event-types.json`](../specs/event-types.json).

## Verb scope

| Scope | Verbs / operations |
|-------|-------------------|
| **v0.1 REQUIRED** | `LOOK`, `MOVE`, `INSPECT`, `MESSAGE`, `WAIT`, `TRADE` (propose/accept/reject), `COMMIT` with `operation` ∈ `ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE`, `HARVEST`, `REPAIR` |
| **v0.1 OPTIONAL** | `QUERY` (read-only records), `ASK` (implemented as MESSAGE with ask semantics) |
| **LATER MILESTONE** | full `BUILD` construction trees, `RESEARCH`, `DELEGATE`, `EXPERIMENT`, `MODEL`, complex `COMMIT` governance |

Wire verbs remain those in [`agent-action.schema.json`](../specs/agent-action.schema.json). Organization and harvest/repair use `COMMIT` + `parameters.operation` so the closed verb enum stays stable while semantics are exact.

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
| ordering | scheduler order |
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
| events_on_success | `MESSAGE` (QUEUED), later `MESSAGE_DELIVERED` |
| events_on_failure | `BUDGET_EXCEEDED` / FORBIDDEN |
| visibility | parties only for text |
| spectator_projection | `message_notice` without text |

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
| events_on_success | `TRADE_ACCEPTED`, then `RESOURCE_TRANSFER` offered, then `RESOURCE_TRANSFER` requested |
| failure | `TRADE_REJECTED` with reason; release reservation |
| atomicity | both transfers commit or neither (single action reduction) |

## TRADE (reject / cancel)

| Field | Contract |
|-------|----------|
| events_on_success | `TRADE_REJECTED`; release reservation |
| reasons | `DECLINED`, `EXPIRED`, `INSUFFICIENT_RESOURCE`, `INVALID_TERMS`, `CANCELLED` |

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
| events_on_failure | insufficient → no debit |

## COMMIT / REPAIR

| Field | Contract |
|-------|----------|
| parameters | `operation=REPAIR`, `entity_id` (infrastructure) |
| preconditions | co-located INFRASTRUCTURE; energy ≥ 3; storage ≥ 1; compute ≥ 2 |
| resource_cost | energy 3, compute 2, storage 1 |
| events_on_success | `BUDGET_CONSUMED`×, `ENTITY_UPDATE` condition +15 (cap 100) |
| spectator_projection | `infrastructure` |

---

## Idempotency (all mutating)

Mutating ACT requires `idempotency_key`. Duplicate MUST return original accept/reject outcome and MUST NOT double-charge or double-append success events.

## Operator path

Operator-initiated world mutations MUST enter through Action Router as authenticated principal actions or declared external inputs (`SITUATION_INJECTED`), never by direct WorldState writes.
