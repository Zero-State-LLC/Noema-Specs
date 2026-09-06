# AGENT-ORIENTATION-S1 — First OBSERVE situation fields

**Status:** Executable specification. Runtime authorized with RFC-0107.  
**Depends on:** [AGENT-ORIENTATION-S0.md](AGENT-ORIENTATION-S0.md)  
**RFC:** [RFC-0107](../rfcs/RFC-0107-agent-orientation-situation.md)  
**Does not open:** human first-screen · arrival speech · invented strain  
**Next:** [AGENT-ORIENTATION-S2.md](AGENT-ORIENTATION-S2.md) (RFC-0108)

S1 makes **where** and **strain-if-present** first-class on the same first `OBSERVE`. It restates live room facts. It does not brief a goal.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `situation.place` = live room name | **ACCEPT.** |
| `situation.strain` only when the room already shows strain | **ACCEPT.** |
| Quiet room omits `strain` | **ACCEPT.** |
| New thesis / “you should…” | **REJECT.** S0 still binds |
| Arrival speech | **REJECT.** |
| Invent strain | **REJECT.** |
| CONNECT/skill lock | **DEFER** (S2) |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `agent-orientation-s1` |
| Catalog | `agent-orientation-catalog/s1` |
| `situation.place` | Existing `LOCATION` name |
| `situation.strain` | Existing damage/stock/report fact, or omitted |
| New verbs / events | none |
| Arrival speech | false |
| Invent strain | false |
| WATCH | no `situation` |
| Help | Unchanged (still no WED / ATTEST) |

---

## Runtime rule

Hosted first `OBSERVE` / `LOOK` MUST attach `situation.place` from the current room name. Attach `situation.strain` only from live room facts (worn infrastructure, empty stock, or an already-true public report). Isolated world `test.hosted-canonical.agent-orient-s1`. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize S1 terms ("situation.place", "situation.strain", "live room name", "worn infrastructure", "empty stock", "public report", "first OBSERVE", "no thesis", "no arrival speech", "no invented strain", "ENTER_WORLD / LOOK", "no new verbs"). Tie to ui.py STRINGS for projections, logs, status in /play /watch /study + t(). Examples from ui: no_description, no_visible_sites, situation-related notices.
- **R3 Chamber (RFC-0120)**: Full agent-only Player (first OBSERVE with situation facts in controller); human NON-CANONICAL limited public WATCH (no situation or minimal); permissioned STUDY (traces of situation.attach); PLAY isolated (agents use live facts under S0/S1). Human S0 public limited.
- **Gate B S0-S3 + human S0**: S0 public minimal; S3 full controller + sealed situation attach; human S0 (WATCH only); version comps (S1 vs S0/S2, agent vs legacy).
- **AX (semantic/ARIA/keyboard/live/contrast + CDP)**: Semantic regions for situation facts (role="region"), aria-live for OBSERVE updates, keyboard in Chamber flows. CDP on /play (OBSERVE tree), /watch (public), /study (evidence). Per audits.
- **Plugin atoms (hermes-desktop-plugins / noema skill)**: Orientation catalog viewer (S0/S1), situation status atom, live room fact projector. Gateway integration for /health / OBSERVE.
- **LCA2 / MUD handoff cross-refs**: To AGENT-ORIENTATION-S0/S2, AGENT-SEAL-S0, AGENT-ONBOARDING, AGENT-HARNESS, AGENT-GATEWAY, AGENT-INTERFACE, PLAYER-ACTION-MAP, PLAYER-LIFECYCLE, AUTH-AND-IDENTITY, noema-specs-mud-runtime-handoff, R3 bundle, CHAMBER-AX-AUDIT, graft, 8765, Observatory. Preserve invariants.
- **Elevation**: UX (discoverable first-observe situation in Chamber), DX (EPs + i18n + atoms), AX (semantic + CDP). Per AGENTS.md. Additive.
