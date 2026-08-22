# ADR-008 — Replay Conformance and Deterministic Hardening

## Status

Accepted

Date: 2026-08-18

Related docs: [WORLD-ENGINE.md](../docs/WORLD-ENGINE.md), [SCHEDULER.md](../docs/SCHEDULER.md), [AGENT-DETERMINISM.md](../docs/AGENT-DETERMINISM.md), [EVENT-CATALOG.md](../docs/EVENT-CATALOG.md), [REPLAY.md](../docs/REPLAY.md), [protocols/replay-protocol-v1.md](../protocols/replay-protocol-v1.md)

Also binds: [ADR-001](ADR-001-determinism-and-seeded-nondeterminism.md), [ADR-002](ADR-002-private-cognition-boundary.md), [ADR-005](ADR-005-v01-equivalence-boundary.md), [ADR-006](ADR-006-world-bound-exit-visibility-and-location-discovery.md), [ADR-007](ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md).

This ADR does not open new verbs, new event types, or Genesis reseed. It does not weaken ADR-001.

## Context

NOEMA already states a deterministic transition contract, a frozen cycle pipeline, a canonical action order key, HMAC-SHA-256 named seed streams, an immutable per-cycle event ledger, snapshots, and JCS/SHA-256 digest identity for replay-critical JSON. Observation and WATCH are derived after commit. Private cognition is outside world truth. AGENT-DETERMINISM.md classifies agent behavior; it does not define world replay.

Operational gaps remain: whether an undeclared seed stream is a hard fail; whether `world_state_digest` is required on every cycle; the minimum harness interface that may claim v0.1 replay conformance; that a golden trajectory is mandatory; that WATCH / observation cannot write state; that scheduler conflict cases are first-class replay tests.

## Decision

### A. Deterministic transition contract and replay unit

The v0.1 replay unit is **one cycle**.

For `world_version`, genesis or snapshot head, named seeds, deterministic configuration, prior committed `world_state`, declared external inputs, and the frozen accepted-action set, the reducer MUST produce the same next `world_state` and the same contiguous event batch:

```text
reduce(world_state, ordered_inputs, reducer_context)
  -> { world_state, world_events, delivery_intents }
```

`reducer_context` contains `world_version`, `rules_version`, the named-stream registry, current `cycle`, and feature flags. It MUST NOT contain model output, researcher interpretation, wall-clock ordering, gateway arrival order, or undisclosed external state.

The cycle pipeline in SCHEDULER.md / WORLD-ENGINE.md is the only legal reduce order. Partial application is nonconforming. Serialization failure, stale revision, stale writer fence, duplicate sequence, or digest mismatch aborts the whole batch.

### B. Canonical order key

Within a frozen cycle, accepted actions sort by:

```text
(action_priority ASC, agent_id ASC, client_action_sequence ASC, action_id ASC)
```

`action_priority` is assigned from the pinned world-rules table. Clients MUST NOT supply it. Gateway arrival order, wall-clock time, socket scheduling, and network latency MUST NOT be reducer inputs.

A stale or reused `client_action_sequence` with a new `idempotency_key` is `CONFLICT`. An exact idempotent retry returns the original result and MUST NOT consume budgets twice.

Replay reconstructs committed order from ledger order. Re-execution from accepted actions sorts the recorded canonical keys and MUST produce the same event order regardless of recorded receive timestamps.

Same-cycle conflict table (from SCHEDULER.md):

| Case | Rule |
|------|------|
| Different agents, different resources | both apply in order |
| Different agents, same resource node harvest | first in order wins stock; later rejects without partial debit |
| Trade open + transfer | reservations prevent double spend |
| MOVE vs capacity | first mover occupies; later may `MOVE_REJECTED` / `CAPACITY_EXCEEDED` |
| Duplicate `idempotency_key` | return original result; no second charge |
| Duplicate `action_id`, different key | reject second as `CONFLICT` |

### C. Named seed-stream registry

Every seeded draw MUST use a stream name present in the world's declared registry. Unknown stream name is a **hard fail**: the cycle batch MUST abort; the implementation MUST NOT invent a default stream or fall back to unnamed entropy.

Draws are derived as in ADR-001 / REPLAY.md:

```text
HMAC-SHA-256(world_seed, stream_name || 0x00 || decision_point || 0x00 || draw_index)
```

Bytes convert to values with a versioned rejection-sampling rule, never modulo bias. Stream name, decision point, and monotonically increasing `draw_index` MUST appear in event provenance for every draw.

WED uses only `world_event_director.v1`. Geography (ADR-006 / ADR-007) has **no** seed stream that creates rooms or exits.

A payload field `seed_stream_id`, when present, MUST name a registered stream or the reducer MUST reject.

### D. Canonical `world_state_digest`

`world_state_digest` is SHA-256 over the canonical serialization of the committed canonical `world_state` after the cycle commit, excluding observation payloads, WATCH snapshots, delivery acknowledgements, and research records.

