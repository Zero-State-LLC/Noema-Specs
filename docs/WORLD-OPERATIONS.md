# World Operations

**Authority.** Canonical post-Genesis **world lifecycle** for the first persistent production world.

This document does not replace [GENESIS.md](GENESIS.md), [WORLD-ENGINE.md](WORLD-ENGINE.md), [OPERATIONS.md](OPERATIONS.md), or `World.status` in [`world-state.schema.json`](../specs/world-state.schema.json).

Related: [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [DEPLOYMENT.md](DEPLOYMENT.md) · [PLATFORM.md](PLATFORM.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md).

---

## Governing rule

Application lifecycle and world lifecycle are **separate** ([OPERATIONS.md](OPERATIONS.md), [DEPLOYMENT.md](DEPLOYMENT.md)).

A code deployment or process restart MUST NOT reset the world, economy, Players, organizations, cycles, or ledger.

---

## Canonical world status (do not fork)

Machine `World.status` remains the frozen enum:

```text
ACTIVE
PAUSED
INCIDENT
ARCHIVED
```

First-world operations MUST use this enum. Do **not** add `RUNNING`, `MAINTENANCE`, `DEGRADED`, or `RECOVERING` to `World.status` without an RFC and schema change.

Genesis **PREVIEW** is a pre-activation admin step. It is **not** a `World.status` value.

---

## Operational envelope

```text
PREVIEW          Genesis candidate exists; not world truth
    ↓ ACCEPT + ACTIVATE
ACTIVE           Canonical world exists; Players may enter
    ↓ operator maintenance
PAUSED           World authority exists; mutating PLAY suspended
    ↓ resume
ACTIVE

ACTIVE
    ↓ required property unhealthy, PLAY still possible
ACTIVE + DEGRADED health
    ↓ PLAY must stop or authority is unsafe
INCIDENT         Fail-closed containment / recovery
    ↓ reconciled
ACTIVE
    ↓ or terminal
ARCHIVED
```

`RUNNING` is not a first-world status. After activation, the live term is `ACTIVE`.

---

## States

### PREVIEW

Genesis candidate exists but is **not** world truth.

- Admin may generate, inspect, regenerate (new `genesis_id` when claim-bearing inputs change), accept, or reject ([GENESIS.md](GENESIS.md)).
- Players, spectators, and researchers MUST NOT enter the candidate as a live world.
- Activation freezes Genesis configuration.

### ACTIVE

Canonical world exists. Players MAY enter and submit mutating actions when `/ready` passes and health is not `PLAY_BLOCKED`.

This is the first-world “the world is up” state. Do not also say `RUNNING`.

### PAUSED

World authority exists, but normal Player mutations are **intentionally** suspended.

First-world uses `PAUSED` as the maintenance window. There is no separate `MAINTENANCE` or `PAUSE` status.

Semantics:

```text
world canonical state preserved
new mutating Player actions rejected
already-accepted in-flight reductions complete or fail by existing idempotency rules
read-only inspection MAY continue
WATCH MAY continue with a maintenance marker
Admin Live remains available
new controlling sessions MUST NOT open for PLAY mutation
```

`PAUSED` is an operator SYSTEM intervention ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)). It is not implied by a deploy, a disconnect, or a single failed request.

Queued-for-later-execution of mutating Player actions during `PAUSED` is **not** first-world policy. Reject, do not silently queue.

### INCIDENT

A required operational property is unsafe or authority is ambiguous. This is the fail-closed world status from [WORLD-ENGINE.md](WORLD-ENGINE.md) and [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

While `INCIDENT`:

- new mutating PLAY is rejected or restricted by the declared incident policy;
- new ENTRY is suspended or diverted;
- writer fencing is checked before any further canonical mutation;
- recovery follows [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md);
- resolution is `ACTIVE` or `ARCHIVED`, with a closing event and audit evidence.

`RECOVERING` is the **procedure** executed while status is `INCIDENT`. It is not a second status.

### ARCHIVED

Terminal. The world is no longer a live play surface. History, backups, and research records remain according to existing retention and evidence rules.

First-world does not require an archive workflow beyond this definition. Do not add extra terminal states.

---

## Health overlay (not World.status)

Operational health is a derived overlay. It MUST NOT replace `World.status`.

| Health | Meaning | Typical status |
|---|---|---|
| `HEALTHY` | Required live, settlement, and auth properties agree | `ACTIVE` |
| `DEGRADED` | A required property is unhealthy, but bounded PLAY may continue | `ACTIVE` |
| `PLAY_BLOCKED` | New mutating Player actions MUST be rejected | `PAUSED` or `INCIDENT` |
| `RECOVERY_REQUIRED` | Authority is ambiguous or ledger integrity failed | `INCIDENT` |

A ledger/digest mismatch is always `RECOVERY_REQUIRED` ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)).

