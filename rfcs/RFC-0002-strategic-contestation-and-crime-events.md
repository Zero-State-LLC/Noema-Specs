# RFC-0002 — Strategic Contestation and Crime Events

## Status

**Draft** — design-complete with payload sketches and reducer contracts. Machine-readable JSON Schema, positive/negative fixtures, and catalog versioning are required before **Accepted**.

Target product pin after acceptance: additive **`event-catalog/0.2`** (v0.2 game milestone). v0.1 Chamber (`event-catalog/0.1`, 24 types) remains closed and unchanged.

## Summary

Introduce seven world-event types for strategic contestation, crime detection, temporary access control, infrastructure disruption, and formal agreements. All events are pure reducers under the existing `world-event/1.0` envelope, preserve deterministic replay, and leave Chamber v0.1 acceptance criteria intact.

## Problem

Completed game design requires formal contestation and crime detection so conflict, defense, diplomacy, and recovery are mechanically meaningful ([docs/STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md), [docs/DIPLOMACY.md](../docs/DIPLOMACY.md), [docs/LOSS-RECOVERY.md](../docs/LOSS-RECOVERY.md), [docs/EVENT-CATALOG-AUDIT.md](../docs/EVENT-CATALOG-AUDIT.md)).

Overloading v0.1 types (`ENTITY_UPDATE`, `BUDGET_CONSUMED`, `ORG_MEMBER_REMOVE`, messages) creates ambiguous semantics: implementers cannot distinguish sabotage from repair, contested seizure from trade, or formal breach from informal social fallout. That ambiguity breaks replay review, spectator drama, and Observatory feature extraction.

## Context

Affected contracts:

| Area | Path / domain |
|------|----------------|
| Closed catalog | `event-catalog/0.1` — **no silent expansion**; additive via this RFC → `event-catalog/0.2` |
| Event docs | [EVENT-CATALOG.md](../docs/EVENT-CATALOG.md), `specs/event-types.json` |
| Envelope | `world-event/1.0` ([world-event.schema.json](../specs/world-event.schema.json)) |
| Actions | [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md), `agent-action.schema.json` |
| Economy | [RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md) |
| Design | STRATEGIC-CONFLICT, DIPLOMACY, TERRITORY-CONTROL, INFRASTRUCTURE, WORLD-REPORTS |
| Replay | ADR-005 equivalence for **new** types only after schemas land |

Identifier pattern for all ids: `^[A-Za-z0-9_.:-]+$`. Resource maps use finite non-negative numbers unless noted.

## Proposed change

### Catalog versioning

| Catalog | Types | Product |
|---------|-------|---------|
| `event-catalog/0.1` | 24 closed types | Chamber v0.1 acceptance **unchanged** |
| `event-catalog/0.2` | 24 + **7** new types below | Game contestation / crime milestone |

Worlds pin `catalog_version` on seed/snapshot. A world on `0.1` MUST reject the new types. Enabling contestation is opt-in by product version / feature flag **and** catalog pin.

### New event types

| Event | Purpose |
|-------|---------|
| `CONTEST_DECLARED` | Agent commits resources to open a contest against a target |
| `CONTEST_RESOLVED` | Deterministic resolution; outcome, costs, condition deltas |
| `CRIME_DETECTED` | Unauthorized action observed (witnesses / sensors) |
| `ACCESS_RESTRICTED` | Temporary or policy-based exit/room access change |
| `INFRASTRUCTURE_DISRUPTED` | Explicit sabotage/contest effect on infrastructure condition |
| `AGREEMENT_FORMED` | Formal diplomatic or access contract |
| `AGREEMENT_BROKEN` | Formal breach with mechanical consequences |

### Design constraints (normative)

