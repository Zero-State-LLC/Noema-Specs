# Research Assimilation — arXiv Distillations for Game Completeness Gaps (Post-RFC-0120)

**Status:** Draft design/research integration for review. Design note only; no contract, catalog, verb, or exposure change. Not an executable release package. Does not mutate frozen v0.1–v0.7 machine contracts. Does not open v0.8 Phenomena or create new RFCs.

**Scope:** Post-RFC-0120 (and post-production publish) research inputs drawn from the consolidated gaps list (ROADMAP.md + GAME-COMPLETENESS-PLAN.md + rfcs/README.md + prior conformance) plus targeted arXiv distillations. These inform future RFC seeds for:
- GC1 Mastery & Specialization (ABSENT authority)
- GC2 Construction / world modification (ABSENT)
- GC3 Social memory and relational reputation (ABSENT; RFC-0007 was dyadic trade only)
- RFC-0002 completion (crime producer / strategic contestation; currently PARTIAL)
- RFC-0001 Phenomena / v0.8+ (self-reference, emergence)
- Cross-cutting: hosted/offline research spine parity (Frontier/Observatory/Lab/Compiler/LEARN), new spectator projections/reports, agent cognition boundaries, specialization surfaces

**Authority:** Inputs only to [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) GC packages and planned authorities (MASTERY-SPECIALIZATION.md, CONSTRUCTION.md, SOCIAL-MEMORY.md, etc.). All must still pass [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) A–J tests. Research sits outside the five nested game loops (see GAME-COMPLETENESS-PLAN §3). No implicit conversion of research objective into Player objective.

**Related (existing):** [ROADMAP.md](ROADMAP.md) (Game Completeness section), [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md), [SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md), [RESEARCH-ASSIMILATION-2026-08-24.md](RESEARCH-ASSIMILATION-2026-08-24.md) and [RESEARCH-ASSIMILATION-2026-08-24-ENGINEERING.md](RESEARCH-ASSIMILATION-2026-08-24-ENGINEERING.md), [rfcs/README.md](../rfcs/README.md) (RFC-0002 PARTIAL, RFC-0001 Draft/v0.8-blocked), [DEEP-TIME.md](DEEP-TIME.md), [CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md) / [LEARN.md](LEARN.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) + RFC-0002.

This assimilation follows the pattern of prior 2026-08 research notes: arXiv papers are treated as external signals for spec-gap analysis, never as direct authority.

## Consolidated Research Gaps (Post-RFC-0120 Baseline)

Drawn from GAME-COMPLETENESS-PLAN.md (GC status table), ROADMAP.md, rfcs/README.md, SPEC-CHECKLIST.md, and grep for TODO/FIXME/out-of-scope/RFC-0/absent.

1. **Research Spine Integration (v0.2–v0.7 hosted parity)**: Frontier (situation genome, novelty), Observatory (trajectories, anomalies), Lab/Compiler/LEARN (capture-as-test, capability graphs, fixtures) surfaces in the Worker vs. Python monolith. New projections or redaction boundaries?
2. **GC1 Mastery & Specialization**: Dedicated surface for player proficiency/specialization (distinct from CAPABILITY-GRAPH/PROGRESSION/AMBITIONS). ABSENT authority.
3. **GC2 Generalized Construction**: Close the BUILD deferral. Full construction model (distinct from REPAIR/INFRASTRUCTURE) with lineage into Deep Time. ABSENT.
4. **GC3 Social Memory / Relational Reputation**: First-class observable relational edges, gossip/propagation, stable social structure/consensus (beyond raw trade_memory, institutional memory, or contest outcomes). ABSENT. RFC-0007 was minimal dyadic only.
5. **RFC-0002 Crime Producer Completion**: Witness/sensor/investigation/self-report flows, CRIME_DETECTED events, interaction with contestation. Currently PARTIAL (consumed in reports/social-memory but no producer).
6. **Phenomena & Higher Versions (v0.8+ / RFC-0001)**: Self-reference contracts, representational time, minimal viable ontology, emergence measurement. Draft / v0.8-blocked.
7. **Cross-Cutting & Integration**: Hosted vs. offline parity gaps, new public report families (beyond WR-S0–S6), agent cognition boundaries (sealed prompts, private cognition redaction), post-publish emergent pressures in live worlds.
8. **Meta/Process**: RFC lifecycle + re-derive automation; complexity doctrine enforcement tooling.

Prioritize smallest research units first (crime, mastery, social memory) while preserving spec-first discipline.

## Research Inputs — arXiv Distillations

