# RFC-0057 — GC2-S6 workshop REPURPOSE

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `STRUCTURE_REPURPOSED`. No `event-catalog/0.3`. No CONNECT.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `REPURPOSE` as a distinct operation with a closed conversion table. GC2-S5 can upgrade a workshop but cannot change its function class. An implementer would invent reverse conversions, new events, or hidden rooms.

## Proposed change

Accept GC2-S6. Add `BUILD` operation `REPURPOSE` for a live public **workshop** the actor owns:

- Closed table: `workshop` → `storage_bay` only. Keep the same `entity_id`
- Cost: energy 4, compute 2, storage 2, influence 1
- Actor co-located. Hidden rooms reject
- Other conversions are `FORBIDDEN`
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say the workshop was repurposed as a storage bay. WATCH silent
- Human alias `repurpose <workshop>` is accepted and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s6.json`](../specs/construction-catalog.gc2-s6.json).  
Slice: [GC2-S6-REPURPOSE.md](../docs/GC2-S6-REPURPOSE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Reverse / other conversions | Open table |
| New `entity_id` | Breaks attribution |
| `STRUCTURE_REPURPOSED` | Extra catalog |
| CONNECT as REPURPOSE | Hidden topology |
| Help BUILD | S0 pin |
| Institution-owned constructibles | Out of this slice |

## Compatibility

Additive operation. Worlds ignoring S6 keep workshops as workshops.

## Data / security

Class change is an `ENTITY_UPDATE` on the existing entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s6`: owned public workshop becomes `storage_bay` with the same `entity_id`; hidden / other conversion reject; no new verbs; no STRUCTURE_*.

## Rollback

Ignore `REPURPOSE` (`INVALID_REQUEST`). Workshop class stays.

## Unresolved

CONNECT. Abandonment. RESTORE. Multi-cycle.
