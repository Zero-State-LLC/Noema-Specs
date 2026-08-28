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
- GC1 B1b multi-focus/parameter magnitudes (covered by S9–S11)

**Seeds added on main (covering open SPEC gaps from REGISTER-2026-08-25):**
- GC1-FAILED-ATTEMPTS-SEED.md (B1a)
- GC1-MULTI-FOCUS-MAGNITUDES-SEED.md (B1b)
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

This continuation seeds the primary remaining open SPEC gaps for the GC campaign (B1–B10 series). All core open/partial B-gaps now covered by design notes. Deferred items (B8b, B9b, etc.) remain as-is per doctrine.

Ready for review on #305 + follow-up for main increments. Let me know next (e.g., GC5/GC6 residuals if any, or RFC drafting).
**Non-GC residuals (PAM1/PAM2):** Quick design notes added for completeness (adapter ambiguity and self-join). See PAM1-ORG-ID-SEED.md and PAM2-ORG-SELF-JOIN-SEED.md. Deferred per register unless onboarding evidence requires action.

**GC5/GC6 post-2026-08 review (as recommended follow-up):**
GC5 Communication Ecology: Authority + S0–S8 pinned (RFC-0009 relay bands + RFC-0021/0028/0054/0062–0066). B5 CLOSED_BY_RFC per SPEC-GAP-REGISTER-2026-08-25. No new residuals or B-gaps requiring design notes in this pass. Composes existing MESSAGE surfaces + infrastructure.
GC6 Systemic Discovery: Authority + S0/S1 pinned (RFC-0010 archive-vs-live INSPECT + RFC-0024 reconstruction). B6 RUNTIME_ONLY per register (composes Deep Time / evidence / EXPLORATION; no quest/oracle). No new seeds needed. Mysteries originate from existing pressures (decay, WED, communication failure, player action).

Reviewed against 2026-08-25 register, COMMUNICATION-ECOLOGY.md, SYSTEMIC-DISCOVERY.md, first slices, and higher S-slices. Stable at pinned S0 + specified later slices. No action in this continuation.

Cites: SPEC-GAP-REGISTER-2026-08-25.md (B5 CLOSED_BY_RFC, B6 RUNTIME_ONLY), GAME-COMPLETENESS-PLAN.md GC5/GC6 sections.


**GC5/GC6 review complete (2026-08 follow-up):**  
No residuals requiring new design notes. GC5 stable (S0–S8 pinned to RFCs; B5 CLOSED_BY_RFC). GC6 stable (S0/S1 pinned; B6 RUNTIME_ONLY). Composes existing surfaces/evidence. Reviewed per recommendation after B-gap seeding.

Next: RFC drafting from any of the B-gap seeds (e.g., GC1-FAILED-ATTEMPTS-SEED.md or GC7 crime seeds) if desired.

Cites: SPEC-GAP-REGISTER-2026-08-25.md, updated GAME-COMPLETENESS-PLAN.md + SPEC-CHECKLIST.md.

**RFC draft started (as next after GC5/GC6 review):** Minimal RFC-PROPOSAL-GC1-FAILED-ATTEMPTS-WEIGHTS.md created from GC1-FAILED-ATTEMPTS-SEED.md (B1a). Bounded proposal only; no contracts changed.

Cites: the seed + register B1a.

**Additional RFC draft:** Minimal RFC-PROPOSAL-GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION.md created from GC7-CRIME-PAYLOAD-VICTIM-SEED.md (B7a). Reconciles victim_id / visibility and "public" definitions for CRIME_DETECTED. Bounded catalog 0.2 amendment style.

Cites: the seed + register B7a + GC3 authorities.

**Additional RFC draft:** Minimal RFC-PROPOSAL-GC7-CRIME-EVIDENCE-ALGORITHM.md created from GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md (B7b). Defines seeded/replayable evidence function for detection (constants as inputs, deterministic).

Cites: the seed + register B7b.

**Additional RFC draft:** Minimal RFC-PROPOSAL-GC8-LOT-GRADE-RESIDUALS.md created from GC8-LOT-GRADE-SEED.md (B8a). Bounded lot-grade attributes with provenance/visibility after quality slices.

Cites: the seed + register B8a.

**Additional RFC draft:** Minimal RFC-PROPOSAL-GC9-THRESHOLD-TRANSMISSION.md created from GC9-THRESHOLD-SEED.md (B9a). Evidence-backed thresholds and transmission for tradition (N repeated REPAIR → inherited CUSTOM). No scores or meters.

Cites: the seed + register B9a.
