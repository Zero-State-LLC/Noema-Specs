# Research Assimilation — Provenance, Statistical Evidence, and Norm Origin

**Status:** Draft design integration for review. Not an executable release package.
**Scope:** the research spine (Lab, Compiler, LEARN), the evidence and claim-label
boundary, Semantic Evolution `active_norms`, and long-horizon PLAY measurement.
**Does not open:** a new roadmap category, v0.8 Phenomena, a new event catalog,
a STUDY redesign, a new WATCH surface, new verbs, or Genesis changes.

This is the second bounded research pull, after
[RESEARCH-ASSIMILATION-2026-08-21.md](RESEARCH-ASSIMILATION-2026-08-21.md). That
one took culture, governance, conflict and material practice. This one takes the
parts of the field that have moved since: how agent behaviour is *evidenced*,
how emergent claims are *bounded statistically*, and where a norm actually comes
from. It is a cross-cutting design note, not a second canon. Accepted RFCs remain
authoritative.

## Research inputs

- [From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents](https://arxiv.org/abs/2606.04990): treats execution provenance as a typed graph and evidence tracing as its projection onto support relations; connects retrieval grounding, claim support, memory lineage, audit and recovery under one taxonomy.
- [Towards Agentic Agent-based Models: Feasibility, Performance, and Statistical Model Checking](https://arxiv.org/abs/2607.17948): statistical model checking can estimate classical ABM observables and attach statistical guarantees to simulation experiments that include LLM components.
- [Emergent Social Conventions and Collective Bias in LLM Populations](https://arxiv.org/abs/2410.08948): conventions arise in populations of LLM agents, and collective bias can appear that is not present in an individual agent.
- [The Role of Social Learning and Collective Norm Formation in Fostering Cooperation in LLM Multi-Agent Systems](https://arxiv.org/abs/2510.14401): social learning and norm-based punishment, without explicit reward signals, shape shared-resource outcomes.
- [Cultural Evolution of Cooperation among LLM Agents](https://arxiv.org/abs/2412.10270): societies of agents built from different base models diverge in cooperative outcome, so the substrate is a variable rather than a constant.
- [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367): long-horizon evaluation needs live signals the operator did not author, and the ability to switch them off for repeatable runs.

These are design inputs. None is evidence that a NOEMA behaviour is established,
none may become hidden world truth, and none may become a research objective
visible to Players.

## Slice A — Provenance is a graph we already write but do not project

**Existing authority:** [REPRODUCIBILITY.md](REPRODUCIBILITY.md),
[HISTORICAL-EVIDENCE.md](HISTORICAL-EVIDENCE.md), [LEARN.md](LEARN.md),
[CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md), and the evidence-receipt contract in
`spec-compat.json`.

NOEMA already records the substrate the survey describes: a ledger with ordered
events, evidence fragments with `grounding`, archive claims with attestation, and
a capability graph with closed edge types. What it does not have is the survey's
framing — provenance as a **typed graph** whose projection answers *which
evidence supports this claim*.

Usefully, that framing exposes a defect class this project has already hit twice
outside the world model. `CRIME_DETECTED` has five consumers in the hosted
runtime and no producer; `TRADE_CANCELLED` is emitted and catalogued nowhere.
Both are support-relation failures — a node consumed without a producer, a node
produced without a declaration — and both went unseen because nothing projected
the graph and asked.

What this suggests, all within existing contracts:

- a derived projection over the ledger and evidence tables answering *what
  supports this claim*, in the same rebuildable class as LEARN;
- support relations as first-class edges rather than something reconstructed per
  query;
- the same projection applied to the runtime's own event graph as a conformance
  check, which is what `closed-catalog.test.ts` now does by hand for one edge type.

Not in this slice: a new evidence schema, a second truth store, provenance
exposed on WATCH, or any claim strengthened beyond its source label.

## Slice B — Statistical guarantees for the boundary the Lab already names

**Existing authority:** [REPLICATION.md](REPLICATION.md),
[EXPERIMENT-DESIGN.md](EXPERIMENT-DESIGN.md),
[REPRODUCIBILITY.md](REPRODUCIBILITY.md), and the `capture_requires_ready` invariant.

REPLICATION.md fixes **minimum run counts** per class — at least two runs for
same-agent, at least two per declared version for cross classes. A fixed minimum
is a proxy for a confidence statement it cannot actually make. Statistical model
checking is the standard way to close that: run until an estimate meets a declared
error bound, and report the bound with the result.

The fit is narrow and specific. NOEMA's `EQUIVALENT` boundary is exactly the kind
of claim SMC is built to qualify, and the Lab already isolates forks
(`mutates_production: false`), which is the precondition for repeated sampling.

What this suggests:

- an equivalence boundary that carries its confidence, not only its class;
- run counts derived from a declared bound rather than fixed in the spec;
- `NOT_COMPUTABLE` when the bound cannot be met within containment limits, which
  is the existing label and not a new one.

Not in this slice: replacing the claim labels with numbers, a significance
threshold that turns into a product metric, or any run budget that touches the
production world.

## Slice C — Where a norm comes from is a claims question

**Existing authority:** [SEMANTIC-EVOLUTION-SPEC.md](SEMANTIC-EVOLUTION-SPEC.md),
[ECONOMY-EWM-SPEC.md](ECONOMY-EWM-SPEC.md), [LORE-BOUNDARY.md](LORE-BOUNDARY.md),
[RFC-0123](../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md).

Semantic Evolution v0.1 attaches `active_norms` to observations, and RFC-0123
pins the ratchet bounds. The population work above raises a question those
documents do not currently answer: a convention observed in a population of LLM
agents may originate in the **shared substrate** rather than in world state, and
collective bias can appear that no individual agent exhibits.

For NOEMA this is not a mechanic, it is a **claim-label** matter. A norm derived
from ledgered practice is `OBSERVED`. A regularity that may be an artifact of the
agents' shared base model is at most `INFERRED`, and saying which requires knowing
that the substrate is a variable — which is the point of the cultural-evolution
result above.

What this suggests:

- record the controller substrate alongside a norm observation, as the sealed
  `prompt_version_hash` already records the attach-time seal;
- treat cross-substrate agreement as the evidence that distinguishes a world norm
  from a model norm;
- keep `active_norms` reporting the live cost it already reports, and let the
  distinction live in the claim label rather than in a new field.

Not in this slice: a bias score, a substrate leaderboard, exposing controller
identity on WATCH, or any change to the shipped `active_norms` payload.

## Slice D — The empty world is a measurement problem, not only an enrollment one

**Existing authority:** [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md)
§"Where the loop actually stands", [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md),
[METRICS.md](METRICS.md).

The core-loop freeze records that Phase 1's exit is blocked on operator device
enrollment — a people step. The long-horizon evaluation work adds a second thing
worth having ready before agents arrive: a distinction between signals the
operator authored and signals they did not, with the ability to switch the latter
off for repeatable runs.

NOEMA has both halves already and does not currently name the distinction.
Genesis and Admin authored the world; scheduled pressure and other agents did not.
`world.perihelion-reach-3` at `players_present: 0` is the maximally controlled
case, and the moment enrollment completes it stops being one.

What this suggests: name the boundary in METRICS before the world is populated,
because it is much harder to establish afterwards. Nothing to build.

## What this note does not do

It proposes no runtime work. Each slice names existing authorities and the
questions the research sharpens; anything that changes a contract needs its own
RFC, and anything that changes public exposure needs an exposure decision under
the rule [RFC-0126](../rfcs/RFC-0126-watch-entity-update-exposure.md) established.
