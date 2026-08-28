# Noema-Specs / Noema Runtime Reconciliation Audit

**Audit date:** 2026-08-28 16:15 PDT  
**Scope:** Read-only reconciliation of `Zero-State-LLC/Noema-Specs` against `Zero-State-LLC/Noema`. No runtime code, generated verbs, or deployment state was changed.

## Evidence baseline

| Surface | Observed value |
|---|---|
| Specs `origin/main` | `aa528d100bbb3dd4264694e94b0fe97c1a082d76` |
| Runtime `origin/main` | `5797c1383cd3e9066c1677789672b4539f835160` |
| Live world | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Live readiness | `ACTIVE`, `ready=true`, `playable=true`, `settlement_health=HEALTHY` |
| Live Worker | `772e244c-52b8-41bf-bdf4-ea600db4f15f`, deployed `2026-08-25T22:54:48.805353Z` |
| Live source recorded by runtime `spec-compat.json` | `27f9aa8ee9344bb3ad41e91bf2f3c7b26cdd0b37` |
| Live build Specs pin recorded by runtime | `81ca8c1e6b1d1ca474cf31958439fb0bdb9a465c` |
| Live protocol | `agent-protocol/v1`, production Stage 0 |

The live source commit is present in the runtime repository and is an ancestor of runtime `origin/main`. The public `/ready` and `/version` responses agree on the world identity and protocol.

## Reconciliation result

### Aligned

1. **World identity and protocol:** Specs expects `world.perihelion-reach-3` and the same Genesis. The live `/ready`, `/version`, and runtime compatibility pin agree. Both sides use protocol version 1.
2. **Event catalog layering:** Specs defines 24 offline `event-catalog/0.1` types and 32 hosted `event-catalog/0.2` types. Runtime `spec-compat.json` explicitly assigns 0.1 to the offline Python runtime and 0.2 to the hosted Worker. The Worker references 30 of the 32 hosted catalog names. `SITUATION_INJECTED` and `NOISE_APPLIED` are intentionally Frontier/observation-spine events rather than hosted Worker producers. `CRIME_DETECTED` is catalogued and consumed by hosted projections but has no hosted producer, which matches the Specs audit notes.
3. **Public route boundary:** Specs documents `POST /v1/command`, `GET /v1/watch/live`, `/health`, `/ready`, and `/version`. Runtime implements those routes plus the public map and WebSocket stream surfaces. The public WATCH surface is projection-only and excludes private player/event fields.
4. **Action layering:** Specs uses canonical `COMMIT.HARVEST` and `COMMIT.REPAIR` operations. The Worker human adapter emits `COMMIT` with `operation=HARVEST|REPAIR`; the offline Python adapter exposes lower-level names such as `HARVEST`, `REPAIR`, and `TRADE_PROPOSE`. This is an explicit adapter-layer distinction, not evidence that the normative Specs catalog should be changed.

### Drift or reconciliation work required

| Severity | Finding | Classification | Safe next action |
|---|---|---|---|
| High | `specs/current-state.v1.yaml` records production Worker `01ebc196...` and source `61234cc`, while the live `/version` and runtime `spec-compat.json` record Worker `772e244c...` and source `27f9aa8...`. | **Stale snapshot versus current pointer ambiguity.** The file is labelled current state but its proof text describes the earlier Gate A promotion. | An operator should either refresh the current production pointer to the verified live values or explicitly label/archive this section as historical Gate A evidence. Do not silently rewrite the authority record.
| Medium | The current-state file's `as_of` date is `2026-08-25`, while the live deployment occurred later that day and the world has since advanced. | **Stale evidence timestamp.** | Update the timestamp only when the corresponding authority decision and evidence packet are approved.
| Medium | `docs/PLAYER-ACTION-MAP.md` says its hosted implementation appendix was inspected at runtime commit `7135e3f7`, which predates the current runtime main and live source. | **Stale non-normative implementation appendix.** | Refresh the appendix against runtime `27f9aa8...`, preserving its non-normative status and the existing adapter-divergence warnings.
| Medium | `validation/validate_freshness.py` verifies live world/Genesis and that `/version` has a Worker ID, but does not compare the live Worker ID or source provenance with `current-state.v1.yaml`. | **Validation coverage gap.** A stale current-state Worker pin can pass freshness validation. | Add a separate operator-authorized provenance check after deciding which artifact is authoritative. Do not make the current historical pin a hard live gate without first reconciling it.
| Low | Specs `.env.example` exposes 65 reference/local variables, while the Worker environment surface exposes 9 secret inputs plus 3 Wrangler variables. | **Intentional layered-environment difference, weakly documented as parity.** | Clarify in environment documentation that Specs reference configuration and Worker deployment configuration are different surfaces.

## Runtime acceptance evidence

The runtime baseline was not fully green at the audited runtime commit:

- The isolated Python reference suite passed: **437 passed, 3 skipped**.
- The Worker test baseline reported **214 passed, 10 failed, 13 skipped**, with failures concentrated in existing RFC-0120 agent-only expectations, enrollment URL expectations, and hosted action responses.
- Worker typecheck reported existing type errors in `world-do.ts`, RFC-0120 tests, and conformance harness typing.
- These runtime failures are outside the permitted Specs-only change scope and were not hidden by changing Specs.

The Specs side is green: canonical validation, direction validation, offline freshness validation, and the validator smoke suite pass on current Specs main. The live public `/ready`, `/version`, WATCH HTTP, WATCH live JSON, map, and WebSocket projection checks also passed during the surrounding acceptance run.

## Recommended reconciliation order

1. Resolve the **current-state versus runtime `spec-compat.json` authority question** with the operator responsible for production evidence.
2. Refresh the non-normative Player Action Map appendix against the current runtime source.
3. Add a provenance-specific validation check only after the authority decision, so it catches future publish lag without rejecting an intentionally historical evidence snapshot.
4. Keep Worker test/typecheck remediation in the Noema runtime repository. Do not weaken or rewrite Specs contracts to make those failures disappear.

## Audit conclusion

The core protocol, world identity, catalog layering, and public projection boundaries are reconciled. The material remaining issue is provenance freshness: the Specs current-state document still describes the earlier `61234cc` / `01ebc196...` Gate A deployment while the verified live deployment is `27f9aa8...` / `772e244c...`. This should be resolved as an explicit authority decision, not guessed from a later source checkout.
