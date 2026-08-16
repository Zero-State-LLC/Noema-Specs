# RFC-0063 — GC5-S5 MESSAGE board retention

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `SHOUT` / `BOARD` / `RUMOR` verbs. No cycle expiry. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists board retention beyond 3. GC5-S3 keeps the last 3 notices. An implementer would invent cycle expiry, archives, or unlimited boards.

## Proposed change

Accept GC5-S5. Same `MESSAGE surface=BOARD` as [RFC-0054](RFC-0054-message-board.md):

- Retention becomes last **5** notices per public room
- Hidden rooms still store none. Cost remains compute 1
- Events unchanged: existing `MESSAGE` with `surface=BOARD`. No `MESSAGE_DELIVERED`
- PLAY and WATCH unchanged. Help still omits board / SHOUT
- Shout last-1 is unchanged

Catalog: [`communication-catalog.gc5-s5.json`](../specs/communication-catalog.gc5-s5.json).  
Slice: [GC5-S5-RETENTION.md](../docs/GC5-S5-RETENTION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Unlimited board | Unbounded room state |
| Cycle expiry | Extra machinery |
| Last 7 / last 10 | Larger than the smallest closed step |
| Change shout last-1 | Separate surface |
| Archive / SEARCH | Out of slice |
| Help advertising board | S0 pin family |

## Compatibility

Widens S3 retention. Worlds ignoring S5 keep last 3. Existing notices older than 5 stay dropped.

## Data / security

Room-local last 5. Hidden rooms store none. WATCH does not carry the text.

## Validation

`check_gc5_s5`: public board keeps last 5; hidden reject; no new verbs; WATCH silent; shout last-1 unchanged.

## Rollback

Keep last 3 (`slice(-3)`).

## Unresolved

Institution notice is [RFC-0064](RFC-0064-institution-notice.md). Org channel. Cycle-based expiry.
