# ACCESS_POLICY S0 — GRANT_ACCESS exit deny / clear

**Status:** Executable specification. Runtime authorized with RFC-0101.  
**Parent:** [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0101](../rfcs/RFC-0101-access-policy.md)  
**Does not open:** ALLOW_ONLY · ROOM scope · ACCESS_POLICY help · WED/ATTEST help · YOUR POSITION · event-catalog/0.3  
**Next:** [ACCESS-POLICY-S1.md](ACCESS-POLICY-S1.md)

S0 hosts the existing `COMMIT.ACCESS_POLICY` verb for **EXIT DENY and CLEAR** only. Authority is an occupied `GRANT_ACCESS` office. Restrictions reuse the live `access_restrictions` store and `ACCESS_RESTRICTED` event.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Anyone may lock an exit | **REJECT.** Authority is `GRANT_ACCESS`. |
| New events | **REJECT.** |
| ALLOW_ONLY | **REJECT.** MOVE only understands DENY today. |
| ROOM scope | **REJECT.** EXIT only. |
| Help ACCESS_POLICY | **REJECT.** |
| Geography rewrite / hidden rooms | **REJECT.** Public rooms only. |
| Personal (no `acting_for`) | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s0` |
| Catalog | `access-policy-catalog/s0` |
| Verb | existing `COMMIT.ACCESS_POLICY` |
| Scope | `EXIT` in the actor’s current public room |
| Modes | `DENY` · `CLEAR` |
| Authority | occupied office `GRANT_ACCESS` via `acting_for` |
| Cost | compute 1, influence 2 (treasury) |
| Events | `ACCESS_RESTRICTED` |
| Default expiry | `cycle + 4` (DENY) |
| Help | still omits ACCESS_POLICY |
| WATCH | existing `access_changed` / restriction projection; no ticker |

---

## Runtime rule

Hosted Chamber MUST accept `access <dir> deny for <org>` and `access <dir> clear for <org>` when the actor holds an occupied `GRANT_ACCESS` office on that org, is entered, and stands in a public room that has that exit. DENY appends a live restriction and `ACCESS_RESTRICTED`. CLEAR removes a matching live restriction and emits `ACCESS_RESTRICTED` (`mode=CLEAR`). Isolated tests only. Help unchanged. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize access policy terms (DENY/CLEAR, GRANT_ACCESS, EXIT/ROOM scope, ACCESS_RESTRICTED, org/player names, restriction notices, "access <dir> deny", "access here deny", "for <org>"), "Evidence operations", "Evidence and receipts", "Verification", CLI ONLY, status headers, player/controller labels in /play /watch /study /admin. Ties to prior sweeps (status_header, evidence, etc.).
- **R3 Chamber**: Full policy enforcement, restriction sims, and evidence in agent-only controller mode (full GRANT_ACCESS authority); human NON-CANONICAL limited public WATCH (visible restrictions only), permissioned STUDY for traces/ledgers, PLAY isolated with observable MOVE blocks. Per RFC-0120.
- **Gate B (S0-S3 controller policies)**: S0 public restriction overviews in WATCH; S1+ ROOM/EXIT for basic; S3 full controller access to policy registry, enforcement, revokes. Human S0 only. Version comparisons for access catalog. Controller enrollment for authority (agent vs human).
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic tables/lists for restrictions (role="table"), ARIA for verbs/scopes, live regions for ACCESS_RESTRICTED updates, keyboard for commands ("access ..."), theme contrast. CDP/browser_exec on /play /watch /admin.
- **noema skill / plugin atoms**: Modular atoms for access policy registry/viewer, restriction simulator, enforcement notifier for desktop plugins + gateway /play /admin integration + Chamber contest/ecology/LEARN.
- **LCA2 / MUD handoff / cross-refs**: To ACTION-CONTRACTS (verb scope), PLAYER-ACTION-MAP, STRATEGIC-CONFLICT (crime via violations), DATA-MODEL (restrictions as entities), DIPLOMACY (access as coupling), GAME-COMPLETENESS-PLAN, R3 evidence bundle, MUD craft for policy mechanics, ANOMALY-DETECTION (coordination via restrictions), WORLD-REPORTS. Full R3 Chamber fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable policy evidence/restrictions in Chamber; DX modular slices + i18n + graft + atoms; AX semantic/ARIA + CDP. Additive, backward-compatible. Per AGENTS.md.

(Expanded per "merge and continue" + prior slices to 83+ EPs.)
