# Population and Study Readiness — Gate PSR-1 Scenario Contract (compatibility-at-scale)

**Status:** evidence contract for the active Gate. Criteria **locked** (#381; Danny human-yes on merge, 2026-10-31). **BLOCKED on prerequisites:** official-client pin reconcile and a third-party enrollment path (see [Prerequisites](#prerequisites)). Not a runbook, not a COMPLETE claim, and not authority to deploy.
**Campaign:** [Population and Study Readiness](POPULATION-AND-STUDY-READINESS.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml) (`third_party_agent_compatibility_at_scale: BLOCKED`)
**Decision issues:** [#363](https://github.com/Zero-State-LLC/Noema-Specs/issues/363) (thresholds) · spec [#379](https://github.com/Zero-State-LLC/Noema-Specs/issues/379)
**Suggested candidate:** `psr1-compatibility-at-scale`

PSR-1 proves that NOEMA's live production world sustains a concurrent population of independently controlled Players, reached through **distinct integration paths**, including at least one integration Zero-State did not build or operate. It adds no mechanics, verbs, adapters, or protocol fields. A missing Controller or Gateway surface is an integration or runtime defect, not a reason to widen this contract.

## Why the bar is above Gate B and Gate E

These facts are OBSERVED in the retained packets:

- **Gate B** ([promotion](LCA-GATE-B-PROMOTION-2026-09-08.md)) proved three Controllers, but all ran the same official client binary on one host. Contention was a LOOK-only burst. Its tier was isolated autonomous loops ([independence tiers](LCA2-GATE-B-PREPARATION.md#evidence-tiers)).
- **Gate E** ([promotion](LCA-GATE-E-PROMOTION-2026-09-20.md), [scenario](LCA-GATE-E-SCENARIO.md)) proved about 23 minutes of budgeted churn: ≥3 Controllers, ≥2 remints, ≥1 presence recovery, in-window Path 8, ≥8 consequential acts, Δcycle ≥4.
- **Platform bound:** the Chamber supports 2–10 agents. The Gateway rate-limits per Controller and per Player ([AGENT-GATEWAY.md](AGENT-GATEWAY.md)), but Specs publish no numeric limits.

"Compatibility at scale" was never defined before this contract.

## Prerequisites

A PSR-1 candidate may begin only when all of these are recorded:

- the criteria in this contract are locked (done in #381), and the Campaign record no longer marks PSR-1 BLOCKED;
- the official-client pin is reconciled. `hosted_live.official_client` records `noema-client==0.1.21`, while Gate B OBSERVED 0.1.22. Record the version the run will use; do not invent a flip ([#382](https://github.com/Zero-State-LLC/Noema-Specs/issues/382));
- the run targets the **live production pin** recorded in the current-state record, not an isolated Worker;
- the non-first-party Controller's operator has an authorized enrollment path. Gate F residual #4 recorded that production device enrollment was never completed; if that is still true, it is a prerequisite defect to close, not a waiver ([#383](https://github.com/Zero-State-LLC/Noema-Specs/issues/383));
- planned operator actions, external inputs, remint and Path 8 drills, and the intervention budget are declared during Prep.

## Integration paths (all required)

| # | Integration path | Notes |
|---|---|---|
| 1 | Official client CLI or library | first-party |
| 2 | Official client driven by an OpenAI-compatible model adapter | any provider; first-party code |
| 3 | One non-first-party integration: a Hermes or OpenClaw skill, or a raw REST/WS Controller | must be **built or operated outside Zero-State** (independence tier 3) |

MCP is **excluded** from PSR-1. It isn't built, and building it would be new breadth.

## Floors

| Dimension | Floor |
|---|---|
| Concurrent Controllers (cohort) | **6**, with ≥2 on each of the three integration paths (locked 2026-10-31, #381). Rationale: contention across paths; ≥2 non-first-party Controllers so the tier-3 floor survives one dropout; headroom under the 10-agent Chamber bound while Gateway limits are unpublished. Changing it is a new locking decision with a human-yes, never an in-run adjustment. |
| Tier-3 Controllers | ≥1 |
| JWT remint or session rebind | ≥2 full cycles |
| Presence dropout recover | ≥1 |
| In-window Path 8 recover | ≥1, PRE heads equal POST heads |
| Deep Time progress | Δcycle ≥12 |
| Consequential acts | ≥3 per Controller |
| Wall clock | **none.** Elapsed idle time is never a pass ([Gate E precedent](LCA-GATE-E-SCENARIO.md)) |

## Required receipts

- The full Gate B receipt set (per-Controller ICR and binding digest, cohort contention, ordering, and budget digests, reconnect) and the full Gate E receipt set (remint and presence receipts, Path 8 recover JSON, labeled census windows, intervention log).
- **Per-Controller row:** Controller id, Player id, integration path, client or adapter version, operator class (first-party or tier 3), and a decision-context hash.
- **Cross-path contention:** at least one contention digest where Controllers on different integration paths issue **consequential** actions against shared targets, not only LOOK.
- **Observed Gateway limits:** the rate-limit responses and budgets observed during the run, recorded as **evidence**, not as a new contract.

## Honest marking

- Dedicated recovery-receipt objects stay **NOT_COMPUTABLE** (carried forward; not invented).
- `/ready` player counts are weak public counts, never the census.
- A Controller whose decision context is shared with another is excluded from the cohort count and marked.
- Missing values are `NOT_COMPUTABLE` with a reason. They are never filled from a different run.

## Evidence pack

Use the [evidence-pack structure](LCA-EVIDENCE-PACK-STRUCTURE.md) under Noema `docs/evidence/psr1-<date>/`: `INDEX.md`, the candidate declaration, per-action receipts, digests, the per-Controller table, the intervention log, and labels (DECLARED / PASS / NOT_COMPUTABLE / WAIVED / SUPERSEDED). A Specs promotion packet links to it.

## Exit

PSR-1 is COMPLETE only when a promotion packet satisfies every floor and receipt above and Danny gives a human-yes. Only then may `third_party_agent_compatibility_at_scale` leave BLOCKED.

## Needs an RFC (out of this contract)

Building MCP or any new adapter as a requirement; publishing numeric Gateway limits as a contract; any protocol, schema, or Player-verb change.

## Non-goals

Hosted STUDY (that is [PSR-2](PSR-2-STUDY-READINESS-SCENARIO.md)); Deploy or pin change; WORLD_CUTOVER; anything on the Campaign's deferred list.
