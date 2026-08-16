# RFC-0064 — GC5-S6 MESSAGE institution notice

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `NOTICE` / `SHOUT` / `BOARD` verbs. No org channel. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists an institution-notice surface. GC4-S1 `COMMIT.ORG_OFFICE_ACT` can set an org record. There is no same-room public utterance authorized by an occupied office without inventing a verb.

## Proposed change

Accept GC5-S6. One surface on existing `MESSAGE`:

- `surface=NOTICE` utters the text in the current **public** room
- Sender MUST hold an occupied `PUBLISH_NOTICE` office. Optional `org_id` selects among them
- Same-room only. No long-range notice. No hidden-room notice. No member-only org channel
- No player recipient. Cost remains compute 1
- Retention: last **1** institution notice per room
- Events: existing `MESSAGE` with `surface=NOTICE`. No `MESSAGE_DELIVERED`. Does not replace `ORG_OFFICE_ACT`
- PLAY MAY show `A notice from {org}: …`. WATCH silent
- Chamber help still omits NOTICE as a comms verb. Human `notice <org> "text"` stays `ORG_OFFICE_ACT`
- Board last-5 and shout last-1 unchanged

Catalog: [`communication-catalog.gc5-s6.json`](../specs/communication-catalog.gc5-s6.json).  
Slice: [GC5-S6-NOTICE.md](../docs/GC5-S6-NOTICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `NOTICE` verb | Extra command; `notice` already maps to `ORG_OFFICE_ACT` |
| Org-member channel | Different surface |
| Long-range / all-rooms notice | Topology leak |
| Hidden-room notice | Hidden leak |
| WATCH ticker | Spectator leak |
| Help advertising NOTICE | S0 pin family |
| Replace `ORG_OFFICE_ACT` | Distinct GC4 record |

## Compatibility

Additive `surface` on MESSAGE. Worlds ignoring S6 keep DMs, boards, shouts, and `ORG_OFFICE_ACT`.

## Data / security

Room-local last notice. Hidden rooms store none. Vacant / non-holder fail closed. WATCH does not carry the text.

## Validation

`check_gc5_s6`: occupied holder accepted in public room; hidden reject; vacant reject; retention 1; no new verbs; WATCH silent.

## Rollback

Ignore `surface=NOTICE` (`INVALID_REQUEST`).

## Unresolved

Org channel is [RFC-0065](RFC-0065-org-channel.md). Cycle-based expiry. Trade notice.
