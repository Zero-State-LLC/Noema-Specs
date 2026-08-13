# RFC-0013 — GC9-S0 Maintenance Custom from Repeated Repair

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog` expansion. No v0.6C. No runtime implementation in this RFC.

## Problem

[EMERGENT-CULTURE.md](../docs/EMERGENT-CULTURE.md) forbids a lore generator but left emergence threshold, PLAY projection, and “lore cannot override ledger” fixtures as SPEC GAP. An implementation agent would invent `RITUAL` or write culture into the ledger.

## Proposed change

Accept GC9-S0: a derived `CUSTOM` from ≥ 3 distinct `ENTITY_UPDATE` condition/repair events on one infrastructure entity.

- PLAY line only for Players who repaired or inspected that entity
- Later `INSPECT` inherits the line
- Lore claims cannot delete or override the events
- WATCH empty; no ledger write
- Reuse `semantic-lineage/0.6` kind `CUSTOM` as the name of the derived state, not a new engine

Catalog: [`culture-catalog.gc9-s0.json`](../specs/culture-catalog.gc9-s0.json).  
Slice: [GC9-FIRST-SLICE.md](../docs/GC9-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Procedural lore generator | Spec freeze + parent |
| Start v0.6C here | Distinct later package |
| RITUAL verb | Verb inflation; repair already exists |
| Custom as WorldState | Would compete with the ledger |

## Compatibility

Additive derived projection. `COMMIT.REPAIR` and `semantic-lineage/0.6` stay unchanged.

## Data / security

Rebuildable cache. Projection must not claim physics, grant authority, or leak hidden entity internals.

## Validation

`check_gc9_s0`: three repairs + later inspect → custom line; two repairs silent; no-access silent; lore claim cannot override; no events written.

## Rollback

Omit the projection.

## Unresolved

GC9-S1: tradition / institution adoption; mutation and revival classes; PLAY names without a second canon.
