# Research Assimilation — Crime Detection, Punishment, and Rehabilitation

**Status:** non-normative design input; not an executable release package
**Date:** 2026-08-25
**Scope:** crime detection, adjudication, sanction, exclusion, enforcement cost, witnesses, sensors, and rehabilitation
**Does not open:** new Player verbs, a `CRIME_DETECTED` producer, `event-catalog/0.3`, Genesis changes, scalar reputation, combat stats, organized-crime mechanics, or any numeric retune of the published sanction ladder

This note follows the bounded pattern of [Research Assimilation — 2026-08-25 (LCA gaps)](RESEARCH-ASSIMILATION-2026-08-25-LCA-GAPS.md) and [2026-08-24](RESEARCH-ASSIMILATION-2026-08-24.md). Accepted RFCs remain authoritative. Research inputs are design material only. None establishes a NOEMA behavior, becomes hidden world truth, becomes a Player reward, or supports a consciousness claim.

The reviewed input is an external arXiv review of the crime mechanic dated 2026-08-25. Its research synthesis is assimilated below. Its spec/runtime findings were re-verified against this repository and the hosted Worker before assimilation; three required correction and are recorded in [Corrections](#corrections-to-the-reviewed-input).

## Doctrine the research supports

The review's central conclusion is assimilated: **the literature does not ask for harsher crime penalties; it asks for a credible evidence-and-enforcement loop.** Existing NOEMA doctrine already matches the papers on the points that matter most —

```text
unauthorized act ≠ detected crime
detection is evidence-path dependent, not omniscient
unknown stays unknown; private stays private
punishment is graduated and non-terminal
public reputation is evidence-backed, not a global scalar
exclusion is temporary
```

No RFC is amended by this note. Nothing below authorizes a runtime change.

## Input map

| Research input | Concept used | NOEMA disposition | Artifact |
|---|---|---|---|
| [Crime aggregation and witness credibility](https://arxiv.org/abs/2009.06470) | aggregating accusations into one severe sanction degrades witness informativeness | Confirms per-incident `source_event_ids` and distinct detection records; argues against automatic sanction on detection | Gap row `B7c`; no RFC yet |
| [Costly punishment under low detectability](https://arxiv.org/abs/2409.09701) | punish the definitively identified; treat the uncertain generously | Confirms the unauthorized/detected split and the paid Player punishment path in RFC-0123 | No change; doctrine already aligned |
| [Incomplete reputation information and punishment](https://arxiv.org/abs/2509.09181) | missed observation, bad assessment, and failed execution behave differently | Confirms fail-closed privacy and silence on insufficient evidence; a single error model is insufficient | [Detection evidence sketch](research/NOTES-CRIME-DETECTION-EVIDENCE.md) |
| [Cooperation by social exclusion](https://arxiv.org/abs/1211.2838) | exclusion beats fines only while monitoring is cheap | Temporary scoped access restriction is sound; world-administered exclusion needs a monitoring cost | Gap row `B7d` |
| [Corruption and institutional punishment](https://arxiv.org/abs/2202.13104) | punitive institutional power is not monotonically good under capture | `ORG_REVIEW_ELIGIBLE` is a flag, not a governance model; any org sanction needs jurisdiction and conflict-of-interest rules | Gap row `B7d`; relates to existing `B4` |
| [Sustainable institutionalized punishment](https://arxiv.org/abs/1204.3888) | enforcement financing and second-order free riders | The published influence debit is institutionally free; formal enforcement needs a payer | Gap row `B7d` |
| [OCEAN observation-based enforcement](https://arxiv.org/abs/cs/0307012) | first-hand observation beats propagated second-hand reputation | Witnesses, sensors, and event provenance dominate rumor; second-hand reports initiate investigation, never a detection record | [Detection evidence sketch](research/NOTES-CRIME-DETECTION-EVIDENCE.md) |
| [Recipient norms and forgiveness](https://arxiv.org/abs/2405.05903) | forgiveness sustains cooperation; stigma contagion collapses it | Rehabilitation stays; never penalize a Player for interacting with a publicly dangerous Player | Gap row `B7e`; confirms no contagion rule exists today |
| [Punishment and reward on cooperation](https://arxiv.org/abs/2309.00556) | targeted penalties have sharply diminishing returns | Explicit `DEFER` on any retune of the published −3 / −8 / −15 ladder | No artifact; forbidden fill recorded |
| [Criminal organizations exhibit hysteresis](https://arxiv.org/abs/2403.03720) | established criminal networks resist the intervention that would have prevented them | `DEFER`: organized crime targets agreements, routes, offices and coordination, not individual influence | After the first detection loop exists; no RFC now |

## Verified state of the crime mechanic

Re-verified 2026-08-25 against Specs `492ccc9` and Worker `6db6782`.

| Finding | Status | Evidence |
|---|---|---|
| No producer for `CRIME_DETECTED` | **Already documented** | [EVENT-CATALOG-AUDIT.md](EVENT-CATALOG-AUDIT.md) §Five catalogued types. Confirmed: no `pushEvent("CRIME_DETECTED")` anywhere in `workers/noema/src`. `applyContestSuccessFollowOns` emits only `RESOURCE_TRANSFER`, `INFRASTRUCTURE_DISRUPTED`, `ACCESS_RESTRICTED`, `ENTITY_UPDATE`, `MOVE` |
| Detection constants have no algorithm | **Confirmed, and wider** | `detection_base_millipoints` (300/400/500/600) and `sensor_min_condition` (50) appear in [contest-config.v02.json](../specs/contest-config.v02.json) and have **zero referents** in Worker source. They express intent, not behavior |
| Payload cannot carry the memory contract | **Confirmed, and reframed** | See [the payload contradiction](#the-payload-contradiction) — this is a Specs-internal contradiction, not a runtime defect |
| Detection and sanction are conflated | **Confirmed** | RFC-0002 line 60 reads `CRIME_DETECTED` = "Detection occurred (not automatic guilt broadcast)", yet the payload `$def` marks `influence_delta` and `influence_applied` **required** |
| Enforcement is free and unaccountable | **Confirmed** | No enforcement cost, budget, jurisdiction, or steward exists in the crime path. RFC-0123 correctly charges the *Player* path 1 influence |

### The payload contradiction

The reviewed input reports this as schema-versus-runtime. It is not. Two **Accepted** GC3 slice contracts specify the exact fields the closed payload forbids:

| Authority | Requires | `CRIME_DETECTED_payload` |
|---|---|---|
| [GC3-S1-BETRAYAL.md](GC3-S1-BETRAYAL.md) §Evidence | `victim_id` → `subject_id` dyadic credit | no `victim_id` property; `additionalProperties: false` |
| [GC3-S2-WATCH-PUBLIC.md](GC3-S2-WATCH-PUBLIC.md) §Bands | `visibility=PUBLIC` gates the public `dangerous` band | no `visibility` property; `additionalProperties: false` |

The hosted Worker implements the **slice documents** faithfully — `social-memory.ts` requires `victim_id` for the dyadic edge and `visibility === "PUBLIC"` for public danger. The outlier is the catalog payload, which carries `flags: ["PUBLIC_HISTORY"]` instead.

Consequently a schema-valid crime record cannot produce the memory effects its own Accepted slices specify. Consumers are split three ways:

| Consumer | `visibility` | `PUBLIC_HISTORY` | Works with a schema-valid payload |
|---|---|---|---|
| `social-memory.ts` dyadic (`victim_id`) | — | — | **No** |
| `social-memory.ts` public danger | yes | no | **No** |
| `world-actions.ts` public social events | yes | no | **No** |
| `world-reports.ts` | yes | yes | Yes |
| `watch-live.ts` projection | yes | yes | Yes |

The third row is not in the reviewed input. [EVENT-CATALOG-AUDIT.md](EVENT-CATALOG-AUDIT.md) already recorded that adding `visibility` or `victim_id` was outside its scope, so the omission is deferred rather than overlooked.

### Resolving the audit's open question

[EVENT-CATALOG-AUDIT.md](EVENT-CATALOG-AUDIT.md) left one question open: whether `CRIME_DETECTED` is "a slice not yet wired or an event only the offline runtime raises," noting "the answer is not in this repository."

The answer is **a slice not yet wired**. The second branch is eliminated:

- `CRIME_DETECTED` does not appear anywhere in the offline Python runtime (`src/noema/`);
- it is not among the 24 types of `event-catalog/0.1` ([event-types.json](../specs/event-types.json));
- it exists only in `event-catalog/0.2`, consumed by the hosted Worker and produced by nothing.

## Corrections to the reviewed input

Recorded so later readers do not inherit them.

1. **The missing producer is not a new finding.** [EVENT-CATALOG-AUDIT.md](EVENT-CATALOG-AUDIT.md) documented it on 2026-08-24, explicitly so "the next audit does not re-derive them." The reviewed input re-derives it.
2. **The payload contradiction is Specs-internal.** Framing it as a runtime mismatch implies the Worker is wrong. The Worker matches the Accepted GC3 slice contracts; the closed payload is the outlier.
3. **Rehabilitation is already victim-specific and already pinned.** The reviewed input says decay and "three accepted trades" erase hostility "regardless of severity, victim, restitution." In fact `rehab_trades: 3` is pinned by [social-memory-catalog.gc3-s4.json](../specs/social-memory-catalog.gc3-s4.json) (schema `"const": 3`), and `rehabbedHostile()` counts trades **with the harmed counterparty only**, after the hostile cycle. It is not a runtime invention and not victim-blind. The criticism that survives is narrower and is registered as `B7e`: any accepted trade counts, severity does not change the requirement, and [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) says "restitution trades" while the pinned catalog counts ordinary ones.

## What this note does not do

- It does not wire detection, add a producer, or propose numbers. The reviewed input rates its own numeric confidence at 0.70; the papers are game-theoretic and do not calibrate NOEMA constants.
- It does not amend RFC-0002, the sanction ladder, or `event-types.0.2.json`.
- It does not open organized crime. That waits for a working first loop, per the hysteresis paper's own sequencing.

Continuation is governed by the rows added to [SPEC-GAP-REGISTER-2026-08-25.md](SPEC-GAP-REGISTER-2026-08-25.md).
