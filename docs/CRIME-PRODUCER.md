# Crime Producer Mechanics (RFC-0002 Completion) — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parent authorities:**
- [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) (Accepted) — defines `CRIME_DETECTED` as detection (not automatic guilt).
- [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)
- [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7)
- [CRIME-PRODUCER-RESEARCH-SEED.md](CRIME-PRODUCER-RESEARCH-SEED.md)
- [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md)

**Gap:** Producer side for generating `CRIME_DETECTED` (witness, sensor ≥50, investigation, self-report, delays, graduated effects). Currently PARTIAL.

**Research inputs (2026-08-27):**
- Crime hotspot dynamics (arXiv:2605.17709v1): delayed feedback leads to oscillations; timely data > density for stabilization.
- Cops and Robbers synthesis (arXiv:2503.11475): formal angles for pursuit/evasion.

**Proposed design framing (for future RFC):**
- Witness/sensor/investigation/self-report flows feeding `CRIME_DETECTED`.
- Delayed revelation consistent with hotspot models.
- Public descriptors feed SOCIAL-MEMORY and WATCH (coarse bands only).
- No new events. Reuses existing catalog + contest/social memory.
- Ties to GC3 relational reputation (public crime as edge signal).

**Boundaries:** Extends STRATEGIC-CONFLICT authority. Complexity doctrine. Partial observability. No new verbs/catalog.

**Citations:** As above + assimilation crime section.

This completes the producer framing as design note alongside the bounded extension in STRATEGIC-CONFLICT.md. Ready for RFC when operator directs.