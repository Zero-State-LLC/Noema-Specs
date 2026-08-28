# Crime Producer Research Seed (RFC-0002 Completion)

**Status:** Research input / design seed. Draft. Design note only. No contract, catalog, verb, or exposure change.

**Parent authorities (do not duplicate or fork):**
- [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) (Accepted) — already defines `CRIME_DETECTED` as a detection event (not automatic guilt).
- [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)
- [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7 / strategic depth + crime as consequence layer)
- [RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md](RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md) (primary arXiv signals)

**Gap statement:** RFC-0002 provides the *event* and some detection language ("Detection requires witness, sensor (condition ≥ 50), investigation, or self-report"). The **producer** side — how play actually generates `CRIME_DETECTED` (sensors, witnesses, delays, reports, investigation mechanics, graduated effects, interaction with existing contestation) — remains the open PARTIAL for full completion. No silent producer in runtime or later slices.

## Key external signals (arXiv distillations)

From the 2026-08-27 assimilation:

- **Crime hotspot dynamics in residential burglary models with police response** (arXiv:2605.17709v1)
  - Agent-based + mean-field PDE model with *delayed* crime-information feedback.
  - Delays cause Hopf bifurcations → sustained oscillations, moving/splitting/merging hotspots.
  - Timely access to crime data is more important for stabilization than raw police/guardian density.
  - Relevance: Models delayed detection, attractiveness/condition dynamics (ties to Noema REPAIR/infrastructure), and guardian response as a third actor.

- **Research Vision: Multi-Agent Path Planning for Cops And Robbers Via Reactive Synthesis** (arXiv:2503.11475)
  - Formal LTL + coordination synthesis for pursuit/evasion realizability.
  - Relevance: Potential for bounded, verifiable contest/crime resolution strategies.

Supporting signals noted in prior work:
- Predictive enforcement as endogenous bandit/inspection games (enforcement itself generates the data used for prediction).
- Target–offender–guardian reaction–advection–diffusion models (thresholds, pattern formation, guardian mobility as tipping points).

## Proposed research framing for a future producer authority

Do not invent new world truth. Build on RFC-0002 constraints:
- `CRIME_DETECTED` is detection only; no automatic guilt or permanent removal.
- Graduated consequences.
- Partial observability.
- Pure reducers for the event itself.

Candidate producer dimensions (to be settled in a later spec/RFC, never here):
1. **Sensors** — condition thresholds, infrastructure state, or dedicated sensor actions that can raise a public or restricted `CRIME_DETECTED`.
2. **Witnesses** — player or agent presence + reporting mechanics (self-report, third-party report). Rules for copies-as-witnesses (already constrained in other RFCs).
3. **Investigation / delayed revelation** — time-bounded or evidence-gated paths that can surface past actions as `CRIME_DETECTED`.
4. **Interaction with contestation** — how `CONTEST_RESOLVED`, `AGREEMENT_BROKEN`, or other events feed or trigger detection without duplicating logic.
5. **Delays and observability** — explicit modeling of information latency (aligns with hotspot paper and existing relay/delay patterns in GC5).
6. **Effects on social memory** — public `CRIME_DETECTED` already feeds danger/deceptive edges (see RFC-0022, RFC-0038); private or restricted detections must not leak.

Cross-cutting constraints (inherit, do not restate):
- Complexity doctrine A–J.
- Research/game membrane (detection mechanics are not Player "quests").
- No permanent character death or unwinnable spirals.
- World truth independent of belief.
- Existing `event-catalog/0.2` only (no 0.3).

## Smallest viable next steps (recommended order)

1. Produce a bounded producer authority doc (e.g. extension to STRATEGIC-CONFLICT or a dedicated CRIME-PRODUCER.md) that names the witness/sensor/investigation flows and their coupling to `CRIME_DETECTED`.
2. Define minimal fixtures for detection generation (distinct from existing contest fixtures).
3. Ensure all producer logic writes to Deep Time / social memory where appropriate and respects leak-forbidden rules.
4. Validate against existing S0–S7 social memory slices (no breaking of accepted GC3 behavior).

## Out of scope for this seed

- New event types.
- WATCH or report surface changes (already partially addressed in other RFCs).
- Full implementation or conformance suite.
- Opening v0.8 Phenomena.

These signals are research inputs only. They do not establish NOEMA behaviour.

**Citations / provenance**
- Primary: RFC-0002, STRATEGIC-CONFLICT.md, GAME-COMPLETENESS-PLAN.md GC sections.
- arXiv signals via RESEARCH-ASSIMILATION-2026-08-27-ARXIV-DISTILLATIONS-GC-GAPS.md.
- Additional constraints from RFC-0022, RFC-0034–0038, RFC-0127, and validation rules around `CRIME_DETECTED`.

This seed is now part of the canonical record for completing the crime producer side of RFC-0002.