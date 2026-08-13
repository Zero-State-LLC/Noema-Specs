# GC3 First Slice — Dyadic Trade Memory

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0007](../rfcs/RFC-0007-dyadic-trade-memory.md)  
**Does not open:** `reputation = 72` · new verbs · `event-catalog/0.3` · public titles · institution edges

S0 is the smallest social-memory increment that can support scenario B’s *cooperation* half on `event-catalog/0.1`. Betrayal / `dangerous` waits for formal `AGREEMENT_BROKEN` or `CRIME_DETECTED` (GC3-S1).

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Universal reputation integer | **REJECT** |
| `REMEMBER` / `REPUTE` verb | **REJECT** |
| New relationship events | **REJECT.** Rebuild from `TRADE_ACCEPTED` |
| Public “trusted trader” on WATCH | **DEFER.** Leak and presentation risk |
| Institution→Player edges | **DEFER** (needs GC4 offices) |
| Decay / paid wipe | **DEFER** / **REJECT** wipe |
| Auto-deceptive from `TRADE_REJECTED` | **REJECT.** Decline is legal |
| Hidden-stockpile text in the descriptor | **REJECT.** Leak |

Pressures: **dependency** (you remember who actually completed exchange) and **uncertainty** (C does not automatically know A–B history).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s0` |
| Catalog | `social-memory-catalog/gc3-s0` |
| Edge | Directed `subject_player_id` → `object_player_id` |
| Evidence | Distinct `trade_id` on `TRADE_ACCEPTED` where both are proposer or counterparty |
| State | Derived. Not WorldState. Not a reducer input |
| Public S0 projection | **None** |

### Thresholds

| Distinct accepted trades with that counterparty | Edge state | Self PLAY line |
|-------------------------------------------------|------------|----------------|
| 0 | `UNKNOWN` | omit |
| 1–2 | `TRADED` | `You have traded with {name}.` |
| ≥ 3 | `RELIABLE` | `You have found {name} reliable in trade.` |

`{name}` is the object’s **public handle**, never an inventory, route, or hidden id.

Both parties independently accrue the same count (the trade lists both). Their PLAY lines are each private.

### Rebuild rules

1. Walk accepted ledger events in `(cycle, sequence)` order.
2. On `TRADE_ACCEPTED`, resolve the trade’s `proposer_id` and `counterparty_id`.
3. If the trade record is missing, skip.
4. Credit **both** directions: A→B and B→A with that `trade_id`.
5. Count distinct `trade_id`s per directed edge.
6. `TRADE_PROPOSED`, `TRADE_REJECTED`, `LOOK`, `INSPECT`, `MESSAGE` do not credit.
7. Replay of the same `event_id` / `trade_id` does not double-count.

### Visibility

| Audience | S0 |
|----------|----|
| Self | Own outgoing edges only |
| Other Players | Nothing from this slice |
| WATCH | Nothing from this slice |
| GUI | Must not hide/show TRADE because of a private edge |

### Coupling (S0)

This slice is **memory projection**, not a price engine. It remains coupled to **TRADE** (evidence source) and **INFORMATION** (asymmetric knowledge). Mechanical trade friction is **GC3-S1** and must not leak inventories.

---

## A–J

| Test | Result |
|------|--------|
| A | Player + trade + information. No eighth primitive |
| B | Dependency + uncertainty |
| C | No extra commands; memory falls out of ordinary TRADE |
| D | Trade + information (later: access, agreements) |
| E | No new verb |
| F | A compact or brokerage habit can form from repeated reliable edges |
| G | Evidence refs are ledger trade ids |
| H | Human and agent Players use the same rebuild |
| I | Meaningful with research hidden |
| J | Without this, social loop has no persistent memory |

---

## Out of S0

```text
dangerous / deceptive / loyal / indebted
AGREEMENT_BROKEN / CRIME_DETECTED
institution edges
WATCH titles
trade refusal automation
decay
MESSAGE-derived private notes as public reputation
```

---

## Acceptance (narrower than scenario B)

1. A and B complete three distinct accepted trades.
2. Each sees the `reliable` self-line naming the other.
3. Player C’s PLAY does not show that line.
4. WATCH does not show it.
5. Five `TRADE_REJECTED` events create no `deceptive` descriptor.
6. Projection text never includes resource amounts or hidden entity ids.

Full scenario B (betrayal changing institutional expectations) is **GC3-S1**.
