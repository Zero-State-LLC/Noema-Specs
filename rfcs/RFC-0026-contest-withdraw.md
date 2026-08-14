# RFC-0026 — GC7-S1 Contest Withdraw

## Status

**Accepted**

Closes the GC7-S0 withdraw SPEC GAP. A committed participant may end further exposure. Withdrawal does not undo spent costs, teleport, or erase the opponent’s valid commitment. No HP. No `event-catalog/0.3`.

## Problem

[GC7-FIRST-SLICE.md](../docs/GC7-FIRST-SLICE.md) left versioned withdraw as SPEC GAP. An implementer would add `RETREAT` as a MOVE, refund reserved stake, or invent `CONTEST_WITHDRAWN` in catalog 0.3.

## Proposed change

Accept GC7-S1:

```text
WITHDRAW ≠ CANCEL BEFORE COMMIT ≠ RETROACTIVE UNDO ≠ TELEPORT
```

- Wire: `COMMIT.CONTEST_WITHDRAW`. Human aliases `withdraw` / `retreat` / `disengage` are not Chamber help.
- Allowed only while the contest is `OPEN` and `cycle < expires_cycle`. Actor must be declarer or recorded defender.
- Settles through existing `CONTEST_RESOLVED` (`event-catalog/0.2`):
  - Declarer withdraws → `outcome=ABORTED`. Declarer reserved stake is **consumed**. Defender reserved stake is **released**. No disruption/seizure follow-on.
  - Defender withdraws → `outcome=SUCCESS` (declarer). Both reserved stakes are **consumed**. Existing SUCCESS follow-ons apply.
- `DECLARE` / `DEFEND` compute-influence costs are never refunded.
- Duplicate withdraw of a closed contest is rejected (`NOT_FOUND`), not a second spend. Same idempotency key replays.
- Disconnect / idle presence does **not** withdraw.
- Institution: a Player withdraws only their own participation. An office does not authorize withdrawing another member’s contest.
- GC3-S1: `ABORTED` is evidence only and does **not** create a danger edge.

Catalog: [`conflict-catalog.gc7-s1.json`](../specs/conflict-catalog.gc7-s1.json).  
Slice: [GC7-S1-WITHDRAW.md](../docs/GC7-S1-WITHDRAW.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New `CONTEST_WITHDRAWN` type | 0.3 / silent catalog |
| Full stake refund | Erases committed exposure |
| Auto-MOVE | Geography is a separate verb |
| Withdraw after resolve | Retroactive undo |
| Idle = withdraw | Transport must not settle contests |
| Cowardice score | Interpretation, not a fact |

## Compatibility

Additive. GC7-S0 declare/defend/resolve unchanged when nobody withdraws. Frozen `event-types.0.2.json` unchanged (`ABORTED` already exists).

## Data / security

No new table. Reservations conserved: consume or release, never both. Cross-world contest ids are `NOT_FOUND`. Stale expected-open on a closed contest is `STALE_HEAD`.

## Validation

`check_gc7_s1`: participant withdraw accepted; nonparticipant / settled / duplicate / stale / cross-world / unauthorized institution rejected; no HP; no new event type.

## Rollback

Stop accepting `CONTEST_WITHDRAW`. Open contests still expire/resolve on cycle commit.

## Unresolved

Institution-as-party, standing offline withdraw policy, information-target form.
