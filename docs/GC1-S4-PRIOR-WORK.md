# GC1-S4 — Prior-Work Track Benefits

**Status:** Executable specification. Runtime authorized with RFC-0044.  
**Depends on:** [GC1-S3-DECAY.md](GC1-S3-DECAY.md)  
**RFC:** [RFC-0044](../rfcs/RFC-0044-prior-work-benefits.md)  
**Does not open:** WATCH titles · class discounts · seal bypass · `event-catalog/0.3`

S4 gives Explorer, Surveyor, and Broker a benefit only when they have already done the work on that room, entity, or counterparty.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Cheaper MOVE / blanket INSPECT | **REJECT.** Class discount |
| Repeat LOOK/INSPECT free on a **known** object | **ACCEPT.** Prior work |
| Broker waives caution for a **prior** party | **ACCEPT.** |
| Bypass sealed INSPECT | **REJECT.** |
| WATCH titles | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s4` |
| Catalog | `mastery-catalog/gc1-s4` |
| Explorer | recognized + MAINTAINED + room already visited → LOOK attention 0 |
| Surveyor | recognized + MAINTAINED + entity already inspected → INSPECT attention 0 |
| Broker | recognized + MAINTAINED + prior settled trade with this party → TRADE_CAUTION extra 0 |
| First time | full cost / caution unchanged |
| LATENT | full cost / caution |

---

## Out of S4

```text
WATCH / public titles
FOCUS_DECLARED
office eligibility — closed by [GC1-S5-OFFICE-ELIGIBILITY.md](GC1-S5-OFFICE-ELIGIBILITY.md)
parameter-access upgrades
SPECIALIZATION_* events
```

---

## Runtime rule

Hosted Chamber MUST waive only the three prior-work costs above. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative extension guidance; this section does not change accepted behavior or prove runtime completion.

- Extend isolated prior-work eligibility fixtures across room, entity and settled counterparty identity. Keep each waiver dependent on recognized, MAINTAINED practice and the relevant prior work; first-time and LATENT attempts retain normal costs.

- Preserve the three published waivers only: repeat LOOK attention, repeat INSPECT attention and prior-party TRADE_CAUTION. No blanket MOVE discount, sealed-target bypass, WATCH title or authority grant follows from recognition.

- Pin mastery-catalog/gc1-s4 and RFC-0044 when comparing adapters. Any changed benefit or eligibility rule needs its governing accepted contract; help, Genesis and isolated-test restrictions remain unchanged.

- Validate known versus new targets, MAINTAINED versus LATENT, absent settled trade evidence and a sealed INSPECT denial. Compare charged costs and authorization results without revealing private practice to other Players.
