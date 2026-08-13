# RFC-0012 — GC8-S0 Distance Interdependence

## Status

**Accepted**

Specification-only. No new verbs. No currency. No v0.6B. No mastery yield. No runtime implementation in this RFC.

## Problem

[ECONOMIC-SPECIALIZATION.md](../docs/ECONOMIC-SPECIALIZATION.md) wants multi-Player supply to beat a lone generalist, but left that fixture and the v0.6B boundary as SPEC GAP. An implementation agent would add an order book, a harvest percent, or a Chamber currency.

## Proposed change

Accept GC8-S0: comparative advantage is the existing single-body + distance constraint.

- Two Players, two rooms, `HARVEST` + `TRADE`: energy 4
- One Player, one hop between rooms: energy 4 + hops
- Recognition does not change harvest amounts
- Currency, order book, global ticker, wallets, and v0.6B stay off

Catalog: [`economy-catalog.gc8-s0.json`](../specs/economy-catalog.gc8-s0.json).  
Slice: [GC8-FIRST-SLICE.md](../docs/GC8-FIRST-SLICE.md).

Costs are copied from [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md) / [RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md). They are not retuned.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Currency | Removal test + parent forbid |
| Order book | Parent: not a clearinghouse |
| GC1-S2 yield now | Deferred; changes frozen magnitudes |
| Start v0.6B here | Completeness plan: distinct follow-up |
| Lot quality in S0 | Still SPEC GAP |

## Compatibility

Additive pin of existing v0.1 economy. `resource-economy.v01.json` is not rewritten.

## Data / security

No wallet, token, or external settlement fields. Public trade notices still omit amounts.

## Validation

`check_gc8_s0`: pair energy 4 vs lone 5 on one hop; recognition yield rejected; currency / order book / wallet / v0.6B rejected.

## Rollback

Omit the catalog. v0.1 harvest/trade/move remain.

## Unresolved

GC8-S1: lot quality / provenance if a later RFC passes the removal test; storage loss; relationship to a future v0.6B RFC.