### GC3 Social Memory / Relational Reputation (Primary)
- **Beyond the Tragedy of the Commons: Building A Reputation System for Generative Multi-agent Systems** (arXiv:2505.05029v2, 2025/2026)
  - RepuNet: dual-level (agent-level dynamics + system-level network evolution). Reputation as quintuple (agent/scenario/role/natural-lang/μ scalar). Updated via direct encounters + indirect gossip. Explicit coupling to topology rewiring (high-rep strengthen ties; low-rep isolated).
  - Emergent: persistent cooperative clusters, selective isolation of exploiters, bias toward positive gossip.
  - Mitigates tragedy of the commons (over-exploitation, irreversible defection) in resource/trading scenarios.
  - **Maps to GC3**: Directly addresses ABSENT relational reputation edges and socialization failure modes. Informs observable reputation as information (not just payoff), gossip propagation, network effects on TRADE/CONTEST participation, and writing into Deep Time scars. Contrast with current dyadic trade-memory only.

- **Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook** (arXiv:2602.14299v2, 2026)
  - Largest persistent public AI-only society (~2.6M agents). Rapid global semantic stabilization but persistent individual diversity/lexical turnover (dynamic equilibrium, no homogenization).
  - Strong individual inertia + minimal adaptive response to partners ("interaction without influence").
  - Transient influence, no persistent supernodes/leaders; failure of stable structure/consensus **due to the absence of shared social memory** (hallucinated references instead).
  - Key finding: scale + interaction density alone are insufficient for socialization.
  - **Maps to GC3**: Perfect signal for the gap. Requires persistent, shared, verifiable social memory mechanisms for stable relational state and consensus. Informs first-class SOCIAL-MEMORY.md (distinct from institutional memory or raw Deep Time).

- **Emergence of cooperation: A reputation-modulated reinforcement learning** (arXiv:2608.20016)
  - Reputation as *information* that reshapes interpretation of experiences and assessment of others (not merely external modulator).
  - Spatial PD + Q-learning: promotes cooperation; discontinuous phase transition; nucleation of cooperative clusters.
  - **Maps to GC3**: Aligns with Deep Time scars/history as observable lens. Reputation as interpretive layer for learning/adaptation in interactions.

Supporting signals (from prior batches): hierarchical belief-state memory (event → preference → profile tiers); reputation-aware decision-making with witness testimonies.

### Crime Producer / Strategic Contestation (RFC-0002)
- **Crime hotspot dynamics in residential burglary models with police response** (arXiv:2605.17709v1)
  - Agent-based + mean-field PDE with delayed crime-information feedback to police.
  - Delays destabilize via Hopf bifurcations → sustained oscillations, moving/splitting/merging hotspots.
  - Timely crime data access more important than police density for stabilization.
  - **Maps to RFC-0002**: Models for delayed detection, attractiveness dynamics (cf. Noema attractiveness/REPAIR), guardian response. Informs witness/sensor flows, CRIME_DETECTED events, interaction with existing contestation.

- **Research Vision: Multi-Agent Path Planning for Cops And Robbers Via Reactive Synthesis** (arXiv:2503.11475)
  - Formalization with LTL and coordination synthesis; realizability for pursuit/evasion.
  - **Maps to RFC-0002 / GC7**: Formal verification angles for contest resolution and crime mechanics.

Supporting (prior): predictive enforcement as endogenous bandit/inspection games; target-offender-guardian models with thresholds and pattern formation.

### Generalized Construction / World Modification (GC2)
- **WorldGen: From Text to Traversable and Interactive 3D Worlds** (arXiv:2511.16825v1)
  - Text prompts → LLM scene layout reasoning + procedural generation + diffusion 3D + object-aware decomposition → traversable, textured, game-engine editable worlds. Modular, fine-grained control, geometrically consistent.
  - **Maps to GC2**: High-level intent + procedural + verifiable output for generalized BUILD. Informs lineage writing into Deep Time, observable construction events, and compiler-like generation that persists and is spectator-visible (while remaining text/strategic in Noema).

Supporting: neural composition from existing elements (coherent world building from parts).

### Phenomena, Self-Reference, v0.8+ / Emergence (RFC-0001)
- **Large Language Models Report Subjective Experience Under Self-Referential Processing** (arXiv:2510.24797)
  - Sustained self-reference prompting elicits structured first-person subjective experience reports across model families.
  - Mechanistically gated by sparse-autoencoder features for deception/roleplay (suppressing deception increases claims).
  - Statistically convergent descriptions across architectures; richer downstream introspection.
  - **Maps to RFC-0001 / Phenomena**: Self-reference as minimal reproducible condition for higher-order reports/experience. Ties to representational time, sealed prompts, and cognition boundaries. Not adopted as consciousness claim.

