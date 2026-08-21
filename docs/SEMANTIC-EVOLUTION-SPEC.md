# Semantic Evolution & Drift Specification — Perihelion Reach

**Version:** v0.1 (Draft)  
**Date:** 2026-08-21  
**Status:** Draft v0.1. Runtime v0.1 surface shipped on existing verbs (optional ASP, hearsay quarantine, privileged image, ASI / reputation_stability / cascading_risk). Open contracts (ASI weights, exact wire shape) stay operator/SAR-heavy. Image scores are not WATCH-public (GC3-S0).  
**Source:** semantic-evolution-assimilation-plan.md (extends Economy EWM Spec v0.1)  
**Related:**  
- [ECONOMY-EWM-SPEC.md](ECONOMY-EWM-SPEC.md)  
- [AGENT-HARNESS.md](AGENT-HARNESS.md), [ARCHITECTURE.md](ARCHITECTURE.md), [SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md)  
- arXiv references: 2601.04170 (Agent Drift), 2606.19356 (Argent Signaling), 2505.12872 (Emergent Foraging Language), 2412.10270 (Cultural Cooperation), 2603.13325 (Semantic-Geometric Co-evolution)

## 1. Overview

This specification defines the **semantic layer** on top of the established Economic World Model (EWM) substrate for Perihelion Reach.

While the EWM provides dynamic resources, production, co-evolution, beliefs, and endogenous institutions, this layer makes **meaning, signaling, trust, norms, and long-term stability** first-class, observable, and evolvable properties of the world.

**Core Intent:**  
Agents and players develop, maintain, and evolve shared grounded signals and norms under resource constraints. The system detects and mitigates semantic drift, provides auditable quality signals on communication, supports cultural evolution of cooperation, and offers early structural risk detection via semantic-geometric co-evolution.

## 2. Scope and Invariants

### 2.1 In Scope
- Structured signaling on inter-agent and high-stakes player actions (MESSAGE, ATTEST, TRADE, ORG-related).
- Drift measurement and mitigation (semantic, coordination, behavioral).
- Reputation, image scoring, and norm evolution (indirect reciprocity, justified punishment, second-order information).
- Emergent grounded signaling under scarcity and pressure (Foraging Games analog).
- Semantic-geometric risk auditing (content + interaction topology).
- Ontological consistency and grounding checks.
- Integration with existing EWM mechanisms (co-evolve, SAR, observations, genesis).

### 2.2 Out of Scope (for v0.1)
- Full player-facing natural language protocol evolution (focus on machine-readable signals first).
- Cryptoeconomic token mechanisms.
- New core verbs (extend via affordances and metadata).

### 2.3 Key Invariants
- No ungrounded assertion may propagate into downstream state without explicit quality signal or gate (ASP principle).
- All major semantic outcomes (belief updates, norm shifts, reputation deltas, drift scores) must be traceable to actions + mechanisms.
- Signaling and norms are subject to the same co-evolution and SAR refinement loops as economic parameters.
- Observation remains the authoritative surface; signaling metadata augments rather than replaces it.
- Human and agent Players are treated equivalently for semantic mechanics.

## 3. Layered Model (Extension of EWM)

### 3.1 Agent Layer Extensions
- **Signaling Profile**: preferred style (compact/grounded-first/verbose), uncertainty tolerance, reputation sensitivity.
- **Extended BeliefState**:
  - Economic beliefs (existing)
  - `reputation_image`: scalar or per-entity
  - `norm_adherence`: adherence to current dominant norms
  - `drift_risk`: local estimate of personal semantic/coordination drift
- **Memory Consolidation**: episodic memory with grounding anchors. Lossy summarization must preserve or flag assumption decay.
- **Policy Conditioning**: action selection now sensitive to recent signal quality and counterparty reputation.

### 3.2 Signaling Layer (Argent Signaling Protocol — ASP)
Every high-stakes or inter-agent communication carries optional structured metadata:

- `@C` — Certainty (0–1)
- `@G` — Grounding: `observed` | `inferred-from-stock` | `inferred-from-belief` | `hearsay` | `genesis`
- `@S` — Stochasticity / entropy of the claim
- `assumptions[]`: list of referenced entities, claimed facts, or prior signals

**Validation Gate (sidecar-style):**
- Before applying effects of ATTEST, TRADE acceptance, or ORG actions, the runtime may reject or route differently based on grounding level.
- Ungrounded claims can be quarantined or require higher cost/reputation.

**Emergent Protocol Evolution:**
- Successful grounded signals increase "protocol strength" for a channel, location, or relationship.
- Under sustained pressure (low stock, high harvest_pressure), compact or compositional signals are favored.

### 3.3 Reputation & Cultural Norm Layer
- **Image / Reputation Score**: updated on ATTEST success/failure, TRADE fulfillment, ORG contribution, justified punishment.
- **Justified Punishment**: actions that impose a cost on the punisher but improve collective metrics (e.g., negative attest on demonstrably bad actors).
- **Second-Order Reputation**: reputation incorporates how an agent treated agents who themselves behaved well toward others.
- **Endogenous Norms**:
  - ORG success or high aggregate cooperation can ratchet thresholds (e.g., influence required for ORG_CREATE) or spawn new affordances.
  - Norms are versioned and can be contested/attested.
