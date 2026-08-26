# World Services Spec Enhancements — Integration Notes

**Date:** 2026-08-25 (drafted in analysis session)

## What was added

1. **New normative document**: `docs/WORLD-SERVICES-AGENT-CONTRACT.md`
   - Structured agent discovery (`service_id` in observations)
   - Exact shapes for `available_services` and `AVAILABLE_ACTIONS`
   - Capability table from agent perspective
   - Protocol usage examples
   - Preconditions, error handling, parity rules

2. **Enhanced `WORLD-SERVICES.md`** (see `WORLD-SERVICES.md.enhanced`)
   - Strengthened "Offices vs Services" disambiguation section
   - New "Discovery Rules" section (location-bound vs institution-bound)
   - Added "Agent Structured Interface" section pointing to the new contract
   - New "Supersession by Player Institutions" section (explicitly DEFERRED)
   - New "Observability" section (Admin Live + WATCH + events)
   - New "Genesis Seeding" section
   - Extended every service table with "Agent View" row
   - Updated Acceptance criteria (added agent parity item)
   - Cross-links to the new agent contract

3. **Machine-readable schema starter**: `specs/world-service-capability.schema.json`
   - JSON Schema for the agent-facing service descriptor
   - Can be referenced from observation schema or agent protocol in future

## Integration Steps (recommended)

1. Review the drafts for terminology and cross-link consistency.
2. Replace or merge `docs/WORLD-SERVICES.md` with the content from `WORLD-SERVICES.md.enhanced`.
3. Add the new file `docs/WORLD-SERVICES-AGENT-CONTRACT.md` to the repo.
4. Add the schema to the specs/ directory and update any index or validation lists.
5. Update `docs/TERMINOLOGY.md` if needed (the "World Service" entry is already accurate; may add pointer to the new contract).
6. Add cross-references from:
   - `docs/AGENT-PLAY.md`
   - `docs/AGENT-GATEWAY.md`
   - `protocols/agent-protocol-v1.md` (optional future)
   - `docs/FIRST-WORLD-SPEC-FREEZE.md` (if you want to call out the agent contract)
7. Run existing spec validation / conformance checks.
8. Update CHANGELOG.md with a note about the agent contract and discovery rules.

## Files created in this draft session

- `/tmp/noema-specs/docs/WORLD-SERVICES-AGENT-CONTRACT.md`
- `/tmp/noema-specs/docs/WORLD-SERVICES.md.enhanced`
- `/tmp/noema-specs/specs/world-service-capability.schema.json`
- This notes file

## Key principles preserved

- Services are **never** Players or persistent system agents.
- Closed capabilities.
- Player confirmation for all writes.
- Agent parity without special privileges.
- Supersession remains deliberately deferred.

## Open items for follow-up

- Wire the new `available_services` shape into the actual observation schema (future RFC or minor update).
- Implement full `servicesAtRoom` + institution discovery logic in the runtime to match the new contract.
- Decide on any additional world events for service consultation (currently routed through existing action events).

Contact the spec maintainers for review before merging.


## Status Update (continued session)

- Core files integrated: WORLD-SERVICES.md replaced with enhanced version.
- Cross-references added to AGENT-PLAY.md, PLAYER-ACTION-MAP.md, INSTITUTIONAL-AUTHORITY.md, FIRST-WORLD-SPEC-FREEZE.md.
- CHANGELOG.md entry added under Unreleased.
- Schema and new agent contract remain in place.
- Ready for review and real-repo merge.

## Assimilation for Runtime Integration (completed)

- Protocol: Added World Services note in agent-protocol-v1.md (affordances / OBSERVE section).
- Schema: observation.schema.json now documents the available_services extension pointing to world-service-capability.schema.json.
- Gateway: AGENT-GATEWAY.md updated to call out service_id capabilities in observations.
- Completeness plan: Updated table entry.
- Runtime: workers/noema/src/world-services.ts header comment updated to cite full spec set (AGENT-CONTRACT + schema).
- All changes preserve existing structure, use canonical cross-links, and prepare direct consumption by agent runtimes and gateways.
- No new verbs or authority model changes.

