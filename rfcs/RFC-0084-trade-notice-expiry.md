# RFC-0084 — GC5-S13 trade-notice cycle expiry

## Status

**Accepted**

Specification-only until hosted. No `MARKET` / `TRADE_NOTICE` verb. No `event-catalog/0.3`. No `MESSAGE_EXPIRED`. Help still omits market. Channel expiry stays [RFC-0083](RFC-0083-channel-expiry.md).

## Problem

[GC5-S8-TRADE-NOTICE.md](../docs/GC5-S8-TRADE-NOTICE.md) keeps the last 1 public stall note until a later note replaces it. Cycle expiry was deferred. An implementer would invent an archive or auto-open TRADE on drop.

## Proposed change

Accept GC5-S13. A `MESSAGE surface=TRADE_NOTICE` still keeps last **1** note per public room. After **1** committed cycle, that note is gone:

- Same last-1 overwrite as S8
- Hidden rooms still reject TRADE_NOTICE send
- Does not open TRADE
- Expiry is silent. No new event. WATCH silent
- Duration other than 1 is out of slice
- Chamber help still omits market / TRADE_NOTICE

Catalog: [`communication-catalog.gc5-s13.json`](../specs/communication-catalog.gc5-s13.json).  
Slice: [GC5-S13-TRADE-NOTICE-EXPIRY.md](../docs/GC5-S13-TRADE-NOTICE-EXPIRY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Duration other than 1 | Extra machinery |
| `MESSAGE_EXPIRED` | Extra catalog |
| MARKET / TRADE_NOTICE verb | Extra command |
| Auto-open TRADE | S8 pin |
| Help market | S0 pin family |
| WATCH ticker | Spectator leak |

## Compatibility

Additive drop on existing `room.trade_notice.cycle`. Worlds ignoring S13 keep last 1 until overwritten.

## Data / security

Uses the stall note’s stored cycle. Hidden rooms store none. WATCH silent.

## Validation

`check_gc5_s13`: public trade notice accepted; after 1 committed cycle it is gone; hidden reject; last-1 overwrite unchanged; no new verbs.

## Rollback

Ignore trade-notice age (keep last 1 until overwritten).

## Unresolved

Third co-owner is [RFC-0085](RFC-0085-third-co-owner.md). Fourth co-owner is [RFC-0086](RFC-0086-fourth-co-owner.md). Fifth co-owner is [RFC-0087](RFC-0087-fifth-co-owner.md). Sixth-and-later co-owners.
