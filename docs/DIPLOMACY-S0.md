# Diplomacy S0 — TRADE agreement form

**Status:** Executable specification. Runtime authorized with RFC-0097.  
**Parent:** [DIPLOMACY.md](DIPLOMACY.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0097](../rfcs/RFC-0097-diplomacy-trade.md)  
**Does not open:** AGREEMENT_TERMINATE · other types · AGREEMENT help · WED/ATTEST help · diplomacy report · event-catalog/0.3  
**Next:** [DIPLOMACY-S1.md](DIPLOMACY-S1.md)

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

## Extension Points (additive, i18n AX R3 Gate B handoff + INSTITUTIONAL / DIPLOMACY / PLAYER / LCA / REMAINING)

- **i18n centralization (STRINGS + t())** for diplomacy terms (TRADE, OFFERED, ACTIVE, AGREEMENT_FORMED, FORM_FORBIDDEN, `form agreement trade with <player>`, agreement form, consent, cost 2 influence 1) — centralize in Chamber /play /connect for R3 agent-only / human S0.
- **AX / CDP** for diplomacy UI (semantic forms, aria for offers, keyboard on agreements, contrast on cards) — ties to /play projections, live regions.
- **R3 / RFC-0120 agent-only Player identity + human S0**: Diplomacy as agent actions; human S0 oversight.
- **Gate B S0-S3 + version comparisons**: S0 for TRADE; later S for other types.
- **Plugin atoms code**: Atomic for agreement packs (graft/ops/maint_evolve atomic_replace etc.; derive from player actions).
- **LCA2 / MUD handoff**: MUD native diplomacy verbs/commands; i18n in parsers; handoff to PLAYER-ACTION-MAP, MUD-NATIVE-INTERACTION-TASKS, ACTION-CONTRACTS, DIPLOMACY.md.
- **Cross-refs**: DIPLOMACY.md, ACTION-CONTRACTS.md, PLAYER-ACTION-MAP.md, AGENT-*, AUTH-AND-IDENTITY, PLATFORM, GAME-COMPLETENESS-PLAN, INSTITUTIONAL seeds, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, graft, 8765, noema-specs-mud-craft.
- **Handoff deepen**: LCA2 Gate B for diplomacy traceability; i18n/AX in R3 Chamber; institutional/attention projection.
