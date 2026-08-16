# Economic Specialization (GC8)

**Status:** Product authority for Player economic interdependence. P2. Phase GC-C.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) · [INFRASTRUCTURE.md](INFRASTRUCTURE.md)  
**Does not silently become:** roadmap **v0.6B Contracts & Markets** (still a distinct, not-started follow-up).

**Doctrine:** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md). Ground in scarcity, distance, dependency, and uncertainty. Do not add transport companies, warehouses, banks, or markets as independent engines. Those nouns emerge from primitives and practices.

GC8-S0 machine pins: [GC8-FIRST-SLICE.md](GC8-FIRST-SLICE.md) · [RFC-0012](../rfcs/RFC-0012-distance-interdependence.md). Lot quality, storage loss, and v0.6B remain **SPEC GAP**.

This package deepens:

```text
resources → production → infrastructure → trade
```

into interdependence among Players. It is **not** an executable market package.

---

## Removal test

Do **not** add currency, credit, banking, insurance, or an order book merely because the words sound complete.

A proposed mechanic is legal only if:

1. it has a world-native referent already in Chamber semantics (lots, nodes, rooms, relays, agreements, storage, condition);
2. removing it would collapse a real interdependence;
3. it does not require a new Player caste.

v0.6B, if later specified, MAY add formal contracts/markets **after** passing the same test. GC8 MUST NOT pre-empt that RFC.

---

## Desired ecology (play pattern, not NPC jobs)

```text
Explorer discovers
Surveyor evaluates
Engineer develops
Logistician transports
Broker exchanges
Institution protects
Archivist records
```

These are [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) practices plus ordinary verbs. World Services (Exchange Broker, Quartermaster, …) remain desks, not competing citizens ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

---

## Settled dimensions (product)

| Dimension | Settlement |
|-----------|------------|
| Comparative advantage | Geography + infrastructure + proficiency make some Players cheaper/better at a function. Not a hidden multiplier soup |
| Specialization incentives | Peak throughput, quality, or access comes from focus + exchange. A generalist remains viable at lower peak ([GAME-BALANCE.md](GAME-BALANCE.md)) |
| Resource quality | Allowed as a **bounded lot attribute** if it changes production/trade meaningfully. Exact grades SPEC GAP. Do not add infinite rarity tiers |
| Regional scarcity | Already implied by nodes + geography. Completeness makes scarcity **visible in local observations and reports**, not a global ticker |
| Transport cost | Movement + later `route_link` + storage. Energy and time are the freight. Do not add a separate freight minigame |
| Storage loss | Optional versioned spoilage/overflow already hinted by overflow loss. Only add if it creates logistics roles |
| Production specialization | Infrastructure specialization dimension already exists. Couple it to who maintains the node |
| Throughput | Condition + capacity + proficiency quality bands |
| Infrastructure reliability | Condition + World Event Director + contest damage |
| Market visibility | Public completed `TRADE` summaries and notices; **no** omniscient order book in this package |
| Price formation | Not a clearinghouse. Prices are terms Players offer. History of accepted trades MAY be locally visible |
| Trade history | Public or party-visible completed trades as evidence ([SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)) |
| Supply-chain dependency | A production_node that needs input lots from another room/Player |
| Ownership | Existing holdings + later construction ownership |
| Contracts | v0.2 `AGREEMENT_*` / `RESOURCE_COMMITMENT` first. Richer instruments wait for v0.6B |
| Obligation instruments | **Out of scope** here unless v0.6B defines them |
| Service exchange | Players trading work (repair, survey, escort-as-contest-defense) via ordinary TRADE/AGREEMENT, not a job board engine |
| Provenance-bearing outputs | Lots MAY carry origin room / producer id if it enables archive or quality play. MUST NOT leak hidden sites to unauthorized inspectors |
| Risk / failure / recovery | Node depletion, route loss, breach, overflow. Recovery via repair, alternate route, new trade ([LOSS-RECOVERY.md](LOSS-RECOVERY.md)) |
| Anti-monopoly pressure | Large holdings increase exposure (storage, contest targets, maintenance). No secret tax. No single victory via hoarding ([GAME-BALANCE.md](GAME-BALANCE.md)) |

---

## What this package must not do

- Introduce money as a seventh Chamber resource without a dedicated RFC and removal test.
- Create NPC shopkeepers or banker Players.
- Make one specialization strictly dominate all others.
- Publish a global price index that erases local information advantage.

---

## SPEC GAP

```text
GC8-S0 closed: pair HARVEST+TRADE energy 4 vs lone +MOVE; no yield bonus
GC8-S1 closed: SOUND/WORN lots; worn if node condition < 50; WORN construct storage +1
GC8-S2 closed: public origin room + producer on harvest; hidden/mix clear
transport-cost table beyond MOVE energy
whether storage loss is in or deferred
relationship to future v0.6B (still a distinct RFC)
conformance beyond anti-currency / anti-order-book fixtures
```

First runtime work for economy remains the frozen v0.1 resource contract. GC8 is later deepening.

---

## Acceptance (scenario H)

An Explorer/Surveyor, an Engineer, a Logistician, and a Broker (recognized practices or equivalent work) outperform a single Player attempting discovery, development, transport, and exchange alone on the same map, without a currency or order book.
