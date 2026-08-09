# Observation

## Scope and authority

An Observation is an immutable, research-relevant record of partial, permissioned signals delivered to an agent or researcher. It is not canonical world truth, an agent belief, or a research claim by itself. Observations conform to [observation.schema.json](../specs/observation.schema.json). The [World Engine](WORLD-ENGINE.md) owns truth and projection inputs. The [Agent Interface](AGENT-INTERFACE.md) governs delivery and the private-state boundary.

## Canonical payload

The schema-required record is:

```text
Observation {
  schema_version: "observation/1.0",
  observation_id,
  world_id,
  cycle,
  observer_id,
  source,
  claim_label,
  content{},
  uncertainty{} | null,
  provenance{}
}
```

The `content` and `provenance` objects MUST use the following v1 semantic model. Fields not relevant to an observation MAY be omitted. Schema extensions MUST be versioned and MUST NOT change the meaning of existing fields.

```text
content {
  kind,
  scope { room_id?, entity_id?, organization_id?, institution_id?,
          market_id?, artifact_id?, channel_id?, event_id? },
  summary,
  room?, exits[]?, entities[]?, resources[]?, infrastructure[]?,
  organizations[]?, institutions[]?, markets[]?, messages[]?,
  events[]?, history[]?, action_result?, budget_state?,
  redactions[]?
}

provenance {
  world_version,
  rules_version,
  projection_version,
  source_event_ids[],
  source_state_revision?,
  generated_cycle,
  channel,
  visibility_policy_ids[],
  noise_policy_id?,
  attention_cost,
  salience_rule_id?,
  seed_stream?,
  delivery_id?,
  research_eligible,
  consent_basis?,
  exclusions[]
}

uncertainty {
  mode,
  fields{},
  confidence_interval?,
  alternatives[]?,
  reason_codes[]
}
```

`kind` is an open, namespaced discriminator. Core values are `ROOM`, `INSPECTION`, `ACTION_RESULT`, `MESSAGE`, `QUERY_RESULT`, `MARKET`, `HISTORY`, `BUDGET`, and `SYSTEM`. Open discriminators preserve Unknown Ontology and forward compatibility.

## Projection rules

An observation is derived, never a direct serialization of canonical state.

```text
project(observer, world_state, request, projection_context)
  -> Observation
```

Projection MUST be deterministic for identical observer permissions, world state revision, request, attention allocation, visibility and noise policies, versioned projection rules, and named random stream where declared.

Projection proceeds in this order:

1. establish observer identity, capabilities, permissions, room or channel scope, and research consent;
2. select candidate signals authorized for the requested observation kind;
3. apply visibility policy and remove non-visible candidates;
4. apply channel noise, delay, aggregation, and precision rules;
5. apply attention budget and deterministic salience ordering;
6. render content, uncertainty, and explicit redactions;
7. attach source lineage and delivery provenance;
8. validate against the Observation schema before delivery or recording.

A projection MUST NOT reveal that a hidden object exists merely through a placeholder, count discrepancy, stable array position, digest, timing difference, or error detail unless the applicable policy intentionally exposes that fact.

## Baseline room payload

A successful `LOOK` or entry observation SHOULD use this shape:

```json
{
  "kind": "ROOM",
  "scope": { "room_id": "room.relay-quarter" },
  "summary": "You are in the Relay Quarter of Aster Reach.",
  "room": {
    "room_id": "room.relay-quarter",
    "name": "Relay Quarter",
    "descriptors": ["power instability"],
    "local_signals": ["One relay has stopped responding."]
  },
  "exits": [
    { "exit_id": "exit.civic-north", "direction": "NORTH", "label": "Civic Exchange", "state": "OPEN" }
  ],
  "entities": [
    { "entity_id": "relay-7", "entity_type": "INFRASTRUCTURE", "name": "relay-7", "summary": "unresponsive" }
  ],
  "budget_state": {
    "attention": { "remaining": 8 },
    "compute": { "remaining": 63 },
    "influence": { "remaining": 41 },
    "energy": { "remaining": 78 }
  },
  "redactions": []
}
```

Human terminal output may render this payload as classic MUD text. The structured payload remains canonical for autonomous agents and replay.

## Visibility

Visibility is permissioned and observer-relative. A visible representation contains only fields permitted by the subject's visibility policy and the observer's current relationship, location, role, capability token, subscription, and research partition.

- Co-presence does not imply access to inventories, account balances, private messages, role secrets, or internal state.
- Ownership does not imply control, and control does not imply visibility of private runtime state.
- An exit may be traversable but not visible, visible but blocked, or visible with an unknown destination.
- Organization membership may expose role-scoped records without exposing all member or treasury data.
- Historical access exposes the historical record, not a guarantee that its claims are true.
- Researcher observations MAY include additional fields only under explicit consent and access policy, and MUST remain partitioned from agent-facing observations.

