# RFC-0054 — GC5-S3 MESSAGE board surface

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `RUMOR` / `SHOUT` / `BOARD` verbs. No rumor score. No `event-catalog/0.3`.

## Problem

[COMMUNICATION-ECOLOGY.md](../docs/COMMUNICATION-ECOLOGY.md) still lists a MESSAGE surface enum and a board. GC5-S2 can pass private claims. There is no same-room public notice without inventing a verb.

## Proposed change

Accept GC5-S3. One surface on existing `MESSAGE`:

- `surface=BOARD` posts the text to the current **public** room
- Same-room only. No long-range board. No hidden-room board
- No player recipient. Cost remains compute 1
- Retention: last **3** notices per room
- Events: existing `MESSAGE` with `surface=BOARD`. No `MESSAGE_DELIVERED`
- PLAY MAY show `A notice on the board: …`. WATCH silent
- Human alias `board "text"` is accepted and **not** listed in Chamber help
- SHOUT remains deferred

Catalog: [`communication-catalog.gc5-s3.json`](../specs/communication-catalog.gc5-s3.json).  
Slice: [GC5-S3-BOARD.md](../docs/GC5-S3-BOARD.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `BOARD` / `SHOUT` verbs | Extra commands |
| Long-range board | Topology / relay leak |
| Hidden-room board | Hidden leak |
| WATCH board ticker | Spectator leak |
| Help advertising board | S0 pin family |

## Compatibility

Additive `surface` on MESSAGE. Worlds ignoring S3 keep private DMs.

## Data / security

Room-local notices. Hidden rooms store none. WATCH does not carry the text.

## Validation

`check_gc5_s3`: board accepted in public room; hidden reject; retention 3; no new verbs; WATCH silent.

## Rollback

Ignore `surface=BOARD` (`INVALID_REQUEST`).

## Unresolved

SHOUT. Retention beyond 3. Office eligibility.
