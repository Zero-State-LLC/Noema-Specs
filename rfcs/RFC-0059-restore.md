# RFC-0059 — GC2-S8 RESTORE

## Status

**Accepted**

No new verbs. No `STRUCTURE_RESTORED`. No `event-catalog/0.3`. No scar restore.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) allows `RESTORE` of abandoned constructibles. GC2-S7 can leave `UNCLAIMED` assets that only DISMANTLE can touch. An implementer would revive GC10-S2 scars or let strangers reclaim.

## Proposed change

Accept GC2-S8. Add `BUILD` operation `RESTORE` for a live **public UNCLAIMED** constructible the actor **owns**:

- Not a GC10-S2 scar / `RUIN`. Scars stay irreparable
- Hidden rooms reject
- Cost equals that class’s `CONSTRUCT` cost (no workshop discount)
- Effect: clear `unclaimed`; stamp `last_steward_cycle`; condition becomes `min(current, 50)`; same `entity_id` and class
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `STRUCTURE_*`
- PLAY MAY say `You restored the {label}.` WATCH silent
- Human alias `restore <thing>` is accepted and **not** listed in Chamber help

Catalog: [`construction-catalog.gc2-s8.json`](../specs/construction-catalog.gc2-s8.json).  
Slice: [GC2-S8-RESTORE.md](../docs/GC2-S8-RESTORE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Restore scars | GC10-S2 irreparable |
| Stranger reclaim | Owner-only pin |
| New `entity_id` / new class | Attribution / catalog |
| `STRUCTURE_RESTORED` | Extra catalog |
| Help BUILD | S0 pin |

## Compatibility

Additive operation. Worlds ignoring S8 keep UNCLAIMED until DISMANTLE.

## Data / security

Clears `unclaimed` on the existing entity. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s8`: owner restores UNCLAIMED; condition capped at 50; hidden / scar / stranger / claimed reject; no new verbs.

## Rollback

Ignore `RESTORE` (`INVALID_REQUEST`).

## Unresolved

CONNECT. Institution ownership is [RFC-0067](RFC-0067-institution-own.md). Shared ownership.
