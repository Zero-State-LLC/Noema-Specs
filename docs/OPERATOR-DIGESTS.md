# Operator Digests

**Authority.** Canonical **Operator Digest** layer: configurable periodic summaries of **settled** world activity for authorized Admins.

This document does not replace [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md), [WATCH.md](WATCH.md), [WORLD-REPORTS.md](WORLD-REPORTS.md), [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md), or control-plane audit. It does not mutate the world.

> Operator Digests compress canonical gameplay into configurable operational summaries.

Related: [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [SECURITY.md](SECURITY.md) · [PLATFORM.md](PLATFORM.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md) · [AGENT-HARNESS.md](AGENT-HARNESS.md).

---

## Doctrine

```text
Player action
  → Action Router
  → canonical event batch
  → settlement
  → world / Admin / WATCH projections
  → Operator Digest derivation
```

Digest generation is **downstream** of canonical gameplay. Digest text is derived output. It is **not** world truth.

```text
canonical ledger
+ world state / projections
+ digest configuration
→ digest
```

Where practical, a digest MUST be reproducible from the evidence window. Do not store generated prose as canonical history.

---

## Distinct surfaces

| Surface | Question | Authority |
|---|---|---|
| PLAY | What can I do? | [PLAY.md](PLAY.md) |
| WATCH | What is happening (public)? | [WATCH.md](WATCH.md) |
| World Report | Cycle-rhythm spectator news | [WORLD-REPORTS.md](WORLD-REPORTS.md) |
| Admin Live | Is the world operating correctly **now**? | [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) |
| Operator Digest | What happened in this **time window**? | this document |
| Audit | Exact control-plane / system trace | [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md), [OPERATIONS.md](OPERATIONS.md) |

```text
OPERATOR DIGEST
→ routine gameplay summary

OPERATIONAL ALERT
→ condition requiring timely operator attention
```

Do not mix them. Normal gameplay is **not** an immediate alert.

World Reports remain cycle-based, partial-observability spectator news. Operator Digests are **wall-clock** Admin summaries and MAY include operational information WATCH/World Reports omit.

Deep Time and lore derive from canonical history, not digest prose.

---

## Player ontology

```text
PLAYER
├── human controller
└── agent controller
```

Default digest language uses world identity:

```text
Nacre repaired Relay Trunk.
Daniel entered Coldline.
Vesper proposed a trade.
```

Do **not** default to “AI Agent Nacre” / “Human Player Daniel”. Controller type is optional operational metadata.

Harness telemetry MAY explain controller operation. It MUST NOT change digest gameplay summaries or introduce Controller credentials into digest prose. [AGENT-HARNESS.md](AGENT-HARNESS.md).

Optional breakdown (never two populations):

```text
Players active: 7
Human-controlled: 3
Agent-controlled: 4
```

---

## Immediate alerts vs periodic digest

Immediate notifications reuse existing incident/alert authority ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md), [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)). Do not invent a second taxonomy.

Immediate (examples):

```text
ledger / digest mismatch
world enters INCIDENT
settlement failure or BLOCKING lag
authentication failure spike
required-infrastructure World Service failure
stuck reservation
backup failure
version incompatibility
```

Periodic (examples):

```text
movement, inspect, trade, repair, harvest
organization activity, agreements, contests
World Service convenience activity
public research notices where allowed
```

### Incident precedence

If a critical operational alert occurs during a digest window: **send the immediate alert first**. The later periodic digest still summarizes the window and **references** the incident. Do not suppress routine evidence because an alert fired.

Delivery failure of a digest is **not** normally a gameplay `INCIDENT`. Report `DIGEST_DELIVERY_DEGRADED` (or equivalent). Do not pause PLAY because email failed.

---

## Cadence

First-world presets only (ISO-8601 durations):

| Preset | Duration |
|---|---|
| `OFF` | disabled |
| `PT15M` | 15 minutes |
| `PT30M` | 30 minutes |
| `PT1H` | 1 hour |
| `PT5H` | 5 hours |
| `PT10H` | 10 hours |
| `PT24H` | 24 hours |

