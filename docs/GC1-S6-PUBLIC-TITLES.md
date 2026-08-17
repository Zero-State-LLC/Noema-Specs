# GC1-S6 — Public titles

**Status:** Executable specification. Runtime authorized with RFC-0105.  
**Depends on:** [GC1-S1-RECOGNITION.md](GC1-S1-RECOGNITION.md) · [GC1-S5-OFFICE-ELIGIBILITY.md](GC1-S5-OFFICE-ELIGIBILITY.md)  
**RFC:** [RFC-0105](../rfcs/RFC-0105-public-titles.md)  
**Does not open:** focus-as-ledger · `FOCUS_DECLARED` · `event-catalog/0.3` · WED / ATTEST help · XP / practice counts on WATCH

S6 lets other Players in a **public** room, and WATCH, see one world-native recognition line derived from existing GC1-S1 evidence. It is not a class, not a new event, and not a cheaper verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Public third-person line from existing recognition | **ACCEPT.** Social reaction |
| Publish practicing (not recognized) lines | **REJECT.** |
| Publish LATENT recognition | **REJECT.** Recognition remains; public line withheld |
| Hidden-room titles | **REJECT.** |
| More than one public line per other Player | **REJECT.** Cap 1 |
| New `SPECIALIZATION_RECOGNIZED` event | **REJECT.** Still derived |
| WATCH ticker / private counts | **REJECT.** Same public line only |
| Self `practice_lines` change | **REJECT.** First-person self lines stay S1/S3 |
| Focus ledger / `FOCUS_DECLARED` | **DEFER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s6` |
| Catalog | `mastery-catalog/gc1-s6` |
| Evidence | Existing GC1-S1 distinct-unit recognition |
| New verbs | none |
| New events | none |
| Self PLAY | Unchanged `practice_lines` |
| Public PLAY | `public_practice_lines` on **other** Players in the same **public** room |
| Copy | World-native, third person. Not XP, not track ids |
| Cap | 1 line per other Player. Prefer catalog `display_order` among live recognized tracks |
| LATENT | No public line |
| Hidden rooms | No public titles |
| WATCH | Same public line while the Player is in a public room. No ticker. No private counts |
| Help | Unchanged (still no WED / ATTEST) |

---

## Public lines (pinned)

When a track is recognized and **not** LATENT, the public line is:

| Track | Public line |
|-------|-------------|
| explorer | `{handle} knows these rooms.` |
| surveyor | `{handle} is known for survey work.` |
| broker | `{handle} is known for closing exchanges.` |
| engineer | `{handle} is known for keeping infrastructure alive.` |

Never print counts, XP, levels, track ids, or research scores.

---

## Out of S6

```text
FOCUS_DECLARED / focus as ledger
event-catalog/0.3
WED / ATTEST help
XP / public practice counts
class discounts
parameter-access upgrades
```

---

## Runtime rule

Hosted Chamber MUST attach at most one third-person public title to each other entered Player in the observer's **public** room, derived from that Player's existing recognition. LATENT and hidden rooms withhold the line. WATCH uses the same line. Isolated world `test.hosted-canonical.gc1-s6`. Help unchanged. No Genesis change.
