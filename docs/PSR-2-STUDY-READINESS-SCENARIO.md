# Population and Study Readiness — Gate PSR-2 Scenario Contract (hosted STUDY evidence readiness)

**Status:** evidence contract for an unproven Gate. **BLOCKED** until PSR-1 is COMPLETE and every `TO LOCK` / `TO NAME` value below is locked by Danny human-yes. Not a runbook, not a COMPLETE claim, not a STUDY reopen, and not authority to deploy.
**Campaign:** [Population and Study Readiness](POPULATION-AND-STUDY-READINESS.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml) (`hosted_study_pipeline: BLOCKED`, `surfaces.study_hosted: BLOCKED`)
**Decision issues:** [#362](https://github.com/Zero-State-LLC/Noema-Specs/issues/362) (gate definition) · spec [#379](https://github.com/Zero-State-LLC/Noema-Specs/issues/379)
**Groundwork (authoritative; completed here, not replaced):** [STUDY reopen companion](LCA-STUDY-REOPEN-COMPANION.md) · [STUDY readiness audit](STUDY-READINESS-AUDIT-2026-09-21.md) (gaps G1–G9) · [live scorecard](LCA-STUDY-REOPEN-LIVE-SCORECARD-2026-09-21.md)
**Suggested candidate:** `psr2-study-evidence-readiness`

PSR-2 proves that hosted STUDY is **ready to host**: real natural play exists, its Observations are research-eligible, and the offline research spine can turn them into a candidate and a reproducibility bundle. It does **not** host STUDY. It adds no routes, schemas, Deploy, or RFC.

## Prerequisites

- **PSR-1 COMPLETE.** Its population is what produces natural play.
- Every `TO LOCK` and `TO NAME` value below is locked.
- The research and ethics steward has accepted the role and signed the consent and opt-in basis for the third-party Players in the window.

## Natural-play window

| Requirement | Value |
|---|---|
| Timing | Separate from, and after, the PSR-1 run. PSR-1's deliberate interventions (remints, Path 8) never count as natural play. |
| Independence | Meets the strongest [Gate B independence tier](LCA2-GATE-B-PREPARATION.md#evidence-tiers): independently operated Controllers, distinct decision contexts, no shared planner. |
| Interventions | None that script the outcome; any such intervention fails the window ([Gate E rule](LCA-GATE-E-SCENARIO.md)). Bounded, logged operator actions are allowed and marked. |
| Window length | **TO LOCK** |

## Evidence floors

| Evidence | Floor |
|---|---|
| Research-eligible Observations from the window | **K = TO LOCK**, each with `consent_basis`, provenance, and `exclusions` intact and `research_eligible: true` ([OBSERVATION.md](OBSERVATION.md); eligibility is not proof of a claim) |
| Offline candidate dossiers (Frontier/Observatory) built from the window | **N = TO LOCK** (≥1) |
| Dry-run reproducibility bundle | 1, from the window, validating against the existing reproducibility-bundle schema |

These close audit gaps **G1** (natural multi-agent population) and **G2** (evidence-readiness receipt). Gaps **G5–G9** (hosted NOTICE/Lab routes, hosted isolation, offline↔hosted equivalence, Deploy) stay **out of scope** and are carried to the separate hosting RFC.

## Owners

| Role | Owner |
|---|---|
| Criteria and human-yes | Danny |
| Research and ethics steward: consent and opt-in, eligibility ledger, retention, and release sign-off | **TO NAME** |
| Runtime receipts | Prabu / Noema Admin |

## Evidence pack

Use the [evidence-pack structure](LCA-EVIDENCE-PACK-STRUCTURE.md) under Noema `docs/evidence/psr2-<date>/`: `INDEX.md`, the candidate declaration, the intervention log, cohort receipts (reusing the PSR-1 rows where unchanged), and an **eligibility ledger**. The ledger counts Observations by `consent_basis`, `research_eligible`, and `exclusions`. It is a documentation artifact that cites existing Observation fields, not a new schema. The pack also includes the offline Frontier/Observatory audit chain, the bundle digest, and a Specs promotion packet.

## Honest marking

- Missing values are `NOT_COMPUTABLE` with a reason; nothing is filled from PSR-1 or offline runs.
- Telemetry without provenance, consent, schema validation, exclusion policy, and eligibility is not evidence.
- Every failed or absent control is reported ([research ethics](../research/research-ethics.md), [experimental controls](../research/experimental-controls.md)).

## Exit

PSR-2 is COMPLETE only when a promotion packet satisfies every floor above and Danny gives a human-yes. Then `hosted_study_pipeline` moves **BLOCKED → NEXT**. `surfaces.study_hosted` **stays BLOCKED** until a separate RFC defines hosted research routes and their isolation.

## Needs an RFC (out of this contract)

Hosted research routes; any new or extended schema, including an eligibility-ledger schema or consent-field change; any change to the consent, research-export, or claims boundary.

## Non-goals

Hosting STUDY; Deploy or pin change; offline↔hosted digest equivalence; anything on the Campaign's deferred list.
