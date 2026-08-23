# RFC-0087 — GC2-S23 fifth co-owner

## Status

**Accepted**

No `STRUCTURE_*`. No `event-catalog/0.3`. No institution-as-Player. Help still omits BUILD. Sixth-and-later co-owners remain deferred. N-of-M roster stays closed.

## Problem

[GC2-S22-FOURTH-CO-OWNER.md](../docs/GC2-S22-FOURTH-CO-OWNER.md) names four co-owners. [CONSTRUCTION.md](../docs/CONSTRUCTION.md) still lists later shared ownership. An implementer would invent a roster, votes, or institution-as-Player.

## Proposed change

Accept GC2-S23. `BUILD.SHARE` on a live **public** constructible the actor **personally owns**:

- First SHARE still sets `co_owner_id` ([RFC-0068](RFC-0068-shared-own.md))
- Second SHARE still sets `co_owner_2_id` ([RFC-0079](RFC-0079-second-co-owner.md))
- Third SHARE still sets `co_owner_3_id` ([RFC-0085](RFC-0085-third-co-owner.md))
- Fourth SHARE still sets `co_owner_4_id` ([RFC-0086](RFC-0086-fourth-co-owner.md))
- A fifth SHARE names one other entered Player as `co_owner_5_id`. Same `entity_id`
- Partner MUST NOT already be owner, `co_owner_id`, `co_owner_2_id`, `co_owner_3_id`, `co_owner_4_id`, or `co_owner_5_id`
- A sixth SHARE rejects (`FORBIDDEN`). Institution-owned assets still reject
- Hidden rooms, scars, `UNCLAIMED`, and `IN_PROGRESS` still reject
- After the fifth share, owner and all five co-owners steward
- A co-owner still cannot SHARE (`NOT_OWNER`)
- `VEST` of a shared asset still rejects
- Cost: compute 1. Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `You share the {label} with {handle}.` WATCH silent
- Human alias unchanged and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s23.json`](../specs/construction-catalog.gc2-s23.json).  
Slice: [GC2-S23-FIFTH-CO-OWNER.md](../docs/GC2-S23-FIFTH-CO-OWNER.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| N-of-M roster | Extra machinery |
| Sixth-and-later in this slice | Out of slice |
| Co-owner may SHARE | Owner remains the namer |
| Share institution assets | S10/S11 pin |
| Vest after share | Mixes modes |
| Institution-as-Player | ADMIN ≠ Player family |
| `STRUCTURE_SHARED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive fifth stamp. Worlds ignoring S23 keep S22’s four-co-owner cap.

## Data / security

`co_owner_5_id` on the existing entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s23`: owner shares a fifth entered Player; same `entity_id`; hidden / stranger / sixth reject; no new verbs.

## Rollback

Ignore `co_owner_5_id` (treat a fifth SHARE as already shared).

## Unresolved

SHARE family closeout is [RFC-0089](RFC-0089-share-closeout.md).
