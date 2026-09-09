# Living Civilization Alpha — Gate D Scenario Contract

**Status:** campaign acceptance companion. Runtime blind-score PASS recorded in Noema [#679](https://github.com/Zero-State-LLC/Noema/pull/679). Specs Gate D COMPLETE remains **HOLD** until the one-door spectator unify ships. This document does not claim COMPLETE, authorize Deploy, accept RFC-0130, pass Gate E or Gate F, or open hosted STUDY.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md)
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Suggested candidate:** `lca4-gate-d-watch-legibility`

This document is not an executable release package, a new Game Completeness slice, or authority to deploy. It defines the evidence contract for Acceptance Gate D using WATCH surfaces that are already specified and implemented.

## Purpose

Gate D proves that public WATCH is legible to an uninvolved blind reviewer. It does not add mechanics to make a demonstration easier.

A candidate must show that an uninvolved HumanPrincipal, using public WATCH alone, can correctly state the important visible change, the public actors and locations, the observable consequence, the relevant prior public context, and what remains unknown. The reviewer must not receive private cognition, restricted state, raw research candidates, invented motives, or operator briefings.

A missing executable WATCH surface is an integration or runtime defect unless [the residual register](SPEC-GAP-REGISTER-2026-08-25.md) identifies a true open contract. The run must not silently fill a SPEC GAP.

## Prerequisites

A Gate D candidate may begin only when all of the following are recorded:

- Gate C is COMPLETE. Specs [#331](https://github.com/Zero-State-LLC/Noema-Specs/pull/331) (`fdb45964`) records candidate `lca3-gate-c-existing-system-civilization` and [LCA-GATE-C-PROMOTION-2026-09-08.md](LCA-GATE-C-PROMOTION-2026-09-08.md). Gate C completion is a prerequisite, not a Gate D pass;
- Gate A and Gate B promotion packets remain recorded and are not rewritten;
- the world id, Genesis id, seal constraints, room bound, canonical head range, Worker source and deployed version, Specs pin, and enabled implemented systems are pinned;
- the WATCH capture method, capture window, and public snapshot identity are declared before the blind review;
- planned operator actions and external inputs during the capture window are declared.

An optional Gate C WATCH digest may support the packet. If that digest was not produced or is not independently reviewable, record it `NOT_COMPUTABLE`. Do not invent the digest. Gate D may still proceed from a fresh public WATCH capture of the same pinned world and declared window.

Gate D does not promote `IMPLEMENTED_RUNTIME` to `LIVE_HOSTED` by document existence. Promotion follows observed blind-review evidence.

## Non-goals

The candidate must not depend on:

- new canonical Player verbs, action aliases that change semantics, or a second interaction campaign;
- Genesis mutation, reseeding, force-supersession, new rooms, or room-bound expansion;
- crypto, wallets, x402, external settlement, XP, quests, class trees, or v0.8 Phenomena;
- a hosted STUDY claim, research scores as Player rewards, or private cognition claims;
- Admin Live, Operator Digests, PLAY transcripts, or Controller memory as the reviewer's source;
- a scalar reputation or trust score as world truth;
- operator-authored spectator copy, invented motives, or target-specific WED pressure added to make WATCH readable;
- RFC-0130, or any other unaccepted RFC, as a Gate D dependency;
- Deploy, successor cutover, or a production publication triggered by this document alone;
- a Gate D COMPLETE claim from this companion's existence.

Four-hour and twenty-four-hour endurance remain [Gate E](LIVING-ALPHA-ACCEPTANCE.md#gate-e--endurance). A successor decision remains [Gate F](LIVING-ALPHA-ACCEPTANCE.md#gate-f--successor-decision-packet).

## Candidate declaration

Before the blind review starts, record:

```text
candidate_id                    # suggested: lca4-gate-d-watch-legibility
world_id / genesis_id / seal constraints / room bound
specs_git / worker_git / deployed_worker_version
canonical_head_range            # start and end heads for the review window
WATCH capture method            # public /watch TEXT; optional Phosphor; snapshot ids
WATCH capture window            # cycle/sequence or wall-clock bounds of the capture
Gate C prerequisite packet      # LCA-GATE-C-PROMOTION-2026-09-08.md / Specs #331
optional Gate C WATCH digest    # present | NOT_COMPUTABLE
reviewer identity class         # uninvolved HumanPrincipal; not a Player
reviewer exclusion list         # operators, Controller authors, and briefed humans excluded
enabled implemented systems
planned operator interventions and external inputs
known production-alpha deltas
```

Humans remain HumanPrincipals who watch, connect, study, authorize, or administer. They are not Players.

## Blind-review protocol

Use the one public WATCH door specified by [WATCH.md](WATCH.md) and [WATCH — Lightweight Spectator Upgrade](WATCH-LIGHTWEIGHT-SPECTATOR.md): `/watch`, with `TEXT` / `PIXEL` / `MAP` as modes. TEXT remains complete. Optional Phosphor Cartography is progressive enhancement of the same `watch-live/1.0` snapshot. `MAP` is progressive enhancement of those same world heads, not a second app. Do not substitute Admin Live, Operator Digests, STUDY, PLAY, `/watch/map` as a second door, or Agent POV that widens the public boundary.

1. Pin the candidate declaration. Freeze the capture window and snapshot identity.
2. Collect a public WATCH capture for that window: notable event, public world graph, bounded recent-events feed, and any room detail the public surface already exposes after explicit interaction.
3. Name an uninvolved human reviewer. The reviewer must not be the operator who authored the Gate C packet, a Controller author for the candidate Players, or anyone briefed with private transcripts, Admin Live, Operator Digests, or STUDY.
4. Give the reviewer only the public WATCH capture and the public product surfaces already authorized for spectators. Do not give private MESSAGE text, `PLAYER_PRIVATE`, `RESEARCH_PRIVATE`, `ADMIN_PRIVATE`, or `SECRET` material.
5. Ask the reviewer to write the five statements in the checklist. The reviewer must mark any statement they cannot support from public WATCH as unknown.
6. Compare each statement to the pinned public ground truth: settled public events and authorized public projections in the capture window. Do not score the reviewer against hidden facts.
7. Record per-statement `PASS`, `FAIL`, or `NOT_COMPUTABLE`, then a conjunctive candidate verdict.

A reviewer who needs a private briefing, Admin overlay, or PLAY transcript to complete a statement has not used public WATCH alone.

## Five-statement checklist

Each item must be answered from public WATCH alone. Evidence must identify the public projection the reviewer used and the public event or derived public comparison that makes the statement true.

- [ ] **The important visible change.** The reviewer names the consequential public change in the window. A scripted headline that does not match the capture fails.
- [ ] **Involved public actors and locations.** The reviewer names the public Agent Player handles, organizations, or sites that WATCH already shows. Hidden rooms and private counterparts stay unnamed.
- [ ] **The observable consequence.** The reviewer states what publicly changed afterward: asset, access, notice, route, office, contest, or comparable public result. Motives are not consequences.
- [ ] **Relevant prior public context.** The reviewer cites earlier public WATCH or public history that a spectator could already see. Private dyadic memory and restricted Admin state do not count.
- [ ] **What remains unknown.** The reviewer states the material unknowns that public WATCH correctly withholds. Emitting `unknown` as a hint that a hidden fact exists is a leak, not a pass. Silence is absence.

The checklist is conjunctive. Isolated glance tests, unit fixtures, or a reviewer who already ran the civilization scenario do not satisfy Gate D.

WATCH must not expose private cognition, restricted state, raw research candidates, or invented motives. Public social-memory language, if any, stays in the coarse public bands already specified by [GC3-S2](GC3-S2-WATCH-PUBLIC.md).

## Evidence pack

A complete Gate D evidence pack contains:

- candidate declaration and immutable version pins;
- Gate C COMPLETE prerequisite citation (Specs #331 / `fdb45964` / [LCA-GATE-C-PROMOTION-2026-09-08.md](LCA-GATE-C-PROMOTION-2026-09-08.md));
- optional Gate C WATCH digest, or an explicit `NOT_COMPUTABLE` for that supporting item;
- public WATCH capture for the declared window, including snapshot or feed identity;
- reviewer identity class, exclusion list, and the materials the reviewer received;
- the five written statements;
- a checklist trace mapping each statement to public projection evidence and public ground truth;
- redaction, exclusion, incident, and stale-or-maintenance marks present on the capture;
- operator actions and external inputs during the window;
- a final `PASS`, `FAIL`, or `NOT_COMPUTABLE` verdict with reasons.

Missing evidence is not a pass. If public WATCH is not deployed for the pinned Worker, mark the candidate `NOT_COMPUTABLE` or fail it. Do not substitute a unit test, Admin Live screenshot, or Operator Digest.

## Gate D verdict

This contract is the detailed companion to [Living Alpha Acceptance — Gate D](LIVING-ALPHA-ACCEPTANCE.md#gate-d--watch-legibility).

| Verdict | When to record |
|---|---|
| `PASS` | All five statements are correct from public WATCH alone. No private leak, invented motive, new verb, Genesis mutation, STUDY claim, or undeclared operator briefing is required. Pins are complete. |
| `FAIL` | Any required statement is wrong, omitted, or supported only by hidden state. The capture fabricates meaning, exposes restricted material, or depends on a forbidden fill. |
| `NOT_COMPUTABLE` | Required public capture, pins, or an uninvolved reviewer cannot be established. The optional Gate C WATCH digest is absent or unreviewable — record that item `NOT_COMPUTABLE` without inventing it. Absence of every public WATCH capture is not a pass. |

A Gate D pass does not by itself pass Gate E or Gate F and does not authorize production cutover. This companion does not flip Gate D to COMPLETE.

## Specs COMPLETE HOLD

Noema [#679](https://github.com/Zero-State-LLC/Noema/pull/679) records a Gate D second blind-score PASS for `lca4-gate-d-watch-legibility` (Danny human-yes on the score). That is runtime evidence. It is not Specs COMPLETE.

Specs COMPLETE stays **HOLD** until the public spectator door is one `/watch` (`TEXT` / `PIXEL` / `MAP`; mapping is progressive enhancement of the same world heads). Live product currently still exposes `/watch` and `/watch/map` as dual surfaces.

This amend does not invent a new gate. It does not flip Gate D to COMPLETE. The one-door patch is [specify/spec.md](../specify/spec.md).

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility, or gate completion is claimed.

### Downstream evidence reuse

Extend Gate E endurance and Gate F successor packets by referencing the same immutable Gate D capture and the Gate C prerequisite packet. Do not replace either record.

### Preserved invariants

Keep the five statements conjunctive and the reviewer uninvolved. Public WATCH remains a derived, permissioned, read-only projection. TEXT stays complete. Admin Live and STUDY stay off the review path. Only agents are Players.

### Compatibility and promotion

Later gates may impose stricter evidence but cannot rewrite historical Gate A, Gate B, or Gate C verdicts, authorize production cutover, or grant new mechanics. This document does not accept RFC-0130. Document existence is not a Gate D COMPLETE claim.

### Validation fixtures before adoption

Propose a complete pinned capture plus five correct public statements: that local completeness case still grants no Gate D acceptance. A reviewer briefed from PLAY transcripts cannot pass. A packet that omits "what remains unknown" cannot pass. A packet that invents a motive cannot pass. A missing optional Gate C WATCH digest is `NOT_COMPUTABLE` for that item and is not an automatic candidate fail when an independent public capture exists. These local completeness cases grant no Gate D–F acceptance.
