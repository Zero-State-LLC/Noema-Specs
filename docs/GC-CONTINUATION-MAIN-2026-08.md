# GC Continuation on Main (post-PR #305)

**Branch/PR:** feat/gc-campaign-pass-2026-08 → PR #305 (pushed)

**Main continuation commits (after switch + pull):**
- 2026-08-25 crime assimilation integration into STRATEGIC-CONFLICT
- GC4 cross-ref + GC4-CRIME-EXPULSION-SEED.md
- GC7 B7d enforcement seed
- GC7 B7b/B7c (algorithm + detection/sanction)
- GC7 B7a (payload/victim_id)
- GC2 B2a quantities + B2b owner/steward
- GC8 B8a lot-grade
- GC9 B9a threshold/transmission
- GC10 B10a/b WED classes + scars
- GC4 B4 broader COI
- GC1 B1a failed-but-legal practice attempts

**Seeds added on main (covering open SPEC gaps from REGISTER-2026-08-25):**
- GC1-FAILED-ATTEMPTS-SEED.md (B1a)
- GC2-CONSTRUCTION-QUANTITIES-SEED.md (B2a)
- GC2-OWNER-STEWARD-SEED.md (B2b)
- GC4-BROADER-COI-SEED.md (B4)
- GC4-CRIME-EXPULSION-SEED.md
- GC7-CRIME-ENFORCEMENT-SEED.md (B7d)
- GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md (B7b)
- GC7-CRIME-DETECTION-SANCTION-SEED.md (B7c)
- GC7-CRIME-PAYLOAD-VICTIM-SEED.md (B7a)
- GC8-LOT-GRADE-SEED.md (B8a)
- GC9-THRESHOLD-SEED.md (B9a)
- GC10-WED-CLASS-SEED.md (B10a/B10b)

All design notes only. Updates to GAME-COMPLETENESS-PLAN.md and SPEC-CHECKLIST.md.

Cites: SPEC-GAP-REGISTER-2026-08-25.md, RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, PR #305 batch.

`git diff --check` clean on increments.

This continuation seeds the primary remaining open SPEC gaps for the GC campaign (B1–B10 series). Deferred items (B8b, B9b, etc.) remain as-is per doctrine.

Ready for review on #305 + follow-up for main increments. Let me know next (e.g., GC5/GC6 residuals if any, or RFC drafting).