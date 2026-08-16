# Changelog

## [Unreleased]

### Added

- **RFC-0039 Accepted / GC3-S7:** preferred-counterparty discount waives `TRADE_CAUTION` when a live `RELIABLE` edge exists. No auto-accept. No hidden rebate. Base TRADE compute stays 1.

### Changed

- **Hosted static pin:** product HTML is Cloudflare Worker `[assets]` on `noema.guru`. Cloudflare Pages is not the live host. GitHub Pages (`site/`) remains marketing/reference.

### Added

- **RFC-0034–0038 Accepted / GC3-S2–S6:** remaining SOCIAL-MEMORY SPEC GAP closed as spec-only slices. WATCH public bands from already-public events (else silent; S0/S1 stay off WATCH). Institution→player edges. Decay/rehab weights (12 cycles / 3 restitution trades; no wipe). Published +1 compute `TRADE_CAUTION` (no auto-refuse). Distinct deceptive edge (`AGREEMENT_BROKEN` / contradicted public `ATTEST`; `TRADE_REJECTED` ignored). No new verbs. No reputation scalar. No runtime in this change.

### Added

- **Social-machine pins:** (1) Deep Time usability — short-session Players MUST be able to leave one durable public/institutional mark; no `TRACE` verb. (2) SOCIAL-MEMORY — WATCH MAY show coarse public descriptor bands only from already-public events; silence if insufficient. (3) INSTITUTIONAL-AUTHORITY — office conflict-precedence is published list or strict-subset scope, else fail closed. No new authority families, verbs, or private-leak paths.

### Changed

- **WATCH Phosphor Glyph Atlas v0.1 locked:** `room_partial` is a three-sided open square; `player_multi` is two stacked diamonds; `player_cluster` is 4×4 + 2×2 bright core. Drawing order exits → rooms → players → pulses. Pure Canvas 2D paths. Spec: `docs/WATCH-LIGHTWEIGHT-SPECTATOR.md` §18.5.

### Added

- **WATCH Phosphor Cartography (optional):** Canvas 2D 320×180 sketch of the same `watch-live/1.0` public snapshot. TEXT remains default and complete. Glyph Atlas v0.1. No new fields, no WebGL, no version pin. Spec: `docs/WATCH-LIGHTWEIGHT-SPECTATOR.md` §18.

### Added

- **WATCH — Lightweight Spectator Upgrade:** public hosted `/watch` as low-load terminal theater (one notable event, public world graph, 5–8 recent events, optional room detail). Informal nickname “WATCH v1.5” is **not** a product pin. Presentation tiers `NORMAL` / `NOTABLE` / `MAJOR`. Pin `watch-live/1.0`. Spec: `docs/WATCH-LIGHTWEIGHT-SPECTATOR.md`. No event-catalog or Genesis change.

### Added

- **RFC-0033 Accepted:** defines non-executable email bootstrap, a machine-readable enrollment document, and an optional operator-approved skill installed into an isolated game-only Controller profile.
- **RFC-0032 Accepted:** Postmark replaces Resend for preferred Worker-composed PLAY and ADMIN magic-link delivery. Supabase remains token authority and fallback; the temporary Cloudflare ADMIN binding is unchanged.
- **Hosted first-entry:** game-first world door at `/` (Perihelion Reach + Player email). Operator login leaves the primary column. Research vocabulary is off first-read. Chamber first screen stays text-first play. Spec: `docs/HOSTED-FIRST-ENTRY.md`. No protocol, Genesis, or world-rule change.

### Added

- **Hosted canonical-head status:** Noema #96 / `272a993` is deployed. Isolated-world verification and Perihelion canonical bootstrap remain blocked. Operator SQL/RPC apply still required. No Genesis reseed.

### Added

- **RFC-0031 Accepted / GC4-S4:** designated institutional succession. Explicit predeclared successor list on an office or emergency scope. No implicit jump. Emergency successor inherits remaining duration. No `SUCCESSION_*` events.

### Added

- **RFC-0030 Accepted / GC4-S3:** institutional emergency scopes as time-bounded AuthorityGrant overlays. Predeclared templates, world-time expiry, no superuser, no `EMERGENCY_*` events.

### Added

- **RFC-0029 Accepted / GC4-S2:** institutional TRADE and REPAIR through occupied office profiles (`OPERATE_RESOURCE_ACCOUNT`, `OPERATE_NAMED_ASSET`). Ordinary verbs. Institution treasury stays institution-owned. No finance engine.

### Added

- **RFC-0028 Accepted / GC5-S2:** rumor provenance as claim + `MESSAGE` lineage. Unchanged retelling keeps the claim; material change derives a new claim. No rumor score. No `RUMOR` verb. No `event-catalog/0.3`.

### Added

