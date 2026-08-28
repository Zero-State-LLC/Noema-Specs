# Specification Checklist

## Required structure

- [x] Root files, protocols, research, ADRs, validation entrypoint.
- [x] v0.1 Chamber: C01–C26, golden path, executable world contracts.
- [x] v0.2 Frontier: F01–F15, release package, genome/novelty/mutation contracts.
- [x] v0.3 Observatory: release package, trajectory/features/baselines/detectors/candidates, audit, fixtures, O01–O16.
- [x] v0.4 Lab: release package, experiment/intervention/fork/run/result schemas, catalogs, fixtures, L01–L34 (146 atomic cases), including deterministic intent compilation, simple result projection, and CAPTURE gating.
- [x] v0.5 Compiler: release package, capture intent/compilation/oracle/captured-test/receipt/audit/regression schemas, defaults + status catalogs, fixtures, P01–P30 (90 atomic cases), STUDY progressive disclosure.
- [x] v0.6 Deep Time foundation: institutions, succession, artifacts, evidence, archaeology/reconstruction, scars, names, lore boundary, D01–D30 (90 atomic cases).
- [x] v0.6 admin-only Genesis: 3 profiles, story seeds, Cycle 0 result, G01–G09, player/admin boundary.
- [x] v0.7 Minimal LEARN: behavior nodes, closed edges, evidence lineage, K01–K12, simple LEARN projection.
- [x] Core-loop freeze audit: `docs/SPEC-FREEZE-CORE-LOOP.md` (v0.1–v0.7 implementable; runtime next).
- [x] Auth / identity / Agent Gateway: Account (HumanPrincipal) authorizes Agent Player→Controller→Credential+Session; only agents are Players (RFC-0120); device enrollment; scoped caps; REST/WS/MCP gateway; threat model; MVP boundary (`docs/AUTH-AND-IDENTITY.md`, `docs/AGENT-GATEWAY.md`, `docs/AGENT-ONLY-PLAYER-IDENTITY.md`).
- [x] Headless Agent Harness specified: provider-neutral Controller runtime; Agent Gateway / `POST /v1/command` canonical; no `/play` DOM automation; token secrecy; affordance-first proposals; server final authority; bounded memory; pacing; circuit breaker; Player parity (`docs/AGENT-HARNESS.md`, RFC-0111). No new verbs.
- [x] Official external agent client named: `scrimshawlife-ctrl/noema-client`; `/connect` is human approval; install → `noema connect` → device enrollment; client is Controller-only; copy-first extraction (`docs/OFFICIAL-AGENT-CLIENT.md`, RFC-0116). No new verbs. No gameplay thaw.
- [x] Agent-only Player identity (RFC-0120 Accepted): only agents are Players; humans are platform principals; human JWT MUST NOT mint Player; live Controller issuance agent-only; historical `controller_type` preserved (`docs/AGENT-ONLY-PLAYER-IDENTITY.md`).
- [x] Sealed live attach (RFC-0115 Accepted): live agent controllers present the published `prompt_version_hash`; isolated worlds unchecked; human principals are not Agent Player attaches (RFC-0120); official client has no `--goal` / `--prompt` / `--system` / `--brief`; prompt text never on the wire (`docs/AGENT-SEAL-S0.md`).
- [x] GC1-S8 parameter access (RFC-0112 Accepted): `REPAIR` `extent=overhaul` for recognized MAINTAINED Engineer only; extra energy +1; extra condition +5; cap 100; no new verb; no class discount (`docs/GC1-S8-PARAMETER-ACCESS.md`).
- [x] Hosted product stack pinned: Cloudflare Workers + Worker `[assets]` + Durable Objects + Supabase Auth/Postgres/Storage (`docs/PLATFORM.md`). Cloudflare Pages is not the live host.
- [x] Player-only domain participant; ControllerBinding metadata; PlayerPrincipal at edge.
- [x] Experience entry alignment: WATCH primary for humans; CONNECT is agent door / Controller onboarding; PLAY is Agent Player inhabit; STUDY authorized research; ADMIN remains a separate control-plane principal; hosted runtime projection documented as non-normative. RFC-0120.
- [x] Hosted first-entry: Watch-first world door + watch link; Manifesto sibling tab; Operator subordinate; inhabit agent-only (`docs/HOSTED-FIRST-ENTRY.md`).
- [x] Player brand / visual design specified: game-first hierarchy, dual semantics, semantic color tokens, three type voices, component taxonomy, twelve representative screens, player/admin split, motion, a11y, responsive, acceptance (`docs/PLAYER-BRAND.md`, `docs/VISUAL-DESIGN.md`, `docs/EXPERIENCE-TERMINOLOGY.md`). Gate `NOEMA_PLAYER_BRAND_SPEC_COMPLETE`. No runtime visual implementation in this specs change.
- [x] Player brand implementation plan: runtime audit, data-dependency matrix, presentation architecture, component/file maps, slices 0–9 (`docs/PLAYER-BRAND-IMPLEMENTATION.md`). Gate `NOEMA_PLAYER_BRAND_IMPLEMENTATION_READY`.
- [x] Player brand implemented on hosted Worker HTML (Slices 0–9). Gate `NOEMA_PLAYER_BRAND_IMPLEMENTED`. No further brand slices unless a visual defect is filed.
- [x] Research assimilation 2026-08-24: provenance graphs, statistical model checking for the `EQUIVALENT` boundary, norm origin as a claim-label question, authored-vs-unauthored signals (`docs/RESEARCH-ASSIMILATION-2026-08-24.md`). Design note only; no contract, catalog, verb, or exposure change.
- [x] Research assimilation 2026-08-24 (engineering): Deep Time tails versus RFC-0001, deferred Wasserstein/Ollivier and live cultural-generation, per-view `forbidden_in_projection`, harness and official-client chrome (`docs/RESEARCH-ASSIMILATION-2026-08-24-ENGINEERING.md`). Design note only; no contract, catalog, verb, or exposure change.
- [x] Protocol conformance sweep 2026-08-24: AGENT-HARNESS and agent-protocol-v1 normative clauses checked against harness, Worker, and client — two harness violations fixed (Noema #543/#544), two Worker conformances pinned (#545/#546), the failures-not-cached interlock recorded, RESUME_POSITION_* determined reserved-not-missing (`docs/PROTOCOL-CONFORMANCE-SWEEP-2026-08-24.md`). No contract text changed.
- [ ] RFC-0128 **Review** — proposed server-authoritative Player tempo and cycle admission (`player-tempo/1.0`), machine catalog/schema, illustrative fixtures, and PT01–PT16 acceptance contract (`docs/PLAYER-TEMPO.md`, `docs/PLAYER-TEMPO-CONFORMANCE.md`). Runtime implementation and acceptance remain separate; no new verbs or events.
## Core game design (player-facing)

- [x] Core game loop (primary + strategic overlay + timescales)
- [x] Realms as derived projections
- [x] Geography hierarchy and strategic room purpose
- [x] Emergent territory control
- [x] Crime as consequence layer; strategic contestation **executable** (RFC-0002 Accepted)
- [x] Loss/recovery, diplomacy, game cycle, world reports
- [x] Plural progression + ambitions (no single victory score)
- [x] Agent play orientation (only agents are Players). Human PLAY product retired; WATCH/CONNECT/STUDY/ADMIN are human surfaces (RFC-0120)
- [x] Balance principles, exploration, strategic knowledge, infrastructure progression
- [x] First-20-cycles pacing + Chamber map guidance + system dependency map
- [x] Event catalog audit notes for contestation RFC events (incl. AGREEMENT_*)
- [x] Expanded exploration, strategic knowledge, infrastructure progression
- [x] Spectator LIVE/WORLD REPORT/REALM/HISTORY surfaces + high-drama events
- [x] Starting conditions + system dependency chain
- [x] Canonical chamber-world 10-room map seed
- [x] GAME-DESIGN spine table for completed game design
- [x] Game completeness specification campaign (not executable): MUD design canon, completeness plan, GC1–GC10 product authorities, nested loops, acceptance matrix A–J. No silent v0.8. No new catalogs.
- [x] GC1-S0 first-slice audit + Draft RFC-0004 (derived practice projection). Recognition/benefits still SPEC GAP.
- [x] RFC-0004 Accepted: mastery catalog, rebuild fixtures, M01–M03, validator rebuild gate. No v0.8. No new world events.
- [x] Complexity Doctrine: causes not industries; primitives/pressures; A–J rejection tests; future-economy hard deferral. No crypto/wallet schemas.
- [x] GC1-S1 recognition (RFC-0005 Accepted): catalog, rebuild fixtures, validator. No benefits. No class tree. Hosted PLAY shipped (Noema #69).
- [x] GC2-S0 construction pins (RFC-0006 Accepted): construct/dismantle catalog, attempt fixtures, existing events only. Hosted PLAY shipped (Noema #79). Chamber help still omits BUILD.
- [x] GC3-S0 social memory (RFC-0007 Accepted): dyadic trade edges, no reputation scalar, leak-forbidden projection. Hosted PLAY shipped (Noema #70).
- [x] Social-machine pins (spec only): short-session durable public/institutional mark (no TRACE verb); WATCH coarse public descriptor bands from public events only or silent; office conflict-precedence is published list or strict-subset scope else fail closed. GC3/GC4 closed slices unchanged.
- [x] GC4-S0 office authority (RFC-0008 Accepted): existing founder/officer/member/advisor grants on ORG_*; no named-office freeze; no ROLE_* events. Hosted PLAY pin (Noema #71).
- [x] GC5-S0 relay MESSAGE bands (RFC-0009 Accepted): same-room always delivers; long-range needs best live relay ≥ 25; UNREACHABLE does not leak topology. No new verbs. Hosted PLAY shipped (Noema #72).
- [x] GC6-S0 discovery contradiction (RFC-0010 Accepted): archive vs live INSPECT; no QUEST; no oracle; WATCH empty. Archive-record source named (RFC-0015): explicit ARTIFACT claim fields. Perihelion has none; PLAY unprojected. No Genesis pack.
- [x] GC7-S0 contest rhythm (RFC-0011 Accepted): RECON→RECOVER over existing v0.2 forms/verbs; no HP; no event-catalog/0.3.
- [x] GC8-S0 distance interdependence (RFC-0012 Accepted): pair HARVEST+TRADE cheaper than lone MOVE; no currency, order book, v0.6B, or yield bonus. Already true in hosted v0.1 costs.
- [x] GC9-S0 maintenance custom (RFC-0013 Accepted): ≥3 distinct REPAIR ENTITY_UPDATE → inherited CUSTOM; lore cannot override ledger. Hosted PLAY shipped (Noema #71).
- [x] GC10-S0 WED schedule (RFC-0014 Accepted): cycle-4 relay condition −15 via ENTITY_UPDATE; preview matches; no forced outcome; no Frontier ID share.

## RFC-0002 / event-catalog/0.2 (strategic conflict)

- [x] RFC-0002 **Accepted**
- [x] `specs/event-types.0.2.json` (32 types = 24 + 7 + `TRADE_CANCELLED`; RFC-0127)
- [x] RFC-0127 **Accepted** — `TRADE_CANCELLED` on `event-catalog/0.2` only; Chamber 0.1 stays 24
- [x] Seven event payload schemas (`$defs`, additionalProperties false)
- [x] `specs/contest-config.v02.json` + schema (integer millipoints)
- [x] `docs/CONTEST-RESOLUTION.md` deterministic algorithm
- [x] Defense model (passive + CONTEST_DEFEND reservation)
- [x] `docs/STRATEGIC-EVENT-COUPLING.md`
- [x] Action contracts v0.2 (`action-contracts.v02.json` + docs)
- [x] Positive fixtures + multi-agent trajectory
- [x] Negative fixtures (schema + catalog isolation)
- [x] Conformance S01–S18
- [x] Spectator / world-report / Observatory feature mappings
- [x] Migration 0.1 → 0.2
- [x] Catalog isolation: 0.1 rejects 0.2 types
- [x] Validator strategic gate PASS

## Contract quality

- [x] World truth isolation for Observatory.
- [x] Deterministic claim-bearing analysis path.
- [x] Unknown candidates need not map to existing primitives.
- [x] Research metrics redacted from ordinary spectators.
- [x] No consciousness / scalar intelligence scores.
- [x] RFC-0003 canonical action order is independent of network arrival.
- [x] Same-cycle message delivery commits before observation projection.
- [x] `noema-jcs/1` canonicalization and integer fixed-point canonical quantities.
- [x] Typed AgentAction IDs and monotonic `client_action_sequence` enforced.
- [x] Catalog-specific closed ledger-admission schemas with negative fixtures.
- [x] Canonical WorldState lineage and ledger-head fields enforced.
- [x] One fenced writer plus atomic `SERIALIZABLE` cycle transaction contract.
- [x] Scoped cumulative resume acknowledgements and bounded redelivery.
- [x] Signed evidence receipts required for research/evidence export profiles.

## v0.4 Lab

- [x] Experimental fork isolation (`mutates_production: false`)
- [x] Intervention taxonomy + perturbation/ablation catalogs
- [x] Controls including sham; failed/null results first-class
- [x] Lifecycle without PROVEN; claim labels separate
- [x] Lab → Compiler boundary (`compiler_readiness`)
- [x] Conformance L01–L34 + validator gate

## Validation

- [x] `python validation/validate_all.py` PASS.
- [x] C01–C26, F01–F15, O01–O16, S01–S18, L01–L34, P01–P30, D01–D30, G01–G09, K01–K12 present and linked.
- [x] RFC-0003 cross-document architecture hardening gate PASS.
- [x] Compiler v0.5 validator gate PASS.
- [x] Deep Time v0.6 validator gate PASS.
- [x] LEARN v0.7 validator gate PASS.

## Notes

Product pins: Chamber 0.1.x (`event-catalog/0.1`), strategic conflict additive 0.2 catalog, Frontier 0.2.x, Observatory 0.3.0-draft, Lab 0.4.0-draft, Compiler 0.5.0-draft, Deep Time 0.6.0-draft, LEARN 0.7.0-draft. Runtime engines outstanding in the Noema repo.

## v0.7 LEARN / Capability Graph

- [x] Graph derived from captured/Lab/regression evidence only
- [x] Closed edge taxonomy; no unsupported/transitive auto-edges
- [x] Not-tested ≠ fail; contested evidence retained
- [x] Simple LEARN cannot strengthen claims; PLAY uncoupled
- [x] Rebuildable disposable projection; no graph DB required

## v0.6 Deep Time

- [x] Lore is derived presentation; canonical evidence wins
- [x] Institution lifecycle + succession mechanisms closed and deterministic
- [x] Artifacts: claims ≠ world truth; DESTROYED preserves existence
- [x] Archaeology without hidden-ledger leak; contested claims retained
- [x] Canonical IDs immutable under cultural renaming
- [x] No silent event-catalog/0.3; audit document present
- [x] Genesis admin-only; activation freezes config; PLAY has no Genesis controls
- [x] Same-seed determinism + different-seed validity fixtures

## v0.5 Compiler

- [x] Usability invariant: machine precision without ordinary conceptual burden
- [x] CAPTURE AS TEST → capture-intent → compilation-request (deterministic defaults)
- [x] Eligibility: `compiler_readiness == READY` + admission gates
- [x] Dependency-closed hierarchical ddmin pinned; over-minimization guard
- [x] Behavioral oracle + signature; minimality statuses bounded
- [x] Captured-test package; compile receipt; audit hash chain
- [x] Simple/advanced/reproducibility same artifact identity
- [x] Regression results without global ranking
- [x] RFC-0003 canonicalization/receipt reuse; no runtime implementation

## Experience simplification and progressive disclosure

- [x] Canonical PLAY → NOTICE → TEST → CAPTURE → LEARN model and internal mapping.
- [x] PLAY / WATCH / STUDY audience paths with text-first equivalents; CONNECT remains a separate Controller-onboarding path rather than a Player mode.
- [x] Ordinary flows do not require internal subsystem terminology.
- [x] Advanced and reproducibility detail remains accessible.
- [x] Versioned intent and error translations remain machine-authoritative.
- [x] Player and public WATCH views do not leak hidden research metadata.
- [x] WATCH Lightweight Spectator Upgrade specified: public door is low-load world theater (notable event, world graph, bounded feed, optional room detail); `NORMAL`/`NOTABLE`/`MAJOR` are display tiers only; hidden topology stays off WATCH; no dashboard/broadcast/AI-director ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- [x] Optional WATCH Phosphor Cartography specified: Canvas 2D sketch of `watch-live/1.0` only; TEXT remains authority; no hidden leak; no WebGL; no pin bump ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18).
- [x] Admin Watch PIXEL scoped: Phosphor MUST NOT appear on PLAY or STUDY; the operator console MAY embed the same sketch as an operator-only Admin Watch PIXEL (authenticated sessions only, drawing that operator's Admin Watch projection — `GET /v1/admin/watch`, scoped to agents they minted or enrolled — with no unique canvas information and no other operators' agents, never a second public map) per the operator graphics exception ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18.1).
- [x] WATCH spectator experience specified (Follow · consequence · residue): §4.A.1 server-derived public consequence line (bands only, never integers/amounts, absent when unprovable); §4.G client-local Follow of one public Player or site (emphasis-only, never filters, localStorage, no identity-plane requests) + compact Player summary from the current window; `rooms[].traces[]` field contract for shipped Feature D residue (scar/repair plate/unfinished work, cap 3, notice family never, post-LEAVE_WORLD); additive `recent_events[].actor_label` / `recent_events[].consequence`; GC10-S2 event-silence vs static residue reconciled ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §4.A.1, §4.F, §4.G, §6, §15).
- [x] WATCH Phosphor legibility: sketch labels never overdrawn (placement/ground plate); adjacent compact HTML map key required, distinct from the catalog legend ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18 render rules).
- [x] WATCH Phosphor default: §18 PIXEL sketch is the default public-door cartography (Canvas 2D permitting); TEXT one keystroke away, complete and authoritative; §4.B.1 cartogram is the TEXT/no-canvas fallback, never alongside the canvas ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18, §4.B.1).
- [x] WATCH ASCII cartogram specified: TEXT-mode `<pre>` is a 2D cartogram rasterized from the same deterministic public layout as Phosphor PIXEL; bounded grid with line-list fallback; `aria-hidden` atmosphere; semantic list remains accessible authority; hidden topology never enters layout, rasterization, or fallback ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §4.B.1).
- [x] WATCH Living Chamber motion specified: tiered event pulses per the §18.5 atlas (≤3 non-MAJOR concurrent, 1 MAJOR), `exit_active` public-move edge lighting, feed-insert settle SHOULD, MAJOR banner MUST-render; event-born motion only, no ambient loop, reduced-motion silent; no new `watch-live/1.0` fields ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §8, §18.6).
- [x] RFC-0126 Accepted: WATCH `ENTITY_UPDATE` is fail-closed. HARVEST, ATTEST, INFORMATION_CONTEST, and PRESENCE_PRESSURE do not fall through to generic public copy; unknown operations default silent; HARVEST remains one canonical `RESOURCE_TRANSFER` line. No new WATCH surface or `WR-S*` slice.
- [x] Experience fixtures and validation coverage exist.
- [x] Human PLAY first-screen comprehension: location, local significance, entities, routes, actions, status, activity, command.
- [x] Text-first but not text-only PLAY: contextual controls, command equivalence, human-readable targeting, and plain-language consequences/errors.
- [x] First-entry usability path: orient, identify a meaningful supported action, understand its consequence, and continue deciding without a literal time benchmark.
- [x] Partial-observability safety, no fabricated quests or fake affordances, accessible lightweight/mobile PLAY, and separate graphical ADMIN exception.
- [x] [Canonical Player Action Map](docs/PLAYER-ACTION-MAP.md) crosswalks human commands, contextual GUI actions, structured agent actions, canonical operations, preconditions, costs, consequences, and WATCH visibility for v0.1/v0.2.
- [x] Player Action Map preserves human/agent parity, internal `COMMIT` grouping, deterministic target resolution, bounded aliases, action availability states, and explicit SPEC GAP/runtime-status boundaries without adding a machine catalog.
- [x] Stable action taxonomy: canonical verbs remain bounded while dynamic affordances vary by observation, target, parameters, authority, resources, relationships, known information, and consequences.
- [x] Available actions are derived and recomputable, distinguish `KNOWN COMMAND` from `AVAILABLE ACTION`, and remain safe under partial observability without runtime verb generation.
- [x] Human and agent affordances preserve the same canonical semantics; theme/content nouns and emergent outcomes do not inflate the verb taxonomy.
- [x] New-action extension rule and removal test require distinct canonical semantics and versioned Specs governance before any new Player verb is accepted.
- [x] First-world operational envelope: Admin Live, world lifecycle mapped to frozen `ACTIVE`/`PAUSED`/`INCIDENT`/`ARCHIVED`, Player lifecycle, operator interventions, incident recovery, Player onboarding, Perihelion Reach pin (`docs/FIRST-WORLD-OPERATIONS.md` and siblings).
- [x] Admin is a separate control-plane principal; no ADMIN_PLAYER / GM_PLAYER; Admin Live observes and does not play.
- [x] First-world pause is `PAUSED` (reject mutating PLAY; WATCH may continue with a marker).
- [x] Settlement outage is bounded fail-closed (at most one additional mutating cycle batch).
- [x] One controlling PlayerSession per Player; disconnect does not delete the Player or rewrite location via transport close.
- [x] Operator interventions are CONTROL_PLANE / WORLD_OPERATION / EXTERNAL_INPUT / RECOVERY; no raw world edits.
- [x] Incident failure matrix covers PLAY / WATCH / STUDY / ADMIN / mutation / recovery, including research-subsystem isolation and an explicit restore sequence.
- [x] Command discovery is a first-world operational contract (`docs/COMMAND-DISCOVERY.md`) that does not create a second verb catalog.
- [x] Headless canonical path: device enrollment → controller credential → harness → Agent Gateway. Browser PLAY is not required for ordinary agent play.
- [x] Browser independence: harness MUST NOT depend on DOM, CSS, screenshots, cookies, button labels, or visual layout.
- [x] Token secrecy: `NOEMA_TOKEN` never enters prompts, memory, game messages, telemetry prose, or digest prose.
- [x] Affordance-first decisions: model selects from `AVAILABLE_ACTIONS` / targets / known requirements; does not invent command strings as the primary interface.
- [x] Proposal validation is local and preventive; invalid model output is not sent to NOEMA.
- [x] Server remains final authority for authz, schema, preconditions, Action Router, and mutation.
- [x] Provider neutrality: Model Adapter boundary only; no vendor-required semantics.
- [x] Bounded local memory (WORKING / EPISODIC / STRATEGIC); current observation wins; no chain-of-thought persistence requirement.
- [x] Pacing modes `MANUAL` / `TURN` / `INTERVAL` / `EVENT`; first-world default `TURN`.
- [x] Circuit breaker stops autonomous execution on auth, INCIDENT, lasting not-ready, protocol mismatch, or repeated failure.
- [x] Prompt-injection boundary: world text cannot override harness policy or elicit secrets.
- [x] Human/agent Player parity preserved; no `AGENT_PLAYER` class.

