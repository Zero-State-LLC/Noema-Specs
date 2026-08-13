# GC8 First Slice — Distance Interdependence

**Status:** Already true in hosted v0.1 costs (RFC-0012 Accepted). No runtime change.  
**Parent:** [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0012](../rfcs/RFC-0012-distance-interdependence.md)  
**Does not open:** currency · order book · v0.6B · lot quality · storage spoilage · mastery yield bonuses · wallets / x402 / crypto

S0 is the smallest economy increment that still satisfies scenario H’s *shape* (several Players doing different work beat one Player doing all of it) using **already-true** Chamber constraints: one body, one budget, rooms are apart, `TRADE` is not co-located. It is not a market engine.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Currency / sixth Chamber resource | **REJECT.** Needs its own RFC and removal test |
| Order book / clearinghouse | **REJECT.** Prices are terms Players offer |
| Silently start v0.6B | **REJECT.** v0.6B stays a distinct later package |
| Engineer harvest percent | **REJECT.** That is GC1-S2, still deferred |
| Lot quality / provenance grades | **DEFER** (SPEC GAP) |
| Storage spoilage | **DEFER** |
| Freight minigame / transport company | **REJECT.** Freight is `MOVE` energy and time |
| NPC shop / banker Player | **REJECT** |
| Global price ticker | **REJECT.** Erases local information advantage |
| Wallets, x402, tokens | **REJECT.** Doctrine hard deferral |

Pressures: **scarcity** (one energy pool), **distance** (nodes are in different rooms), **dependency** (you cannot occupy two rooms), **uncertainty** (no omniscient book).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc8-s0` |
| Catalog | `economy-catalog/gc8-s0` |
| Verbs | Existing `HARVEST`, `MOVE`, `TRADE` only |
| Advantage | Single-body distance, not a hidden multiplier |
| Events | Existing `BUDGET_CONSUMED`, `RESOURCE_TRANSFER`, `TRADE_*` |

### Comparative advantage (pinned)

A Player occupies **one** room and spends **one** energy pool.

`HARVEST` is co-located ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)).  
`TRADE` propose/accept is **not** co-located (both ACTIVE is enough).  
`MOVE` costs energy **1** per hop (plus any exit traversal_cost).  
`HARVEST` costs energy **2**, compute **1**.  
`TRADE` propose or accept costs compute **1**. Fees: none.

To collect from two rooms:

| Pattern | Required actions | Energy |
|---------|------------------|--------|
| Two Players, one at each node, then `TRADE` | `HARVEST` + `HARVEST` + `TRADE` | **4** |
| One Player | `HARVEST` + `MOVE`×hops + `HARVEST` | **4 + hops** |

The pair spends less energy for the same two-node collection whenever hops ≥ 1. That **is** S0 interdependence. Recognition strings (`explorer`, `engineer`, …) do not change `HARVEST` amounts or costs.

A generalist remains viable. They pay movement. They are not forbidden from harvesting both nodes.

### Explicitly not in the comparison

- Yield or cost multipliers from GC1 recognition
- Quality grades
- A courier verb
- A market-maker spread
- Remote `HARVEST`

### Market visibility

Completed `TRADE` may already project a public notice without amounts ([SPECTATOR.md](SPECTATOR.md), [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)). S0 adds **no** global index, ticker, or order book.

---

## A–J

| Test | Result |
|------|--------|
| A | Resource + location + trade + player. No currency primitive |
| B | All four pressures |
| C | No extra commands |
| D | Couples to mastery (no bonus), social memory, later construction routes |
| E | Verb-stable |
| F | A sit-and-trade habit can form without a company engine |
| G | Existing transfer events remain attributable |
| H | Human and agent Players use the same costs |
| I | Meaningful with research hidden |
| J | Without this, “specialization” is only a title |

---

## Out of S0

```text
currency credit banking insurance
order book global price index
v0.6B contracts and markets
lot quality / provenance schema
storage spoilage
route_link freight table
GC1-S2 repair/harvest percent
NPC shops
wallets x402 NFTs tokens
```

---

## Runtime rule

Hosted v0.1 already contains the comparison: pair `HARVEST`+`TRADE` spends energy 4; lone `HARVEST`+`MOVE`+`HARVEST` spends 5. Magnitudes are unchanged. No mastery yield. No economy fields added to production Genesis.

## Acceptance (narrower than scenario H)

1. Two Players harvesting two rooms and trading spend energy 4.
2. One Player doing the same with one intervening hop spends energy 5.
3. An `engineer` recognition does not raise harvest amount.
4. Currency, order book, wallet, and v0.6B flags are `FEATURE_FORBIDDEN`.

Full scenario H (named Explorer/Engineer/Broker practices outperforming a generalist across discovery *and* development) still needs GC1-S2 and/or later quality/transport pins. S0 only pins the distance half.
