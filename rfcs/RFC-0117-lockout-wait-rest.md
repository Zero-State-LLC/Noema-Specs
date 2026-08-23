# RFC-0117 — Lockout WAIT rest

## Status

**Accepted**

No new Player verbs. AUTH-INFRA-CLASS harvest/move costs unchanged. RFC-0019 WAIT quorum unchanged.

## Problem

Hosted harvest spends free `storage` as capacity (GC8-S4 cargo signal) and costs energy 2. A Player can reach **energy 0 and storage 0**: cargo-full and unable to MOVE (cargo MOVE 2) or HARVEST (energy 2 + free storage 1). WAIT is already free and already rests attention/compute. Without a lockout rest, that Player can only WAIT forever.

Live Perihelion OBSERVED this state on `player.a7a22752ad02` while the world stayed ACTIVE.

## Proposed change

When a Player successfully WAITs and, after that WAIT's cycle-commit side effects, `energy == 0` and `storage == 0`, set:

| Budget | After rest |
|--------|------------|
| `energy` | **2** |
| `storage` | **1** |

- One-shot per such WAIT. Not passive energy regen. Not a new verb.
- Does not change HARVEST/MOVE costs. Does not refill harvest nodes (empty-node regen stays cycle-commit).
- Does not grant energy or storage when only one of the two is zero.
- PLAY MAY say `If you have no energy and no free storage, wait.` WATCH does not.

Catalog: [`economy-catalog.lockout-wait.json`](../specs/economy-catalog.lockout-wait.json).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| DROP / DUMP verb | New verb; freeze |
| Passive energy regen | RESOURCE-ECONOMY energy regen stays 0 |
| Grant on cycle commit only | Cycle can stall if other present actors do not WAIT |
| Flip harvest to capacity-check-not-debit | Live-budget migrate; separate RFC |
| Change MOVE cargo extra | AUTH-INFRA-CLASS / GC8-S4 |

## Compatibility

Additive WAIT rest. Worlds ignoring this RFC keep today's lockout. No event-catalog change.

## Data / security

No new Player fields. Hidden rooms unchanged.

## Validation

`check_rfc_0117`: lockout WAIT grants energy 2 and storage 1; non-lockout WAIT grants neither; no new verbs.

## Rollback

Stop applying the rest. WAIT still free; lockout returns.

## Unresolved

Whether later cargo can convert to energy by TRADE. Whether harvest debit vs capacity-check is migrated.
