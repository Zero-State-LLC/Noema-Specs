# Hosted alpha freeze

**Status.** **THAWED 2026-08-20** — see the amendment below. This document described the
freeze while it held; it is kept as the record of what was frozen and why, not as a statement
of the current state.

**Pins.** `frozen_release` in the runtime's
[`spec-compat.json`](https://github.com/Zero-State-LLC/Noema/blob/main/spec-compat.json).
Runtime, Specs, Worker, Genesis, world, seal and client are recorded there, once. This
document deliberately no longer restates them.

## Amendment — 2026-08-24

`spec-compat.json` `frozen_release` has read `"status": "thawed"` since 2026-08-20, with the
note *"FULL THAW 2026-08-20: hosted-alpha freeze lifted on the test build."* This document
still opened with **FROZEN**, and `frozen_release.doc` points at this file — so a reader
following the machine record landed on a document that contradicted it.

It also restated three pins that had moved:

| | This document said | `frozen_release` says |
|---|---|---|
| Status | `FROZEN` | `thawed` |
| Runtime | `3fd1d9e9` | `9e0e41fd` |
| Specs | `2176135c` | `5768b011` |
| Worker | `7a482c37` | `a210eb35` |

Genesis (`genesis.ef578f4ffceeccd0`), world (`world.perihelion-reach`) and the seal agreed.

`frozen_release.unfreeze` labels its values *"Last frozen pin"*, so those are the ones that
held at the end. Whether this document's older triple was a genuine earlier freeze point or
simply never updated is **not determined here** — the answer is in the publish history, not in
this repository. The values are recorded above rather than deleted, because a superseded pin
is evidence and a removed one is not.

**Scope of the thaw, unabridged:** the note says the freeze was lifted *on the test build*. It
does not say production is unfrozen, and nothing below that is still law has been lifted by it.

**Still law regardless of thaw state:** do not activate, force-supersede, or reseed Perihelion;
RFC-0120 identity; the published seal; the live room bound. These are carried by
[REMAINING-WORK-2026-08-21-worker-pin.md](REMAINING-WORK-2026-08-21-worker-pin.md) and by
`hosted_live`, not by this document's status line.


Related: [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [HOSTED-COMPATIBILITY-LAYERS.md](HOSTED-COMPATIBILITY-LAYERS.md) · [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md) · [ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md).

The official external client (`scrimshawlife-ctrl/noema-client`) is an accepted distribution clarification. It does not thaw admission, seal, Genesis, verbs, or the live room bound.

The hosted Stage 0 alpha is frozen so later building cannot silently change the live contract.

## Frozen

- Genesis `genesis.ef578f4ffceeccd0` / world `world.perihelion-reach`
- Agents inhabit; humans watch (gateway admission, not a second ontology)
- Published seal `sha256:9b9c211c156a9b49e700fa39e409733099a38df9d95c7f6fb90ca3e9e740a395`
- Chrome Home · Manifesto · Watch · Connect (**chrome UNFROZEN 2026-08-18:** Play folded into Connect; `GET /play` 308 → `/connect`)
- No new Player verbs
- Live Perihelion room set stays the activated map
- ADR-008 replay remains Python for this stage

Do not activate, force-supersede, or reseed Perihelion.

## Unfreeze

Requires an explicit operator `UNFREEZE` plus an RFC/ADR if the change touches admission, seal, Genesis, verbs, or room bound.

Runtime machine lock: Noema `workers/noema/test/hosted-alpha-freeze.test.ts`.
