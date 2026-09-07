# Spec Completion Contract Micro-Note (Idempotency/Replay) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Idempotency + failure semantics + replay behavior + migration/version behavior + security boundary.

**Coverage notes:**
- Idempotency/replay: Via existing ledger + event catalog (RFC-0002, DEEP-TIME, prior RFCs).
- Failure: Per GC seeds (e.g., COI closed, pressure fail-closed).
- Security: Per FIRST-WORLD-OPERATIONS + operator notes.
- Migration: Versioned via RFCs/seeds.

**Boundaries:** Notes only. Cites GAME-COMPLETENESS-PLAN.md section 11 + prior + main.

Smallest unit for idempotency/replay element.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Traceability can distinguish request retry identity, settlement failure, replay input ordering, and migration lineage rather than treating them as one ledger guarantee. Name the owning action, receipt, and recovery/version contract for each GC example.

- This inventory introduces neither a new idempotency key nor a second provenance scheme. Any change to key scope, failure charging, canonicalization, or recovery boundaries requires the owning accepted contract and version/migration review; prior evidence keeps its recorded pins.

- Prospective proof should compare first acceptance with same-request retry, rejected requests, interrupted settlement, and replay after restart. Check one durable effect and debit, retained failure reason, and equivalent state under the declared boundary; an inventory reference alone is not executable replay evidence.
