# GC1-S5 — Office eligibility

**Status:** Executable specification. Runtime authorized with RFC-0055.  
**Depends on:** [GC1-S4-PRIOR-WORK.md](GC1-S4-PRIOR-WORK.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md)  
**RFC:** [RFC-0055](../rfcs/RFC-0055-office-eligibility.md)  
**Does not open:** WATCH titles · class discounts · `ROLE_*` · evict-on-latent · Explorer/Surveyor gates  
**Next:** [GC1-S6-PUBLIC-TITLES.md](GC1-S6-PUBLIC-TITLES.md) (RFC-0105)

S5 lets a named office require a recognized Engineer or Broker. Others cannot sit that seat. It is not a title and not a cheaper verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Gate every repair / treasury office | **REJECT.** Additive field only |
| WATCH titles | **REJECT.** |
| Class discount | **REJECT.** |
| Evict when LATENT | **REJECT.** Recognition remains |
| `ROLE_*` / new verb | **REJECT.** Existing `ORG_OFFICE_ASSIGN` |
| Explorer / Surveyor required | **DEFER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s5` |
| Catalog | `mastery-catalog/gc1-s5` |
| Create | optional `requires_track` ∈ {`engineer`, `broker`} |
| Assign | existing `ORG_OFFICE_ASSIGN` |
| Eligible | recognized on that track (LATENT included) |
| Ineligible | `FORBIDDEN` |
| Unrestricted office | any current member |
| Events | `ENTITY_*` / `BUDGET_CONSUMED` |
| PLAY reject | `That office requires a recognized Engineer.` / `Broker.` |
| WATCH | silent |
| Help | unchanged |

---

## Out of S5

```text
WATCH / public titles
class discounts
ROLE_*
evict-on-latent
Explorer / Surveyor required tracks
FOCUS_DECLARED
```

---

## Runtime rule

Hosted Chamber MUST refuse `ORG_OFFICE_ASSIGN` (and designated succession seating) when `requires_track` is set and the target is not recognized on that track. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend eligibility explanations around optional requires_track on named offices, showing the assignment or succession refusal without publishing private mastery history. Test the same seat through recognition, LATENT status, and successor selection.

### Compatibility and promotion

RFC-0055 leaves unrestricted offices unchanged and allows recognized engineer/broker only where the optional gate is set. LATENT does not evict an incumbent. S5 does not add public titles, extra tracks, discounts, ROLE_* events, or Controller-level grants. Later title slices do not retroactively widen this visibility.

### Verification before adoption

Exercise unrestricted assignment, each recognized required track, wrong/unrecognized track, LATENT eligibility, and designated succession. Confirm no automatic eviction, no WATCH eligibility detail, and no mutation on FORBIDDEN. Preserve older office fixtures and require a versioned authority change for any additional track or seating rule.
