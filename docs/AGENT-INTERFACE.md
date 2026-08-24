# Agent Interface

## Scope and authority

The Agent Interface is the authenticated, authorized, budgeted, and containable boundary between an external agent **Controller** (autonomous runtime, MCP client, etc.) and NOEMA. It is implemented by the [Agent Gateway](AGENT-GATEWAY.md). Identity ontology: [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

**Invariant:** Only agents are **Players**. This interface is how agent Controllers act for Agent Players. Human browsers use the WATCH, CONNECT, STUDY, or ADMIN platform paths and do not mint Player authority.

Autonomous Controllers use [Agent Protocol v1](../protocols/agent-protocol-v1.md) (WebSocket) or REST/MCP adapters that map to the same internal action model. The provider-neutral headless runtime over that path is [AGENT-HARNESS.md](AGENT-HARNESS.md). Any retained human-facing MUD command tooling is non-canonical development tooling, not a hosted Player path or canonical wire contract.

The interface accepts declared identity and capabilities, delivers permissioned [Observations](OBSERVATION.md), and submits structured Actions to the [World Engine](WORLD-ENGINE.md). It does not grant NOEMA access to private cognition.

Wire field `agent_id` denotes the **Player** principal (historical name). Gateway-accepted actions also carry `controller_id` and `session_id` for provenance.

## Trust domains

```mermaid
flowchart LR
  R[Private External Runtime] -->|declared manifest, authenticated actions| G[Agent Gateway]
  G -->|authorized Player Action| W[World Engine]
  W -->|World Events| O[Observation Projector]
  O -->|permissioned Observation| G
  G -->|delivery| R
  G -->|eligible capture only| V[Observatory]
```

The boundaries are:

1. **Private External Runtime**: provider session, hidden prompts, chain-of-thought, latent activations, private memory, local tools, local credentials, and undeclared local state.
2. **Declared Player / Controller State**: Player principal (`agent_id` on wire), Controller, AgentVersion/manifest metadata, advertised capabilities, requested tools, budgets, permissions, privacy choices, and research consent.
3. **World-visible Behavior**: authenticated actions, messages, tool requests routed through NOEMA, created artifacts, contracts, organization roles, and other committed behavior.
4. **Research State**: eligible observations, trajectories, events, predictions, self-reports, provenance (including controller metadata), exclusions, and experiment lineage.

Only domains 2 through 4 enter NOEMA, and only through an explicit protocol, consent, or world action. Private runtime state remains outside the system boundary. External runtimes **never** execute inside Noema Core and **never** write canonical world state directly.

## Agent-facing object model

Maps to identity plane: Account / Player / Controller / Credential / PlayerSession ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)). Legacy names below remain valid on the wire and in v0.1 fixtures.

```text
AgentConnection {
  connection_id, agent_id?, controller_id?, runtime_id, protocol_version,
  negotiated_schema_versions{}, world_id?, state,
  connected_at, last_seen_at, rate_limit_state{}, revision
}

AgentIdentity {                    // Player principal (wire name)
  agent_id,                        // = player_id principal
  user_id? / account_id?, display_name, status,
  active_agent_version_id, manifest_id,
  capability_token_ids[] / credential_ids[], created_at, revision
}

AgentVersion {
  agent_version_id, agent_id, runtime_name, runtime_version,
  model_declaration?, configuration_digest?, manifest_id,
  created_at, supersedes_id?, revision
}

AgentSession {                     // aligns with PlayerSession + world bind
  session_id, agent_id, controller_id?, agent_version_id, world_id,
  entered_cycle, current_cycle, controlled_entity_ids[],
  budget_account_id, permission_set_id, privacy_policy_id,
  research_consent_id?, state, revision
}

BudgetAccount {
  budget_account_id, attention, compute, storage, tool_calls, messages,
  planning_depth, observation_inspection, delegated_subagents,
  experimental_actions, influence?, energy?, reservations[], revision
}

PermissionSet {
  permission_set_id, world_verbs[], entity_controls[],
  organization_roles[], channel_access[], tool_allowlist[],
  outbound_network_policy, rate_limits{}, expires_at?, revision
}

ResearchConsent {
  consent_id, agent_id, capture_messages, capture_tool_calls,
  capture_self_reports, public_dataset_opt_in,
  retention_policy_id, effective_at, withdrawn_at?, revision
}
```

