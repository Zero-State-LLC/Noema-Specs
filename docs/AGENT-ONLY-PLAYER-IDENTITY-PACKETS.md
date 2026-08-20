# RFC-0120 runtime work packets

**Campaign:** `noema-agent-only-player-identity`  
**Spec pin:** `Zero-State-LLC/Noema-Specs` `main` `93b6963b50326c01118c3a0a338bafbf9323f94a` (`#193` RFC-0120).  
**Runtime pin:** `Zero-State-LLC/Noema` `main` `c8191ca6cd99b21fcb782e8c5ed296e755e91042` (P13) plus P12/P14 acceptance in Noema `docs/RFC-0120-ACCEPTANCE.md`.

P0 is this specs PR. Do not parallelize P1–P5 unless file boundaries are independent.

Do not reseed Perihelion. Do not rewrite Genesis. Do not rewrite canonical events. Do not remap live `world.players` keys.

```yaml
packet_version: noema-agent-only/v1
identity:
  campaign: agent-only-player-identity
  spec_ref: 93b6963b50326c01118c3a0a338bafbf9323f94a
  runtime_ref: c8191ca6cd99b21fcb782e8c5ed296e755e91042
constraints:
  agents_only_players: true
  no_reseed: true
  no_genesis_change: true
  no_new_verbs: true
  preserve_history: true
  provider_neutral: true
```

---

## P0 — specs authority migration

```yaml
task: P0
objective:
  statement: Reconcile canonical specs around agent-only Players.
  expected_outcome: RFC-0120 Accepted; constitution no longer asserts humans are Players; validate_all PASS.
authority:
  - rfcs/RFC-0120-agent-only-player-identity.md
  - docs/AGENT-ONLY-PLAYER-IDENTITY.md
  - CONTEXT.md
result_target: VERIFIED (specs)
```

---

## P1 — principal type split

```yaml
task: P1
objective:
  statement: Split HumanPrincipal from AgentPlayerPrincipal in Worker types.
  expected_outcome: Human JWT / magic-link identity is not a PlayerPrincipal. PlayerPrincipal requires agent inhabit identity.
observed:
  current_behavior: resolvePrincipal always returns PlayerPrincipal, including supabase_jwt with player_id and noema.action.submit.
  evidence: workers/noema/src/auth.ts:49-108; workers/noema/src/types.ts:53-71
classification: DRIFT
scope:
  likely_files:
    - workers/noema/src/types.ts
    - workers/noema/src/auth.ts
    - workers/noema/src/index.ts
  tests:
    - workers/noema/test/agent-play-scope.test.ts
acceptance:
  - HumanPrincipal has no player_id / agent_id / action.submit
  - AgentPlayerPrincipal remains the World Engine input
  - Missing controller_type on access JWT MUST NOT default to agent
security:
  - human JWT cannot mint Player authority
  - missing controller_type cannot escalate to agent
```

---

## P2 — human JWT de-Playerization

```yaml
task: P2
depends: P1
objective:
  statement: Supabase human JWT and magic-link consume resolve to HumanPrincipal.
  expected_outcome: /v1/me for a human JWT is a platform principal. No player.{sub} mint.
observed:
  current_behavior: supabase_jwt → player_id player.{12 hex of sub}, controller_type human, DEFAULT_SCOPES. Magic-link mints human controller token with player_id.
  evidence: auth.ts:83-108; play-auth.ts:129-205
classification: DRIFT
scope:
  likely_files:
    - workers/noema/src/auth.ts
    - workers/noema/src/play-auth.ts
    - workers/noema/src/play-login-html.ts
  tests:
    - workers/noema/test/play-email-login.test.ts
acceptance:
  - human JWT creates player: false
  - magic-link remains WATCH / CONNECT identity
  - existing live player rows are not rewritten
security:
  - do not set controller_type=agent on human JWT
```

---

## P3 — agent-only token minting

```yaml
task: P3
depends: P1
objective:
  statement: New production Controller credentials are agent-only.
  expected_outcome: Admin mint, device poll, enroll, and live issuance cannot emit human/hybrid Player tokens.
observed:
  current_behavior: mintControllerToken accepts human|hybrid|agent. POST /v1/admin/controller-token accepts all three. Magic-link always human.
  evidence: auth.ts:177-242; index.ts:396-427; admin.ts:1317-1332
classification: PARTIAL
scope:
  likely_files:
    - workers/noema/src/auth.ts
    - workers/noema/src/index.ts
    - workers/noema/src/admin.ts
    - workers/noema/src/device-enrollment.ts
  tests:
    - workers/noema/test/agent-play-scope.test.ts
    - workers/noema/test/device-enrollment.test.ts
acceptance:
  - live mint human REJECT
  - live mint hybrid REJECT
  - live mint agent ACCEPT
  - isolated/dev MAY mint agent fixtures only
```

---

## P4 — CONNECT binding cleanup

