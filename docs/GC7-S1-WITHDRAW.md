# GC7-S1 — Withdraw

**Status:** Executable specification. Runtime authorized with RFC-0026.  
**Parent:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)  
**RFC:** [RFC-0026](../rfcs/RFC-0026-contest-withdraw.md)  
**Does not open:** HP · `event-catalog/0.3` · auto-MOVE · Chamber help advertising CONTEST

S1 is the smallest increment that still lets a committed participant reduce further exposure without deleting the contest or the opponent’s commitment.

---

## Doctrine

```text
WITHDRAW ≠ CANCEL BEFORE COMMIT ≠ RETROACTIVE UNDO ≠ FORFEIT IDENTITY ≠ TELEPORT
```

| Temptation | Verdict |
|------------|---------|
| New event type | **REJECT.** Reuse `CONTEST_RESOLVED` |
| Refund spent declare/defend cost | **REJECT** |
| Refund reserved stake on declarer walk-away | **REJECT.** Consume |
| Idle / disconnect withdraws | **REJECT** |
| Withdraw after `CLOSED` | **REJECT** |
| MOVE as a side effect | **REJECT** |
| Cowardice / HP | **REJECT** |

Pressures: **scarcity** (stake is real) and **uncertainty** (walking away has a known cost, not a previewed score).

---

## Lifecycle

```text
OPEN (declared, optional defend)
  → WITHDRAW (Player COMMIT.CONTEST_WITHDRAW)
  → CONTEST_RESOLVED
  → RECOVER (existing verbs)
```

Window: contest `OPEN` and `world.cycle < expires_cycle`. After expiry the world-side resolver still owns settlement.

---

## Reservations

| Item | Declarer withdraws | Defender withdraws |
|------|--------------------|--------------------|
| Declare/defend fee | already consumed | already consumed |
| Declarer reserved stake | **consume** | **consume** |
| Defender reserved stake | **release** | **consume** |
| `CONTEST_RESOLVED.outcome` | `ABORTED` | `SUCCESS` |
| Disruption / seizure | none | existing SUCCESS follow-on |
| Danger (GC3-S1) | none (`ABORTED`) | existing SUCCESS rule |

No duplication. No stuck reservation. No silent mint.

---

## Authority

Actor must be `declarer_id` or recorded `defender_id`. An office/founder title does not let a Player withdraw someone else’s contest. Institution-as-party remains later.

---

## Ordering

The World DO serializes commands. Same-cycle withdraw vs defend is the order those commands are applied, not HTTP arrival across processes. After `CLOSED`, a later withdraw is `NOT_FOUND` (or `STALE_HEAD` if the caller asserted `expected_status=OPEN`).

---

## Projection

Participants see the consequence and `CONTEST_RESOLVED`. Public contest list drops the now-closed contest. Do not show private stake maps on WATCH. Help still omits CONTEST / withdraw.

---

## A–J

| Test | Result |
|------|--------|
| A | Existing contest + resources. No HP |
| B | Scarcity + uncertainty |
| C | One COMMIT operation |
| D | Couples to resolve follow-ons and recovery verbs |
| E | No frozen new top-level verb |
| F | Walking away is a habit, not a combat class |
| G | `CONTEST_RESOLVED` remains attributable |
| H | Human and agent identical |
| I | Meaningful without research scores |
| J | Without this, commit has no exit except expiry |

---

## Out of S1

```text
standing offline withdraw policy
institution-as-party
information-target form
HP / ATTACK / SCAN
event-catalog/0.3
Chamber help advertising CONTEST
```
