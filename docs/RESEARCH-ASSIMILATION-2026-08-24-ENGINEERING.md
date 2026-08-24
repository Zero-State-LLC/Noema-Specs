# Research Assimilation — Engineering: Deep Time Tails, Deferred Culture
Metrics, Projection Views, and Client Chrome

**Status:** Draft design integration for review. Not an executable release package.
**Scope:** Deep Time tails versus RFC-0001, deferred Wasserstein / Ollivier and
live cultural-generation, per-view `forbidden_in_projection`, and harness /
official-client chrome.
**Does not open:** a new RFC, new verbs, `event-catalog/0.3`, Genesis, a Worker
publish, WATCH copy, v0.8 Phenomena acceptance, SPEC-FREEZE Slice D hosting, or
a crime producer.

This is the third bounded research pull on 2026-08-24, after
[RESEARCH-ASSIMILATION-2026-08-24.md](RESEARCH-ASSIMILATION-2026-08-24.md). That
one took provenance, statistical evidence, and norm origin. This one takes the
engineering half of the same day's field: what the hosted Deep Time tails
already do, which culture metrics stay inert, how projection bans stay
per-view, and what the harness and official client may render. It is a
cross-cutting design note, not a second canon. Accepted RFCs remain
authoritative.

## Research inputs

Culture, Wasserstein, Ollivier — all deferred as live product default:

