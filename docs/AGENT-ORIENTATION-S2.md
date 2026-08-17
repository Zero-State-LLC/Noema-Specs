# AGENT-ORIENTATION-S2 — CONNECT / skill withhold

**Status:** Executable specification. Runtime authorized with RFC-0108.  
**Depends on:** [AGENT-ORIENTATION-S1.md](AGENT-ORIENTATION-S1.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [RFC-0033](../rfcs/RFC-0033-agent-bootstrap-and-game-profile.md)  
**RFC:** [RFC-0108](../rfcs/RFC-0108-agent-orientation-connect.md)  
**Does not open:** human first-screen withhold · arrival speech · invented strain · new verbs

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
