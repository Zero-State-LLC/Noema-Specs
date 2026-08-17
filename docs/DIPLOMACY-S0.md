# Diplomacy S0 — TRADE agreement form

**Status:** Executable specification. Runtime authorized with RFC-0097.  
**Parent:** [DIPLOMACY.md](DIPLOMACY.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0097](../rfcs/RFC-0097-diplomacy-trade.md)  
**Does not open:** AGREEMENT_TERMINATE · other types · AGREEMENT help · WED/ATTEST help · diplomacy report · event-catalog/0.3  
**Next:** AGREEMENT_TERMINATE or remaining types

S0 hosts the existing `COMMIT.AGREEMENT_FORM` verb for **TRADE** only.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Bind without accept | **REJECT.** |
| All five types | **REJECT.** TRADE only. |
| AGREEMENT_TERMINATE | **REJECT.** Later. |
| Help AGREEMENT | **REJECT.** |
| New events | **REJECT.** |
| Preferential discount | **REJECT.** GC3-S7 already exists. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `diplomacy-s0` |
| Catalog | `diplomacy-catalog/s0` |
| Verb | existing `COMMIT.AGREEMENT_FORM` |
| Type | `TRADE` only |
| Consent | offer then matching accept |
| Cost | compute 2, influence 1 per successful form |
| Events | `AGREEMENT_FORMED` on accept only |
| Help | still omits AGREEMENT |
| WATCH | existing `agreement_formed` projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `form agreement trade with <player>` when both parties are entered in the same public room. The first call stores an `OFFERED` TRADE agreement. The named counterparty's matching call marks it `ACTIVE` and appends `AGREEMENT_FORMED`. Other types are `FORM_FORBIDDEN`. Isolated tests only. Help unchanged. No Genesis change.
