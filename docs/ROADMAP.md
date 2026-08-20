# Roadmap

## v0.1 — The Chamber

Persistent strategic ecology (2–10 Players): rooms, movement, observations, structured actions, messaging, exact resource economy, production/harvest/repair, infrastructure, organizations, trade, deterministic scheduler, World Event Director pressure, spectator projections, event ledger, snapshots, world seed, deterministic replay.

**Onboarding and deployment (in-scope):** PLAY / WATCH / STUDY, with CONNECT as a separate Controller-onboarding path; Compose modular monolith; backup/verify; runtime manifest; restart persistence.

**WATCH — Lightweight Spectator Upgrade** (informal “WATCH v1.5”; not a product pin): public `/watch` as low-load world theater — one notable event, public world graph, bounded recent events, optional room detail. Spec: [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md). Does not reopen spectator-projection/1.0 or event catalogs.

**Player brand (presentation gate):** [PLAYER-BRAND.md](PLAYER-BRAND.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md) · [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md). Gates: `NOEMA_PLAYER_BRAND_SPEC_COMPLETE` (specified) → `NOEMA_PLAYER_BRAND_IMPLEMENTATION_READY` (plan) → `NOEMA_PLAYER_BRAND_IMPLEMENTED` (Slices 0–9 on `Zero-State-LLC/Noema`, hosted Worker HTML). See [PLAYER-BRAND-IMPLEMENTATION.md](PLAYER-BRAND-IMPLEMENTATION.md). Not an uncontrolled rewrite. Does not reopen world rules. No further brand slices unless a visual defect is filed.

**Identity / auth / gateway (spec-authoritative; runtime slice sequenced below):** Account → Player → Controller → Credential + PlayerSession; human auth via **Supabase Auth**; agent device enrollment; scoped credentials; Agent Gateway (REST / WebSocket; MCP later). Humans and agents are both Players.