First-world **minimum** frequency: **15 minutes**. Custom cadence is **DEFERRED**.

Recommended default: **`PT30M`**, **STANDARD**, dashboard on, email off.

Cadence is an operator preference. Changing it MUST NOT affect world state.

---

## Depth

Presentation only. Source authority does not change.

### BRIEF

Counts and health. Example:

```text
PERIHELION REACH — 30 MIN

7 Players active.
4 trades proposed.
1 relay repaired.
2 Players entered Coldline.
1 contest opened.

System healthy.
```

### STANDARD (recommended default)

Notable Player names, important locations, meaningful state changes, trade / infrastructure / institution activity, world condition, operational health.

### DETAILED

Action counts, event-class breakdown, resource/infrastructure deltas, org/trade/contest/agreement state, World Service activity, ledger/settlement **references**. Do not dump raw JSON.

---

## Composition

Approximate structure (headings MAY vary):

```text
WORLD HEADER
ACTIVITY
IMPORTANT CHANGES
ECONOMY / INFRASTRUCTURE / INSTITUTIONS
ATTENTION
SYSTEM STATUS
```

STANDARD / DETAILED MUST include concise system status, for example:

```text
World ACTIVE
Settlement healthy
No active incidents
```

World condition MAY reuse Admin Live derivations (infrastructure, economy, institutions, conflict, connectivity). Do not invent a parallel metric system.

Non-normative STANDARD example:

```text
PERIHELION REACH — 30 MIN DIGEST

Players active
7

Key activity
- Nacre repaired the Grid Anchor relay.
- Vesper proposed three trades; one settled.
- Two Players entered Coldline.
- Archive Fragment 4 was inspected twice.
- One access contest opened at Contract Town.

World changes
- Relay condition improved from 35 to 50.
- Trade access through Grid Anchor improved.
- Open trades increased from 2 to 4.

Attention
- Dead Spur remains isolated from a valid route.

System
Healthy
Settlement current
```

No invented motives.

---

## Windows and identity

Each digest MUST identify:

```text
world_id
window_start
window_end
generated_at
cadence
depth
source ledger / event boundary
```

Windows MUST NOT overlap by default:

```text
previous_digest_end → current_digest_end
```

Do not silently double-count events.

If persisted operationally, identity MAY be:

```text
digest.<world_id>.<window_end>.<sequence>
```

Digest IDs are **not** world truth.

### Missed delivery

A missed scheduled digest MUST NOT alter world state.

**Deterministic recovery:** the next generation emits a **separate** digest for the missed window (same cadence length), labeled missed/recovered, then the current window. Do not silently merge windows.

---

## Aggregation

Compress repeated low-level actions when the facts support it.

Bad: five LOOK/INSPECT/MOVE lines.  
Good: “Nacre explored Grid Anchor and Coldline and inspected two infrastructure sites.”

If events cannot safely be combined, report them separately. Do not invent a narrative.

Hard rule:

> Digests summarize observed canonical actions and derived state changes, not inferred intent.

If evidence is insufficient: omit the claim or mark `NOT_COMPUTABLE`. Do not guess why.

---

## Configuration

Only authorized Admin / control-plane principals may change digest settings. Players cannot configure global operator summaries.

First-world fields:

```text
enabled
cadence
depth
delivery channels
included categories
```

Categories MAY include: Player activity, Trade, Infrastructure, Organizations, Strategy, World Services, Research notices, System status. Controller metadata is optional.

**First-world preference model:** **per operator** when Admin identity supports distinct principals. If not, one global deployment setting. Do not build a subscription marketplace.

Configuration changes MUST be control-plane auditable:

```text
Admin principal
old/new cadence
old/new depth
delivery changes
timestamp
```

This is not gameplay history.

### First-world defaults (Perihelion Reach)

```text
Enabled:     yes
Cadence:     PT30M
Depth:       STANDARD
Dashboard:   enabled
Email:       disabled
Immediate operational alerts: enabled
```

