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

Non-normative extension guidance; accepted contracts and closed decisions remain authoritative.

- **Situation seam:** Extend first-observation fixtures that map `situation.place` to the current LOCATION name and attach `situation.strain` only from an already-visible worn-infrastructure, empty-stock, or public-report fact.
- **Preserved invariants:** A quiet room omits strain; no inferred crisis, goal briefing, arrival speech, or invented evidence. WATCH has no `situation`, not a reduced or minimal version. Agent status does not unlock research-private traces.
- **Compatibility:** Keep S0 orientation doctrine and S1 catalog behavior stable while testing the S2 integration boundary. A localization layer may translate display text but cannot rename wire keys, change omission semantics, or add help verbs.
- **Verification:** Test quiet and strained rooms, current-room changes, and a report unavailable to the actor. Compare first OBSERVE/LOOK with its canonical room facts and inspect WATCH payloads for absence of `situation`; an isolated fixture is not proof of live deployment.
- **Consumer experience:** Controller adapters can render a compact situation summary without assigning a task. Any human-facing test viewer remains non-canonical tooling, with semantic text for present/absent facts and no synthesized strain announcements.
