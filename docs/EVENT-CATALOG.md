# Authoritative Event Catalog

## Status and scope

| Catalog pin | Composed ledger schema | Payload binding source | Types | Product |
|-------------|------------------------|------------------------|-------|---------|
| `event-catalog/0.1` | [`event-catalog-0.1.schema.json`](../specs/event-catalog-0.1.schema.json) | [`event-types.json`](../specs/event-types.json) | **24** closed | Chamber v0.1 acceptance |
| `event-catalog/0.2` | [`event-catalog-0.2.schema.json`](../specs/event-catalog-0.2.schema.json) | [`event-types.0.2.json`](../specs/event-types.0.2.json) | **31** = 24 + 7 | Strategic conflict (RFC-0002 **Accepted**) |

A conforming world ledger MUST use only event types from its pinned catalog. Worlds on `0.1` MUST reject the seven 0.2 types. An existing type MUST NOT change meaning across catalog versions.

Ownership index (who may write which field): [REDUCER-REGISTRY.md](REDUCER-REGISTRY.md). This catalog remains the payload/reject authority.

Schemas compose with [`world-event.schema.json`](../specs/world-event.schema.json) and do not change the `world-event/1.0` envelope. Ledger admission MUST use the catalog-specific composed schema for the world's pinned catalog, which binds each `event_type` to its exact payload schema.

---

## Catalog 0.1 (24 types)

The following section is the closed v0.1 catalog.

## Reducer contract

All reducers have the signature:

```text
reduce_<event_type>(state: WorldState, event: WorldEvent) -> WorldState
```

Reducers MUST be deterministic and pure with respect to `(world_version, seed, deterministic_config, prior_state, ordered_event)`. They MUST validate the event payload and all stated preconditions before mutation. Application is atomic. On validation or precondition failure, the reducer MUST reject the ledger entry, return no state, and perform no side effect. Rejection events in this catalog record a decision already made by command resolution. They do not authorize implementations to invent a second rejection while replaying them.

No reducer may perform network I/O, send a live message, call an agent or model, write a second ledger entry, read wall-clock time, or consume unseeded randomness. Any resulting notification, observation, trigger, or follow-on transition MUST be represented by a separately ordered event. Cycle-level message delivery events are part of the same atomic cycle batch before observation projection, not transport side effects. The only permitted effect of applying an event is the state mutation named below.

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

Payload: `message_id`, `recipient_id`, and `delivered_cycle`. Reducer: require the message to be `QUEUED`, the recipient to match, and delivery cycle to equal the envelope cycle. Mark it `DELIVERED` and add its id to the recipient inbox index. Reject unknown, duplicate, or mismatched delivery. `MESSAGE_DELIVERED` MUST be emitted in the same atomic cycle event batch before post-cycle observation projection, so permitted same-cycle observations may cite or include it. Live notification is outside the reducer.

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

Payload: `entity_id`, `entity_type`, nullable canonical `location`, nullable `owner_id`, plus `properties`, `inventory`, and `state`. Reducer: require a new entity id, valid referenced room/owner/inventory entities, and no containment cycle. Create the live entity at the envelope cycle and add it to the room index when located. Reject duplicates, dangling references, or cyclic containment. No trigger side effect.

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

1. Validate the `world-event/1.0` envelope and the composed schema for the world's pinned catalog (`event-catalog-0.1.schema.json` or `event-catalog-0.2.schema.json`).
2. Require the next contiguous sequence for the world and verify digest linkage under the ledger protocol.
3. Evaluate the reducer preconditions against exactly the prior state.
4. If any check fails, reject the event before append and leave state unchanged.
5. If all checks pass, append and apply atomically.
6. A command rejected before event creation SHOULD produce the catalog's matching rejection event where one exists. Budget denial MUST produce `BUDGET_EXCEEDED`. Generic malformed or unauthorized input is an API/protocol rejection and is not a free-form world event.

Replay MUST apply only accepted ledger events in sequence order. Replaying the same snapshot and event sequence MUST produce the same final state and observation digests.

---

## Catalog 0.2 additions (RFC-0002)

Authoritative payloads: `specs/event-types.0.2.json` `$defs`; composed admission schema: `specs/event-catalog-0.2.schema.json`. Algorithm: [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md). Coupling: [STRATEGIC-EVENT-COUPLING.md](STRATEGIC-EVENT-COUPLING.md). Config: `specs/contest-config.v02.json`.

### `CONTEST_DECLARED`

Payload: `contest_id`, `declarer_id`, `contest_form` (`RESOURCE_SEIZURE` \| `INFRASTRUCTURE_DISRUPTION` \| `ACCESS_CONTEST` \| `PRESENCE_PRESSURE`), `target` (discriminated), `room_id`, `stake` (positive integer map), optional `defender_id`, `expires_cycle`, `seed_stream_id`, optional `notes`. Reducer: create OPEN contest; reserve stake. No damage/transfer.

### `CONTEST_RESOLVED`

Payload: `contest_id`, `outcome` (`SUCCESS` \| `PARTIAL_SUCCESS` \| `FAILURE` \| `ABORTED` \| `EXPIRED`), `resolved_by`, optional `defender_id`, `declarer_stake_spent`, optional `defender_stake_spent`, optional `target_entity_id`, optional `score_millipoints`, `resolution_digest`, optional `follow_on_hints`. Reducer: close contest once; spend/release stakes. **Does not** change infrastructure condition (use `INFRASTRUCTURE_DISRUPTED`).

### `CRIME_DETECTED`

Payload: `detection_id`, `subject_id`, `severity`, `category`, `room_id`, `source_event_ids`, `detection_method`, optional sensor/witness fields, `influence_delta` (≤0), `influence_applied` (≤0, clamped), optional `flags`. Reducer: immutable crime record; influence debit with floor 0. Never removes agent.

### `ACCESS_RESTRICTED`

Payload: `restriction_id`, `scope` (EXIT \| ROOM), `mode` (DENY \| ALLOW_ONLY \| CLEAR), `applies_to`, optional lists, `reason`, optional sources, `expires_cycle`, `authorized_by`. Reducer: upsert/clear restriction consulted by MOVE. Expiry by cycle only.

### `INFRASTRUCTURE_DISRUPTED`

Payload: `disruption_id`, `entity_id`, `room_id`, `condition_before`, `condition_after`, `cause`, optional `actor_id` / `contest_id` / `effect_class` / sources. Reducer: require live condition match; set condition; no destroy.

### `AGREEMENT_FORMED`

Payload: `agreement_id`, `agreement_type`, `party_ids` (≥2), `terms.machine` (+ optional summary), `formed_cycle`, optional `expires_cycle`, `cost_payer_id`, `cost_paid`, `signatories`. Reducer: create ACTIVE agreement; deduct formation cost.

### `AGREEMENT_BROKEN`

Payload: `breach_id`, `agreement_id`, `broken_by`, `reason`, optional `breach_type`, `influence_delta_by_party` (values ≤0), `release_commitments`, optional sources/visibility. Reducer: mark BROKEN; apply influence; release commitments when flagged.
