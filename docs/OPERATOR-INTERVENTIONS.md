# Operator Interventions

**Authority.** Canonical first-world **control-plane interventions**. Admin intervention is governed system operation, not free-form cheating.

This document is **not** [INTERVENTIONS.md](INTERVENTIONS.md). That file is the v0.4 Lab research taxonomy (`PERTURBATION`, `ABLATION`, …). Do not overload it.

Related: [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) · [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [OPERATIONS.md](OPERATIONS.md) · [GENESIS.md](GENESIS.md).

---

## Canonical rule

> Admin intervention is governed system operation, not free-form cheating.

Operator surfaces MUST NOT bypass the Action Router / declared external-input path for world mutations ([MODULE-CONTRACTS.md](MODULE-CONTRACTS.md)).

---

## Closed classification

First-world uses four classes:

```text
IDENTITY
SYSTEM
WORLD
RECOVERY
```

Do not add arbitrary editing classes.

### IDENTITY

Control-plane access and session control. Does **not** rewrite world history.

```text
terminate session
revoke credential
disable / revoke controller
suspend account
QUARANTINE / REVOKE_QUARANTINE
```

Reuse [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) for quarantine and revocation. Committed actions stay committed.

### SYSTEM

Operational mode of an existing world, without editing Player holdings or rooms.

```text
enter PAUSED (maintenance)
resume ACTIVE
trigger verification (`noema verify` semantics)
KILL_SWITCH
declare / close INCIDENT
```

Reuse [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) and [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

### WORLD

Only **explicit, already-authorized** world-truth operations.

For first world, that set is:

- Genesis create / preview / accept / activate **before** the world is live ([GENESIS.md](GENESIS.md));
- no post-activation free-form world edits.

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
delete event
rewrite trade
edit ledger
change institution membership directly
```

There is no first-world “GM console” that writes WorldState fields.

---

## World-changing path

Any Admin operation that changes world truth MUST follow:

```text
authenticated
  → authorized
  → validated
  → previewed where appropriate
  → confirmed
  → Action Router / declared external input
  → canonical event
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

The audit record MUST include operator principal, class, target (`world_id` / `player_id` / `controller_id` / `session_id` as applicable), reason when required, timestamp, and resulting event or receipt id.

---

## Existing sequences to reuse

Do not invent parallel names for these:

| Sequence | Class | Authority |
|---|---|---|
| Quarantine / revoke quarantine | IDENTITY | SECURITY-SEQUENCES §1 |
| Credential / Controller revocation | IDENTITY | SECURITY-SEQUENCES §2 |
| World-level INCIDENT | SYSTEM | SECURITY-SEQUENCES §3 |
| Kill switch | SYSTEM | SECURITY-SEQUENCES §4 |
| Genesis preview / activate | WORLD (pre-live) | GENESIS |
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
