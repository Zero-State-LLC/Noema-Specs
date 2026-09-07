# RFC-PROPOSAL: GC7 Crime Payload Victim ID / Visibility Reconciliation (B7a)

**Status:** Superseded by [RFC-0129](RFC-0129-crime-detected-payload-reconciliation.md), which specifies the first of the two exits framed below. Retained for its framing, boundaries, and citations. Do not treat this note and RFC-0129 as two live proposals for `B7a`.

**Original status:** Minimal draft proposal. Derived from design note. Inputs only until accepted.

**Parent gap:** SPEC-GAP-REGISTER-2026-08-25 B7a (`CLOSED_BY_RFC` by RFC-0129). This note stays superseded.

**Source design note:** [GC7-CRIME-PAYLOAD-VICTIM-SEED.md](../docs/GC7-CRIME-PAYLOAD-VICTIM-SEED.md)

**Proposed change (bounded):**
- Reconcile the three Accepted definitions of "public" for `CRIME_DETECTED` into one canonical form (e.g., `PUBLIC_HISTORY` + derived victim).
- Amend `event-catalog/0.2` payload (in the style of RFC-0127) to declare consistent `victim_id` / `visibility` fields, or derive them from separate history and remove from detection payload.
- Keep `CRIME_DETECTED` semantics strictly detection-only (no automatic sanction).
- GC3 social memory and WATCH consume only the reconciled public form.

**Scope boundaries (per seed + doctrine):**
- Targets the schema vs. authority contradiction in payload/envelope.
- One narrow amendment RFC or clarification (no new event types).
- Research input only. Ties to GC3 seeds and prior B7 work.
- No aggregation of reports; per-incident, first-hand preference preserved.

**Citations:**
- SPEC-GAP-REGISTER-2026-08-25.md (B7a)
- GC7-CRIME-PAYLOAD-VICTIM-SEED.md
- GC3-S1-BETRAYAL.md, GC3-S2-WATCH-PUBLIC.md, RFC-0094, EVENT-CATALOG-AUDIT.md, event-types.0.2.json, world-event.schema.json
- RESEARCH-ASSIMILATION-2026-08-25-CRIME.md
- STRATEGIC-CONFLICT.md, GAME-COMPLETENESS-PLAN.md (GC7)
- PR #305 + main 2026-08 continuation (design notes pass)

**Readiness:** Smallest viable unit from the seed for payload reconciliation. Ready for review/acceptance as narrow RFC. Ties cleanly to other B7 seeds.

**Next smallest if accepted:** Amend catalog 0.2 + reconcile GC3/WATCH consumption.