Admin Live SHOULD show both status and health, for example `ACTIVE` + `DEGRADED`.

---

## Pause / maintenance

Admin MAY pause a live world by setting `World.status` to `PAUSED`.

That is the first-world pause. Exact meaning is the `PAUSED` section above.

Do not implement a second “soft pause” that leaves status `ACTIVE` while silently dropping mutations.

Resume is an authenticated SYSTEM intervention that returns status to `ACTIVE` only when `noema verify` semantics pass for the live/settled pair required by [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md).

---

## Deployment behavior

Routine deployment answers:

| Question | First-world rule |
|---|---|
| Can existing world authority continue? | Yes, if the new Worker / runtime pin is compatible with the world's runtime manifest. |
| Can new sessions enter? | Yes, if status is `ACTIVE`, `/ready` passes, and health is not `PLAY_BLOCKED`. |
| What happens to in-flight actions? | Already-accepted actions finish under existing idempotency. Unaccepted requests fail or retry; they MUST NOT double-apply. |
| What does readiness report? | `/health` = process up. `/ready` = world loadable, writer unambiguous, pins compatible, settlement within bound. `/version` = product/spec/protocol/world pins. |
| What if Worker version changes? | Compatible Workers MAY serve the existing Durable Object / world. Incompatible code MUST fail closed and MUST NOT mutate the existing world. |

Incompatible `world_rules_version`, event-catalog semantics, or spec pins MUST fail closed or require an explicit migration to a new `world_version` ([OPERATIONS.md](OPERATIONS.md)). Silent semantic adoption is forbidden.

Hosted shape remains Cloudflare Workers + one Stage 0 Durable Object per world, with settlement to Supabase Postgres ([PLATFORM.md](PLATFORM.md)). Local reference deployments remain the modular monolith with one fenced writer ([DEPLOYMENT.md](DEPLOYMENT.md)).

A Worker or Durable Object code change is an application lifecycle event. It is not a Genesis rerun and MUST NOT invent a new `world_id`.

---

## Writer and persistence

Each `world_id` MUST have exactly one active fenced canonical writer.

- Hosted live authority: World Durable Object.
- Durable history: settled Postgres ledger.
- Local reference: one fenced Postgres writer.

These lanes MUST NOT silently diverge. If live and settled heads disagree beyond the settlement bound, health becomes `RECOVERY_REQUIRED` and status MUST enter `INCIDENT`.

Crash reconciliation outcomes remain `CLEAN`, `REDELIVER_ONLY`, and `FAIL_CLOSED` ([OPERATIONS.md](OPERATIONS.md)).

---

## Backup and restore

Do not create a second backup system. Use [OPERATIONS.md](OPERATIONS.md):

```text
noema backup
noema restore <bundle>
noema verify
```

Restore MUST preserve `world_id` + `world_version` identity, refuse incompatible lineage without explicit migration, acquire a **fresh** writer fence, and pass `noema verify` before mutating traffic.

---

## Acceptance

1. After Genesis activation, the live term is `ACTIVE`, not `RUNNING` or `PREVIEW`.
2. `PAUSED` preserves canonical state and rejects new mutating PLAY.
3. `INCIDENT` fail-closes mutating PLAY until reconciled.
4. Deploy/restart does not reset world identity or history.
5. Incompatible Worker / rules pins fail closed.
6. Backup/restore remain the existing OPERATIONS commands.

---

## Non-goals

- Multi-world orchestration
- Extra status values in `world-state.schema.json`
- Disposable worlds
- Queuing mutating PLAY through a maintenance window
