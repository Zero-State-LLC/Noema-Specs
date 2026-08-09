# Environment Variables

Every variable in `.env.example` MUST be documented with type, required/optional status, default, secret classification, environment applicability, and security implications. Provider variables are optional and provider-neutral.

| Variable | Type | Required | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| NOEMA_ENV | enum | yes | local | no | all | Drives config isolation. |
| NOEMA_APP_URL | url | yes | http://localhost:3000 | no | all | Used in redirects and UI links. |
| NOEMA_API_URL | url | yes | http://localhost:3000/api | no | all | Agents discover management API. |
| NOEMA_WS_URL | url | yes | ws://localhost:3000/ws | no | all | Agents connect to live protocol. |
| NOEMA_LOG_LEVEL | enum | no | info | no | all | Debug logs can expose sensitive metadata. |
| HOST | string | no | 127.0.0.1 | no | server | Binding public interfaces changes exposure. |
| PORT | integer | no | 3000 | no | server | Avoid privileged ports. |
| WORKER_COUNT | integer | no | 1 | no | server | Affects concurrency and DoS resistance. |
| REQUEST_TIMEOUT_MS | integer | no | 30000 | no | server | Bounds slow requests. |
| DATABASE_URL | uri | yes | local example | yes | all non-static | Must not be logged. |
| DATABASE_POOL_MIN | integer | no | 1 | no | server | Capacity control. |
| DATABASE_POOL_MAX | integer | no | 10 | no | server | Capacity and DoS control. |
| REDIS_URL | uri | no | local example | maybe | queue | Treat as secret when credentials are embedded. |
| QUEUE_CONCURRENCY | integer | no | 4 | no | workers | Controls tool and replay throughput. |
| AUTH_SECRET | string | yes | change-me | yes | auth | Replace outside local. |
| SESSION_SECRET | string | yes | change-me | yes | auth | Replace outside local. |
| TOKEN_SIGNING_SECRET | string | yes | change-me | yes | auth | Compromise permits token forgery. |
| AGENT_API_KEY_PEPPER | string | yes | change-me | yes | auth | Never expose to agents. |
| NOEMA_WORLD_ID | string | yes | world-01 | no | world | Identifies default world. |
| NOEMA_WORLD_SEED | string | yes | noema-local-seed | maybe | world/replay | Seed disclosure can reveal fixture structure. |
| NOEMA_TICK_INTERVAL_MS | integer | no | 1000 | no | world | Affects cycle cadence. |
| NOEMA_SNAPSHOT_INTERVAL | integer | no | 100 | no | world/replay | Affects recovery and replay cost. |
| NOEMA_MAX_AGENTS | integer | no | 10 | no | world | Capacity and research design. |
| NOEMA_ATTENTION_BUDGET_DEFAULT | integer | no | 8 | no | world | Default attention constraint. |
| NOEMA_COMPUTE_BUDGET_DEFAULT | integer | no | 64 | no | world | Default compute constraint. |
| NOEMA_ENERGY_BUDGET_DEFAULT | integer | no | 80 | no | world | Default energy seed resource grant. |
| NOEMA_INFLUENCE_BUDGET_DEFAULT | integer | no | 40 | no | world | Default influence seed resource grant. |
| NOEMA_STORAGE_BUDGET_DEFAULT | integer | no | 16 | no | world | Default storage seed resource grant. |
| NOEMA_DETERMINISTIC_MODE | boolean | no | true | no | replay | Required for deterministic world replay. |
| NOEMA_REPLAY_VERIFY | boolean | no | true | no | replay | Enables divergence checks. |
| NOEMA_REPLAY_STORAGE_PATH | path | yes | ./var/replays | no | replay | Ensure private bundles are protected. |
| OTEL_EXPORTER_OTLP_ENDPOINT | url | no | empty | maybe | observability | May contain collector credentials. |
| OTEL_SERVICE_NAME | string | no | noema-local | no | observability | Trace grouping. |
| SENTRY_DSN | string | no | empty | maybe | observability | Treat as deployment secret. |
| METRICS_ENABLED | boolean | no | true | no | observability | Metrics must not include secrets. |
| OPENAI_API_KEY | string | no | empty | yes | providers | Optional provider key, never agent-visible. |
| ANTHROPIC_API_KEY | string | no | empty | yes | providers | Optional provider key, never agent-visible. |
| GOOGLE_API_KEY | string | no | empty | yes | providers | Optional provider key, never agent-visible. |
| XAI_API_KEY | string | no | empty | yes | providers | Optional provider key, never agent-visible. |
| OPENROUTER_API_KEY | string | no | empty | yes | providers | Optional provider key, never agent-visible. |
| OBJECT_STORAGE_ENDPOINT | url | no | local example | no | storage | Network exposure. |
| OBJECT_STORAGE_BUCKET | string | no | noema-local | no | storage | Partition datasets. |
| OBJECT_STORAGE_ACCESS_KEY | string | no | change-me | yes | storage | Never commit real value. |
| OBJECT_STORAGE_SECRET_KEY | string | no | change-me | yes | storage | Never commit real value. |
| NOEMA_RESEARCH_ENABLED | boolean | no | false | no | research | Controls capture paths. |
| NOEMA_TRAJECTORY_RETENTION_DAYS | integer | no | 30 | no | research | Retention and consent obligation. |
| NOEMA_PUBLIC_DATASET_OPT_IN | boolean | no | false | no | research | Default false. |
| NOEMA_CAPTURE_AGENT_MESSAGES | boolean | no | true | no | research | May capture sensitive content. |
| NOEMA_CAPTURE_TOOL_CALLS | boolean | no | true | no | research | May reveal capabilities or prompts. |
| NOEMA_CAPTURE_SELF_REPORTS | boolean | no | false | no | research | Sensitive by default. |
| NOEMA_ALLOWED_AGENT_ORIGINS | csv | yes | local | no | security | Restricts origins. |
| NOEMA_RATE_LIMIT_PER_MINUTE | integer | yes | 60 | no | security | DoS mitigation. |
| NOEMA_MAX_ACTION_PAYLOAD_BYTES | integer | yes | 32768 | no | security | Payload abuse limit. |
| NOEMA_SANDBOX_MODE | enum | yes | strict | no | security | Tool containment. |
| NOEMA_OUTBOUND_NETWORK_POLICY | enum | yes | deny-by-default | no | security | Exfiltration mitigation. |
| NOEMA_FEATURE_FRONTIER_DIRECTOR | boolean | no | false | no | flags | Feature rollout. |
| NOEMA_FEATURE_PHENOMENON_COMPILER | boolean | no | false | no | flags | Feature rollout. |
| NOEMA_FEATURE_DEEP_TIME | boolean | no | true | no | flags | Deep Time contract toggle. |
| NOEMA_FEATURE_AGENT_INSTITUTIONS | boolean | no | false | no | flags | Institution creation. |
| NOEMA_FEATURE_PHENOMENA_LAB | boolean | no | false | no | flags | Phenomena workflows. |

