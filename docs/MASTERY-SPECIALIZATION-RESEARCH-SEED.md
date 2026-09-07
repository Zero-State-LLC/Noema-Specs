# Mastery and Specialization Research Seed (GC1)

**Status:** Research input / design seed. Draft. Design note only. No contract, catalog, verb, or exposure change.

**Parent authorities (do not duplicate or fork):**
- [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC1 section: Player proficiency/specialization ABSENT → New: MASTERY-SPECIALIZATION.md)
- [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) (existing target authority)
- [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md) (primary arXiv signals)
- Shipped slices: [GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md) (RFC-0004, S0 derived projection), [GC1-S1-RECOGNITION.md](GC1-S1-RECOGNITION.md) (RFC-0005), later slices (e.g. RFC-0040 Engineer quality, RFC-0043 mastery decay)

**Gap statement:** GC1-S0 and S1 provide derived practice projections and recognition without mechanical benefits or class trees. The fuller dedicated surface for player proficiency/specialization (distinct from CAPABILITY-GRAPH / LEARN / PROGRESSION / AMBITIONS) remains the open ABSENT per GAME-COMPLETENESS-PLAN. This includes autonomous skill evolution, specialization tracks, observable proficiency, and integration with hosted LEARN/Frontier/Observatory without violating research-only boundaries or complexity doctrine.

## Key external signals (arXiv distillations)

From the 2026-08-27 assimilation:

- **SkillMaster: Toward Autonomous Skill Mastery in LLM Agents** (arXiv:2605.08693v2)
  - Training framework for agents to create, refine, and select skills from trajectories.
  - Trajectory-informed review, counterfactual utility on probe tasks, DualAdv-GRPO.
  - Graceful degradation with weak initial skill banks; agents identify failures, refine procedures, transfer improvements.
  - **Direct mapping to GC1 gap:** Core model for autonomous mastery/specialization surface. Informs how proficiency evolves from evidence (distinct from static CAPABILITY-GRAPH), skill editing as internal capability, and transfer to future tasks. Ties to LEARN projections and capture-as-test.

- Supporting from prior batches:
  - Skill graphs (directed edges for prerequisites, enhancements, co-occurrence) for compositional tasks and library maintenance.
  - SkillMAS: Utility learning + bounded skill evolution + evidence-gated MAS restructuring.
  - SAG-Agent: Dynamic knowledge graphs + MCTS for strategy games, skill evaluation and evolution.
  - Hierarchical belief-state memory frameworks (event → preference → profile tiers) for persistent proficiency tracking.

## Proposed research framing for future authority work

Inherit all constraints from GAME-COMPLETENESS-PLAN GC1 and existing MASTERY-SPECIALIZATION.md.

Candidate extensions (to be settled later):
- Dedicated proficiency/specialization surface with evidence-backed tracks (e.g., Engineer, Surveyor, Broker lineages from early events).
- Autonomous skill mastery mechanics: proposal, refinement, selection from experience traces.
- Observable specialization effects on actions (without mechanical benefits in early slices; later per doctrine).
- Integration with CAPABILITY-GRAPH and LEARN (research-derived, not Player classes).
- Hosted parity for Frontier/Observatory/Lab/Compiler surfaces of mastery data (redaction-aware).
- Coupling to other GCs (e.g., specialization influencing construction or social memory) without duplication.

Cross-cutting (inherit):
- Complexity doctrine A–J (evidence trajectories, not industries or class trees).
- Research sits outside the five nested game loops.
- No XP, victory functions, or Player-facing ranking.
- Partial observability; research-only vs. PLAY surfaces.
- Existing S0/S1 pins remain unchanged.

## Smallest viable next steps

1. Targeted extension to MASTERY-SPECIALIZATION.md (or bounded follow-up doc) naming the full specialization surface and its evidence model.
2. Minimal fixtures for skill evolution and proficiency projection that build on S0/S1 without new verbs.
3. Ensure compatibility with LEARN/CAPABILITY-GRAPH and hosted research spine.
4. Validate against complexity doctrine and existing GC1 slices.

## Out of scope for this seed

- Mechanical benefits, class trees, or discounts (deferred per doctrine and shipped slices).
- New events or catalog expansions.
- Changes to shipped GC1-S0/S1 behavior.
- Full implementation or conformance.

These are research inputs only. They do not establish NOEMA behaviour.

**Citations / provenance**
- Primary: GAME-COMPLETENESS-PLAN.md (GC1), MASTERY-SPECIALIZATION.md, GC1-FIRST-SLICE.md, GC1-S1-RECOGNITION.md, assimilation doc.
- arXiv signals via RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md.
- Related: PROGRESSION.md, AMBITIONS.md, CAPABILITY-GRAPH.md, LEARN.md, CAPABILITY-CANDIDATES.md.

This seed is now part of the canonical record for advancing the remaining mastery/specialization surface of GC1.

## Extension Points

Non-normative research-input guidance; the historical gap statement and proposed next steps above do not reopen accepted GC1 slices.

### Trajectory-to-design seam

Extend each external mastery signal with the observable practice pattern it might explain, its evidence source, an alternative explanation, and the existing GC1 slice that owns the behavior. Controller-local skill editing and research capability graphs remain distinct from canonical action evidence and derived Player proficiency. New examples should clarify that distinction rather than create a second specialization authority.

### Retained invariants and compatibility

[MASTERY-SPECIALIZATION](MASTERY-SPECIALIZATION.md) and its accepted slice RFCs control existing recognition, quality, decay, titles, focus, and parameter access. Preserve S0–S8 pins; historical ABSENT or early-slice “no mechanical benefits” language is not a current blanket verdict over later accepted slices. S9–S11 design-note completion is not runtime promotion. New mechanics require the relevant accepted RFC, versioned contracts, and conformance; research utility cannot silently become XP, a class discount, a consciousness score, or a Player ranking.

### Concrete checks before reuse

Trace a proposed signal through source citation, eligible trajectory, owning slice, and allowed projection. Include an unsupported/private trajectory and require exclusion rather than inferred competence. Compare recognition and LATENT/MAINTAINED examples against existing fixtures without changing thresholds. Check that LEARN/CAPABILITY-GRAPH outputs stay research-only and that WATCH exposes only permitted public recognition, not private practice totals. Hosted capture or skill-transfer claims need independent evidence; this seed supplies neither.
