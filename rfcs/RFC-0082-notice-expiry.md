# RFC-0082 — GC5-S11 notice cycle expiry

## Status

**Accepted**

Specification-only until hosted. No `NOTICE` verb. No `event-catalog/0.3`. No `MESSAGE_EXPIRED`. Help still omits NOTICE. CHANNEL / TRADE_NOTICE keep last-1 with no cycle drop. Shout and board expiry stay [RFC-0080](RFC-0080-shout-expiry.md) / [RFC-0081](RFC-0081-board-expiry.md).

## Problem

[GC5-S6-NOTICE.md](../docs/GC5-S6-NOTICE.md) keeps the last 1 institution notice until a later notice replaces it. Cycle expiry was deferred. An implementer would invent an archive or drop every remaining surface at once.

## Proposed change

Accept GC5-S11. A public-room `MESSAGE surface=NOTICE` still keeps last **1**. After **1** committed cycle, that notice is gone:

- Same last-1 overwrite as S6
- Occupied `PUBLISH_NOTICE` still required. Vacant / non-holder still fail
- Hidden rooms still reject NOTICE
- Expiry is silent. No new event. WATCH silent
- CHANNEL and TRADE_NOTICE last-1 have no cycle drop
- Duration other than 1 is out of slice
- Chamber help still omits NOTICE

Catalog: [`communication-catalog.gc5-s11.json`](../specs/communication-catalog.gc5-s11.json).  
Slice: [GC5-S11-NOTICE-EXPIRY.md](../docs/GC5-S11-NOTICE-EXPIRY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| All remaining surfaces expire | Out of slice |
| Duration other than 1 | Extra machinery |
| `MESSAGE_EXPIRED` | Extra catalog |
| NOTICE verb | Extra command |
| Help NOTICE | S0 pin family |
| WATCH ticker | Spectator leak |

## Compatibility

Additive drop on existing `institution_notice.cycle`. Worlds ignoring S11 keep last 1 until overwritten.

## Data / security

Uses the notice’s stored cycle. Hidden rooms store none. WATCH silent.

## Validation

`check_gc5_s11`: public notice accepted; after 1 committed cycle it is gone; hidden reject; last-1 overwrite unchanged; no new verbs.

## Rollback

Ignore notice age (keep last 1 until overwritten).

## Unresolved

Cycle expiry for CHANNEL, TRADE_NOTICE. Fourth-and-later co-owners.
