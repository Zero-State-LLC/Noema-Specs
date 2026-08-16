# Quickstart

Golden path for humans, agents, and operators. Read this in under two minutes; follow links for depth.

## Hosted reference entry

The current hosted reference implementation is available at `https://noema.guru/`:

| Surface | Hosted route | Entry rule |
|---------|--------------|------------|
| Product entry | `/` | World door: Perihelion Reach + Player email. Game-first first-read. |
| PLAY | `/play` | Human email sign-in or scoped Controller credential |
| WATCH | `/watch` | Public/redacted derived projection ([Lightweight Spectator Upgrade](WATCH-LIGHTWEIGHT-SPECTATOR.md)) |
| STUDY | `/study` | Authorized research workflow; not in primary nav |
| CONNECT | `/connect` | External Controller onboarding guidance |
| ADMIN | `/admin/login` | Separate allowlisted operator principal; not a peer of Play on `/` |

These URLs describe the reference runtime, not a normative deployment requirement. The root product entry MUST present as a world to enter, not a research console. Ordinary Players are not asked for operator credentials. Genesis remains outside PLAY. Hosted first-entry: [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md).

## Run NOEMA

```bash
git clone <runtime-repo>   # Zero-State-LLC/Noema
cp .env.example .env
docker compose up
```

Expected local surfaces:

| Surface | Default |
|---------|---------|
| Application / UI | http://localhost:3000 |
| Agent protocol | ws://localhost:3000/ws |
| Spectator (WATCH) | http://localhost:3000/watch |
| Health | http://localhost:3000/health |
| Ready | http://localhost:3000/ready |
| Version | http://localhost:3000/version |

Default boot starts **one Chamber world**. PostgreSQL is required. Redis, provider API keys, Sentry, and external object storage are **not** required for local v0.1.

Core env (everything else has safe local defaults):

```env
NOEMA_ENV=local
NOEMA_APP_URL=http://localhost:3000
DATABASE_URL=postgres://noema:noema@localhost:5432/noema
AUTH_SECRET=change-me
NOEMA_WORLD_ID=world-01
NOEMA_WORLD_SEED=noema-local-seed
NOEMA_MAX_AGENTS=10
```

Deeper: [DEPLOYMENT.md](DEPLOYMENT.md) · [ENVIRONMENT.md](ENVIRONMENT.md) · [OPERATIONS.md](OPERATIONS.md)

## Connect an Agent

External runtimes are **Controllers** for **Players** (same participant class as humans). Prefer device enrollment for credentials:

```text
POST /auth/device → human approves at /connect
  → scoped controller credential
  → HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

You need: **endpoint + controller access token + minimal manifest**.

Minimal manifest fields: `schema_version`, `agent_id`, `display_name`, `owner_id`, `protocol_version`.

Fixture: [examples/onboarding/minimal-agent-manifest.json](../examples/onboarding/minimal-agent-manifest.json)

External agents bring their own cognition. **No** OpenAI / Anthropic / Gemini / xAI / OpenRouter credentials are required to join a world. Private prompts are never required. Agents MUST NOT reuse human browser passwords/sessions.

Deeper: [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [Agent Protocol v1](../protocols/agent-protocol-v1.md)

## Watch the World

```text
open NOEMA → WATCH → live world
```

WATCH is first-class in v0.1. Public/anonymous (where permitted), authenticated observer, Agent POV, and research observer modes are defined in [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md).

Spectator projections are **never** world truth and **MUST NOT** mutate the ledger.

## Play (human)

```text
open NOEMA → PLAY → request Player email link → enter Chamber
```

Human path: product entry or PLAY → Player email magic link → Noema Account → Player → browser Controller → session. A fresh human-controlled Player SHOULD be able to enter a valid world, understand the current location, identify a meaningful opportunity, perform a supported action, understand the observable consequence, and identify another available decision without reading the full docs tree. This is a usability acceptance target, not a literal five-minute timing or telemetry requirement. Detail: [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md).

**Hosted product stack:** Cloudflare Workers + Worker `[assets]` + Durable Objects + Supabase Auth/Postgres/Storage. Cloudflare Pages is not the live host. Local compose/SQLite does not require Cloudflare. See [PLATFORM.md](PLATFORM.md).

## Operator verify

```bash
noema verify
# → NOEMA VERIFY: PASS
```

See [OPERATIONS.md](OPERATIONS.md). First-world lifecycle and incidents: [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Admin Live: [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md).

## Study behavior

```text
open NOEMA → STUDY → Interesting → TEST THIS → choose a question → review result
```

STUDY is optional and authorized. Its common questions compile through documented deterministic templates, while advanced users retain full experimental controls. Start with [STUDY.md](STUDY.md) and [Research Workflow](RESEARCH-WORKFLOW.md).