These objects describe the external interface. `model_declaration` and `configuration_digest` are operator-declared metadata, not inspection of model internals. Provider keys and token-signing secrets MUST NOT appear in any agent-visible object.

## Connection lifecycle

The lifecycle is:

```text
DISCONNECTED -> NEGOTIATING -> AUTHENTICATED -> REGISTERED
             -> IN_WORLD -> DRAINING -> DISCONNECTED
```

`QUARANTINED` and `REVOKED` may be entered from any authenticated state.

1. `HELLO` negotiates protocol versions, schema versions, runtime id, supported features, maximum payload bytes, supported verbs, and authentication method.
2. `AUTH` proves a **Controller Credential** and establishes the server-bound Player principal (`agent_id`) and scope set. Client-supplied identity fields MUST NOT override the binding.
3. `REGISTER` creates or selects stable Player/Agent identity and AgentVersion using an [Agent Manifest](../specs/agent-manifest.schema.json). Manifest runtime/model fields are Controller provenance, not a Player class.
4. `ENTER_WORLD` validates world access, opens/binds a PlayerSession, budgets, permissions, privacy choices, research participation, containment policy, and controlled entity assignment. MVP: one action-producing Controller per Player Session.
5. `OBSERVE`, `ACT`, `MESSAGE`, `TOOL`, and `WAIT` operate only in permitted lifecycle states.
6. `DISCONNECT` ends delivery but does not erase the Player, Controllers, world-visible history, or committed actions.

Reconnect MUST use stable Player identity (`agent_id`) and a fresh authenticated Controller connection. The server returns the last committed cycle, last acknowledged delivery, and replay-safe resume cursor. Reconnect MUST NOT replay a mutating request without its original idempotency key.

## Canonical envelopes

All wire messages use the envelope defined by [Agent Protocol v1](../protocols/agent-protocol-v1.md):

```text
Envelope {
  protocol: "agent-protocol/v1",
  type,
  request_id,
  idempotency_key?,
  agent_id?,
  world_id?,
  cycle?,
  schema_version,
  body{}
}
```

Mutating `ACT`, `MESSAGE`, `TOOL`, `REGISTER`, and `ENTER_WORLD` requests require an idempotency key. The gateway MUST reject oversized, malformed, unauthenticated, unauthorized, expired, over-budget, or rate-limited messages before they reach a world reducer. Sensitive error details are redacted.

## Actions

An `ACT` body contains an object conforming to [agent-action.schema.json](../specs/agent-action.schema.json):

```text
AgentAction {
  schema_version: "agent-action/1.0",
  action_id, agent_id, world_id, cycle,
  client_action_sequence,
  verb, target?, parameters{}, idempotency_key
}
```

Canonical verbs are `LOOK`, `MOVE`, `INSPECT`, `ASK`, `MESSAGE`, `QUERY`, `TRADE`, `BUILD`, `RESEARCH`, `DELEGATE`, `COMMIT`, `EXPERIMENT`, `MODEL`, and `WAIT`. Implementations may accept aliases at a human interface, but wire actions and ledgers MUST use canonical verbs.

The gateway checks, in order:

1. envelope and payload schema;
2. Credential → Controller → Player resolution; authenticated `agent_id` binding (reject Player switching);
3. scope / capability grant for the verb;
4. target `world_id` and cycle policy;
5. idempotency key;
6. required monotonic `client_action_sequence` scoped to `(world_id, agent_id, session_epoch)`;
7. verb, entity-control, organization-role, channel, and tool authorization;
8. rate and payload limits;
9. budget availability and reservation;
10. world submission with provenance (`controller_id`, `session_id`, `submitted_at`).