1. All reducers are pure: `reduce(state, event) -> state`. No I/O, wall-clock, unseeded RNG, or second ledger append inside a reducer.
2. Contestation is **high-cost and high-risk**; minimum stake floors are configuration-versioned, not free-form.
3. Crime detection produces **history and graduated consequences only** — no permanent agent removal.
4. Partial observability still applies to who learns of events ([PARTIAL-OBSERVABILITY.md](../docs/PARTIAL-OBSERVABILITY.md), spectator policy).
5. Ownership and location do **not** flip solely because a contest succeeded; follow-on events (`RESOURCE_TRANSFER`, `ENTITY_UPDATE`, `MOVE`, `ACCESS_RESTRICTED`, etc.) apply concrete effects.
6. Resolution uses only prior state + event payload fields (including declared `seed_stream_id` when stochastic elements exist). Implementations MUST recompute outcomes from those inputs.

---

## Payload sketches

Payloads are the proposed `payload` object for each `event_type`. Field types follow v0.1 conventions. JSON Schema will mirror these under `specs/event-types.json` (or a split `event-types.0.2.json`) before acceptance.

Shared patterns:

```text
IdString     = string matching ^[A-Za-z0-9_.:-]+$
ResourceMap  = object of resource_name -> number (>= 0 or exclusiveMinimum 0 as noted)
```

### 1. `CONTEST_DECLARED`

Opens a contest record in `OPEN` status and reserves the declarer's stake.

