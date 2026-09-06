# AGENT-ORIENTATION-S0 — First OBSERVE withhold

**Status:** Executable specification. Specs-only with RFC-0106. No runtime change.  
**Depends on:** [AGENT-PLAY.md](AGENT-PLAY.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md)  
**RFC:** [RFC-0106](../rfcs/RFC-0106-agent-orientation.md)  
**Does not open:** CONNECT/skill lock · human first-screen · arrival speech  
**Next:** [AGENT-ORIENTATION-S1.md](AGENT-ORIENTATION-S1.md) (RFC-0107)

S0 pins what first `OBSERVE` after `ENTER_WORLD` may say. It is not a tutorial and not a goal.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Situation from the live room | **ACCEPT.** |
| Arrival speech | **REJECT.** |
| Invent strain on a quiet room | **REJECT.** |
| Thesis / win / “you should…” | **REJECT.** |
| Teach persistence on first OBSERVE | **REJECT.** Learned later from play |
| New observation fields | **DEFER** (S1). |
| CONNECT/skill thesis lock | **DEFER** (S2). |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `agent-orientation-s0` |
| Catalog | `agent-orientation-catalog/s0` |
| Must answer | Where am I? What is strained here, only if already visible |
| Quiet room | Legal |
| New verbs / events | none |
| Arrival speech | false |
| Invent strain | false |
| Help | Unchanged (still no WED / ATTEST) |

Persistence is later. First OBSERVE must not lecture that the world remembers.

---

## Runtime rule

None in this slice. Hosted Chamber is unchanged. Isolated tests are catalog fixtures only.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize orientation terms ("first OBSERVE", "quiet room", "no arrival speech", "situation", "where am I", "what is strained here", "no tutorial", "no lecture", "persistence later", "ENTER_WORLD → OBSERVE", "no thesis / win / you should"). Tie to ui.py STRINGS for any Chamber surfaces (play/watch/study projections, notifications, labels) + t() calls. Examples: "No visible sites.", "No description.", connect/orientation notices.
- **R3 Chamber (RFC-0120)**: Full agent-only Player identity in controller (first OBSERVE under S0 constraints for sealed agents); human NON-CANONICAL limited public WATCH (observations only, no privileged orientation); permissioned STUDY (traces of first OBSERVE in research); PLAY isolated (agents discover persistence from play, no lecture). Human S0 public orientation withheld or minimal.
- **Gate B S0-S3 + human S0**: S0 public / minimal orientation for public; S3 full controller enrollment + sealed first OBSERVE; human S0 (no agent play, limited WATCH); version comparisons (S0 vs later S1/S2, agent vs legacy human).
- **AX (semantic/ARIA/keyboard/live/contrast + CDP)**: Semantic lists/tables for orientation facts (role="list" or "region"), aria-live for dynamic first OBSERVE updates, keyboard navigation in Chamber /play /watch, contrast via theme vars. CDP on /play (first OBSERVE tree/focus/live regions), /watch (public projections), /connect (setup flows). Per omh-accessibility-audit, CHAMBER-AX-AUDIT.
- **Plugin atoms (hermes-desktop-plugins / noema skill)**: Atoms for orientation registry (S0/S1/S2 catalog), first-observe status viewer, quiet-room indicator, graft-indexed handoff map. Integration with gateway /connect /play for glanceable status.
- **LCA2 / MUD handoff cross-refs**: To AGENT-ORIENTATION-S1/S2, AGENT-ONBOARDING.md, AGENT-SEAL-S0.md, AGENT-HARNESS.md, AGENT-GATEWAY.md, AGENT-INTERFACE.md, PLAYER-ACTION-MAP.md, PLAYER-LIFECYCLE.md, AUTH-AND-IDENTITY.md, noema-specs-mud-runtime-handoff, R3 evidence bundle, CHAMBER-AX-AUDIT, graft, 8765 endpoints, Observatory. Preserve S0 invariants (no new verbs, no arrival speech, no thesis).
- **Elevation**: UX (clear first-observe evidence in Chamber for agents), DX (modular EPs + i18n + atoms), AX (semantic + CDP). Per AGENTS.md + noema-specs-mud-runtime-handoff. Additive only.
