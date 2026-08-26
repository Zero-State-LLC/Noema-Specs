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

## Push Status (2026-08-25) — SUCCESS

**Branches created:**
- Noema-Specs: `world-services-agent-contract-integration`
- Noema: `world-services-agent-contract-integration`

**Push results:**
- Both pushes **succeeded** after CLI auth.
- Commits are local on the branches in /tmp clones.

**Patch bundles generated (ready to apply or attach to PR):**
- /tmp/world-services-specs.patch (60KB, full changes for Noema-Specs)
- /tmp/world-services-runtime.patch (7.5KB, runtime worker changes)

**Branches pushed:****
```bash
cd /tmp/noema-specs
git push -u origin world-services-agent-contract-integration

cd /tmp/noema
git push -u origin world-services-agent-contract-integration
```

Or use the patches:
```bash
git apply /tmp/world-services-specs.patch
git apply /tmp/world-services-runtime.patch
```

## PR Preparation
A draft PR description has been added below (see PR-DESCRIPTION.md).

All changes preserve existing behavior where possible and follow the closed-capability model.

## Deliverables for User
- Patches copied to:
  ~/world-services-specs.patch
  ~/world-services-runtime.patch

- PR description: /tmp/noema-specs/PR-DESCRIPTION.md
- Status: /tmp/noema-specs/RUNTIME-INTEGRATION-WS-STATUS.md

Branches in clones:
- /tmp/noema-specs (branch: world-services-agent-contract-integration)
- /tmp/noema (branch: world-services-agent-contract-integration)

Next recommended: manual push from your machine using the patches or direct from the /tmp clones after configuring git credentials.


## GitHub Branches (live)
- Specs: https://github.com/Zero-State-LLC/Noema-Specs/tree/world-services-agent-contract-integration
- Runtime: https://github.com/Zero-State-LLC/Noema/tree/world-services-agent-contract-integration

## Create PRs
Use these direct links:
- Noema-Specs PR: https://github.com/Zero-State-LLC/Noema-Specs/pull/new/world-services-agent-contract-integration
- Noema PR: https://github.com/Zero-State-LLC/Noema/pull/new/world-services-agent-contract-integration

Patches in ~/ are still available as backup.

## Additional Work After Push
- Added conformance case v03-WS01-02 + no-services.json fixture for the "no World Services" scenario.
- This covers the edge case of rooms with zero applicable desks.
