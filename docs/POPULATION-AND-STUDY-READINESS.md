# Population and Study Readiness

**Status:** ACTIVE_INTEGRATION Campaign. Opened by the #361 direction packet; human-yes is the owner's confirmation and merge of #378 (2026-10-31).
**Campaign id:** `population-and-study-readiness` (confirmed at merge, 2026-10-31).
**Supersedes:** [Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md) "no further Living Alpha gate; no LCA-6" guidance. Living Alpha is closed with Gates A–F COMPLETE; its packets are not rewritten.
**Owns:** near-term sequencing for the two BLOCKED integration edges.
**Does not own:** Player ontology, action semantics, Genesis, claim policy, frozen world truth, or any Gate's acceptance thresholds (those belong to the decision issues named below).

Related: [ROADMAP.md](ROADMAP.md) · [`current-state.v1.yaml`](../specs/current-state.v1.yaml) · [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md) · [LCA-GATE-F-PROMOTION-2026-09-21.md](LCA-GATE-F-PROMOTION-2026-09-21.md) · [GLOSSARY.md](../GLOSSARY.md) (Campaign, Gate, Successor decision)

## Outcome

> Prove that NOEMA sustains a population of independent third-party agents, then prove that the natural play it produces is ready to be studied on the hosted platform.

This Campaign is not breadth. It closes the only two unproven integration edges in the current-state record, in evidence order.

## Why this order

Under the [future-work admission rule](DIRECTION-AUTHORITY.md#future-work-admission), work is authorized only when it closes the earliest unproven integration edge. After Gate F, the record names two BLOCKED capabilities:

| Capability | Blocker (OBSERVED in current-state) |
|---|---|
| `third_party_agent_compatibility_at_scale` | multi-agent endurance and adapter evidence |
| `hosted_study_pipeline` | production-like natural-play and evidence-readiness gate |

Hosted STUDY needs production-like natural play. A sustained multi-agent population is what produces it. Compatibility-at-scale is therefore the earlier edge (INFERRED from the two blockers), and it comes first.

## Gates

| Gate | Milestone | Closes | Scenario contract | Criteria owner | State |
|---|---|---|---|---|---|
| **PSR-1: Compatibility at scale** | PSR-1 | `third_party_agent_compatibility_at_scale` | [PSR-1-COMPATIBILITY-AT-SCALE-SCENARIO.md](PSR-1-COMPATIBILITY-AT-SCALE-SCENARIO.md) | [#363](https://github.com/Zero-State-LLC/Noema-Specs/issues/363) | Active; criteria locked (#381); BLOCKED on prerequisite: third-party enrollment (#383); client pin resolved (#382) |
| **PSR-2: Hosted STUDY evidence readiness** | PSR-2 | `hosted_study_pipeline` | [PSR-2-STUDY-READINESS-SCENARIO.md](PSR-2-STUDY-READINESS-SCENARIO.md) | [#362](https://github.com/Zero-State-LLC/Noema-Specs/issues/362) | Unproven; window, K, and N locked (#381); waits for PSR-1 and a named research and ethics steward |

Milestone ids `PSR-1` and `PSR-2` are confirmed. They deliberately do not extend Living Alpha's `LCA-*` numbering.

**Criteria live in each scenario contract (#379).** Values without evidence are written `TO LOCK` (or `TO NAME` for an owner). The direction validator keeps a Gate BLOCKED while its contract still contains them. Each Gate's acceptance thresholds (for PSR-1: adapters covered, cohort size, duration, receipts; for PSR-2: acceptance criteria, evidence pack, owner) are human decisions owned by its issue. Until that issue records them, the Gate is BLOCKED, and no evidence run may start against invented criteria. Gates may reuse the Gate B (external population) and Gate E (endurance) evidence shapes where they fit.

## Exit criteria

- **PSR-1 COMPLETE** when a promotion packet satisfies the criteria recorded on #363, with Danny human-yes. Only then may `third_party_agent_compatibility_at_scale` leave BLOCKED.
- **PSR-2 COMPLETE** when a promotion packet satisfies the gate defined on #362, with Danny human-yes. Only then may `hosted_study_pipeline` and the `study_hosted` surface leave BLOCKED.
- **Campaign closes** when both Gates are COMPLETE, or by an explicit superseding direction packet.

## Direction metadata

Required by [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md#required-metadata-for-direction-work).

| Field | Value |
|---|---|
| Existing implementation and evidence commit | Advanced Worker evidence `61234cc`; live Worker `86978241-3983-4075-b289-fa28f9e75c46` from source `565ccc1595c89f992110808401e147b7692b2735`; Gate F COMPLETE evidence Worker `1e52e827` / `65086d32` ([LCA-GATE-F-PROMOTION-2026-09-21.md](LCA-GATE-F-PROMOTION-2026-09-21.md)) |
| Status and scope | ACTIVE_INTEGRATION. Integration and evidence only. No new semantics. |
| Authorities it depends on | Accepted RFCs and ADRs (including RFC-0120 agent-only identity); [CONTEXT.md](../CONTEXT.md) Platform; [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md); the frozen hosted alpha boundary; Gate B and Gate E evidence-pack shapes |
| Authorities it does not replace | All of the above. Planning chooses when work occurs; it does not change normative semantics. |
| Production-alpha delta | **None at opening.** No Deploy, no pin change, no WORLD_CUTOVER. |
| Current-state entries affected | `active_campaign` (new Campaign); `completed_campaigns` (Living Alpha); `authority.active_campaign`; `capabilities.spark_orin_nvidia_stack` (SPECULATIVE). `third_party_agent_compatibility_at_scale` and `hosted_study_pipeline` stay BLOCKED; `external_crypto_economy` stays DEFERRED. |
| Acceptance or exit gate | PSR-1, then PSR-2 (see [Exit criteria](#exit-criteria)) |
| Blockers | #363 criteria (PSR-1); #362 gate definition (PSR-2) |
| Non-goals | Everything on the [deferred list](#explicitly-deferred); RFC-0130; any protocol, schema, or Player-verb change; Deploy; WORLD_CUTOVER; promoting spec 014 |
| Superseded direction | Living Alpha's "no further Living Alpha gate; no LCA-6" (live guidance only; history kept) |

## Explicitly deferred

Unchanged from Living Alpha. Opening this Campaign does not admit:

- new canonical Player verbs;
- new GC breadth not already implemented;
- external crypto settlement, wallets, token minting, or x402;
- v0.8 Phenomena implementation;
- new Genesis Profiles, Story Seeds, or live room-bound expansion;
- multi-world orchestration;
- infrastructure justified only by hypothetical scale.

## Speculative directions

[Spec 014: Spark + Orin Nano NVIDIA stack](../specs/014-spark-orin-nvidia-stack/spec.md) is SPECULATIVE: direction without implementation authority, scoped to a local or offline research topology. It does not change the hosted Platform and is not part of this Campaign.

## Work admission

A task enters this Campaign only when it names the Gate it advances, the capability edge it exercises, its observable acceptance, and confirms it does not widen a freeze. A task that cannot name a Gate remains an idea.
