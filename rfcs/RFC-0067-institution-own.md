# RFC-0067 — GC2-S10 institution-owned constructibles

## Status

**Accepted**

No `STRUCTURE_*`. No `event-catalog/0.3`. No institution-as-Player. Help still omits BUILD. Shared ownership remains deferred.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `INSTITUTION` ownership. GC2-S0–S9 owner is the creating Player. An implementer would make the org a Player, invent a second property law, or skip office scope.

## Proposed change

Accept GC2-S10. `BUILD.VEST` on a live **public** constructible the actor **personally owns**:

- Actor MUST hold an occupied `OPERATE_NAMED_ASSET` office in `org_id`
- Same `entity_id`. `owner_id` becomes that org
- Hidden rooms, scars, `UNCLAIMED`, and `IN_PROGRESS` reject
- After vest, steward acts are the occupied `OPERATE_NAMED_ASSET` holder: `DISMANTLE`, `UPGRADE`, `REPURPOSE`, `RESTORE`, and `REPAIR` that stamps `last_steward_cycle`
- Vacant office / non-holder / former personal owner: `NOT_OWNER`
- Cost: compute 1. Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `The {label} is held by {org}.` WATCH silent
- Human alias `vest <thing> to <org>` is accepted and **not** listed in Chamber help
- Shared / co-owner records remain deferred

Catalog: [`construction-catalog.gc2-s10.json`](../specs/construction-catalog.gc2-s10.json).  
Slice: [GC2-S10-INSTITUTION.md](../docs/GC2-S10-INSTITUTION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Institution-as-Player | ADMIN ≠ Player family |
| SHARED this slice | Extra record |
| Vest UNCLAIMED / scar / in-progress | Attribution / S8–S9 pins |
| New property law | Use existing office grant |
| `STRUCTURE_VESTED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive `VEST`. Worlds ignoring S10 keep player-only owners.

## Data / security

`owner_id` becomes `org_id`. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s10`: owner+office vests; same `entity_id`; hidden / vacant / stranger reject; no new verbs.

## Rollback

Ignore `VEST` (`INVALID_REQUEST`).

## Unresolved

CONNECT. Shared ownership is [RFC-0068](RFC-0068-shared-own.md). Other-class multi-cycle.
