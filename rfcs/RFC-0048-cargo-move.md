# RFC-0048 — GC8-S4 Cargo MOVE Extra

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. No currency. No route_link freight minigame.

## Problem

[ECONOMIC-SPECIALIZATION.md](../docs/ECONOMIC-SPECIALIZATION.md) says freight is MOVE energy and time. GC8-S0 pins empty MOVE at 1. After a harvest, hauling lots costs the same as walking empty, so a Logistician has no role.

## Proposed change

Accept GC8-S4, a one-row transport table on existing `MOVE`:

| Load | MOVE energy |
|------|-------------|
| Empty (`storage` ≥ 16, the default grant) | **1** (S0 unchanged) |
| Carrying (`storage` < 16) | **2** |

- HARVEST already spends free `storage` as capacity. That is the cargo signal
- No courier verb. No company. No `route_link` table
- PLAY MAY say `Carrying lots costs extra to move.` WATCH does not
- Pair `HARVEST`+`TRADE` still spends energy 4. Lone harvest-then-move spends 6

Catalog: [`economy-catalog.gc8-s4.json`](../specs/economy-catalog.gc8-s4.json).  
Slice: [GC8-S4-TRANSPORT.md](../docs/GC8-S4-TRANSPORT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Courier verb | Extra command |
| route_link freight table | Freight minigame |
| Percent of holdings | Floats; inventory minigame |
| Currency / v0.6B | Doctrine |
| WATCH cargo ticker | Spectator leak |

## Compatibility

Additive MOVE extra. Worlds ignoring S4 keep S0 MOVE 1.

## Data / security

No new Player fields. Hidden rooms unchanged.

## Validation

`check_gc8_s4`: empty MOVE 1; carrying MOVE 2; no new verbs; no currency; no route_link.

## Rollback

Charge MOVE 1 always.

## Unresolved

v0.6B. `route_link` as later construction, not a freight engine.
