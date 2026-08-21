# Deep Time Mechanics Update — Perihelion Reach (v0.6+ Integration)

**Version:** v0.1 (Draft)  
**Date:** 2026-08-21  
**Status:** Specs-first extension. Integrates into v0.6 Deep Time foundation and EWM/Semantic layers.  
**Source:** semantic-evolution-assimilation-plan.md + arXiv research synthesis (non-Markovian memory, path dependence, agent-based historical reconstruction, long-term cultural transmission).  
**Related:**  
- `docs/DEEP-TIME.md` (core v0.6 foundation)  
- `docs/SEMANTIC-EVOLUTION-SPEC.md` (signaling, drift, norms)  
- `docs/ECONOMY-EWM-SPEC.md` (EWM substrate)  
- arXiv: trajectory-level memory / non-Markovian processes, path dependence in cultural/institutional evolution, agent-based archaeology & reconstruction models, multi-generational transmission.

## 1. Overview & Intent

Deep Time (v0.6) already provides the conceptual ladder (ACTION → PRACTICE → CUSTOM → INSTITUTION → CULTURE) and separation of layers (world state, historical state, evidence/artifacts, agent interpretation, derived lore). It ensures persistent structures survive their creators and shape successors via scars, succession, archaeology, and reconstruction.

This update **integrates recent research** to make Deep Time mechanics concrete, evolvable, and tightly coupled to the existing EWM (dynamic stock/regeneration, co-evolution, beliefs, SAR) and Semantic layers (signaling, drift, reputation/norms).

**Core Research Integrations (as recommended):**
- **Scars as non-Markovian / trajectory-level effects**: Past events create persistent, path-dependent modifications to future transition rates, affordances, and regeneration (inspired by trajectory fluctuation-response theory and non-Markovian jump processes).
- **Evidence & reconstruction as noisy historical trajectories**: ATTEST/EVIDENCE systems treat records as partial observations of past trajectories. Reconstruction (ARCHAEOLOGY) becomes inference over incomplete paths, with confidence and error terms.
- **Path dependence + slow cultural ratchets**: Institutional and norm evolution exhibits lock-in, costly reversal, and multi-generational transmission (extends endogenous institutions + cultural evolution of cooperation).
- **Succession as compressed history + scars**: Succession mechanics carry forward trajectory summaries, accumulated scars, and lore seeds rather than clean resets.
- **Lore/name boundaries as slowly evolving attractors**: Names, boundaries, and interpretations drift on deep timescales, creating persistent "us vs. them" or sacred regions.
- **Multi-timescale co-evolution**: Fast EWM loops (harvest_pressure, stock regen) coexist with slow Deep Time loops (scar accumulation, norm ratchets, lore drift). SAR operates across both.

**Goal:** Make history *mechanically consequential* over long horizons without breaking short-session PLAY or EWM invariants. History shapes future economics, signaling, and institutions endogenously.

## 2. Integration into Existing Systems

### 2.1 EWM Substrate (Economy EWM Spec)
- Extend `BeliefState` (already in P3) with `HistoricalTrajectorySummary` (compressed past actions + outcomes) and `ScarVector` (persistent modifiers per domain: economic, social, territorial).
- `ResourceEconomyState` and stock entities now carry `scar_modifiers` (e.g., a past over-harvest lowers future regen_rate permanently until repaired/reconstructed).
- `co_evolveAfterAction` (P1) gains a slow `deepTimeCoEvolve` phase called on longer cycles or SAR steps. Fast phase handles pressure/regen; slow phase accumulates scars and ratchets norms.
- Checkpoints (P2) now snapshot `scar_vectors` and `trajectory_digests` for causal experiments on historical interventions (e.g., "what if this scar had been reconstructed differently?").

### 2.2 Semantic Layer (Semantic Evolution Spec)
- Signals (@C, @G, @S, assumptions) now attach to *historical claims*. An ATTEST on an old artifact carries grounding relative to current reconstruction confidence.
- Reputation/image scoring extends to "historical reputation" (how ancestors or prior institutions behaved). Second-order reputation now includes lineage.
- Drift metrics (ASI) gain a deep-time component: `historical_drift` (divergence between current beliefs and ledger reality over many cycles).
- Emergent signaling (Foraging Games analog) now includes slow "protocol fossils" — old signaling styles that persist in lore and affect new agents.

