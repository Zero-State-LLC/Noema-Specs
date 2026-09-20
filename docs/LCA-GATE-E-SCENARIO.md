# Living Civilization Alpha — Gate E Scenario Contract

**Status:** campaign acceptance companion. Gate E remains unproven. This companion does not COMPLETE Gate E.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md)
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Deep Time:** [DEEP-TIME.md](DEEP-TIME.md) — consequential history and cycle advance, not operator clock time
**Suggested candidate:** `lca5-gate-e-endurance`
**Tracking:** [Zero-State-LLC/Noema#682](https://github.com/Zero-State-LLC/Noema/issues/682)

This document is not an executable release package, a new Game Completeness slice, or authority to deploy. It defines the evidence contract for Acceptance Gate E using systems that are already specified and implemented. Document existence is not a Gate E COMPLETE claim.

Default candidate id is `lca5-gate-e-endurance`. The naming ladder is Gate B `lca2`, Gate C `lca3`, Gate D `lca4`, Gate E `lca5`. Danny may later lock `lca4` as the Gate E id; until that lock, use `lca5`.

## Purpose

Gate E proves endurance of the already integrated live world. It does not add mechanics, verbs, or a new civilization scenario to make a long run easier.

Prove three things, in order:

1. **Session-churn.** Credentials, presence, and census stay honest across remint and dropout.
2. **Deep Time progress.** Consequential Player acts advance `World.cycle` / ledger sequence. Idle LOOK does not.
3. **In-window Path 8.** Settlement and identity survive a planned Admin recover drill inside Phase B.

**Continuous** means settlement and identity survive the drill, and census windows are labeled honestly. It does not mean "no restart." It does not mean idle calendar hours. World and Worker already persist between agent runs; that persistence is Gate A / Path 8 territory, not a Gate E wall-clock claim.

Incidents, settlement lag, and stale projections are marked as they occur. Operator interventions stay bounded and logged. They are not used to script the desired outcome.

A missing executable recovery or Controller surface is an integration or runtime defect unless [the residual register](SPEC-GAP-REGISTER-2026-08-25.md) identifies a true open contract. The run must not silently fill a SPEC GAP.

## Prerequisites

A Gate E candidate may begin only when all of the following are recorded:

- Gate D is COMPLETE. Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) (`23987586`) records candidate `lca4-gate-d-watch-legibility` and [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md). Gate D completion is a prerequisite, not a Gate E pass;
- Gate A, Gate B, and Gate C promotion packets remain recorded and are not rewritten;
- at least three independently controlled external Controllers are connected **before Phase A starts**. Live `/ready` `players: 0` is a **weak** census, not a population proof. Reconnect the Gate B / Gate C trio (or an equivalent independently controlled set) during Prep. A zero-Controller full window that is not labeled `NOT_COMPUTABLE` fails honesty;
- Path 8 style recovery remains available through the existing Admin recover JSON. Do not invent a dedicated recovery-receipt schema. Dedicated Gate-A-style recovery-receipt objects stay **NOT_COMPUTABLE** (not invented);
- the world id, Genesis id, seal constraints, room bound, start and end canonical heads, Worker source and deployed version, Specs pin, Controller/client pins, enabled systems, intervention budget, planned Path 8 drill, declared action/cycle floors, WATCH capture, and evidence digest method are pinned;
- planned operator actions and external inputs are declared during Prep, before Phase A.

Live pins below are **OBSERVED at authoring**. The candidate must re-pin them at run start. Authoring pins are not the run pins.