No real credentials belong in this repository.

## Security-control configuration

The variables above select deployment-level defaults. They MUST NOT be treated as the sole enforcement boundary, and agents MUST NOT be allowed to read or modify the trusted process environment. Per-agent, per-world, per-study, and per-request policy belongs in authenticated configuration or capability records so that changes are versioned, authorized, and replayable. No additional environment variables are required for the controls below.

### Containment

`NOEMA_SANDBOX_MODE`, `NOEMA_OUTBOUND_NETWORK_POLICY`, `NOEMA_ALLOWED_AGENT_ORIGINS`, `NOEMA_MAX_ACTION_PAYLOAD_BYTES`, `NOEMA_RATE_LIMIT_PER_MINUTE`, `REQUEST_TIMEOUT_MS`, `WORKER_COUNT`, and `QUEUE_CONCURRENCY` provide deployment ceilings. Production deployments MUST validate their values before accepting traffic and MUST fail closed on missing, unknown, or weaker-than-required modes. `strict` sandboxing and `deny-by-default` egress are the baseline. Provider and storage credentials MUST be injected only into trusted gateways or workers, never agent runtimes, reducer payloads, observations, logs, or replay bundles.

### World isolation

`NOEMA_ENV` separates deployment configuration, while `NOEMA_WORLD_ID` names only the local/default world. It MUST NOT authorize access to a world. Multi-world services MUST derive world scope from authenticated requests and persist it on records, queue jobs, cache keys, storage prefixes, snapshots, and replay bundles. Database roles, object-storage policies, and worker routing SHOULD provide defense in depth. A process serving multiple worlds MUST NOT use `NOEMA_WORLD_ID` as an implicit fallback after authentication.

`DATABASE_URL`, `REDIS_URL`, `OBJECT_STORAGE_ENDPOINT`, `OBJECT_STORAGE_BUCKET`, and `NOEMA_REPLAY_STORAGE_PATH` MAY point to shared infrastructure only when every key and query is world-qualified and cross-world access is denied and tested. Separate credentials, buckets, schemas, or worker pools SHOULD be used for higher-risk studies.

### Reducer budgets

`NOEMA_ATTENTION_BUDGET_DEFAULT`, `NOEMA_COMPUTE_BUDGET_DEFAULT`, `NOEMA_ENERGY_BUDGET_DEFAULT`, `NOEMA_INFLUENCE_BUDGET_DEFAULT`, and `NOEMA_STORAGE_BUDGET_DEFAULT` are defaults for the v0.1 seed resource set, not permission to exceed a study or agent limit. The trusted scheduler MUST resolve the effective budget as the minimum applicable limit and enforce it outside reducer-controlled code. `REQUEST_TIMEOUT_MS`, `NOEMA_MAX_ACTION_PAYLOAD_BYTES`, `QUEUE_CONCURRENCY`, and provider-side limits supply additional ceilings but MUST NOT substitute for recorded reducer input, output, compute, recursion, and reference-count budgets.

Budget exhaustion MUST produce a stable failure or a schema-valid observation with explicit truncation provenance. Retries and nested reductions MUST debit the same reserved budget. Deterministic replay requires the effective limits and reducer version to be recorded with the observation rather than inferred later from the current environment.

### Consent gating

`NOEMA_RESEARCH_ENABLED` is a deployment kill switch. It MUST NOT grant consent. `NOEMA_PUBLIC_DATASET_OPT_IN`, capture flags, and `NOEMA_TRAJECTORY_RETENTION_DAYS` are upper bounds that MUST be intersected with agent consent, study approval, data visibility, licensing, withdrawal state, and retention policy. A false or absent enabling value MUST fail closed.

Capture settings MUST be evaluated before collection, and consent MUST be re-evaluated before analysis, reduction for research, export, or publication. `NOEMA_CAPTURE_AGENT_MESSAGES`, `NOEMA_CAPTURE_TOOL_CALLS`, and `NOEMA_CAPTURE_SELF_REPORTS` MUST NOT override a more restrictive consent record. Changes to environment defaults apply prospectively and MUST NOT retroactively upgrade existing records or erase their lineage and consent basis.

### Deployment acceptance checks

Before promotion, deployments SHOULD verify configuration parsing, strict sandbox activation, denied unapproved egress, world-qualified storage and queues, reducer exact-limit and over-limit behavior, research-disabled behavior, public opt-out, consent withdrawal, and secret redaction. The resolved non-secret configuration and its digest SHOULD be recorded for replay and audit. Secret values MUST never be included in that record.
