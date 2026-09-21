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

## Extension Points

Non-normative research and fixture-design seams; this seed does not authorize a producer or turn detection into adjudicated guilt.

- **Seam:** extend witness, sensor, self-report, and delayed-investigation hypotheses with bounded input/output examples, evidence provenance, duplicate-report handling, and an explicit account of when detection is withheld. Keep external hotspot and pursuit models as comparison hypotheses rather than imported algorithms or new actions.
- **Retained invariants:** preserve RFC-0002's detection/consequence distinction, partial observability, pure event reduction, graduated consequences, and existing catalog scope. Only agents are Players under RFC-0120; a human platform role is not an additional witness-Player category. Restricted evidence does not become WATCH or research access permission.
- **Compatibility/promotion:** [RFC-0129](../rfcs/RFC-0129-crime-detected-payload-reconciliation.md) already accepts optional `victim_id` and `visibility` in event-catalog/0.2, with no visibility default. A public producer record pairs `visibility: PUBLIC` with `PUBLIC_HISTORY` in both directions. That payload reconciliation does not settle detection algorithms, jurisdiction, costs, or producer activation; use [the gap register](SPEC-GAP-REGISTER-2026-08-25.md) and a separately accepted producer contract for those decisions.
- **Proposed checks:** cover unnamed victims (no dyadic victim edge), omitted visibility (no implicit public grant), restricted records, paired public markers, and invalid one-sided public markers. Compare the same admissible public fixture across social memory, world reports, and WATCH; add replay, duplicate-report, sensor-threshold, and delayed-evidence cases only against a pinned producer rule. These are future checks, not results from this seed.

## Appendix — Complementary research feed 2026-09-12 (OBSERVED / INFERRED)

**Status:** Research overlay only. Does not change contracts, catalog, verbs, events, Genesis, WATCH, or producer activation.
**Companion Notion:** https://app.notion.com/p/3d93e8ba2f5c81b7822ae7f4f8fb807f
**Mosca ingest Notion:** https://app.notion.com/p/3d93e8ba2f5c814b8878ffe490f275c2

### Sources fetched (OBSERVED)

| Source | URL |
| --- | --- |
| Mancur Olson, *Dictatorship, Democracy, and Development*, APSR 87(3) 1993 | https://doi.org/10.2307/2938736 · PDF https://neoconomica.org/userfiles/files/olson.pdf |
| Charles Tilly, *War Making and State Making as Organized Crime* | https://theanarchistlibrary.org/library/charles-tilly-war-making-and-state-making-as-organized-crime · DOI https://doi.org/10.1017/cbo9780511628283.008 |
| Diego Gambetta, *The Sicilian Mafia* (HUP) + 20-years-after note | https://www.hup.harvard.edu/books/9780674807426 · https://diegogambetta.org/wp-content/uploads/2022/06/sicilian_mafia_20_years_after_publication.pdf |
| Stafford Beer VSM / algedonic (high-level secondary) | https://en.wikipedia.org/wiki/Viable_System_Model · https://vsmg.lrc.org.uk/screen.php?page=6infsys |
| Thomas Schelling focal points / credible commitment (secondary notes) | https://home.uchicago.edu/~rmyerson/research/stratofc_notes.pdf |
| Mosca video captions (prior ingest) | https://youtu.be/Xk5kmFFEYQ8 |

### Compact OBSERVED extracts

- **Olson:** Roving bandits destroy investment incentives; a stationary bandit who monopolizes theft as taxes can lower extract rate and provide order/public goods because of encompassing interest; short tenure → confiscatory (roving-like) behavior.
- **Tilly:** War making and state making are protection rackets with legitimacy; banditry–piracy–gangland–policing–war making form one continuum; four activities: war making, state making, protection, extraction; double-edged “protection” (shelter vs racket).
- **Gambetta:** Mafia as private protection industry exploiting scarce trust; reputation does the work; impostors free-ride on signals; protection provision can reinforce distrust while enabling illicit markets.
- **Beer (high-level):** System 4 = outward intelligence/adaptation; algedonic signals escalate pain/pleasure alerts when performance fails capability.
- **Schelling (bounded):** Focal points coordinate expectations; credible threats often require staking reputation / limiting own future choices.

### INFERRED overlays for existing CRIME-PRODUCER path (no mint)

Tag language only — apply to existing producers / social-memory / institutional surfaces when an accepted producer exists:

1. `stationary` / `roving` — horizon + encompassing interest typology.
2. `protection_market` — private protection as contested service.
3. `moral_buffer` / `algedonic` — spectator/Player outrage soft regulator (SIGNAL-adjacent).
4. `s4_capture` — observation/intel ownership risk (WATCH/report consumers).
5. `double_extract` — stacked official + extralegal costs in contested zones.
6. `legitimation` — predation seeking charter/respectable form.

### Locks (reaffirm)

- No new verbs, events, `event-catalog/0.3`, Genesis, or WATCH changes from this appendix.
- Assimilation pin stands: organized crime remains **DEFER** until the first detection loop exists ([RESEARCH-ASSIMILATION-2026-08-25-CRIME.md](RESEARCH-ASSIMILATION-2026-08-25-CRIME.md)).
- Specs remain authority; Notion is research surface. Human-yes gates Worker publish / RFC mint.
