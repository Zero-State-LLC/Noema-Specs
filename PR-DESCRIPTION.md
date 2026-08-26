# PR: World Services Agent Contract + Runtime Integration

**Branches (pushed):**
- Specs: https://github.com/Zero-State-LLC/Noema-Specs/tree/world-services-agent-contract-integration
- Runtime: https://github.com/Zero-State-LLC/Noema/tree/world-services-agent-contract-integration

**Direct PR creation:**
- Specs: https://github.com/Zero-State-LLC/Noema-Specs/pull/new/world-services-agent-contract-integration
- Noema: https://github.com/Zero-State-LLC/Noema/pull/new/world-services-agent-contract-integration


## Summary
This PR introduces the normative agent-facing contract for first-world World Services and integrates it into the runtime so agents can discover and use them via structured observations.

**Core change:** World Services (Exchange Broker, Quartermaster, Registrar, Relay Keeper, Archivist, Contract Clerk) are now exposed to agents as `available_services` in observations with machine-readable operations, preconditions, and status — while remaining strict convenience adapters (never Players).

## Key Additions
- `docs/WORLD-SERVICES-AGENT-CONTRACT.md` — Full normative specification for how agents see `service_id`, operations, preconditions, and parity with human presentation.
- Enhanced `docs/WORLD-SERVICES.md` — Discovery rules (location vs institution bound), supersession model (explicitly DEFERRED), observability, Genesis seeding, and per-service "Agent View".
- `specs/world-service-capability.schema.json` — Starter JSON Schema for the capability shape.
- Updates to `observation.schema.json`, `agent-protocol-v1.md`, `AGENT-GATEWAY.md`, `INTEGRATION-SURFACE.md`, and related docs.
- New conformance case `v03-WS01-01` and example observation fixture.

## Runtime Changes (Noema)
- `types.ts`: Added `available_services` to `Observation` interface with structured operations.
- `world-services.ts`: `servicesAtRoom()` now emits operations in the contract-expected object form.
- `world-actions.ts`: Observations now emit under the `available_services` key; mapping and comments updated.
- `protocol-ws.ts`: Passthrough notes for wire delivery.

## Principles Preserved
- No new verbs or top-level service actions.
- All state changes require explicit Player confirmation of canonical actions (HARVEST, REPAIR, TRADE, ORG_*, etc.).
- Closed capabilities only.
- LLM/presentation layers have no authority.
- Backward compatibility retained for legacy `services` key where it existed.

## Testing / Validation
- New conformance case exercises `available_services` shape and rules.
- Example fixture: `examples/observations/with-world-services.json` (Relay + Quartermaster).
- Runtime changes keep existing observation paths working.

## Related
See `docs/WORLD-SERVICES-INTEGRATION-NOTES.md` and `RUNTIME-INTEGRATION-WS-STATUS.md` for full history.

## How to Test (Agent Side)
1. Enter a room with infrastructure or resource nodes.
2. OBSERVE.
3. Inspect `available_services` for `service_id`, structured `operations`, `status`, `preconditions`.
4. Submit canonical actions (e.g. `HARVEST` on the target entity) — the service only prepares.

## Status
Ready for review. Branches:
- Noema-Specs: world-services-agent-contract-integration
- Noema: world-services-agent-contract-integration

Patches available in the working session if direct push is needed.