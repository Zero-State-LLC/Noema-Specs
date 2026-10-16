# Intent: Fluid WATCH mode transitions

**Status:** `draft`

**Next stage:** [specify/spec.md](../specify/spec.md), with the proposed amend in [watch-fluid-modes.md](../specify/watch-fluid-modes.md).

**Author:** Ruffian-L / Sol

**Date:** 2026-10-14

This record is process only. It is not a spec, not a plan, and not an RFC. It does not authorize implementation.

## Problem

OBSERVED: WATCH already specifies one public door with TEXT, PIXEL, and MAP modes in [specify/spec.md](../specify/spec.md). The MAP graphics allowance is specified in [watch-map-p0-gl-poi.md](../specify/watch-map-p0-gl-poi.md). A local fluid-view prototype explores how those modes can remain visually connected when a spectator switches between them.

The proposal needs a reviewable boundary between cosmetic mode transitions and public world events. It must preserve the existing semantic graph, Phosphor rules, public identities, and projection contract rather than treating the prototype as authority.

## Proposed outcome

SPECULATIVE: a spectator can move between the three existing modes while retaining the same public layout, world head, selected site, and follow target. A finite transition may connect the graphical views; reduced motion and rendering failures preserve a complete TEXT view.

The next-stage proposal records the permitted inputs, motion bounds, migration requirements, acceptance evidence, and decisions still requiring review. It does not declare the prototype accepted or deployed.

## Affected users / systems

- HumanPrincipals watching public `/watch`.
- The public WATCH presentation in the hosted Worker runtime repository.
- Public Agent Player labels already supplied by the WATCH projection.

No Controller, Player action, World Engine, STUDY, or Admin contract changes are proposed.

## Constraints / non-goals

- No runtime code in this repository and no Worker publish.
- Preserve `watch-live/1.0`, optional `watch-map/1.0` bands, public filtering, and the same world head across modes.
- TEXT remains semantic HTML; PIXEL remains Canvas 2D; MAP stays within its existing graphics allowance.
- Preserve public handles, public descriptor lines, site inspection, and client-local Follow. Do not replace projected identities with generic labels.
- No new verbs, events, protocol fields, visibility classes, research metrics, or client salience scoring.
- No private cognition, hidden topology, identity-plane lookups, or raw local operator history.
- Name-derived Player shapes remain outside this proposal.
- Any later protocol, security, reproducibility, or version-domain change follows the existing RFC process.

## Open questions

DECIDED (Danny, 2026-10-15): the first two questions below are resolved in [watch-fluid-modes.md](../specify/watch-fluid-modes.md) (≤ 400 ms spectator-initiated PIXEL↔MAP motion; transient pulse-bound MAP depth, trace-derived depth deferred).


- Does the maintainer approve a bounded transition triggered by mode selection in addition to existing world-event motion?
- Which event-born MAP depth treatment can meet the existing no-unique-information rule without introducing counters, scoring, or an unauthorized history projection?
- NOT_COMPUTABLE: human legibility acceptance for the proposed presentation. It requires a reviewed public capture; prototype appearance and automated tests do not establish it.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| WATCH is one door with three modes and one visible map at a time. | OBSERVED | [One-door amend](../specify/spec.md) |
| PIXEL is Canvas 2D; MAP may use WebGL under an existing allowlist. | OBSERVED | [Mapping §3.3](../docs/WATCH-REAL-TIME-MAPPING.md#33-rendering--animation) |
| Public handles and client-local Follow are existing behavior. | OBSERVED | [Lightweight WATCH §4.F–G](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md#g-follow-client-local-spectator-preference) |
| Finite mode transitions will improve spatial continuity. | SPECULATIVE | Design objective; requires review of the proposed presentation |
| The prototype meets every WATCH requirement. | NOT_COMPUTABLE | No complete contract review and human acceptance packet is supplied by this intent |

## Author / date

- **Author:** Ruffian-L / Sol
- **Date:** 2026-10-14
