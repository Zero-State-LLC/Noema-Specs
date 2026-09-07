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

Non-normative first-observation fixture and presentation seams; RFC-0106 remains closed.

- Add paired first-OBSERVE examples for a quiet room and a room with already-visible strain. Derive place and permitted facts from the room projection; do not fabricate tension, arrival speech, persistence lessons or a preferred ambition.
- Preserve the S0 no-new-fields/no-new-verbs boundary. Later S1 situation fields and S2 thesis lock belong to their own accepted contracts, not an S0 retrofit. S0/S1/S2 are orientation slices, and ACCESS S0–S3 are not human/Controller privilege levels.
- Compatibility/promotion: version fixture expectations by orientation catalog and retain legacy examples as historical data. No fixture, translated label or viewer may promote hidden research context into Agent Player observations; humans inspect only authorized WATCH or STUDY projections.
- Verification proposal: compare observed visible facts to room inputs, including the absence of strain in the quiet case; reject thesis, win, class, quest and tutorial additions. Verify repeated rendering does not produce world events. A human evidence viewer can localize captions and announce arrival of a record without transforming it into instructions to a Player.
