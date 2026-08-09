# Observability Contract

## Purpose

Observability supports operations and scientific provenance. Telemetry is not the canonical event ledger and MUST NOT be used to reconstruct research claims when canonical evidence exists. It MUST never contain credentials, raw authorization headers, private prompts, unrestricted message/tool bodies, or model-provider keys.

## Correlation context

Every research-critical log, trace, metric exemplar, job, and event receipt SHOULD carry the applicable identifiers:

- `trace_id`, `span_id`, and `correlation_id`
- `world_id`, World Version, `cycle_id`/cycle, and event sequence
- `agent_id` and Agent Version, pseudonymized where required
- `session_id`, `experiment_id`, run/replication ID, and `trajectory_id`
- protocol/schema versions and deployment/source revision

Identifiers MUST remain stable across gateway, queue, worker, ledger, projection, replay, research, and export boundaries. Trace headers from agents are untrusted input; the gateway MUST validate or replace them.

## Structured logs

Logs MUST be machine-readable structured records with timestamp, severity, service/module, environment, event name, message, correlation context, outcome, duration when applicable, and stable error code. Stack traces belong only on error records and must pass redaction.

Use allowlisted fields rather than logging arbitrary request objects. Hash or pseudonymize sensitive identifiers when operational debugging does not require raw values. Log access and retention MUST follow the data classification of the most sensitive included field.

Required operational events include process lifecycle, configuration validation result, protocol negotiation, auth decision without credential, agent admission/quarantine/disconnect, action accepted/rejected, ledger commit failure, world-writer lease changes, snapshot result, replay result/divergence, experiment state transition, export approval/result, and security incident-mode transition.

## Tracing

Distributed traces SHOULD cover agent handshake; observe/action/receipt; message delivery; tool authorization and execution; world-cycle transition; ledger append and projection; snapshot; replay; experiment; phenomenon compilation; and dataset export. External model/tool calls MUST be separate spans with provider/model identifiers, token/compute accounting when available, timeout, and outcome, but no sensitive prompt or response body by default.

Sampling MUST retain errors, replay divergence, ledger failures, security decisions, and experiment/export terminal spans. Sampling policy and telemetry version SHOULD be recorded for research runs when telemetry contributes evidence.

## Metrics

Implementations MUST expose equivalent metrics for:

| Signal | Suggested type | Key dimensions |
|---|---|---|
| Action latency | histogram | action type, outcome, world version |
| Queue latency | histogram | queue/job type, outcome |
| World tick duration | histogram | world ID/version |
| Replay divergence | counter + gauge | boundary, world/protocol version |
| Agent disconnects | counter | reason, protocol version |
| Invalid actions | counter | stable error code, action type |
| Tool-call failures | counter | tool class, reason; never arguments |
| Compute usage | counter/histogram | agent version, experiment, unit |
| Attention usage | counter/histogram | agent version, experiment |
| Messages | counter | delivery outcome, visibility class |
| Experiment completion | counter + duration | experiment type, outcome |
| Phenomenon replication | counter/gauge | phenomenon/case, status |
| Dataset export | counter + duration/bytes | release, partition, outcome |

Also track request rate/errors, active agents, world cycle lag, ledger append latency/errors, projection lag, snapshot age/failures, dead-letter jobs, database pool saturation, object checksum failures, and telemetry pipeline drops.

Metrics labels MUST be bounded. Never use message content, raw error text, event IDs, trajectory IDs, or unbounded agent IDs as ordinary metric labels. Use traces or logs for high-cardinality correlation.

## Event receipts

An event receipt is durable evidence returned for an accepted or rejected action/event. It SHOULD include receipt/event ID, action/idempotency key, world/version, cycle/sequence, schema version, outcome, timestamp, payload digest, correlation ID, and integrity proof or signature where feasible. Receipts are stored with the ledger, not only telemetry.

## Health and service objectives

- **Liveness:** process can make progress. It MUST NOT imply dependency or world readiness.
- **Readiness:** configuration valid, migrations compatible, required stores reachable, and the process may safely serve its role.
- **World readiness:** a current fenced writer owns the world and ledger append succeeds.

Before production, operators MUST set numeric objectives for action acceptance latency, cycle deadline success, ledger durability, replay verification success, projection lag, and recovery. Alerts SHOULD page on ledger integrity failure, unauthorized/multiple writers, replay divergence, containment failure, sustained world-cycle failure, snapshot/backup failure, and telemetry loss during research runs.

## Research dashboards and status

Dashboards SHOULD distinguish operational failure from scientific outcome. A failed replication is a valid research result; a replication with missing evidence or infrastructure failure is incomplete. Experiment and phenomenon statuses MUST use stable states and link to canonical evidence. No dashboard may promote `INFERRED` or `SPECULATIVE` material as `OBSERVED`.

## Redaction and validation

Telemetry pipelines MUST apply field allowlists, secret-pattern redaction, size limits, access control, encryption in transit/at rest, retention, and deletion policy. CI/security tests SHOULD seed canary secrets and verify they do not appear in logs, traces, metrics, error responses, snapshots, or exported bundles.
