# Research Spine Hosted Parity Audit (v0.2–v0.7) — 2026-08-27

**Status:** Draft design/research note. Inputs only. No contract, catalog, verb, or exposure change.

**Authorizing:** [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md) (research spine gap) · [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) · v0.2–v0.7 packages.

## Purpose
Map which Frontier/Observatory/Lab/Compiler/LEARN contracts exist only in the Python monolith vs. the hosted Worker stack. Flag projection/redaction needs for research surfaces post-Deep Time / identity changes.

## Quick inventory (high level; expand with runtime audit)

| Surface | Monolith (Python) | Hosted Worker | Notes / Gaps |
|---------|-------------------|---------------|--------------|
| v0.2 Frontier (genome, novelty, mutation, attention) | Full F01–F15 | Partial (via Worker replay/observatory?) | Situation genome + deterministic mutations need parity; redaction for spectator research. |
| v0.3 Observatory (trajectories, detectors, candidates) | Full O01–O16 | Partial projections | Trajectories/capture for LEARN may need hosted capture path. |
| v0.4 Lab (experiments, results, fixtures) | Full L01–L34 | ? | Intent compilation / result projection parity. |
| v0.5 Compiler (capture, receipts, regression) | Full P01–P30 | ? | STUDY progressive disclosure; sealed prompts boundary. |
| v0.7 LEARN (behavior nodes, capability edges) | Full K01–K12 | Research-only surface | Must remain outside PLAY; no Player stat projection. Redaction for agent-only. |
| Deep Time / evidence | Full D01–D30 + G | Partial (archive settlement) | Lineage writing; per-view forbidden_in_projection. |

## Flags for follow-up
- New projection surfaces or redaction boundaries for hosted research (WATCH vs STUDY vs internal).
- Capability graph / LEARN edges from hosted capture vs monolith.
- Parity for Frontier novelty vectors and Observatory anomaly detection in live worlds.
- No changes to frozen contracts; research-only.

**Citations:** Assimilation 2026-08-27 research spine item; SPEC-FREEZE-CORE-LOOP; v0.2–v0.7 conformance packages; AGENT-SEAL / RFC-0115.

Design note only. Next: runtime audit against live world.perihelion-reach-3 or equivalent.

## Extension Points

Non-normative audit-method guidance; “Full”, “Partial”, and question marks in the historical inventory are hypotheses or dated summaries, not fresh hosted verification.

### Per-contract parity seam

Expand one inventory row into a bounded comparison of input contract, implementation revision, execution plane, deterministic output, and projection exclusions. Frontier mutations, Observatory trajectories, Lab results, Compiler receipts, LEARN edges, and Deep Time lineage need separate evidence: the presence of a route or module does not prove its end-to-end contract. Keep test artifacts and exclusions attached to the surface they actually exercise.

### Retained invariants and promotion

Use [DIRECTION-AUTHORITY](DIRECTION-AUTHORITY.md) and [current-state](../specs/current-state.v1.yaml) for plane distinctions. Offline parity does not establish Worker deployment, and hosted acceptance does not establish a research claim. Preserve consent, provenance, version lineage, deterministic replay inputs, sealed-prompt privacy, and the separation of authorized STUDY from public WATCH. Only agents are Players; human research authorization is not inhabit or full-state Controller access. New projections or export fields require owning-contract review rather than adoption through this audit table.

### Concrete audit checks

Compare equivalent version-pinned inputs across available implementations and record output differences, unavailable paths, and excluded data explicitly. Test replay lineage and capture-to-receipt references; distinguish missing evidence from NOT_COMPUTABLE claims under the relevant contract. Include unauthorized research access, private prompt material, and a public WATCH projection as negative disclosure cases. Require LEARN/novelty/anomaly outputs to remain outside Player rewards and ordinary PLAY. Run only separately authorized runtime audits; this document-only extension records no live, localization, or accessibility verification.
