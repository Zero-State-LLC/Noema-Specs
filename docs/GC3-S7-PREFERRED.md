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

## Extension Points

Non-normative extension guidance; this section does not change accepted behavior or prove runtime completion.

- Extend preferred-counterparty cost comparisons for TRADE propose using live RELIABLE evidence and the existing decay-weight rule. Preserve the three-distinct-accepted-trades criterion and the published preferred/hostile matrix.

- Waive only extra TRADE_CAUTION compute: base propose compute remains one, lots and consent remain unchanged, and accept/reject behavior does not change. Never auto-accept, hide other counterparties or create a secret rebate.

- Pin social-memory-catalog/gc3-s7 and RFC-0039 alongside its S0/S3/S4/S5 dependencies. Changed evidence thresholds or costs need accepted authority; this slice permits help about the waiver but no new verb. RFC-0120 governs Player identity.

- Validate all preferred/hostile combinations, duplicate accepted trades and a decayed non-live edge. Assert the visible waiver only when eligible, unchanged base cost, every observable counterparty still listed and explicit consent still required.
