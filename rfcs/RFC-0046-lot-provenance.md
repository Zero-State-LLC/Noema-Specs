# RFC-0046 — GC8-S2 Lot Provenance

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No hidden-room leak. No currency.

## Problem

[ECONOMIC-SPECIALIZATION.md](../docs/ECONOMIC-SPECIALIZATION.md) allows lots to carry origin room / producer if that enables archive or quality play. GC8-S1 grades stacks but not where they came from. An implementer would stamp hidden room ids onto TRADE or WATCH.

## Proposed change

Accept GC8-S2:

- HARVEST from a **public** room stamps `origin_room_id` + `producer_id` on that resource stack
- HARVEST in a hidden room stamps **nothing** (same as unknown)
- Mixing two different public origins **clears** the stamp (mixed, not a third name)
- Same origin keeps the stamp. Spending a stack to 0 clears it
- TRADE carries the offered stamp; the recipient mixes
- PLAY MAY say `Your energy is from {public room name}.` WATCH does not
- Grades (SOUND/WORN) unchanged. No yield bonus

Catalog: [`economy-catalog.gc8-s2.json`](../specs/economy-catalog.gc8-s2.json).  
Slice: [GC8-S2-PROVENANCE.md](../docs/GC8-S2-PROVENANCE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Stamp hidden rooms | Leak |
| WATCH origin ticker | Spectator leak |
| Keep both origins as a list | Inventory minigame |
| Storage spoilage | Separate |

## Compatibility

Additive origin cache. Worlds ignoring S2 keep S1 grades only.

## Data / security

Optional `lot_origins` on the Player cache. Hidden `room_id` MUST NOT be stored or shown.

## Validation

`check_gc8_s2`: public harvest stamps; hidden harvest empty; mixed origins clear; no hidden id; no new verbs.

## Rollback

Ignore origins.

## Unresolved

Storage spoilage. Transport table. v0.6B.
