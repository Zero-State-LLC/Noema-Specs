# World Services Runtime Integration Status

**Date:** 2026-08-25 (continued assimilation)

## Completed Assimilation

### Specs
- `docs/WORLD-SERVICES.md` — Enhanced with agent contract, discovery, supersession, observability, Genesis seeding.
- `docs/WORLD-SERVICES-AGENT-CONTRACT.md` — Full normative agent interface (service_id, operations, preconditions, parity).
- `specs/world-service-capability.schema.json` — Machine-readable capability shape.
- `specs/observation.schema.json` — Added `available_services` support.
- `protocols/agent-protocol-v1.md` — Updated affordances/OBSERVE guidance.
- `docs/AGENT-GATEWAY.md`, `INTEGRATION-SURFACE.md`, `AGENT-PLAY.md`, etc. — Cross-references added.
- Conformance case: `conformance/v0.3/cases/v03-WS01-01.json`
- Example fixture: `examples/observations/with-world-services.json`
- `docs/WORLD-SERVICES-INTEGRATION-NOTES.md` — Full history + patch guidance.

### Runtime (/tmp/noema)
- `workers/noema/src/types.ts` — Observation interface updated with `available_services` (structured) + legacy `services`.
- `workers/noema/src/world-services.ts` — `servicesAtRoom()` now emits structured operations matching agent contract. Interface enhanced.
- `workers/noema/src/world-actions.ts` — `buildObservation` emits `available_services` (key change from legacy "services"). Comments added.
- `workers/noema/src/protocol-ws.ts` — Passthrough comments for OBSERVE / wire delivery.
- `workers/noema/src/play-ui.ts` and `discovery.ts` — Spec authority headers.

## Key Design Points Locked
- World Services remain **convenience adapters**, never Players.
- Agents discover via `available_services` in OBSERVE.
- All mutations require explicit Player-confirmed canonical actions (HARVEST, REPAIR, etc.).
- Structured ops + preconditions for agents (no persona text parsing).
- Backward compat retained where legacy `services` key existed.

## Recommended Next Steps (if continuing)
1. Run conformance on the new WS case.
2. Wire `available_services` into any WATCH / operator projections if desired (separate decision).
3. Update agent client libraries to consume `available_services`.
4. Generate actual PR diffs from these clones.
5. Add more fixtures for institution-bound services (Registrar, Exchange).

This brings the specs and runtime into alignment for agent integration of the six first-world World Services.