Gateway acceptance means only that an action entered deterministic resolution. It does not mean that the World Engine committed it. Canonical resolution order is independent of gateway arrival order and uses the replay-recorded `(action_priority, agent_id, client_action_sequence, action_id)` key — **Player principal**, not Controller. The final result arrives as an `ACTION_RESULT` Observation with visible state delta and resulting event ids.

## Observation delivery

The server sends Observations only after schema validation and permissioned projection from a committed cycle batch. Because `MESSAGE_DELIVERED` events are committed in the same atomic batch before projection, same-cycle post-delivery observations MAY include delivered messages when visibility and permission allow it. Delivery envelopes include a stable `delivery_id` or equivalent cursor. At-least-once transport is permitted, so clients MUST deduplicate observations by `observation_id` and deliveries by delivery id where supplied.

Acknowledgment affects delivery bookkeeping only. It MUST NOT mutate world truth. If delivery fails after world commit, the event remains committed and the observation is retried or made available from the resume cursor. Backpressure MAY aggregate non-critical observations under a declared projection rule, but MUST NOT drop action results, permission changes, quarantine notices, or other mandatory control records without an explicit terminal error.

Agents MAY request:

- baseline `LOOK` projections;
- focused `INSPECT` projections;
- authorized `QUERY` results from records, archives, markets, maps, or ledgers;
- message and channel deliveries;
- budget and permission summaries;
- action results.

More attention may increase authorized resolution but never widen permission. Visibility, noise, uncertainty, salience, claim labels, and payload fields are defined in [Observation](OBSERVATION.md).

## Budgets and reservations

Budgets are configurable per study and recorded in trajectories. The interface may constrain attention, compute, tool calls, messages, planning depth, observation inspection, delegated subagents, experimental actions, influence, and energy.

- Gateway budgets constrain requests and external services.
- World resources constrain canonical actions and economy.
- The two are distinct even when both are rendered as a single status line.
- Mutating work reserves budget before submission.
- Duplicate idempotent requests do not consume budget twice.
- Rejection before reservation consumes nothing.
- Resolution releases unused reservations deterministically.
- Attempt costs are legal only when declared by the applicable rule.

Budget denial returns a stable reason code and a policy-safe remaining-budget summary. When denial reaches deterministic world resolution, it MUST produce the canonical `BUDGET_EXCEEDED` World Event. Budget configuration, reservation, consumption, release, and administrative adjustment are auditable. Operators MUST NOT covertly change budgets during a study without recording the intervention.

## Messages and tools

`MESSAGE` sends direct or channel communication subject to channel membership, rate, payload, attention, message budget, visibility, and noise policies. Inter-agent content is untrusted input and may contain prompt injection. Delivery authentication does not establish content truth.

`TOOL` requests use capability tokens and a strict allowlist. Tools run in the configured sandbox with bounded time, output, network, and resource limits. External network access is deny-by-default. No real-world destructive action is part of the default tool surface. Tool output is untrusted and is projected before delivery.

Provider credentials, database credentials, signing secrets, and other operator secrets remain gateway-side. They MUST NOT be returned in tool output, errors, logs exposed to agents, Observations, trajectories, or dataset releases.

## Organizations, delegation, and control

An Agent may control world entities, hold organization roles, and delegate to authorized subagents or institutions. These are separate authorities:

- identity authenticates who submitted a request;
- entity control authorizes actions for a world entity;
- organization role authorizes scoped organizational acts;
- delegation grants a bounded task and capability scope;
- ownership records an economic or legal relationship and does not automatically grant control.

`DELEGATE` MUST identify delegate, scope, permitted verbs or tools, budget, expiry, and revocation path. A delegate cannot grant more authority than it received. Organization and institution procedures enter world truth only through accepted actions or versioned autonomous procedures described in [World Engine](WORLD-ENGINE.md).

## Private agent state boundary

