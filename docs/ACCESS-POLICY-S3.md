# ACCESS_POLICY S3 — Chamber ACCESS help

**Status:** Executable specification. Runtime authorized with RFC-0104.  
**Parent:** [ACCESS-POLICY-S2.md](ACCESS-POLICY-S2.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0104](../rfcs/RFC-0104-access-policy-help.md)  
**Does not open:** WED/ATTEST help · YOUR POSITION · event-catalog/0.3 · new modes  
**Next:** ACCESS_POLICY S0–S3 is the hosted family. WED / ATTEST help stay parked. Do not invent S4.

S3 lets Chamber PLAY name ACCESS. The operations are the ones already hosted in S0–S2.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New ACCESS verb | **REJECT.** |
| Help WED / ATTEST | **REJECT.** |
| Advertise ACCESS_POLICY schema name | **REJECT.** Player line is ACCESS. |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s3` |
| Catalog | `access-policy-catalog/s3` |
| Help ACCESS | true |
| Help WED / ATTEST | false |
| New verbs | none |
| Modes | DENY · CLEAR · ALLOW_ONLY (unchanged) |
| WATCH | unchanged |

---

## Runtime rule

Hosted Chamber MUST list ACCESS on `help` and list existing deny / clear / allow aliases on `help access`. MUST still omit WED, ATTEST, and the schema name ACCESS_POLICY. Isolated tests only. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize ACCESS help text, aliases (deny/clear/allow), policy descriptions, "Chamber ACCESS help", help affordances in /play /watch /study, "help access", player labels, status, "Evidence operations". Ties to prior i18n (shell_*, trade, history, etc.).
- **R3 Chamber**: Full help for ACCESS in agent-only controller (full R3+ help surfaces); human NON-CANONICAL public WATCH / permissioned STUDY / PLAY with help. Per RFC-0120.
- **Gate B (S0-S3 controller policies)**: S3 enables help for access policies; full controller access to help content. Human S0. Version comps.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic lists for help (role="list"), ARIA for aliases, live regions for dynamic policy, keyboard for help commands, contrast. CDP on /play /watch.
- **noema skill / plugin atoms**: Atoms for help registry, policy help viewer for plugins + gateway + Chamber.
- **LCA2 / MUD handoff / cross-refs**: To S0-S2, PLAYER-ACTION-MAP, R3/R4 help, access as strategic, handoff map, AX audit, noema skill, 8765.
- **Elevation (UX/DX/AX)**: UX discoverable help in Chamber; DX modular + i18n + graft + atoms; AX semantic/ARIA + CDP. Per AGENTS.md.

(Expanded per "merge and continue".)
