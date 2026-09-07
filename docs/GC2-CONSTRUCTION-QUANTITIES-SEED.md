# GC2 Construction Quantities and Material Tables — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [CONSTRUCTION.md](CONSTRUCTION.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC2) · GC2-FIRST-SLICE.md

**Gap (SPEC-GAP-REGISTER-2026-08-25 B2a):** Generalized BUILD material quantity tables are not first-world free-form authority.

**Proposed framing (for future RFC):**
- First-world generalized construction uses closed, versioned quantity tables per operation + class (not free-form or player-chosen).
- Tables live in the construction catalog (versioned).
- Existing S0 pins remain (v0.1 classes).
- Ties to resource economy, budgets, and Deep Time attribution of built structure.

**Boundaries:** Extends CONSTRUCTION authority. No runtime free-form generation. Research input only. S0 unchanged.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B2a), CONSTRUCTION.md, GC2-FIRST-SLICE.md, PR #305 + main continuation.

Smallest unit for GC2 material tables gap. Ready for RFC.

## Extension Points

Non-normative extension guidance; this section does not change accepted behavior or prove runtime completion.

- Extend proposed material-table examples by existing operation and constructible class, recording resource units and the source catalog pin. Quantities remain closed, versioned entries rather than Player-selected recipes or free-form generation.

- Preserve current S0 quantities, budgets and accepted construction behavior. This seed remains research input and does not activate a generalized materials system, create a new verb or authorize runtime changes.

- A future table proposal needs the narrow governing RFC, explicit mapping from old entries and compatibility analysis for retained examples. New versions must not silently reinterpret historical construction costs or resource attribution.

- Validate representative operation/class lookups, absent entries, invalid quantities and insufficient budgets against the proposed schema and existing pins. Require explicit rejection or unresolved status rather than defaulting a missing material cost to zero.