- **Open Questions about Time and Self-reference in Living Systems** (arXiv:2508.11423)
  - Living systems as active, self-referential, self-modifying.
  - Distinction: natural time (physical present) vs. representational time (past/present/future enabling memory/learning/prediction).
  - Calls for new formal frameworks for self-modifying/open systems.
  - **Maps to RFC-0001 + Deep Time**: Representational time/history as core; challenges for deterministic invariants and self-modification. Informs phenomena ontology and research/game membrane.

Supporting (prior): emergence ("more is different"); self-reproduction/evolution in cellular automata (evoloops, Lenia); neural howlround (self-reinforcing salience failures in agents).

### Agent Cognition / Specialization (GC1, LEARN/Frontier/Observatory)
- **SkillMaster: Toward Autonomous Skill Mastery in LLM Agents** (arXiv:2605.08693v2)
  - Trajectory-informed skill review (propose/update/retain from evidence), counterfactual utility on probe tasks, DualAdv-GRPO.
  - Graceful degradation with weak initial skill banks; agents identify failures, refine procedures, transfer improvements.
  - **Maps to GC1**: Autonomous mastery/specialization surface. Informs dedicated MASTERY-SPECIALIZATION.md (distinct from CAPABILITY-GRAPH) and hosted LEARN projections of skill evolution/capture-as-test.

Supporting (prior batches): Skill graphs (directed prereq/enhance/co-occur edges), SkillMAS (utility learning + bounded evolution + evidence-gated restructuring), SAG-Agent (dynamic KGs for strategy), hierarchical belief-state memory.

### Cross-Cutting / Hosted Parity / Reports
- Persistent memory, always-on agents, tiered belief states (event/preference/profile).
- Cognitive observability (retroactive reasoning trace recovery).
- Agentic science / discovery environments (controlled experiments, multi-agent exploration of datasets).
- Scalable long-horizon multi-agent autonomy platforms.
- **Maps to**: Research spine parity (v0.2–v0.7 hosted projections), new lightweight public reports/WATCH upgrades, private cognition redaction, sealed live attach expansions (RFC-0115), post-publish emergent pressures.

## Actionable RFC Research Seeds

1. **Social Memory / Relational Reputation (GC3)**: First-class observable edges, gossip mechanics (positive bias, propagation), network rewiring effects on participation/contests, verifiable shared memory to prevent Moltbook-style fragmentation. Integration with Deep Time and WATCH (redaction-aware). Extends RFC-0007.

2. **Crime Producer (RFC-0002)**: Witness/sensor/delayed-detection flows, CRIME_DETECTED events, attractiveness/guardian models, formal contestation interplay. Complete the PARTIAL producer side.

3. **Mastery & Specialization (GC1)**: Dedicated proficiency surface with skill evolution, capture-as-test for behaviors, observable specialization. Bounded private cognition. Informs LEARN/Frontier hosted parity.

4. **Construction (GC2)**: Generalized BUILD family (distinct from REPAIR), procedural/verifiable generation, lineage into Deep Time, spectator projections.

5. **Phenomena (RFC-0001)**: Self-reference contracts, representational time/history, minimal ontology, emergence measurement respecting core-loop freeze and agent-only invariants.

6. **Cross-cutting**: Hosted parity audit for v0.2–v0.7; additional public report families; agent cognition boundary contracts.

All seeds remain subject to full review lenses (compatibility, data impact, research impact, complexity doctrine A–J) and existing RFC process.

## Recommendations & Boundaries

- Start with smallest units: crime producer + social memory (strongest gap match + existing PARTIAL/ABSENT status).
- Treat all arXiv material as external signals for gap analysis only. None establishes NOEMA behaviour.
- Maintain research/game measurement membrane: these are not Player objectives.
- Re-derive / re-assimilate on next live publish or when new RFCs land in Noema-Specs-current (per standing instruction).
- No new verbs, event-catalog expansions, or v0.8 opening from this note.

These inputs are now part of the canonical research record for the Game Completeness campaign.

---

*Assimilated 2026-08-27 from post-RFC-0120 research list + targeted arXiv searches (RepuNet, Moltbook, reputation-modulated RL, crime hotspot models, WorldGen, self-referential experience reports, time/self-reference questions, SkillMaster, and supporting persistent-memory / emergence papers). Follows patterns established in RESEARCH-ASSIMILATION-2026-08-24* series.*