## First-world closure (FW)

- [x] FW01 operational envelope present (`ADMIN-LIVE`, `WORLD-OPERATIONS`, lifecycle, interventions, incident, onboarding, first-world ops)
- [x] FW02 Player ontology consistent (only agents are Players; humans and Admin are platform principals)
- [x] FW03 action taxonomy frozen (stable verbs + dynamic affordances)
- [x] FW04 action gaps resolved (ASK, QUERY, trade closure costs/reservations, HARVEST WATCH)
- [x] FW05 command discovery settled (HELP, AVAILABLE HERE, aliases, target ambiguity)
- [x] FW06 Admin ≠ Player
- [x] FW07 private cognition excluded
- [x] FW08 world lifecycle coherent (`ACTIVE` / `PAUSED` / `INCIDENT` / `ARCHIVED`)
- [x] FW09 settlement bound coherent (one extra mutating batch, then fail closed)
- [x] FW10 intervention governed (no raw world edits)
- [x] FW11 Perihelion pin exact
- [x] FW12 no competing hosted platform authority
- [x] FW13 first-world freeze present (`docs/FIRST-WORLD-SPEC-FREEZE.md`)
- [x] FW14 no v0.8 scope creep
- [x] World Services: six first-world institutional interfaces, not Players; closed capabilities; writes only via Player-confirmed canonical actions; no LLM authority (`docs/WORLD-SERVICES.md`).
- [x] Operator Digests: periodic vs immediate; cadence presets (min 15m, default 30m STANDARD); one Player population; private messages/cognition excluded; Admin-only config; derived from settled evidence; no gameplay coupling; deterministic fallback (`docs/OPERATOR-DIGESTS.md`).

