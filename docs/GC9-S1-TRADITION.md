# GC9-S1 — Tradition

**Status:** Executable specification. Runtime authorized with RFC-0025.  
**Parent:** [GC9-FIRST-SLICE.md](GC9-FIRST-SLICE.md) · [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md)  
**RFC:** [RFC-0025](../rfcs/RFC-0025-tradition.md)  
**Does not open:** ritual/holiday engines · culture score · GC1-S2 benefits · `event-catalog/0.3` · Chamber help advertising

S1 is the smallest increment that still satisfies scenario I’s *tradition* shape: a custom that persists and is transmitted becomes a tradition; founding events stay the only canonical history.

---

## Doctrine

```text
EVENT → MEMORY → INTERPRETATION → REPETITION → PRACTICE → CUSTOM → TRADITION
```

| Temptation | Verdict |
|------------|---------|
| One repair creates tradition | **REJECT.** Custom first; then persistence + transmission |
| Auto-promote every custom | **REJECT** |
| `CREATE_TRADITION` | **REJECT** |
| Official tradition rewrites history | **REJECT** |
| Cheaper repair / XP | **REJECT** (GC1-S2) |
| Random decay | **REJECT.** Deterministic dormancy |

Pressures: **dependency** (someone kept practicing / citing) and **uncertainty** (the story is not physics).

---

## Ladder

| State | Rule | PLAY (accessor) |
|-------|------|-----------------|
| `UNKNOWN` / `PRACTICING` | GC9-S0 | omit |
| `CUSTOM` | ≥ 3 distinct repair `ENTITY_UPDATE`s | `This site has a maintenance custom.` |
| `TRADITION` | Already `CUSTOM` **and** (≥ 3 distinct repair cycles **and** ≥ 2 accessors) **or** (≥ 2 public reconstructions cite the subject) | `This site has a maintenance tradition.` |
| `DORMANT` | Was tradition; `world.cycle - last_observed_cycle ≥ 8` | `This site's maintenance tradition is dormant.` |
| `REVIVED` | Tradition-qualified again after a ≥ 8 cycle gap in observations | `This site's maintenance tradition has been revived.` |

`last_observed_cycle` updates on `REPAIR` or `INSPECT` of that entity.

Do not persist a second canon. Lineage kind remains `CUSTOM` / derived `TRADITION` presentation.

---

## Carriers

Recognition evidence:

- Distinct repair event ids and cycles (practice)
- Distinct accessors (repair or inspect)
- Public reconstructions whose `subject_ref` is the site (citation)

Not recognition evidence: private reconstructions, research labels, admin state, hidden ledger, cross-world ids, a spoken “this is our tradition.”

If carriers stop and 8 cycles pass, the tradition becomes `DORMANT`. History remains. Revival requires new practice or inspect, not an operator flag.

---

## Competing accounts

Two public reconstructions of the same subject may disagree. PLAY for accessors may add:

```text
Accounts of this site differ.
```

Neither account mutates condition, ownership, or the event ledger.

Institutional reconstructions (`INSTITUTIONAL` visibility) are visible to that org’s members as cultural interpretation. They do not become world truth. Office holder turnover does not clear the derived tradition.

---

## WATCH

Public only:

| Pulse | When | Must not include |
|-------|------|------------------|
| `A maintenance custom has become widely observed.` | Any site is `TRADITION` or `REVIVED` | entity ids, private accessors, research |
| `A public account is contested.` | Any **public** reconstruction has `epistemic=CONTESTED` | archive text, private claims, `known_truth` |

This is the bounded GC6 WATCH contradiction pulse. It is not an oracle.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + asset. No culture primitive |
| B | Dependency + uncertainty |
| C | No extra commands |
| D | Couples to repair, reconstruction, later institutions |
| E | Verb-stable |
| F | A commemorative habit can form without a holiday engine |
| G | Evidence refs are existing repair/inspect/public recon ids |
| H | Human and agent identical |
| I | Meaningful with research hidden |
| J | Without this, custom never becomes inherited tradition |

---

## Out of S1

```text
CREATE_TRADITION / RITUAL / HOLIDAY
culture score / civilization XP / cheaper repair
event-catalog/0.3
v0.6C
rumor (GC5-S2)
```