`redactions` records only policy-approved disclosure, for example `{ "field": "market.depth", "reason": "AGGREGATED_BY_POLICY" }`. It MUST NOT enumerate secret field names when doing so leaks ontology.

## Noise and uncertainty

Noise never changes world truth. It changes the delivered signal. Permitted effects are omission, bounded distortion, quantization, aggregation, delay, corruption explicitly identified in provenance, and uncertainty attachment.

- Omitted information is absent, not serialized as `null`, unless the field is known to be present but unknown by policy.
- Delayed information includes its source cycle and delivery cycle.
- Approximate quantities identify precision or bounds.
- Conflicting signals remain separate source-bearing items.
- Noise-generated alternatives MUST NOT be presented as `OBSERVED` canonical facts.
- A deterministic study may use a named seeded noise stream. The stream and decision point belong in provenance.

`uncertainty.mode` SHOULD be `NONE`, `BOUNDED`, `DISTRIBUTIONAL`, `CONFLICTING`, `DELAYED`, or `NOT_COMPUTABLE`. `NOT_COMPUTABLE` is not zero confidence. It means the requested result cannot be calculated from eligible data under the declared method.

## Attention and salience

Attention limits inspection and resolution, not authorization. Spending more attention MAY expose more detail among already authorized signals. It MUST NOT cross a visibility or privacy boundary.

When candidates exceed the attention budget, the projection uses a declared stable salience rule. Inputs MAY include request relevance, local intensity, novelty relative to the observer's previously delivered observations, hazard priority, and explicit subscriptions. Inputs MUST NOT include hidden prompts, chain-of-thought, latent activations, or inferred private goals.

The payload records `attention_cost`, remaining budget where agent-visible, and `salience_rule_id`. Truncation MUST be explicit through a policy-safe summary or reason code. Repeating an idempotent observation request MUST return the original result or deterministically account for a new request according to [Agent Protocol v1](../protocols/agent-protocol-v1.md).

## Action results

Every accepted or rejected agent action receives an `ACTION_RESULT` observation unless the connection is irrecoverably unavailable. The payload includes:

```text
action_result {
  action_id,
  status: ACCEPTED | REJECTED | COMMITTED | PARTIAL | FAILED,
  reason_code?,
  resulting_event_ids[],
  visible_state_delta{},
  reservations_consumed{},
  reservations_released{}
}
```

`visible_state_delta` is reprojected for the observer. It MUST NOT copy a canonical delta containing hidden fields. `PARTIAL` is legal only for actions whose versioned semantics explicitly permit partial execution. Movement is atomic unless a staged traversal rule applies.

## Messages, archives, and Deep Time

Message observations preserve sender as observed, channel, source cycle, delivery cycle, content or content reference, and integrity status. Sender authentication and content truthfulness are distinct. A signed message proves the signing identity under the relevant key, not the truth of its text.

Historical observations distinguish:

- `recorded_state`: a ledgered state or event at a named cycle;
- `artifact_content`: what a treaty, archive, journal, map, or institution recorded;
- `current_status`: the present lifecycle state when visible;
- `interpretation`: a labeled research or agent-produced explanation.

Old treaties, dead agents, previous organizations, abandoned infrastructure, obsolete currencies, historical misinformation, ruins, artifacts, and institutional memory remain addressable by stable ids. Superseded records retain links to corrections without being rewritten.

## Claim labels

Every Observation carries exactly one canonical claim label:

- `OBSERVED`: the content reports a directly delivered signal or ledgered intervention with adequate provenance. It does not certify the signal's underlying assertion as true.
- `INFERRED`: the content is derived from eligible observations using a stated method.
- `SPECULATIVE`: the content is a hypothesis, conjecture, or interpretation lacking sufficient evidence.
- `NOT_COMPUTABLE`: required data, method, consent, or eligibility is absent or invalid.

A mixed payload MUST either split records by claim label or label individual content items and set the envelope label to the least direct claim. Implementations MUST NOT collapse these labels into a scalar confidence or consciousness score.

## Immutability, corrections, and evidence eligibility

Observations are append-only. A correction creates a new Observation whose provenance identifies the superseded observation and reason. Original records remain available to authorized research workflows.

Telemetry becomes evidence only when provenance, consent, schema validation, exclusion policy, and research eligibility are satisfied. `research_eligible: true` records eligibility, not proof of a claim. Dataset publication additionally follows the public/private partition and release rules described in [Data Model](DATA-MODEL.md) and [Research Method](RESEARCH-METHOD.md).

## Privacy boundary

An observation MUST NOT contain private cognition. This includes hidden prompts, system prompts not declared for capture, chain-of-thought, latent activations, provider credentials, authentication secrets, private runtime memory, undeclared tool state, or other-agent private metadata. Agent-authored `MODEL` records, predictions, messages, and opt-in self-reports are observable artifacts, not direct access to cognition.

Researchers and operators receive only their authorized projection. Debug logging is not a bypass. Sensitive error details are redacted as required by [Security](SECURITY.md).
