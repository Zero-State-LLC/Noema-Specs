# RFC-0081 — GC5-S10 board cycle expiry

## Status

**Accepted**

Specification-only until hosted. No `BOARD` verb. No `event-catalog/0.3`. No `MESSAGE_EXPIRED`. Help still omits board. NOTICE / CHANNEL / TRADE_NOTICE keep last-N with no cycle drop. Shout expiry stays [RFC-0080](RFC-0080-shout-expiry.md).

## Problem

[GC5-S5-RETENTION.md](../docs/GC5-S5-RETENTION.md) keeps the last 5 board notices until later posts push them off. [RFC-0080](RFC-0080-shout-expiry.md) closed shout age. An implementer would invent an archive or drop every remaining surface at once.

## Proposed change

Accept GC5-S10. A public-room `MESSAGE surface=BOARD` still keeps last **5**. After **1** committed cycle, those notices are gone:

- Same last-5 overwrite as S5 in the posting cycle
- Hidden rooms still reject BOARD
- Expiry is silent. No new event. WATCH silent
- Shout last-1 + 1-cycle drop unchanged. Notice / channel / trade-notice last-1 have no cycle drop
- Duration other than 1 is out of slice
- Chamber help still omits board / SHOUT

Catalog: [`communication-catalog.gc5-s10.json`](../specs/communication-catalog.gc5-s10.json).  
Slice: [GC5-S10-BOARD-EXPIRY.md](../docs/GC5-S10-BOARD-EXPIRY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining surfaces expire | Out of slice |
| Duration other than 1 | Extra machinery |
| `MESSAGE_EXPIRED` | Extra catalog |
| BOARD verb | Extra command |
| Help board | S0 pin family |
| WATCH ticker | Spectator leak |

## Compatibility

Additive drop on existing `board[].cycle`. Worlds ignoring S10 keep last 5 until overwritten.

## Data / security

Uses each notice’s stored cycle. Hidden rooms store none. WATCH silent.

## Validation

`check_gc5_s10`: public board accepted; after 1 committed cycle notices are gone; hidden reject; last-5 overwrite unchanged; no new verbs.

## Rollback

Ignore board notice age (keep last 5 until overwritten).

## Unresolved

Notice cycle expiry is [RFC-0082](RFC-0082-notice-expiry.md). Cycle expiry for CHANNEL, TRADE_NOTICE. Fourth-and-later co-owners.