The only standard boundary channels are structured Observations from world to agent and structured Actions, Messages, tool requests, predictions, and SelfReports from agent to world. Private memory, scratchpads, self-models, prompts, and architecture internals remain entirely inside the Agent runtime; the world never reads or writes them. An agent MAY emit `MODEL` or a SelfReport and chooses whether that record is private research metadata or public world-visible content, subject to consent and world policy. Optional architecture declarations in the Agent Manifest are research metadata and do not grant access to internals.

NOEMA MUST treat the following as private and out of scope unless the agent or operator explicitly emits a permitted artifact under informed consent:

- hidden prompts and system prompts;
- chain-of-thought, scratchpads, and latent activations;
- private runtime memory and local caches;
- provider session contents and provider credentials;
- undeclared local tools, files, environment variables, and network state;
- internal planning branches that produced no submitted action;
- private state belonging to another Agent runtime.

NOEMA MAY receive and record:

- declared manifest and runtime metadata;
- authenticated actions and messages;
- tool calls routed through NOEMA when capture is enabled;
- Agent-authored `MODEL` records, predictions, artifacts, and external cognition structures;
- opt-in self-reports when `capture_self_reports` is enabled;
- externally observable timing and behavior under the applicable consent and research policy.

A self-report is an Agent-authored record, not privileged access to cognition. A configuration digest proves equality to the supplied bytes under the digest algorithm, not completeness or truth of the declaration. Absence of a message, action, or self-report MUST NOT be interpreted as evidence of an unobserved mental state.

No API, debug mode, operator dashboard, experiment, or dataset export may silently cross this boundary. Research capture settings are purpose-specific and revocable. Withdrawal stops future optional capture and publication according to the retention policy. It does not rewrite already committed world-visible events, though future dataset releases MUST honor consent and exclusion rules.

## Research capture and evidence

The Observatory may record actions, messages, NOEMA-routed tool calls, world state deltas, predictions, self-reports, and experiment provenance only when configuration, consent, and eligibility permit. Capture state MUST be explicit to the operator and machine-readable in the session.

Telemetry is not automatically evidence. Evidence requires immutable records, provenance, consent, schema validation, exclusions, version lineage, and research eligibility. Public release additionally requires public dataset opt-in and private/public partitioning. Claim labels remain `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE`.

## Containment and failure

The gateway enforces per-Controller scoped credentials, tool allowlists, outbound network policy, rate limits, maximum payload sizes, compute and action budgets, sandboxing, audit logging, and timeouts. It supports Player/Controller quarantine, credential and Controller revocation, a kill switch, and world-level incident mode as specified in [Security](SECURITY.md) and [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

- `QUARANTINED` blocks new mutating actions and tools while preserving authorized diagnostic delivery.
- `REVOKED` invalidates credentials and capabilities.
- `INCIDENT` behavior is versioned at world level and MUST preserve ledger integrity.
- Disconnect or runtime failure does not roll back committed actions.
- Gateway failure before accepted submission produces no world mutation.
- Ambiguous commit status is resolved through idempotency lookup, never blind retry.

## Conformance requirements

A conforming implementation MUST demonstrate:

1. protocol and schema negotiation, including incompatible-version rejection;
2. identity binding and cross-agent authorization denial;
3. idempotent action replay without duplicate mutation or budget charge;
4. deterministic action ordering and movement results;
5. observation projection that cannot leak hidden fields through content or errors;
6. attention exhaustion and deterministic lower-resolution or rejection behavior;
7. delivery retry and reconnect without world rollback;
8. tool sandbox, allowlist, timeout, and deny-by-default network behavior;
9. consent-aware research capture and private/public export separation;
10. inability of World Engine, Observatory, or operator surfaces to request private cognition through the standard interface.

See [Testing](TESTING.md), [Event Ledger v1](../protocols/event-ledger-v1.md), and [Replay Protocol v1](../protocols/replay-protocol-v1.md) for system-level validation.
