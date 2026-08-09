# Observability

## Required context fields

Structured logs, traces, metrics, and event receipts SHOULD include trace IDs, world IDs, agent IDs, experiment IDs, trajectory IDs, cycle IDs, request IDs, protocol versions, and schema versions.

## Metrics

Track action latency, queue latency, world tick duration, replay divergence, agent disconnects, invalid actions, tool-call failures, compute usage, attention usage, messages, experiment completion, phenomenon replication status, and dataset export status.

## Secret handling

Do not log secrets, provider keys, private prompts, private metadata, or raw sensitive tool outputs. Redaction must happen before export.
