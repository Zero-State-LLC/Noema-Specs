# Public `/watch` MAP WebGL allowlist (brand-lock reopen)

- **Kind:** thin presentation amend. Docs only in this repository.
- **Status:** Specified. Does not implement FE. Does not Deploy.
- **Date:** 2026-09-09
- **RFC:** No. No new verbs, events, protocol fields, or gates.
- **Authority to patch:** [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md) §3.3 (canonical allowlist), [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md), [WATCH-VISUAL-DIRECTION.md](../docs/WATCH-VISUAL-DIRECTION.md), and the brand pointers they name.
- **Prior door contract:** [specify/spec.md](spec.md) (one `/watch`; TEXT / PIXEL / MAP). This amend does not replace that door.

This file is a proposed patch to existing WATCH and brand presentation contracts. It does not replace those contracts. It does not authorize a Worker publish.

## Workflows

- **google-developer-style** — lead with the task, use short present-tense sentences, prefer tables over prose, do not invent jargon.
- **SKILL.SPEC_CHANGE** — edit the smallest canonical WATCH surface, then pointers, checklist, and changelog.
- **SKILL.EXPERIENCE** — keep PLAY, WATCH, and STUDY separate; WATCH stays a derived spectator projection.
- **Owner specialist:** WATCH public spectator MAP stage.
- **Existing Action:** reuse repository validation (`.github/workflows/` unchanged). Do not add a workflow.
- Do not invent an RFC, skill, bot, verb, or gate.

## Goal

Reopen the brand lock so public `/watch` MAP MAY use WebGL / Three.js (or equivalent) as the public spectator graphic stage.

TEXT remains authority. Projection is not world truth. Anti-cosplay bans stay.

PIXEL stays Canvas 2D until a later explicit row. This amend does not implement FE.

## Decision

1. Name [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md) §3.3 as the canonical public `/watch` graphics allowlist.
2. Allow WebGL / Three.js (or equivalent) on the MAP mode stage only when every allowlist condition holds.
3. Keep PIXEL on Canvas 2D. PIXEL WebGL waits for a later explicit row.
4. Keep anti-cosplay bans on public WATCH.
5. Keep spectator ≠ world truth, reduced-motion hard cuts, one map/stage at a time, access language only, and no new Player verbs or Genesis.
6. Point MAP P0 acceptance intent at existing product contracts. Do not implement them here.

## Allowlist (normative text)

The binding copy lives in [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md) §3.3. Restated here for reviewers:

**MAY**

- WebGL / Three.js (or equivalent) MAY render the MAP mode stage (and, by later explicit row, PIXEL enhancement) when motion is event-born, camera targets public `room_id` / actors only, and TEXT remains complete without GL.

**Still banned on public WATCH**

- Orbitron / sci-fi display fonts as brand voice
- CRT scanlines
- Military HUD packing
- Ambient particle / fog loops
- Dashboard KPI walls
- Fake depth that invents or implies hidden rooms/topology
- Decorative WebGL unrelated to a public event or follow target

**Unchanged**

- Spectator ≠ world truth
- `prefers-reduced-motion` → hard cuts / no easing
- One map/stage at a time
- No new Player verbs or Genesis
- Access language only

## MAP P0 acceptance intent (product, not implement)

A later runtime slice proves MAP stage quality against these existing contracts. This repository does not implement that slice.

| Intent | Meaning | Existing authority |
|---|---|---|
| Direct-Camera | Camera targets only public `room_id` / public actors already on the snapshot. No invented rooms or hidden topology. | Allowlist above; lightweight §7; mapping §1.1 |
| Gate D five-slot | A spectator can still write the five public statements from `/watch`, including MAP. | [LCA-GATE-D-SCENARIO.md](../docs/LCA-GATE-D-SCENARIO.md) five-statement checklist |
| Follow-that-teaches | Follow remains one public Player or site; emphasis only; unrelated activity stays visible. MAP camera MAY track that follow target. | [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §4.G |

## Non-goals

- Runtime / FE code in this repository
- PIXEL WebGL in this amend (later explicit row only)
- New Player verbs, events, gates, protocol fields, or Genesis
- Deploy, Gate E/F COMPLETE, hosted STUDY, or RFC-0130
- Dashboards, AI narration, spectator analytics, or cinema
- A second visual-identity campaign
- Loosening Orbitron / CRT / HUD / particle / KPI / fake-depth bans

## Acceptance (this Specs change)

- Canonical allowlist is in mapping §3.3. Absolute “no WebGL on public WATCH” sentences are updated.
- PIXEL §18 remains Canvas 2D only.
- Anti-cosplay bans remain.
- One-door `/watch` and spectator-is-not-truth language remain.
- MAP P0 points at Direct-Camera / Gate D five-slot / Follow-that-teaches as product intent, not implementation.
- `python3 validation/validate_all.py` PASSes.