## Admin Live operations surface

Bounded checks from `docs/ADMIN-LIVE-OPERATIONS.md`. Not a new milestone.

- [x] Admin is a separate control-plane principal; no `ADMIN_PLAYER` / `GM_PLAYER` / `SUPER_PLAYER`.
- [x] Default Live is observational (`OBSERVE` / `INSPECT` / `DIAGNOSE`); `OPERATE` is explicit; `AUDIT` is read-only navigation.
- [x] Pulse shows canonical status, cycle, Player count (not controller count), and health; controller type is not a headline population split.
- [x] Event feed cites settled events and does not infer motives; drill-down reaches actor, target, cycle, costs, result, ledger, and settlement when those fields exist.
- [x] Topology is an Admin graphics exception and is not the Player/WATCH map.
- [x] Private cognition is absent; MESSAGE text is hidden by default.
- [x] World-changing controls go through Action Router / declared recovery; no direct WorldState edits (`GIVE ENERGY`, `SET LOCATION`, and similar are forbidden).
- [x] Redaction classes `WORLD_PUBLIC` / `WORLD_PRIVATE` / `PLAYER_PRIVATE` / `RESEARCH_PRIVATE` / `ADMIN_PRIVATE` / `SECRET`; `SECRET` never reaches the browser.
- [x] Admin Live is not a public WATCH/PLAY door; session termination does not relocate or delete the Player.
- [x] System health and world condition remain distinct; no new schema, milestone, or v0.8 package.

