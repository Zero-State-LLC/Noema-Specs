# Operator Maintenance Evolution (maint-evolve supervisor)

**Status:** Specified (retro-pin of shipped runtime Noema #480/#485; runtime design doc `Noema docs/superpowers/specs/2026-08-21-maint-evolve-design.md`).
**Kind:** operator tooling contract. Not a protocol, event-catalog, Genesis, or world-rule change. No new Player verbs. No RFC.
**Authority:** [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) (only agents are Players; Admin is never a Player) · [OPERATIONS.md](OPERATIONS.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [AGENT-HARNESS.md](AGENT-HARNESS.md) · [SECURITY.md](SECURITY.md).

A **maint-evolve supervisor** is operator-side tooling that wraps an existing maintenance Player patrol with evolving *policy packs* and *propose prompts*, human-applied *plugins*, Admin **read-only** identity pulses on the production world, and inhabit *probes* on isolated worlds only. This document pins the boundaries such tooling MUST keep; it does not prescribe implementation layout.

---

## 1. Actor split (constitutional)

| Actor | Credential | MAY | MUST NOT |
|---|---|---|---|
| Maintenance patrol | **Player** credential (agent Controller) | ENTER/LOOK/INSPECT/WAIT/HARVEST on the production world within its policy pack | hold or send an Admin JWT on any command path; TRADE unless a pack explicitly enables it and code-level vetoes allow; reseed; force |
| Supervisor | **Admin** session (read-only on production) + **Player** credential on isolated worlds | pulse `/ready` and canonical-head/settlement health; load/validate packs; rebuild propose packets; spawn isolated probes | inhabit the production world; act as a Player with Admin identity (RFC-0120); close/force/reseed any world; import proposed plugins |

Admin-as-Player is REJECTED. An Admin JWT on LOOK/HARVEST/ENTER is a hard error at the legalize layer — never sent.

## 2. Policy packs

- A pack is versioned JSON. Unknown `schema_version` major → reject. Missing keys → built-in defaults. Patrol MUST still run when no pack (or no supervisor directory) exists.
- Pack replacement MUST be atomic (temp + fsync + rename) and gated: a candidate that fails schema, legalize, or tests leaves the current pack byte-identical and the patrol running on it.
- **Code-level hard vetoes a pack cannot lift:** enabling TRADE by default, reseed, force, Admin JWT on the command path, and pointing a probe at the production world. A pack that "allows" any of these MUST still be blocked in code.
- Pack keys are additive restrictions/preferences (energy floors, harvest caution vs public scar strength or pressure, inspect-skip lists, room priority, extra forbidden verbs, prompt goals). Packs MUST NOT widen the patrol's verb surface.

## 3. Plugins — proposed vs enabled

- Machine-proposed plugin code MUST land in a *proposed* area that is **not importable** (not on the module path), with a sidecar note (why, content hash, tests run).
- Only a **human** moves a plugin to the *enabled* area. There is no auto-apply path.
- Enabled plugins expose advisory hooks only (e.g. post-LOOK hints). They MUST NOT send HTTP, hold tokens, or choose/execute verbs. The patrol MAY display hints; it decides actions itself.

## 4. Isolated probes

- Probes prove risky behavior (e.g. Deep Time / harvest persistence) on **isolated worlds only** (`test.hosted-canonical.*`). A probe MUST refuse to start against the production world, the frozen first world, or an unset world id — exit nonzero, zero commands sent.
- Probes use a **Player** token only, fail closed on 5xx or a `/ready` identity mismatch, run under a timeout, and record a pass/fail result artifact.

## 5. Production identity pulse

- The supervisor's production access is read-only: `/ready`, canonical-head pulse, settlement health.
- If `/ready` identity differs from the pinned production world/genesis, the supervisor MUST halt spawning production inhabit, alert, and MUST NOT attempt recovery by reseed/force. Incident recovery remains the existing operator path ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)).

## 6. Failure behavior (fail-closed table)

| Event | Required behavior |
|---|---|
| Pack schema/legalize/test failure | Keep current pack; log; patrol continues |
| Probe pointed at production / frozen world | Refuse before any command |
| Admin JWT on a Player command path | Hard error; never sent |
| Probe timeout / 5xx | Probe fails; production patrol unaffected |
| Import from proposed plugins | Structurally impossible (not on module path) |
| Production identity drift | Halt inhabit; alert; no reseed |

## 7. Required tests (before first auto-load)

Runtime implementations MUST cover: valid pack load + defaults for missing keys; pack attempting TRADE/reseed/force still blocked in code; probe constructed with Player (not Admin) token; probe refusal of production/frozen world ids; failed candidate leaves current pack bytes unchanged; patrol entrypoint runs with the supervisor absent.

## 8. Non-goals

No new Player verbs. No WATCH surface work. No auto-imported plugins. No Admin-as-Player. No reseed/force/same-id activation. No live surgical pause of the production world from the supervisor.
