# Systemic Discovery (GC6)

**Status:** Product authority for evidence problems, not authored quests. P1. Phase GC-B.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Composes, does not replace:** [EXPLORATION.md](EXPLORATION.md) · [HISTORICAL-EVIDENCE.md](HISTORICAL-EVIDENCE.md) · [HISTORICAL-RECONSTRUCTION.md](HISTORICAL-RECONSTRUCTION.md) · [ARCHAEOLOGY.md](ARCHAEOLOGY.md) · [CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md) · [LORE-BOUNDARY.md](LORE-BOUNDARY.md) · [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md)

No authored omniscient quest narrator. No second lore canon.

**Doctrine:** mysteries are world-state + partial observability + evidence. No quest engine ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)).

GC6-S0 machine pins: [GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md) · [RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md). GC6-S1 reconstruction: [GC6-S1-RECONSTRUCTION.md](GC6-S1-RECONSTRUCTION.md) · [RFC-0024](../rfcs/RFC-0024-historical-reconstruction.md). Public WATCH contradiction pulse remains **SPEC GAP**.

---

## Thesis

NOEMA should produce **evidence problems**:

```text
Archive evidence says Relay Seven was destroyed.
Relay Seven is operating.
Why?
```

Players investigate with ordinary actions. The world does not hand them a quest giver, a journal checkbox, or a research oracle.

---

## How mysteries originate

Closed origin classes:

| Origin | How it appears |
|--------|----------------|
| Genesis / story seeds | Unresolved records, missing evidence, scars ([STORY-SEEDS.md](STORY-SEEDS.md), [GENESIS.md](GENESIS.md)) |
| Player / institution action | Construction, dismantle, breach, archive damage, abandoned offices |
| Decay | Incomplete or corrupted accessible evidence ([HISTORICAL-DECAY.md](HISTORICAL-DECAY.md)) |
| Communication failure | Delayed, rumored, or partial reports ([COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)) |
| World Event Director | Bounded condition change that leaves traces ([WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md)) |
| Ordinary contradiction | Stale sensor vs current `INSPECT` ([CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md)) |

Forbidden origin: an operator-authored quest chain with predetermined Player steps.

Potential world conditions (examples, not a content pack):

```text
hidden routes
forgotten infrastructure
misidentified artifacts
abandoned institutions
unknown resource sites
historical contradictions
encrypted / inaccessible records
lost agreements
ruined settlements
uncertain maps
damaged archives
environmental anomalies
```

---

## Canonical truth vs what Players have

| Layer | Authority |
|-------|-----------|
| Canonical truth | Ledger + current world state |
| Surviving evidence | Accessible artifacts, archives, scars, reports, infrastructure state |
| Decayed evidence | Still in ledger if it was an event; **in-world access** may be gone or fragmentary |
| Player observation | Permissioned, noisy, partial ([OBSERVATION.md](OBSERVATION.md)) |
| Player belief | Private; never rewrites truth |
| Shared reconstruction | Historical reconstruction output; may remain `CONTESTED` |
| Institutional memory | What the institution records, possibly wrong |
| Derived lore | Presentation only ([LORE-BOUNDARY.md](LORE-BOUNDARY.md)) |

The engine MAY know which archive line is false. PLAY MUST NOT be told unless ordinary evidence makes it knowable.

---

## Investigation through normal actions

No `QUEST` verb. Investigation is:

```text
LOOK · INSPECT · optional QUERY
MOVE to the site
REPAIR / later BUILD.RESTORE
MESSAGE / archives / boards
TRADE for documents or access
ORG / office access
CONTEST or diplomacy for access
historical reconstruction when the Player compiles accessible evidence
```

Discovery states remain those in [EXPLORATION.md](EXPLORATION.md):

```text
unknown → discovered → observed → investigated → understood
```

`understood` means actionable Player knowledge, not guaranteed truth.

---

## False beliefs, contradiction, settlement

- False beliefs form when Players trust fragmentary or rumored evidence.
- Contradiction is represented by existing contradiction sets and contested reconstructions — not by a narrator saying “you are wrong.”
- A discovery is **settled for a Player** when their accessible evidence set supports a reconstruction with no remaining contradiction they can see.
- A discovery is **settled for the world** only if world state is actually that way. Player consensus is not world truth.
- Shared knowledge forms by messages, notices, archives, and institutions choosing to record a reconstruction.
- Institutional memory may adopt a reconstruction. That adoption is evidence of **belief**, not a ledger rewrite.

If two institutions adopt opposite stories, both records stand. Canonical history is still the ledger.

---

## Effects on other systems

A better-evidenced reconstruction MAY change:

- which routes Players use;
- which sites they harvest or repair;
- which institutions they trust ([SOCIAL-MEMORY.md](SOCIAL-MEMORY.md));
- which contests they start;
- which archives they fund.

It MUST NOT automatically teleport, spawn loot, or complete a quest flag.

---

## PLAY / WATCH / research

| Surface | Rule |
|---------|------|
| PLAY | Evidence, uncertainty, and ordinary actions. No quest log of hidden objectives |
| WATCH | Public discoveries and public contradictions; no research `known_truth_relationship` |
| STUDY | May ask why beliefs diverged; Lab/Compiler remain isolated from production truth |

---

## SPEC GAP

```text
GC6-S0 closed: archive vs live INSPECT contradiction; no QUEST; no oracle
GC6-S0 source closed (RFC-0015): INSPECT ARTIFACT with explicit archive_subject_entity_id + archive_claim
GC6-S1 closed: Player reconstruction from accessible archive/inspect; not ledger truth
hosted Perihelion: genesis artifacts still silent until ATTEST
WATCH public contradiction without known_truth leak
settled-for-world by consensus (still rejected)
```

Prefer **zero** new verbs and **reuse** of Deep Time schemas.

---

## Acceptance (scenario F)

Players find conflicting archive vs live `INSPECT` evidence, investigate with ordinary actions, hold different beliefs, and later produce a better-evidenced reconstruction. No quest oracle tells them the answer. The ledger is unchanged by their story.
