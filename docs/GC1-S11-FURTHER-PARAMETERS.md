# GC1-S11 — Further parameters (BUILD / TRADE / INSPECT)

**Status:** Design note / next slice authority extension. Not yet shipped. Builds on research assimilation 2026-08-27.  
**Depends on:** [GC1-S8-PARAMETER-ACCESS.md](GC1-S8-PARAMETER-ACCESS.md) · [GC1-S9-MULTI-FOCUS.md](GC1-S9-MULTI-FOCUS.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) · [CONSTRUCTION.md](CONSTRUCTION.md) (for BUILD)  
**RFC:** See [RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md](../rfcs/RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md) (draft)  
**Does not open:** new verbs · `event-catalog/0.3` · class discounts · WED / ATTEST help

S11 extends parameter access to additional operations on focused tracks (BUILD, TRADE, INSPECT families) for recognized MAINTAINED specialists. Same-verb richer parameters only. Incorporates autonomous skill mastery signals for trajectory-informed selection of when to apply advanced parameters.

---

## Doctrine decisions

| Temptation                            | Verdict |
|---------------------------------------|---------|
| Parameter access on focused tracks    | **ACCEPT.** Mastery incentive. |
| New verbs or discounts                | **REJECT.** Same verbs, no class bonuses. |
| Unrestricted parameter access         | **REJECT.** Requires recognized + MAINTAINED + focus credit. |
| BUILD-only or TRADE-only this slice   | **REJECT.** Bounded set across families. |

---

## Slice contract

| Field                  | Value |
|------------------------|-------|
| Slice id               | `gc1-s11` |
| Catalog                | `mastery-catalog/gc1-s11` |
| Verbs                  | existing (BUILD + ops, TRADE, INSPECT) |
| Who may use advanced   | S1-recognized + MAINTAINED on a track in active focus set |
| Parameters             | Versioned richer options (e.g. BUILD extent, TRADE caution bypass, INSPECT depth) |
| Standard behavior      | Unchanged for all Players |
| New events             | none |
| Help                   | Updated for focused specialists |

---

## Evidence model (research-informed)

- Advanced parameters available when the relevant track is actively focused (S9) and the Player is MAINTAINED (S3).
- Autonomous management: Trajectory review and skill graphs allow Player to focus the right track before high-stakes BUILD/TRADE/INSPECT actions to unlock parameters.
- No mechanical "level" — purely evidence + focus state.

---

## Lines (pinned)

No new public lines. Effects appear through richer outcomes under existing verbs when conditions met.

---

## Runtime rule

When conditions met (recognized + MAINTAINED + focused track):
- Additional parameter options exposed on the relevant verbs.
- All budgets, authorization, and observability rules unchanged.
- Isolated test: `test.hosted-canonical.gc1-s11`.

---

## Citations / provenance

- Parent: [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) (research section + S8/S9).
- Research input: SkillMaster signals (autonomous skill selection for parameter use) via 2026-08-27 assimilation and seed.
- Prior: S8 (RFC-0112), CONSTRUCTION.md.
- GAME-COMPLETENESS-PLAN GC1 (research seeds).

Design note only. Completes the listed remaining parameter items for GC1. All proposals pass doctrine A–J. No new verbs.