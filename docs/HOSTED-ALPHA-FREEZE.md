# Hosted alpha freeze

**Status.** FROZEN  
**Runtime pin.** Zero-State-LLC/Noema `3fd1d9e9af47b4ce6e654fa6c2f902ec6d87e3fe`  
**Specs pin.** this repo `2176135c94f8e2aae7dd4ef9bf9cf1f4ff768d6b`  
**Worker.** `7a482c37-3c93-48b6-bc68-ed02819b510e` on https://noema.guru  

Related: [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [HOSTED-COMPATIBILITY-LAYERS.md](HOSTED-COMPATIBILITY-LAYERS.md) · [ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md).

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
