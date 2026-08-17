# RFC-0080 — GC5-S9 shout cycle expiry

## Status

**Accepted**

Specification-only until hosted. No `SHOUT` verb. No `event-catalog/0.3`. No `MESSAGE_EXPIRED`. Help still omits shout. Other surfaces keep last-N with no cycle drop.

## Problem

[GC5-S4-SHOUT.md](../docs/GC5-S4-SHOUT.md) keeps the last 1 shout until a later shout replaces it. [GC5-S5-RETENTION.md](../docs/GC5-S5-RETENTION.md) deferred cycle expiry. An implementer would invent an archive, a ticker, or drop every surface at once.

## Proposed change

Accept GC5-S9. A public-room `MESSAGE surface=SHOUT` still keeps last **1**. After **1** committed cycle, that shout is gone:

- Same last-1 overwrite as S4
- Hidden rooms still reject SHOUT
- Expiry is silent. No new event. WATCH silent
- Board last-5, notice last-1, channel last-1, trade notice last-1 are unchanged
- Duration other than 1 is out of slice
- Chamber help still omits shout / BOARD

Catalog: [`communication-catalog.gc5-s9.json`](../specs/communication-catalog.gc5-s9.json).  
Slice: [GC5-S9-SHOUT-EXPIRY.md](../docs/GC5-S9-SHOUT-EXPIRY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All surfaces expire | Out of slice |
| Duration other than 1 | Extra machinery |
| `MESSAGE_EXPIRED` / `STRUCTURE_*` | Extra catalog |
| SHOUT verb | Extra command |
| Help shout | S0 pin family |
| WATCH ticker | Spectator leak |

## Compatibility

Additive drop on existing `shout.cycle`. Worlds ignoring S9 keep last-1 until overwritten.

## Data / security

Uses the shout’s stored cycle. Hidden rooms store none. WATCH silent.

## Validation

`check_gc5_s9`: public shout accepted; after 1 committed cycle it is gone; hidden reject; last-1 overwrite unchanged; no new verbs.

## Rollback

Ignore shout age (keep last 1 until overwritten).

## Unresolved

Board cycle expiry is [RFC-0081](RFC-0081-board-expiry.md). Notice cycle expiry is [RFC-0082](RFC-0082-notice-expiry.md). Channel cycle expiry is [RFC-0083](RFC-0083-channel-expiry.md). Cycle expiry for TRADE_NOTICE.
