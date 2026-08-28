# GC7 Crime Detection vs Sanction Separation — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7) · [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md)

**Gap (SPEC-GAP-REGISTER-2026-08-25 B7c):** RFC-0002 calls `CRIME_DETECTED` "Detection occurred (not automatic guilt broadcast)" yet the payload requires `influence_delta` / `influence_applied`. Detection and sanction are conflated.

**Research inputs (2026-08-25 + prior):**
- Detection should be evidence-path dependent.
- Unauthorized act ≠ detected crime.
- Sanction should be separate, governed step (not automatic on detection).
- Costly punishment under low detectability: punish only the definitively identified.

**Proposed design framing (for future RFC):**
- Split semantics: `CRIME_DETECTED` (or equivalent evidence record) carries only detection facts (source events, witnesses, condition, timestamp, actor, location).
- Separate sanction application (influence debit, exclusion, etc.) as a governed follow-on (via contest, institutional action, or dedicated sanction event if RFC'd).
- Payload for detection must not require influence fields.
- Ties to GC3 (public descriptors from detections only; restitution trades are victim-specific).
- Enforcement cost/jurisdiction (see GC7-CRIME-ENFORCEMENT-SEED.md) applies only at sanction step.

**Boundaries:** Extends RFC-0002 detection intent. No new verbs here. Aligns with "not automatic guilt". Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B7c), RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, GC3-S1-BETRAYAL.md, RFC-0002, GC7-CRIME-ENFORCEMENT-SEED.md, PR #305.

Smallest unit for clarifying detection semantics in GC7 crime producer work. Ready for RFC when needed.