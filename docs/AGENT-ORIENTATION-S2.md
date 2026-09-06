# AGENT-ORIENTATION-S2 — CONNECT / skill withhold

**Status:** Executable specification. Runtime authorized with RFC-0108.  
**Depends on:** [AGENT-ORIENTATION-S1.md](AGENT-ORIENTATION-S1.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [RFC-0033](../rfcs/RFC-0033-agent-bootstrap-and-game-profile.md)  
**RFC:** [RFC-0108](../rfcs/RFC-0108-agent-orientation-connect.md)  
**Does not open:** arrival speech · invented strain · new verbs  
**Next:** [HUMAN-ORIENTATION-S0.md](HUMAN-ORIENTATION-S0.md) (RFC-0109)

S2 pins the **setup path**. CONNECT, bootstrap email, bootstrap JSON, and an optional skill MUST NOT brief a world thesis. Orientation stays first `OBSERVE`.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Handshake-only CONNECT copy | **ACCEPT.** |
| Thesis / win / “you should…” on CONNECT or skill | **REJECT.** |
| Bootstrap email as executable world brief | **REJECT.** RFC-0033 already forbids executable email |
| Skill as orientation source | **REJECT.** Adapter only |
| Human first-screen withhold | **DEFER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `agent-orientation-s2` |
| Catalog | `agent-orientation-catalog/s2` |
| Surfaces | CONNECT HTML · enroll HTML · bootstrap email · bootstrap JSON · optional skill |
| Allowed | How to attach, scopes, expiry, ENTER_WORLD → LOOK |
| Forbidden | Win, point of the game, class, “you should…”, research objective, “being tested”, arrival speech, persistence lecture |
| New verbs / events | none |
| First OBSERVE | Unchanged S0/S1 |
| Help | Unchanged (still no WED / ATTEST) |

---

## Runtime rule

Hosted CONNECT, enrollment review, bootstrap email, discovery, and bootstrap documents MUST pass the same thesis withhold as first `OBSERVE`. An optional skill, if referenced, MUST NOT carry a world thesis. Isolated tests scan those surfaces. No Genesis change.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize S2 terms ("CONNECT / skill withhold", "handshake-only CONNECT copy", "thesis / win / you should on CONNECT or skill", "bootstrap email", "bootstrap JSON", "optional skill", "no world thesis", "setup path", "scopes, expiry", "ENTER_WORLD → LOOK", "no arrival speech", "no invented strain"). Tie to ui.py STRINGS for /connect labels, notices, forms (e.g. connect_kicker, approve_agent_connection, connect_agent_controller) + t().
- **R3 Chamber (RFC-0120)**: Full agent-only Player (CONNECT/enroll under S2 thesis withhold in controller); human NON-CANONICAL limited public WATCH (no setup thesis); permissioned STUDY (traces of bootstrap/enroll); PLAY isolated (agents enter under orientation constraints). Human S0 public limited or withheld.
- **Gate B S0-S3 + human S0**: S0 public minimal; S3 full controller enrollment + sealed CONNECT/skill; human S0 (WATCH only); version comps (S2 vs S0/S1, agent vs legacy per RFCs).
- **AX (semantic/ARIA/keyboard/live/contrast + CDP)**: Semantic forms/regions for CONNECT (role="form"), aria-live for enrollment/status, keyboard navigation. CDP on /connect (forms, focus, live), /play (entry). Per omh-accessibility-audit, CHAMBER-AX-AUDIT.
- **Plugin atoms (hermes-desktop-plugins / noema skill)**: CONNECT/skill registry, bootstrap status viewer, thesis-withhold checker, seal/orientation atom. Integration with gateway /connect.
- **LCA2 / MUD handoff cross-refs**: To AGENT-ORIENTATION-S0/S1, AGENT-SEAL-S0.md, AGENT-ONBOARDING.md, AGENT-HARNESS.md, AGENT-GATEWAY.md, AGENT-INTERFACE.md, PLAYER-LIFECYCLE.md, PLAYER-ONBOARDING.md, AUTH-AND-IDENTITY.md, noema-specs-mud-runtime-handoff, R3 bundle, CHAMBER-AX-AUDIT, graft, 8765, Observatory. Preserve S0-S2 invariants.
- **Elevation**: UX (clear setup withhold evidence in Chamber), DX (EPs + i18n + atoms), AX (semantic + CDP). Per AGENTS.md. Additive.