Do not require email before Genesis.

---

## Delivery

First-world channels:

```text
ADMIN DASHBOARD   canonical
OPTIONAL EMAIL    operator-enabled
```

Do not require Slack, Discord, SMS, webhooks, or push infrastructure.

Dashboard SHOULD offer a **bounded** history (for example latest, 30m, 1h, 5h, 24h). Do not keep unlimited generated reports in the browser.

If email fails: world unaffected; digest remains in Admin; report `DIGEST_DELIVERY_DEGRADED`.

Scheduling MUST be possible on the existing hosted stack (Cloudflare scheduled/timer execution + settled-event queries) or equivalent. No dedicated queue/worker fleet. Specs do not pin a scheduler product.

---

## World-state coupling

Digest scheduling MUST NOT advance cycles, delay actions, change ordering, change settlement, or alter world state.

| `World.status` | Digest |
|---|---|
| `ACTIVE` | Normal recurring digest |
| `PAUSED` | MAY report maintenance + settled activity in the window |
| `INCIDENT` | Immediate alert first; digest still summarizes and cites the incident |
| `ARCHIVED` | No recurring digest unless explicitly configured |

---

## Privacy and security

Default digest MUST NOT include private MESSAGE text. It MAY include “4 private messages delivered” if policy permits. Privileged message inspection remains a separate audited Admin action.

MUST NOT include chain-of-thought, hidden reasoning, scratchpads, or unsubmitted plans.

Distinguish: canonical world state · private Player data · research-private state · Admin-private state · secrets.

Never include tokens, API keys, database credentials, service-role keys, or signing material.

Configuration requires authenticated Admin. Delivery destinations MUST be operator-controlled.

---

## World Services and research

MAY summarize World Service **observable** activity without implying agency beyond [WORLD-SERVICES.md](WORLD-SERVICES.md):

```text
Relay Keeper processed 5 infrastructure requests.
Registrar recorded 1 new institution.
```

Research notices are **optional**. Examples: Observatory candidates, Lab replication completed, LEARN rebuilt. No research-private detail unless Admin authority permits. Research failures alert separately; they do not stop PLAY ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)).

---

## LLM, fallback, cost

LLM summarization MAY enhance presentation later. It is **not** required.

Any model MUST be grounded only in provided canonical evidence. No world tools. No secrets. No private cognition.

First-world generation MUST have a deterministic fallback: templates, event aggregation, state-delta tables.

Retain provenance (source event refs, state boundary, aggregation rule/version, generation mode) for inspection. Do not require it in the default UI.

Do not design continuous LLM commentary, per-event inference, or per-Player narratives.

Generation MUST NOT materially degrade PLAY. Use the digest window only — do not scan complete history every 15 minutes.

Retention: recent operational history is enough. Canonical events remain permanent authority. Indefinite prose retention is not required.

---

## Non-normative Admin UI

```text
GAMEPLAY DIGESTS
Enabled [x]
Cadence [ 30 minutes ]
Depth [ STANDARD ]
Include Player / Trades / Infrastructure / Institutions / Strategy / World Services / System
[ ] Controller breakdown
[ ] Research notices
Delivery [x] Admin dashboard  [ ] Email
```

---

## Acceptance

1. Observational only; no world mutation.
2. Derived from settled canonical evidence.
3. Presets OFF / 15m–24h; minimum 15m; default 30m STANDARD.
4. BRIEF / STANDARD / DETAILED defined.
5. Routine gameplay summarized; failures alert immediately.
6. One Player population; optional controller breakdown.
7. Private messages hidden; no private cognition; no secrets.
8. Dashboard canonical; email optional.
9. No extra streaming/queue fleet required.
10. Deterministic fallback without LLM.
11. Admin Live / WATCH / Audit / Digest remain distinct.
12. First-world freeze includes this document.

---

## Non-goals

- v0.8
- Continuous commentary
- Slack/Discord/SMS/webhook first-world requirement
- Replacing Admin Live, WATCH, World Reports, or audit
