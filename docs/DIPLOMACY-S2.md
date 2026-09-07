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

## Extension Points

Non-normative extension guidance; the authorities above remain controlling.

- **Five-type agreement presentation:** An agreement adapter can derive help and accessible type selection from diplomacy-catalog/s2 while submitting the existing form/accept/terminate path. Localize explanatory labels, not the five machine identifiers or canonical command grammar.
- **Preserved invariants:** S2 closes the AGREEMENT family: no sixth type, ACCESS_POLICY verb, new event, WED/ATTEST help, ticker, or YOUR POSITION projection. Breach effects do not turn into pre-emptive contest blocking.
- **Compatibility and promotion:** Keep S0/S1 formation lifecycle and RFC-0100 effects authoritative. A richer client requires no effect-writing plugin; any changed machine semantics need separate accepted authority, not an EP implementation choice.
- **Verification targets:** In isolated fixtures cover every catalog type, malformed and sixth-type rejection, applicable live effects, and the same ordinary authority checks for native and assisted commands. Confirm AGREEMENT help appears while forbidden help and WATCH ticker remain absent; retain Genesis unchanged.