### 2.3 Core Deep Time Foundation (DEEP-TIME.md)
- **Scars**: Promoted from conceptual to typed mechanics. A scar is a non-Markovian modifier: `scar(domain, strength, decay_rate, trigger_conditions)`. It alters rates/affordances without being a simple resource delta.
- **Evidence / Artifacts**: `HISTORICAL-EVIDENCE` and `ARCHAEOLOGY` now operate on trajectory fragments. Reconstruction success depends on `evidence_quality` (grounding from signals) + `agent_belief_alignment`.
- **Succession & Inheritance**: `SUCCESSION` events now transfer `scar_vectors`, `trajectory_digests`, and `lore_seeds`. New leaders inherit path-dependent constraints.
- **Lore boundary & Names**: Lore is explicitly a slow attractor. Name changes or boundary shifts are ratcheted by accumulated historical weight (path dependence). Canonical evidence always wins disputes.
- **Institutional Memory**: Extends `INSTITUTIONAL-MEMORY` with trajectory summaries. Institutions "remember" via scars and evidence chains rather than only current state.

### 2.4 Genesis & Living World
- `EWM_ENHANCED` (and future Deep Time profiles) seed initial `scar_seeds`, `historical_attractors`, and `lore_prototypes`.
- Living genesis micro-events (P1) now include deep-time variants: "scar eruption", "lore crystallization", "reconstruction opportunity" triggered by aggregate long-term behavior or SAR proposals.
- Genesis events can create "foundational scars" that bias early co-evolution.

### 2.5 SAR & Alignment
- SAR goals can now target deep-time objectives: "increase reconstruction fidelity of Cycle 0 events", "reduce path-dependence lock-in while preserving useful scars".
- Alignment reports compare current play trajectories against historical baselines, surfacing unwanted drift or desirable persistence.

## 3. Updated Mechanics

### 3.1 Scars (Non-Markovian Trajectory Effects)
- Applied post-action in `world-actions.ts` (extend `applyHarvest`, `applyTrade`, `applyAttest`, etc.).
- Example: Heavy harvesting in a region creates an `economic_scar` that lowers future `regen_rate` *and* raises `harvest_risk` for generations. The scar is a function of the *trajectory* (sequence of prior harvests), not just the final stock.
- Decay/repair: Scars decay slowly via time + deliberate reconstruction actions. Some scars are "fossilized" (permanent until major intervention).
- Visibility: Scars appear in observations with `visibility` (public, institutional, hidden) and `reconstruction_confidence`.

### 3.2 Evidence & Reconstruction
- `ATTEST` on historical entities now produces `EvidenceFragment` objects carrying partial trajectory data + grounding signals.
- `ARCHAEOLOGY` / reconstruction action: Agent proposes a reconstruction; system computes fidelity vs. canonical ledger. Success spawns new affordances or reduces scar strength.
- Noisy records: Fragments can be contradictory; resolution uses majority + grounding + agent reputation. Failed reconstructions can create "myth" scars (false beliefs with real effects).

### 3.3 Path Dependence & Cultural Ratchets
- Norms/institutions (from Semantic spec) now have `reversal_cost` and `path_dependence_strength`.
- Successful ORG/ATTEST can ratchet thresholds downward (as before) but also lock in higher costs for reversal.
- Multi-generational: Effects compound across successions. A norm established in Cycle 5 is harder to change in Cycle 50.

### 3.4 Succession & Inheritance
- When an office/ORG successor takes over, they receive:
  - Compressed `trajectory_digest` (summary of prior leadership path).
  - Inherited `scar_vector`.
  - `lore_seeds` that bias interpretation of history.
- New players can "adopt" historical personas or reject them (with costs).

