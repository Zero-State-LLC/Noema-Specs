# GC1-S8 — Engineer overhaul parameter

**Status:** Hosted. Agent Players discover `extent=overhaul` on structured REPAIR affordances when a recognized, maintained Engineer. No new verb.  
**Depends on:** [GC1-S2-ENGINEER-QUALITY.md](GC1-S2-ENGINEER-QUALITY.md) · [GC1-S3-DECAY.md](GC1-S3-DECAY.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)  
**RFC:** [RFC-0112](../rfcs/RFC-0112-parameter-access.md)  
**Does not open:** new verbs · `event-catalog/0.3` · multi-focus · decay-window credit · WED / ATTEST help · class discounts

S8 is the first **parameter-access** slice. A recognized, maintained Engineer MAY attempt a harder `REPAIR` extent. Same verb. No cheaper default repair.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Same verb + optional harder parameter | **ACCEPT.** |
| Cheaper ordinary REPAIR for Engineers | **REJECT.** Class discount |
| Overhaul without recognition | **REJECT.** |
| LATENT still overhauls | **REJECT.** Practiced hands have gone slack |
| New OVERHAUL verb | **REJECT.** |
| BUILD.UPGRADE-only this slice | **REJECT.** Perihelion play is REPAIR first |
| WED / ATTEST help | **REJECT.** Parked |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s8` |
| Catalog | `mastery-catalog/gc1-s8` |
| Verb | existing `COMMIT` · operation `REPAIR` |
| Parameter | `extent=standard` (default) or `extent=overhaul` |
| Human | `repair <target>` · `repair <target> overhaul` |
| Who may overhaul | S1-recognized Engineer and **MAINTAINED** (not LATENT) |
| Overhaul extra energy | +1 (on top of ordinary REPAIR) |
| Overhaul extra condition | +5 (on top of S2 +15/+20), cap 100 |
| Standard REPAIR | Unchanged for every Player |
| New events | none |
| Help | `help repair` names overhaul. WED / ATTEST stay omitted |

---

## Lines (pinned)

On accepted overhaul:

```text
You overhaul {label}.
```

Ordinary repair lines stay as they are. Never print XP or track ids.

On locked overhaul, explain the observable blocker. Do not leak hidden practice counts.

---

## Runtime rule

Hosted inhabit MUST accept structured `COMMIT.REPAIR` with `extent=overhaul` only for a recognized, maintained Engineer who can pay the extra energy. Observation affordances expose that parameter when eligible. Isolated `test.hosted-canonical.gc1-s8`. No Genesis change. Human `repair <target> overhaul` remains Chamber/test tooling (RFC-0120).
