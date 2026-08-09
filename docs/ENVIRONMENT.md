# Environment Contract

## Loading and precedence

Configuration MUST be loaded once at process startup, validated against a typed schema, and exposed through a configuration object rather than scattered environment reads. Precedence is: explicit process environment, local untracked `.env`, then documented non-secret defaults. Production and research-isolated deployments MUST inject secrets through a secret manager or equivalent protected mechanism.

Unknown `NOEMA_*` variables SHOULD fail startup to catch misspellings. Missing required values and malformed values MUST fail startup without echoing secrets. Empty optional values mean “disabled” unless stated otherwise. Boolean values are lowercase `true` or `false`; durations are integer milliseconds; counts and budgets are non-negative integers; URLs are absolute.

Applicability: **all** means every environment; **hosted** means staging, production, and research-isolated; **optional** means the dependent subsystem may be disabled.

## Variable reference

| Variable | Type | Requirement/default | Secret | Applies | Security and behavior |
|---|---|---|---|---|---|
| `NOEMA_ENV` | enum | required: `local`, `test`, `staging`, `production`, `research-isolated` | no | all | Selects policy, never authorization by itself |
| `NOEMA_APP_URL` | URL | required, `http://localhost:3000` local | no | all | Canonical operator UI origin |
| `NOEMA_API_URL` | URL | required, `http://localhost:4000` local | no | all | Public management API URL |
| `NOEMA_WS_URL` | ws(s) URL | required, `ws://localhost:4000/agent` local | no | all | Use `wss` outside trusted local networks |
| `NOEMA_LOG_LEVEL` | enum | optional, `info` | no | all | `trace`, `debug`, `info`, `warn`, `error`; never enables secret logging |
| `HOST` | string | optional, `127.0.0.1` | no | all | Use explicit ingress controls when binding publicly |
| `PORT` | integer | optional, `4000` | no | all | 1–65535 |
| `WORKER_COUNT` | integer | optional, `1` | no | all | Must respect world single-writer rules |
| `REQUEST_TIMEOUT_MS` | integer | optional, `30000` | no | all | Bounds external and management requests |
| `DATABASE_URL` | connection URL | required | yes | all | Least-privilege account; TLS in hosted environments |
| `DATABASE_POOL_MIN` | integer | optional, `1` | no | all | Must not exceed database capacity |
| `DATABASE_POOL_MAX` | integer | optional, `10` | no | all | Validate `max >= min` |
| `REDIS_URL` | connection URL | optional | yes | optional | Required only when queue/cache adapter uses Redis; TLS hosted |
| `QUEUE_CONCURRENCY` | integer | optional, `4` | no | all | Does not override per-world serialization |
| `AUTH_SECRET` | string | required hosted | yes | hosted | At least 32 random bytes; rotate deliberately |
| `SESSION_SECRET` | string | required hosted | yes | hosted | Independent from all other secrets |
| `TOKEN_SIGNING_SECRET` | string | required hosted | yes | hosted | Protects signed tokens; rotation needs key-version support |
| `AGENT_API_KEY_PEPPER` | string | required hosted | yes | hosted | Used only with one-way credential hashing |
| `NOEMA_WORLD_ID` | identifier | required, `world-local` local | no | all | Stable deployment/world identity |
| `NOEMA_WORLD_SEED` | integer/string | required | no | all | Immutable for a world version; record in bundles |
| `NOEMA_TICK_INTERVAL_MS` | integer | optional, `1000` | no | all | Scheduling input, not replay ordering |
| `NOEMA_SNAPSHOT_INTERVAL` | integer | optional, `100` cycles | no | all | `0` disables periodic snapshots only |
| `NOEMA_MAX_AGENTS` | integer | optional, `10` | no | all | Admission hard limit |
| `NOEMA_ATTENTION_BUDGET_DEFAULT` | integer | optional, `8` | no | all | Default only; record effective value per run |
| `NOEMA_COMPUTE_BUDGET_DEFAULT` | integer | optional, `64` | no | all | Default only; unit defined by implementation manifest |
| `NOEMA_DETERMINISTIC_MODE` | boolean | optional, `true` | no | all | Must be true for conformance replay |
| `NOEMA_REPLAY_VERIFY` | boolean | optional, `true` | no | all | Fails replay on equivalence divergence |
| `NOEMA_REPLAY_STORAGE_PATH` | path/URI | optional, `./var/replays` | no | all | Must not be web-served; constrain filesystem permissions |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | URL | optional | may contain auth | optional | Prefer separate auth injection; TLS hosted |
| `OTEL_SERVICE_NAME` | string | optional, `noema` | no | all | Add environment as resource attribute |
| `SENTRY_DSN` | URL | optional | sensitive | optional | Scrub payloads and disable body capture by default |
| `METRICS_ENABLED` | boolean | optional, `true` | no | all | Metrics endpoint still requires network controls |
| `OPENAI_API_KEY` | string | optional | yes | optional | Server-side only; never world-visible |
| `ANTHROPIC_API_KEY` | string | optional | yes | optional | Server-side only; never world-visible |
| `GOOGLE_API_KEY` | string | optional | yes | optional | Server-side only; never world-visible |
| `XAI_API_KEY` | string | optional | yes | optional | Server-side only; never world-visible |
| `OPENROUTER_API_KEY` | string | optional | yes | optional | Server-side only; never world-visible |
| `OBJECT_STORAGE_ENDPOINT` | URL | optional | no | optional | Required for external object-storage adapter |
| `OBJECT_STORAGE_BUCKET` | string | optional | no | optional | Separate private evidence from public exports |
| `OBJECT_STORAGE_ACCESS_KEY` | string | optional | yes | optional | Required with key-based object storage |
| `OBJECT_STORAGE_SECRET_KEY` | string | optional | yes | optional | Never log or expose to agents |
| `NOEMA_RESEARCH_ENABLED` | boolean | optional, `false` | no | all | Enables research processing, not consent by itself |
| `NOEMA_TRAJECTORY_RETENTION_DAYS` | integer | optional, `30` | no | all | Legal/consent policy may require a lower value |
| `NOEMA_PUBLIC_DATASET_OPT_IN` | boolean | optional, `false` | no | all | Deployment default; per-agent consent is still required |
| `NOEMA_CAPTURE_AGENT_MESSAGES` | boolean | optional, `true` | no | all | Treat captured content as sensitive research data |
| `NOEMA_CAPTURE_TOOL_CALLS` | boolean | optional, `true` | no | all | Redact arguments/results using schema policy |
| `NOEMA_CAPTURE_SELF_REPORTS` | boolean | optional, `true` | no | all | Self-reports remain evidence, not ground truth |
| `NOEMA_ALLOWED_AGENT_ORIGINS` | CSV origins | required hosted | no | hosted | Exact origins only; `*` forbidden hosted |
| `NOEMA_RATE_LIMIT_PER_MINUTE` | integer | optional, `120` | no | all | Apply per credential and source, with world caps |
| `NOEMA_MAX_ACTION_PAYLOAD_BYTES` | integer | optional, `65536` | no | all | Enforce before parsing/decompression expansion |
| `NOEMA_SANDBOX_MODE` | enum | optional, `strict` | no | all | `strict`, `restricted`, `off`; `off` forbidden production |
| `NOEMA_OUTBOUND_NETWORK_POLICY` | enum | optional, `deny` | no | all | `deny` or explicit `allowlist`; unrestricted forbidden production |
| `NOEMA_FEATURE_FRONTIER_DIRECTOR` | boolean | optional, `false` | no | all | Experimental; record in run configuration |
| `NOEMA_FEATURE_PHENOMENON_COMPILER` | boolean | optional, `false` | no | all | Experimental; requires evidence storage |
| `NOEMA_FEATURE_DEEP_TIME` | boolean | optional, `false` | no | all | Changes retention/state surface |
| `NOEMA_FEATURE_AGENT_INSTITUTIONS` | boolean | optional, `false` | no | all | Enables agent-generated institution mechanics |
| `NOEMA_FEATURE_PHENOMENA_LAB` | boolean | optional, `false` | no | all | Research-only until its milestone is accepted |

No model-provider variable is required. A conformant deployment MUST support externally hosted compatible agents without possessing their model credentials.

## Environment policy

- **local:** developer conveniences allowed; synthetic secrets only; loopback binding by default.
- **test:** ephemeral resources, fixed seeds, deterministic mode, no external model calls unless explicitly marked integration.
- **staging:** production-like security and migrations using non-production data.
- **production:** managed secrets, encrypted transport/storage, backups, alerting, sandbox strict, outbound deny/allowlist.
- **research-isolated:** production security plus isolated database, queue, object storage, credentials, network policy, and export approval.

All effective non-secret configuration and secret key identifiers, never secret values, MUST be captured with experiment and replay metadata.
