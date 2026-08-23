# RFC-0058 — GC2-S7 abandonment

## Status

**Accepted**

No new verbs. No `STRUCTURE_ABANDONED`. No `event-catalog/0.3`. No scar on the abandon transition.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) says neglect after a versioned window makes a constructible `UNCLAIMED`. GC2-S6 can change class but a deserted workshop stays owned forever.

## Proposed change

Accept GC2-S7. After **12** committed cycles with no owner `REPAIR` or `UPGRADE`, a live **public** constructible becomes `UNCLAIMED`:

- Stamp `last_steward_cycle` on `CONSTRUCT`, owner `REPAIR`, and `UPGRADE`
- Hidden rooms never abandon
- Genesis / unstamped assets never abandon
- The entity stays. Owner id is kept for later RESTORE. No evict. No delete. No scar
- Anyone colocated may `DISMANTLE` an `UNCLAIMED` asset (existing salvage + public scar rules)
- Events: `ENTITY_UPDATE` with `unclaimed=true`. No `STRUCTURE_*`
- PLAY MAY say `The {label} is unclaimed.` WATCH silent

Catalog: [`construction-catalog.gc2-s7.json`](../specs/construction-catalog.gc2-s7.json).  
Slice: [GC2-S7-ABANDON.md](../docs/GC2-S7-ABANDON.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Auto-delete | History loss |
| Scar on abandon | Confuses GC10-S2 DISMANTLE scars |
| Evict the Player | Unrelated |
| Hidden-room abandon | Hidden leak |
| WATCH ticker | Spectator leak |

## Compatibility

Additive flag. Worlds ignoring S7 keep perpetual ownership.

## Data / security

`unclaimed` plus `last_steward_cycle` on the entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s7`: 12 idle cycles → UNCLAIMED; 11 stay owned; hidden never; owner REPAIR resets; anyone may DISMANTLE UNCLAIMED.

## Rollback

Ignore `unclaimed`. Ownership stays.

## Unresolved

CONNECT. Multi-cycle. RESTORE is RFC-0059.
