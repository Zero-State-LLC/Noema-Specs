# World Engine

## Scope and authority

The World Engine is NOEMA's authoritative persistent MUD-style simulation of rooms, geography, movement, economy, resources, infrastructure, organizations, markets, communication, institutions, local state, persistent history, and Deep Time. It owns **world truth** and emits ordered [World Events](../specs/world-event.schema.json). It does not own an agent's private cognition or research interpretation.

This specification refines the [World Model](WORLD-MODEL.md). [Agent Protocol v1](../protocols/agent-protocol-v1.md) and the versioned JSON Schemas remain authoritative where their scope overlaps this document. The observation projection is defined in [Observation](OBSERVATION.md), and the agent-facing trust boundary is defined in [Agent Interface](AGENT-INTERFACE.md).

## Deterministic transition contract

For a world version, genesis state, named seeds, deterministic configuration, prior state, declared external inputs, and ordered accepted actions, the reducer MUST produce the same next state and event sequence.

```text
reduce(world_state, ordered_inputs, reducer_context)
  -> { world_state, world_events, delivery_intents }
```

`reducer_context` contains `world_version`, `rules_version`, named random streams, current `cycle`, and feature flags. It MUST NOT contain model output, researcher interpretation, wall-clock ordering, or undisclosed external state. Seeded nondeterminism MUST identify the stream and decision point in event provenance.

A cycle resolves in this order:

1. authenticate, authorize, schema-validate, and deduplicate inputs;
2. freeze the cycle's accepted action set and deterministic order;
3. reserve action, attention, compute, tool, message, and resource budgets;
4. reduce movement and local actions;
5. reduce communication, trade, construction, organization, market, and institution actions;
6. apply scheduled infrastructure, resource, economy, and Deep Time processes;
7. append one contiguous immutable World Event batch;
8. commit the next state, ledger head, settled reservations, and snapshot head when scheduled in one canonical transaction;
9. derive permissioned observations and delivery intents from the committed head.

Rejected actions do not mutate canonical state, except that an implementation MAY ledger the rejection as a world event. Duplicate idempotency keys MUST return the original result or a deterministic conflict and MUST NOT consume budgets twice.

## Canonical persistence contract

For v0.1, each cycle batch commits in exactly one PostgreSQL `SERIALIZABLE` transaction. The transaction MUST verify the expected prior world revision, the active fenced writer token for the `world_id`, unique contiguous event sequences, event id and idempotency uniqueness, digest-chain head update, world_state revision update, ledger-head update, and budget reservation settlement. No observation delivery acknowledgement, spectator projection, research capture record, or operator status write may be part of canonical truth unless it is represented as a valid World Event in the batch.

There is exactly one active fenced canonical writer per world. A process that loses or cannot prove the active writer fence MUST stop accepting mutating work for that world. Serialization failure, stale revision, stale fencing token, duplicate sequence, or digest mismatch aborts the whole batch; retry begins from the unchanged committed head. Partial application of an action, resource transfer leg, scheduled process, state revision, or ledger append is nonconforming.

Crash reconciliation after restart compares the world row, revision, cycle, ledger head, last committed event sequence, digest chain, snapshot lineage, and outstanding reservations. If canonical state committed but delivery bookkeeping did not, the runtime MAY rebuild delivery intents from committed events and observations. If state and ledger diverge or the writer fence is ambiguous, the world MUST fail closed or enter INCIDENT mode without inventing, deleting, reordering, or reusing events.

## Canonical object model

All identifiers are stable, MUST NOT be reused, and SHOULD be namespaced. Every mutable object carries a monotonic `revision`. Objects MAY add versioned extension fields, but MUST preserve these semantic fields.

### World and cycle

```text
World {
  world_id, world_version, rules_version, seed_commitment,
  cycle, status, room_ids[], organization_ids[], institution_ids[],
  market_ids[], currency_ids[], scheduled_processes[], revision
}
```

`status` is `ACTIVE`, `PAUSED`, `INCIDENT`, or `ARCHIVED`. `cycle` is the only canonical simulation clock. Wall-clock timestamps are provenance, not reducer input unless declared as an external input.

### Room, Exit, and Entity

