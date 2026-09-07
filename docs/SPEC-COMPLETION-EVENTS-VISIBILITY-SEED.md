# Spec Completion Contract Micro-Note (Events/Visibility) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Events + visibility + partial-observability behavior.

**Coverage notes:**
- Events: Via event catalog (0.1/0.2) + RFC-0002 + GC seeds (e.g., CRIME_DETECTED, ENTITY_UPDATE, WED pressure).
- Visibility: Per GC authorities (public bands, private, operator-only, research redaction).
- Partial-observability: Inherent in GC5/GC6 (latency, mystery, discovery states) + new couplings.

**GC examples:** GC7 crime events have visibility reconciliation (B7a); GC10 pressure events have preview/audit.

**Boundaries:** Notes only. Cites GAME-COMPLETENESS-PLAN.md section 11 + event catalog + prior seeds + main.

Smallest unit for events/visibility element.

## Extension Points

Non-normative future guidance; the existing authorities and frozen behavior remain unchanged.

This input note can accumulate event-to-audience examples connecting GC7 crime reconciliation and GC10 pressure audit to their existing owners. Preserve catalog 0.1/0.2, current redaction and the inputs-only status: an example is not permission to publish an event. Promote an exposure or event change only through the owning GC contract and explicit catalog/RFC decision. Validate each proposed example against an allowed viewer and a denied viewer, including research/operator separation, before claiming completion.
