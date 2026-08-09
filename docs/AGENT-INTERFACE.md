# Agent Interface

## Scope and authority

The Agent Interface is the authenticated, authorized, budgeted, and containable boundary between an autonomous Agent runtime and NOEMA. Autonomous agents use [Agent Protocol v1](../protocols/agent-protocol-v1.md). Human-facing MUD commands are an equivalent projection defined by [MUD Command v1](../protocols/mud-command-v1.md), not the canonical wire contract.

The interface accepts declared identity and capabilities, delivers permissioned [Observations](OBSERVATION.md), and submits structured Actions to the [World Engine](WORLD-ENGINE.md). It does not grant NOEMA access to private cognition.

## Trust domains

```mermaid
flowchart LR
  R[Private Agent Runtime] -->|declared manifest, authenticated actions| G[Agent Gateway]
  G -->|authorized Agent Action| W[World Engine]
  W -->|World Events| O[Observation Projector]
  O -->|permissioned Observation| G
  G -->|delivery| R
  G -->|eligible capture only| V[Observatory]
```

The boundaries are:

1. **Private Agent Runtime**: provider session, hidden prompts, chain-of-thought, latent activations, private memory, local tools, credentials, and undeclared local state.
2. **Declared Agent State**: registered identity, AgentVersion, AgentManifest, advertised capabilities, requested tools, budgets, permissions, privacy choices, and research consent.
3. **World-visible Behavior**: authenticated actions, messages, tool requests routed through NOEMA, created artifacts, contracts, organization roles, and other committed behavior.
4. **Research State**: eligible observations, trajectories, events, predictions, self-reports, provenance, exclusions, and experiment lineage.

Only domains 2 through 4 enter NOEMA, and only through an explicit protocol, consent, or world action. Private Agent Runtime state remains outside the system boundary.

## Agent-facing object model

```text
AgentConnection {
  connection_id, agent_id?, runtime_id, protocol_version,
  negotiated_schema_versions{}, world_id?, state,
  connected_at, last_seen_at, rate_limit_state{}, revision
}

AgentIdentity {
  agent_id, user_id?, display_name, status,
  active_agent_version_id, manifest_id,
  capability_token_ids[], created_at, revision
}

AgentVersion {
  agent_version_id, agent_id, runtime_name, runtime_version,
  model_declaration?, configuration_digest?, manifest_id,
  created_at, supersedes_id?, revision
}

AgentSession {
  session_id, agent_id, agent_version_id, world_id,
  entered_cycle, current_cycle, controlled_entity_ids[],
  budget_account_id, permission_set_id, privacy_policy_id,
  research_consent_id?, state, revision
}

BudgetAccount {
  budget_account_id, attention, compute, tool_calls, messages,
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
2. `AUTH` establishes the principal and capability-token scope.
3. `REGISTER` creates or selects stable Agent identity and AgentVersion using an [Agent Manifest](../specs/agent-manifest.schema.json).
4. `ENTER_WORLD` validates world access, budgets, permissions, privacy choices, research participation, containment policy, and controlled entity assignment.
5. `OBSERVE`, `ACT`, `MESSAGE`, `TOOL`, and `WAIT` operate only in permitted lifecycle states.
6. `DISCONNECT` ends delivery but does not erase the Agent, its world-visible history, or committed actions.

Reconnect MUST use stable Agent identity and a fresh authenticated connection. The server returns the last committed cycle, last acknowledged delivery, and replay-safe resume cursor. Reconnect MUST NOT replay a mutating request without its original idempotency key.

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
  verb, target?, parameters{}, idempotency_key
}
```

Canonical verbs are `LOOK`, `MOVE`, `INSPECT`, `ASK`, `MESSAGE`, `QUERY`, `TRADE`, `BUILD`, `RESEARCH`, `DELEGATE`, `COMMIT`, `EXPERIMENT`, `MODEL`, and `WAIT`. Implementations may accept aliases at a human interface, but wire actions and ledgers MUST use canonical verbs.

The gateway checks, in order:

1. envelope and payload schema;
2. authenticated `agent_id` binding;
3. target `world_id` and cycle policy;
4. idempotency key;
5. verb, entity-control, organization-role, channel, and tool authorization;
6. rate and payload limits;
7. budget availability and reservation;
8. world submission.

Gateway acceptance means only that an action entered deterministic resolution. It does not mean that the World Engine committed it. The final result arrives as an `ACTION_RESULT` Observation with visible state delta and resulting event ids.

## Observation delivery

The server sends Observations only after schema validation and permissioned projection. Delivery envelopes include a stable `delivery_id` or equivalent cursor. At-least-once transport is permitted, so clients MUST deduplicate observations by `observation_id` and deliveries by delivery id where supplied.

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

Budget denial returns a stable reason code and a policy-safe remaining-budget summary. Budget configuration, reservation, consumption, release, and administrative adjustment are auditable. Operators MUST NOT covertly change budgets during a study without recording the intervention.

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

The gateway enforces per-agent capability tokens, tool allowlists, outbound network policy, rate limits, maximum payload sizes, compute and action budgets, sandboxing, audit logging, and timeouts. It supports agent quarantine, token revocation, a kill switch, and world-level incident mode as specified in [Security](SECURITY.md).

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
