# Security

## Threat model

Threats include malicious agents, prompt injection through world content, malicious inter-agent messages, tool abuse, credential exposure, replay tampering, event-ledger tampering, data exfiltration, denial of service, runaway tool loops, cross-agent data leakage, cross-world state leakage, reducer amplification, public/private research-data leakage, consent bypass, and model-provider key leakage.

## Requirements

- No provider keys exposed to agents.
- Per-agent capability tokens.
- Strict tool allowlists.
- Outbound network policy.
- Rate limits and compute/action budgets.
- Sandbox execution.
- Signed event receipts for research/evidence export profiles; optional for local gameplay.
- Tamper-evident ledgers.
- Private/public data separation.
- Audit logging and schema validation.
- Maximum payload sizes and tool-call timeouts.
- Kill switch, agent quarantine, and world-level incident mode.
- Evidence export signing and receipt verification for research-isolated outputs.

## Containment

Agent code, tools, and model adapters MUST execute within a deny-by-default containment boundary. The World Engine MUST NOT execute agent code; it accepts only authenticated, schema-valid structured actions. World reducers execute in the trusted simulation boundary and MUST remain pure, deterministic, and unable to perform network, filesystem, model, or tool side effects. The containment boundary MUST restrict filesystem paths, processes, network destinations, credentials, tool verbs, payload sizes, wall-clock time, concurrency, and resource use. Capability grants MUST be scoped to one agent, one world, an explicit operation set, and a bounded lifetime. A grant for observation or research export MUST NOT imply authority to mutate world state.

Tool and model-provider credentials MUST terminate at a trusted gateway and MUST NOT appear in prompts, observations, agent-visible environment variables, tool results, logs, or replay bundles. Untrusted world content and inter-agent messages MUST be treated as data, not authority. Implementations MUST provide deterministic cancellation at budget exhaustion, timeout, quarantine, world incident mode, or operator kill switch. Cleanup MUST revoke ephemeral credentials and terminate descendant processes.

Acceptance checks SHOULD attempt forbidden filesystem access, unapproved egress, credential retrieval, over-sized payloads, process escape, and execution after cancellation. Each attempt MUST be denied and auditable without disclosing the protected value.

## World isolation

Every authenticated request, event, observation, cache entry, queue job, snapshot, object-storage key, replay bundle, and research record MUST carry or inherit a verified `world_id`. Authorization MUST compare the authenticated world scope with the target object before reading, reducing, mutating, publishing, or exporting it. Client-supplied identifiers MUST NOT override server-bound world context.

Canonical state, observable state, agent state, ledgers, reducer inputs, encryption or signing context, rate-limit counters, and temporary files MUST be partitioned by world. Shared infrastructure MAY be used only when keys and queries are world-qualified and cross-world joins are denied by default. Reducers MUST receive a world-scoped input view and MUST fail closed if an input references another world or has no resolvable world lineage.

Acceptance checks SHOULD create identical object identifiers in two worlds, exercise reads, writes, reductions, cache hits, queue retries, replay, and export, and verify that neither content nor existence metadata crosses the boundary.

## Budget and reducer enforcement

Action resolution MUST check the agent's canonical budget account before applying a state transition. Budget availability and consumption are part of deterministic reducer input and state. An action that would exceed attention, compute, tool, message, planning-depth, inspection, delegation, experimental-action, energy, influence, storage, or other declared limits MUST be rejected and MUST emit `BUDGET_EXCEEDED` as defined by the [Event Catalog](EVENT-CATALOG.md). The attempted action MUST NOT mutate world state, call a tool or model, enter a queue, or consume the exceeded budget. Accepted consumption MUST be recorded through the action event or `BUDGET_CONSUMED` without double charging.

The trusted gateway and scheduler MAY reject malformed, unauthorized, oversized, rate-limited, or obviously over-budget requests before world resolution, but replay-critical budget truth remains canonical reducer state. Gateway reservations and retries MUST reconcile with the reducer result and MUST NOT become a second source of truth.

