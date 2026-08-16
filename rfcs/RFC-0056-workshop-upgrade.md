# RFC-0056 — GC2-S5 workshop UPGRADE

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `STRUCTURE_UPGRADED`. No `event-catalog/0.3`. No CONNECT.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `UPGRADE` as a distinct operation. GC2-S2 workshops always save 1 storage. There is no way to increase a built dimension without dismantling.

## Proposed change

Accept GC2-S5. Add `BUILD` operation `UPGRADE` for a live public **workshop** the actor owns:

- Cost: energy 4, compute 2, storage 2, influence 1
- Actor co-located. Hidden rooms reject
- Effect: that workshop’s in-room CONSTRUCT/REPAIR storage save becomes **2**. Once (`tier` 0 → 1). Second UPGRADE is `FORBIDDEN`
- Other classes are not valid UPGRADE targets
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say the workshop was upgraded. WATCH silent
- Human alias `upgrade <workshop>` is accepted and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s5.json`](../specs/construction-catalog.gc2-s5.json).  
Slice: [GC2-S5-UPGRADE.md](../docs/GC2-S5-UPGRADE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Upgrade every class | Second dimension |
| Defensive millipoints / relay condition | Other class |
| `STRUCTURE_UPGRADED` | Extra catalog |
| CONNECT as UPGRADE | Hidden topology |
| Help BUILD | S0 pin |
| Repeatable UPGRADE | Unbounded power |

## Compatibility

Additive operation. Worlds ignoring S5 keep workshop save 1.

## Data / security

`upgrade_tier` on the workshop entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s5`: owned public workshop upgrades once; storage save 2; hidden / other class / second upgrade reject; no new verbs; no STRUCTURE_*.

## Rollback

Ignore `UPGRADE` (`INVALID_REQUEST`). Workshop save stays 1.

## Unresolved

REPURPOSE. Abandonment. RESTORE. CONNECT. Multi-cycle.
