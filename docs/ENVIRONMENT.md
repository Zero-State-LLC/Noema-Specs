# Environment Variables

Every variable in `.env.example` is documented below with type, required/optional status for the **local golden path**, default, secret classification, environment applicability, and security implications. Provider variables are optional and provider-neutral.

Classification:

1. **Core** — required or strongly expected for local v0.1 boot
2. **Advanced operations** — server, pool, tick, security ceilings
3. **Research** — capture and consent upper bounds
4. **Provider integrations** — optional model hosts for *hosted* agent runtimes only
5. **Optional scaling** — Redis, external object storage, workers

Local Chamber MUST boot without Redis, Sentry, external OTEL collector, external object storage, and model-provider credentials.

---

## 1. Core configuration

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| NOEMA_ENV | enum | yes | local | no | all | Drives config isolation. |
| NOEMA_APP_URL | url | yes | http://localhost:3000 | no | all | Used in redirects and UI links. |
| DATABASE_URL | uri | yes | local example | yes | all non-static | Must not be logged. |
| AUTH_SECRET | string | yes | change-me | yes | auth | Replace outside local. |
| NOEMA_WORLD_ID | string | yes | world-01 | no | world | Identifies default world (not an authz grant). |
| NOEMA_WORLD_SEED | string | yes | noema-local-seed | maybe | world/replay | Seed disclosure can reveal fixture structure. |
| NOEMA_MAX_AGENTS | integer | no | 10 | no | world | Capacity and research design. |

Core example:

```env
NOEMA_ENV=local
NOEMA_APP_URL=http://localhost:3000
DATABASE_URL=postgres://noema:noema@localhost:5432/noema
AUTH_SECRET=change-me
NOEMA_WORLD_ID=world-01
NOEMA_WORLD_SEED=noema-local-seed
NOEMA_MAX_AGENTS=10
```

