# Economy EWM Spec — Perihelion Reach (Draft v0.1)

**Source:** economy-evm-assimilation-plan.md + P0-P4 execution (2026-08)  
**Status:** **Pinned to shipped v0.1 (2026-08-23).** See *Pinned scope* below for what ships and what is deferred. Formalising any deferred item requires a new RFC.  
**See also:** SEMANTIC-EVOLUTION-SPEC.md (v0.1 extension)

## Pinned scope — shipped v0.1 (2026-08-23)

This document is **pinned to what ships**. Everything below the line is live on
`world.perihelion-reach-3`; everything in the deferred table is declared somewhere but
inert, and none of it may be treated as behaviour a reader can rely on.

### Shipped and live

| Mechanism | Where |
|---|---|
| ASP signals (`@C` / `@G` / `@S`), grounding gates, hearsay quarantine | `src/signal.ts` |
| `protocol_strength` under harvest pressure; compositionality | `src/reputation.ts` |
| `harvest_pressure` / `regen_mod` | `src/reputation.ts`, `src/deep-time.ts` |
| Privileged `image_score` / `second_order` — never a WATCH public scalar (GC3-S0) | `src/reputation.ts` |
| Bounded upward norm ratchet — cap 5, decay 1 per slow pass after 10 quiet cycles, floor 0 | [RFC-0123](../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md) |
| Costly TRADE-reject — 1 influence, image −2, conduct −1; no `harvest_pressure` coupling | [RFC-0123](../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md) |
| Forman–Ricci `cascading_risk` weighted by degrading grounding | `src/curvature.ts` |

### Deferred — declared but inert, not behaviour

None of these is implemented. Each is named here because the prose above once read as
though they were, and a reader could reasonably have believed it.

| Deferred | Actual state in the runtime |
|---|---|
| `conversion_rate` | A Genesis seed value only (`initial_beliefs`). Nothing reads or updates it |
| `unlocked_affordances` | A field on a type (`types.ts`). Never populated, never emitted |
| `BeliefState` / per-agent beliefs | An interface only. Never instantiated; `reputation.ts` records that beliefs and styles await G3 |
| Wasserstein / Ollivier curvature | Forman–Ricci is the shipped metric. Specs forbid Wasserstein Ollivier as product default |
| Live cultural generation | No generator exists. Culture is derived from ledgered practice (GC9-S0/S1/S2) |

**Locking any of those numbers requires a new RFC.** Pinning them here would make a
promise the runtime does not keep — which is the failure this pin exists to end.

## 1. Agent Layer (P3)
- Heterogeneous roles (salvager, trader, archivist, maintainer, generalist).
- Per-agent `BeliefState`: expected_regen, conversion_rate, org_threshold, counterparty_reliability.
- Policy adaptation: action choice driven by role + current beliefs.
- Production functions: role × action → resource deltas (e.g. salvager.HARVEST: +1.8 materials, +0.3 influence).

## 2. Environment + Resource Model (P3-04)
- Resources: attention (flow), compute, energy, influence, storage, materials (stocked).
- Production: explicit functions per role/action.
- Conversion table (unlocked/endogenous):
  - materials → compute (rate ~0.6)
  - materials → energy (rate ~0.7)
  - compute → influence (rate ~0.4)
- Decay: idle budgets decay at configurable rate (0.05/cycle default).
- Stock entities: max_stock, regen_rate, current stock_amount (activity + time regen + co-evo pressure).

## 3. Co-evolution (P1 + P3)
- `coevolveAfterAction`: pressure → regen_mod, genesis_evolutions.
- Belief revision + institutional drift from aggregate play.

## 4. Endogenous Institutions (P3-03)
- ORG/ATTEST success mutates:
  - org_influence_threshold (downward ratchet)
  - conversion rates
  - spawns new affordances (e.g. "salvage_to_influence")
- Charters/rules can evolve via contest/attest (future: proposal effects).

## 5. Counterfactual + SAR (P2)
- Checkpoint: snapshot of stocks, budgets, co_evo, genesis_evos.
- Resume-with-intervention: apply param patches (regen_x, max_x, threshold).
- SAR loop: goal → sim (with co-evo + economy) → KPIs → propose patch → re-validate.

## 6. Observation / Affordance
- Enriched with: co_evolution, genesis_evolutions, unlocked_affordances.
- Affordances respect current budgets/stock/beliefs/role.

## 7. Metrics (Verification)
- Stock velocity, influence production rate, org formation, attention health, affordance hit rate, belief convergence, concentration index.

## Implementation Notes
- Harness (sar-skeleton.py): full P0-P4 prototype with verifiable runs.
- Worker stubs: BeliefState, AgentRole, ProductionFunction, ConversionRule, ResourceEconomyState (types.ts).
- EWM_ENHANCED genesis profile with tuned params.

**P4 Deliverable Target:** This doc + Noema-Specs pin + client exposure.

## 8. Client Parity (P4)
- Observation now carries co_evolution, beliefs, unlocked_affordances, resource_economy.
- Harness SAR demos full round-trip.

## 9. Production Cutover (P4-04)
- Enhanced genesis variant: `EWM_ENHANCED` profile.
- See `plans/perihelion-evm-cutover.md` and `RUNTIME_CUTOVER_RUNBOOK.md`.

## 10. Semantic Evolution Extension (v0.1+)
This base EWM spec is extended by `SEMANTIC-EVOLUTION-SPEC.md`, which adds:
- Signaling Layer (ASP-style @C/@G/@S/assumptions)
- Drift metrics (ASI composite)
- Reputation & cultural norms
- Semantic-geometric risk
- Ontological grounding

All new semantic mechanics are designed to compose with the above EWM layers without breaking existing contracts.