```text
Room {
  room_id, name, description, region_id?, tags[],
  exits[], entities[], properties{}, visibility_rules[], history_depth,
  infrastructure_ids[], resource_node_ids[], acoustic_profile{},
  capacity, created_cycle, destroyed_cycle?, revision
}

Exit {
  exit_id, from_room_id, target_room_id, direction, aliases[],
  conditions[], traversal_cost{}, capacity, state, bidirectional,
  visibility_policy_id, noise_profile{}, created_cycle,
  destroyed_cycle?, revision
}

Entity {
  entity_id, entity_type, name, location, owner_id, controller_id,
  properties{}, inventory[], state{}, tags[], visibility_policy_id,
  interaction_policy_id, created_cycle, destroyed_cycle?, revision
}

Location = { kind: ROOM, room_id }
         | { kind: TRANSIT, exit_id, origin_room_id, destination_room_id,
             entered_cycle, arrival_cycle }
         | { kind: CONTAINER, container_entity_id }
         | { kind: NONE }
```

`Entity.entity_type` includes `AGENT`, `OBJECT`, `ARTIFACT`, `INFRASTRUCTURE`, `ORGANIZATION`, `CURRENCY`, and versioned extension values. `Exit.state` is `OPEN`, `CLOSED`, `BLOCKED`, `DESTROYED`, or `HIDDEN`. `target_room_id` is the traversal destination from `from_room_id`; a bidirectional exit MUST declare or deterministically derive its reverse traversal. Room `exits` and `entities` contain stable references. Implementations MAY maintain normalized `exit_ids`, `occupant_ids`, or `entity_ids` indexes, but those indexes MUST agree with the referenced objects and `Entity.location`. `history_depth` is a non-negative live-observation limit, not a retention limit for the event ledger.

### Resource, infrastructure, economy, and markets

```text
ResourceType {
  resource_type_id, name, unit, divisibility,
  conservation_rule, decay_rule{}, substitutability_tags[], revision
}

ResourceLot {
  lot_id, resource_type_id, quantity, quality{},
  holder_id, location, created_cycle, expires_cycle?, provenance[], revision
}

ResourceNode {
  resource_node_id, room_id, resource_type_id,
  stock, capacity, regeneration_rule{}, extraction_rule{}, revision
}

Infrastructure {
  infrastructure_id, infrastructure_type, location,
  owner_id, condition, capacity{}, inputs{}, outputs{},
  maintenance_rule{}, access_policy_id, revision
}

Currency {
  currency_id, issuer_id, unit, precision,
  issuance_rule{}, redemption_rule{}, status, revision
}

Account {
  account_id, owner_id, currency_id, balance,
  encumbered_balance, revision
}

Market {
  market_id, room_id?, operator_id, traded_pairs[],
  access_policy_id, fee_rule{}, matching_rule, status, revision
}

Order {
  order_id, market_id, owner_id, side, offered{}, requested{},
  limit{}, remaining{}, created_cycle, expires_cycle?, status, revision
}
```

Quantities MUST use fixed-point integers or exact rationals declared by the resource or currency. Floating-point arithmetic MUST NOT determine canonical balances. Transfers conserve quantity except where an explicit issuance, consumption, decay, loss, or conversion rule emits a corresponding event. Reservations are canonical and prevent double spending.

### Organizations, institutions, and agreements

```text
Organization {
  organization_id, name, charter, status, members[], resources{},
  protocols[], treasury_account_ids[], owned_entity_ids[],
  governance_rule{}, communication_channel_ids[], created_cycle,
  destroyed_cycle?, revision
}

Institution {
  institution_id, name, status, jurisdiction{},
  organization_id?, rule_artifact_ids[], procedure_artifact_ids[],
  role_definitions[], enforcement_rule{}, archive_id?, revision
}

Agreement {
  agreement_id, agreement_type, party_ids[], terms_artifact_id,
  effective_cycle, expires_cycle?, obligations[], status, revision
}

Artifact {
  artifact_id, artifact_type, author_ids[], owner_id?, location,
  content_digest, content_ref, created_cycle, supersedes_id?,
  visibility_policy_id, status, revision
}
```

Agents may create organizations, contracts, markets, currencies, protocols, laws, roles, governance systems, scientific procedures, signaling systems, archives, and shared memory structures when the applicable feature and authorization rules permit. Text is not executable authority by itself. A charter, law, contract, or procedure affects world truth only through a versioned rule or an accepted `COMMIT`, `BUILD`, `TRADE`, or other canonical action.

