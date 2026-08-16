# RFC-0065 — GC5-S7 MESSAGE org channel

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `CHANNEL` / `NOTICE` / `SHOUT` / `BOARD` verbs. No cycle expiry. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists an organization channel. GC5-S6 can post a public institution notice. There is no current-member channel without inventing a verb or leaking who belongs.

## Proposed change

Accept GC5-S7. One surface on existing `MESSAGE`:

- `surface=CHANNEL` requires `org_id` and current membership
- Last **1** channel note per organization. Visible to **current** members only
- Unknown org and non-member use the **same** fail: `NOT_ADDRESSABLE` / `That channel is not addressable.`
- Hidden-room send rejects `NOT_OBSERVABLE`. No membership list in PLAY or WATCH
- No player recipient. Cost remains compute 1
- Events: existing `MESSAGE` with `surface=CHANNEL`. No `MESSAGE_DELIVERED`
- PLAY MAY show `A channel note in {org}: …` to current members. WATCH silent
- Human alias `channel <org> "text"` is accepted and **not** listed in Chamber help
- Board last-5, shout last-1, notice last-1 unchanged

Catalog: [`communication-catalog.gc5-s7.json`](../specs/communication-catalog.gc5-s7.json).  
Slice: [GC5-S7-CHANNEL.md](../docs/GC5-S7-CHANNEL.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `CHANNEL` verb | Extra command |
| Distinct unknown-org vs non-member errors | Membership / existence oracle |
| Public room broadcast | That is NOTICE / BOARD |
| WATCH ticker | Spectator leak |
| Help advertising channel | S0 pin family |
| Unlimited history | Unbounded org state |

## Compatibility

Additive `surface` on MESSAGE. Worlds ignoring S7 keep DMs, boards, shouts, and notices.

## Data / security

Stored on the organization. Hidden rooms store none. Former members lose visibility. WATCH does not carry the text. Failure text does not name members or confirm membership.

## Validation

`check_gc5_s7`: member accepted; hidden reject; outsider and unknown share `not_addressable`; retention 1; no new verbs; WATCH silent.

## Rollback

Ignore `surface=CHANNEL` (`INVALID_REQUEST`).

## Unresolved

Cycle-based expiry. Trade notice.
