# RFC-0045 — GC8-S1 Lot Quality (SOUND / WORN)

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No currency. No harvest yield bonus. No provenance schema.

## Problem

[ECONOMIC-SPECIALIZATION.md](../docs/ECONOMIC-SPECIALIZATION.md) allows a bounded lot attribute if it changes production or trade. Leaving every harvested unit identical makes damaged nodes only a stock number.

## Proposed change

Accept GC8-S1. Two grades only:

| Grade | Source |
|-------|--------|
| `SOUND` | HARVEST from a node with condition ≥ 50, or default holdings |
| `WORN` | HARVEST from a node with condition < 50, or a mixed stack |

- Holdings keep one grade per resource key (not a parallel inventory)
- Mixing SOUND with WORN yields WORN
- TRADE transfers the offered resource’s grade; the recipient mixes
- CONSTRUCT that spends storage pays **+1 storage** when storage is WORN
- HARVEST amounts, MOVE energy, TRADE compute, and REPAIR deltas are unchanged
- No WATCH ticker. PLAY may say holdings are worn. Hidden rooms are not named

Catalog: [`economy-catalog.gc8-s1.json`](../specs/economy-catalog.gc8-s1.json).  
Slice: [GC8-S1-LOT-QUALITY.md](../docs/GC8-S1-LOT-QUALITY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Infinite rarity tiers | SPEC parent |
| Harvest amount bonus | GC8-S0 / GC1 yield forbid |
| Currency / order book | Doctrine |
| Provenance schema | Separate if needed |
| Storage spoilage | Still deferred |

## Compatibility

Additive grade cache. Worlds ignoring S1 stay S0-conformant (all SOUND).

## Data / security

Optional `lot_grades` on the Player cache. RESOURCE_TRANSFER MAY include `grade`. WATCH does not narrate grades.

## Validation

`check_gc8_s1`: condition 40 → WORN; 70 → SOUND; mix WORN; WORN construct storage +1; no currency/yield.

## Rollback

Ignore grades (treat all SOUND).

## Unresolved

Provenance fields. Storage spoilage. Transport table. v0.6B.
