# GC5-S1 — Deterministic Delay on Degraded Relays

**Status:** Shipped as hosted MESSAGE delay (RFC-0021 Accepted; reference runtime PR #85). Rumor still out.  
**Parent:** [GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0021](../rfcs/RFC-0021-relay-message-delay.md)  
**Does not open:** `SHOUT` / `BOARD` / `RUMOR` verbs · `MESSAGE_FAILED` · `event-catalog/0.3` · org/public boards. Rumor is [GC5-S2-RUMOR.md](GC5-S2-RUMOR.md).

S1 is the smallest increment that still satisfies scenario E’s *delay* shape: a degraded path delivers later; repair restores a faster class. Local `MESSAGE` is unchanged. Failure remains `UNREACHABLE`.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `RUMOR` verb / rumor schema | **DEFER** (GC5-S2) |
| Random delay | **REJECT.** Delay is a closed integer |
| Change the S0 fail floor (25) | **REJECT.** `< 25` or no relay stays `UNREACHABLE` |
| `MESSAGE_FAILED` | **REJECT.** Delayed send still emits `MESSAGE` |
| Must stand next to the relay | **REJECT.** Same as S0 |
| Extra compute retune | **REJECT.** Cost stays compute 1 |

Pressures: **distance**, **dependency**, **uncertainty** (sender knows it is delayed; not when the path will heal).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s1` |
| Catalog | `communication-catalog/gc5-s1` |
| Verb | `MESSAGE` |
| Delay | **1** world cycle when long-range and `25 ≤ best < 50` |
| Same-cycle long-range | best live relay `≥ 50` |
| Fail | best `< 25` or none → `UNREACHABLE`, no events |
| Local | always same-cycle when addressable |

### Band table (long-range)

| Best live relay `condition` | Outcome |
|-----------------------------|---------|
| `≥ 50` | `MESSAGE` + same-cycle `MESSAGE_DELIVERED` |
| `25`–`49` | `MESSAGE` now; `MESSAGE_DELIVERED` when `World.cycle` reaches send cycle + 1 |
| `0`–`24`, or no live relay | `UNREACHABLE` (no events, no debit) |

Local (same room) ignores this table.

`DELAYED` is not a failure code. The send is `ok`. The sender-visible consequence may say delivery is delayed. It MUST NOT name a relay id, hidden room, or recipient room.

Repair that raises best from 49 → 50 restores same-cycle for **new** sends. In-flight delayed messages keep their `deliver_at_cycle`.

World-time is RFC-0019 (WAIT quorum). Cron does not deliver.

### Events

| Moment | Types |
|--------|-------|
| Send (immediate or delayed) | `MESSAGE` |
| Delivery (same cycle or later) | `MESSAGE_DELIVERED` (`delivered_cycle`) |

No `MESSAGE_FAILED`. No rumor types.

### Inbox

The recipient inbox receives the text only at `MESSAGE_DELIVERED`. Pending text is not WATCH and not another Player’s observation.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + asset + location. World-time already exists |
| B | Distance, dependency, uncertainty |
| C | No extra command |
| D | Couples to REPAIR / GC10 condition / RFC-0019 |
| E | `MESSAGE` stays the verb |
| F | Courier / wait-for-mail habits can form |
| G | Send and delivery remain attributable |
| H | Same band for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, scenario E has no delay class |

---

## Out of S1

```text
SHOUT BOARD RUMOR
rumor records / source_class
org channel / public board
MESSAGE_FAILED
variable delay by hop count
region schema
WATCH DM text
```

---

## Runtime rule

Hosted Chamber applies this table on existing `MESSAGE`. Help still omits a delay tutorial. Do not add rumor. Do not reseed Genesis.
