# Operator Interventions

**Authority.** Canonical first-world **control-plane interventions**. Admin intervention is governed system operation, not free-form cheating.

This document is **not** [INTERVENTIONS.md](INTERVENTIONS.md). That file is the v0.4 Lab research taxonomy (`PERTURBATION`, `ABLATION`, …). Do not overload it.

Related: [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) · [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [OPERATIONS.md](OPERATIONS.md) · [GENESIS.md](GENESIS.md).

---

## Canonical rule

> Administrative authority is not arbitrary world-edit authority.

Admin Live supports `OBSERVE` / `INSPECT` / `DIAGNOSE` / `OPERATE` / `AUDIT` ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)). Default Admin Live is observational:

```text
OBSERVE
INSPECT
DIAGNOSE
AUDIT (read-only)
```

`OPERATE` is never the landing mode. World-changing operations require an explicit governed path. Operator surfaces MUST NOT bypass the Action Router / declared external-input path for world mutations ([MODULE-CONTRACTS.md](MODULE-CONTRACTS.md)).

---

## Closed classification

First-world uses four classes:

```text
CONTROL_PLANE
WORLD_OPERATION
EXTERNAL_INPUT
RECOVERY
```

Do not add arbitrary editing classes. Earlier IDENTITY / SYSTEM / WORLD labels map onto this closed set; do not keep a second taxonomy.

Consequential operator **receipts** (id, actor, cycle, class, reason, target, pre/post, authority, incident/experiment) map `class` onto these four. Causal labels MAINTENANCE / EXPERIMENTAL / EMERGENCY in [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md) are receipt semantics, not a fifth closed taxonomy.

### CONTROL_PLANE

Access, session, and operational mode. Does **not** rewrite world history.

```text
revoke credential
terminate session
disable / revoke controller
suspend account
QUARANTINE / REVOKE_QUARANTINE
enter PAUSED (maintenance)
resume ACTIVE
trigger verification (`noema verify` semantics)
KILL_SWITCH
declare / close INCIDENT
```

Reuse [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) and [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md). Committed actions stay committed.

### WORLD_OPERATION

Only if canonical operator semantics already exist.

For first world, that set is:

- Genesis create / preview / accept / activate **before** the world is live ([GENESIS.md](GENESIS.md));
- no post-activation free-form world edits.

### EXTERNAL_INPUT

A declared input entering through governed world contracts (Action Router / declared external input), never a dashboard field poke.

`SITUATION_INJECTED` remains a Frontier/catalog event with its own contract. It is **not** a first-world Admin Live cheat code and MUST NOT be exposed as “spawn content.”

### RECOVERY

Restore and reconcile existing authority.

```text
restore from backup
reconcile crash / writer fence
recover settlement
fail closed pending restore
```

Reuse [OPERATIONS.md](OPERATIONS.md) and [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Recovery MUST NOT invent replacement events or truncate the ledger except via an RFC-approved disaster procedure.

---

## Prohibited direct world edits

The following raw Admin operations are **forbidden** unless represented as a canonical authorized operation that already exists:

```text
set Player energy
teleport Player
delete trade
rewrite ledger
edit institution membership
change infrastructure condition directly
delete history
delete event
```

There is no first-world “GM console” that writes WorldState fields.

---

## World-changing path

Any Admin operation that changes world truth MUST follow:

```text
AdminPrincipal
  → authorized operation
  → validation
  → consequence preview
  → confirmation
  → Action Router / declared recovery path
  → canonical result
  → audit receipt
```

Never direct WorldState mutation. Never a silent Durable Object field poke. Never a SQL update of ledger rows.

Read-only Admin Live inspection is **not** a world-changing operation and does not use this path.

---

## Intervention reason

Privileged world-changing interventions and privileged private-message inspection MUST record a concise operator reason.

Example:

```text
reason:
recovering stuck settlement after verified infrastructure failure
```

Ordinary read-only inspection does **not** require a reason.

Store the reason in Admin audit provenance. Do **not** inject reason text into world history unless a canonical event already requires an operator note.

The audit record MUST include operator principal, class, target (`world_id` / `player_id` / `controller_id` / `session_id` as applicable), reason when required, timestamp, and resulting event or receipt id.

---

## Existing sequences to reuse

Do not invent parallel names for these:

| Sequence | Class | Authority |
|---|---|---|
| Quarantine / revoke quarantine | CONTROL_PLANE | SECURITY-SEQUENCES §1 |
| Credential / Controller revocation | CONTROL_PLANE | SECURITY-SEQUENCES §2 |
| World-level INCIDENT | CONTROL_PLANE | SECURITY-SEQUENCES §3 |
| Kill switch | CONTROL_PLANE | SECURITY-SEQUENCES §4 |
| Genesis preview / activate | WORLD_OPERATION (pre-live) | GENESIS |
| Backup / restore / verify | RECOVERY | OPERATIONS |

---

## Acceptance

1. An operator cannot set energy, teleport, delete events, or rewrite trades from Admin Live.
2. World-changing operations are authenticated, authorized, validated, confirmed, routed, ledgered, and receipted.
3. Privileged mutations and message-text inspection require a reason and an audit record.
4. Lab `INTERVENTIONS.md` is unused for live-world ops.
5. Identity disable leaves Player history intact.

---

## Non-goals

- GM_PLAYER / SUPER_PLAYER
- Arbitrary room or ledger editors
- A second intervention taxonomy besides the four classes
- Using Lab perturbations against the production world
