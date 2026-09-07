# GC3-S5 — Published Trade Caution

**Status:** Executable specification. Runtime authorized with RFC-0037.  
**Parent:** [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)  
**RFC:** [RFC-0037](../rfcs/RFC-0037-trade-friction.md)  
**Does not open:** auto-refuse · hidden markups · affordance hiding

S5 couples live (S4 weight > 0) danger/deceptive edges to a **published** extra compute on `TRADE` propose. It rejects RFC-0022's deferred auto-refuse.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Auto-reject dangerous counterparties | **REJECT.** |
| Hidden price / inventory markup | **REJECT.** Leak + price engine |
| Hide TRADE in the GUI | **REJECT.** Partial-observability leak |
| Change offer/want lots | **REJECT.** Frozen v0.1 amounts |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc3-s5` |
| Catalog | `social-memory-catalog/gc3-s5` |
| Trigger | `TRADE` propose |
| Extra | `+1` compute when a live hostile edge exists |
| Reason | `TRADE_CAUTION` |
| Auto-reject | false |

### Live hostile edge

The acting subject (the Player, or the org when `acting_for` is set) has S4 weight > 0 on danger (S1/S3) or deceptive (S6/S3) toward the counterparty.

Decayed or rehabilitated edges do **not** surcharge.

### Observation

- Affordance lists the extra compute before confirm
- Failed pay: `BUDGET_EXCEEDED` + `TRADE_CAUTION`
- Accept/reject remain Player/office choice
- Line MAY add `You proceed with caution toward {name}.` after a successful propose; never names method or stock

---

## A–J

| Test | Result |
|------|--------|
| A | Trade + memory |
| B | Extra cost is public to the actor, not a secret markup |
| C | No extra command |
| D | TRADE only |
| E | No new verb |
| F | Players may still deal, at visible caution |
| G | Uses existing danger/deceptive evidence |
| H | Same surcharge for human and agent |
| I | Meaningful with STUDY hidden |
| J | Without this, memory cannot change trade without auto-refuse |

---

## Out of S5

```text
auto-refuse
hidden prices
preferred-counterparty discounts — closed by [GC3-S7](GC3-S7-PREFERRED.md)
hiding TRADE
```

---

## Runtime rule

Hosted Chamber MAY add +1 compute on propose when a live hostile edge exists. v0.1 base TRADE compute remains. Help may mention caution cost on `help trade` / `help org`. No new verb.

## Extension Points

Non-normative published-cost and acting-subject regression seams.

- Extend TRADE propose previews across personal and acting_for subjects, selecting that subject’s live S4 danger/deceptive edge toward the counterparty. Weight greater than zero permits the published +1 compute caution; decayed or rehabilitated edges do not surcharge.
- Preserve visible pre-confirm cost, BUDGET_EXCEEDED plus TRADE_CAUTION on failed payment, frozen offer/want lots and independent accept/reject choice. Never auto-refuse, hide TRADE, mark up inventory or reveal the underlying hidden method through a reason label.
- Compatibility/promotion: pin social-memory-catalog/gc3-s5/RFC-0037 and base TRADE costs; retain the runtime rule’s MAY rather than claiming every host has enabled it. RFC-0120 limits Player execution to agents; comparison fixtures confer no human gameplay authority or Controller access to org-private edges.
- Verification proposal: test positive/zero hostile weights, org versus personal memory, sufficient/insufficient compute and unchanged lots/affordances. Check pre-confirm cost equals the admitted path and the optional successful caution line names only the permitted handle. Localized and accessible cost text must expose the surcharge without disclosing another subject’s memory.
