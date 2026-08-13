# GC6 First Slice — Archive vs Live Inspect

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md)  
**Does not open:** `QUEST` · quest log · discovery events · reconstruction compile action · `event-catalog/0.3` · authored quest chains

S0 is the smallest discovery increment that still satisfies scenario F’s *shape* (conflicting archive vs live `INSPECT`, no oracle). It reuses [CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md) and [EXPLORATION.md](EXPLORATION.md) discovery states. Historical reconstruction compile is GC6-S1.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `QUEST` / `JOURNAL` / `DISCOVER` verb | **REJECT.** Investigation is ordinary `LOOK` / `INSPECT` |
| Quest log of hidden objectives | **REJECT.** PLAY shows evidence, not a checkbox |
| Engine tells which signal is true | **REJECT.** `known_truth_relationship` is research-only |
| `DISCOVERY_*` / `QUEST_*` events | **REJECT.** Reuse existing `INSPECT` / `OBSERVATION_GENERATED` and accessible archive records |
| Player consensus rewrites the ledger | **REJECT.** Lore is not truth ([LORE-BOUNDARY.md](LORE-BOUNDARY.md)) |
| WATCH publishes the research answer | **REJECT.** S0 WATCH is empty |
| Auto-settle when popular | **REJECT.** Parent: popularity is not fact |
| Genesis reseed with a “Relay Seven was destroyed” pack | **REJECT.** This slice does not add first-world content |

Pressures: **uncertainty** (two accessible signals disagree) and **dependency** (you only see the contradiction if you actually read both).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc6-s0` |
| Catalog | `discovery-catalog/gc6-s0` |
| Evidence pair | Accessible archive claim + accessible live `INSPECT` of the same entity |
| State | Derived PLAY projection. Not WorldState. Not a reducer input |
| Events | None new. Existing observation / archive records only |
| Public S0 projection | **None** |

### Conflict rule

A Player sees the S0 contradiction when all of:

1. An archive record about entity E is accessible to them.
2. They have a live `INSPECT` observation of E.
3. Archive claim ∈ {`DESTROYED`, `OPERATING`} disagrees with inspect observation ∈ {`DESTROYED`, `OPERATING`}.

Then:

| Field | Value |
|-------|--------|
| `resolution_status` | `open` |
| `agent_visible_relationship` | `unresolved` |
| Discovery state | `investigated` (not `understood`) |
| Self PLAY line | `The archive and the live site do not agree.` |
| WATCH | omit |
| Other Players | omit unless they independently hold both members |

If only one member is accessible, there is **no** contradiction line and no quest prompt. Archive-only is `discovered`. Inspect-only is `observed`. Both agreeing is `investigated` with no S0 line.

`understood` is not granted by S0. That waits for a later reconstruction the Player compiles from accessible evidence ([HISTORICAL-RECONSTRUCTION.md](HISTORICAL-RECONSTRUCTION.md)).

### Rebuild rules

1. Restrict archive and inspect members to those listing the subject in `accessible_to`.
2. Ignore members whose `subject_entity_id` differs.
3. Compare `claim` vs `observation` only on the closed pair `{DESTROYED, OPERATING}`.
4. Never copy `known_truth_relationship` or `research_visible_relationship` into PLAY or WATCH.
5. Never emit a quest objective, reward, or “you are wrong” line.
6. Projection does not write events and does not mutate the ledger.

### Visibility

| Audience | S0 |
|----------|----|
| Self (both members) | Conflict line only |
| Self (one member) | Nothing from this slice |
| Other Players | Nothing from this slice |
| WATCH | Nothing from this slice |
| STUDY / research | May hold `known_truth_relationship`; must stay off PLAY |

### Coupling (S0)

This slice is **evidence projection**, not a reward engine. It remains coupled to **INFORMATION** (partial access) and **ASSET** (the live entity). Later repair, MOVE to the site, or reconstruction may change what is accessible; they do not complete a quest flag.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + asset. No quest primitive |
| B | Uncertainty + dependency |
| C | No extra commands; contradiction falls out of archive + `INSPECT` |
| D | Couples to repair, archives, later reconstruction, social memory |
| E | No new verb |
| F | An archive-reading habit can form without a quest giver |
| G | Member refs are existing evidence ids |
| H | Human and agent Players use the same rebuild |
| I | Meaningful with STUDY hidden; research truth stays off PLAY |
| J | Without this, archive vs live is flavor |

---

## Out of S0

```text
QUEST JOURNAL DISCOVER
quest log / objectives / XP
DISCOVERY_* events
historical reconstruction compile
settled-for-world by consensus
WATCH contradiction pulse
rumor-as-evidence (GC5-S1)
Genesis content pack
oracle / narrator
```

---

## Runtime rule

This document does not change Chamber PLAY and does not add archive rows to Perihelion Reach.

**Hosted adapter: blocked.** Chamber has no structured archive record `{subject_entity_id, claim ∈ {DESTROYED, OPERATING}, accessible_to}`. Existing `entity.archive-ledger` is an ARTIFACT without those fields. S0 must not infer a claim from flavor text, World Services copy, or WATCH. A Perihelion “destroyed relay” pack remains rejected ([RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md)). Do not project the conflict line until a later RFC names the archive-record source.

## Acceptance (narrower than scenario F)

1. A Player with an accessible “destroyed” archive and a live `OPERATING` `INSPECT` of the same entity sees the conflict line.
2. A Player with only the `INSPECT` sees no conflict line and no quest prompt.
3. A third Player sees nothing from this slice.
4. WATCH is empty.
5. `known_truth_relationship` never appears in PLAY lines.
6. The projection writes no events.

Full scenario F (divergent beliefs, later better-evidenced reconstruction) is **GC6-S1**.