- **RFC-0027 Accepted / GC10-S1:** additional world pressure classes (`resource_scarcity`, `access_restriction`) via existing `ENTITY_UPDATE` / `ACCESS_RESTRICTED`. S0 relay drop remains. No Admin spawn. No rubber-band. No `event-catalog/0.3`.

### Added

- **RFC-0026 Accepted / GC7-S1:** contest withdraw via `COMMIT.CONTEST_WITHDRAW`. Settles existing `CONTEST_RESOLVED` (`ABORTED` or forfeit `SUCCESS`). No HP. No `event-catalog/0.3`.

### Added

- **RFC-0025 Accepted / GC9-S1:** tradition from persistent transmitted custom (or public reconstruction citation). Dormant/revived. No bonus. Bounded public WATCH pulses. No `event-catalog/0.3`.

### Added

- **RFC-0024 Accepted / GC6-S1:** Player-authored historical reconstruction from accessible `ARCHIVE_CLAIM` / `LIVE_INSPECT` evidence. Contradiction may be recorded. Not canonical truth. No `QUEST`. No `event-catalog/0.3`.

### Added

- **RFC-0023 Accepted / GC4-S1:** named institutional offices as persistent vacant/occupied seats on an organization. Membership roles unchanged. Evidence is `ENTITY_CREATE` / `ENTITY_UPDATE`. No `ROLE_*`. Hosted exercise is `PUBLISH_NOTICE` only.

### Added

- **RFC-0022 Accepted / GC3-S1:** private danger edge from `CONTEST_RESOLVED` (and `AGREEMENT_BROKEN` / `CRIME_DETECTED` when those events exist). Line `You have found {name} dangerous.` Self only. No reputation scalar. `TRADE_REJECTED` still ignored. Does not thaw `AGREEMENT_FORM`.

### Added

- **RFC-0021 Accepted / GC5-S1:** long-range `MESSAGE` delays 1 world cycle when the best live relay is 25–49. Same-cycle at ≥ 50. Rumor still out. No new verbs.

### Added

- **RFC-0020 hosted:** `COMMIT.ATTEST` writes paired archive-claim fields on a visible ARTIFACT. `INSPECT` remains a reader. Chamber help omits ATTEST. No Genesis pack.

### Added

- **S0 closeout + RFC-0020 Accepted:** `docs/GC-S0-CLOSEOUT-2026-08-13.md` and `docs/GC-S1-ORDER.md`. Later `COMMIT.ATTEST` is specified only; runtime unsupported. No Genesis pack. No Chamber help. Readiness snapshot updated in Noema.

### Added

- **GC10-S0 hosted:** cycle-4 schedule drops a live relay by 15 via `ENTITY_UPDATE` when the preview stays ≥ 25. One fire in cycles 1–20. PLAY omits WED. No Admin spawn. No Genesis reseed.

### Added

- **GC7-S0 hosted:** isolated `CONTEST_DECLARE` → world-side `CONTEST_RESOLVED` on RFC-0019 cycle commit. Four existing forms. No HP. Chamber help still omits CONTEST. No `event-catalog/0.3`.

### Added

- **RFC-0019 Accepted:** hosted world-time. `WAIT` still does not advance `World.cycle` alone; present-player wait quorum is the cycle commit. No contest. No WED. No Genesis reseed. GC7 thaw-readiness (`docs/GC7-THAW-READINESS.md`) is not a thaw.

### Added

