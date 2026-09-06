# ACCESS_POLICY S2 — ALLOW_ONLY

**Status:** Executable specification. Runtime authorized with RFC-0103.  
**Parent:** [ACCESS-POLICY-S1.md](ACCESS-POLICY-S1.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)  
**RFC:** [RFC-0103](../rfcs/RFC-0103-access-policy-allow-only.md)  
**Does not open:** ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3 · inbound-only locks  
**Next:** [ACCESS-POLICY-S3.md](ACCESS-POLICY-S3.md)

S2 adds **ALLOW_ONLY** to the existing `COMMIT.ACCESS_POLICY` verb. EXIT/ROOM DENY and CLEAR from S0/S1 stay. Authority, cost, and `ACCESS_RESTRICTED` stay.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New events | **REJECT.** |
| ALLOW_ONLY `applies_to=*` | **REJECT.** A list is required. |
| ALLOW_ONLY punches through DENY | **REJECT.** DENY still wins. |
| Help ACCESS_POLICY | **REJECT.** |
| Inbound lock | **REJECT.** Same outbound MOVE check as DENY. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s2` |
| Catalog | `access-policy-catalog/s2` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scopes | `EXIT` · `ROOM` |
| Modes | `DENY` · `CLEAR` · `ALLOW_ONLY` |
| Authority | occupied `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| ALLOW_ONLY list | named Player; not `*` |
| MOVE | listed party may take the route; anyone else is rejected |
| Help | still omits ACCESS_POLICY |
| WATCH | existing restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access <dir|here> allow for <org> applies_to=<player>` under the same GRANT_ACCESS rule as S0/S1. ALLOW_ONLY writes a live restriction. MOVE on a matching route succeeds only for the listed player. Other live DENY restrictions still reject. CLEAR removes a matching ALLOW_ONLY restriction. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize ALLOW_ONLY terms, "access <dir|here> allow for <org> applies_to=<player>", restriction notices, MOVE rejections, "Evidence operations", status, player/controller labels, "Evidence and receipts" in /play routes/actions, /watch projections, admin. Ties to prior (evidence, status_header, from_agent_tag, etc.).
- **R3 Chamber**: Full ALLOW_ONLY policy enforcement, restriction sims, MOVE success/fail in agent-only controller mode; human NON-CANONICAL public WATCH (visible restrictions), permissioned STUDY traces, PLAY observable blocks. Per RFC-0120.
- **Gate B (S0-S3 controller policies)**: Builds on S0/S1; S2 ALLOW_ONLY for listed players; S3 full registry/enforcement. Human S0. Version comps. Controller enrollment impact on authority.
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic for restrictions (role="table"), ARIA states, live regions for success/fail, keyboard commands ("access ... allow"), contrast via vars. CDP/browser_exec on /play /watch.
- **noema skill / plugin atoms**: Atoms for policy registry/restriction viewer/sim/enforcement notifier for desktop plugins + gateway /play /watch /admin + Chamber contest/ecology/LEARN.
- **LCA2 / MUD handoff / cross-refs**: To S0/S1, ACTION-CONTRACTS, PLAYER-ACTION-MAP, STRATEGIC-CONFLICT (crime), DATA-MODEL, DIPLOMACY, GAME-COMPLETENESS, R3 evidence bundle, MUD craft, ANOMALY, WORLD-REPORTS. Full R3 Chamber fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable policy in Chamber; DX modular slices + i18n + graft + atoms; AX semantic/ARIA + CDP. Additive. Per AGENTS.md.

(Expanded per "continue" / merge and continue + prior to 83+ EPs.)
