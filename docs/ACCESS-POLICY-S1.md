# ACCESS_POLICY S1 — ROOM deny / clear

**Status:** Executable specification. Runtime authorized with RFC-0102.  
**Parent:** [ACCESS-POLICY-S0.md](ACCESS-POLICY-S0.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**RFC:** [RFC-0102](../rfcs/RFC-0102-access-policy-room.md)  
**Does not open:** ALLOW_ONLY · ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3  
**Next:** [ACCESS-POLICY-S2.md](ACCESS-POLICY-S2.md)

S1 adds **ROOM** scope to the existing `COMMIT.ACCESS_POLICY` verb. EXIT DENY/CLEAR from S0 stay. Authority, cost, and event stay S0.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| ALLOW_ONLY | **REJECT.** MOVE still only checks DENY. |
| Inbound lock | **REJECT.** ROOM DENY blocks leaving the room, same as contest. |
| Help ACCESS_POLICY | **REJECT.** |
| New events | **REJECT.** |
| Hidden rooms | **REJECT.** Public rooms only. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s1` |
| Catalog | `access-policy-catalog/s1` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scopes | `EXIT` (S0) · `ROOM` (this slice) |
| Modes | `DENY` · `CLEAR` |
| Authority | occupied `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| Help | still omits ACCESS_POLICY |
| WATCH | existing restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access here deny for <org>` and `access here clear for <org>` (alias `room`) under the same GRANT_ACCESS rule as S0. ROOM DENY writes a live restriction on the actor’s current public room. MOVE from that room is rejected while the restriction is live. CLEAR removes a matching ROOM restriction. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize ROOM scope terms, "access here deny/clear", restriction notices, error messages, "Evidence operations", status, player/controller labels, "Evidence and receipts" in /play /watch /admin. Ties to prior i18n (evidence, status_header).
- **R3 Chamber**: Full ROOM policy enforcement/sims in agent-only controller (full authority); human NON-CANONICAL public WATCH restrictions, permissioned STUDY traces, PLAY observable blocks. Per RFC-0120.
- **Gate B (S0-S3)**: Builds on S0; S1 ROOM for basic, S3 full registry/enforcement. Human S0. Version comps. Controller enrollment impact.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic for restrictions (role="table"), ARIA, live regions for updates, keyboard commands, contrast. CDP on /play /watch /admin.
- **noema skill / plugin atoms**: Atoms for policy viewer, restriction sim for plugins + gateway /play /admin + Chamber integration.
- **LCA2 / MUD handoff / cross-refs**: To S0, ACTION-CONTRACTS, STRATEGIC-CONFLICT, DATA-MODEL, DIPLOMACY, R3 bundle, MUD, ANOMALY, WORLD-REPORTS. Full R3 fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable in Chamber; DX modular + i18n + atoms; AX semantic/ARIA + CDP. Additive. Per AGENTS.md.

(Expanded per "merge and continue" + prior to 83+ EPs.)
