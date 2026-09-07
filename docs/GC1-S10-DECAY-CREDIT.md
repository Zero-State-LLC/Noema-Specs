# GC1-S10 — Focus decay-window credit

**Status:** Design note / next slice authority extension. Not yet shipped. Builds on research assimilation 2026-08-27.  
**Depends on:** [GC1-S3-DECAY.md](GC1-S3-DECAY.md) · [GC1-S7-FOCUS.md](GC1-S7-FOCUS.md) · [GC1-S9-MULTI-FOCUS.md](GC1-S9-MULTI-FOCUS.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)  
**RFC:** See [RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md](../rfcs/RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION.md) (draft)  
**Does not open:** new events · `event-catalog/0.3` · mechanical benefits or discounts · changes to base S3 rates · WED / ATTEST help

S10 grants decay-window credit to declared focus tracks (active set receives longer idle tolerance before LATENT). Non-focused recognized tracks follow normal S3 decay. This provides incentive for focused practice without class discounts or new verbs. Incorporates autonomous skill signals for trajectory-informed focus management that can affect decay behavior.

---

## Doctrine decisions

| Temptation                          | Verdict |
|-------------------------------------|---------|
| Decay credit only for active focus  | **ACCEPT.** Opportunity cost of focus. |
| Change base S3 decay rates          | **REJECT.** S3 magnitudes stay fixed. |
| New DECAY event or catalog bump     | **REJECT.** This slice. |
| Automatic rehab or recognition boost| **REJECT.** Evidence only. |
| Credit stacks across unlimited tracks| **REJECT.** Cap tied to multi-focus. |
| Public line changes                 | **ACCEPT.** Follows S7/S9 withhold rules. |

---

## Slice contract

| Field                | Value |
|----------------------|-------|
| Slice id             | `gc1-s10` |
| Catalog              | `mastery-catalog/gc1-s10` |
| Verb                 | existing (focus + practice actions) |
| Who receives credit  | Recognized tracks that are in the active focus set (S7/S9) |
| Credit amount        | Versioned (initial: +N idle cycles before LATENT; e.g. +6) |
| Non-focused tracks   | Normal S3 decay (12 idle → LATENT) |
| Rehab                | Normal (3 qualifying successes) |
| New events           | none |
| Self PLAY            | Focus lines show credit status implicitly via maintenance |
| Public PLAY / WATCH  | Same as S7/S9 |
| Help                 | FOCUS / decay help updated for credit on focused tracks |

---

## Evidence model (research-informed)

- Only active focus tracks (per S9) receive the decay-window credit.
- Autonomous management (SkillMaster-style trajectory review): Player can strategically focus tracks with high recent evidence to protect them from decay, or rotate focus for balanced maintenance.
- Skill-graph composition: Complementary tracks in active set can share or extend effective maintenance windows through joint practice.
- No change to recognition evidence or base S3 mechanics for non-focused tracks.

---

## Lines (pinned)

No new public lines. Focus lines remain as S7/S9. Decay credit is observable via longer maintenance of the focused track.

---

## Runtime rule

When a track is in the active focus set:
- Idle tolerance before LATENT is increased by the credit amount (versioned).
- All other decay/rehab rules (S3) unchanged.
- Credit does not apply if the track is not focused.
- Isolated test: `test.hosted-canonical.gc1-s10`.

---

## Citations / provenance

- Parent: [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) (research assimilation 2026-08-27 + S3/S7/S9).
- Research input: [MASTERY-SPECIALIZATION-RESEARCH-SEED.md](MASTERY-SPECIALIZATION-RESEARCH-SEED.md) + [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md) (SkillMaster autonomous mastery, trajectory-informed management, multi-track handling).
- Prior: GC1-S3-DECAY (RFC-0043), S7 (RFC-0110), S9.
- GAME-COMPLETENESS-PLAN GC1 (research seeds 2026-08-27).

Design note only. Moves decay-window credit from "Still open" once a full RFC is Accepted. No new verbs. All proposals must still pass complexity doctrine A–J.