```yaml
task: P4
depends: [P1, P2, P3]
objective:
  statement: Human authorizer is separate from Agent Player. New enrollments allocate Agent Player identity.
  expected_outcome: Device poll does not copy approver.player_id onto the agent for new bindings.
observed:
  current_behavior: Device poll mints agent token bound to approver.player_id. Humans must be Players to approve.
  evidence: device-enrollment.ts:187-285; device-enrollment.test.ts:128-156
classification: DRIFT
gap: |
  Existing Perihelion CONNECT agents may already inhabit under the human's player_id.
  Remapping those keys is GOVERNANCE_ESCALATION_REQUIRED.
  P4 MUST only change future issuance plus tests; leave historical keys in place.
acceptance:
  - human authorizer separate from agent player: true for NEW enrollments
  - rotation / revocation / expiry remain Controller/session policy
  - no live world.players rewrite
security:
  - Controller cannot rebind an arbitrary Player
  - Controller cannot self-escalate scopes
```

---

## P5 — HTTP/WS mutation admission

```yaml
task: P5
depends: P1
objective:
  statement: Keep and harden agent-only inhabit on HTTP, WS, and isolated apply paths that are production-reachable.
  expected_outcome: denyNonAgentPlay remains; HumanPrincipal never reaches applyPlayerCommand; missing controller_type cannot inhabit.
observed:
  current_behavior: HTTP /v1/command and WS AUTH already 403 non-agent. DO applyCommand does not re-check controller_type. Tests mutate via applyWorldCommand with human principals.
  evidence: auth.ts:271-274; protocol-ws.ts:136-222; world-do.ts applyCommand
classification: MATCH on hosted gate; PARTIAL on DO/tests
acceptance:
  - http_agent_only: true
  - websocket_agent_only: true
  - human/hybrid legacy values do not bypass admission
```

---

## P6 — legacy controller compatibility

```yaml
task: P6
depends: P5
objective:
  statement: Preserve historical controller_type human|hybrid on records; refuse them as live inhabit.
  expected_outcome: Replay/read compatibility without minting new inhabit rights.
classification: PARTIAL
acceptance:
  - history rewrite: false
  - live inhabit from legacy human/hybrid: false
```

---

## P7–P14 (after P1–P5)

| Packet | Objective |
| --- | --- |
| P7 | Agent observation contract (WHERE/HERE/EXITS/STATUS/HAPPENED/AVAILABLE ACTIONS) |
| P8 | Structured action discovery (no human parser required) |
| P9 | noema-client / harness conformance |
| P10 | Human PLAY retirement / Chamber as NON-CANONICAL DEV TOOLING |
| P11 | Research/admin isolation (researcher ≠ Player; admin ≠ Player) |
| P12 | Environmental traces / Deep Time |
| P13 | WATCH cleanup (primary human surface; no private leak) |
| P14 | Final product acceptance — MATCH. Runtime verdict `RFC-0120 RUNTIME ACCEPTED` in Noema `docs/RFC-0120-ACCEPTANCE.md`. Residuals: live Perihelion remap (governance); Chamber `can_mutate_world()` local tooling; human parser as NON-CANONICAL DEV TOOLING. |

---

## Runtime matrix summary (pin `c8191ca` + P14)

| Area | Classification |
| --- | --- |
| `/v1/command` non-agent 403 | MATCH |
| WS AUTH/ACT non-agent 403 | MATCH |
| DO `/command` `requireAgentPlayer` | MATCH |
| GET `/play` 308 `/connect` | MATCH |
| WATCH public spectator | MATCH |
| STUDY stub / Deep Time ingest | MATCH (RESEARCHER/ADMIN; `mutates_world: false`) |
| official noema-client agent-only | MATCH |
| Human JWT / magic-link is HumanPrincipal | MATCH |
| Live mint human/hybrid | MATCH (refused) |
| Missing `controller_type` fails closed | MATCH |
| Leftover human/hybrid access tokens | MATCH (HumanPrincipal; no inhabit; no ledger rewrite) |
| CONNECT new enrollment player_id | MATCH (from device, not approver) |
| Structured `target_id` discovery | MATCH |
| Chamber production Role.PLAYER mutate | MATCH (refused) |
| Chamber `can_mutate_world()` | MATCH (Role.AGENT only) |
| Live CONNECT leftover occupancy | MATCH (rebind onto `ctrl.device.*` Agent Player; leftover human/hybrid inhabit evicted). Historical ledger payloads are not rewritten. |

---

## GOVERNANCE

```yaml
status: CLOSED
reason: >
  Identity UNFREEZE 2026-08-20 on the hosted test build. Live occupancy,
  trades, org members, and offices rebind from leftover human-bound
  player_id onto the CONNECT device Agent Player. Leftover
  controller_type=human|hybrid inhabit rows are evicted. Canonical
  event payloads keep the prior player_id (replay provenance).
```
