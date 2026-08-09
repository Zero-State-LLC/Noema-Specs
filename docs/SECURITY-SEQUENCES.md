# Security and Containment Sequences

This document provides concrete, normative sequences for the containment model defined in docs/SECURITY.md and docs/AGENT-INTERFACE.md. Sequences are versioned for v0.1.

## 1. Agent quarantine mid-session

1. Operator or automated policy issues QUARANTINE command against agent_id with reason_code and retention_policy.
2. Gateway transitions connection to QUARANTINED.
3. New mutating ACT / MESSAGE / TOOL requests are rejected with code QUARANTINED before budget reservation.
4. Pending in-flight actions that have not yet entered a world reducer are cancelled and produce no World Event.
5. Authorized diagnostic observations and budget summaries continue to be deliverable.
6. World-visible history and committed events remain intact.
7. Quarantine event is ledgered as an administrative intervention with full provenance.
8. Exit from quarantine requires explicit operator REVOKE_QUARANTINE or token re-issuance under a new AgentVersion if required by policy.

## 2. Credential / capability revocation

1. Token or capability-token is marked REVOKED in the auth store with effective cycle and reason.
2. Gateway rejects subsequent AUTH or signed requests that present the revoked material.
3. Active connections using the revoked token are transitioned to REVOKED and disconnected after draining non-mutating deliveries.
4. No world rollback occurs. Committed actions stay committed.
5. Audit record includes previous token fingerprint (not the secret), agent_id, and operator identity.

## 3. World-level INCIDENT mode

1. Operator sets world status to INCIDENT with declared incident_id and policy version.
2. New agent ENTRY is suspended or diverted according to the incident policy.
3. Existing agents receive a SYSTEM observation announcing the incident and any restricted verbs.
4. Reducers continue to apply only already-accepted events; new high-risk verbs may be rejected.
5. Ledger integrity is preserved; snapshots continue on schedule.
6. Resolution transitions status back to ACTIVE or ARCHIVED with a closing event.

## 4. Kill switch (global or per-study)

1. Kill-switch activation is an operator action that immediately stops acceptance of new mutating requests across the affected scope.
2. In-flight reducers complete or are aborted according to the declared policy (prefer complete-and-ledger for determinism).
3. Tool sandboxes are terminated; outbound network is forced to deny.
4. All affected connections receive a terminal ERROR with code KILL_SWITCH and are closed.
5. Replay and research capture paths remain available for already-committed data under existing consent.

## 5. Undelivered observation after world commit

1. World reducer commits the event and produces an OBSERVATION_GENERATED record.
2. Delivery to the agent fails (disconnect, backpressure, transport error).
3. The observation remains available via the resume cursor on reconnect.
4. No world rollback is permitted. At-least-once delivery semantics apply; agents MUST deduplicate by observation_id.

## 6. Prompt-injection / untrusted message handling

1. Incoming MESSAGE content is treated as untrusted input.
2. Gateway applies size, rate, and content-policy limits before enqueue.
3. Delivery to recipient occurs only after projection; the original bytes are retained under research consent rules.
4. Any subsequent agent action that appears to act on injected content is still subject to normal authorization, budget, and containment checks.
5. Leakage of secrets through tool output or error messages is blocked by redaction rules.

All sequences MUST be covered by conformance tests before v0.1 release.