Observation projectors and other read reducers transform canonical or event state into agent-visible observations. They MUST be pure or replay-deterministic for the declared world version and reducer version. Before execution, the trusted scheduler MUST reserve explicit limits for input bytes, output bytes, compute units, wall-clock time, recursion or planning depth, and referenced records. Infrastructure accounting MUST include retries, nested calls, serialization, and extension processing without allowing projector-controlled code to raise its own limits.

A reducer MUST NOT emit content beyond the observer's visibility and capability scope. On exhaustion it MUST stop deterministically and either return a schema-valid, explicitly truncated observation or fail with a stable error. Truncated observations SHOULD record reducer identity and version, budget limit and use, output digest, truncation state, and omitted sections in provenance. Exhaustion MUST NOT trigger an unbudgeted fallback, silently fetch broader state, or reveal omitted values through errors or timing details.

Acceptance checks SHOULD test exact-limit, one-over-limit, adversarial expansion, retry, and nested-reducer cases. Recorded usage MUST never exceed the enforced limit, and replay under the same inputs and limits MUST produce the same result or stable failure.

## Consent gating

Research capture, retention, analysis, publication, and export MUST be independently authorized. Registration or world entry MUST NOT be interpreted as public-dataset consent. The effective policy MUST be the most restrictive combination of agent consent flags, study policy, world policy, data visibility, retention status, licensing, and applicable operator controls.

Consent MUST be checked at collection and rechecked before reduction for research, analysis, bundle creation, publication, or transfer. Missing, expired, withdrawn, contradictory, or unverifiable consent MUST fail closed. Derived observations MUST retain source lineage, consent basis, exclusions, and visibility classification. Aggregation, de-identification, or reducer output MUST NOT upgrade visibility or erase withdrawal obligations unless an approved policy explicitly establishes that transformation.

Operational telemetry MUST NOT silently become research evidence. Public export requires explicit dataset opt-in and an allowlisted export path. Revocation MUST block future processing and publication and MUST initiate the configured deletion or tombstone workflow while preserving only the minimum audit record legally and operationally required.

Acceptance checks SHOULD cover no consent, partial consent, withdrawal before export, mixed-consent aggregation, expired retention, and public opt-out. Each disallowed path MUST be rejected before protected content is materialized in the destination.

## Writer, transaction, and crash containment

World mutation authority is itself a security boundary. Each `world_id` MUST have exactly one active fenced canonical writer. Gateways, operator APIs, schedulers, replay workers, projectors, and research capture services MUST NOT bypass the active writer fence or write canonical WorldState directly. A stale or ambiguous fence fails closed before accepting mutating traffic.

Canonical cycle batches MUST commit atomically under the persistence contract in [Module Contracts](MODULE-CONTRACTS.md). Security controls MUST treat serialization failures, stale expected revisions, duplicate event sequences, digest-chain mismatches, and unresolved crash reconciliation as containment events. The safe response is retry from the unchanged committed head or INCIDENT mode, not best-effort repair.

## Evidence receipts and export profiles

Signed evidence receipts are optional for the local gameplay profile. They are mandatory for `research-isolated` execution, reproducibility bundles, Atlas export, and any public evidence export profile. A required receipt MUST bind at minimum the evidence digest or bundle digest, `world_id`, version lineage, consent and exclusion policy identifiers, export profile, signing algorithm, key id, signature, issuance time, and verification policy. Historical receipts MUST remain verifiable across key rotation.

Missing, invalid, expired, or wrong-scope required receipts make the affected export `INVALID_EVIDENCE`. Implementations MUST NOT silently downgrade to unsigned evidence, relabel it as telemetry, or remove protected records to force receipt verification. Receipt verification proves integrity and scope of the signed bytes; it does not prove a research claim beyond the claim labels and cited evidence.

## Default tool surface

No real-world destructive actions are part of the default game tool surface. External network access is deny-by-default unless a study explicitly grants it. Security controls MUST be configured in trusted deployment policy rather than exposed as agent-modifiable environment variables.