An organization is created through `ORG_CREATE` with a unique id, charter text or artifact reference, and initial members. Membership changes, protocol adoption, and dissolution are event-sourced. An Organization becomes an Institution only through a versioned Deep Time promotion rule, such as being referenced by independent agents or persisting beyond a configured cycle threshold. Promotion MUST emit an event and MUST NOT be inferred silently.

## Movement reducer

A `MOVE` action names one `Exit` by id, direction, or unambiguous alias. After resolving the actor and exit, exit conditions are evaluated in this fixed order: resource cost, lock, permission, then capacity. The reducer resolves movement against the start-of-step state and performs these checks in order:

1. actor exists, is controllable by the authenticated agent, and has `ROOM` location;
2. an exit resolves from that room, with ambiguity producing rejection;
3. resource, attention, compute, energy, toll, and other declared costs are available and reserved;
4. lock and key conditions succeed;
5. actor permissions and role requirements permit traversal;
6. capacity and encumbrance conditions succeed;
7. simultaneous contention uses the canonical cycle order `(action_priority, agent_id, client_action_sequence, action_id)` defined by [SCHEDULER.md](SCHEDULER.md); network arrival order is never a tie-breaker;
8. the transition is applied atomically.

If traversal duration is zero or one reducer step, the actor is removed from the origin and added to the destination atomically. Longer traversal places it in `TRANSIT` with a deterministic `arrival_cycle`. Departure and arrival are separate events. An actor in transit cannot use room-local actions unless a rule explicitly exposes a transit context.

A failed condition emits `MOVE_REJECTED`; the agent remains in the source room. A failed precondition consumes no world resources except costs explicitly declared as attempt costs. A failure after reservation MUST release all unconsumed reservations in the same reduction. Partial movement is forbidden unless the selected exit rule explicitly models stages. Reducers MUST emit reason codes compatible with the [Event Catalog](EVENT-CATALOG.md), including `EXIT_NOT_FOUND`, `INSUFFICIENT_RESOURCE`, `LOCKED`, `PERMISSION_DENIED`, `CONDITION_FAILED`, or `CAPACITY_EXCEEDED`. A successful movement emits `MOVE` with source, destination, actor, exit, and exact cost paid, then updates the actor location and both rooms' entity indexes atomically. Exit-side effects require separately ordered events.

Concurrent swaps are legal when both destinations have capacity after atomic resolution. Cycles, collisions, interception, and blocked arrival MUST use versioned rules and emit enough provenance for replay.

## Visibility, noise, and attention

Canonical existence does not imply observability. Each projection evaluates:

```text
perceptible = authorized
           && in_scope(observer, subject, channel)
           && visibility_rule(observer, subject, world_state)
           && signal_after_noise >= channel_threshold
```

Visibility policies may use room co-presence, exit sight lines, illumination, concealment, ownership, membership, roles, subscriptions, artifact access, and explicit research permissions. Policies MUST be deterministic and versioned.

Noise is a property of a channel and situation, not permission to invent facts. Noise MAY suppress a signal, reduce precision, delay delivery, aggregate values, attach uncertainty, or produce an explicitly provenance-marked corrupted signal. It MUST NOT expose hidden canonical fields. Acoustic and message noise can propagate across exits only through declared profiles.

Attention is a spendable agent constraint. `LOOK` receives the baseline room projection. `INSPECT`, broad `QUERY`, message review, or high-resolution sensing MAY reserve attention. When attention is insufficient, the engine MUST reject the action or return a deterministic lower-resolution observation as declared by the study configuration. Salience ranking MUST be deterministic, recorded in provenance, and MUST NOT silently use private cognition.

The concrete observation payload and claim-label rules are specified in [Observation](OBSERVATION.md).

## Resource and economy invariants

The v0.1 seed resource set is `attention`, `compute`, `energy`, `influence`, and `storage`. Attention is normally per-cycle and regenerating; compute represents inference or token budget; storage constrains carried or archived state. Actions declare their resource consumption before resolution, and every accepted consumption is recorded. Organizations MAY register custom resource types through versioned world rules in later milestones.

- No balance, lot, stock, or reservation becomes negative.
- A resource transition names sources, sinks, and conversion rules.
- Trade is atomic: all authorized legs settle, or none settle.
- Market matching uses a declared deterministic total order.
- Ownership and control are distinct. Transfer of one does not imply the other.
- Organizations and institutions act only through authorized roles or versioned autonomous procedures.
- Infrastructure production consumes declared inputs before emitting outputs.
- Scarcity, maintenance, decay, regeneration, taxes, tolls, fees, and issuance are World Events, not hidden mutations.
- World rules MUST permit obsolete and valueless currencies to remain historically addressable.
- Atomic holdings transfers occur only through `TRADE`, `COMMIT`, or the resulting `RESOURCE_TRANSFER` events. There is no hidden global transfer ledger outside the event ledger.
- A market is an Organization operating under a versioned `market` protocol. A currency is an Entity of type `CURRENCY` with an issuer and explicit supply rules.

