# GC3-S7 — Preferred-Counterparty Discount

**Status:** Executable specification. Runtime authorized with RFC-0039.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [GC3-S5-TRADE-FRICTION.md](GC3-S5-TRADE-FRICTION.md)  
**RFC:** [RFC-0039](../rfcs/RFC-0039-preferred-counterparty.md)  
**Does not open:** auto-accept · hidden rebates · hiding TRADE · free propose

S7 is the published discount RFC-0037 left out of S5. Preference **waives caution**. It does not change lots or skip consent.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Auto-accept reliable counterparties | **REJECT.** |
| Hide other TRADE affordances | **REJECT.** Leak |
| Secret rebate | **REJECT.** |
| Compute 0 on propose | **REJECT.** Frozen v0.1 base |
| Change offer/want | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s7` |
| Catalog | `social-memory-catalog/gc3-s7` |
| Trigger | `TRADE` propose |
| Preferred | live S0/S3 `RELIABLE` (≥ 3 distinct accepted trades, S4 weight > 0) |
| Discount | waive S5 `TRADE_CAUTION` extra compute |
| Auto-accept | false |

### Cost table

| Live RELIABLE | Live hostile | Extra compute |
|---------------|--------------|---------------|
| no | no | 0 |
| no | yes | 1 (`TRADE_CAUTION`) |
| yes | no | 0 |
| yes | yes | 0 (waiver) |

Base TRADE compute remains 1. Accept/reject unchanged.

### Observation

- Affordance MAY say preferred; it still lists every visible counterparty
- Waiver is observable: no `TRADE_CAUTION` on the cost line
- PLAY MAY add `You prefer to deal with {name}.` — never amounts or methods

---

## A–J

| Test | Result |
|------|--------|
| A | Trade + memory |
| B | Discount is public to the actor |
| C | No extra command |
| D | TRADE propose only |
| E | No new verb |
| F | A brokerage habit can form without auto-accept |
| G | Uses S0/S3/S4 evidence |
| H | Same for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, preference cannot change cost except as a hidden minigame |

---

## Out of S7

```text
auto-accept
hiding TRADE
secret rebate
compute 0 base
changing offer/want
```

---

## Runtime rule

Hosted Chamber MUST waive `TRADE_CAUTION` when the acting subject has a live `RELIABLE` edge toward the counterparty. Help may mention the waiver. No new verb.
