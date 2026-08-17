# Diplomacy S1 — AGREEMENT_TERMINATE

**Status:** Executable specification. Runtime authorized with RFC-0098.  
**Parent:** [DIPLOMACY-S0.md](DIPLOMACY-S0.md) · [DIPLOMACY.md](DIPLOMACY.md)  
**RFC:** [RFC-0098](../rfcs/RFC-0098-diplomacy-terminate.md)  
**Does not open:** other types · AGREEMENT help · WED/ATTEST help · diplomacy report · event-catalog/0.3  
**Next:** [DIPLOMACY-S2.md](DIPLOMACY-S2.md)

S1 hosts the existing `COMMIT.AGREEMENT_TERMINATE` verb for agreements already formed by S0.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Silent delete | **REJECT.** |
| Bystander break | **REJECT.** |
| Help AGREEMENT | **REJECT.** |
| Other types | **REJECT.** |
| Influence map debit | **REJECT.** Compute cost only. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `diplomacy-s1` |
| Catalog | `diplomacy-catalog/s1` |
| Verb | existing `COMMIT.AGREEMENT_TERMINATE` |
| Who | a `party_id` |
| Active | `AGREEMENT_BROKEN` |
| Offered | offerer withdraw, no event |
| Cost | compute 1 |
| Help | still omits AGREEMENT |
| WATCH | existing `agreement_broken`; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `terminate agreement <id> reason=<enum>` from a party. ACTIVE → `BROKEN` and `AGREEMENT_BROKEN`. OFFERED withdrawn by the offerer emits nothing. Isolated tests only. Help unchanged. No Genesis change.
