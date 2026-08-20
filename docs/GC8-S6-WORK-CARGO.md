# GC8-S6 — Work consumes cargo

Authority: [RFC-0118](../rfcs/RFC-0118-work-consumes-cargo.md). Catalog: [`economy-catalog.gc8-s6.json`](../specs/economy-catalog.gc8-s6.json).

`storage` stays free capacity. Grant 16. Full hold is 0. Do not invert live numbers. Work verbs consume cargo (free storage up). TRADE `storage: N` is cargo. No new verbs. No currency/crypto. WATCH silent on pack.

## Verb table

AUTH-INFRA-CLASS **amounts** stay. The **sign** of `storage` on work verbs flips.

| Act | Hold | Energy / other |
|-----|------|----------------|
| HARVEST | fills: free storage −amount, require free storage ≥ amount | energy 2, compute 1; node `stock_amount` still pays energy; empty node still “Not enough stock available.” |
| REPAIR | consumes: free storage **+** cargo cost (base 1, workshop may discount) | energy 3, compute 2 unchanged; require occupied hold ≥ cargo cost |
| CONSTRUCT | same as REPAIR: cargo in, free storage up | existing energy/compute/influence; WORN construct extra is extra **cargo**, not extra empty pack |
| TRADE `storage: N` | cargo: giver free storage **+N**, receiver **−N** | energy / compute / influence still giver minus, receiver plus |
| MOVE | unchanged | empty 1, carrying 2 |
| WAIT | unchanged | RFC-0117: if energy 0 **and** storage 0 after cycle side effects → energy 2, storage 1 |

Empty hold (16): can harvest; cannot repair (“no materials in hold”).  
Full hold (0): can repair; cannot harvest.

## PLAY copy, WATCH, rejects

Agents paraphrase affordance `reason`. Name hold and cargo. Never “storage capped,” wallets, coins, crypto.

**Help**

- HARVEST: fills hold · costs energy 2, compute 1 · needs free storage. Empty-node WAIT and lockout WAIT lines stay.
- REPAIR: costs energy 3, compute 2, and cargo 1 (frees storage).
- CONSTRUCT: cargo in, free storage up.
- TRADE: `storage:` on an offer is cargo. Giver frees hold; receiver must have free storage.

**Affordance / command reject (self-only)**

| Case | Line |
|------|------|
| Harvest, pack full | `You do not have enough free storage.` |
| Harvest, node empty | `Not enough stock available.` |
| Repair / construct, empty hold | `You do not have materials in hold.` |
| Repair, no energy/compute | existing energy/compute line |
| TRADE, giver not carrying | `You are not carrying that.` |
| TRADE, receiver pack full | `They do not have enough free storage.` |

**WATCH**

Silent on pack fullness, cargo tickers, and TRADE contents. Repair/harvest stay self-only. Public pulses stay culture/pressure, not inventory. GC8-S4 WATCH-silent cargo stands.
