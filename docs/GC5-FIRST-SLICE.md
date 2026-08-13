# GC5 First Slice — Relay Bands on Existing MESSAGE

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0009](../rfcs/RFC-0009-relay-message-delivery.md)  
**Does not open:** `SHOUT` / `BOARD` / `RUMOR` verbs · `MESSAGE_FAILED` · `event-catalog/0.3` · rumor records · multi-cycle delay · region schema

S0 is the smallest communication increment that still satisfies scenario E’s *shape* (damaged infrastructure changes long-range delivery; local `MESSAGE` still works) using the existing `MESSAGE` verb and `event-catalog/0.1` types. Boards, rumors, and delay math wait for GC5-S1.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `SHOUT` / `BOARD` / `RUMOR` verbs | **REJECT.** Surfaces are addressability of `MESSAGE`, not new mutations |
| `MESSAGE_FAILED` / catalog 0.3 | **REJECT.** Fail closed with a typed API reason; no silent drop |
| Region / realm schema for “another region” | **REJECT.** S0 uses rooms. Same room = local; different room = long-range |
| Multi-cycle delay function | **DEFER** (GC5-S1). Exact delay is still SPEC GAP |
| Rumor provenance records | **DEFER** |
| Org channel / public board / institution notice | **DEFER** (needs GC4 scopes and surface parameters) |
| Must stand next to a relay to send | **REJECT.** That is a post-office industry. Path quality is world relay state |
| Extra compute retune | **REJECT.** Keep the existing `< 25` local-relay cost. This slice is delivery, not price |

Pressures: **distance** (another room is not free), **dependency** (someone must keep a relay alive), **uncertainty** (failure is `UNREACHABLE`, not a topology leak).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s0` |
| Catalog | `communication-catalog/gc5-s0` |
| Verb | `MESSAGE` (optional `ASK` still reduces to `MESSAGE`) |
| Surface | Direct Player→Player only |
| Events on success | Existing `MESSAGE`, then same-cycle `MESSAGE_DELIVERED` |
| Events on delivery fail | none (typed failure) |

### Local vs long-range

| Class | Definition | Relay required |
|-------|------------|----------------|
| Local | `sender.room_id == recipient.room_id` | No |
| Long-range | Different rooms | Yes: a live `relay` at or above the band |

Adjacent rooms are long-range in S0. Do not invent adjacency-as-local.

### Path metric

Among live `INFRASTRUCTURE` entities whose class is `relay`, take the **maximum** `condition` (0–100). Missing or none live → no path.

One genesis relay can serve the whole chamber. Repair of that relay restores the prior delivery class. Do not require the sender to occupy the relay’s room.

### Condition band (pinned)

Reuse the existing `MESSAGE` stressed-relay number from [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) (`local relay condition < 25` extra compute). Do not invent a second magic threshold.

| Best live relay `condition` | Long-range | Local |
|-----------------------------|------------|-------|
| ≥ `25` | Same-cycle `MESSAGE` + `MESSAGE_DELIVERED` | Same-cycle |
| 0–24, or no live relay | `UNREACHABLE` (no events) | Same-cycle |

`DELAYED` is **not** an S0 outcome.

Recipient not entered / not in this world remains the existing addressability failure (`FORBIDDEN` in hosted v0.1). S0 does not rename it.

### Failure visibility

Sender-visible reason for the new path failure is exactly `UNREACHABLE`.

Must not include: relay `entity_id`, hidden room ids, exit graphs, recipient room when that room is hidden, inventory, or message text on WATCH.

WATCH remains `message_notice` without text on success. WATCH sees no DM text on `UNREACHABLE`.

### Costs

Unchanged: compute 1; additional compute 1 if the **sender’s local** relay condition is `< 25`. That cost rule is not a delivery band. A local send with a broken world relay still succeeds if budget is paid.

`COMMIT.REPAIR` is unchanged (+15 condition, cap 100). Raising the best live relay from 24 to 25 restores long-range.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + asset (relay) + location. No eighth primitive |
| B | Distance, dependency, uncertainty |
| C | No extra commands |
| D | Couples to `REPAIR` / later `BUILD` and to social coordination |
| E | `MESSAGE` stays the verb |
| F | A repair habit or courier practice can form without a mail engine |
| G | `MESSAGE` / `MESSAGE_DELIVERED` remain attributable |
| H | Human and agent Players use the same band |
| I | Meaningful with research hidden |
| J | Without this, relay condition is flavor text |

---

## Out of S0

```text
SHOUT BOARD RUMOR
MESSAGE_FAILED event-catalog/0.3
DELAYED cycle function
rumor records / source_class
org channel, public board, institution notice, trade notice
region schema
route_link as required path
WATCH DM text
omniscient search
```

---

## Runtime rule

Chamber `MESSAGE` stays the current same-cycle path until an implementation pass is authorized. This document does not change production delivery. First-world verb freeze is not thawed.

## Acceptance (narrower than scenario E)

1. Same-room `MESSAGE` succeeds while the best live relay is at condition 0.
2. Different-room `MESSAGE` with best live relay ≥ 25 succeeds with `MESSAGE` + `MESSAGE_DELIVERED`.
3. Different-room `MESSAGE` with best live relay 24, or with no live relay, is `UNREACHABLE` and emits no events.
4. The sender-visible reason is `UNREACHABLE` and does not name a relay id or hidden room.
5. WATCH never includes DM text.

Full scenario E (degraded delay, then repair restoring a delay class) is **GC5-S1**.
