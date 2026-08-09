# Authoritative Event Catalog v0.1

## Status and scope

This document defines the closed 24-type `event_type` catalog for NOEMA v0.1. A conforming v0.1 world ledger MUST use exactly one of the event types listed here. New types require a versioned specification change through the RFC process. An existing type MUST NOT change meaning.

The machine-readable authority is [`event-types.json`](../specs/event-types.json). It composes with [`world-event.schema.json`](../specs/world-event.schema.json), narrows the otherwise generic `payload` object by `event_type`, and does not change the `world-event/1.0` envelope.

## Reducer contract

All reducers have the signature:

```text
reduce_<event_type>(state: WorldState, event: WorldEvent) -> WorldState
```

Reducers MUST be deterministic and pure with respect to `(world_version, seed, deterministic_config, prior_state, ordered_event)`. They MUST validate the event payload and all stated preconditions before mutation. Application is atomic. On validation or precondition failure, the reducer MUST reject the ledger entry, return no state, and perform no side effect. Rejection events in this catalog record a decision already made by command resolution. They do not authorize implementations to invent a second rejection while replaying them.

No reducer may perform network I/O, send a live message, call an agent or model, write a second ledger entry, read wall-clock time, or consume unseeded randomness. Any resulting notification, observation, trigger, or follow-on transition MUST be represented by a separately ordered event. The only permitted effect of applying an event is the state mutation named below.

Identifiers use `^[A-Za-z0-9_.:-]+$`. Resource quantities are finite non-negative numbers. Resource deltas are finite non-zero numbers and MUST NOT make a holding negative unless the event type explicitly represents a rejected operation.

## Closed catalog

### `AGENT_ENTERED_WORLD`

Payload: `agent_id`, `room_id`, `budgets` (resource-name to non-negative quantity), and optional `manifest_id`. Reducer: require the agent to be registered, not active in any world, the room to exist, and each budget to be within configured grants. Set the agent active in this world, set its location, initialize current budgets, and add it to the room entity set. Reject duplicate entry, cross-world presence, unknown agent/room, or invalid grants. No external side effect.

### `AGENT_LEFT_WORLD`

Payload: `agent_id`, `room_id`, and `reason` (`DISCONNECTED`, `VOLUNTARY`, `REMOVED`, or `WORLD_CLOSED`). Reducer: require the agent to be active at `room_id`. Remove it from the room entity set, clear its live location, and mark its world presence inactive while retaining history. Reject mismatched presence or location. No external side effect.

### `MOVE`

Payload: `agent_id`, `exit_id`, `from_room_id`, `to_room_id`, and `cost_paid` (resource-name to non-negative quantity). Reducer: require the agent at the source, the exit to connect the named rooms, all conditions to have been resolved, and exact available costs. Atomically deduct costs, move the agent, and update both rooms' entity sets. Reject stale location, invalid exit/destination, unmet conditions, or insufficient holdings. Exit triggers and observations require later events.

### `MOVE_REJECTED`

Payload: `agent_id`, `exit_id` (nullable), `from_room_id`, and `reason` (`EXIT_NOT_FOUND`, `CONDITION_FAILED`, `INSUFFICIENT_RESOURCE`, `LOCKED`, `PERMISSION_DENIED`, or `CAPACITY_EXCEEDED`). Reducer: require the agent still at `from_room_id`; append the rejection reference to bounded agent/world audit state only. Location, room membership, and resources remain unchanged. Reject if the recorded source is stale. No notification side effect.

### `LOOK`

Payload: `agent_id`, `room_id`, `attention_spent`, and `observation_id`. Reducer: require the agent in the room, a non-negative spend not exceeding attention, and an unused observation id. Deduct attention and record the observation request metadata. It does not construct or deliver an observation. Reject stale location, insufficient attention, or duplicate observation id. `OBSERVATION_GENERATED` is a separate event.

### `INSPECT`

Payload: `agent_id`, `entity_id`, `room_id`, `attention_spent`, and `observation_id`. Reducer: require co-location, inspect visibility/permission established by deterministic resolution, sufficient attention, and a fresh observation id. Deduct attention and record request metadata. Do not expose private state or generate observations in this reducer. Reject failed visibility/permission, stale location, insufficient attention, or duplicate observation id.