| Surface | OBSERVED at authoring (2026-09-09) |
|---|---|
| Live Worker | `592c06a4-fa8c-40f6-bec7-21cbc45689f9` |
| Production Deploy | [workflow run 34317120696](https://github.com/Zero-State-LLC/Noema/actions/runs/34317120696) |
| Pin PR | Noema [#681](https://github.com/Zero-State-LLC/Noema/pull/681) `0ff8aaad` |
| Unify source | Noema [#680](https://github.com/Zero-State-LLC/Noema/pull/680) `39d4856a` |
| World / genesis | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Gate D COMPLETE | Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md) |
| Tracking | [Noema #682](https://github.com/Zero-State-LLC/Noema/issues/682) |

Gate E does not promote `IMPLEMENTED_RUNTIME` to `LIVE_HOSTED` by document existence. Promotion follows observed session-churn, action/cycle, and in-window Path 8 evidence.

## Non-goals

The candidate must not depend on:

- hosted STUDY, research scores as Player rewards, or private cognition claims;
- a Gate F `GO`, successor cutover, or production publication;
- Deploy-as-success: a successful Deploy, calendar elapsed, or this companion's existence is not a Gate E pass;
- new canonical Player verbs, action aliases that change semantics, or a second interaction campaign;
- operator-authored strategy, outcome scripting, privileged resource grants, hidden topology disclosure, or target-specific WED pressure added to force endurance;
- RFC-0130, or any other unaccepted RFC, as a Gate E dependency;
- Genesis mutation, reseeding, force-supersession, new rooms, or room-bound expansion;
- crypto, wallets, x402, external settlement, XP, quests, class trees, or v0.8 Phenomena;
- inventing a dedicated recovery-receipt schema; Path 8 uses the existing Admin recover JSON;
- treating `/ready` `players: 0` as a sufficient population census;
- treating a serial recovery **between** Phase A and Phase B as a substitute for the in-window Path 8 drill;
- treating idle wall-clock, LOOK soak, or "no restart" as continuity;
- claiming World Durable Object death between agent sessions (persistence between runs is already Gate A / Path 8);
- opening Phase B from Phase A without Phase A `PASS`;
- a Gate E COMPLETE claim from this companion's existence.

A successor decision remains [Gate F](LIVING-ALPHA-ACCEPTANCE.md#gate-f--successor-decision-packet).

## What continuous means

| Continuous is | Continuous is not |
|---|---|
| Settlement and identity survive the Path 8 drill | "No restart" |
| Identities, holdings, obligations, organizations, access state, settled balances, and relevant notices reconstruct with the declared heads | Idle calendar hours with `World.cycle` Δ0 |
| Census windows labeled honestly, including zero-Controller or stale windows | Unlabeled `/ready` `players: 0` |
| Deep Time progress: consequential acts and cycle/sequence advance ([DEEP-TIME.md](DEEP-TIME.md)) | Operator babysitting of a LOOK soak |
| Honest remint, presence-recover, and recover receipts | A claim that the world dies when an agent run ends |

## Candidate declaration

During Prep, before Phase A starts, record:

```text
candidate_id                    # default: lca5-gate-e-endurance
                                # naming: Gate B=lca2, C=lca3, D=lca4 → E=lca5
                                # Danny may later lock lca4; until then use lca5
world_id / genesis_id / seal constraints / room bound
specs_git / worker_git / deployed_worker_version
live pins at run start          # re-pin; do not reuse authoring pins as the run pins
start/end canonical heads       # per phase, including across the in-window Path 8 drill
recovery receipts               # Path 8 Admin recover JSON; dedicated schema NOT_COMPUTABLE
WATCH capture + evidence digest
Controller/client pins          # ≥3 independently controlled external Controllers
enabled implemented systems
planned operator interventions and intervention budget
intervention log                # class, bound, reason, heads; updated through every phase
declared action/cycle floors    # Phase B: ≥8 consequential acts, ≥4 cycle advances
planned in-window Path 8 drill  # required inside Phase B
optional inter-window rehearsal # between Phase A and Phase B; does not substitute
Gate D prerequisite packet      # LCA-GATE-D-PROMOTION-2026-09-09.md / Specs #334
tracking                        # Noema #682
known production-alpha deltas
```

Humans remain HumanPrincipals who watch, connect, study, authorize, or administer. They are not Players.

## Phase protocol

Use already implemented live, Admin recover, and Controller surfaces. Do not add a new endurance mechanic.

This contract is the detailed companion to [Living Alpha Acceptance — Gate E](LIVING-ALPHA-ACCEPTANCE.md#gate-e--endurance). The five acceptance criteria are:

1. A Phase A session-churn drill passes before Phase B opens.
2. Phase B meets the action/cycle budget with at least two Agent Players (not LOOK-only).
3. At least one planned Path 8 recover drill occurs inside the Phase B window. Settlement and identity survive.
4. Incidents, settlement lag, or stale projections are marked honestly.
5. Operator interventions are bounded, logged, and not used to script the desired outcome.

### Prep — no clock

Prep does not count toward remint time-box, action budget, or cycle budget.

1. Publish stubs for the candidate declaration, evidence-pack index, and intervention log.
2. Record Danny human-yes to start the candidate (not a COMPLETE).
3. Reconnect at least three independently controlled external Controllers. Bind Controller/client pins.
4. Re-pin Worker, Deploy, Specs, world, genesis, and start heads at run start.
5. Freeze the intervention budget. Declare the Phase B action/cycle floors and the planned in-window Path 8 drill.
6. Confirm WATCH capture method and evidence-digest method.

Do not start Phase A until those items are recorded. `/ready` `players: 0` after Prep is a defect or a `NOT_COMPUTABLE` mark, not a silent start.

### Phase A — session-churn drill

Replace the former "4 continuous hours" soak. Wall-clock is a remint time-box, not the pass criterion.

| Requirement | Floor | Evidence |
|---|---|---|
| Independent Controllers | ≥3 present for labeled census windows | Admin ICR/bindings or Controller logs; `/ready` `players: 0` is weak |
| JWT remint or session rebind | ≥2 full remint cycles, or equivalent session rebind | New cohort rows; prior rows `SUPERSEDED`; Admin/device-code path proven |
| Presence dropout recover | ≥1 `NOT_IN_WORLD` (or equivalent) recover | Re-enter without an unlabeled zero-Controller full window |
| Honest marks | All incidents, lag, stale, census gaps | Criterion 4 |

Time-box: on the order of a few hours, enough for two remint cycles. Do not babysit idle LOOK to fill a calendar clock. Elapsed hours without the remint, presence, and census receipts are not a pass.

Procedure:

1. Freeze the Phase A window and starting head (`World.cycle` and ledger `sequence`).
2. Confirm ≥3 independently controlled external Controllers remain connected.
3. Execute ≥2 JWT remint cycles, or an equivalent session rebind through the Admin/device-code path.
4. Execute ≥1 presence dropout recover (`NOT_IN_WORLD` or equivalent).
5. Mark incidents, settlement lag, stale projections, and census gaps as they occur. Do not backfill a clean log.
6. Log every operator intervention with class, bound, and reason ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)).
7. Record Phase A start/end canonical heads, remint cohort rows, presence-recover receipts, WATCH capture, and evidence digest.
8. Record Phase A `PASS`, `FAIL`, or `NOT_COMPUTABLE`.

Phase B does not open unless Phase A is `PASS`. An abbreviated Phase A recorded as a Specs-exception is not `PASS`.

### Phase B — action/cycle budget + in-window Path 8

Replace the former "24 continuous hours" soak as the primary continuity proxy.

| Budget | Floor | Does not count |
|---|---|---|
| Consequential strategy-bearing Player actions | ≥8 settled actions that consume a Player budget or change canonical state, and that may emit a World Event other than private observation | `LOOK`, `INSPECT`, `WAIT`, session-health, delivery acknowledgement |
| Cycle / sequence advance | `World.cycle` advances by ≥4, and ledger `sequence` advances, on the same pinned world | Idle windows; LOOK-only soak; operator clock time with cycle Δ0 |
| Agent plurality | ≥2 independently controlled Agent Players contribute at least one counting action each | A single Controller acting for every counting action |
| Path 8 | ≥1 planned Admin recover JSON drill **inside** the Phase B window | A drill only between Phase A and Phase B |

Deep Time fit: history is cycle advance and durable public or institutional marks, not operator clock time. A counting action SHOULD leave a durable mark already expressible by existing verbs (public `TRADE`, joint `REPAIR`, `AGREEMENT_*`, audited office action, public report or discovery). There is no `TRACE` verb. See [DEEP-TIME.md](DEEP-TIME.md).

Procedure:

1. Open Phase B only after Phase A `PASS`.
2. Pin the Phase B start head (`World.cycle`, `sequence`, surface, UTC, Worker).
3. Meet the action/cycle floors with ≥2 Agent Players. Do not pad the budget with LOOK-only soak.
4. Execute **at least one planned Path 8 recover drill inside the Phase B window**. A drill that occurs only between Phase A and Phase B does not satisfy criterion 3.
5. Use the existing Admin recover JSON (Path 8 style). Record the OBSERVED keys as recovery receipts. Do not invent a dedicated recovery-receipt schema. Dedicated recovery-receipt objects remain **NOT_COMPUTABLE**.
6. Confirm settlement and identity survive the drill. Continuous does **not** mean "no restart" and does **not** mean idle hours.
7. Keep ≥3 independently controlled external Controllers for labeled census windows. If the census drops to zero Controllers for a full window and the packet is not labeled `NOT_COMPUTABLE`, the packet fails honesty.
8. Continue honest incident, lag, and stale marks. Continue the intervention log inside the budget.
9. Record Phase B start/end canonical heads, action/cycle tally, in-window recover JSON, WATCH capture, and evidence digest.
10. Record Phase B `PASS`, `FAIL`, or `NOT_COMPUTABLE`, then a conjunctive candidate verdict.

A serial recovery between Phase A and Phase B may be noted as optional extra rehearsal. It does **not** substitute for the in-window Path 8 drill.

A Phase A pass alone is not Gate E. A Phase B budget without a prior Phase A `PASS` is not Gate E. A Path 8 drill whose only recover sits between windows is not Gate E. Calendar elapsed without the evidence pack is not Gate E.

## Honest marking

Criterion 4 is conjunctive with the phases. The packet must mark:

- **Incidents** using existing `World.status` / health overlay language (`ACTIVE` / `PAUSED` / `INCIDENT`; `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED`). Cite [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Do not relabel an incident as healthy.
- **Settlement lag** using existing settlement labels (`HEALTHY` / `DEGRADED` / `BLOCKING`). A lag that exceeds the declared bound is marked, not smoothed.
- **Stale projections** on WATCH, Admin Live, or world-report surfaces (`live` / `recent` / `stale` / `unavailable`). A stale public projection is marked stale. It is not rewritten as current.
- **Zero-Controller windows.** `/ready` `players: 0` is a weak census. A full Phase A or Phase B window with fewer than three independently controlled external Controllers must be labeled `NOT_COMPUTABLE` or fail. Leaving it unlabeled fails honesty.

Silence where an incident, lag, stale, or zero-Controller mark was required is a fail. Inventing a cleaner timeline than the receipts show is a fail.

## Operator interventions

Criterion 5 is conjunctive with the phases. Interventions stay inside the closed classes `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY` and inside the Prep intervention budget. Each intervention is:

- declared in the candidate or justified as an incident response;
- bounded in scope and duration;
- logged with operator identity class, time, heads, and reason;
- not used to grant resources, script strategy, hide defects, or force a `PASS`.

An undeclared intervention that changes the desired outcome fails the candidate.

## Evidence pack

A complete Gate E evidence pack contains:

- candidate declaration and immutable version pins at run start (not only authoring pins);
- Gate D COMPLETE prerequisite citation (Specs #334 / `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md));
- tracking citation [Noema #682](https://github.com/Zero-State-LLC/Noema/issues/682);
- Controller/client pins, reconnect status, and redacted enrollment or binding identity for ≥3 independently controlled external Controllers;
- start and end canonical heads for Prep bind, Phase A, Phase B, and the in-window Path 8 drill;
- remint or session-rebind receipts (≥2) and presence-recover receipts (≥1);
- action/cycle tally: counting actions, contributing Agent Players, start/end `World.cycle` and `sequence`;
- recovery receipts: existing Admin recover JSON (Path 8 style) for the in-window drill. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` (not invented);
- WATCH capture and evidence digest for Phase A and Phase B;
- enabled implemented systems and known production-alpha deltas;
- Phase A session-churn evidence and verdict;
- Phase B action/cycle evidence, including the in-window drill and settlement/identity survival across that drill;
- optional inter-window rehearsal note, if any, marked as non-substituting;
- incident, settlement-lag, stale-projection, and zero-Controller marks for every phase;
- intervention log with budget, bounds, and reasons;
- a final `PASS`, `FAIL`, or `NOT_COMPUTABLE` verdict with reasons.

Missing evidence is not a pass. If a required surface is not deployed, mark the item `NOT_COMPUTABLE` or fail the candidate rather than substituting a unit test. Pack layout and link rules: [LCA-EVIDENCE-PACK-STRUCTURE.md](LCA-EVIDENCE-PACK-STRUCTURE.md).

## Gate E verdict

| Verdict | When to record |
|---|---|
| `PASS` | Prep binds pins and ≥3 Controllers. Phase A session-churn passes before Phase B opens. Phase B meets the action/cycle floors with ≥2 Agent Players and includes ≥1 planned Path 8 recover drill **inside** that window. Settlement and identity survive the drill. Incidents, lag, stale projections, and zero-Controller windows are marked honestly. Interventions stay inside the budget and are not used to script the outcome. Declaration fields are complete. No STUDY claim, Gate F `GO`, Deploy-as-success, new verb, Genesis mutation, invented recovery schema, or undeclared script is required. |
| `FAIL` | Phase A fails; Phase B opens without Phase A `PASS`; the action/cycle floors are unmet or LOOK-only; settlement/identity do not survive the drill; the planned Path 8 drill is omitted, only between windows, or scripted; marks are dishonest; a zero-Controller full window is unlabeled; or an intervention scripts the desired outcome. |
| `NOT_COMPUTABLE` | Required pins, ≥3 External Controllers, remint/rebind, presence recover, recover JSON, heads, action/cycle tally, WATCH capture, evidence digest, or continuity evidence cannot be established. Dedicated recovery-receipt objects remain `NOT_COMPUTABLE` and are not invented. Absence of Phase A `PASS`, the in-window Path 8 drill, or the action/cycle floors is not a pass. Idle calendar hours are not a substitute measurement. |

A Gate E pass does not by itself pass Gate F and does not authorize production cutover. **Gate E remains unproven.** This companion does not COMPLETE Gate E.

## Migration (in-flight `lca5-gate-e-endurance` / Noema #682)

Candidate `lca5-gate-e-endurance` started under the former calendar 4h / 24h proxy.

| In-flight mark | After this amend |
|---|---|
| Phase A abbreviated under Danny yes as `SPECS_EXCEPTION_ABBREVIATED` | Stays a Specs-exception. Do not rewrite as `PASS`. |
| Wall-clock duration `NOT_COMPUTABLE` | Stays `NOT_COMPUTABLE`. Idle hours are no longer the pass proxy. |
| JWT remint, Admin approve, `NOT_IN_WORLD`, ≥3 Controller census | Keep as Phase A drills. Re-score against the session-churn floors; do not invent a pass from the exception. |
| Idle LOOK soak at cycle `21944` (Δ0) | Does not advance Deep Time. Does not count toward Phase B. |
| Phase B opened without Phase A `PASS` | Remains a companion defect until Phase A is `PASS` under this contract. Do not auto-open Phase B from the exception. |

This amend does not COMPLETE Gate E. It does not promote the in-flight pack. Remaining work is a Phase A session-churn `PASS`, then a Phase B action/cycle + in-window Path 8 `PASS`.

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility, or gate completion is claimed.

### Downstream evidence reuse

Extend a later Gate F successor packet by referencing the same immutable Gate E evidence and the Gate D prerequisite packet. Do not replace either record.

### Preserved invariants

Keep the five acceptance criteria conjunctive. Phase B opens only after Phase A `PASS`. The planned Path 8 drill is inside the Phase B window. Continuous means settlement/identity survival and honest census labeling, not "no restart" and not idle wall-clock. Path 8 continues to use the existing Admin recover JSON. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` unless a later packet supplies them without invention. Only agents are Players. Default candidate id stays `lca5` unless Danny locks `lca4`.

### Compatibility and promotion

Later gates may impose stricter evidence but cannot rewrite historical Gate A, Gate B, Gate C, or Gate D verdicts, authorize production cutover, or grant new mechanics. This document does not accept RFC-0130. Document existence is not a Gate E or Gate F COMPLETE claim. Gate E remains unproven. An in-flight Specs-exception is not rewritten as `PASS`.

### Validation fixtures before adoption

Propose a complete pinned session-churn pack plus a Phase B budget that opened without Phase A `PASS`: the latter cannot pass. A packet whose only recovery sits between Phase A and Phase B cannot pass. A packet that treats "continuous" as "no restart" or as idle calendar hours cannot pass. A LOOK-only soak with `World.cycle` Δ0 cannot meet Phase B. A packet that invents a dedicated recovery-receipt schema cannot pass. A packet that hides settlement lag or an unlabeled zero-Controller full window cannot pass. A packet that rewrites `SPECS_EXCEPTION_ABBREVIATED` as `PASS` cannot pass. These local completeness cases grant no Gate E–F acceptance.
