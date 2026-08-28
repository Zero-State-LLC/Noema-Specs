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
