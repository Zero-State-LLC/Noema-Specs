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
- [x] Auth / identity / Agent Gateway: Account→Player→Controller→Credential+Session; humans and agents both Players; device enrollment; scoped caps; REST/WS/MCP gateway; threat model; MVP boundary (`docs/AUTH-AND-IDENTITY.md`, `docs/AGENT-GATEWAY.md`).
- [x] Hosted product stack pinned: Cloudflare Workers + Worker `[assets]` + Durable Objects + Supabase Auth/Postgres/Storage (`docs/PLATFORM.md`). Cloudflare Pages is not the live host.
- [x] Player-only domain participant; ControllerBinding metadata; PlayerPrincipal at edge.
- [x] Experience entry alignment: PLAY primary; WATCH/STUDY secondary product paths; CONNECT is Controller onboarding, not a Player mode; ADMIN remains a separate control-plane principal; hosted runtime projection documented as non-normative.
- [x] Hosted first-entry: world door + Player email; game-first first-read; Operator subordinate; Chamber first screen text-first (`docs/HOSTED-FIRST-ENTRY.md`).
## Core game design (player-facing)

- [x] Core game loop (primary + strategic overlay + timescales)
- [x] Realms as derived projections
- [x] Geography hierarchy and strategic room purpose
- [x] Emergent territory control
- [x] Crime as consequence layer; strategic contestation **executable** (RFC-0002 Accepted)
- [x] Loss/recovery, diplomacy, game cycle, world reports
- [x] Plural progression + ambitions (no single victory score)
- [x] Human play / agent play orientation (both are Players; Controllers differ)
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
- [x] `specs/event-types.0.2.json` (31 types = 24 + 7)
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
- [x] WATCH Lightweight Spectator Upgrade specified: public door is terminal theater (notable event, world graph, bounded feed, optional room detail); `NORMAL`/`NOTABLE`/`MAJOR` are display tiers only; hidden topology stays off WATCH; no dashboard/broadcast/AI-director ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- [x] Optional WATCH Phosphor Cartography specified: Canvas 2D sketch of `watch-live/1.0` only; TEXT remains authority; no hidden leak; no WebGL; no pin bump ([WATCH-LIGHTWEIGHT-SPECTATOR.md](docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18).
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

## First-world closure (FW)

- [x] FW01 operational envelope present (`ADMIN-LIVE`, `WORLD-OPERATIONS`, lifecycle, interventions, incident, onboarding, first-world ops)
- [x] FW02 Player ontology consistent (humans and agents are Players; Admin is not a Player)
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

- [x] Player / Controller parity; humans and agents use equivalent facts, actions, commitments, and consequences.
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
- [x] RFC-0041 Accepted: GC7-S2 institution contest party via occupied office. Treasury pays. No new forms.
- [x] RFC-0042 Accepted: GC7-S3 INFORMATION_CONTEST on a visible public ARTIFACT. INSPECT seal via ENTITY_UPDATE. No hidden leak. No catalog 0.3.
- [x] RFC-0023 Accepted: GC4-S1 named offices. Membership roles unchanged. No `ROLE_*`. Later S1s remain SPEC GAP.
- [x] RFC-0024 Accepted: GC6-S1 historical reconstruction from accessible evidence. No quest/oracle. Later S1s remain SPEC GAP.
- [x] RFC-0025 Accepted: GC9-S1 tradition from persistent transmitted custom. No culture score. WATCH pulse is not an oracle.
- [x] RFC-0026 Accepted: GC7-S1 contest withdraw. Reuses `CONTEST_RESOLVED`. No HP. No catalog 0.3.
- [x] RFC-0027 Accepted: GC10-S1 additional pressure classes via existing events. S0 remains. No Admin spawn. No rubber-band.
- [x] RFC-0028 Accepted: GC5-S2 rumor provenance as claim + MESSAGE lineage. No rumor score. No `RUMOR` verb.
- [x] RFC-0029 Accepted: institutional TRADE/REPAIR via occupied office profiles. No new verbs. Emergency scopes and succession remain later.
- [x] RFC-0030 Accepted: emergency scopes as time-bounded grants. Designated succession remains later.
- [x] RFC-0031 Accepted: designated institutional succession. No implicit jump. Emergency remaining duration. Consensus/dynasty remain out.
- [ ] Hosted canonical-head settlement: Worker #96 deployed; SQL/RPC apply and isolated verification not yet observed. Perihelion bootstrap blocked.
- [x] Reducer registry + mutation ownership map: every cataloged event listed; GC projections are non-writers; DO/Postgres split preserved (`docs/REDUCER-REGISTRY.md`).
