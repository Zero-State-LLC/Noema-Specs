# RFC-0138: WS06 Civic Contracts and Archivist / Herald Mastery Tracks

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-25 (`orin_deeptime_mechanics_plan.md`).

This RFC extends Contract Clerk `WS06` (`world-services.ts`) and adds two additive derived mastery tracks to `practice.ts` / `focus.ts` (aligning with `RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md`) without altering the 4 existing tracks (`explorer`, `surveyor`, `broker`, `engineer`).

## Decisions

### 1. Bounded Escrowed Civic Contracts (`CONTRACT_POST` / `CONTRACT_FULFILL`)

1. **Kinds (Closed Enum):**
   - `"REPAIR_TARGET"`: target public infrastructure entity reaches `condition >= target_condition` (bounded `50..100`, default `80`).
   - `"ATTEST_ROOM"`: target public room accumulates `>= target_count` (`1..3`) independent `ATTEST` evidence fragments after `posted_cycle`.
2. **Posting (`COMMIT` `operation: "CONTRACT_POST"`):**
   - Available to any seated office holder (`OPERATE_RESOURCE_ACCOUNT` or `PUBLISH_NOTICE` or org founder) in a public room.
   - Escrows `reward_amount` (`1..5`) of `"storage"` (from org treasury) or `"influence"` (from poster, capped at `3`) at post time.
   - Max `3` open contracts per organization (`MAX_OPEN_CONTRACTS_PER_ORG = 3`); default expiry `posted_cycle + 24`. Expired contracts automatically refund escrowed resources back to treasury/poster on cycle commit.
3. **Fulfilling (`COMMIT` `operation: "CONTRACT_FULFILL"`):**
   - Available to any Player (other than the poster, or any non-poster member/external agent) co-located in the contract's target room once the deterministic completion predicate holds.
   - Releases the escrowed reward atomically to the fulfiller, marks contract `"FULFILLED"`, emits `RESOURCE_TRANSFER` (`kind: "contract"`), and projects as `verb: "contract"` in public `rooms[].room_activity[]`.

### 2. Archivist & Herald Mastery Tracks (`practice.ts` + `focus.ts`)

Add two additive derived tracks (same recognition / latency / rehabilitation semantics as existing `PRACTICE_TRACKS`, `PUBLIC_TITLE_CAP = 1` unchanged):

| Track ID | Focus Token | Credit Events | Recognition Threshold | Public Title Line | Mechanical Benefit (when maintained) |
|---|---|---|---|---|---|
| `track.archivist.01` | `archivist` | Distinct subjects in `RECONSTRUCT` / `RECONSTRUCT_PUBLISH` / `ATTEST` | `3` | `"{handle} keeps the Reach's record."` | `-1` attention cost on `RECONSTRUCT` and `ATTEST` (min `1`) |
| `track.herald.01` | `herald` | Distinct cycles/subjects with `PUBLISH_NOTICE` / `BOARD` / `SHOUT` / corroborated `rumor` | `3` | `"{handle} carries the Reach's word."` | `MESSAGE` / `ORG_OFFICE_ACT` compute cost reduced by `1` (min `0`) |

## Security & Privacy Invariants

- Escrowed contracts prevent negative balances or double payout (idempotent status transition `OPEN -> FULFILLED | EXPIRED`).
- Public WATCH never leaks private contract negotiation or raw mastery counts — only existing `public_title_lines` (capped at `1`) and band-safe contract fulfillment deeds.

## Rollback

Disable `CONTRACT_POST`/`CONTRACT_FULFILL` affordances (refunding any open escrows) and remove the two additive track entries from `PRACTICE_TRACKS`.
