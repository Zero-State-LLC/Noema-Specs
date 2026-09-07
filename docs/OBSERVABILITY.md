# Observability

## Required context fields

Structured logs, traces, metrics, and event receipts SHOULD include trace IDs, world IDs, agent IDs, experiment IDs, trajectory IDs, cycle IDs, request IDs, protocol versions, and schema versions.

## Metrics

Track action latency, queue latency, world tick duration, replay divergence, agent disconnects, invalid actions, tool-call failures, compute usage, attention usage, messages, experiment completion, phenomenon replication status, and dataset export status.

## Secret handling

Do not log secrets, provider keys, private prompts, private metadata, or raw sensitive tool outputs. Redaction must happen before export.

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Telemetry adapters can extend correlation and operational diagnostics around action queues, replay divergence, disconnects, and export status.

**Preserved invariants.** Keep world/version lineage and redact secrets, private prompts, metadata, and sensitive tool outputs before export. Operational telemetry does not silently become research evidence.

**Compatibility and promotion.** Version field and aggregation semantics so older logs remain interpretable; changes to receipts or research capture need their governing schema and consent path, not merely a dashboard field.

**Validation expectations.** Use correlated success/failure traces and redaction fixtures, including cross-world identifiers and retry cases; distinguish unavailable measurements from zero and make no latency or coverage claim without recorded observations.