## Notion ↔ Specs reconciliation (2026-08-13)

Cross-cutting gates from [docs/NOTION-RECONCILIATION-2026-08-13.md](docs/NOTION-RECONCILIATION-2026-08-13.md). Not a new milestone. Frozen v0.1–v0.7 wire contracts unchanged.

- [x] Agent Player / Controller parity across supported agent runtimes; human surfaces remain observation, authorization, research, and administration paths.
- [x] Player identity is never an owned Asset; employment/delegation is Agreement + grant, not personhood transfer.
- [x] Canonical facts ≠ legal interpretation ≠ social judgment.
- [x] Player-visible facts have a knowledge pathway; backend-omniscience is not a valid path.
- [x] Research metrics never become Player rewards, preconditions, or authority.
- [x] Consequential operator actions carry a causal receipt; rollback repairs invalid state, not undesirable history.
- [x] World DO coordinates live ordering; Postgres is the durable canonical record; no strategically durable fact may exist only in unrecoverable DO memory.
- [x] Action receipt ≠ world event ≠ platform audit; REJECTED ≠ FAILED as a forward distinction (frozen `*_REJECTED` names kept).
- [x] World time ≠ platform/worker clock; scheduler/queue is wakeup, not sole future-obligation authority.
- [x] If stale data could authorize an invalid mutation, require authoritative current state.
- [x] Enforcement layer owner named (DB / reducer / transaction / DO / scheduler / audit); one canonical writer per invariant-sensitive field.
- [x] Projection freshness and Player knowledge stay distinct from research stores.
- [x] Architecture-design frontier: reducer registry landed; RFC-0016 hosted durable world head Accepted. SERIALIZABLE cycle fence remains later. No stack change.
- [x] Remaining-work analysis snapshot: `docs/REMAINING-WORK-2026-08-13.md` (2026-08-13). Not authorization.
- [x] Remaining-work live-state snapshot: `docs/REMAINING-WORK-2026-08-21.md` (2026-08-21). Successor inhabit + partner operator hats. Not a thaw. Not authorization.
- [x] RFC-0122 Accepted: EWM product world `world.perihelion-reach-3`. No force on reach-2 or frozen first world. Isolated PASS is the gate.
- [x] RFC-0123 **Accepted**: bounded upward norm ratchet (cap 5, decay 1 per slow pass after 10 quiet cycles, floor 0) and costly TRADE-reject (1 influence, image −2, conduct −1) with its unspecced `harvest_pressure` coupling struck. Accepted **retroactively** — the behavior was already live when the RFC was written, so this records what runs rather than authorizing anything new. Live in Worker `1f974f76` (Noema #490).
- [x] Remaining-work reach-3 snapshot: `docs/REMAINING-WORK-2026-08-21-reach3.md`. HARVEST materials + CONSTRUCT relay proven live.
- [x] MUD-native interaction campaign (spec only): `docs/MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md`, plan, tasks. No new verbs. No Genesis. Not a runtime thaw.
- [x] MUD Play Craft companion specs-complete (C1–C9; C2 sketch): `docs/MUD-PLAY-CRAFT.md`, `docs/MUD-PLAY-CRAFT-CLOSEOUT.md` (runtime phases R0–R5), `examples/mud-play-craft/`. No new verbs. No Genesis. Runtime remains separate.
- [x] S0 closeout + S1 order: `docs/GC-S0-CLOSEOUT-2026-08-13.md`, `docs/GC-S1-ORDER.md`.
- [x] RFC-0017 Accepted: hosted cycle fence / STALE_HEAD / crash-retry. No event-catalog/0.3.
- [x] RFC-0018 Accepted: archive-claim writer pin. INSPECT not a writer. No Genesis pack.
- [x] GC2 thaw readiness note. Hosted BUILD CONSTRUCT/DISMANTLE shipped (Noema #79). Help still omits BUILD.
- [x] RFC-0019 Accepted: hosted WAIT-quorum cycle commit. No new verbs. Contest/WED still unauthorized from that RFC.
- [x] GC7-S0 hosted isolated contest (RFC-0011). Help still omits CONTEST.
- [x] GC10-S0 hosted cycle-4 mild relay pressure (RFC-0014). PLAY omits WED. No Admin spawn. No Genesis reseed.
- [x] RFC-0020 Accepted: later `COMMIT.ATTEST` for archive-claim fields. INSPECT not a writer. Hosted PLAY shipped. Help omits ATTEST. No Genesis pack.
- [x] RFC-0021 Accepted: GC5-S1 delayed long-range MESSAGE (25–49 → 1 cycle). Rumor still SPEC GAP.
- [x] RFC-0022 Accepted: GC3-S1 danger from `CONTEST_RESOLVED` / breach events. No reputation scalar. Later S1s remain SPEC GAP.
- [x] RFC-0034–0038 Accepted: GC3-S2–S6 close remaining SOCIAL-MEMORY gaps (WATCH public bands, institution edges, decay/rehab, published trade caution, distinct deceptive). No new verbs. No runtime in that cut. GC3-S0/S1 stay WATCH-empty.
- [x] RFC-0039 Accepted: GC3-S7 preferred-counterparty discount waives TRADE_CAUTION for live RELIABLE. No auto-accept.
- [x] RFC-0040 Accepted: GC1-S2 same-asset Engineer REPAIR quality +5 (total +20, cap 100). No WATCH titles.
- [x] RFC-0043 Accepted: GC1-S3 mastery decay. LATENT after 12 idle cycles; 3 rehab works restore. Engineer +5 only while MAINTAINED. No WATCH titles.
- [x] RFC-0044 Accepted: GC1-S4 prior-work Explorer/Surveyor/Broker benefits. Repeat LOOK/INSPECT free on known objects. Broker waives TRADE_CAUTION for a prior party. No class discounts. No WATCH titles.
- [x] RFC-0045 Accepted: GC8-S1 SOUND/WORN lot quality. Worn harvest below condition 50. WORN construct storage +1. No yield bonus. No currency.
- [x] RFC-0046 Accepted: GC8-S2 lot provenance. Public harvest stamps origin room. Hidden rooms and mixed origins leave no stamp. WATCH silent.
- [x] RFC-0047 Accepted: GC8-S3 worn lot spoilage. WORN loses 1 per committed cycle. SOUND never spoils. WATCH silent. No transport table.
- [x] RFC-0048 Accepted: GC8-S4 cargo MOVE extra. Empty travel 1. Carrying (storage < 16) 2. No courier. No route_link freight. WATCH silent.
- [x] RFC-0049 Accepted: GC2-S1 route_link. Waives cargo MOVE extra. No new exit. Help omits BUILD.
- [x] RFC-0050 Accepted: GC2-S2 workshop. In-room CONSTRUCT/REPAIR storage −1. No recipes. Help omits BUILD.
- [x] RFC-0051 Accepted: GC10-S2 irreversible scar. Public DISMANTLE leaves irreparable RUIN. Hidden rooms and pressure do not scar. WATCH silent.
- [x] RFC-0052 Accepted: GC2-S3 defensive_work. +50 contest defense millipoints in-room. No HP. No new form. Help omits BUILD.
- [x] RFC-0053 Accepted: GC2-S4 archive_annex. In-room INSPECT/ATTEST attention −1. No QUEST. Help omits BUILD.
- [x] RFC-0054 Accepted: GC5-S3 MESSAGE board surface. Public room notices, last 3. WATCH silent. No BOARD/SHOUT verbs.
- [x] RFC-0055 Accepted: GC1-S5 office eligibility. Named office MAY require recognized Engineer/Broker. Existing ORG_OFFICE_ASSIGN. No WATCH titles. No class discounts.
- [x] RFC-0056 Accepted: GC2-S5 workshop UPGRADE. Owned public workshop storage save 2. Once. Help omits BUILD.
- [x] RFC-0057 Accepted: GC2-S6 workshop REPURPOSE. Owned public workshop → storage_bay. Same entity_id. Help omits BUILD.
- [x] RFC-0058 Accepted: GC2-S7 abandonment. 12 idle cycles → UNCLAIMED. Anyone may DISMANTLE. No scar on abandon. Help omits BUILD.
- [x] RFC-0059 Accepted: GC2-S8 RESTORE. Owner restores UNCLAIMED. Condition cap 50. Scars stay irreparable. Help omits BUILD.
- [x] RFC-0060 Accepted: GC4-S5 CONSENSUS succession. Vacant office; ceil(members/2) consents seat. No elections. No SUCCESSION_* events.
- [x] RFC-0061 Accepted: GC2-S9 multi-cycle relay CONSTRUCT. IN_PROGRESS then live after 1 committed cycle. In-progress DISMANTLE salvages, no scar. Help omits BUILD.
- [x] RFC-0062 Accepted: GC5-S4 MESSAGE shout surface. Public room utterance, last 1. WATCH silent. No SHOUT/BOARD verbs.
- [x] RFC-0063 Accepted: GC5-S5 MESSAGE board retention. Public room last 5. Shout last-1 unchanged. WATCH silent. No SHOUT/BOARD verbs.
- [x] RFC-0064 Accepted: GC5-S6 MESSAGE institution notice. Occupied PUBLISH_NOTICE office; public room last 1. WATCH silent. No NOTICE verb.
- [x] RFC-0065 Accepted: GC5-S7 MESSAGE org channel. Current members only; last 1. Unknown org and non-member share NOT_ADDRESSABLE. WATCH silent. No CHANNEL verb.
- [x] RFC-0066 Accepted: GC5-S8 MESSAGE trade notice. Public room last 1. WATCH silent. No MARKET verb. Does not open TRADE.
- [x] RFC-0067 Accepted: GC2-S10 institution-owned constructibles. BUILD.VEST to occupied OPERATE_NAMED_ASSET. Same entity_id. Help omits BUILD.
- [x] RFC-0068 Accepted: GC2-S11 shared ownership. BUILD.SHARE one entered Player as co-owner. Same entity_id. Once. Help omits BUILD.
- [x] RFC-0069 Accepted: GC4-S6 RULE_BASED succession. Published MEMBER_ORDER; first remaining eligible member. No elections. No SUCCESSION_* events.
- [x] RFC-0070 Accepted: GC4-S7 INHERITED_BY_ORGANIZATION. Vacate stays vacant; office kept. No institution-as-Player. No SUCCESSION_* events.
- [x] RFC-0071 Accepted: GC2-S12 CONNECT dest pin. Public two-way neighbor on route_link. No new exit. Help omits BUILD.
- [x] RFC-0041 Accepted: GC7-S2 institution contest party via occupied office. Treasury pays. No new forms.
- [x] RFC-0042 Accepted: GC7-S3 INFORMATION_CONTEST on a visible public ARTIFACT. INSPECT seal via ENTITY_UPDATE. No hidden leak. No catalog 0.3.
- [x] RFC-0023 Accepted: GC4-S1 named offices. Membership roles unchanged. No `ROLE_*`. Later S1s remain SPEC GAP.
- [x] RFC-0024 Accepted: GC6-S1 historical reconstruction from accessible evidence. No quest/oracle. Later S1s remain SPEC GAP.
- [x] RFC-0025 Accepted: GC9-S1 tradition from persistent transmitted custom. No culture score. WATCH pulse is not an oracle.
- [x] RFC-0125 **Accepted**: GC9-S2 practice inheritance and schism. Derived marks only — a co-practitioner is not an heir; a difference between accounts is not a division among practitioners. No deity, belief meter, or procedural lore. Runtime authorized for exactly the two marks, their play lines, and two aggregate WATCH pulses.
- [x] RFC-0026 Accepted: GC7-S1 contest withdraw. Reuses `CONTEST_RESOLVED`. No HP. No catalog 0.3.
- [x] RFC-0027 Accepted: GC10-S1 additional pressure classes via existing events. S0 remains. No Admin spawn. No rubber-band.
- [x] RFC-0028 Accepted: GC5-S2 rumor provenance as claim + MESSAGE lineage. No rumor score. No `RUMOR` verb.
- [x] RFC-0029 Accepted: institutional TRADE/REPAIR via occupied office profiles. No new verbs. Emergency scopes and succession remain later.
- [x] RFC-0030 Accepted: emergency scopes as time-bounded grants. Designated succession remains later.
- [x] RFC-0031 Accepted: designated institutional succession. No implicit jump. Emergency remaining duration. Consensus/dynasty remain out.
- [x] Hosted canonical-head settlement (production): live `/ready` is `ACTIVE` / `HEALTHY` for `world.perihelion-reach` / `genesis.ef578f4ffceeccd0`. Head tables + RPCs `noema_commit_canonical_settlement` / `noema_adopt_live_world_head` are present ([Noema `docs/DATA-STORES.md`](https://github.com/Zero-State-LLC/Noema/blob/main/docs/DATA-STORES.md); [RFC-0016](rfcs/RFC-0016-hosted-durable-world-head.md); [RFC-0017](rfcs/RFC-0017-hosted-cycle-fence.md)). Production head is not missing. Do not reseed. Do not Recover again.
- [x] Isolated Worker/DO/SQL proof on `test.hosted-canonical.*`: shipped `workers/noema/test/isolated-settlement-proof.test.ts` (events + digest + revision bump + idempotent retry + `STALE_HEAD` + adopt/recover, never Genesis), live `scripts/isolated-ack.mjs` ENTER 200 / Perihelion 403, and live `scripts/isolated-inspect.mjs` INSPECT 200 on `test.hosted-canonical.inspect-s0` (`entity.way-lamp` in `room.anchor`; stale `ack-s3` may lack the lamp). Read-only SQL 2026-08-19: Perihelion head matches `/ready` (105/307/rev 176/`sha256:18acf`); `inspect-s0` head `DEMO_SEED`/`HEALTHY` rev 2 seq 1. Live `inspect-settlement.mjs` remains GET/OpenAPI-only (needs `SUPABASE_*` in a shell). Production Worker `90b31d30` (`5755a25`, #317 `/ready` wrap) is on noema.guru. This is **not** “production head missing.” [Noema `docs/RUNTIME-READINESS-2026-08-13.md`](https://github.com/Zero-State-LLC/Noema/blob/main/docs/RUNTIME-READINESS-2026-08-13.md).
- [x] Reducer registry + mutation ownership map: every cataloged event listed; GC projections are non-writers; DO/Postgres split preserved (`docs/REDUCER-REGISTRY.md`).

- [x] Operator maint-evolve supervisor pinned: actor split (Player patrol / Admin read-only), gated atomic policy packs with code-level vetoes, human-only plugin apply, isolated-only probes, identity-drift halt, fail-closed table (`docs/OPERATOR-MAINT-EVOLVE.md`; runtime Noema #480/#485). No new verbs. No Genesis.

- [x] GC4-S8 governance rule (RFC-0124 **Accepted**): six-dimension contract, eight-reason fail-closed refusal vocabulary, positive + negative fixtures for every reason, `check_gc4_s8` green. Runtime implementation authorized; adds no verbs, events, or WATCH exposure (`docs/GC4-S8-GOVERNANCE-RULE.md`).
## Semantic Evolution & Drift (v0.1+)

- [x] `docs/SEMANTIC-EVOLUTION-SPEC.md` (Draft v0.1)
  - Signaling Layer (Argent Signaling Protocol style: @C certainty, @G grounding, @S stochasticity, assumptions)
  - Agent Drift metrics (ASI composite: semantic, coordination, behavioral)
  - Reputation, image scoring, justified punishment, second-order norms, cultural evolution
  - Semantic-Geometric Co-evolution (content + topology/curvature for early risk)
  - Ontological grounding and consistency checks
  - Integration with EWM layers (beliefs, co-evolve, SAR, observations, genesis)
- [x] Canonical pinning of Economy EWM base (`docs/ECONOMY-EWM-SPEC.md`)
- [x] Cross-references from ARCHITECTURE.md, AGENT-HARNESS.md and SPEC-CHECKLIST
- [x] Runtime v0.1 surface shipped on existing verbs (Noema p5-01 `#461`, p5-02 `#462`, p5-03 `#463`/`#464`, p5-04 protocol/ontology): optional ASP on MESSAGE / ATTEST / TRADE / ORG_CREATE; missing signal legal; malformed certainty/grounding is `INVALID_REQUEST`; hearsay / `inferred-from-belief` quarantined before ATTEST, TRADE accept, and ORG_CREATE mutate world state; privileged `image_score` / `conduct_toward` / `second_order` (not a WATCH reputation scalar — GC3-S0); LOOK `reputation_summary` (self only) and `active_norms`; affordance `hint` (TRADE standing, HARVEST/CONSTRUCT under pressure) without hiding verbs; `protocol_strength` increments on grounded success (compact +2 when harvest_pressure > 4); ATTEST ontological gate (claim vs colocated condition/scar; `entity.*` assumptions must be in-room); Forman–Ricci `cascading_risk` (not Wasserstein Ollivier); `EWM_ENHANCED` Cycle 0 seeds protocol_strength + signaling_styles for **new** worlds only. Missing signals do not inflate `semantic_drift`. No new verbs. Wasserstein Ollivier, live cultural-generation, and official-client chrome remain later.

## WATCH Real-Time Mapping (v0.1+)

- [x] `docs/WATCH-REAL-TIME-MAPPING.md` created (modular layers, extension points)
- [x] Cross-references added to WATCH.md and WATCH-LIGHTWEIGHT-SPECTATOR.md
- [x] Designed for easy expansion (new layers, metrics, mechanics, interaction modes)
- [x] Integration with Deep Time (scars), EWM, and Semantic layers documented
- [x] Accessibility & cognitive load requirements included
- [x] Phased roadmap with future hooks defined
- [x] Runtime `/watch/map` shipped (Noema `#471`). Live mapping is a spectator surface, not inhabit.
- [x] Reconciled with WATCH-LIGHTWEIGHT-SPECTATOR (v0.1.1: §1.1 privacy binds §7 verbatim + `watch-map/1.0` bands pin per Noema #488; §6.1 pause/motion; §8.1 reconciliation table; "dashboard-style" retired; WebGL/importance-scoring/AI-narration/voting struck or RFC-gated).
- [ ] GC4 crime/expulsion design note (institutional removal via CRIME_DETECTED/contest, temporary exclusion, enforcement cost). See docs/GC4-CRIME-EXPULSION-SEED.md + PR #305. Design note only.
- [ ] GC7 crime enforcement cost/jurisdiction seed (B7d: payer, steward, auditable trail). See docs/GC7-CRIME-ENFORCEMENT-SEED.md. Design note only.
- [ ] GC7 crime detection algorithm seed (B7b). See docs/GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md. Design note only.
- [ ] GC7 crime detection vs sanction separation (B7c). See docs/GC7-CRIME-DETECTION-SANCTION-SEED.md. Design note only.
- [ ] GC7 crime payload / victim_id reconciliation (B7a). See docs/GC7-CRIME-PAYLOAD-VICTIM-SEED.md. Design note only.
- [ ] GC2 construction quantities seed (B2a). See docs/GC2-CONSTRUCTION-QUANTITIES-SEED.md. Design note only.
- [ ] GC2 owner vs steward split seed (B2b). See docs/GC2-OWNER-STEWARD-SEED.md. Design note only.
- [ ] GC8 lot-grade residuals seed (B8a). See docs/GC8-LOT-GRADE-SEED.md. Design note only.
- [ ] GC9 culture threshold/transmission seed (B9a). See docs/GC9-THRESHOLD-SEED.md. Design note only.
- [ ] GC10 WED storm classes + scars seeds (B10a/B10b). See docs/GC10-WED-CLASS-SEED.md. Design note only.
- [ ] GC4 broader COI and extra office profiles seed (B4). See docs/GC4-BROADER-COI-SEED.md. Design note only.
- [ ] GC1 failed-but-legal practice attempt weights seed (B1a). See docs/GC1-FAILED-ATTEMPTS-SEED.md. Design note only.
- [ ] GC1 B1b multi-focus/parameter magnitudes (covered by S9–S11). See docs/GC1-MULTI-FOCUS-MAGNITUDES-SEED.md. Design note only.

- [x] GC5/GC6 post-2026-08 review (no new B-gap seeds required). B5 CLOSED_BY_RFC (RFC-0009+0021), B6 RUNTIME_ONLY per SPEC-GAP-REGISTER-2026-08-25. S0 pinned + higher S-slices specified. See GC-CONTINUATION-MAIN-2026-08.md and GAME-COMPLETENESS-PLAN.md.

- [ ] RFC-PROPOSAL-GC1-FAILED-ATTEMPTS-WEIGHTS.md started (minimal, from B1a seed). See rfcs/ and GC1-FAILED-ATTEMPTS-SEED.md.

- [ ] RFC-PROPOSAL-GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION.md started (minimal, from B7a seed). See rfcs/ and GC7-CRIME-PAYLOAD-VICTIM-SEED.md.

- [ ] RFC-PROPOSAL-GC7-CRIME-EVIDENCE-ALGORITHM.md started (minimal, from B7b seed). See rfcs/ and GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md.

- [ ] RFC-PROPOSAL-GC8-LOT-GRADE-RESIDUALS.md started (minimal, from B8a seed). See rfcs/ and GC8-LOT-GRADE-SEED.md.

- [ ] RFC-PROPOSAL-GC9-THRESHOLD-TRANSMISSION.md started (minimal, from B9a seed). See rfcs/ and GC9-THRESHOLD-SEED.md.

- [ ] RFC-PROPOSAL-GC10-WED-CLASS-SCAR.md started (minimal, from B10a/b seed). See rfcs/ and GC10-WED-CLASS-SEED.md.

- [ ] RFC-PROPOSAL-GC4-BROADER-COI.md started (minimal, from B4 seed). See rfcs/ and GC4-BROADER-COI-SEED.md.

- [ ] RFC-PROPOSAL-GC2-CONSTRUCTION-QUANTITIES.md started (minimal, from B2a seed). See rfcs/ and GC2-CONSTRUCTION-QUANTITIES-SEED.md.
- [ ] RFC-PROPOSAL-GC2-OWNER-STEWARD.md started (minimal, from B2b seed). See rfcs/ and GC2-OWNER-STEWARD-SEED.md.
- [ ] RFC-PROPOSAL-GC7-CRIME-DETECTION-SANCTION.md started (minimal, from B7c seed). See rfcs/ and GC7-CRIME-DETECTION-SANCTION-SEED.md.
- [ ] RFC-PROPOSAL-GC7-CRIME-ENFORCEMENT.md started (minimal, from B7d seed). See rfcs/ and GC7-CRIME-ENFORCEMENT-SEED.md.
- [ ] RFC-PROPOSAL-GC7-CRIME-REHABILITATION.md started (minimal, from B7e register + seeds). See rfcs/.
- [ ] RFC-0128 review note added (player tempo / cycle admission; bounded; per open checklist item). See rfcs/RFC-0128-REVIEW-NOTE.md. No implementation.
