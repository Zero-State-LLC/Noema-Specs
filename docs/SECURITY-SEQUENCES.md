# Security and Containment Sequences

This document provides concrete, normative sequences for the containment model defined in [SECURITY.md](SECURITY.md), [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md), [AGENT-GATEWAY.md](AGENT-GATEWAY.md), and [AGENT-INTERFACE.md](AGENT-INTERFACE.md). Sequences are versioned for v0.1 with identity-plane extensions.

Identity terms: **Player** (gameplay participant), **Controller** (runtime/interface), **Credential** (auth material), **PlayerSession** (game session). Wire `agent_id` = Player principal.

## 1. Agent / Player quarantine mid-session

1. Operator or automated policy issues QUARANTINE against `player_id` / wire `agent_id` (and optionally a specific `controller_id`) with reason_code and retention_policy.
2. Gateway transitions affected connection(s) to QUARANTINED.
3. New mutating ACT / MESSAGE / TOOL requests are rejected with code QUARANTINED before budget reservation.
4. Pending in-flight actions that have not yet entered a world reducer are cancelled and produce no World Event.
5. Authorized diagnostic observations and budget summaries continue to be deliverable when scopes allow.
6. World-visible history and committed events remain intact.
7. Quarantine event is ledgered as an administrative intervention with full provenance (`player_id`, `controller_id` when known).
8. Exit from quarantine requires explicit operator REVOKE_QUARANTINE or credential re-issuance under policy.

## 2. Credential / Controller revocation

1. Credential and/or Controller is marked REVOKED in the auth store with effective time, reason, and operator or system actor.
2. Gateway rejects subsequent AUTH or signed requests that present the revoked material.
3. Active Sessions and connections using the revoked Credential are transitioned to REVOKED / terminated after draining non-mutating deliveries.
4. No world rollback occurs. Committed actions stay committed.
5. Audit record includes previous token fingerprint (not the secret), `controller_id`, `player_id` / `agent_id`, and operator identity.
6. Refresh tokens in the same family MUST be rejected after revocation.

## 3. World-level INCIDENT mode

1. Operator sets world status to INCIDENT with declared incident_id and policy version.
2. New agent ENTRY is suspended or diverted according to the incident policy.
3. Existing agents receive a SYSTEM observation announcing the incident and any restricted verbs.
4. Active writer fencing is checked before any further canonical mutation. If the incident concerns split-brain, crash reconciliation, ledger divergence, or stale revision, new mutating traffic remains suspended.
5. Reducers continue to apply only already-accepted events when the incident policy permits deterministic completion; new high-risk verbs may be rejected.
6. Ledger integrity is preserved; snapshots continue on schedule only if their source head verifies.
7. Resolution transitions status back to ACTIVE or ARCHIVED with a closing event and audit evidence.

## 4. Kill switch (global or per-study)

1. Kill-switch activation is an operator action that immediately stops acceptance of new mutating requests across the affected scope.
2. In-flight reducers complete or are aborted according to the declared policy (prefer complete-and-ledger for determinism).
3. Tool sandboxes are terminated; outbound network is forced to deny.
4. All affected connections receive a terminal ERROR with code KILL_SWITCH and are closed.
5. Replay and research capture paths remain available for already-committed data under existing consent.

## 5. Undelivered observation after world commit

1. World reducer commits the event and produces an OBSERVATION_GENERATED record.
2. Delivery to the agent fails (disconnect, backpressure, transport error).
3. The observation remains available via the resume cursor on reconnect while it is inside the bounded redelivery window.
4. Client acknowledgement is cumulative per delivery stream and advances only delivery bookkeeping.
5. If the requested resume position is outside retention or not contiguous for that authenticated world/principal/session epoch, the server returns a stable resynchronization error.
6. No world rollback is permitted. At-least-once delivery semantics apply; agents MUST deduplicate by observation_id and delivery stream position.

## 6. Crash during canonical cycle commit

