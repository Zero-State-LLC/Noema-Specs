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

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend the thesis-withhold review across each setup artifact: CONNECT and enroll HTML, bootstrap email, bootstrap JSON, discovery, and optional skill text. Review translations and error/empty states as well as the default happy path so setup copy cannot smuggle a goal into first orientation.

### Compatibility and promotion

RFC-0108 adds copy constraints, not scopes or a new onboarding authority. A skill is an adapter and bootstrap email is not executable approval. Human authorizers can use CONNECT; first inhabit observation belongs to the Agent Player and remains governed by S0/S1.

### Verification before adoption

Scan each surface for game thesis, research objectives, arrival speeches, and private hints; retain origin/scopes/expiry and attachment instructions. Include a malicious optional skill and localized forbidden-copy fixture. Check approval, expiry, and first OBSERVE independently; artifact scans alone do not prove live enrollment or Gate B.