### `MESSAGE`

Payload: `message_id`, `sender_id`, `recipient_id`, `text`, and `cost_paid`. Reducer: require the sender active, recipient addressable in the same world, a new message id, permitted content size, and exact available costs. Deduct cost and create an immutable `QUEUED` message record. Reject duplicates, cross-world recipients, containment/permission failure, size violation, or insufficient holdings. Transport is not a reducer side effect.

### `MESSAGE_DELIVERED`

Payload: `message_id`, `recipient_id`, and `delivered_cycle`. Reducer: require the message to be `QUEUED`, the recipient to match, and delivery cycle to equal the envelope cycle. Mark it `DELIVERED` and add its id to the recipient inbox index. Reject unknown, duplicate, or mismatched delivery. Live notification is outside the reducer.

### `TRADE_PROPOSED`

Payload: `trade_id`, `proposer_id`, `counterparty_id`, `offered`, `requested`, and optional `expires_cycle`. Reducer: require both parties active in the same world, a new trade id, nonempty positive holdings maps, proposer ownership of offered holdings, and an expiry later than the event cycle. Create an `OPEN` trade reservation and reserve the offered quantities. Reject duplicates, self/cross-world trades, invalid expiry, or insufficient holdings. No message is sent implicitly.

### `TRADE_ACCEPTED`

Payload: `trade_id`, `accepted_by`. Reducer: require an open, unexpired trade; accepter must be its counterparty and own the requested holdings. Mark the proposal `ACCEPTED_PENDING_TRANSFER`. Holdings do not move here. Reject wrong party, missing/closed/expired trade, or insufficient requested holdings. `RESOURCE_TRANSFER` events perform transfers.

### `TRADE_REJECTED`

Payload: `trade_id`, `rejected_by`, and `reason` (`DECLINED`, `EXPIRED`, `INSUFFICIENT_RESOURCE`, `INVALID_TERMS`, or `CANCELLED`). Reducer: require an open proposal and an authorized party, except deterministic expiry may be recorded by the world actor. Mark it `REJECTED`, store the reason, and release proposer reservations. Reject missing/closed trade or unauthorized rejection. No notification side effect.

### `RESOURCE_TRANSFER`

Payload: `transfer_id`, `from_id`, `to_id`, `resource`, `amount`, and optional `trade_id`. Reducer: require distinct existing holders in the same world, a fresh transfer id, positive amount, sufficient unreserved or correctly reserved balance, and a matching accepted trade when `trade_id` is present. Atomically debit, credit, release the matching reservation, and record the transfer. Reject any mismatch or overdraft. No external settlement exists.

### `ORG_CREATE`

Payload: `org_id`, `name`, `charter`, `creator_id`, and nonempty `initial_members` containing unique `{agent_id, role}` objects. Reducer: require a new org id, unique valid members, an active creator included among them, and valid bounded text. Create an `ACTIVE` organization with the envelope cycle and memberships. Reject duplicates, invalid membership, or missing creator. No invitations or messages are implicit.

### `ORG_MEMBER_ADD`

Payload: `org_id`, `agent_id`, `role`, and `authorized_by`. Reducer: require an active organization, a nonmember agent, and an authorizer permitted by the organization protocol. Add membership with the envelope cycle. Reject unknown/dissolved org, duplicate member, unknown agent, or failed authorization. No notification side effect.

### `ORG_MEMBER_REMOVE`

Payload: `org_id`, `agent_id`, `authorized_by`, and `reason`. Reducer: require an active organization, current membership, and protocol authorization. Remove active membership and retain its historical end cycle/reason. Reject unknown/dissolved org, absent member, or failed authorization. Owned resources are not moved implicitly.

### `ENTITY_CREATE`

Payload: `entity_id`, `entity_type`, nullable `location` and `owner_id`, plus `properties`, `inventory`, and `state`. Reducer: require a new entity id, valid referenced room/owner/inventory entities, and no containment cycle. Create the live entity at the envelope cycle and add it to the room index when located. Reject duplicates, dangling references, or cyclic containment. No trigger side effect.