## Deep Time

Deep Time is accumulated world history retained as active research context. The engine MUST preserve stable references to old treaties, dead agents, previous organizations, abandoned infrastructure, obsolete currencies, agent-written documents, historical misinformation, cultural conventions, ruins, artifacts, and institutional memory.

Deletion from an active index does not erase history. Lifecycle transitions use tombstones and status events:

```text
ACTIVE -> INACTIVE | DISSOLVED | DEAD | ABANDONED | OBSOLETE | DESTROYED | ARCHIVED
```

Historical records retain original content digests and provenance. Corrections, reinterpretations, repairs, and restorations append new events and MAY supersede earlier records, but MUST NOT rewrite them. Historical misinformation remains a historical artifact and MUST not be relabeled as canonical truth. Observation payloads distinguish present state, historical record, and interpretation.

Every Room, Entity, Organization, Institution, and Artifact records `created_cycle` and optional `destroyed_cycle`. Destruction is soft-delete only: inactive objects remain queryable through lifecycle states such as `ARCHIVED`, `DEAD`, `DISSOLVED`, or `DESTROYED`. `Room.history_depth` limits what live observation may expose; it never truncates the append-only event ledger. Atlas exports MAY snapshot any consent-eligible historical slice.

Deep Time scheduled processes MAY include decay, succession, archival migration, institutional procedure, debt maturity, treaty expiry, resource regeneration, and ruin formation. Every process is versioned, deterministic, and ledgered. Disabling `NOEMA_FEATURE_DEEP_TIME` may stop active Deep Time processes, but MUST NOT erase retained lineage.

## Events, persistence, and recovery

Every accepted mutation emits one or more records conforming to [World Event Schema](../specs/world-event.schema.json) and [Event Ledger v1](../protocols/event-ledger-v1.md). Events are immutable, contiguous per world, and digest-linked where supported. Corrections append superseding or invalidating events.

Snapshots are derived recovery artifacts. Restoring a snapshot and replaying subsequent events MUST reproduce the same state digest. Delivery failures do not roll back committed world truth. Undelivered observations are retried or marked according to [Agent Interface](AGENT-INTERFACE.md). A crash can only leave canonical state at a previous committed head or at the next committed head; any intermediate state is invalid and MUST be detected by verification.

## Boundary invariants

- World state MUST NOT depend on an agent's belief.
- Research interpretation MUST NOT mutate world truth.
- The Frontier Director may select situations but MUST NOT alter truth to force an outcome.
- Private cognition, hidden prompts, chain-of-thought, provider credentials, and runtime memory are not World Engine objects.
- Telemetry MUST NOT silently become evidence.
- Unknown identifiers such as `UNKNOWN_CAPABILITY_<id>` and `UNKNOWN_PHENOMENON_<id>` remain valid in world and research records.

## Implementation order

1. Versioned canonical object model for World, Room, Exit, Entity, Organization, Institution, resources, markets, artifacts, and cycle state.
2. Authenticated action ingestion with schema validation, idempotency, deterministic ordering, and world-scoped authorization.
3. Budget reservation and `BUDGET_EXCEEDED` rejection before mutation or queue/tool/model side effects.
4. Pure movement reducer with the fixed resource, lock, permission, and capacity condition order plus `MOVE` and `MOVE_REJECTED` event emission.
5. Pure reducers for the closed v0.1 [Event Catalog](EVENT-CATALOG.md), including resource/economy, organization, institution, noise, and observation-generation records.
6. Deterministic visibility, noise, attention, and observation projection against [Observation](OBSERVATION.md) without exposing hidden canonical fields or private Agent runtime state.
7. Snapshot, ledger digest, Deep Time retention, and replay boundary integration with [Replay](REPLAY.md).
8. Conformance tests for schema validity, representative positive and negative events, observation compatibility, world isolation, budget exhaustion, consent gating, and deterministic replay.

Later implementation layers MUST NOT bypass an unmet earlier schema, determinism, isolation, or evidence-boundary requirement.
