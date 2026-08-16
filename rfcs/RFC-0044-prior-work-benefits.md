# RFC-0044 — GC1-S4 Prior-Work Track Benefits

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No WATCH titles. No naked class discounts.

## Problem

GC1-S2/S3 give Engineer a world-procedure quality bonus that rusts. Explorer, Surveyor, and Broker remain lines-only. A class-wide cheaper MOVE/INSPECT/TRADE would be a level discount.

## Proposed change

Accept GC1-S4. Benefits apply only while the track is recognized **and** MAINTAINED (S3). Evidence is prior work on that object or party:

| Track | Prior work | Benefit |
|-------|------------|---------|
| Explorer | this room already in explorer units | Repeat `LOOK` here pays **0** attention |
| Surveyor | this entity already in surveyor units | Repeat `INSPECT` of it pays **0** attention |
| Broker | a settled `TRADE` with this counterparty | `TRADE_CAUTION` extra compute is **0** |

First LOOK of a room, first INSPECT of an entity, and first TRADE with a stranger are unchanged. Sealed records stay `FORBIDDEN`. Hidden facts are not revealed. LATENT withholds the benefit. Engineer +5 unchanged.

Catalog: [`mastery-catalog.gc1-s4.json`](../specs/mastery-catalog.gc1-s4.json).  
Slice: [GC1-S4-PRIOR-WORK.md](../docs/GC1-S4-PRIOR-WORK.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Cheaper MOVE / all INSPECT / all TRADE | Naked class discount |
| WATCH titles | Leak |
| Bypass `inspect_restricted` | Hidden-fact / seal leak |
| 1-work restore of decay | RFC-0043 |

## Compatibility

Additive. Worlds ignoring S4 keep paying full attention and caution.

## Data / security

Practice cache MAY store broker counterparties. Rebuildable from `TRADE_ACCEPTED`. WATCH silent.

## Validation

`check_gc1_s4`: prior+maintained waives the named cost; first/stranger/LATENT do not; no new verbs; no WATCH titles.

## Rollback

Ignore the three waivers.

## Unresolved

Focus declaration. Public titles. Parameter-access / office-eligibility benefits.
