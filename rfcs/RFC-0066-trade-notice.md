# RFC-0066 — GC5-S8 MESSAGE trade notice

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `TRADE_NOTICE` / `MARKET` verbs. Does not replace `TRADE`. No price oracle. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists a trade-notice surface. GC5-S7 can post a member channel. There is no market-local public stall note without inventing a verb or certifying prices.

## Proposed change

Accept GC5-S8. One surface on existing `MESSAGE`:

- `surface=TRADE_NOTICE` posts the text in the current **public** room
- Same-room / market-local only. No long-range stall. No hidden-room stall
- No player recipient. Does not open a `TRADE`. Cost remains compute 1
- Retention: last **1** trade notice per room
- Events: existing `MESSAGE` with `surface=TRADE_NOTICE`. No `MESSAGE_DELIVERED`
- PLAY MAY show `A trade notice: …`. The engine does not certify quantities or prices. WATCH silent
- Human alias `market "text"` is accepted and **not** listed in Chamber help
- Board last-5, shout last-1, notice last-1, channel last-1 unchanged

Catalog: [`communication-catalog.gc5-s8.json`](../specs/communication-catalog.gc5-s8.json).  
Slice: [GC5-S8-TRADE-NOTICE.md](../docs/GC5-S8-TRADE-NOTICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `MARKET` / `TRADE_NOTICE` verb | Extra command; `TRADE` already exists |
| Auto-open TRADE | Distinct mutation |
| Certified prices / inventory | Oracle / holdings leak |
| Long-range stall | Topology leak |
| Hidden-room stall | Hidden leak |
| WATCH ticker | Spectator leak |
| Help advertising market | S0 pin family |

## Compatibility

Additive `surface` on MESSAGE. Worlds ignoring S8 keep DMs, boards, shouts, notices, channels, and `TRADE`.

## Data / security

Room-local last notice. Hidden rooms store none. WATCH does not carry the text. Text is Player speech, not ledger truth.

## Validation

`check_gc5_s8`: public room accepted; hidden reject; retention 1; no new verbs; WATCH silent; TRADE unchanged.

## Rollback

Ignore `surface=TRADE_NOTICE` (`INVALID_REQUEST`).

## Unresolved

Cycle-based expiry.