**Hosted product stack (pinned):** Cloudflare Workers + Worker `[assets]` + Durable Objects · Supabase Auth + Postgres + Storage. Cloudflare Pages is not the live host. Specs: [PLATFORM.md](PLATFORM.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [DEPLOYMENT.md](DEPLOYMENT.md).

**Executable world contracts (in-scope):** [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) · [SCHEDULER.md](SCHEDULER.md) · [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [SPECTATOR.md](SPECTATOR.md) · [`examples/v01-strategic/`](../examples/v01-strategic/).

Golden path: [QUICKSTART.md](QUICKSTART.md). Acceptance: ADR-005 equivalence **and** C01–C26. See [v0.1-ACCEPTANCE.md](v0.1-ACCEPTANCE.md).

**Complexity doctrine (all future game systems):** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) — model causes, not industries; seven primitives; four pressures; A–J rejection tests. Future crypto / x402 / wallets / external settlement are hard-deferred.

**Core game design (player-facing structure):** [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) · [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) · [REALMS.md](REALMS.md) · [GEOGRAPHY.md](GEOGRAPHY.md) · [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [LOSS-RECOVERY.md](LOSS-RECOVERY.md) · [DIPLOMACY.md](DIPLOMACY.md) · [GAME-CYCLE.md](GAME-CYCLE.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md) · [PROGRESSION.md](PROGRESSION.md) · [AMBITIONS.md](AMBITIONS.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [GAME-BALANCE.md](GAME-BALANCE.md) · [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md) · [CHAMBER-MAP.md](CHAMBER-MAP.md) · [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) · [EXPLORATION.md](EXPLORATION.md) · [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) · [INFRASTRUCTURE.md](INFRASTRUCTURE.md).

**Game completeness (specification campaign, not executable):** [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md) · [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) · [MUD-PLAY-CRAFT-CLOSEOUT.md](MUD-PLAY-CRAFT-CLOSEOUT.md) · [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) · [CONSTRUCTION.md](CONSTRUCTION.md) · [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md) · [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md) · [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md) · [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md).

### Recommended implementation sequence (platform + identity)

Dependency order (does not open v0.8 game content):

1. Player identity model (Account / Player / Controller)
2. Supabase schema (identity + world)
3. Supabase Auth human bind → PlayerPrincipal
4. ControllerBinding + device enrollment credentials
5. Cloudflare Worker API boundary (Agent Gateway)
6. Stage 0 `NoemaWorldDO` + command path
7. Agent Protocol v1 / transport-independent commands over Worker/WS
8. Idempotent settlement of durable events to Postgres
9. **One** reference agent adapter (Hermes preferred; else REST agent)
10. OpenClaw / Grok as same-protocol adapters
11. Telemetry settlement + research capture
12. Admin control plane (separate principal) — [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)
13. First-world operate / recover / audit — [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)
14. Scaling topology only if evidence requires

**Not in early slices:** K8s, Redis, Kafka, multi-controller arbitration, framework-specific Core backends, premature DO sharding.

## v0.2 — The Frontier

Situation Genome, Frontier Director, partial observability, attention degradation, noise, contradictory evidence, novelty vectors, deterministic mutations, information-gain planning estimates, capability primitives (minimal), anti-repetition/controls, Frontier audit + replay, spectator research redaction.

**Executable package:** [docs/releases/v0.2/](releases/v0.2/) · [FRONTIER-DIRECTOR.md](FRONTIER-DIRECTOR.md) · [examples/v02-frontier/](../examples/v02-frontier/) · [conformance/v0.2/](../conformance/v0.2/) (F01–F15).

Prerequisite: v0.1 C01–C26 green. Frontier changes **conditions** only; does not force research outcomes.

## v0.3 — The Observatory

Trajectory representation, behavior features, baselines, anomaly/shift candidates, capability/unknown candidates, agent-version comparison, external cognition & coordination signals, Observatory audit + analysis-run identity, spectator research redaction.

**Executable package:** [docs/releases/v0.3/](releases/v0.3/) · [OBSERVATORY.md](OBSERVATORY.md) · [examples/v03-observatory/](../examples/v03-observatory/) · [conformance/v0.3/](../conformance/v0.3/) (O01–O16).

Prerequisite: v0.1 C01–C26 and v0.2 F01–F15 green. Observatory does not mutate world truth or force capability claims.

## v0.4 — The Lab

Deterministic replay harness, experimental forks, perturbation, ablation, lesion studies (adapter-declared), counterfactuals, controls, replication, and lab-result handoff to Compiler.

**Executable package:** [docs/releases/v0.4/](releases/v0.4/) · [EXPERIMENT-LAB.md](EXPERIMENT-LAB.md) · [examples/v04-lab/](../examples/v04-lab/) · [conformance/v0.4/](../conformance/v0.4/) (**L01–L34**, 146 atomic cases).

Prerequisite: C01–C26, F01–F15, O01–O16 green. Lab does **not** mutate production worlds; does not emit `PROVEN`. STUDY intents compile by versioned rules into the same isolated Lab plan, and simple results preserve Lab limits and capture readiness.

## v0.5 — The Compiler

Phenomenon Compiler executable package: CAPTURE AS TEST, capture-intent compilation, dependency-closed minimization, behavioral oracle, captured-test packages, receipts/audit, STUDY progressive disclosure, and behavioral regression (no scalar ranking).

**Executable package:** [docs/releases/v0.5/](releases/v0.5/) · [PHENOMENON-COMPILER.md](PHENOMENON-COMPILER.md) · [CAPTURE-INTENT-COMPILATION.md](CAPTURE-INTENT-COMPILATION.md) · [examples/v05-compiler/](../examples/v05-compiler/) · [conformance/v0.5/](../conformance/v0.5/) (**P01–P30**, 90 atomic cases).

Prerequisite: C01–C26, F01–F15, O01–O16, S01–S18, L01–L34, RFC-0003 green. Compiler does **not** rewrite Lab/world history; ordinary users see one action — CAPTURE AS TEST — while machine contracts pin full determinism.

## v0.6 — Deep Time

**Foundation (this package):** institutions, succession, historical artifacts, evidence, archaeology/reconstruction, institutional memory, cultural transmission foundations, world scars, historical names — so structures persist beyond agents and lore can later be **derived** from real history (never a second canon).

**Admin-only Genesis (simplified):** one-time world creation from seed + 3 profiles + optional story seeds → valid Cycle 0 → activate; no player Genesis surface, no Genesis runtime service.

**Executable package:** [docs/releases/v0.6/](releases/v0.6/) · [DEEP-TIME.md](DEEP-TIME.md) · [GENESIS.md](GENESIS.md) · [examples/v06-deep-time/](../examples/v06-deep-time/) · [conformance/v0.6/](../conformance/v0.6/) (**D01–D30** + **G01–G09**).

Prerequisite: C/F/O/S/L/P + RFC-0003 green. No runtime Deep Time engine; no authored lore canon; no silent event-catalog expansion.

**Recommended follow-ups (not started):** v0.6B Contracts & Markets · v0.6C Semantic Evolution (full).

## v0.7 — Capability Graph / LEARN (minimal)

Minimal evidence-backed behavior relationships and simple LEARN surface: what was reproduced, by whom, dependencies, generalization, failures, and not-yet-tested — derived from captured tests and Lab/regression evidence.

**Executable package:** [docs/releases/v0.7/](releases/v0.7/) · [CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md) · [LEARN.md](LEARN.md) · [examples/v07-capability-graph/](../examples/v07-capability-graph/) · [conformance/v0.7/](../conformance/v0.7/) (**K01–K12**).

Prerequisite: C/F/O/S/L/P/D/G + RFC-0003 green. No graph DB/service, ranking, consciousness scores, or architecture attribution.

**Deferred beyond v0.7:** phase transitions, automatic ontology induction, architecture attribution (later research).

**Core-loop freeze:** [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) — freeze v0.1–v0.7 for implementation; do not open v0.8 until runtime feedback demands it.

## Game Completeness — parallel PLAY-depth campaign (not a release tag)

Post-core **specification** campaign for mature Player-world depth. It does **not** reopen v0.1–v0.7 machine contracts, does **not** redefine v0.6B Contracts & Markets or v0.6C Semantic Evolution, and does **not** open **v0.8 Phenomena**.

Authority: [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · ancestry [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md).

```text
GC-A  Identity and Persistence     GC1 Mastery · GC2 Construction · GC3 Social Memory
GC-B  Society and Information      GC4 Offices · GC5 Communication · GC6 Discovery
GC-C  Strategic Depth              GC7 Conflict v2 · GC8 Economic specialization
GC-D  Civilization                 GC9 Emergent culture · GC10 World Event Director
```

These phases are design authorities. They are **not** executable packages. Machine contracts, fixtures, and conformance remain **SPEC GAP** until RFC.

**Shipped:** **GC1-S0 Derived Practice Projection** ([GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md), Accepted [RFC-0004](../rfcs/RFC-0004-derived-mastery-projection.md)).

**GC1-S1 Recognition** ([GC1-S1-RECOGNITION.md](GC1-S1-RECOGNITION.md), Accepted [RFC-0005](../rfcs/RFC-0005-mastery-recognition.md)): self-only recognized lines at distinct-unit thresholds. Hosted Chamber PLAY (runtime PR #69). No benefits. No new events.

Mechanical benefit is **GC1-S2** (separate RFC). Do not implement S1 or S2 in the same cut as S0.

**GC2-S0 construction pins** ([GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md), Accepted [RFC-0006](../rfcs/RFC-0006-construction-existing-events.md)): `CONSTRUCT` / `DISMANTLE` on the four v0.1 infrastructure classes using existing `ENTITY_*` events. `BUILD` stays unsupported in Chamber PLAY until a later implementation pass.

**GC3-S0 social memory** ([GC3-FIRST-SLICE.md](GC3-FIRST-SLICE.md), Accepted [RFC-0007](../rfcs/RFC-0007-dyadic-trade-memory.md)): derived Player→Player reliability from accepted trades. Hosted Chamber PLAY (runtime PR #70). No reputation integer.

**GC4-S0 office authority** ([GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md), Accepted [RFC-0008](../rfcs/RFC-0008-office-authority-pins.md)): existing v0.1 roles as membership grants. Hosted Chamber PLAY pin (runtime PR #71). No Steward/Treasurer freeze. No `ROLE_*` events.

**GC5-S0 relay MESSAGE bands** ([GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md), Accepted [RFC-0009](../rfcs/RFC-0009-relay-message-delivery.md)): long-range delivery requires a live relay at the existing condition 25 band. Local same-room `MESSAGE` is unchanged. Hosted Chamber PLAY (runtime PR #72).

**GC6-S0 discovery contradiction** ([GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md), Accepted [RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md) · [RFC-0015](../rfcs/RFC-0015-archive-record-source.md)): archive vs live `INSPECT` as a self-only PLAY line. Source is explicit ARTIFACT `archive_subject_entity_id` + `archive_claim`. Perihelion has neither field; PLAY unprojected. No quest log. No Genesis pack.

**GC7-S0 contest rhythm** ([GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md), Accepted [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md)): RECON→RECOVER composed from existing v0.2 forms and verbs. No HP. No `event-catalog/0.3`. No Chamber contest thaw.

**GC8-S0 distance interdependence** ([GC8-FIRST-SLICE.md](GC8-FIRST-SLICE.md), Accepted [RFC-0012](../rfcs/RFC-0012-distance-interdependence.md)): pair harvest+trade vs lone move. Already true in hosted v0.1 costs. Not v0.6B. No currency.

**GC9-S0 maintenance custom** ([GC9-FIRST-SLICE.md](GC9-FIRST-SLICE.md), Accepted [RFC-0013](../rfcs/RFC-0013-maintenance-custom.md)): repeated `REPAIR` becomes an inherited custom. Hosted Chamber PLAY (runtime PR #71). Lore cannot override the ledger. Not v0.6C.

**GC10-S0 WED schedule** ([GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md), Accepted [RFC-0014](../rfcs/RFC-0014-wed-schedule-pressure.md)): cycle-4 mild relay condition drop via existing `ENTITY_UPDATE`. No forced outcome. No Chamber runtime.

v0.6B and v0.6C stay distinct recommended follow-ups. GC8/GC9 may later depend on them; they do not consume those names.

## v0.8 — Phenomena

Self-model metrics, temporal continuity, metacognition, integration, autogenous goals, and introspective causal accuracy.

## v0.9 — Atlas

Reproducibility bundles, dataset release tooling, public/private partitions, cross-model comparison, and research reports.

## v1.0 — NOEMA

Acceptance: a third party can connect an arbitrary compatible agent, allow it to inhabit NOEMA, discover a candidate capability, reproduce the event, test its generalization and dependencies, and export the evidence as a versioned Reproducibility Bundle.

## Cross-cutting experience requirement

Every future milestone MUST provide a simple user-facing workflow, an advanced technical workflow, and a versioned machine contract. Product navigation uses PLAY / WATCH / STUDY and the explanatory sequence PLAY → NOTICE → TEST → CAPTURE → LEARN. This presentation layer cannot weaken determinism, research isolation, claims discipline, partial observability, agent parity, or conformance.
