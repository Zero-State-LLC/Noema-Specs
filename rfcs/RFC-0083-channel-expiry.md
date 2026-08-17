# RFC-0083 — GC5-S12 channel cycle expiry

## Status

**Accepted**

Specification-only until hosted. No `CHANNEL` verb. No `event-catalog/0.3`. No `MESSAGE_EXPIRED`. Help still omits CHANNEL. TRADE_NOTICE keeps last-1 with no cycle drop. Notice expiry stays [RFC-0082](RFC-0082-notice-expiry.md).

## Problem

[GC5-S7-CHANNEL.md](../docs/GC5-S7-CHANNEL.md) keeps the last 1 member note until a later note replaces it. Cycle expiry was deferred. An implementer would invent an archive or leak membership on drop.

## Proposed change

Accept GC5-S12. A `MESSAGE surface=CHANNEL` still keeps last **1** note per org. After **1** committed cycle, that note is gone:

- Same last-1 overwrite as S7
- Current members only. Unknown org and non-member still share `NOT_ADDRESSABLE`
- Hidden rooms still reject CHANNEL send
- The note lives on the org, not the room. Expiry does not name members
- Expiry is silent. No new event. WATCH silent
- TRADE_NOTICE last-1 has no cycle drop
- Duration other than 1 is out of slice
- Chamber help still omits CHANNEL

Catalog: [`communication-catalog.gc5-s12.json`](../specs/communication-catalog.gc5-s12.json).  
Slice: [GC5-S12-CHANNEL-EXPIRY.md](../docs/GC5-S12-CHANNEL-EXPIRY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| TRADE_NOTICE in this slice | Out of slice |
| Duration other than 1 | Extra machinery |
| `MESSAGE_EXPIRED` | Extra catalog |
| CHANNEL verb | Extra command |
| Distinct outsider fail | Membership leak |
| Help CHANNEL | S0 pin family |
| WATCH ticker | Spectator leak |

## Compatibility

Additive drop on existing `org.channel.cycle`. Worlds ignoring S12 keep last 1 until overwritten.

## Data / security

Uses the channel note’s stored cycle. Hidden rooms store none. Expiry does not list members. WATCH silent.

## Validation

`check_gc5_s12`: member channel accepted; after 1 committed cycle it is gone; hidden reject; last-1 overwrite unchanged; no new verbs.

## Rollback

Ignore channel age (keep last 1 until overwritten).

## Unresolved

Cycle expiry for TRADE_NOTICE. Fourth-and-later co-owners.
