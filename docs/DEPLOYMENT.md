# Deployment Contract

## Environments

| Environment | Purpose | Data and external access |
|---|---|---|
| local | Individual development and manual exploration | Synthetic data; loopback defaults |
| test | Automated deterministic validation | Ephemeral data; external calls stubbed unless integration-marked |
| staging | Production-like release validation | Non-production data and credentials |
| production | Persistent live worlds | Full security, backup, monitoring, change control |
| research-isolated | Sensitive or high-risk experiments | Dedicated trust boundary, restricted egress, controlled export |

An environment MUST NOT share database credentials, signing keys, queue namespaces, object-storage prefixes, or agent credentials with another environment. Research-isolated SHOULD use separate infrastructure accounts/projects where available.

## Deployable topology

v0.1 MAY deploy one modular application containing gateway, auth, registry, world engine, state, ledger, observation, action, message, scheduler, and operator UI modules. Background worker processes MAY handle projections, snapshots, replay, and research jobs. Later service extraction MUST preserve module contracts and ordering.

Production requires at minimum: ingress/TLS, application/world processes, durable relational database, optional queue/cache, private object storage, worker capacity, telemetry export, secrets delivery, and backup targets. No named cloud or vendor is mandatory.

## Release procedure

1. Build an immutable artifact identified by source revision and NOEMA product/spec compatibility.
2. Validate configuration without printing secret values.
3. Run schema, protocol, migration, security, and deterministic replay checks.
4. Back up or verify a recent restorable backup before destructive migrations.
5. Apply backward-compatible database migrations with a single migration owner.
6. Deploy processes with readiness disabled until dependencies and schema versions pass.
7. Start workers, then world writers using leases/fencing tokens so only one writer owns each world.
8. Run smoke tests: auth, agent handshake, observe/action receipt, ledger append, projection, metrics, and replay fixture.
9. Record artifact, configuration hash, migrations, world versions, protocol versions, operator, and timestamps.
10. Promote traffic gradually where supported. Roll back on acceptance failure.

World rule or seed changes MUST create a new World Version, not silently alter a running version.

## Configuration and secrets

Follow [ENVIRONMENT.md](ENVIRONMENT.md). Hosted deployments MUST inject secrets at runtime from a protected store, use independent high-entropy values, restrict secret access per process, and support rotation. Secrets MUST NOT appear in images, source, logs, traces, snapshots, replay bundles, crash reports, or operator URLs.

Effective non-secret configuration and secret key identifiers MUST be captured for audit. Feature flags affecting behavior MUST be captured with each experiment and replay.

## Database and migrations

The relational store is authoritative for identities, metadata, ledger/index records, and transactional coordination. Migrations MUST be ordered, repeat-safe where feasible, tested on production-shaped data, and documented with compatibility, expected duration, locking behavior, validation, rollback/forward-fix, and data lineage impact.

Expand-and-contract migrations are required for zero-downtime changes. Schema-breaking changes require version bumps and an RFC. Research-critical rows MUST not be destructively rewritten by routine migrations.

## Queue and workers

Queue delivery is at least once unless a stronger guarantee is proven. Jobs MUST carry unique IDs, correlation IDs, version metadata, retry limits, and idempotency keys. Dead-letter jobs MUST be inspectable without exposing secrets.

- Projection workers update derived state from committed events.
- Replay workers run deterministic/protocol/behavioral-equivalence verification in resource-isolated jobs.
- Research workers analyze trajectories and compile candidates without mutating canonical evidence.
- Export workers create checksum manifests and enforce privacy/consent gates.

Backpressure MUST preserve ledger integrity and world safety, even if analytics lag.

## Object storage

Trajectory bodies, snapshots, replay fixtures, reproducibility bundles, and dataset artifacts SHOULD use content-addressed objects. Private evidence and public exports MUST use separate access policies. Enable encryption, versioning or immutability controls where available, lifecycle rules consistent with retention, and checksum verification on write/read/export.

## World process operations

Each world has one logical transition writer. The deployment MUST use leases with fencing or an equivalent mechanism, stop transitions on lease loss, and prevent stale writers from committing. Graceful shutdown stops admission, drains in-flight actions, commits or rejects them explicitly, writes a final safe snapshot when possible, releases the lease, and records shutdown evidence.

Scaling gateways and read workers horizontally MUST NOT introduce multiple world writers or reorder canonical events.

## Backups and disaster recovery

Back up the database, object metadata/content, world configuration, ledger integrity material, and signing-key recovery metadata according to the security policy. Queue/cache contents SHOULD be reconstructible and are not sufficient backups.

Production MUST define and test RPO/RTO targets before launch. Restore drills MUST verify database integrity, object checksums, ledger chain/receipts, snapshot compatibility, credential invalidation or preservation policy, and replay of at least one canonical fixture. A restore creates an incident/audit record.

## Snapshot retention

Keep genesis metadata, ledger history, and snapshots required by the research and disaster-recovery policies. At minimum retain the latest verified snapshot, snapshots referenced by active experiments or reproducibility bundles, milestone/release snapshots, and enough prior snapshots to meet RPO. Never delete a referenced snapshot without first creating and validating a replacement bundle. Retention decisions MUST account for participant consent and private-data erasure obligations.

## Rollback and incident mode

Application artifacts MAY roll back only while remaining compatible with the current database, world, protocol, and schema versions. Database rollback is permitted only with a tested non-destructive plan; otherwise use a forward fix. Replay divergence, ledger integrity failure, unauthorized writer, secret exposure, or containment failure triggers world-level incident mode: stop affected writes, preserve evidence, revoke exposed credentials, isolate workers, and follow the security response contract.
