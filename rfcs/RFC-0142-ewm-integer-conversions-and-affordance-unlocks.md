# RFC-0142: Integer EWM Infrastructure Synthesis (`COMMIT.CONVERT`), Affordance Unlock Provenance, and Belief-Boundary Cleanup

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).

## Problem

[ECONOMY-EWM-SPEC.md](../docs/ECONOMY-EWM-SPEC.md) documents three declared-but-inert stubs (`conversion_rate`, `unlocked_affordances`, and `BeliefState`), while runtime `construction.ts` retains unused floating-point stubs (`P3_RESOURCE_PRODUCTION`, `P3_CONVERSIONS`) that conflict with [RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md) non-negative integer accounting, and `types.ts` declares a server-side `BeliefState` interface that conflicts with `CONTEXT.md` ("World state MUST NOT depend on an agent's belief").

## Decisions

### 1. Deterministic Integer Infrastructure Synthesis (`COMMIT.CONVERT`)

1. Remove floating-point `P3_RESOURCE_PRODUCTION` and `P3_CONVERSIONS` stubs from runtime `construction.ts`.
2. Define `COMMIT` `operation: "CONVERT"` (`cmd: "convert <power|compute>"`), available when co-located with an operational (`!in_progress`, `condition >= 50`, `!scar`) infrastructure entity of the matching class:
   - **`mode: "power"` (requires `generator` in room):**
     - Cost: `2 SILICA_CELL` cargo (or `3` untyped/`SALVAGE_COMPOSITE` cargo) + `{ compute: 1 }`.
     - Grant: `energy_gain = 6 + min(4, floor(room_protocol_strength / 3))` (`6..10` integer `energy`, clamped at `80`; refused with `BUDGET_EXCEEDED` if actor already has `energy >= 80`).
     - Infrastructure wear: `generator.condition = max(25, condition - 1)` via `ENTITY_UPDATE` (`operation: "CONVERT"`).
   - **`mode: "compute"` (requires `archive_annex` in room):**
     - Cost: `2 SILICA_CELL` cargo + `{ energy: 1 }`.
     - Grant: `compute_gain = 5 + min(3, floor(room_protocol_strength / 3))` (`5..8` integer `compute`, clamped at `64`; refused if `compute >= 64`).
     - Infrastructure wear: `archive_annex.condition = max(25, condition - 1)` via `ENTITY_UPDATE` (`operation: "CONVERT"`).
3. Emits `BUDGET_CONSUMED`, `RESOURCE_TRANSFER` (from entity/conversion sink to `player_id`), and `ENTITY_UPDATE` within `event-catalog/0.2`.

### 2. Deterministic `Observation.unlocked_affordances`

Populate `Observation.unlocked_affordances?: Array<{ operation: string; unlocked_by: string }>` whenever a dynamic affordance is unlocked by a non-baseline capability:
- Equipped items ([RFC-0139](RFC-0139-regional-lots-and-portable-items.md)): e.g., `{ operation: "INVESTIGATE", unlocked_by: "item:chrono_lens" }`.
- Maintained mastery ([MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md)): e.g., `{ operation: "REPAIR:overhaul", unlocked_by: "mastery:engineer" }`.
- Occupied office ([RFC-0133](RFC-0133-quartermaster-treasury-services.md), [RFC-0140](RFC-0140-storefronts-barter-and-supersession.md)): e.g., `{ operation: "SUPPLY", unlocked_by: "office:OPERATE_RESOURCE_ACCOUNT" }`.
- Room infrastructure: e.g., `{ operation: "CRAFT", unlocked_by: "infra:workshop" }`, `{ operation: "RECHARGE", unlocked_by: "infra:generator" }`, `{ operation: "CONVERT", unlocked_by: "infra:generator" }`.

### 3. `BeliefState` Constitutional Cleanup

Remove the unused server-side `BeliefState` interface from Worker runtime types. Agent expectations, counterparty reliability priors, and tactical knobs belong exclusively to Controller-local memory (`ADR-0002`, [RFC-0141](RFC-0141-orin-system-fleet-and-client-v02-contracts.md)) and MUST NEVER enter canonical `WorldState` or gate server preconditions.

## Rollback

Disable `CONVERT` affordance advertising and omit optional `unlocked_affordances` from observations. No ledger migration required.
