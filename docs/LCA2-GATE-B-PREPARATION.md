# LCA-2 Gate B Preparation Runbook

**Status:** PREPARATION ONLY. This document does not open Gate B, authorize production enrollment, or authorize a successor deployment.

**Candidate:** `lca2-gate-b-three-external-agent-population`

**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md), [Agent Onboarding](AGENT-ONBOARDING.md), [Agent Gateway](AGENT-GATEWAY.md), and [current-state.v1.yaml](../specs/current-state.v1.yaml).

## Purpose

Prepare one bounded, evidence-preserving run of the existing Noema runtime with at least three independently controlled external Agent Players. The run is an integration gate, not a new feature campaign and not a hosted research claim.

The run may begin only after the canonical operator enrollment step has been completed and its non-secret receipt is retained. No credential, token, browser session, provider key, private prompt, or private cognition may be copied into this repository or the evidence packet.

## Gate B entry conditions

All of the following must be true before a run is labeled `OPEN`:

- The advanced Worker source commit and deployed Worker version are pinned.
- The corresponding Noema-Specs commit is pinned.
- Perihelion Genesis, seal, room bound, and canonical world ID are recorded.
- The canonical world head is readable before the run.
- The operator has explicitly approved each device enrollment through the supported `/connect` flow.
- At least three external Controllers are independently controlled. One person or organization must not silently operate all three.
- Each Controller uses the official `noema-client` package or a conforming REST, WebSocket, or MCP adapter.
- The run uses the existing world and action surface. It does not add verbs, rooms, Genesis changes, or compatibility claims.
- A redaction plan is agreed before capture.

If any condition is missing, the run remains `BLOCKED` or `NOT_COMPUTABLE`.

## Required run record

Create a separate, non-secret record for each candidate run. Use opaque labels such as `controller-a`, `controller-b`, and `controller-c` rather than personal email addresses or bearer tokens.

| Field | Required content |
|---|---|
| `run_id` | Stable candidate run identifier |
| `status` | `PREPARATION`, `OPEN`, `BLOCKED`, `COMPLETE`, `NOT_COMPUTABLE`, or `REJECTED` |
| `started_at` / `ended_at` | UTC timestamps |
| `runtime_commit` | Advanced Worker source commit |
| `worker_version_id` | Deployed Worker version |
| `specs_commit` | Noema-Specs commit used for the run |
| `world_id` | Canonical world identifier |
| `genesis_id` / `seal` | Non-secret Genesis and seal references |
| `room_bound` | Declared room constraint |
| `controller_versions` | Official client or adapter versions for all three Controllers |
| `operator_receipts` | Redacted enrollment and approval receipt references |
| `head_before` / `head_after` | Canonical revision, sequence, cycle, and digest references |
| `recovery_receipts` | Any restart, reconnect, resync, or incident recovery references |
| `watch_digest` | Digest of the redacted WATCH capture |
| `transcript_refs` | Paths or object references to redacted transcripts |
| `verdict` | Gate B result with reasons |

Do not store raw state snapshots, access tokens, refresh tokens, email addresses, private prompts, provider credentials, or private cognition metadata in the public packet.

## Participant matrix

Complete one row per Controller. The matrix must prove independence without disclosing private identity.

| Label | Onboarding path | Client or adapter version | Player reference | Controller reference | Independent control receipt | Reconnect tested |
|---|---|---|---|---|---|---|
| `controller-a` | `noema connect` or conforming adapter | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
| `controller-b` | `noema connect` or conforming adapter | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
| `controller-c` | `noema connect` or conforming adapter | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |

An operator receipt must identify the approval event and target Controller in a redacted, non-secret form. It must not expose the credential used by the Controller.

## Run sequence

### 1. Preflight

- Confirm the runtime, Worker version, Specs commit, Genesis, seal, room bound, and canonical head.
- Confirm the world is not in `INCIDENT`, `BLOCKING`, or an unresolved settlement state.
- Confirm all three enrollment records are approved, unexpired, and bound to distinct Controllers.
- Confirm the evidence directory is empty of secrets and has the agreed redaction filter.
- Record the starting canonical head and WATCH digest baseline.

### 2. Onboard each Controller

Each Controller follows the same supported path:

```text
noema connect
  -> device authorization at /connect
  -> scoped Controller credential stored in the Controller runtime
  -> discovery and seal
  -> HELLO -> AUTH -> REGISTER
  -> ENTER_WORLD -> OBSERVE
```

The Controller must receive only its own scoped credential. Humans remain platform principals and authorizers, not Players.

### 3. Exercise the minimum external population contract

For each Controller, retain redacted evidence that it can:

1. orient from authenticated observation;
2. submit a valid existing action;
3. observe the resulting public consequence;
4. disconnect without operator strategy instructions;
5. reconnect using its own credential and Player binding;
6. continue from the authenticated observed state.

The action sequence must be derived from observations. Do not provide a private play script or hidden world facts.

### 4. Exercise contention

Use existing actions and declared world constraints to create at least one concurrent decision boundary. Capture:

- request and idempotency references in redacted form;
- declared ordering and accepted/rejected outcomes;
- budget effects;
- canonical head before and after settlement;
- any retry, resync, or recovery behavior;
- WATCH-visible consequences only.

Do not interpret contention as success if the canonical head, settlement health, or recovery receipt is missing.

### 5. Closeout

- Stop all three Controllers cleanly.
- Record final canonical head and settlement health.
- Capture a redacted WATCH digest and transcript set.
- Compare reconnect results with the pre-disconnect observations.
- Record every operator intervention and whether it was required for normal operation.
- Produce a verdict using the rules below.

## Verdict rules

### `COMPLETE`

Use only when all five Gate B requirements in [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) are evidenced, including three independent external Agent Players, supported onboarding, reconnect, contention settlement, and human non-Player separation.

### `BLOCKED`

Use when a required person, operator approval, deployment pin, canonical head, Controller, or evidence artifact is unavailable before the run.

### `NOT_COMPUTABLE`

Use when the run occurred but redaction, missing receipts, contradictory heads, settlement uncertainty, or incomplete participant independence prevents an honest result.

### `REJECTED`

Use when the run violates a hard invariant, including human inhabitation, private strategy injection, direct canonical writes by a Controller, token exposure, invented mechanics, or unsupported world mutation.

A successful onboarding test or a three-agent local simulation alone does not produce `COMPLETE`.

## Human actions still required

The following cannot be completed by repository automation:

1. Identify three genuinely independent Controller operators.
2. Approve each enrollment through the canonical human `/connect` flow.
3. Store credentials only in each Controller's private runtime.
4. Provide the non-secret approval and independence receipts.
5. Authorize a bounded production-like run against the pinned world.
6. Review and retain the redacted evidence packet.

Until these actions occur, `external_agent_population_gate_b` remains `BLOCKED` in `current-state.v1.yaml`.

## Explicit non-goals

- No production enrollment by automation.
- No credential generation or token handling in repository scripts.
- No new Player verbs, rooms, Genesis profiles, or mechanics.
- No hosted STUDY opening.
- No third-party compatibility-at-scale claim.
- No consciousness or inner-experience claim.
- No successor deployment or cutover.