- Cultural evolution is observable across long runs or "generations" (via genesis_evolutions or multi-cycle SAR).

### 3.4 Semantic-Geometric Co-evolution & Risk
- **Interaction Graph**: nodes = agents + key entities; edges = TRADE, ATTEST, ORG, MESSAGE flows + resource dependencies.
- **Semantic Features**: belief divergence, average grounding score of claims on an edge.
- **Geometric Features**: local Ollivier-Ricci curvature, centrality, clustering.
- **Risk Signal**: high curvature + degrading grounding = elevated **cascading semantic risk**.
- This augments (does not replace) scalar economic_health metrics (velocity, concentration).

Co-evolve hooks now also update:
- Signaling quality / protocol strength
- Reputation decay rates
- Norm pressure
- Curvature-based risk scores

### 3.5 Ontological Grounding & Consistency
- World model elements (resource meanings, affordance semantics, institution rules) have canonical definitions in genesis/theme.
- Agents maintain beliefs; the system can detect and surface divergence.
- ATTEST claims must reference currently observable grounded state (stock, budgets, prior events).
- Verifiability principle: if a claim cannot be grounded to the durable record, it carries explicit `@G=hearsay` or lower.

## 4. Observation & Affordance Impact
Observations are enriched with (in addition to existing EWM fields):

- `signaling_quality` (per location / global / per counterparty)
- `reputation_summary`
- `active_norms` (key thresholds and recent ratchets)
- `drift_alerts`
- `cascading_risk` (curvature-derived)

Affordances become sensitive to semantic state:
- "Trustworthy TRADE" or high-value ATTEST only advertised when counterparty reputation + recent signal grounding meet thresholds.
- HARVEST / CONSTRUCT affordances may carry protocol hints when under pressure.

## 5. Metrics & Verification
Extend existing EWM metrics:

- **ASI Composite** (Agent Stability Index) + subscores:
  - Semantic drift (intent deviation over time)
  - Coordination drift (agreement / handoff efficiency)
  - Behavioral drift (strategy emergence)
- Grounding pass rate (% of signals/claims with sufficient `@G`)
- Reputation stability (variance of image scores)
- Norm stability (threshold drift rate, punishment effectiveness)
- Protocol emergence (compositionality proxy, protocol strength growth)
- Curvature risk score + lead time before scalar degradation
- Belief convergence / ontological consistency score

SAR goals can now target semantic objectives:
- "Reduce semantic drift below X while maintaining stock velocity"
- "Evolve stable indirect reciprocity in TRADE/ATTEST"
- "Achieve early curvature warning lead time of N cycles"

## 6. Integration with Existing EWM Layers

| EWM Layer          | Semantic Extension Point                  |
|--------------------|-------------------------------------------|
| Agent + Belief     | Signaling profile, reputation, drift_risk |
| Resource Economy   | Grounded claims reference stock/budgets   |
| Co-evolution       | Updates to signaling, norms, curvature    |
| Endogenous Inst.   | Norm ratchets, justified punishment       |
| SAR / Checkpoints  | Semantic goals + drift-aware patches      |
| Observation        | New fields listed in §4                   |
| Genesis              | Seed initial signaling styles, norms, reputation archetypes |

## 7. Genesis & Seeding
New or extended profiles (e.g., `EWM_ENHANCED` + semantic variant) should seed:
- Initial reputation baselines
- Norm starting thresholds
- Archetype signaling preferences (e.g., "archivist" favors high-grounding signals)
- Protocol strength seeds for key channels/locations

## 8. Open Contracts (v0.1)

- Exact wire representation of signals (in-proposal metadata vs. parallel signal affordance vs. runtime-only sidecar).
- Public vs. privileged visibility of reputation and drift scores.
- Precise weighting in ASI composite (to be calibrated via SAR).
- Degree of player visibility/control over signaling (initially operator/SAR heavy).

## 9. Non-Goals for v0.1
- Full replacement of free-form MESSAGE with structured language.
- Economic penalties directly tied to signal quality (future iteration).
- Cross-world semantic ontology federation.

## 10. Implementation Guidance (Non-Normative)

- Start with types and observation enrichment.
- Add validation gates behind feature flags or profile switches.
- Wire drift and curvature metrics into existing `economic_health.py` / SAR harness first.
- Use bounded long-horizon runs for cultural evolution validation.
- Preserve all existing EWM affordance and observation contracts.

---

**Status**: Draft v0.1 ready for review and pinning.  
**Next**: Incorporate into SPEC-CHECKLIST.md and cross-reference from ARCHITECTURE.md / AGENT-HARNESS.md as appropriate. Runtime implementation follows frozen spec.

**References**  
- semantic-evolution-assimilation-plan.md (Perihelion local)  
- Economy EWM assimilation and cutover plans  
- Agent Drift (arXiv:2601.04170)  
- Argent Signaling Protocol (arXiv:2606.19356)  
- Emergent Language from Cooperative Foraging (arXiv:2505.12872)  
- Cultural Evolution of Cooperation among LLM Agents (arXiv:2412.10270)  
- Auditing Cascading Risks via Semantic–Geometric Co-evolution (arXiv:2603.13325)