The specs are now assimilated and ready for runtime teams to implement against (e.g., extend OBSERVE responses, wire service capabilities in AVAILABLE_ACTIONS, align world-services.ts logic with the agent contract tables).

Next typical steps for full runtime integration:
- Implement available_services in observation projections.
- Wire service capabilities into the agent gateway affordance builder.
- Add conformance tests referencing the new schema and contract.

## Further Runtime Assimilation (this continuation)

- observation.schema.json: Formal `available_services` property added (references world-service-capability.schema.json).
- Runtime files updated with authority comments:
  - workers/noema/src/world-actions.ts
  - workers/noema/src/play-ui.ts
  - workers/noema/src/discovery.ts
- Additional spec surfaces assimilated:
  - docs/AGENT-INTERFACE.md
  - docs/LLM-AGENT-INTEGRATION.md
- Protocol, Gateway, and completeness plan already cross-linked.

The agent contract is now referenced from:
- Core protocol
- Observation schema
- Gateway
- Agent play surface docs
- Runtime service and UI code

This enables direct implementation:
- Gateway can emit available_services in OBSERVE
- UI and actions can surface service_id consistently
- Agents get machine-readable service capabilities without parsing text.

Ready for:
- Adding sample observation fixtures with services
- Updating conformance cases
- Runtime PRs that cite these specs

## Runtime Code Integration (continued)

- Enhanced ServiceView in world-services.ts to produce structured operations matching agent contract.
- Changed observation key from "services" to "available_services" in buildObservation.
- Added available_services: [] to emptyPlayObservation.
- Added example fixture: examples/observations/with-world-services.json
- Added section to docs/INTEGRATION-SURFACE.md for runtime teams.

This completes the core assimilation loop: specs define the shape → runtime produces it in observations → agents consume via protocol/gateway.

Next recommended (if continuing): 
- Add conformance test case
- Update observation fingerprint or other projections
- Generate diff for PR to both repos

## Runtime Integration Continuation (this step)

- Updated Observation interface in workers/noema/src/types.ts:
  - Added canonical `available_services` with structured operations.
  - Retained legacy `services` for compatibility.
  - Operations now support object form {action, target, preconditions, description}.

- Added conformance case: conformance/v0.3/cases/v03-WS01-01.json
  - Validates `available_services` presence, service_id format, structured operations, and "no direct mutation" rule.
  - References the agent contract and schema.

- Extended protocol-ws.ts:
  - Added comments for OBSERVE passthrough of available_services.
  - Ensures World Service data reaches agent clients on the wire.

- Refined world-actions.ts buildObservation:
  - Confirmed mapping to available_services uses the structured shape from world-services.ts.

- All changes align runtime output with specs/WORLD-SERVICES-AGENT-CONTRACT.md.

This makes the feature testable via conformance and ready for gateway/agent consumption.

## Patch / Diff Summary (generated)

To apply these runtime integration changes:

1. Specs repo:
   - Copy or merge the enhanced WORLD-SERVICES.md
   - Add WORLD-SERVICES-AGENT-CONTRACT.md
   - Add specs/world-service-capability.schema.json
   - Add examples/observations/with-world-services.json
   - Add conformance/v0.3/cases/v03-WS01-01.json
   - Apply cross-references and schema updates

2. Runtime (Noema worker):
   - Apply changes to workers/noema/src/types.ts (Observation interface)
   - Apply changes to workers/noema/src/world-services.ts (structured ops)
   - Apply changes to workers/noema/src/world-actions.ts (available_services key + mapping)
   - Apply changes to workers/noema/src/protocol-ws.ts (passthrough comments)

All changes preserve backward compatibility where possible and follow the "services are not players" doctrine.

Full git diff stats available in the working clones.

## Post-Push Continuation (after CLI auth)

- Successfully pushed both branches to origin.
- Added second conformance case: v03-WS01-02 (empty available_services for rooms without services).
- Added supporting fixture: examples/observations/no-services.json.
- Updated RUNTIME-INTEGRATION-WS-STATUS.md and PR-DESCRIPTION.md with live GitHub links.
- Runtime header added in world-actions.ts.

Branches are now live on GitHub. User can open PRs directly from the links.
