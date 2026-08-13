# Emergent Culture (GC9)

**Status:** Product authority for evidence-backed cultural persistence. P2. Phase GC-D.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Extends:** [DEEP-TIME.md](DEEP-TIME.md) · [LORE-BOUNDARY.md](LORE-BOUNDARY.md) · [INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md)  
**Does not silently become:** roadmap **v0.6C Semantic Evolution**.

Hard invariant:

> Culture and lore may interpret history. They may never rewrite canonical history.

---

## Canonical chain

```text
repeated behavior
  → custom
  → tradition
  → institution
  → cultural identity
```

This chain is **derived**. Institutions already have a first-class lifecycle ([INSTITUTIONS.md](INSTITUTIONS.md)). Culture is how later Players **inherit interpreted practice**.

---

## Layer distinction (must remain distinct)

| Layer | What it is | May be wrong? | May rewrite ledger? |
|-------|------------|---------------|---------------------|
| Canonical event | Ledgered world event | No (it happened) | — |
| Historical evidence | Accessible remnant | Incomplete / corrupted | No |
| Institutional memory | What an institution records | Yes | No |
| Player belief | Private interpretation | Yes | No |
| Shared interpretation | Reconstruction or widely messaged story | Yes | No |
| Cultural convention | Derived custom/tradition presentation | Yes | No |
| Derived lore | PLAY/WATCH compression of the above | Yes | No |

If lore conflicts with evidence, **evidence wins** ([LORE-BOUNDARY.md](LORE-BOUNDARY.md)).

---

## Candidate derived forms

Examples, not a content pack:

```text
names
titles (presentation only unless bound to an office)
rituals (repeated scheduled practices)
symbols
phrases
taboos
memorials
holidays (cycle-recurring commemorations)
founding stories
local terminology
governance customs
institutional practices
```

A “ritual” that changes world state is either an existing action (repair schedule, meeting) or it is presentation. Presentation has no authority ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)).

---

## Emergence, mutation, extinction, revival

| Concern | Rule |
|---------|------|
| Threshold | Versioned repetition of a practice by an institution or local population across cycles. Exact N is SPEC GAP |
| Evidence | Ledgered actions + institutional practice records + names/scars |
| Persistence | Derived culture records persist while evidence remains accessible or institutionally held |
| Mutation | Later practice drift creates a successor convention with a lineage edge; old convention remains historical |
| Disagreement | Two groups MAY hold incompatible conventions about the same events. Both are culture. Neither edits the ledger |
| Extinction | No custodians and no accessible evidence → convention becomes `LATENT` / fragmentary, not deleted |
| Revival | New practice plus citation of old evidence may mark `REVIVED` with continuity class, similar to institution revival |
| Succession | Cultural display names follow Deep Time naming; IDs stable |
| Presentation | PLAY speaks in inherited names and customs without claiming they are physics |

v0.6C, if later specified, MAY deepen semantic lineage. GC9 MUST NOT implement a procedural lore generator ([SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) out-of-scope list).

---

## SPEC GAP

```text
custom/tradition derived schema (or reuse semantic-lineage + institution practices)
emergence thresholds
PLAY projection without a second canon
fixtures: repeated repair custom → institution practice → later generation still sees it
conformance: lore cannot override ledger
```

---

## Acceptance (scenario I)

Players repeatedly perform a practice (for example, a maintenance order at a named relay). Later Players inherit an evidence-backed custom or institutional tradition using that name. Archives and culture interpret the founding. The original events remain the only canonical history.
