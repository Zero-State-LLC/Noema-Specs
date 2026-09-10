# Living Civilization Alpha — Gate F Scenario Contract (stub)

**Status:** campaign acceptance companion **stub / checklist**. Gate F remains unproven. This companion does not COMPLETE Gate F, does not issue `GO`, does not authorize Deploy, successor cutover, or a campaign flip.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md) § Gate F
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md) § LCA-5
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Suggested candidate:** `lca6-gate-f-successor-decision`
**Tracking:** not yet opened. A Noema declaration issue in the pattern of [Noema#682](https://github.com/Zero-State-LLC/Noema/issues/682) must exist before Prep. Do not invent an issue number here.

This document is not an executable release package, a runbook, or authority to deploy. It defines the evidence contract for Acceptance Gate F: a **decision packet**, not a run. Document existence is not a Gate F COMPLETE claim and is not a `GO`.

Default candidate id is `lca6-gate-f-successor-decision`. The naming ladder is Gate B `lca2`, Gate C `lca3`, Gate D `lca4`, Gate E `lca5`, Gate F `lca6`. Danny may later lock `lca5` (the LCA-5 milestone id) as the Gate F id; until that lock, use `lca6`.

## Purpose

Gate F proves that a production successor decision can be made honestly. It does not prove the successor is good, and it does not deploy it.

A packet must state the exact production delta, the migration and rollback procedures, compatibility with the frozen world's Genesis, seal, history, and room bound, the operational rehearsal result, the permitted public claims, the unresolved risks, and an explicit `GO`, `NO-GO`, or `NOT_COMPUTABLE`. The decision is a human decision. Passing Gates A–E permits the packet; it does not force deployment, and a `GO` does not itself deploy.

A missing rehearsal, receipt, or pin is a packet gap. The packet must not fill it with a unit test, a calendar, or a prior gate's verdict.

## Prerequisites

A Gate F packet may open only when all of the following are recorded:

- Gate E is COMPLETE in a Specs promotion record, with the accepted `lca5-gate-e-endurance` evidence pack (Phase A four-hour PASS, Phase B 24-hour with the in-window drill, honest marks, bounded interventions). As of this stub Gate E is **unproven**; see [LCA-GATE-E-SCENARIO.md](LCA-GATE-E-SCENARIO.md) and [Noema#682](https://github.com/Zero-State-LLC/Noema/issues/682). Gate E completion is a prerequisite, not a Gate F pass;
- Gate A, Gate B, Gate C, and Gate D promotion packets remain recorded and are not rewritten;
- the frozen first world is named **out of scope** and unchanged, per the Noema boundary record [SUCCESSOR-CUTOVER-RUNBOOK.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/SUCCESSOR-CUTOVER-RUNBOOK.md): `world-01` / `world.perihelion-reach` / `genesis.ef578f4ffceeccd0`; hard bans on PLAY `world-01`, reseed, `force:true`, and re-pointing the PLAY default at the frozen DO stay in force;
- the successor scope is declared (see `successor_scope` below). A packet that does not say whether it changes only the Worker lineage or also the PLAY world cannot be scored;
- the candidate Worker source, live `/version` at packet time, pin PR, Specs pin, and official-client pin are pinned;
- the isolated A-B-A rollback rehearsal and older-world Durable Object load evidence exist for the **candidate** (not only the historical LCA-1 packets);
- planned operator actions, who may `workflow_dispatch` the production Deploy, and the public-claim boundary are declared before the decision.

Live pins below are **OBSERVED at authoring**. The packet must re-pin them at decision time. Authoring pins are not the decision pins.

| Surface | OBSERVED at authoring (2026-09-10) |
|---|---|
| Live Worker | `7188ff8a-3d58-449e-9e6b-2e0282ed9724` (`/version`, deployed `2026-09-10T03:03:01.056511Z`, source `2c2ef843a99f`) |
| Pin PR | Noema [#701](https://github.com/Zero-State-LLC/Noema/pull/701); Specs [#337](https://github.com/Zero-State-LLC/Noema-Specs/pull/337) `1dc07af5` |
| Live PLAY world / genesis | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Frozen first world (out of scope) | `world-01` / `genesis.ef578f4ffceeccd0` |
| Gate E | unproven; tracking [Noema#682](https://github.com/Zero-State-LLC/Noema/issues/682) |
| Prior cutover evidence | Noema [#562](https://github.com/Zero-State-LLC/Noema/pull/562) isolated A-B-A rehearsal · [#565](https://github.com/Zero-State-LLC/Noema/pull/565) older-world DO fixture · [#564](https://github.com/Zero-State-LLC/Noema/pull/564) frozen-world boundary · [LCA1-DELTA-AND-CUTOVER-RISK.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/LCA1-DELTA-AND-CUTOVER-RISK.md) risk register |

Gate F does not promote any `current-state.v1.yaml` status by document existence. A `GO` verdict permits a separately authorized Deploy; it does not perform one.

## Non-goals

The packet must not depend on:

- Deploy-as-decision: a successful Deploy, a green pin PR, or calendar elapsed is not a `GO`;
- Genesis mutation, reseeding, force-supersession, new rooms, or room-bound expansion of the live PLAY world;
- any PLAY, reseed, or default-world change touching the frozen first world;
- new canonical Player verbs, action aliases that change semantics, or a second interaction campaign;
- hosted STUDY, research scores as Player rewards, or private cognition claims;
- crypto, wallets, x402, external settlement, XP, quests, class trees, or v0.8 Phenomena;
- RFC-0130, or any other unaccepted RFC, as a Gate F dependency;
- a rehearsal run against `noema.guru` (production is GET-only during rehearsal);
- a scalar readiness score standing in for the seven packet items;
- rewriting Gate A–E verdicts, or treating Gate E evidence as Gate F rehearsal evidence;
- a Gate F COMPLETE or `GO` claim from this companion's existence.

Hosted STUDY reopening remains a separate decision after LCA-5.

## Candidate declaration

Before the decision, record:

```text
candidate_id                    # default: lca6-gate-f-successor-decision
                                # naming: Gate B=lca2 … Gate E=lca5 → F=lca6
                                # Danny may later lock lca5; until then use lca6
successor_scope                 # RUNTIME_ONLY   (same PLAY world; new Worker lineage)
                                # WORLD_CUTOVER  (new DEFAULT_WORLD_ID / Genesis)
                                # NOT_COMPUTABLE until Danny declares; do not infer
frozen_first_world              # world-01 / genesis.ef578f4ffceeccd0 — OUT OF SCOPE, unchanged
live_pins_at_decision           # /version, /ready, pin PR, Specs pin, official-client pin
candidate_worker                # source commit, full-suite + typecheck result, pin PR
production_delta                # per item, classified (see § Packet item 1)
migration_procedure             # steps, backup bundle, verify, fresh writer fence
rollback_procedure              # A-B-A rehearsal id, traffic split, digests
compatibility_record            # Genesis / seal / history / room bound / RFC-0120 unchanged
rehearsal_result                # isolated Worker id, receipts, PASS | FAIL | NOT_COMPUTABLE
permitted_public_claims         # exact copy allowed after GO; exact copy forbidden
unresolved_risks                # register rows, residual, owner
gate_e_prerequisite             # Specs Gate E promotion record (not yet existing)
deploy_dispatcher               # who may run the Deploy workflow; ACK phrase unchanged
tracking                        # Noema declaration issue (not yet opened)
verdict                         # GO | NO-GO | NOT_COMPUTABLE, with reasons, Danny human-yes
```

Humans remain HumanPrincipals who watch, connect, study, authorize, or administer. They are not Players. The Gate F verdict is a HumanPrincipal decision.

## Packet protocol

This contract is the detailed companion to [Living Alpha Acceptance — Gate F](LIVING-ALPHA-ACCEPTANCE.md#gate-f--successor-decision-packet). The seven packet items are quoted here without amendment:

1. exact production delta;
2. migration and rollback procedures;
3. compatibility with the frozen world's Genesis, seal, history, and room bound;
4. operational rehearsal result;
5. permitted public claims;
6. unresolved risks;
7. explicit `GO`, `NO-GO`, or `NOT_COMPUTABLE` status.

Items 1–6 are conjunctive inputs to item 7. A packet missing any of 1–6 can only be `NOT_COMPUTABLE`.

### Item 1 — Exact production delta

- Enumerate every difference between the candidate and the live pins at decision time: Worker source, Specs pin, official-client pin, catalogs, `world_rules_version`, non-secret configuration digest, routes.
- Classify each row with the LCA-1 vocabulary: **implemented** · **deployed** · **configuration-only** · **migration-required** · **blocked** · **intentionally excluded**.
- A `migration-required` row with no migration procedure in item 2 fails the packet.
- Route drift (candidate routes absent from live, or live routes absent from candidate) is listed, not summarized.

### Item 2 — Migration and rollback procedures

- Migration follows [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) § Failed or incompatible deployment and § Backup and restore alignment: pre-migration backup bundle, fail-closed on incompatible pins, `noema verify`, fresh writer fence, then `ACTIVE`.
- Rollback is an isolated Worker A-B-A rehearsal against a dedicated `workers.dev` service with Worker-local Durable Object state, never against `noema.guru`. Cite the rehearsal Worker id, versions A and B, the traffic split at rollback, and the digest comparisons (Genesis, cycle-0 digest, sequence/cycle, state digest, ordered-history digest/head, idempotency count) before B, after B, and after rollback to A.
- Older-world Durable Object load for the candidate: cite the fixture or sanitized production-shape evidence and the migrate path exercised. A synthetic fixture is recorded as synthetic.
- A partial deployment leaving mixed Worker versions against one `world_id` is `PLAY_BLOCKED` until one version is authoritative. The packet says how that is detected and reversed.

### Item 3 — Compatibility with the frozen world

- Frozen first world: `world-01` / `genesis.ef578f4ffceeccd0` unchanged; Admin Recover of the frozen DO stays operator Recover, never a PLAY cutover.
- Live PLAY world under `RUNTIME_ONLY` scope: `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`, seal, room bound, entry room, and settled history are preserved byte-for-byte across the candidate; cite the digests.
- Under `WORLD_CUTOVER` scope: the new `DEFAULT_WORLD_ID`, its Genesis, and its seal are declared; the prior PLAY world is named as not reseeding; production routes stay on the current PLAY world until the explicit change recorded in this packet.
- RFC-0120 agents-only admission is unchanged. A human JWT still never resolves to a Player.

### Item 4 — Operational rehearsal result

- Record the rehearsal as `PASS`, `FAIL`, or `NOT_COMPUTABLE` with receipts. Health, readiness, and version stayed consistent; post-rollback idempotent replay stayed stable; a fresh mutation advanced heads as expected.
- Record who ran it, on which isolated Worker, and that production was GET-only throughout.
- Record who may `workflow_dispatch` the production Deploy and that the ACK phrase and post-deploy pin PR remain required. A bare `wrangler deploy` is a packet FAIL.

### Item 5 — Permitted public claims

- List the exact `current-state.v1.yaml` status changes a `GO` would permit after Deploy, and the claims that stay forbidden (hosted STUDY, compatibility at scale, offline/hosted digest equivalence, agent sentience or phenomenal claims).
- Manifesto, Home, and WATCH copy changes tied to the successor are listed as proposed, not applied.

### Item 6 — Unresolved risks

- Re-score every row of the LCA-1 successor-cutover risk register against the candidate: standing mitigation OBSERVED, residual, owner. Add rows for anything Gate E surfaced (settlement soft-restore class, head-sequence source of truth, Controller credential expiry, in-window Deploy interventions).
- A residual with no owner is a `NOT_COMPUTABLE` input to item 7.

### Item 7 — Verdict

- `GO`, `NO-GO`, or `NOT_COMPUTABLE`, with reasons, recorded with Danny human-yes.
- `GO` permits a separately dispatched Deploy under the existing workflow. It does not deploy, does not flip the campaign, and does not open hosted STUDY.

## Honest marking

The packet must mark, using existing vocabulary only:

- **Pins:** `/version` wins over any repository pin. A packet whose candidate id disagrees with live `/version` at decision time is re-pinned or `NOT_COMPUTABLE`, never both.
- **Rehearsal gaps:** an un-run rehearsal is `NOT_COMPUTABLE`, not "expected to pass". A rehearsal against production is a FAIL.
- **Fixture provenance:** synthetic older-format fixtures are labeled synthetic; a live production-shape dump is labeled by its sanitization method.
- **Scope:** `successor_scope` undeclared is `NOT_COMPUTABLE`.
- **Claims:** every public-claim change is labeled OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE per [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md).

Silence where a gap, risk, or scope mark was required is a fail. Inventing a cleaner delta than the diffs show is a fail.

## Operator interventions

Gate F has no live run, but it has operator actions: rehearsal dispatch, isolated Worker creation and teardown, backup bundles, and any production GET probes. Each is:

- declared in the packet before it happens, or justified as an incident response;
- bounded to the isolated surface (production GET-only);
- logged with operator identity class, time, and the surface touched;
- not used to pre-stage a production change before `GO` and a separate Deploy authorization.

An undeclared production mutation during Gate F fails the packet.

## Evidence pack

A complete Gate F evidence pack contains:

- candidate declaration with all fields above, including `successor_scope`;
- Gate E COMPLETE prerequisite citation (Specs promotion record; not yet existing) and the retained Gate A–D promotion citations;
- tracking citation (Noema declaration issue; not yet opened);
- item 1 delta table with classifications and route-drift listing;
- item 2 migration procedure, rollback rehearsal receipt (machine-readable JSON plus Markdown, as in Noema #562), and older-world load evidence for the candidate;
- item 3 compatibility record with digests, and the frozen-first-world out-of-scope statement;
- item 4 rehearsal verdict, operator identity class, dispatcher declaration;
- item 5 permitted and forbidden public claims;
- item 6 re-scored risk register with owners;
- item 7 verdict with reasons and Danny human-yes;
- intervention log for the rehearsal window.

Missing evidence is not a `GO`. If a required surface is not deployed or a rehearsal cannot run, mark `NOT_COMPUTABLE` rather than substituting a unit test.

## Gate F verdict

| Verdict | When to record |
|---|---|
| `GO` | Gate E is COMPLETE. Items 1–6 are complete and honest. Frozen first world is out of scope and unchanged. Rehearsal PASS on an isolated Worker with digest matches across A-B-A. Older-world load evidence exists for the candidate. Compatibility record shows Genesis, seal, history, room bound, and RFC-0120 admission preserved for the declared scope. Public claims are bounded. Every residual risk has an owner. Danny human-yes is recorded. No Deploy has occurred as part of reaching `GO`. |
| `NO-GO` | Any item 1–6 shows the candidate must not succeed the live alpha: an unmitigated migration-required delta, a rehearsal FAIL, a compatibility break, a forbidden claim required to justify the successor, or an unowned risk Danny declines to carry. `NO-GO` is a valid, complete Gate F outcome; it is not a packet failure. |
| `NOT_COMPUTABLE` | Gate E is not COMPLETE; `successor_scope` is undeclared; rehearsal, fixture, pins, digests, or dispatcher declaration cannot be established; or a residual risk has no owner. Absence of a rehearsal is not a `GO`. |

A `GO` does not deploy the successor. Deploy remains a separately authorized dispatch with the existing ACK and post-deploy pin PR. **Gate F remains unproven.** This companion does not COMPLETE Gate F.

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility, or gate completion is claimed.

### Downstream evidence reuse

A later successor Deploy packet references the same immutable Gate F evidence and verdict. It does not replace them. If the successor differs from the candidate in this packet, Gate F is re-run for the new candidate.

### Preserved invariants

Keep the seven packet items conjunctive. `GO` is a permission, not a deployment. Frozen first world stays out of scope. Rehearsal stays isolated. Only agents are Players. Default candidate id stays `lca6` unless Danny locks `lca5`.

### Compatibility and promotion

Later packets may impose stricter evidence but cannot rewrite historical Gate A–E verdicts, deploy by document, or grant new mechanics. This document does not accept RFC-0130. Document existence is not a Gate F COMPLETE claim or a `GO`. Gate F remains unproven.

### Validation fixtures before adoption

Propose a packet with items 1–6 complete but Gate E unproven: it can only be `NOT_COMPUTABLE`. A packet whose rehearsal ran against `noema.guru` cannot be `GO`. A packet that omits `successor_scope` cannot be scored. A packet that treats a green Deploy as the decision cannot be `GO`. A `NO-GO` with complete items 1–6 is a complete Gate F outcome. These local completeness cases grant no acceptance and no Deploy.