Replay-critical JSON MUST declare `canonicalization_version` `noema-cjson-jcs-digest/v1` and `hash_algorithm` `sha256` when used as replay identity (REPLAY.md). The v0.1 Python acceptance view MAY use sorted-key JSON SHA-256 (`sha256:` prefix) as the fixture digest already published for `examples/v01-seed/`.

Implementations MUST write `world_state_digest`:

- on every snapshot (including genesis snapshot at cycle 0);
- on the cycle commit record / ledger head for **every** cycle.

The contiguous cycle event batch has an `event_batch_digest`. Snapshot heads carry `world_state_digest`, last event sequence, `cycle`, schema version, and world version.

Mismatch is `DIVERGENT`. Missing required digest bytes are `NOT_COMPUTABLE`. Implementations MUST NOT silently substitute a current default.

### E. Replay harness interface

A harness that claims v0.1 world-replay conformance MUST:

1. Load genesis (cycle 0 snapshot) **or** a named snapshot head.
2. Apply the ledger (or the recorded accepted-action set) **cycle-by-cycle** through the versioned reducers.
3. After each cycle, assert `event_batch_digest` and `world_state_digest` when those records exist; at minimum assert the published final-state digest and per-event digest chain (as `replay_v01_seed` does for v01-seed).
4. At each snapshot boundary, assert snapshot head fields match.
5. Emit `EQUIVALENT` only when every required digest matches.

The harness MUST NOT use receive timestamps, live WATCH polls, or PLAY DOM as reduce inputs.

### F. Golden trajectory

v0.1 conformance REQUIRES at least one golden trajectory:

```text
fixed world_version + fixed genesis seed + fixed deterministic_config
+ fixed accepted-action / event script
  → fixed event digests + fixed world_state_digest
```

`examples/v01-seed/` (and the runtime copy `fixtures/v01-seed/`) is the required catalog golden. Re-running the harness MUST be `EQUIVALENT`. Changing receive timestamps MUST still be `EQUIVALENT`. An undeclared stream MUST be `DIVERGENT` or hard-fail. v01-seed is not the hosted play map (ADR-005 / ADR-006).

### G. External inputs only

Reducer-legal external inputs are exactly:

1. World seed streams named in the registry (§C).
2. Ledgered operator injections recorded **before** cycle freeze.
3. Accepted authenticated Player actions in the frozen set.

Wall-clock, network, LLM private cognition, unofficial client prose parsing, WATCH clients, and observation delivery acks are **not** external inputs.

### H. Observation and WATCH are post-commit only

Observation and spectator projections derive from the committed head. That derivation MUST NOT mutate `world_state`, MUST NOT append ledger events, and MUST apply ADR-006 / ADR-007 filters. Changing observation or WATCH bytes without a state change MUST NOT change `world_state_digest`.

## Consequences

Positive: Replay has a single unit (the cycle), a single order key, a hard-fail stream registry, and required digests. Golden trajectories make geography + scheduler + economy comparable. WATCH and observation cannot become a second writer.

Trade-offs: Per-cycle digest has a serialization cost. Unknown streams fail closed. Operator injections must be ledgered before freeze or they do not exist.

Illegal without a later RFC: using receive order as a tie-break; unnamed or implicit random streams; skipping `world_state_digest` except on snapshots; claiming EQUIVALENT after substituting missing bytes; treating WATCH, PLAY DOM, or LLM output as reduce input; creating rooms/exits during replay.

## Implementation notes

1. Pin digest algorithm `sha256` on cycle commit records and snapshot heads.
2. Persist the full order key and session epoch in action provenance.
3. Maintain an explicit stream registry; reject unknown `seed_stream_id` before applying the event reducer.
4. Golden fixture remains `examples/v01-seed/` / `fixtures/v01-seed/`.
5. Geography from ADR-006 / ADR-007 is part of `world_state_digest`. A replay that adds a room is `DIVERGENT`.

Minimal conformance tests:

1. `replay_v01_seed` on the published fixture is `EQUIVALENT`; a second run yields the same `final_state_digest`.
2. Event digest chain (`digest` / `previous_digest`) is intact.
3. Unknown `seed_stream_id` on a payload that carries one is a reducer hard fail.
4. Receive-timestamp fields are not reducer inputs (replaying the same ledger is `EQUIVALENT`).
5. Observation/WATCH-only bytes are excluded from the acceptance-view digest.

## Alternatives considered

**Receive-order reduce.** Rejected. Replay would be a function of the network.

**Digest only on snapshots.** Rejected. The cycle is the replay unit.

**Unknown stream falls back to a default HMAC.** Rejected. Silent substitution is the failure mode REPLAY.md forbids.

**Observation-inclusive state digest.** Rejected. Two observers would diverge the world hash.

**Stochastic-agent output as an implicit reduce input.** Rejected. Private cognition stays off-world (ADR-002).
