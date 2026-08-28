# GC7 Crime Payload and Victim Id Reconciliation — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7) · [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md)

**Gap (SPEC-GAP-REGISTER-2026-08-25 B7a):** Three Accepted authorities reference `victim_id` / `visibility` on `CRIME_DETECTED`; the payload and envelope do not declare them. GC3-S2 and RFC-0094 also define "public" differently for the same event.

**Research inputs (2026-08-25 + prior):**
- Per-incident, first-hand evidence.
- Incomplete reputation information behaves differently for missed observation vs. bad assessment.
- No aggregation of weak reports into severe sanction.
- Public descriptors must be consistent.

**Proposed design framing (for future RFC):**
- Reconcile the three definitions of "public" for crime events into one canonical representation (e.g. `PUBLIC_HISTORY` + derived victim).
- Amend `event-catalog/0.2` payload (in the style of RFC-0127) to include consistent victim_id / visibility fields, or remove the requirement from detection payload and derive via separate history.
- Keep detection semantics clean (no automatic sanction).
- GC3 social memory consumes the reconciled public form only.

**Boundaries:** Targets the schema vs. authority contradiction. One amendment RFC or clarification. Research input only. Ties to GC3 and prior B7 seeds.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B7a), GC3-S1-BETRAYAL.md, GC3-S2-WATCH-PUBLIC.md, RFC-0094, EVENT-CATALOG-AUDIT.md, event-types.0.2.json, RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, PR #305 + main continuation.

Smallest unit for payload reconciliation in GC7 crime work. Ready for RFC.