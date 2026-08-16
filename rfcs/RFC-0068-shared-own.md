# RFC-0068 — GC2-S11 shared constructible ownership

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No institution-as-Player. Help still omits BUILD. Third-and-later co-owners remain deferred.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `SHARED` ownership. GC2-S10 can vest to an institution. There is no explicit second Player on the same constructible without inventing a joint-title minigame.

## Proposed change

Accept GC2-S11. `BUILD.SHARE` on a live **public** constructible the actor **personally owns** alone:

- Names one other entered Player as `co_owner_id`. Same `entity_id`
- Once. A second SHARE rejects. Institution-owned assets reject
- Hidden rooms, scars, `UNCLAIMED`, and `IN_PROGRESS` reject
- After share, owner and co-owner both steward: `DISMANTLE`, `UPGRADE`, `REPURPOSE`, `RESTORE`, and personal `REPAIR` that stamps `last_steward_cycle`
- Self-share and unknown Player fail closed. Stranger SHARE is `NOT_OWNER`
- `VEST` of a shared asset rejects (institution and shared stay distinct)
- Cost: compute 1. Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `You share the {label} with {handle}.` WATCH silent
- Human alias `share <thing> with <player>` is accepted and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s11.json`](../specs/construction-catalog.gc2-s11.json).  
Slice: [GC2-S11-SHARED.md](../docs/GC2-S11-SHARED.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| N-of-M roster | Extra machinery |
| Share institution assets | Distinct S10 mode |
| Vest after share | Mixes modes |
| Institution-as-Player | ADMIN ≠ Player family |
| `STRUCTURE_SHARED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive `SHARE`. Worlds ignoring S11 keep sole owners.

## Data / security

`co_owner_id` on the existing entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s11`: owner shares with an entered Player; same `entity_id`; hidden / stranger / already-shared reject; no new verbs.

## Rollback

Ignore `SHARE` (`INVALID_REQUEST`).

## Unresolved

CONNECT dest pin is [RFC-0071](RFC-0071-connect-dest.md). Third-and-later co-owners. Other-class multi-cycle.
