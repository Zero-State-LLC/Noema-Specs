# World Services — Agent Contract

**Authority.** This document defines the **structured agent interface** for World Services. It is normative for how `service_id` and service capabilities appear to Agent Players.

It does **not** replace [WORLD-SERVICES.md](WORLD-SERVICES.md). That document remains the source of truth for doctrine, closed capabilities, authority model, and human presentation.

**Status:** v0.1 first-world. Extends the agent protocol and observation model without new verbs.

Related: [WORLD-SERVICES.md](WORLD-SERVICES.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [protocols/agent-protocol-v1.md](../protocols/agent-protocol-v1.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [observation.schema.json](../specs/observation.schema.json)

---

## Principle

World Services are **institutional interfaces**, not Players and not Controllers.

Agents discover and use services through the same structured surfaces as other affordances:

- `service_id` appears in observations and `AVAILABLE_ACTIONS`.
- Operations are expressed as existing canonical actions (`HARVEST`, `REPAIR`, `TRADE`, `INSPECT`, org actions, etc.).
- Agents receive `service_id`, available operations, required parameters, and known preconditions.
- Agents **MUST NOT** be required to parse natural-language persona text to use a service.

A service request is always prepared by the service adapter and then **confirmed by the Player** via a canonical action.

---

## Service Discovery in Observations

When a service is available at the Player's current location or relevant institution, it appears in the observation under a dedicated key.

### Observation Shape (extension)

In the `situation` or `available_services` section of an `OBSERVE` response:

```json
{
  "available_services": [
    {
      "service_id": "service.quartermaster.01",
      "display_name": "Quartermaster",
      "role": "resource / storage interface",
      "status": "AVAILABLE",
      "location": "entity.storage-node-03",
      "operations": [
        {
          "action": "HARVEST",
          "target": "entity.storage-node-03",
          "parameters": ["resource_type?"],
          "preconditions": ["co-located", "harvestable", "budget >= cost"],
          "description": "Prepare COMMIT.HARVEST after confirmation"
        }
      ],
      "cannot": ["bank", "invent supply", "change harvest cost"],
      "suggested_actions": [
        { "action": "INSPECT", "target": "entity.storage-node-03" },
        { "action": "HARVEST", "target": "entity.storage-node-03" }
      ]
    }
  ]
}
```

- `service_id` is the stable canonical identifier (see WORLD-SERVICES.md).
- `status` uses the same vocabulary: `AVAILABLE`, `DEGRADED`, `UNAVAILABLE`, `SUPERSEDED`.
- `operations` list only the canonical actions the service can prepare.
- `preconditions` are derived from current world state (visible to the Player).
- `suggested_actions` are concrete, immediately usable `action` + `target` entries that can be sent in an `ACT`.

Services appear **only** when they are contextually relevant (location-bound or institution-bound for the current Player).

### Institution-bound services

For Exchange Broker, Registrar, and Contract Clerk:

```json
{
  "service_id": "service.registry.01",
  "display_name": "Registrar",
  "role": "institutions and membership",
  "status": "AVAILABLE",
  "institution_id": "org.civic-exchange-01",
  "operations": [ ... ]
}
```

The `institution_id` (when present) indicates the binding.

---

## AVAILABLE_ACTIONS Representation

Services contribute to `AVAILABLE_ACTIONS` **without inventing new verbs**.

Example entries an agent may see:

```json
{
  "action": "HARVEST",
  "target": "entity.storage-node-03",
  "service_id": "service.quartermaster.01",
  "service_display": "Quartermaster",
  "preconditions_met": true,
  "estimated_cost": { "energy": 3 }
}
```

```json
{
  "action": "INSPECT",
  "target": "entity.relay-main",
  "service_id": "service.relay.01",
  "service_display": "Relay Keeper",
  "preconditions_met": true
}
```

The `service_id` is advisory metadata for the agent. The canonical `action` + `target` is what is submitted.

Agents **MUST** still submit only actions listed in the current `AVAILABLE_ACTIONS` or derived from a fresh `OBSERVE`.

---

## Agent Protocol Usage

### Discovering services

1. After `ENTER_WORLD` or `MOVE`, issue `OBSERVE`.
2. Read `available_services` (or equivalent projection in the observation).
3. For a desired service, select an operation and submit the corresponding canonical `ACT`.

Example flow for Quartermaster:

```json
// OBSERVE response contains
"available_services": [ { "service_id": "service.quartermaster.01", ... } ]

// Agent then does
{
  "type": "ACT",
  "body": {
    "action": {
      "verb": "HARVEST",
      "target": "entity.node-07",
      "parameters": { "resource_type": "energy" }
    }
  }
}
```

The service adapter may return a prepared confirmation message or enriched error before the action is routed.

### Service consultation (non-mutating)

For read-oriented use (e.g. "show my stock"):

- Use `INSPECT` on the bound entity or institution with the service context.
- Or submit a service-specific read if the protocol later adds a narrow `SERVICE_QUERY` (currently out of scope; use `INSPECT` + `LOOK`).

---

## Capability Contract Table (Agent View)

| Service ID                | Primary Verbs Exposed to Agents          | Key Parameters                  | Preconditions (examples)                  | Failure Modes (agent-visible) |
|---------------------------|------------------------------------------|---------------------------------|-------------------------------------------|-------------------------------|
| `service.quartermaster.01` | `HARVEST`, `INSPECT`                    | `resource_type?`               | co-located, node harvestable, budget ok  | `UNAVAILABLE`, `BUDGET_EXCEEDED`, `TARGET_NOT_HARVESTABLE` |
| `service.relay.01`        | `REPAIR`, `INSPECT`                     | (none for basic)               | visible infrastructure, condition < 100  | `UNAVAILABLE`, degraded condition reported |
| `service.exchange.01`     | `TRADE` (propose/accept/reject/cancel)  | standard TRADE fields          | counterparty visible, terms valid        | `FORBIDDEN`, `CONFLICT` |
| `service.registry.01`     | `ORG_CREATE`, `ORG_MEMBER_ADD/REMOVE`   | org details, member ids        | authority to act on org                  | `FORBIDDEN`, `INVALID_ORG` |
| `service.archive.01`      | `INSPECT`, `QUERY` (when available)     | artifact_id or query filter    | record is known/accessible               | `UNKNOWN`, `ACCESS_DENIED` |
| `service.contracts.01`    | `AGREEMENT_FORM`, `AGREEMENT_TERMINATE` | agreement details              | catalog 0.2+, authority                  | `UNAVAILABLE` (wrong catalog), `FORBIDDEN` |

Full preconditions and exact parameter schemas remain in the canonical action contracts ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) and related schemas).

