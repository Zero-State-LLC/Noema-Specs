# Incident Recovery

**Authority.** First-world behavior when a required operational property fails. This is platform recovery, not gameplay [LOSS-RECOVERY.md](LOSS-RECOVERY.md).

Reuse [OPERATIONS.md](OPERATIONS.md) crash outcomes, [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) INCIDENT / kill-switch sequences, and [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) status/health. Do not create a second backup system or an enterprise incident framework.

Related: [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [PLATFORM.md](PLATFORM.md) · [DEPLOYMENT.md](DEPLOYMENT.md) · [SECURITY.md](SECURITY.md).

---

## Failure hierarchy

Classify first-world incidents with three health values. They overlay `World.status`; they do not replace it.

```text
DEGRADED
PLAY_BLOCKED
RECOVERY_REQUIRED
```

| Class | Meaning | Mutating PLAY | Typical status |
|---|---|---|---|
| `DEGRADED` | A required property is unhealthy; authority is still unambiguous | MAY continue only inside the explicit bound below | `ACTIVE` |
| `PLAY_BLOCKED` | New mutating Player actions MUST be rejected | No | `PAUSED` or `INCIDENT` |
| `RECOVERY_REQUIRED` | Canonical authority is ambiguous or integrity failed | No | `INCIDENT` |

Fail closed when world authority is ambiguous. Do not best-effort-repair history.

Settlement lag uses the same overlay with these operator labels:

| Settlement | Meaning | Mutation |
|---|---|---|
| `HEALTHY` | Live and settled heads agree within the current batch | Allowed if world is `ACTIVE` |
| `DEGRADED` | Durable settle failed; still inside the one-batch bound | Allowed only for that bound |
| `BLOCKING` | Bound exceeded, or heads disagree | Stop. `PLAY_BLOCKED` or `RECOVERY_REQUIRED` |

---

## Failure matrix

| Failure | PLAY | WATCH | STUDY | ADMIN | World mutation | Recovery action |
|---|---|---|---|---|---|---|
| Durable Object unavailable | Reject new mutations | Last settled + stale marker | Read settled evidence only | Report unavailable / degraded | Blocked | Restore from last verified settled head; do not invent a fallback world |
| Supabase settlement unavailable | Allowed for at most one mutating cycle batch, then reject | Last settled + stale after bound | Read settled evidence; do not treat unsettled live as evidence | Show settlement `DEGRADED` then `BLOCKING` | Bounded then blocked | Retry idempotent settle; then `INCIDENT` / restore |
| Settlement lag (`DEGRADED`) | Continue only inside the bound | May show live with unsettled marker | Do not promote unsettled events to evidence | Alert | Inside bound only | Catch up or fail closed |
| Ledger / digest mismatch | Reject | Last verified snapshot only | Confound if a run is in progress | `RECOVERY_REQUIRED` | Blocked | Restore / reconcile; never pick the prettier digest |
| Auth provider unavailable | Existing valid sessions until expiry; no new login | Public/anonymous WATCH if already permitted | Existing authorized sessions until expiry | Fail closed if Admin depends on the provider | Existing scoped sessions only | Out-of-band restore access; no auth bypass |
| Failed / incompatible deploy | Reject if pins disagree | Stale/maintenance marker | Isolated research only | Report pin mismatch | Blocked | Roll back compatible build or restore pre-migration backup |
| Partial migration | Reject | Stale | Confound | `RECOVERY_REQUIRED` | Blocked | Restore pre-migration bundle |
| Snapshot / recovery mismatch | Reject | Last verified ledger projection | Confound | `RECOVERY_REQUIRED` | Blocked | Rebuild snapshot from verified ledger or restore |
| Research subsystem failure (Frontier / Observatory / LEARN / Compiler) | **Unaffected** if world authority is healthy | Unaffected public WATCH | STUDY/research overlay degraded or blocked | Research overlay `Blocked` | Unchanged | Repair research pipeline; do not pause PLAY |

```text
PLAY readiness
≠
optional research readiness
```

A failed Frontier, Observatory, Lab derivation, Compiler, or LEARN rebuild MUST NOT, by itself, stop gameplay or force `PAUSED` / `INCIDENT`.

Critical operational alerts fire **immediately**. Periodic [Operator Digests](OPERATOR-DIGESTS.md) still cover the window and reference the incident. Digest or email delivery failure is `DIGEST_DELIVERY_DEGRADED`, not a gameplay `INCIDENT`, and MUST NOT pause PLAY.

---

## Durable Object unavailable

Hosted live authority is the World Durable Object ([PLATFORM.md](PLATFORM.md)).

| Question | First-world rule |
|---|---|
| What becomes unavailable? | Live command serialization, new mutating PLAY, live connection coordination. |
| Can WATCH show last settled state? | Yes. Project from the last verified settled ledger / snapshot and mark the view **stale**. |
| Does PLAY reject mutations? | Yes. New mutating actions fail closed. |
| How does recovery select canonical state? | Last `noema verify`-passing settled head + compatible snapshot. If DO memory and settled head disagree, `RECOVERY_REQUIRED`. |

Admin Live MAY remain available for read-only inspection of settled state and alerts.

Do not invent a replacement world from WATCH projections.

---

## Supabase settlement outage

If the live Durable Object is healthy but durable settlement (Postgres / Storage as required) is unavailable:

First-world policy is **bounded fail-closed**, not unlimited un-settled mutation.

| Question | First-world rule |
|---|---|
| May world mutation continue? | Only for **at most one additional mutating cycle batch** after the first failed settlement attempt of a durable event. |
| For how long? | That single bounded batch, then stop. Wall-clock retry of the failed settle MAY continue without accepting new mutations. |
| Must settlement catch up before more actions? | Yes, after the bound. No further mutating PLAY until the unsettled durable events are confirmed or the world is restored. |
| When does readiness fail? | `/ready` MUST fail as soon as the bound is reached, and SHOULD fail earlier if settlement has been unconfirmed for the entire current batch. |

During the bound:

- retain durable event candidates with idempotent `event_id`;
- mark unsettled backlog;
- never invent compensating world rewrites;
- Admin Live MUST show settlement `DEGRADED`.

After the bound:

- health `PLAY_BLOCKED` or `RECOVERY_REQUIRED`;
- status `INCIDENT` unless an operator has already set `PAUSED` for maintenance;
- WATCH MAY continue from last settled state with a stale marker.

Local reference deployments that use Postgres as the fenced writer already fail closed when the database is unavailable. They MUST NOT accept mutating traffic without the writer fence ([DEPLOYMENT.md](DEPLOYMENT.md)).

---

## Ledger mismatch

A ledger / digest / snapshot-head mismatch is:

```text
RECOVERY_REQUIRED
```

No ordinary PLAY mutation may continue until authority is reconciled.

Crash reconciliation remains:

1. `CLEAN` — resume.
2. `REDELIVER_ONLY` — rebuild delivery from committed observations/events.
3. `FAIL_CLOSED` — enter `INCIDENT`; restore or migrate.

Forbidden: synthesizing events, truncating the ledger, reusing sequences, marking unverified reservations spent, or blind-retrying an ambiguous mutating request ([OPERATIONS.md](OPERATIONS.md)).

---

## Auth outage

Supabase Auth (or the configured managed provider) is identity **proof**, not a bypass hatch.

| Principal | During auth-provider outage |
|---|---|
| Existing valid sessions | MAY continue until the session or access credential expires. Do not extend silently. |
| New sessions | Fail closed. |
| Admin access that depends on the provider | Fail closed. |
| Agent controllers with valid unexpired controller credentials | MAY continue until expiry. Enrollment, refresh, and new credentials fail closed. |

Do **not** silently bypass authentication, accept unsigned tokens, or fall back to a shared emergency Player.

If Admin cannot authenticate, recovery uses out-of-band operator access already required to run `noema restore` / infrastructure controls — not a backdoor on the public Worker.

---

## Failed or incompatible deployment

Incompatible Worker, runtime, spec, catalog, or `world_rules_version` pins MUST NOT mutate an existing world.

Required behavior:

1. Fail closed on boot or first mutating request against the existing world.
2. Keep the previous compatible deployment serving, or leave the world `INCIDENT` / not ready.
3. If a migration partially applied, restore from the pre-migration backup bundle ([OPERATIONS.md](OPERATIONS.md)).
4. Run `noema verify`.
5. Only then acquire a fresh writer fence and resume `ACTIVE`.

A partial deployment that leaves mixed Worker versions against one `world_id` is `PLAY_BLOCKED` until a single compatible version is authoritative.

---

## Snapshot mismatch and failed migration

| Failure | Class | Action |
|---|---|---|
| Snapshot digest does not match ledger head | `RECOVERY_REQUIRED` | Fail closed; restore or rebuild snapshot from verified ledger. Do not pick the prettier digest. |
| Failed migration | `RECOVERY_REQUIRED` | Restore pre-migration bundle; do not complete a half-applied semantic change. |
| Configuration digest mismatch (non-secret pins) | `PLAY_BLOCKED` until explained | Incompatible pins fail closed; compatible config drift is operator-reviewed. |

---

## Configuration mismatch

Resolved non-secret configuration MUST validate against [`deployment-config.schema.json`](../specs/deployment-config.schema.json). The running world MUST match the runtime-manifest pins.

If pins disagree with the loaded world:

- do not adopt new semantics silently;
- `/ready` fails;
- mutating PLAY is rejected.

---

## Backup and restore alignment

There is one backup system: [OPERATIONS.md](OPERATIONS.md).

| Question | Rule |
|---|---|
| When do backups occur? | Before migration, before production Genesis activation, and on the operator's declared schedule. First-world SHOULD take a verify-passing backup immediately after successful activation and before any incompatible deploy. |
| What must be verified? | The `noema verify` checklist: config, connectivity, schema/spec pins, ledger and snapshot integrity, writer uniqueness, persistence atomicity, bounded resume windows, required evidence receipts. |
| What does restore mean? | Install the bundle into a clean compatible environment; preserve `world_id` + `world_version`; do not invent a new Genesis. |
| How is world identity preserved? | Restore MUST refuse to mint a new genesis for an existing `world_id` + `world_version`. |
| How is post-restore authority checked? | Fresh writer fence + `noema verify` PASS before mutating traffic. Replay under ADR-005 remains `EQUIVALENT` when fixtures are included. |
| What identity does a backup contain? | `world_id`, `world_version`, pins, ledger, snapshots, runtime manifest, non-secret config digest — not secrets ([OPERATIONS.md](OPERATIONS.md)). |
| What happens to world authority during restore? | No active writer until verify passes and a **fresh** fence is acquired. |

Restore is never a one-click Admin Live action:

```text
ADMIN
  → select backup
  → verify bundle
  → PAUSED or INCIDENT
  → restore
  → verify canonical identity (world_id + world_version + digest lineage)
  → noema verify PASS
  → acquire fresh writer fence
  → readiness / ACTIVE
```

---

## Player-visible and WATCH behavior

During `PAUSED` or `INCIDENT`:

- PLAY MUST reject new mutating actions with a stable, plain-language error plus a machine code;
- WATCH MAY continue with an explicit maintenance / stale / incident marker;
- STUDY MUST NOT treat a degraded or restored world as a new experiment without recording the incident as a confound when research is in progress.

Do not fabricate world events to explain the outage.

---

## Acceptance

1. DO unavailability rejects PLAY mutations and allows stale settled WATCH.
2. Settlement outage permits at most one additional mutating cycle batch, then fail closed.
3. Ledger mismatch is `RECOVERY_REQUIRED` with no ordinary PLAY.
4. Auth outage does not mint anonymous sessions or extend expired ones.
5. Incompatible Workers cannot mutate an existing world.
6. Restore uses OPERATIONS and preserves world identity.
7. Research-subsystem failure does not, by itself, stop PLAY.

---

## Non-goals

- PagerDuty-style severity matrices
- Unlimited live mutation during durable outage
- A second snapshot or backup format
- Silent ledger surgery