### `ENTITY_DESTROY`

Payload: `entity_id`, `reason`, and optional `successor_id`. Reducer: require a live entity and valid successor when supplied. Set `destroyed_cycle`, change status to `ARCHIVED` (or `DEAD` for an agent entity), remove live location/inventory indexes, and retain the full record. Reject unknown/already destroyed entity or invalid successor. Never hard-delete or implicitly transfer contents.

### `ENTITY_UPDATE`

Payload: `entity_id`, `set` (property/state keys to JSON values), and `unset` (unique property/state keys). Reducer: require a live entity, at least one operation, no overlap, and only mutable allowlisted keys. Apply keys in lexicographic order. Reject immutable/private keys, overlap, unknown entity, or invalid values. It cannot change identity, ownership, location, inventory, or lifecycle fields.

### `WAIT`

Payload: `agent_id` and `cycles` (positive integer). Reducer: require an active agent and a duration allowed by configuration. Set or extend its deterministic wait-until cycle to `event.cycle + cycles`. Reject inactive agents or excessive duration. It does not advance the world clock by itself.

### `BUDGET_CONSUMED`

Payload: `agent_id`, `resource`, `amount`, `action_id`, and `remaining`. Reducer: require the current holding to be at least `amount`, a fresh `(action_id, resource)` consumption key, and `remaining` to equal current minus amount. Debit once and record consumption. Reject overdraft, duplicate consumption, or arithmetic mismatch. No provider/tool call is performed.

### `BUDGET_EXCEEDED`

Payload: `agent_id`, `resource`, `requested`, `available`, and `action_id`. Reducer: require `available` to equal the current holding and `requested > available`; record the rejected action and budget reason in audit state only. Budgets and world state remain otherwise unchanged. Reject stale balances, non-exceeding requests, or duplicate rejection keys. The attempted action MUST NOT be applied, called, queued, or charged.

### `SITUATION_INJECTED`

Payload: `situation_id`, `genome_id`, `genome_version`, `target_room_ids`, `selection_score`, `score_components`, and `seed_stream_id`. Reducer: require a new situation id, existing target rooms, finite scores whose components deterministically reproduce the declared selection score under versioned configuration, and a named seed stream. Add the active situation and its room references. Reject unknown rooms, duplicate ids, score mismatch, or unnamed nondeterminism. Any concrete entities or noise require separate events.

### `NOISE_APPLIED`

Payload: `noise_id`, `observation_id`, `agent_id`, `level`, `fields_affected`, `operations`, and `seed_stream_id`. Reducer: require a pending observation for the agent, a fresh noise id, level in `[0,1]`, unique affected paths, allowed operations, and reproducibility from the named stream. Attach the immutable noise decision to pending observation metadata. Reject unknown observations, forbidden/private paths, mismatches, or unnamed nondeterminism. It does not edit canonical world state.

### `OBSERVATION_GENERATED`

Payload: `observation_id`, `agent_id`, `source_event_ids`, `observation_digest`, `redactions`, and optional `noise_id`. Reducer: require a pending request, ordered existing source events, a fresh digest record, and matching noise metadata when supplied. Mark the observation record generated and index its digest for replay/research. Canonical room/entity state and private agent state do not change. Delivery/export requires separate policy-controlled processing and is not a reducer side effect.

## Ordering and rejection rules

1. Validate the `world-event/1.0` envelope and the matching payload schema from `event-types.json`.
2. Require the next contiguous sequence for the world and verify digest linkage under the ledger protocol.
3. Evaluate the reducer preconditions against exactly the prior state.
4. If any check fails, reject the event before append and leave state unchanged.
5. If all checks pass, append and apply atomically.
6. A command rejected before event creation SHOULD produce the catalog's matching rejection event where one exists. Budget denial MUST produce `BUDGET_EXCEEDED`. Generic malformed or unauthorized input is an API/protocol rejection and is not a free-form world event.

Replay MUST apply only accepted ledger events in sequence order. Replaying the same snapshot and event sequence MUST produce the same final state and observation digests.
