# RFC-PROPOSAL: GC7 Crime Detection vs Sanction Separation (B7c)

**Status:** Minimal draft proposal. Bounded. Design/research only. No contract, catalog, verb, or exposure change.

**Parent gap:** SPEC-GAP-REGISTER-2026-08-25 B7c (OPEN_SPEC in GC7 crime).

**Source:** GC7-CRIME-DETECTION-SANCTION-SEED.md + RFC-0002

**Proposed:**
- `CRIME_DETECTED` (or equivalent evidence record) carries only detection facts: source events, witnesses, condition, timestamp, actor, location, per-incident first-hand evidence.
- Sanction application (influence debit, exclusion, etc.) is a separate, governed follow-on step (via contest resolution, institutional action, or dedicated mechanism if RFC'd later).
- Detection payload must not require `influence_delta` / sanction fields (aligns with RFC-0002 phrasing: "Detection occurred (not automatic guilt broadcast)").
- Ties to GC3 (public descriptors from detections only; restitution trades victim-specific per SOCIAL-MEMORY.md).
- Enforcement cost/jurisdiction (B7d) applies only at sanction step.

**Scope / Boundaries:** Extends RFC-0002 detection intent and STRATEGIC-CONFLICT.md. No new verbs. No aggregation of weak reports. Aligns with "not automatic guilt". Research input only. Smallest viable unit for B7c.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B7c), GC7-CRIME-DETECTION-SANCTION-SEED.md, RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, RFC-0002, GC3-S1-BETRAYAL.md / GC3-S2-WATCH-PUBLIC.md, GC7-CRIME-ENFORCEMENT-SEED.md, GAME-COMPLETENESS-PLAN.md (GC7), PR #305.

**Readiness:** Smallest unit. Ready for review to clarify honest detection semantics before full crime producer.

---
**Verification note:** Draft only; does not mutate specs.
