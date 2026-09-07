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

## Extension Points (additive, i18n AX R3 Gate B handoff + DIPLOMACY-S / without full sections)

- **i18n centralization (STRINGS + t())** for AGREEMENT_TERMINATE, COMMIT.AGREEMENT_TERMINATE, AGREEMENT_BROKEN, terminate agreement, reason=enum, party_id, OFFERED withdrawn — for /play /watch /study diplomacy surfaces.
- **R3 / RFC-0120**: Agent-only; diplomacy for agents + human S0 oversight.
- **Gate B**: S1 slice contract; access for terminate; versioned catalog.
- **AX**: ARIA for agreement lists, live updates on BROKEN; semantic tables; keyboard for forms.
- **Plugin atoms**: Atomic for agreement packs (terminate, validate); graft/ops for diplomacy.
- **LCA2 / MUD / PLAYER-ACTION-MAP**: Native verbs for terminate; i18n parser terms; handoff to S0/S2.
- **Cross-refs**: DIPLOMACY-S0.md, DIPLOMACY.md, ACTION-CONTRACTS.md, PLAYER-ACTION-MAP.md, AGENT-*/AUTH/PLATFORM/GAME-COMPLETENESS, NOEMA-HIGH-VALUE..., graft, 8765, noema-specs-mud-craft.
- **Handoff**: LCA2 Gate B traceability for institutional/diplomacy flows + attention projection.