- **GC2-S0 hosted:** Chamber `BUILD` CONSTRUCT/DISMANTLE on the four existing infrastructure classes (Noema #79). Existing `ENTITY_CREATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` only. Chamber help still omits BUILD. No `event-catalog/0.3`.

### Added

- **RFC-0017 Accepted:** hosted cycle fence and durable settlement recovery. `STALE_HEAD` on revision mismatch; no last-write-wins; no Genesis recovery. No gameplay.
- **RFC-0018 Accepted:** archive-claim writer is `ENTITY_CREATE` / allowlisted `ENTITY_UPDATE` only. `INSPECT` is not a writer. No Chamber verb. No Genesis pack.
- **GC2 thaw readiness:** `docs/GC2-THAW-READINESS.md` — architecture not a blocker; BUILD still unauthorized.

### Added

- **Remaining-work snapshot:** `docs/REMAINING-WORK-2026-08-13.md` lists shipped S0, operator SQL, thaw-gated GC2/GC7/GC10, and SPEC GAP S1s. Not a thaw.

### Added

- **RFC-0016 Accepted:** hosted durable world head. Postgres `noema_world_heads` is the reconstructable WorldRuntime copy; DO remains live ordering. Restore only when DO world is missing. No Genesis reseed. No new events. SERIALIZABLE cycle fence remains later.

### Added

- **Hosted readiness pointer:** SPEC-CHECKLIST architecture pause notes that Postgres reconstructable world record is unimplemented; evidence in Noema `docs/RUNTIME-READINESS-2026-08-13.md`. No contract change.

### Added

- **RFC-0015 Accepted:** GC6-S0 archive-record source. Accessible archive member only from `INSPECT` of an `ARTIFACT` that already has `archive_subject_entity_id` and `archive_claim` ∈ {DESTROYED, OPERATING}. Perihelion `entity.archive-ledger` has neither field, so PLAY stays unprojected. Flavor-text inference and a destroyed-relay Genesis pack remain rejected. No catalog 0.3. No frozen contract rewrite.

### Added

- **GC6-S0 hosted adapter blocked:** Chamber has no structured archive `{subject_entity_id, claim, accessible_to}`. Flavor-text inference and a Perihelion destroyed-relay pack remain rejected. Architecture pause footer aligned: reducer registry already landed.

### Added

- **Hosted slice status reconciliation:** GC1-S1 (#69), GC3-S0 (#70), and GC4-S0 pin (#71) marked shipped. GC8-S0 recorded as already true in hosted `HARVEST`/`MOVE`/`TRADE` costs. No catalog change. No new runtime behavior.

### Added

- **GC5-S0 hosted:** Chamber `MESSAGE` applies relay delivery bands (Noema #72). Same-room always delivers; long-range needs best live relay ≥ 25 or fails `UNREACHABLE` with no events. Specs status updated to shipped. No catalog change.

### Added

- **GC9-S0 hosted:** Chamber PLAY projects `This site has a maintenance custom.` for accessors after three distinct repairs (Noema #71). Specs status updated to shipped. No catalog change.

### Added

- **Reducer registry + mutation ownership:** `docs/REDUCER-REGISTRY.md` indexes existing 0.1/0.2 event reducers and names the sole writer for each field family. Derived GC projections are non-writers. No new events. No runtime.

### Added

- **2026-08-13 — Notion ↔ Specs reconciliation:** `docs/NOTION-RECONCILIATION-2026-08-13.md` assimilates cross-cutting doctrine (parity, labor/delegation, law, privacy, decay, measurement membrane, operator receipts, invariants, action/event/state/time/schema/enforcement). Clarifies hosted authority **inside** the existing Cloudflare + Supabase stack: DO = live ordering/process coordination; Postgres = durable canonical record and recoverability. Architecture-design frontier **paused**. No runtime implementation. No crypto/future-economy activation. Frozen v0.1–v0.7 wire contracts unchanged.

### Added

- **Admin Live operations surface:** `docs/ADMIN-LIVE-OPERATIONS.md` is the canonical control-plane observation contract. Admin remains a separate principal (not `ADMIN_PLAYER` / `GM_PLAYER`). Default Live is observational (`OBSERVE` / `INSPECT` / `DIAGNOSE`); `OPERATE` is explicit and audited through existing Action Router / intervention paths; `AUDIT` navigates the existing ledger. Covers world pulse, settled event feed, progressive inspection, operational topology, inspectors, redaction classes, secret status-only handling, Overview vs Live IA, freshness, bounded polling, and PLAY/WATCH separation. No new schema, milestone, or gameplay. Updates: TERMINOLOGY, EXPERIENCE, WATCH, OPERATOR-INTERVENTIONS, FIRST-WORLD-SPEC-FREEZE, SPEC-CHECKLIST.

### Added

- **RFC-0014 Accepted:** GC10-S0 seeded mild relay pressure. Cycle 4 schedule drops a named relay by 15 via `ENTITY_UPDATE`; preview matches activation; no forced Player response; no Frontier ID share. No runtime.

### Added

- **RFC-0013 Accepted:** GC9-S0 maintenance custom. ≥3 distinct `ENTITY_UPDATE` repairs on one site become a derived `CUSTOM`; later `INSPECT` inherits; lore cannot override the ledger. No v0.6C. No runtime.

### Added

- **RFC-0012 Accepted:** GC8-S0 distance interdependence. Two-Player `HARVEST`+`TRADE` spends less energy than a lone `MOVE` between rooms. No currency, order book, v0.6B, mastery yield, or wallets. No runtime.

### Added

- **RFC-0011 Accepted:** GC7-S0 existing contest rhythm. Stage table over `event-catalog/0.2` verbs and the four v0.2 forms. No HP, no death, no fifth form, no catalog mutation. No runtime.

### Added

- **RFC-0010 Accepted:** GC6-S0 archive vs live `INSPECT` contradiction. Relay Seven pattern as derived PLAY line; no quest UI; `known_truth_relationship` stays off PLAY; WATCH empty. No new verbs. No runtime.

### Added

- **RFC-0009 Accepted:** GC5-S0 relay bands on existing `MESSAGE`. Same-room delivery ignores relay condition; different-room requires best live relay ≥ 25; `UNREACHABLE` emits no events and no topology leak. No new verbs. No runtime.

### Added

- **RFC-0008 Accepted:** GC4-S0 existing roles as bounded authority. Pins founder/officer invite and remove, member/advisor self-leave only, no founder invite, last-founder guard, cosmetic titles have zero authority. No `ROLE_*` events. No runtime.

### Added

- **RFC-0007 Accepted:** GC3-S0 dyadic trade memory. Derived edges from `TRADE_ACCEPTED`; RELIABLE at 3 distinct trades; no reputation scalar; WATCH empty; leak tokens forbidden. No runtime.

### Added

- **RFC-0006 Accepted:** GC2-S0 construction pins. `CONSTRUCT`/`DISMANTLE` on existing infrastructure classes; reuses `ENTITY_CREATE`/`ENTITY_DESTROY`; no `event-catalog/0.3`. Attempt fixtures + `check_gc2_s0`. No runtime BUILD.

### Added

- **RFC-0005 Accepted:** GC1-S1 recognition catalog `mastery-catalog/gc1-s1`, rebuild fixtures (cross-threshold and same-entity repair spam), `check_gc1_s1`. No benefits, no event-catalog change.

### Added

- **Complexity Doctrine:** `docs/COMPLEXITY-DOCTRINE.md` — model causes, not industries; seven primitives; four pressures; noun-stable verbs; civilization ladder; decision/coupling density; A–J acceptance tests; hard deferral of crypto/x402/wallets/external settlement. Completeness campaign and system map now cite it. No runtime, no new schemas for deferred economy.
- **GC1-S1 Recognition (Draft):** `docs/GC1-S1-RECOGNITION.md` + `rfcs/RFC-0005-mastery-recognition.md`. Distinct-unit recognition thresholds; self-only line replacement; no benefits; cycle-0 safe. Not executable until RFC-0005 is Accepted with fixtures.

### Added

- **RFC-0004 Accepted:** GC1-S0 derived practice projection. Catalog `specs/mastery-catalog.gc1-s0.json`, rebuild schema, executed fixtures, conformance M01–M03. No `event-catalog` change. No mechanical benefits.

### Added

- **GC1-S0 slice audit:** `docs/GC1-FIRST-SLICE.md` selects the smallest later runtime slice (derived explorer/surveyor/broker/engineer practice, self-only PLAY lines, no benefits). Draft `rfcs/RFC-0004-derived-mastery-projection.md`. No schemas, no event-catalog change, no runtime code.

### Added

- **NOEMA MUD Completeness Expansion (specification campaign):** parallel PLAY-depth track beside the frozen v0.1–v0.7 core loop. Does not open v0.8 Phenomena and does not redefine v0.6B/v0.6C. Campaign: `docs/GAME-COMPLETENESS-PLAN.md`. Ancestry: `docs/MUD-DESIGN-CANON.md`. Domain authorities: `docs/MASTERY-SPECIALIZATION.md` (GC1), `docs/CONSTRUCTION.md` (GC2; closes generalized BUILD deferral at spec level), `docs/SOCIAL-MEMORY.md` (GC3), `docs/INSTITUTIONAL-AUTHORITY.md` (GC4), `docs/COMMUNICATION-ECOLOGY.md` (GC5), `docs/SYSTEMIC-DISCOVERY.md` (GC6), Strategic Conflict GC7 v2 section, `docs/ECONOMIC-SPECIALIZATION.md` (GC8), `docs/EMERGENT-CULTURE.md` (GC9), `docs/WORLD-EVENT-DIRECTOR.md` (GC10). No new schemas, event types, or conformance suites. Machine contracts remain SPEC GAP until RFC. Preferred later runtime slice: GC1 Mastery.

### Added

- **Hosted experience alignment:** the reference Worker now projects the Specs entry model with Player email entry and PLAY primary at `/`, WATCH/STUDY/CONNECT as secondary doors, and ADMIN as a separate allowlisted control-plane route. `docs/EXPERIENCE.md` defines CONNECT as Controller onboarding rather than a Player mode; `docs/QUICKSTART.md` records current hosted routes as non-normative implementation guidance.
- **Operator Digests:** `docs/OPERATOR-DIGESTS.md` — configurable periodic Admin summaries of settled gameplay (15m–24h presets, default 30m STANDARD). Distinct from immediate operational alerts, Admin Live, WATCH, and World Reports. Observational only.

### Added

- **World Services:** `docs/WORLD-SERVICES.md` — six first-world institutional interfaces (Exchange Broker, Quartermaster, Registrar, Relay Keeper, Archivist, Contract Clerk). Not Players. Closed capabilities. Writes only through Player-confirmed canonical actions. LLM/presentation has no authority.

### Added

- **First-world operational envelope:** Admin Live, world operations, Player lifecycle, operator interventions, incident recovery, Player onboarding, and Perihelion Reach pin. Specs: `docs/ADMIN-LIVE-OPERATIONS.md`, `docs/WORLD-OPERATIONS.md`, `docs/PLAYER-LIFECYCLE.md`, `docs/OPERATOR-INTERVENTIONS.md`, `docs/INCIDENT-RECOVERY.md`, `docs/PLAYER-ONBOARDING.md`, `docs/FIRST-WORLD-OPERATIONS.md`. Maps operational language onto frozen `World.status` (`ACTIVE` / `PAUSED` / `INCIDENT` / `ARCHIVED`); does not add gameplay, profiles, or seeds.
- Admin Live observes the authoritative system and does not play; private cognition stays out of scope; private message text is hidden by default.
- First-world settlement outage is bounded fail-closed (at most one additional mutating cycle batch). One controlling PlayerSession per Player; transport disconnect does not emit `AGENT_LEFT_WORLD`.
- Operator interventions classified `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY`; raw Admin world edits prohibited.
- Incident failure matrix, settlement `HEALTHY`/`DEGRADED`/`BLOCKING`, research-failure isolation from PLAY, and explicit restore sequence.
- `docs/COMMAND-DISCOVERY.md` for first-world HELP / AVAILABLE HERE / agent capability discovery.
- **First-world spec freeze:** `docs/FIRST-WORLD-SPEC-FREEZE.md`. ASK = MESSAGE convenience; QUERY optional/deferred read-only; TRADE propose/accept compute 1, reject/cancel 0, reservation release exact; public HARVEST WATCH wording settled. Additive `harvest` spectator projection id.

### Added

- **Auth, identity, and Agent Gateway architecture:** canonical Account → Player → Controller → Credential + PlayerSession model; humans and agents are both Players; managed human auth (Supabase Auth direction); agent device enrollment; scoped capabilities; Noema Agent Gateway (REST / WebSocket / MCP); framework adapters (Hermes, OpenClaw, Grok Bot, …) outside Core; action provenance; auth threat model; MVP identity boundary. Specs: `docs/AUTH-AND-IDENTITY.md`, `docs/AGENT-GATEWAY.md`. Updates: ARCHITECTURE, DATA-MODEL, SECURITY, SECURITY-SEQUENCES, AGENT-INTERFACE, AGENT-ONBOARDING, HUMAN-PLAY, AGENT-PLAY, TERMINOLOGY, EXPERIENCE-TERMINOLOGY, AMBITIONS, ROADMAP, agent-protocol-v1, id-rules, validate_all required docs.
- **Pinned hosted product stack:** Supabase Auth + Supabase Postgres (+ optional Storage) · Noema always-on compute · external agents → WS/REST · marketing GitHub Pages. Env: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_JWT_SECRET`; `DATABASE_URL` → Supabase Postgres.
- **Platform revision (Cloudflare + Supabase):** `docs/PLATFORM.md` — Durable Objects own live world; Workers are Agent Gateway; Supabase owns Auth/Postgres/Storage; settlement model; free-tier-first; PlayerPrincipal; non-goals (no K8s/Redis/Kafka). Updates ARCHITECTURE, DEPLOYMENT, AUTH-AND-IDENTITY, AGENT-GATEWAY, ENGINEERING, ROADMAP, SECURITY, ENVIRONMENT, DATA-MODEL, CONTEXT, README, QUICKSTART, SPEC-CHECKLIST.

### Added

- **Core-loop spec freeze & implementation readiness audit:** `docs/SPEC-FREEZE-CORE-LOOP.md` freezes v0.1–v0.7 for runtime implementation priority (Chamber first; no v0.8 yet).
- **v0.7 Minimal LEARN / Capability Graph:** `docs/releases/v0.7/*`, behavior-node + capability-edge (+ disposable graph projection) schemas, LEARN surface, fixtures from v0.5 shared-ledger evidence, **K01–K12**, contested/not-tested distinctions, no graph DB or ranking.
- **v0.6 Deep Time foundation:** `docs/releases/v0.6/*`, institutions/succession/historical-artifact/claim/reconstruction/semantic-lineage/name/scar/evidence schemas, decay + significance catalogs, multi-era fixtures `examples/v06-deep-time/`, conformance **D01–D30**, lore-boundary and hidden-history gates. Lore is derived presentation only — not a second source of truth.
- **v0.6 admin-only Genesis (simplified):** profile + story-seed + genesis-result contracts, 3 profiles, closed story seeds, Cycle 0 fixtures with same/different seed determinism, **G01–G09**, no player Genesis surface and no Genesis runtime service.
- **v0.5 Phenomenon Compiler executable package:** `docs/releases/v0.5/*`, capture-intent/compilation-request/phenomenon-candidate/dependency-graph/unit-manifest/minimization-record/behavioral-oracle/compiler-result/compile-receipt/compiler-audit/captured-test/regression schemas, capture defaults + status/reason catalogs, STUDY CAPTURE progressive disclosure, fixtures `examples/v05-compiler/`, conformance **P01–P30** (90 cases).
- Docs: CAPTURE-INTENT-COMPILATION, COMPILATION-IDENTITY, BEHAVIORAL-ORACLE, BEHAVIORAL-SIGNATURE, OVER-MINIMIZATION, CAPTURED-TEST-FORMAT, BEHAVIORAL-REGRESSION.
- Validator Compiler gate: schema fixtures, digest/audit chains, simple/advanced identity equivalence, budget/privacy/over-minimization negatives, RFC-0003 receipt reuse.
- **Specification workflows:** root `SKILLS.md` provides deterministic, non-authoritative procedures for orientation, spec/RFC/milestone work, schemas, fixtures, conformance, determinism, drift, experience, game/research contracts, migration/versioning, validation, continuation, review, prompts, and runtime handoff.
- **v0.4 Lab executable package:** `docs/releases/v0.4/*`, experiment/intervention/plan/run/fork/lab-result/audit schemas, perturbation + ablation catalogs, variable registry, full Lab docs (identity, lifecycle, design, controls, fork, counterfactual, outcomes, replication, isolation, audit, lesions, determinism), fixtures `examples/v04-lab/`, conformance **L01–L16**.
- Validator Lab gate: schema fixtures, production isolation negatives, null results retained.
- **Experience-integrated Lab contracts:** versioned `ExperimentIntent`, deterministic intent compilation rules, intent provenance on experiments/results, simple-result projection schema, CAPTURE readiness gate, stable plain-language reason codes, and L23–L34 conformance coverage.
- **RFC-0003 Accepted and implemented** — deterministic contract hardening for independent implementations.
- Catalog-specific ledger-admission schemas for `event-catalog/0.1` and `event-catalog/0.2`, with positive and negative fixtures.
- Machine validation gate for canonical action ordering, delivery visibility, exact quantities, typed action IDs, state lineage, writer fencing, recovery, and signed evidence profiles.

### Changed

- ROADMAP/README/VERSIONING/SPEC-CHECKLIST/EXPERIMENT-LAB for executable Lab scope.
- Expanded v0.4 Lab into a machine-checkable experimental contract: immutable identity, isolated forks, explicit intervention/control/replication rules, audit chain, catalogs, fixtures, and L01–L22 conformance.
- Added the PLAY / WATCH / STUDY experience layer, progressive disclosure contracts, deterministic experiment-intent templates, error translations, and audience fixtures.
- Canonical same-cycle order is `(action_priority, agent_id, client_action_sequence, action_id)`; network arrival order is noncanonical.
- `MESSAGE_DELIVERED` commits before post-cycle observation projection.
- Replay canonicalization is pinned to `noema-jcs/1` (RFC 8785 JCS over I-JSON with integer fixed-point quantities).
- Canonical WorldState now requires version/catalog lineage, state revision, canonicalization/hash pins, and ledger-head digest.
- Reference persistence now requires one fenced writer and atomic `SERIALIZABLE` cycle commits with crash reconciliation.
- Agent Protocol resume uses scoped cumulative acknowledgements and bounded deterministic redelivery.
- Signed receipts are mandatory for research-isolated and public evidence export profiles.

### Added

- **RFC-0002 Accepted** — strategic conflict executable contracts (`event-catalog/0.2`).
- `specs/event-types.0.2.json` (31 types), `contest-config.v02.json` + schema, `action-contracts.v02.json`.
- Docs: CONTEST-RESOLUTION, STRATEGIC-EVENT-COUPLING, strategic conflict acceptance/conformance/migration.
- Fixtures: `examples/v02-strategic-conflict/` (trajectory, resolution, spectator, report, Observatory features, negatives).
- Conformance: `conformance/v0.2-strategic/` families **S01–S18**.
- Validator gate for catalog isolation, resolution arithmetic, S-suite.

### Changed

- EVENT-CATALOG documents 0.1 vs 0.2; ACTION-CONTRACTS, SPECTATOR, DIPLOMACY, BEHAVIOR-FEATURES, VERSIONING, SPEC-CHECKLIST, README.

### Added

- RFC-0002 expanded to full Draft: payload sketches, reducer preconditions, coupling, observability, worked sequence for seven contestation/crime/agreement events.
- `examples/chamber-world/start-distributions.json` — ENTER_WORLD assignment profiles.
- Chamber seed route pressure: `traversal_cost` on edge/vault routes, edge condition tags; richer `map_design` (starts, chokepoints, scarcity).

### Changed

- SPEC-CHECKLIST / README / EVENT-CATALOG-AUDIT / STRATEGIC-CONFLICT / rfcs index for RFC-0002 payload-draft status and chamber-world depth.

### Added

- `examples/chamber-world/` — canonical 10-room Chamber starting map + `world-seed.json`.
- `rfcs/RFC-0002-strategic-contestation-and-crime-events.md` (Draft skeleton).
- GAME-DESIGN completed spine table linking all player-facing game docs.

### Changed

- CHAMBER-MAP / STARTING-CONDITIONS point at chamber-world product map (v01-seed remains ADR-005 fixture).

### Added

- `docs/STARTING-CONDITIONS.md`, `docs/GAME-SYSTEM-DEPENDENCY.md`.
- Expanded EXPLORATION, STRATEGIC-KNOWLEDGE, INFRASTRUCTURE, SPECTATOR (primary surfaces + high-drama events).
- EVENT-CATALOG-AUDIT: `AGREEMENT_FORMED` / `AGREEMENT_BROKEN` as v0.2 RFC candidates.

### Changed

- GAME-SYSTEM-MAP cross-links and indexes for completed core game design.

### Added

- **Core game design completion package:** LOSS-RECOVERY, DIPLOMACY, GAME-CYCLE, WORLD-REPORTS, PROGRESSION, AMBITIONS, HUMAN-PLAY, AGENT-PLAY, GAME-BALANCE, EXPLORATION, STRATEGIC-KNOWLEDGE, INFRASTRUCTURE (progression), FIRST-20-CYCLES, CHAMBER-MAP, GAME-SYSTEM-MAP, EVENT-CATALOG-AUDIT.
- Expanded STRATEGIC-CONFLICT with full crime + contestation forms, defense, RFC event list.

### Changed

- GAME-DESIGN contracts map, TERMINOLOGY, ROADMAP, README, SPEC-CHECKLIST for full player-facing design index.

### Added

- **Core game design foundation:** `docs/CORE-GAME-LOOP.md`, `docs/REALMS.md`, `docs/GEOGRAPHY.md`, `docs/TERRITORY-CONTROL.md`, `docs/STRATEGIC-CONFLICT.md` (crime consequence layer; strategic P2P contestation as next milestone; no closed-catalog event expansion without RFC).

### Changed

- Linked GAME-DESIGN, TERMINOLOGY, SPECTATOR, ROADMAP, README to core game design docs.

### Added

- **v0.3 Observatory executable package:** `docs/releases/v0.3/*`, trajectory/0.3, behavior features, context normalization, baselines, anomaly/shift/capability/unknown candidates, agent-version comparison, external cognition & coordination signals, analysis-run + audit schemas, `examples/v03-observatory/`, conformance **O01–O16** (96 cases).
- Docs: TRAJECTORY, BEHAVIOR-FEATURES, CONTEXT-NORMALIZATION, BASELINES, ANOMALY-DETECTION, BEHAVIOR-SHIFT, AGENT-VERSION-COMPARISON, CAPABILITY-CANDIDATES, CONTRADICTION-ANALYSIS, EXTERNAL-COGNITION, COORDINATION-SIGNALS, EMERGENCE-CANDIDATES, OBSERVATORY-AUDIT; expanded OBSERVATORY.md.

### Changed

- Roadmap/README/VERSIONING/MODULE-CONTRACTS/SPECTATOR/TESTING for Observatory executable scope.

### Added

- **v0.2 Frontier executable package:** `docs/releases/v0.2/*`, Situation Genome 0.2, novelty axes, mutation catalog, noise/attention/info-gain configs, capability primitives, Frontier request/plan/candidate/audit/replay schemas.
- Docs: SITUATION-GENOME, NOVELTY-VECTOR, CAPABILITY-PRIMITIVES, SITUATION-MUTATION, PARTIAL-OBSERVABILITY, NOISE-MODEL, CONTRADICTORY-EVIDENCE, ATTENTION-PROJECTION, INFORMATION-GAIN, FRONTIER-CONTROLS.
- Fixtures: `examples/v02-frontier/` end-to-end deterministic Frontier scenario.
- Conformance: `conformance/v0.2/` families **F01–F15** (76 atomic cases).
- Hardened `FRONTIER-DIRECTOR.md` cross-links to versioned configs; spectator Frontier projections; migration/version domains.

### Changed

- Roadmap/README/VERSIONING/MODULE-CONTRACTS/SPECTATOR updated for v0.2 Frontier executable scope.
- Conformance-case schema: acceptance_items max 200; family_id; frontier-director actor.

### Added (prior)

- Executable world/game contracts: `docs/MODULE-CONTRACTS.md`, `docs/RESOURCE-ECONOMY.md`, `docs/ACTION-CONTRACTS.md`, `docs/SCHEDULER.md`, `docs/SPECTATOR.md`.
- Machine-readable: `module-contracts.v01.json`, `resource-economy.v01.json`, `action-contracts.v01.json`, `id-rules.v01.json`, spectator-projection + module-contracts schemas.
- Strategic fixture package `examples/v01-strategic/` (4-agent coupled scenario).
- Conformance families **C18–C26** (resource, production, trade, org, infrastructure, scheduler, director, spectator, strategic persistence).
- Onboarding/deployment golden path docs: `docs/QUICKSTART.md`, `docs/OPERATIONS.md`, `docs/SPECTATOR-ONBOARDING.md`.
- Schemas: `runtime-manifest.schema.json`, `deployment-config.schema.json`.
- Fixtures: `examples/onboarding/`, `examples/deployment/`.
- Conformance families **C11–C17** (human/agent/spectator onboarding, reference deployment, restart persistence, backup/restore, version pinning).
- v0.1 Chamber **conformance suite** (`conformance/v0.1/`, docs/v0.1-CONFORMANCE.md) covering acceptance items C01–C17 (C01–C10 retained).
- Schemas: `world-state`, `world-seed`, `world-snapshot`, `equivalence-boundary`, `agent-protocol-message`, `conformance-case`.
- Protocol wire fixtures (`examples/protocol/`) and observation positives (`examples/observations/`).
- Genesis snapshot example for seed load (`examples/v01-seed/genesis-snapshot.json`).
- Expanded `protocols/agent-protocol-v1.md` with ACT→event mapping, error codes, resume, sandbox, and private cognition rules.
- Canonical NOEMA persistent MUD multi-agent specification baseline.
- Exact required protocol documents for MUD commands, agent protocol, event ledger, and replay.
- Ten requested Draft 2020-12 JSON Schema files and matching examples.
- Lowercase research ontology, controls, claims, and ethics files.
- RFC README and template for contract-changing decisions.
- `validation/` merge-gate suite (structure, JSON parse, link check, claim-label scan).
- `adr/` directory with five foundational ADRs (determinism, private cognition, claim labels, world-truth isolation, v0.1 equivalence boundary).
- `docs/SECURITY-SEQUENCES.md` — concrete containment, quarantine, revocation, incident, kill-switch, and undelivered-observation sequences.
- `docs/v0.1-ACCEPTANCE.md` — operational acceptance criteria and minimum conformance tests for The Chamber.
- `docs/CONTRACT-CARDS.md` — progressive-disclosure summaries of major contracts.
- `docs/INTEGRATION-SURFACE.md` — explicit extension points for Zero State / Abraxas ecosystem consumers.
- `research/phenomena-operational-definitions.md` — operational definitions, required data, confounds, and limits for the five high-signal constructs.
- `examples/negative/` — invalid fixtures for schema, catalog, and semantic rejection testing.
- `examples/v01-seed/` — concrete Chamber seed: world genesis, full 24-type trajectory, equivalence boundary, and expected digests.
- `.github/workflows/spec-validation.yml` — CI validation gate.

### Changed

- Expanded `docs/GAME-DESIGN.md`, `docs/DATA-MODEL.md`, `docs/WORLD-MODEL.md`, `docs/ENGINEERING.md` for Chamber strategic ecology and executable transitions.
- Extended acceptance/conformance/testing/roadmap to C01–C26; world-state schema optional infrastructure/resource_nodes fields.
- Clarified verb scope: v0.1 REQUIRED vs OPTIONAL vs LATER (GAME-DESIGN, ACTION-CONTRACTS, mud-command).
- Rewrote `docs/AGENT-ONBOARDING.md` for minimal HELLO→ACT path; advanced/research registration is secondary.
- Rewrote `docs/DEPLOYMENT.md` with normative modular-monolith reference architecture and explicit non-requirements.
- Reorganized `docs/ENVIRONMENT.md` and `.env.example` into Core / Advanced / Research / Providers / Optional scaling; local boot without Redis/Sentry/OTEL/external object storage/provider keys.
- Extended `docs/v0.1-ACCEPTANCE.md`, `docs/ROADMAP.md`, `docs/TESTING.md`, `README.md` for PLAY/WATCH/CONNECT AGENT and ops surface.
- Relaxed `agent-manifest.schema.json` required fields to minimal identity + protocol (compatible with full advanced manifests).
- Reframed all core docs from an agent-centered research-apparatus baseline to the requested autonomous-agent research apparatus.
- Reinforced claim-label and consciousness-score policy through ADR-003 and operational definitions.
- Made v0.1 equivalence boundary explicit and mandatory via ADR-005.
- Strengthened `validation/validate_all.py` to enforce structure, env docs, seed catalog coverage, digest chain, and negative corpus rejection.

### Removed

- Thought-centric protocol, schema, and example artifacts that were inconsistent with NOEMA.

### Notes

- Spec checklist structure, contract quality, tree validation, and CI on `main` are green.
- Specs release candidate tagged `v0.1.0-rc1`.
- Independent World Engine Chamber replay is implemented in `Zero-State-LLC/Noema` and matches `examples/v01-seed/` digests (`EQUIVALENT`).