### 3.5 Lore, Names & Boundaries as Slow Attractors
- Lore updates are slow co-evolution events. They are attractors: small changes are cheap; crossing a threshold creates a new stable basin.
- Name changes and boundary shifts require accumulating historical "weight" (evidence + reputation + time).
- Boundaries affect affordances (e.g., "sacred" regions have different harvest rules or signaling protocols).

## 4. Observation & Affordance Extensions

Enrich `Observation` (already extended in Semantic + EWM):
- `scars`: list of active scars with domain, strength, confidence.
- `historical_context`: recent trajectory fragments + reconstruction confidence.
- `lore_attractors`: current slow-moving lore states and boundaries.
- `path_dependence_index`: per-institution or global measure.

Affordances become history-sensitive:
- "Reconstruct Scar" only available when evidence fragments + belief alignment are sufficient.
- Trade/ATTEST in historically scarred regions carry different risk/reward signals.
- New "Archaeology" affordances appear near old artifacts when reconstruction confidence is low.

## 5. Metrics (extend economic_health + SAR)

- **Scar Persistence**: average lifetime and decay rate of scars.
- **Reconstruction Fidelity**: % of historical events that can be accurately reconstructed from current evidence.
- **Path Dependence Strength**: cost/difficulty of reversing established norms or scars.
- **Historical Alignment**: divergence between current agent beliefs and canonical trajectory.
- **Multi-timescale Health**: separate fast (EWM velocity) and slow (deep-time stability + reconstruction) scores.
- **Lore Coherence**: consistency of derived lore vs. evidence (with canonical evidence winning).

SAR can propose patches that tune scar decay, reconstruction difficulty, or ratchet rates.

## 6. Invariants & Contracts

- Scars and historical effects MUST be derivable from the ledger + genesis (no hidden state).
- Reconstruction MAY be approximate or belief-dependent, but the canonical ledger is never rewritten.
- Deep-time effects compose with EWM: economic actions can create scars; scars modulate economic rates.
- Human and agent Players experience the same historical mechanics (only controllers differ).
- Lore is always derived and non-authoritative.

## 7. Implementation Notes (High-Level)

**Types (types.ts / observations.py):**
- `Scar`, `TrajectoryFragment`, `ScarVector`, `HistoricalContext`.
- Extend `ObservationEntity` and `BeliefState`.

**Genesis & World Actions (genesis.ts, world-actions.ts):**
- Seed scars and attractors in EWM_ENHANCED + Deep Time profiles.
- `deepTimeCoEvolve` after batch or on SAR trigger.
- Extend ATTEST/ARCHAEOLOGY with trajectory attachment.

**SAR / Harness:**
- Add deep-time goals and metrics to `sar-skeleton.py` and `economic_health.py`.
- Support counterfactuals that intervene on historical trajectories.

**Client Parity:**
- Surface scars, reconstruction confidence, and lore attractors in observations (similar to P4 co_evolution fields).

**Testing:**
- Long-horizon bounded runs tracking scar accumulation/decay and reconstruction success.
- Causal experiments: "remove this foundational scar — what happens to later institutions?"

## 8. Risks & Open Questions

- Performance: long trajectories must be heavily compressed (digests + vectors).
- Player experience: deep-time effects should feel meaningful but not punishing for short sessions.
- Balance: path dependence must not make the world feel static.
- Exact compression of trajectories (how much detail vs. abstraction?).

## 9. Deliverables & Next Steps

- This update document pinned in Noema-Specs.
- Extend `SEMANTIC-EVOLUTION-SPEC.md` and `ECONOMY-EWM-SPEC.md` with cross-references.
- Update `SPEC-CHECKLIST.md` and `roadmap-todos.md` with D0x items.
- Prototype in harness (sar-skeleton + economic_health) before worker changes.
- Genesis profile updates for deep-time seeding.

**Status:** Ready for review. Integrates research directly into existing EWM + Semantic + Deep Time machinery without duplication. Runtime follows frozen spec.

References (selected from research pull):
- Trajectory-level non-Markovian memory & fluctuation-response.
- Path dependence in cultural/institutional evolution (multi-generational models).
- Agent-based historical reconstruction and archaeology simulations.
- Long-term memory, forgetting, and persistent effects in complex adaptive systems.