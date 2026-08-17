# RFC-0085 — GC2-S21 third co-owner

## Status

**Accepted**

Specification-only until hosted. No `STRUCTURE_*`. No `event-catalog/0.3`. No institution-as-Player. Help still omits BUILD. Fourth-and-later co-owners remain deferred. N-of-M roster stays closed.

## Problem

[GC2-S20-SECOND-CO-OWNER.md](../docs/GC2-S20-SECOND-CO-OWNER.md) names two co-owners. [CONSTRUCTION.md](../docs/CONSTRUCTION.md) still lists later shared ownership. An implementer would invent a roster, votes, or institution-as-Player.

## Proposed change

Accept GC2-S21. `BUILD.SHARE` on a live **public** constructible the actor **personally owns**:

- First SHARE still sets `co_owner_id` ([RFC-0068](RFC-0068-shared-own.md))
- Second SHARE still sets `co_owner_2_id` ([RFC-0079](RFC-0079-second-co-owner.md))
- A third SHARE names one other entered Player as `co_owner_3_id`. Same `entity_id`
- Partner MUST NOT already be owner, `co_owner_id`, `co_owner_2_id`, or `co_owner_3_id`
- A fourth SHARE rejects (`FORBIDDEN`). Institution-owned assets still reject
- Hidden rooms, scars, `UNCLAIMED`, and `IN_PROGRESS` still reject
- After the third share, owner and all three co-owners steward
- A co-owner still cannot SHARE (`NOT_OWNER`)
- `VEST` of a shared asset still rejects
- Cost: compute 1. Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `You share the {label} with {handle}.` WATCH silent
- Human alias unchanged and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s21.json`](../specs/construction-catalog.gc2-s21.json).  
Slice: [GC2-S21-THIRD-CO-OWNER.md](../docs/GC2-S21-THIRD-CO-OWNER.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| N-of-M roster | Extra machinery |
| Fourth-and-later in this slice | Out of slice |
| Co-owner may SHARE | Owner remains the namer |
| Share institution assets | S10/S11 pin |
| Vest after share | Mixes modes |
| Institution-as-Player | ADMIN ≠ Player family |
| `STRUCTURE_SHARED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive third stamp. Worlds ignoring S21 keep S20’s two-co-owner cap.

## Data / security

`co_owner_3_id` on the existing entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s21`: owner shares a third entered Player; same `entity_id`; hidden / stranger / fourth reject; no new verbs.

## Rollback

Ignore `co_owner_3_id` (treat a third SHARE as already shared).

## Unresolved

Fourth co-owner is [RFC-0086](RFC-0086-fourth-co-owner.md). Fifth co-owner is [RFC-0087](RFC-0087-fifth-co-owner.md). Sixth-and-later co-owners.
