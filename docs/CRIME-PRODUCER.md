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

## Extension Points

Non-normative producer-design guidance. The historical PARTIAL/design-note status above is not a claim of a live producer.

### Detection-to-consumer seam

Extend witness, sensor, investigation, and self-report scenarios as evidence-origin cases, keeping incident time, later detection, and any separately authorized sanction distinguishable. Specify provenance and deterministic ordering before choosing a detection algorithm; research hotspot models do not establish guilt or a mandatory penalty.

### Retained pins and compatibility

[Accepted RFC-0129](../rfcs/RFC-0129-crime-detected-payload-reconciliation.md) now permits optional `victim_id` and `visibility` on the existing `CRIME_DETECTED` payload. `visibility` has no default; absence is not public. `PUBLIC_HISTORY` and `visibility: PUBLIC` travel together. A missing victim supplies no named-victim dyadic edge. This reconciles the payload, not the producer, detection algorithm, or unresolved enforcement policy. Preserve RFC-0002's detection-not-automatic-guilt boundary, existing sanction pins, closed catalog versions, and no new verbs or Genesis.

### Promotion and concrete checks

A future producer needs accepted rules and versioned conformance before runtime integration can be claimed. Review fixtures with neither optional field, a named victim, paired public markers, and each invalid one-sided public marker. Feed the same eligible records through GC3 dyadic/public memory and world-report/WATCH gates; require consistent public selection without private incident leakage. Add delayed, duplicate, and reordered detection cases to establish deterministic handling rather than silently double-applying consequences. Record producer execution evidence separately from schema acceptance.
