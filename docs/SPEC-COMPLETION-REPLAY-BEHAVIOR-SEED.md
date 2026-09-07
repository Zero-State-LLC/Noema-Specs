# Spec Completion Contract Micro-Note (Replay Behavior) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Replay behavior + deterministic ordering.

**Coverage notes:**
- Replay via ledger + event catalog (RFC-0002, DEEP-TIME, prior).
- Deterministic ordering per existing (e.g., scheduler, cycle fence).
- GC-specific: contest replay, WED pressure replay, culture inheritance replay via seeds.

**Boundaries:** Notes only. Cites GAME-COMPLETENESS-PLAN.md section 11 + prior + main.

Smallest unit for replay/deterministic element.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Replay coverage seam:** Extend the inventory with explicit contest, WED, and derived-culture replay cases identifying their source ledger, snapshot, rules/catalog pin, observation boundary, and expected comparison. Preserve the distinction between replaying world effects and reproducing an agent's stochastic response.
- **Compatibility boundary:** Ordering and equivalence remain owned by REPLAY, WORLD-ENGINE, and the accepted event contracts. New scheduler or comparison semantics need versioned authority; this seed neither supplies them nor weakens existing digest requirements.
- **Validation expectations:** Pair successful rebuilds with reordered/missing-event and undeclared-input failures. Check that WED replay invents no operator injection and culture reconstruction retains source references. A fixture description alone is not replay evidence: link actual results and first-divergence diagnostics without converting unknowns to equivalence.
