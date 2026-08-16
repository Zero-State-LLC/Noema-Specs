# RFC-0062 — GC5-S4 MESSAGE shout surface

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `SHOUT` / `BOARD` / `RUMOR` verbs. No rumor score. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists a local-notice surface. GC5-S3 can post a persistent board. There is no same-room public utterance without inventing a verb.

## Proposed change

Accept GC5-S4. One surface on existing `MESSAGE`:

- `surface=SHOUT` utters the text in the current **public** room
- Same-room only. No long-range shout. No hidden-room shout. No adjacent-room leak
- No player recipient. Cost remains compute 1
- Retention: last **1** shout per room
- Events: existing `MESSAGE` with `surface=SHOUT`. No `MESSAGE_DELIVERED`
- PLAY MAY show `A shout: …`. WATCH silent
- Human alias `shout "text"` is accepted and **not** listed in Chamber help
- Board retention stays 3. Retention beyond 3 remains deferred

Catalog: [`communication-catalog.gc5-s4.json`](../specs/communication-catalog.gc5-s4.json).  
Slice: [GC5-S4-SHOUT.md](../docs/GC5-S4-SHOUT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `SHOUT` / `BOARD` verbs | Extra commands |
| Long-range / adjacent shout | Topology / relay leak |
| Hidden-room shout | Hidden leak |
| WATCH shout ticker | Spectator leak |
| Help advertising shout | S0 pin family |
| Board retention change | Separate SPEC GAP |

## Compatibility

Additive `surface` on MESSAGE. Worlds ignoring S4 keep DMs and boards.

## Data / security

Room-local last shout. Hidden rooms store none. WATCH does not carry the text.

## Validation

`check_gc5_s4`: shout accepted in public room; hidden reject; retention 1; no new verbs; WATCH silent.

## Rollback

Ignore `surface=SHOUT` (`INVALID_REQUEST`).

## Unresolved

Board retention is [RFC-0063](RFC-0063-board-retention.md) (last 5). Org / institution notice surfaces.