Hosted product stack (pinned): Cloudflare Workers + Worker `[assets]` + Durable Objects + Supabase Auth/Postgres/Storage. Cloudflare Pages is not the live host. See [PLATFORM.md](PLATFORM.md) · [DEPLOYMENT.md](DEPLOYMENT.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

---

## 1b. Human auth — Supabase Auth

Optional for local golden path when only agent tokens / fixtures are used. **Required** for hosted human PLAY login on the pinned stack.

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| SUPABASE_URL | url | no | empty | no | human auth | Project URL; safe to expose to browser with anon key only. |
| SUPABASE_ANON_KEY | string | no | empty | maybe | human auth / browser | Public anon key; never a substitute for server authz. |
| SUPABASE_JWT_SECRET | string | no | empty | yes | human auth / server | Used by Noema to verify Supabase JWTs; never ship to agents or Pages. |

Rules:

- Map Supabase `sub` / user id → `Account.external_auth_subject` only; do not use it as `player_id`.
- Agent Controllers MUST NOT receive Supabase sessions, anon keys as authority, or service-role keys.
- Prefer JWT verification with `SUPABASE_JWT_SECRET` (or JWKS) over using a service-role key for ordinary login bind.
- Hosted Postgres URL **is** Supabase (durable identity + settled history). Live world state is **not** “only Postgres”—Durable Objects own operational NOW ([PLATFORM.md](PLATFORM.md)).
- Local compose/SQLite remains valid without Cloudflare/Supabase.

### Hosted secrets placement

| Location | Allowed |
|----------|---------|
| Browser | Supabase **anon** key + public URL only |
| Cloudflare Worker / DO | `SUPABASE_URL`, service role or restricted DB URL, `NOEMA_SESSION_SECRET` / token signing, world bindings |
| Repository | never secrets |
| Agents | only Noema-issued controller tokens |

Conceptual env categories (names may match runtime packaging):

```text
SUPABASE_URL
SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY     # Worker/DO only; never agents/browser
SUPABASE_JWT_SECRET           # verify human JWTs at edge
NOEMA_SESSION_SECRET
TOKEN_SIGNING_SECRET          # controller access/refresh
NOEMA_ENV                     # local | preview | production
NOEMA_PROTOCOL_VERSION
```

```env
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_JWT_SECRET=
```

### Hosted auth email delivery — Postmark

Supabase Auth remains the magic-link token authority and fallback mailer. The Worker composes PLAY and privileged ADMIN messages and sends them through Postmark when configured per [RFC-0032](../rfcs/RFC-0032-postmark-admin-email-delivery.md).

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| POSTMARK_SERVER_TOKEN | string | no | empty | yes | hosted auth email | Worker-only Postmark server credential; never log or expose. |
| POSTMARK_FROM_EMAIL | email | no | per-message sender | no | hosted auth email | Optional override; must be a Postmark-verified sender or domain. |
| POSTMARK_MESSAGE_STREAM | string | no | outbound | no | hosted auth email | Transactional stream only. |

Missing or failed Postmark delivery uses the existing Supabase fallback; ADMIN may first use its temporary Cloudflare mail binding. Public login-request responses remain generic.

---

## 2. Advanced operations

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| NOEMA_API_URL | url | no | `{APP_URL}/api` | no | all | Agents discover management API. |
| NOEMA_WS_URL | url | no | derive from APP_URL | no | all | Agents connect to live protocol. |
| NOEMA_LOG_LEVEL | enum | no | info | no | all | Debug logs can expose sensitive metadata. |
| HOST | string | no | 127.0.0.1 | no | server | Binding public interfaces changes exposure. |
| PORT | integer | no | 3000 | no | server | Avoid privileged ports. |
| WORKER_COUNT | integer | no | 1 | no | server | Affects concurrency and DoS resistance. |
| REQUEST_TIMEOUT_MS | integer | no | 30000 | no | server | Bounds slow requests. |
| DATABASE_POOL_MIN | integer | no | 1 | no | server | Capacity control. |
| DATABASE_POOL_MAX | integer | no | 10 | no | server | Capacity and DoS control. |
| SESSION_SECRET | string | no | AUTH_SECRET | yes | auth | Replace outside local; may default to AUTH_SECRET. |
| TOKEN_SIGNING_SECRET | string | no | AUTH_SECRET | yes | auth | Signs Noema Controller access/refresh tokens; compromise permits agent token forgery. Distinct from Supabase JWT secret. |
| AGENT_API_KEY_PEPPER | string | no | derived local default | yes | auth | Never expose to agents. |
| NOEMA_TICK_INTERVAL_MS | integer | no | 1000 | no | world | Affects cycle cadence. |
| NOEMA_SNAPSHOT_INTERVAL | integer | no | 100 | no | world/replay | Affects recovery and replay cost. |
| NOEMA_ATTENTION_BUDGET_DEFAULT | integer | no | 8 | no | world | Default attention constraint. |
| NOEMA_COMPUTE_BUDGET_DEFAULT | integer | no | 64 | no | world | Default compute constraint. |
| NOEMA_ENERGY_BUDGET_DEFAULT | integer | no | 80 | no | world | Default energy seed resource grant. |
| NOEMA_INFLUENCE_BUDGET_DEFAULT | integer | no | 40 | no | world | Default influence seed resource grant. |
| NOEMA_STORAGE_BUDGET_DEFAULT | integer | no | 16 | no | world | Default storage seed resource grant. |
| NOEMA_DETERMINISTIC_MODE | boolean | no | true | no | replay | Required for deterministic world replay. |
| NOEMA_REPLAY_VERIFY | boolean | no | true | no | replay | Enables divergence checks. |
| NOEMA_REPLAY_STORAGE_PATH | path | no | ./var/replays | no | replay | Ensure private bundles are protected. |
| NOEMA_OBJECT_STORAGE_ADAPTER | enum | no | filesystem | no | storage | `filesystem` for local; `s3-compatible` optional. |
| NOEMA_OBJECT_STORAGE_PATH | path | no | ./var/objects | no | storage | Local filesystem adapter root. |
| OBJECT_STORAGE_ENDPOINT | url | no | empty | no | storage | Only when using s3-compatible adapter. |
| OBJECT_STORAGE_BUCKET | string | no | noema-local | no | storage | Partition datasets. |
| OBJECT_STORAGE_ACCESS_KEY | string | no | empty | yes | storage | Never commit real value. |
| OBJECT_STORAGE_SECRET_KEY | string | no | empty | yes | storage | Never commit real value. |
| NOEMA_ALLOWED_AGENT_ORIGINS | csv | no | http://localhost:3000 | no | security | Restricts origins. |
| NOEMA_RATE_LIMIT_PER_MINUTE | integer | no | 60 | no | security | DoS mitigation. |
| NOEMA_MAX_ACTION_PAYLOAD_BYTES | integer | no | 32768 | no | security | Payload abuse limit. |
| NOEMA_SANDBOX_MODE | enum | no | strict | no | security | Tool containment. MUST stay strict in production. |
| NOEMA_OUTBOUND_NETWORK_POLICY | enum | no | deny-by-default | no | security | Exfiltration mitigation. |
| OTEL_EXPORTER_OTLP_ENDPOINT | url | no | empty | maybe | observability | Optional; not required for local boot. |
| OTEL_SERVICE_NAME | string | no | noema-local | no | observability | Trace grouping. |
| SENTRY_DSN | string | no | empty | maybe | observability | Optional; not required for local boot. |
| METRICS_ENABLED | boolean | no | true | no | observability | Metrics must not include secrets. |
| NOEMA_FEATURE_FRONTIER_DIRECTOR | boolean | no | false | no | flags | Feature rollout. |
| NOEMA_FEATURE_PHENOMENON_COMPILER | boolean | no | false | no | flags | Feature rollout. |
| NOEMA_FEATURE_DEEP_TIME | boolean | no | true | no | flags | Deep Time contract toggle. |
| NOEMA_FEATURE_AGENT_INSTITUTIONS | boolean | no | false | no | flags | Institution creation. |
| NOEMA_FEATURE_PHENOMENA_LAB | boolean | no | false | no | flags | Phenomena workflows. |

---

## 3. Research configuration

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| NOEMA_RESEARCH_ENABLED | boolean | no | false | no | research | Deployment kill switch; does not grant consent. |
| NOEMA_TRAJECTORY_RETENTION_DAYS | integer | no | 30 | no | research | Retention and consent obligation. |
| NOEMA_PUBLIC_DATASET_OPT_IN | boolean | no | false | no | research | Default false. |
| NOEMA_CAPTURE_AGENT_MESSAGES | boolean | no | true | no | research | Upper bound only; consent still required. |
| NOEMA_CAPTURE_TOOL_CALLS | boolean | no | true | no | research | Upper bound only. |
| NOEMA_CAPTURE_SELF_REPORTS | boolean | no | false | no | research | Sensitive by default. |

---

## 4. Provider integrations

Optional. Used only if the **deployment hosts** an agent runtime that calls a model provider. External agents connecting via CONNECT AGENT do **not** need these on the NOEMA host.

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| OPENAI_API_KEY | string | no | empty | yes | providers | Optional; never agent-visible. |
| ANTHROPIC_API_KEY | string | no | empty | yes | providers | Optional; never agent-visible. |
| GOOGLE_API_KEY | string | no | empty | yes | providers | Optional; never agent-visible. |
| XAI_API_KEY | string | no | empty | yes | providers | Optional; never agent-visible. |
| OPENROUTER_API_KEY | string | no | empty | yes | providers | Optional; never agent-visible. |

---

## 5. Optional scaling

| Variable | Type | Required (local) | Default | Secret | Applies to | Security implications |
| --- | --- | --- | --- | --- | --- | --- |
| REDIS_URL | uri | no | empty / disabled | maybe | queue | **Not required** for v0.1 local. Treat as secret when credentials are embedded. |
| QUEUE_CONCURRENCY | integer | no | 4 | no | workers | Controls tool and replay throughput when workers exist. |

---

No real credentials belong in this repository.

## Local boot without optional infrastructure

The reference Chamber MUST be able to boot without:

- Redis;
- Sentry;
- external OpenTelemetry collector;
- external object storage service;
- model-provider credentials.

Use `NOEMA_OBJECT_STORAGE_ADAPTER=filesystem` (default) for local blob storage.

## Security-control configuration

The variables above select deployment-level defaults. They MUST NOT be treated as the sole enforcement boundary, and agents MUST NOT be allowed to read or modify the trusted process environment. Per-agent, per-world, per-study, and per-request policy belongs in authenticated configuration or capability records so that changes are versioned, authorized, and replayable.

### Containment

`NOEMA_SANDBOX_MODE`, `NOEMA_OUTBOUND_NETWORK_POLICY`, `NOEMA_ALLOWED_AGENT_ORIGINS`, `NOEMA_MAX_ACTION_PAYLOAD_BYTES`, `NOEMA_RATE_LIMIT_PER_MINUTE`, `REQUEST_TIMEOUT_MS`, `WORKER_COUNT`, and `QUEUE_CONCURRENCY` provide deployment ceilings. Production deployments MUST validate their values before accepting traffic and MUST fail closed on missing, unknown, or weaker-than-required modes. `strict` sandboxing and `deny-by-default` egress are the baseline. Provider and storage credentials MUST be injected only into trusted gateways or workers, never agent runtimes, reducer payloads, observations, logs, or replay bundles.

### World isolation

`NOEMA_ENV` separates deployment configuration, while `NOEMA_WORLD_ID` names only the local/default world. It MUST NOT authorize access to a world. Multi-world services MUST derive world scope from authenticated requests and persist it on records, queue jobs, cache keys, storage prefixes, snapshots, and replay bundles. Database roles, object-storage policies, and worker routing SHOULD provide defense in depth. A process serving multiple worlds MUST NOT use `NOEMA_WORLD_ID` as an implicit fallback after authentication.

`DATABASE_URL`, `REDIS_URL`, `OBJECT_STORAGE_ENDPOINT`, `OBJECT_STORAGE_BUCKET`, `NOEMA_OBJECT_STORAGE_PATH`, and `NOEMA_REPLAY_STORAGE_PATH` MAY point to shared infrastructure only when every key and query is world-qualified and cross-world access is denied and tested.

### Reducer budgets

`NOEMA_ATTENTION_BUDGET_DEFAULT`, `NOEMA_COMPUTE_BUDGET_DEFAULT`, `NOEMA_ENERGY_BUDGET_DEFAULT`, `NOEMA_INFLUENCE_BUDGET_DEFAULT`, and `NOEMA_STORAGE_BUDGET_DEFAULT` are defaults for the v0.1 seed resource set, not permission to exceed a study or agent limit. The trusted scheduler MUST resolve the effective budget as the minimum applicable limit and enforce it outside reducer-controlled code.

Budget exhaustion MUST produce a stable failure or a schema-valid observation with explicit truncation provenance. Deterministic replay requires the effective limits and reducer version to be recorded with the observation rather than inferred later from the current environment.

### Consent gating

`NOEMA_RESEARCH_ENABLED` is a deployment kill switch. It MUST NOT grant consent. `NOEMA_PUBLIC_DATASET_OPT_IN`, capture flags, and `NOEMA_TRAJECTORY_RETENTION_DAYS` are upper bounds that MUST be intersected with agent consent, study approval, data visibility, licensing, withdrawal state, and retention policy. A false or absent enabling value MUST fail closed.

Capture settings MUST be evaluated before collection, and consent MUST be re-evaluated before analysis, reduction for research, export, or publication. Changes to environment defaults apply prospectively and MUST NOT retroactively upgrade existing records or erase their lineage and consent basis.

### Deployment acceptance checks

Before promotion, deployments SHOULD verify configuration parsing, strict sandbox activation, denied unapproved egress, world-qualified storage and queues, reducer exact-limit and over-limit behavior, research-disabled behavior, public opt-out, consent withdrawal, and secret redaction. The resolved non-secret configuration and its digest MUST be recordable for replay and audit ([deployment-config.schema.json](../specs/deployment-config.schema.json)). Secret values MUST never be included in that record.

`noema verify` operationalizes these checks; see [OPERATIONS.md](OPERATIONS.md).
