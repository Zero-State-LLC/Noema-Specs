# Diplomacy S2 — remaining types, effects, and help

**Status:** Executable specification. Runtime authorized with RFC-0100.  
**Parent:** [DIPLOMACY-S1.md](DIPLOMACY-S1.md) · [DIPLOMACY.md](DIPLOMACY.md)  
**RFC:** [RFC-0100](../rfcs/RFC-0100-diplomacy-closeout.md)  
**Does not open:** ACCESS_POLICY verb · WED/ATTEST help · event-catalog/0.3 · YOUR POSITION  
**Next:** [ACCESS-POLICY-S0.md](ACCESS-POLICY-S0.md)

S2 closes the AGREEMENT family. Form, accept, and terminate stay S0/S1.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New events | **REJECT.** |
| ACCESS_POLICY verb | **REJECT.** |
| Help WED / ATTEST | **REJECT.** |
| Sixth type | **REJECT.** |
| Block contest instead of breach | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `diplomacy-s2` |
| Catalog | `diplomacy-catalog/s2` |
| Types | TRADE · NON_AGGRESSION · ACCESS · RESOURCE_COMMITMENT · MUTUAL_DEFENSE |
| Help AGREEMENT | true |
| Help WED / ATTEST | false |
| New verbs | none |
| WATCH | existing formed/broken projections; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `form agreement <type> with <player>` for all five catalog types, apply the live effects in RFC-0100, and list AGREEMENT on `help` / `help agreement`. Isolated tests only. No Genesis change.