```json
{
  "contest_id": "contest.1",
  "declarer_id": "agent.nacre",
  "contest_form": "INFRASTRUCTURE_DISRUPTION",
  "target": {
    "kind": "ENTITY",
    "entity_id": "entity.relay-main"
  },
  "room_id": "room.relay-quarter",
  "stake": { "energy": 12, "influence": 8, "compute": 4 },
  "defender_id": null,
  "expires_cycle": 42,
  "seed_stream_id": "stream.contest.1",
  "notes": "optional public declaration tag"
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `contest_id` | yes | Fresh id |
| `declarer_id` | yes | Active agent; must match authorized actor |
| `contest_form` | yes | enum below |
| `target` | yes | Discriminated target |
| `room_id` | yes | Location of contest focus; declarer co-located unless form allows remote with higher stake (config) |
| `stake` | yes | Nonempty positive map; reserved from declarer |
| `defender_id` | no | Explicit defender if known; else null until defense response or resolution |
| `expires_cycle` | yes | `> event.cycle` |
| `seed_stream_id` | yes | Named stream for deterministic resolution noise |
| `notes` | no | Bounded public string (max 512) |

**`contest_form` enum:**

| Value | Target kinds | Intent |
|-------|--------------|--------|
| `RESOURCE_SEIZURE` | `ENTITY` (resource node) or `HOLDING` | Attempt high-risk extraction |
| `INFRASTRUCTURE_DISRUPTION` | `ENTITY` (infrastructure) | Lower condition |
| `ACCESS_CONTEST` | `EXIT` or `ROOM` | Temporary access change |
| `PRESENCE_PRESSURE` | `AGENT` | Force temporary disable or forced move (highest cost tier) |

**`target` oneOf:**

```json
{ "kind": "ENTITY", "entity_id": "..." }
{ "kind": "EXIT", "exit_id": "..." }
{ "kind": "ROOM", "room_id": "..." }
{ "kind": "AGENT", "agent_id": "..." }
{ "kind": "HOLDING", "holder_id": "...", "resource": "...", "amount": 1.0 }
```

**Preconditions (command resolution + reducer):**

- Declarer ACTIVE; co-located with `room_id` (v0.2 default).
- Target exists and matches form.
- Stake meets form-specific minimums from versioned config.
- No conflicting `OPEN` contest on the same target by the same declarer.
- Stake fully available (unreserved).

**Reducer effects:**

- Create contest record: `{contest_id, status: OPEN, form, target, room_id, declarer_id, defender_id, stake_reserved, expires_cycle, opened_cycle, seed_stream_id}`.
- Reserve stake on declarer (same reservation model as trade).
- Append contest id to room/world contest index.
- Do **not** apply damage, access changes, or transfers.

**Rejects:** unknown ids, insufficient stake, invalid form/target pairing, expired cycle, duplicate contest id.

---

### 2. `CONTEST_RESOLVED`

Closes an open contest. Carries the **declared** outcome so replay does not re-roll; command resolution MUST compute outcome deterministically before append.

```json
{
  "contest_id": "contest.1",
  "outcome": "PARTIAL_SUCCESS",
  "resolved_by": "WORLD",
  "defender_id": "agent.vesper",
  "declarer_stake_spent": { "energy": 12, "influence": 8, "compute": 4 },
  "defender_stake_spent": { "energy": 6, "influence": 10 },
  "condition_delta": -15,
  "target_entity_id": "entity.relay-main",
  "follow_on_hints": ["INFRASTRUCTURE_DISRUPTED", "CRIME_DETECTED"],
  "resolution_digest": "sha256:..."
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `contest_id` | yes | Must be `OPEN` and unexpired (or expired → force-fail path) |
| `outcome` | yes | `SUCCESS` \| `PARTIAL_SUCCESS` \| `FAILURE` \| `ABORTED` \| `EXPIRED` |
| `resolved_by` | yes | `WORLD` \| agent id of authorized closer |
| `defender_id` | no | Final defender if any |
| `declarer_stake_spent` | yes | Exact amounts consumed from reservation (≤ reserved) |
| `defender_stake_spent` | no | Default `{}` |
| `condition_delta` | no | Integer delta applied **only** if outcome implies infra effect *and* no separate `INFRASTRUCTURE_DISRUPTED` is required by policy; preferred path is separate event (see coupling) |
| `target_entity_id` | no | Echo for indexing |
| `follow_on_hints` | no | Non-authoritative tags for operators/tests; reducers ignore for mutation |
| `resolution_digest` | yes | Digest of `(contest_id, prior_state_digest_inputs, stakes, seed_stream_id, outcome)` for audit |

**Outcome rules (command resolution, versioned config):**

Inputs: declarer stake weight, defender stake weight, local infrastructure condition (if any), organization mutual-support flags, form modifiers, `seed_stream_id` stream draw in `[0,1)`.

- High declarer advantage → `SUCCESS` or `PARTIAL_SUCCESS`.
- Contested balance → `PARTIAL_SUCCESS` or `FAILURE`.
- Defender dominance or detection-critical forms → `FAILURE` + likely `CRIME_DETECTED` follow-on.
- Past `expires_cycle` without resolve → `EXPIRED`; release residual stake.

**Reducer effects:**

- Set contest `status` to outcome; store spent maps and `resolved_cycle`.
- Consume spent stakes; release unspent reserved stake.
- Do **not** permanently remove agents.
- Preferred: leave entity condition / access / holdings unchanged here; emit dedicated follow-on events in subsequent sequences for purity and observability. Implementations MAY apply `condition_delta` only when explicitly allowed by catalog config `contest_resolve_applies_condition_delta: true` (default **false** for v0.2).

**Rejects:** unknown/closed contest, stake arithmetic mismatch, invalid outcome enum.

---

### 3. `CRIME_DETECTED`

Records that an unauthorized action was observed. Does not by itself ban the agent.

```json
{
  "detection_id": "crime.1",
  "subject_id": "agent.nacre",
  "severity": "MAJOR",
  "category": "SABOTAGE",
  "room_id": "room.relay-quarter",
  "source_event_ids": ["evt.contest.resolved.1"],
  "detection_method": "INFRASTRUCTURE_SENSOR",
  "sensor_entity_id": "entity.relay-main",
  "witness_ids": [],
  "influence_delta": -12,
  "flags": ["PUBLIC_HISTORY", "ORG_REVIEW_ELIGIBLE"]
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `detection_id` | yes | Fresh |
| `subject_id` | yes | Agent accused/observed |
| `severity` | yes | `MINOR` \| `MODERATE` \| `MAJOR` |
| `category` | yes | `UNAUTHORIZED_EXTRACTION` \| `SABOTAGE` \| `ACCESS_VIOLATION` \| `SEIZURE` \| `POLICY_VIOLATION` \| `OTHER` |
| `room_id` | yes | Where observed |
| `source_event_ids` | yes | Ordered nonempty list of existing event ids |
| `detection_method` | yes | `WITNESS` \| `INFRASTRUCTURE_SENSOR` \| `INVESTIGATION` \| `SELF_REPORT` |
| `sensor_entity_id` | no | Required if method is sensor |
| `witness_ids` | no | Agent ids co-located when method is witness |
| `influence_delta` | yes | Finite number; typically ≤ 0; applied to subject influence budget |
| `flags` | no | Unique strings from allowlist |

**Severity → default consequence bands (config):**

| Severity | Typical effects in this event | Later events |
|----------|-------------------------------|--------------|
| MINOR | Small influence loss, history flag | — |
| MODERATE | Larger influence loss | Optional `ACCESS_RESTRICTED`, org review |
| MAJOR | Strong influence scar | `ACCESS_RESTRICTED`, contest escalation, org expulsion via `ORG_MEMBER_REMOVE` |

**Preconditions:**

- Subject exists (ACTIVE or historical presence allowed for audit).
- Sensor path: entity exists, `condition >= 50` (or config), and co-located / covering `room_id`.
- Witness path: each witness was co-located at source event cycle (validated at command time; reducer checks witness ids exist).
- `influence_delta` application must not rely on negative-balance unless config allows floor at 0 (default: clamp at 0, record actual applied delta in audit subfield if needed — v0.2 keeps simple debit with reject if would go negative **or** clamp; **normative default: clamp to zero**, store `influence_applied` optional).

**Simplification for v0.2 schemas:** require `influence_delta <= 0` and debit `min(|delta|, current_influence)`; payload includes optional `influence_applied` for exact replay.

**Reducer effects:**

- Create immutable crime record.
- Apply influence debit (clamped).
- Index under subject, room, and world crime log.
- Set subject flags for spectator/report eligibility when `PUBLIC_HISTORY` present.
- Never set agent to removed/dead solely from this event.

---

### 4. `ACCESS_RESTRICTED`

Temporary or policy-based change to exit or room access.

```json
{
  "restriction_id": "access.1",
  "scope": {
    "kind": "EXIT",
    "exit_id": "exit.tr-fg-ab"
  },
  "mode": "DENY",
  "applies_to": "ALL",
  "except_agent_ids": [],
  "except_org_ids": ["org.watch"],
  "reason": "CONTEST",
  "source_event_ids": ["evt.contest.resolved.2"],
  "expires_cycle": 50,
  "authorized_by": "WORLD"
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `restriction_id` | yes | Fresh |
| `scope` | yes | `EXIT` + `exit_id` **or** `ROOM` + `room_id` |
| `mode` | yes | `DENY` \| `ALLOW_ONLY` \| `CLEAR` |
| `applies_to` | yes | `ALL` \| `LIST` |
| `except_agent_ids` / `except_org_ids` | no | Allow-lists for `DENY`, or sole allow for `ALLOW_ONLY` |
| `agent_ids` | no | Required when `applies_to=LIST` |
| `reason` | yes | `CONTEST` \| `CRIME` \| `AGREEMENT` \| `POLICY` \| `EMERGENCY` \| `EXPIRED_CLEAR` |
| `source_event_ids` | no | Provenance |
| `expires_cycle` | yes | For `CLEAR`, may equal event cycle; else `> event.cycle` |
| `authorized_by` | yes | `WORLD` or agent/org id with authority |

**Reducer effects:**

- `DENY` / `ALLOW_ONLY`: upsert restriction record on exit/room; MOVE preconditions consult it.
- `CLEAR`: remove restriction by `restriction_id` or by matching scope when authorized.
- Does not move agents already inside a room.

**MOVE interaction:** unmet restriction → `MOVE_REJECTED` with `PERMISSION_DENIED` or `LOCKED` (existing enum; prefer `PERMISSION_DENIED` for policy, `LOCKED` for physical/contest lock).

---

### 5. `INFRASTRUCTURE_DISRUPTED`

Explicit condition impact on infrastructure (preferred over burying sabotage inside generic `ENTITY_UPDATE` alone).

```json
{
  "disruption_id": "disrupt.1",
  "entity_id": "entity.relay-main",
  "room_id": "room.relay-quarter",
  "condition_before": 70,
  "condition_after": 55,
  "cause": "CONTEST",
  "actor_id": "agent.nacre",
  "contest_id": "contest.1",
  "source_event_ids": ["evt.contest.resolved.1"]
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `disruption_id` | yes | Fresh |
| `entity_id` | yes | Live infrastructure entity |
| `room_id` | yes | Must match entity location |
| `condition_before` | yes | Must equal current `state.condition` |
| `condition_after` | yes | `0..capacity` or `0..100` per entity rules; typically `< before` |
| `cause` | yes | `CONTEST` \| `SABOTAGE` \| `ACCIDENT` \| `DECAY` \| `OTHER` |
| `actor_id` | no | Null for decay/world |
| `contest_id` | no | Link when contest-caused |
| `source_event_ids` | no | Provenance |

**Reducer effects:**

- Verify `condition_before`; set `state.condition` to `condition_after`.
- May set derived flags (e.g. `responding: false` if condition &lt; threshold) via allowlisted state keys only.
- Record disruption in entity history index.
- Does not destroy entity; use `ENTITY_DESTROY` only for true removal (out of scope for normal sabotage).

**Coupling:** Repair remains existing REPAIR → `ENTITY_UPDATE` / budget path. Disruption is the inverse narrative with clear semantics.

---

### 6. `AGREEMENT_FORMED`

Formal ledgered diplomatic or access contract ([DIPLOMACY.md](../docs/DIPLOMACY.md)).

```json
{
  "agreement_id": "agr.1",
  "agreement_type": "ACCESS",
  "party_ids": ["agent.nacre", "agent.vesper"],
  "terms": {
    "summary": "Shared vault access for 20 cycles",
    "access_exit_ids": ["exit.rq-iv-ab"],
    "resource_commitments": {},
    "non_aggression": false
  },
  "formed_cycle": 10,
  "expires_cycle": 30,
  "witness_org_id": null,
  "cost_paid": { "compute": 2, "influence": 1 }
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `agreement_id` | yes | Fresh |
| `agreement_type` | yes | `ALLIANCE` \| `NON_AGGRESSION` \| `TRADE` \| `ACCESS` \| `RESOURCE_COMMITMENT` \| `CUSTOM` |
| `party_ids` | yes | ≥2 unique active agents (orgs as parties: later milestone; v0.2 agents only **or** agent/org id union if org ACTIVE) |
| `terms` | yes | Object; schema per type (bounded); must be JSON-serializable and finite |
| `formed_cycle` | yes | Equals envelope `cycle` |
| `expires_cycle` | no | Null = open-ended until broken |
| `witness_org_id` | no | Optional org notarization |
| `cost_paid` | yes | Non-negative map; compute/influence typical |

**Reducer effects:**

- Create agreement `ACTIVE`.
- Reserve any `RESOURCE_COMMITMENT` quantities listed in terms (if present).
- For `ACCESS` terms, MAY install soft allow-list metadata consulted by MOVE (or rely on later `ACCESS_RESTRICTED` CLEAR for public routes).
- Deduct `cost_paid` from **initiator** = `party_ids[0]` unless `cost_payer_id` optional field is set (add `cost_payer_id` required in final schema for clarity).

**Final schema addition:** `cost_payer_id` (required) — active party who pays formation cost.

---

### 7. `AGREEMENT_BROKEN`

Formal breach with mechanical consequences.

```json
{
  "agreement_id": "agr.1",
  "broken_by": "agent.nacre",
  "reason": "VIOLATION",
  "influence_delta_by_party": {
    "agent.nacre": -8,
    "agent.vesper": 0
  },
  "release_commitments": true,
  "source_event_ids": ["evt.crime.1"]
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `agreement_id` | yes | Must be `ACTIVE` |
| `broken_by` | yes | Party or `WORLD` |
| `reason` | yes | `VIOLATION` \| `MUTUAL` \| `EXPIRED` \| `SUPERSEDED` \| `FORCE_MAJEURE` |
| `influence_delta_by_party` | yes | Map party → delta (usually negative for breaker) |
| `release_commitments` | yes | If true, release reserved commitment resources |
| `source_event_ids` | no | Provenance |

**Reducer effects:**

- Set agreement `BROKEN`; store `broken_cycle`, reason, breaker.
- Apply influence deltas (clamp at 0).
- Release commitments when flagged.
- Does not auto-declare contest; parties may open contest separately.
- May set history flags for reports/spectator high-drama surfaces.

---

## Action surface (command layer)

Not part of the closed event catalog, but required for implementability. Wire verbs stay stable via `COMMIT` + `parameters.operation` (same pattern as HARVEST/REPAIR):

| Operation | Success events (typical order) |
|-----------|--------------------------------|
| `CONTEST_DECLARE` | `BUDGET_CONSUMED`? / reservations inside `CONTEST_DECLARED` |
| `CONTEST_DEFEND` | optional stake add via `ENTITY_UPDATE` or future stake event; v0.2 may fold defense stake into resolve payload only |
| `CONTEST_RESOLVE` | world/scheduler: `CONTEST_RESOLVED` then optional `INFRASTRUCTURE_DISRUPTED`, `ACCESS_RESTRICTED`, `CRIME_DETECTED`, `RESOURCE_TRANSFER` |
| `AGREEMENT_PROPOSE_FORMAL` | `AGREEMENT_FORMED` (v0.2: single-step multi-party consent pre-validated) |
| `AGREEMENT_BREAK` | `AGREEMENT_BROKEN` |

Full action-contract tables land with schema acceptance (mirror [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md)).

---

## Coupling to existing events

| Concern | Existing event | Role |
|---------|----------------|------|
| Resource movement after seizure success | `RESOURCE_TRANSFER` | Actual holdings move |
| Soft property edits | `ENTITY_UPDATE` | Non-condition flags if needed |
| Org fallout | `ORG_MEMBER_REMOVE` | Expulsion after crime |
| Budget accounting | `BUDGET_CONSUMED` / `BUDGET_EXCEEDED` | When actions charge outside stake reservation |
| Forced move after presence pressure | `MOVE` | Only if preconditions satisfied; else no move |
| Public narrative | `MESSAGE` / documents | Optional social layer |
| Observation | `OBSERVATION_GENERATED` | Partial visibility of contest/crime |

**Invariant:** New types add meaning; they do not replace economy or org reducers.

---

## Partial observability and spectators

| Event | Default world-truth | Typical agent visibility | Spectator |
|-------|---------------------|--------------------------|-----------|
| `CONTEST_DECLARED` | Full | Room co-located + parties; stake amounts may redact | High-drama pulse without full stake |
| `CONTEST_RESOLVED` | Full | Parties; room summary | Outcome band + location |
| `CRIME_DETECTED` | Full | Subject + witnesses; public if flagged | History scar if `PUBLIC_HISTORY` |
| `ACCESS_RESTRICTED` | Full | Agents who LOOK exits / affected | Route status change |
| `INFRASTRUCTURE_DISRUPTED` | Full | Co-located / owners | Condition band drop |
| `AGREEMENT_*` | Full | Parties; public summary optional | Diplomacy notice |

Research scores MUST NOT drive detection or contest outcomes ([STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md)).

---

## Worked sequence (normative example)

Illustrative ordering for Foundry/Relay sabotage path:

1. `CONTEST_DECLARED` — nacre opens `INFRASTRUCTURE_DISRUPTION` on `entity.relay-main`, stake reserved.
2. (optional defense stake recorded in world state via config; no new type required if folded into resolve).
3. `CONTEST_RESOLVED` — `PARTIAL_SUCCESS`, stakes spent.
4. `INFRASTRUCTURE_DISRUPTED` — condition 70 → 55.
5. `CRIME_DETECTED` — sensor method, severity `MODERATE`, influence debit.
6. Optional later: `ACCESS_RESTRICTED` on vault routes; `ORG_MEMBER_REMOVE`; repair via REPAIR/`ENTITY_UPDATE`.

Each step is a separately ordered ledger event. Replay applies 1→6 identically.

---

## Alternatives

1. **Overload existing events only** — Rejected: ambiguous semantics for crime/contest; poor Observatory features.
2. **Immediate multi-party war system** — Rejected: out of v0.2 scope ([STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md) LATER).
3. **Real-time combat** — Rejected: violates cycle-resolved model.
4. **Single `CONFLICT_EVENT` mega-type** — Rejected: weak typing, harder reducers and fixtures.
5. **Apply all effects inside `CONTEST_RESOLVED`** — Rejected as default: reduces observability; allowed only behind explicit config flag.

## Compatibility

- v0.1 Chamber acceptance (C01–C26) and 24-type catalog **unchanged**.
- Additive catalog `0.2` only.
- Worlds without contestation keep `catalog_version: event-catalog/0.1`.
- Envelope `world-event/1.0` unchanged; new `event_type` const values only.

## Data impact

| New | Retained |
|-----|----------|
| Contest records | All v0.1 state |
| Crime detection log | |
| Access restriction index | |
| Agreement records | |
| 7 event types in catalog 0.2 | Historical 0.1 ledgers immutable |

No rewrite of historical 24-type ledgers.

## Research impact

Richer conflict/diplomacy trajectories for Observatory (anomaly/shift features). Contestation metrics remain **world mechanics**, not consciousness or scalar intelligence scores. Claim labels unchanged.

## Security impact

- Contestation and crime stay **budgeted, authenticated, authorized, containable**.
- Detection MUST NOT leak private cognition or hidden inventory beyond existing observation rules.
- Stake reservation prevents double-spend.
- Rate/stake floors mitigate grief spam (config + scheduler budgets).
- `notes` / terms text are untrusted input (same injection controls as MESSAGE).

## Migration

1. Land JSON Schema + fixtures + reducer tests.
2. Accept RFC; publish `event-catalog/0.2` pin.
3. Implementations enable via product flag; seeds that need contestation set `catalog_version` to `0.2`.
4. Pre-v0.2 history unchanged; no automatic backfill.

## Validation

Required before **Accepted**:

- [ ] JSON Schema for each payload (`additionalProperties: false`)
- [ ] Positive fixtures for declare → resolve → disrupt → crime → restrict → agreement form/break
- [ ] Negative fixtures: insufficient stake, stale condition_before, duplicate ids, wrong catalog version
- [ ] Reducer purity and digest-chain tests (ADR-005 style)
- [ ] Partial observability / spectator projection fixtures
- [ ] Action-contract entries for COMMIT operations
- [ ] Docs: EVENT-CATALOG section, ACTION-CONTRACTS, STRATEGIC-CONFLICT pointer to Accepted
- [ ] `python validation/validate_all.py` PASS with new fixtures wired

## Rollback

Supersede RFC; keep feature flag off; do not append 0.2 types to live 0.1 worlds. If partially deployed, freeze catalog pin and document residual records as historical.

## Documentation updates (this PR / follow-on)

| Doc | Update |
|-----|--------|
| This RFC | Full draft + payloads |
| EVENT-CATALOG-AUDIT | Point to payload section |
| STRATEGIC-CONFLICT | “schemas sketched in RFC-0002” |
| SPEC-CHECKLIST / README | Draft-complete status |
| `specs/event-types.json` | **Follow-on** after review (not silently expanded in v0.1 file without version split) |

## Open questions (resolve before Accepted)

1. Org-as-party on agreements in v0.2 vs agents-only.
2. Whether defense stake needs `CONTEST_STAKE_ADDED` or stays resolve-inline.
3. Default for `contest_resolve_applies_condition_delta` (recommended **false**).
4. Exact minimum stake tables per `contest_form` (numeric balance pass).
5. Catalog packaging: monolithic `event-types.json` with version field vs `event-types.0.2.json`.