- [Tracking Semantic Change in Slovene: A Novel Dataset and Optimal Transport-Based Distance](https://arxiv.org/abs/2402.16596): held-out optimal-transport distance for lexical change; a Lab fixture shape, not a PLAY metric.
- [Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](https://arxiv.org/abs/2412.12569): unbalanced OT for lexical shift when mass is not conserved.
- [Ollivier Ricci-flow on weighted graphs](https://arxiv.org/abs/2010.01802): Ricci-flow on weighted graphs; Forman–Ricci remains the shipped p5-04 metric.
- [Community Detection in networks by Dynamical Optimal Transport Formulation](https://arxiv.org/abs/2205.08468): OT as a community-detection method on an existing graph.
- [Unfolding the multiscale structure of networks with dynamical Ollivier-Ricci curvature](https://arxiv.org/abs/2106.05847): dynamical Ollivier-Ricci as a multiscale graph read.
- [When Stories Evolve: Benchmarking LLM Storytelling Across Agent Architectures in Open-Ended World Simulations](https://arxiv.org/abs/2608.15654): WSE-bench measures story evolution across architectures; it is not a hosted generator.
- [LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations](https://arxiv.org/abs/2603.01952): a cultural benchmark for LLM populations, not a live culture engine.
- [It Means More if It Sounds Good: Yet Another Hypothesis Concerning the Evolution of Polysemous Words](https://arxiv.org/abs/2003.05758): Ollivier-Ricci on a synonym graph as a polysemy proxy.

Deep Time tails, path dependence, attractors, and unsupported belief — none of
these is RFC-0001:

- [The dynamics of cultural systems](https://arxiv.org/abs/2601.00440): cultural systems as dynamical objects distinct from individual self-model constructs.
- [The Non-Optimality of Scientific Knowledge: Path Dependence, Lock-In, and The Local Minimum Trap](https://arxiv.org/abs/2604.11828): path dependence and lock-in as measured properties, not cost drivers by themselves.
- [When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings](https://arxiv.org/abs/2407.04503): cultural attractors as evaluation tools for multi-turn drift.
- [TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies](https://arxiv.org/abs/2603.16910): open-endedness in an LLM ecology; not a reason to accept v0.8.
- [Emergent Culture in Minimal LLM Systems](https://arxiv.org/abs/2606.30668): culture can appear in a minimal system; NOEMA still derives it from ledgered practice.
- [Never eat a Pigeon with a Pumpkin: a model for the emergence and fixation of unsupported beliefs](https://arxiv.org/abs/2411.10743): unsupported beliefs can fixate; that is not a myth-scar producer.
- [Modeling Trust and Liquidity Under Payment System Stress: A Multi-Agent Approach](https://arxiv.org/abs/2602.16186): stress and lock-in under load; not a new verb or event.
- [The Lock-in Hypothesis: Stagnation by Algorithm](https://arxiv.org/abs/2506.06166): algorithmic lock-in; `reversal_cost` remains the cost, `path_dependence_strength` does not.

Already cited by [RFC-0001](../rfcs/RFC-0001-phenomena-self-reference-integration.md)
— not new inputs, and not a reason to accept the draft:

- [Consciousness in Artificial Intelligence: Insights from the Science of Consciousness](https://arxiv.org/abs/2308.08708)
- [Initial results of the Digital Consciousness Model](https://arxiv.org/abs/2601.17060)
- [Emergent Language as an Approach to Conscious AI](https://arxiv.org/abs/2606.06380)

Projection and fail-closed views:

- [When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents](https://arxiv.org/abs/2607.18261): a schema-valid payload can still be the wrong view.
- [Verifier-Bound Communication for LLM Agents: Certified Bounds on Covert Signaling](https://arxiv.org/abs/2603.00381): verifier-bound channels; public WATCH stays the fail-closed view.
- [Blockaid: Data Access Policy Enforcement for Web Applications](https://arxiv.org/abs/2205.06911): policy enforcement at the view, not a global string deny-list.
- [Data Guard: A Fine-grained Purpose-based Access Control System for Large Data Warehouses](https://arxiv.org/abs/2502.01998): purpose-based allow/deny per surface.
- [FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs](https://arxiv.org/abs/2607.27267): evidence-backed permission graphs; claim labels stay on derived scores.
- [Intent-Governed Tool Authorization for AI Agents](https://arxiv.org/abs/2606.22916): intent-governed authorization; default DENY until a surface names the token.
- [Introducing the Generative Application Firewall (GAF)](https://arxiv.org/abs/2601.15824): a generative firewall is still a per-channel policy.
- [Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models](https://arxiv.org/abs/2608.06690): auditable capability masks; LOOK chrome is not a second truth.

These are design inputs. None is evidence that a NOEMA behaviour is
established, none may become hidden world truth, and none may become a
research objective visible to Players.

## Slice A — Deep Time tails are not RFC-0001

**Existing authority:** [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md)
§7 and Slice H, [RFC-0001](../rfcs/RFC-0001-phenomena-self-reference-integration.md),
[rfcs/README.md](../rfcs/README.md), [research/phenomena-ontology.md](../research/phenomena-ontology.md),
[DEEP-TIME-MECHANICS-UPDATE.md](DEEP-TIME-MECHANICS-UPDATE.md),
[DEEP-TIME.md](DEEP-TIME.md), [LORE-BOUNDARY.md](LORE-BOUNDARY.md),
[RFC-0123](../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md),
and [REMAINING-WORK-2026-08-21-worker-pin.md](REMAINING-WORK-2026-08-21-worker-pin.md).

**OBSERVED.** RFC-0001 is Draft / v0.8-blocked / runtime NONE. It adds five
SELF / INTEGRATION constructs inside `phenomena-ontology/0.1` (Indexical
Encoding Competence, Persistent Self-State Latch, Echo-Mismatch Repair,
Workspace Broadcast Proxy, Multi-Timescale Coherence). It does not mention
`path_dependence_strength`, myth scars, or lore attractors. SPEC-FREEZE §7
puts RFC-0001 and v0.8 Phenomena out of scope for first implementation.

Slice H is partial-live. The freeze already names the shipped half: scars,
evidence fragments, RFC-0123 ratchets, succession, and checkpoint restore in
hosted `deep-time.ts`. The tails are sharper than the freeze table's
"computed but unconsumed / inert" line:

- `path_dependence_strength` is computed on the ratchet and folded into LOOK
  `path_dependence_index` (max of scar-strength mean and ratchet mean). It is
  not a cost driver. `reversal_cost` is.
- The WATCH map forbids the index
  ([WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) §1.1;
  remaining-work `/v1/watch/map` row).
- Lore attractors exist. They tick on the slow pass (`cycle % 5`), inherit as
  labels when an officer leaves the formation, and render on LOOK. They do
  not change harvest or signaling.
- Myth scars have no domain (`economic` / `social` / `territorial` only) and
  no producer.

The Deep Time papers above sharpen concordance, not acceptance. Path
dependence, cultural attractors, and unsupported-belief fixation describe
tails the hosted world already computes or leaves empty. They do not describe
the five RFC-0001 constructs, and they do not move RFC-0001 out of Draft.

What this suggests, all within existing contracts:

- offline fixtures that pin current LOOK / WATCH behaviour for
  `path_dependence_index`, lore-attractor labels, and the absent myth
  producer;
- a concordance that keeps RFC-0001 in `phenomena-ontology/0.1` and Deep Time
  tails in Slice H, with no shared field;
- no tail RFC this pass.

Do not accept RFC-0001. Do not host SPEC-FREEZE Slice D (Frontier NOTICE):
enrolment is still zero, and `noema doctor` against production reports
`credential: missing` (Specs #283 / remaining-work).

Not in this slice: live Genesis, v0.8 acceptance, a myth producer, or lore
that rewrites the ledger.

## Slice B — Wasserstein / Ollivier / live cultural-generation stay deferred

**Existing authority:**
[REMAINING-WORK-2026-08-21-worker-pin.md](REMAINING-WORK-2026-08-21-worker-pin.md)
(deferred-research table), [SEMANTIC-EVOLUTION-SPEC.md](SEMANTIC-EVOLUTION-SPEC.md)
(deferred table), [ECONOMY-EWM-SPEC.md](ECONOMY-EWM-SPEC.md),
[EMERGENT-CULTURE.md](EMERGENT-CULTURE.md),
[GC9-S2-INHERITANCE-SCHISM.md](GC9-S2-INHERITANCE-SCHISM.md),
[LORE-BOUNDARY.md](LORE-BOUNDARY.md),
[RFC-0125](../rfcs/RFC-0125-practice-inheritance-and-schism.md),
and RFC-0001 (which does not mention culture, Wasserstein, or Ollivier).

**OBSERVED.** Remaining-work and the Semantic Evolution pin both keep
Wasserstein / Ollivier and live cultural-generation inert. Forman–Ricci
`cascading_risk` is the shipped p5-04 metric and is WATCH-banned. Hosted
culture is GC9-derived custom / tradition / schism on existing verbs, not a
generator. RFC-0001 does not mention culture, Wasserstein, or Ollivier.
`players_present: 0`, so any generated culture would be authored, not
ledgered. The closed catalog is `event-catalog/0.2`. Lore may interpret; it
must never rewrite the ledger.

The OT / Ollivier / cultural-benchmark papers above sharpen a later Lab
shape, not a live swap. Held-out OT, unbalanced mass, Ricci-flow, and
story/culture benches all assume a graph or a histogram you already have.
An empty world is `NOT_COMPUTABLE` for those reads.

What this suggests: if an RFC ever exists, it is offline Lab fixtures only —

- histogram support and graph weights declared in the fixture;
- empty-world `NOT_COMPUTABLE`;
- no live metric swap for Forman–Ricci;
- no new verbs or events;
- no WATCH leak of Wasserstein, Ollivier, or `image_score`.

Not in this slice: a hosted generator, a Forman swap, WED / ATTEST invention,
or `CULTURE_*` events.

## Slice C — `forbidden_in_projection` is per-view, not a global deny-list

**Existing authority:** the sixteen slice catalogs that already carry
`forbidden_in_projection` (GC3 social-memory, GC5 communication, GC6
discovery / reconstruction, GC7 conflict, GC9 culture),
[SPECTATOR.md](SPECTATOR.md),
[`spectator-projection.schema.json`](../specs/spectator-projection.schema.json)
(`visibility`: `public` / `authenticated` / `agent_pov` / `research`),
[WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §7,
[WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) §1.1,
[RFC-0126](../rfcs/RFC-0126-watch-entity-update-exposure.md),
and Noema #539.

**OBSERVED.** Noema #539 asserts thirteen `FORBIDDEN_GLOBAL` tokens
(`hitpoints`, `known_truth`, `oracle`, `deity`, `devotion`, `heresy`,
`truth_probability`, `rumor_score`, `culture score`, `mystery solved`,
`the answer`, `you are wrong`, `the ledger is wrong`). Twenty-one leftovers
stay `NOT_YET_SCOPED` because LOOK `reputation_summary` and WATCH
`entity_id` are legitimate. SPECTATOR is already per-`projection_id`.
Substring match false-positives (`stock` versus the live line `Stocks
recovered`) are why a global assert on leftovers is wrong.

The view papers above sharpen the same split the catalogs already imply. A
schema-valid payload can still be the wrong surface. Policy belongs on the
view: LOOK, WATCH, AGENT_POV, WORLD_REPORT. Default DENY. No new verb. No
new WATCH line.

What this suggests: a later RFC would be per-slice
`{LOOK, WATCH, AGENT_POV, WORLD_REPORT} × {allow, deny}`, default DENY.
Without that RFC, keep the 13 / 21 split. Do not global-assert the leftovers.

Not in this slice: a schema change, a global-assert of leftovers, or new
WATCH lines.

## Slice D — Harness and official client

**Existing authority:** [AGENT-HARNESS.md](AGENT-HARNESS.md),
[AGENT-INTERFACE.md](AGENT-INTERFACE.md), [OBSERVATION.md](OBSERVATION.md),
[WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md),
[OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md),
[RFC-0111](../rfcs/RFC-0111-agent-harness.md),
[RFC-0116](../rfcs/RFC-0116-official-agent-client.md),
[SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md) Semantic Evolution chrome,
[SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) Slice C
(`noema-client==0.1.15` re-verified against production), and remaining-work
official-client chrome notes plus Specs #283 (`noema doctor` versus the pin).

**OBSERVED** from remaining-work. Official-client LOOK chrome already renders
scars, `lore_attractors`, and `protocol_strength`. 0.1.15 also renders
`reputation_summary` and `active_norms`. WATCH public bands must not show
`path_dependence_index`, `cascading_risk`, `stock_velocity`,
`scar_persistence`, `reputation_summary`, or `image_score`.

The projection papers above sharpen chrome, not protocol. A renderer can
echo a lawful LOOK field and still leak if it invents a WATCH line. Schema
validity is not a view grant.

What this suggests for the harness:

- agent traces and LOOK payloads may carry those LOOK fields;
- harness docs should say which fields are self-only and which are public;
- claim labels stay on every derived score;
- the harness must not treat `lore_attractors` as physics or
  `path_dependence_index` as a cost;
- the harness must not invent WATCH chrome for banned scalars.

What this suggests for the official client
(`scrimshawlife-ctrl/noema-client`, pin `0.1.15`):

- chrome is a renderer of LOOK, not a second truth;
- do not add chrome for Wasserstein, Ollivier, `cascading_risk`, or
  `image_score`;
- do not hide lawful LOOK `reputation_summary`;
- do not surface WATCH entity internals beyond the public room list;
- verify with `noema doctor` against production; do not trust the pin
  (Specs #283);
- the client pin stays `0.1.15`; this note does not bump PyPI or retarget
  `hosted_live`.

Production systems stay docs and pin only. No secrets in fixtures. No
migrations. Fail closed.

Not in this slice: a client release, a harness protocol verb, a new LOOK
field, a new WATCH line, or publishing the Worker.

## What this note does not do

It proposes no runtime work. It drafts no RFC text. It does not accept
RFC-0001. It does not host SPEC-FREEZE Slice D. It does not produce
`CRIME_DETECTED`. It does not publish a Worker. It does not open
`event-catalog/0.3`. Each slice names existing authorities and the questions
the research sharpens; anything that changes a contract needs its own RFC,
and anything that changes public exposure needs an exposure decision under
the rule [RFC-0126](../rfcs/RFC-0126-watch-entity-update-exposure.md)
established.
