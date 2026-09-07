# GC1-S9 — Multi-focus

**Status:** Design note / next slice authority extension. Not yet shipped. Builds on research assimilation 2026-08-27.  
**Depends on:** [GC1-S7-FOCUS.md](GC1-S7-FOCUS.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)  
**RFC:** See [RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md](../rfcs/RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md) (draft)  
**Does not open:** new events · `event-catalog/0.3` · mechanical benefits or discounts · recognition changes · WED / ATTEST help

S9 extends focus to a bounded active set (recommended cap 1–3). A Player may maintain multiple recognized tracks with maintenance credit on the active set; non-active tracks decay faster. It remains soft intent and practice evidence only. No class lock. Incorporates autonomous skill management signals (trajectory review, compositional graphs) from research without leaking research metrics into PLAY.

---

## Doctrine decisions

| Temptation                        | Verdict |
|-----------------------------------|---------|
| Hard cap 1–3 on active focus      | **ACCEPT.** Opportunity cost + maintenance. |
| New `FOCUS` event or catalog bump | **REJECT.** This slice. |
| Automatic recognition or benefits | **REJECT.** Evidence only. |
| Change base decay rates           | **REJECT.** S3 magnitudes stay. |
| One optimal super-track           | **REJECT.** Complementary interdependence required. |
| Public lines for all active       | **ACCEPT.** Same rules as S7 (LATENT/hidden withhold). |

---

## Slice contract

| Field                | Value |
|----------------------|-------|
| Slice id             | `gc1-s9` |
| Catalog              | `mastery-catalog/gc1-s9` |
| Verb                 | existing `COMMIT` · operation `FOCUS` (or extension of S7 affordance) |
| Human                | `focus <track>[,<track2>]` (bounded) · `focus clear <track>` |
| Active cap           | Versioned (initial 1–3); maintenance credit on active set |
| Recognition required | For any track to receive credit |
| New events           | none |
| Self PLAY            | List of active focus lines; coarse standing on each |
| Public PLAY / WATCH  | Third-person lines for active tracks in public rooms only; omit if LATENT or hidden room |
| Hidden rooms         | No public focus lines |
| Help                 | FOCUS help updated for multi; no WED / ATTEST |

---

## Evidence model (research-informed)

- A declared focus track receives maintenance credit only while in the active set.
- Non-active recognized tracks decay toward LATENT on the normal S3 schedule (or slightly accelerated).
- Autonomous management: Player-internal trajectory review and refinement (informed by SkillMaster-style signals) allows selection/refinement of which tracks to keep active. Evidence comes from world-native practice, not research scores.
- Skill-graph style composition: complementary tracks (e.g. Engineer + Surveyor on the same infrastructure) produce interdependent outcomes (no lone optimal path).

---

## Lines (pinned)

Active focus lines follow S7 format, listed for each active track.

Clear removes specific track(s) from the active set.

Never print XP, totals, or internal track ids.

---

## Runtime rule

Hosted systems persist a bounded active-focus set (cap versioned) on the Player snapshot. Project self lines for active tracks. Project public lines in public rooms/WATCH only for active + not LATENT tracks. Non-active recognized tracks follow normal decay. No change to S3 base rates or recognition evidence.

Isolated test: `test.hosted-canonical.gc1-s9`.

---

## Citations / provenance

- Parent: [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) (research assimilation 2026-08-27 section + Still open items).
- Research input: [MASTERY-SPECIALIZATION-RESEARCH-SEED.md](MASTERY-SPECIALIZATION-RESEARCH-SEED.md) + [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md) (SkillMaster autonomous mastery, skill graphs, multi-track management).
- Prior: GC1-S7-FOCUS.md (RFC-0110), S3 decay (RFC-0043).
- GAME-COMPLETENESS-PLAN GC1 table (research seeds 2026-08-27).

Design note only. Moves multi-focus from "Still open" once a full RFC is Accepted. No new verbs. All proposals must still pass complexity doctrine A–J.