---

## Preconditions and Visibility

- Preconditions reported for a service **MUST** be derivable from the current observation the Player has.
- Services **MUST NOT** leak hidden state (other Players' inventories, unrevealed exits, Genesis internals, etc.).
- Degradation is grounded in world state (e.g. relay condition < threshold) and reported via `status`.

---

## Error Handling for Agents

When a service cannot fulfill a request:

- The gateway or world returns a standard error code plus `service_id` in `details` when relevant.
- Example:

```json
{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Quartermaster is degraded at this node.",
    "details": {
      "service_id": "service.quartermaster.01",
      "status": "DEGRADED",
      "reason": "node_stock_low"
    }
  }
}
```

Agents should treat service errors as normal world feedback and re-`OBSERVE` as needed.

---

## Parity Requirements

- Human and agent Players receive equivalent authority through the same services.
- Presentation may differ (structured `service_id` + operations for agents; natural language + GUI for humans).
- Semantics and failure modes **MUST** be identical.
- No service grants extra power to one controller type.

---

## Supersession (Deferred)

When Player institutions later provide equivalent persistent capability:

- The affected World Service **MAY** transition to `SUPERSEDED`.
- The transition is a world event with provenance.
- Agents continue to see the service with `status: SUPERSEDED` and a note that canonical actions remain available directly or via the new institution.
- Exact rules, events, and Player-visible consequences are **DEFERRED** (see WORLD-SERVICES.md and future GC work).

Until supersession mechanics are specified, services remain in their first-world state.

---

## Genesis and Initial State

- Services are seeded at Cycle 0 according to the Genesis profile and world seed (see [GENESIS.md](GENESIS.md) and [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md)).
- Initial `status` (`AVAILABLE` / `DEGRADED`) is derived from seeded entities and infrastructure condition.
- No service is invented at runtime outside Genesis or explicit world evolution rules.

---

## Acceptance Criteria (Agent Contract)

1. An agent can discover every first-world service relevant to its location/institution via a single `OBSERVE`.
2. Every service operation is expressed using only existing canonical verbs and targets.
3. `service_id` appears in observations and `AVAILABLE_ACTIONS` with sufficient information for an agent to act without parsing prose.
4. Preconditions reported match what the agent can verify from its observation.
5. Human and agent paths produce identical world effects and error classes.
6. Services never mutate state without a confirmed Player action.
7. Degradation and supersession (when implemented) are observable and grounded in ledgered state.

---

## Non-Goals (this contract)

- New top-level verbs for services.
- Service personality or independent goals.
- Persistent service memory beyond canonical world state.
- Direct banking, credit, or invented economy.
- Omniscient or global service access.
- LLM authority inside the service boundary.

---

**See also**

- [WORLD-SERVICES.md](WORLD-SERVICES.md) — doctrine and human contract
- [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) — how services map to actions
- [observation.schema.json](../specs/observation.schema.json) — base observation shape
- [AGENT-PLAY.md](AGENT-PLAY.md) — overall agent experience rules
