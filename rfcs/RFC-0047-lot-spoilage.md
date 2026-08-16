# RFC-0047 — GC8-S3 Worn Lot Spoilage

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No currency. No transport table.

## Problem

[ECONOMIC-SPECIALIZATION.md](../docs/ECONOMIC-SPECIALIZATION.md) allows versioned storage loss if it creates logistics roles. GC8-S1 marks WORN lots but they last forever. Hoarding damaged harvest has no cost.

## Proposed change

Accept GC8-S3:

- Only **WORN** holdings spoil. SOUND and ungraded (treated SOUND) never spoil
- On each committed world cycle, each WORN resource stack loses **1**
- Spending a stack to 0 clears grade and origin
- PLAY MAY say `Your worn energy spoiled.` WATCH does not
- Existing `BUDGET_CONSUMED` records the loss. No new events
- HARVEST amounts, MOVE energy, TRADE compute, and REPAIR stay S0/S1/S2

Catalog: [`economy-catalog.gc8-s3.json`](../specs/economy-catalog.gc8-s3.json).  
Slice: [GC8-S3-SPOILAGE.md](../docs/GC8-S3-SPOILAGE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Spoil SOUND | Quality would not matter |
| Per-cycle percent | Floats forbidden; inventory minigame |
| Transport table | Separate |
| Currency / v0.6B | Doctrine |
| WATCH spoilage ticker | Spectator leak |

## Compatibility

Additive cycle loss on the existing WORN cache. Worlds ignoring S3 keep S2 grades/origins.

## Data / security

No new Player fields required beyond S1/S2 caches. Hidden room ids stay unstamped.

## Validation

`check_gc8_s3`: WORN loses 1; SOUND keeps; exhaust clears grade; no currency/transport/new verbs.

## Rollback

Ignore cycle spoilage.

## Unresolved

Transport table. v0.6B.