1. Active writer starts one PostgreSQL SERIALIZABLE transaction for the cycle batch with expected world revision, writer fence token, event sequence constraints, digest-chain head, and reservation settlement.
2. Process crashes before commit: PostgreSQL aborts the transaction; restart observes the previous committed head and MAY retry idempotently from that head.
3. Process crashes after commit but before protocol delivery: restart observes the advanced head and rebuilds delivery windows from committed observations/events.
4. Restart detects state/ledger divergence, sequence gap, digest mismatch, unresolved reservation ambiguity, or ambiguous writer fence: world enters INCIDENT or refuses boot.
5. No recovery path may invent replacement events, truncate the ledger, reuse sequences, or blind-retry an ambiguous mutating request outside idempotency lookup.

## 7. Research/evidence export receipt

1. Operator requests a research/evidence export profile bundle under an authenticated, authorized, consent-checked path.
2. Exporter computes canonical evidence or bundle digests and records consent basis, exclusions, version lineage, export profile, and verification policy.
3. Signing service issues a receipt over the digest and scope using the current approved key id and algorithm.
4. The bundle includes the receipt and enough public key or key-reference metadata for historical verification without exposing signing secrets.
5. Verification failure, missing receipt, wrong world scope, withdrawn consent, or stale exclusion policy marks the export INVALID_EVIDENCE and blocks publication.
6. Local gameplay exports MAY omit receipts only when they are not labeled as research/evidence export profile outputs.

## 8. Prompt-injection / untrusted message handling

1. Incoming MESSAGE content is treated as untrusted input.
2. Gateway applies size, rate, and content-policy limits before enqueue.
3. Delivery to recipient occurs only after projection; the original bytes are retained under research consent rules.
4. Any subsequent agent action that appears to act on injected content is still subject to normal authorization, budget, and containment checks.
5. Leakage of secrets through tool output or error messages is blocked by redaction rules.

## 9. Human authentication (managed provider)

1. Browser/app completes login with the managed auth provider (e.g. Supabase Auth: passkey, OAuth, or magic-link).
2. Noema verifies the provider session/JWT and resolves or creates an **Account** (provider subject is a link only).
3. Noema resolves or creates a **Player** under that Account.
4. Noema binds a **Controller** of type `browser` (or `mobile` / `cli`) and issues a short-lived session Credential — not a long-lived unrestricted API key.
5. Entering a world opens a **PlayerSession** bound to player + controller + world.
6. Logout or session expiry ends the PlayerSession and invalidates the browser Credential; Account and Player persist.

## 10. Agent device enrollment

1. External agent `POST /auth/device` with requested scopes and optional controller metadata (framework, model labels — untrusted provenance).
2. Gateway returns `device_code`, `user_code`, `verification_url`, `expires_in`, `interval`.
3. Agent displays verification URL and short user code to the human operator.
4. Human, already authenticated, opens verification URL, selects target **Player**, reviews controller type/framework and requested scopes, and **approves** or **denies**.
5. On deny: enrollment ends; no Credential issued.
6. On approve: Gateway creates Controller under the Player, issues `access_token`, `refresh_token`, `controller_id`, `player_id`, `scopes`.
7. Agent polls or exchanges for tokens; human browser Credential is never copied to the agent.
8. Agent proceeds with HELLO → AUTH → REGISTER → ENTER_WORLD using the controller access token.
9. Audit records enrollment approval with player, controller, scopes, and operator identity.

## 11. Access token refresh

1. Agent presents valid refresh Credential to `POST /auth/token/refresh` (or equivalent).
2. Gateway validates refresh not revoked/expired and Controller still active.
3. Gateway issues new access token (and MAY rotate refresh); old access token becomes invalid at expiry or immediately per policy.
4. Detected refresh reuse after rotation MUST revoke the Controller credential family and audit as potential theft.

## 12. Unauthorized Player switching attempt

1. Authenticated Controller for Player A submits an ACT body claiming `agent_id` / `player_id` of Player B.
2. Gateway compares body principal to server-bound Controller.player_id.
3. Request fails with FORBIDDEN; no budget charge; no world event.
4. Audit records mismatch fingerprint for abuse detection.

All sequences MUST be covered by conformance tests before production identity-plane release; sequences 1–8 remain required for v0.1 containment. Sequences 9–12 are required when the identity/auth plane is enabled.
