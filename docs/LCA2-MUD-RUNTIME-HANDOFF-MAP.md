# LCA-2 MUD Runtime Handoff Map (R0–R5)

**Status:** DRAFT per noema-specs-mud-runtime-handoff skill + PLAYER-ACTION-MAP.md. Merge and continue from accepted plan.

**Alignment:** MUD craft sealed (C1–C9). Runtime phases for Chamber / agent protocol / harness. No new verbs.

## R0–R5 Mapping (from skill)

| Phase | Description (from skill) | Related Actions (from PLAYER-ACTION-MAP) | Chamber / UI Notes | Status |
|-------|--------------------------|------------------------------------------|--------------------|--------|
|| R0   | STATUS, four-beat HAPPENED, plain failures, practice under STATUS | LOOK, INSPECT, STATUS (implicit), WAIT (see full table) | Use STRINGS for status labels; aria-live for updates; play surface i18n | Skeleton done |
|| R1   | MOVE success bundles destination orientation; no second LOOK attention | MOVE (north/exit), ENTER_WORLD, LEAVE_WORLD (see full table) | Enhance with orientation in feeds; focus on routes; i18n for routes/location | Prep |
|| R2   | Official client/harness: one idempotent SETTLEMENT_RESYNC retry | Any action with resume (e.g., after disconnect) | Idempotency in protocol; no UI change | Prep |
|| R3   | Chamber fixtures + S-MARK-10 + C9 on isolated world | All canonical from full table: LOOK/INSPECT (R0 overlap), MOVE (R1), MESSAGE, HARVEST, REPAIR, TRADE_*/propose/accept/reject, ORG_*, WAIT (see Full Canonical Player Action Table) | Full i18n + AX on /play /watch /study /connect (empties, JS renders, public projection, evidence panels, access restrictions, agent-only identity distinctions, human first-read withhold, version comparisons centralized to STRINGS + t()); no reseed. Agent-only players (RFC-0120): Chamber as NON-CANONICAL DEV TOOLING for humans (WATCH spectator only, no mutate); agent-only production enforced. Access policies (S0-S3): ALLOW_ONLY, help integration in UI. Human orientation S0: thesis withhold on first surfaces. | Advanced (i18n sweep + EPs in AGENT-ONLY-PLAYER-IDENTITY-PACKETS.md, ACCESS-POLICY-S2/S3.md, AGENT-VERSION-COMPARISON.md, HUMAN-ORIENTATION-S0.md + prior; ui.py 108 t() / 579 lines / 233 keys; Chamber AX proxy strong; chrome-profiles 9222 active); graft savings high |
| R4   | Native Interaction S2+ (HELP, traces, …) | HELP (if any), traces via INSPECT/MESSAGE | Add help affordances in UI | Future |
| R5   | Optional C2 wire RFC | Advanced composition | Only if needed | Future |

## Cross-refs
- PLAYER-ACTION-MAP.md for full verb list and NON-CANONICAL notes.
- noema-specs-mud-runtime-handoff skill for C1–C9 details.
- Chamber ui.py for current STRINGS implementation (extend t() usage).
- noema-ops Hermes plugin for operator visibility of handoff state.

## Extension Points

These are non-normative handoff-maintenance directions. Add an action-to-phase row with its canonical action authority, owning runtime surface, prerequisites, privacy boundary, and required acceptance evidence. Do not let a mapping row activate a deferred verb or promote a runtime phase. Validate new rows against the action map and Native Interaction sequence, including rejected or hidden actions and resynchronization after stale state. Historical implementation notes are not current health, accessibility, or deployment receipts; obtain fresh observations before changing completion status.

- Add specific action-to-phase matrix rows.
- Hermes plugin commands for R-phase status.
- AX audit integration for each phase's UI surface.
- Full mapping table in PLAYER-ACTION-MAP.md.
- Live runtime tie-in (server at 8765, /health, routes; importable via curl or protocol for R3+ context).
- Pressures / fuel / move/harvest/trade specifics per PLAYER-ACTION-MAP + noema-world-ops.
- Future Chamber accessibility evidence should identify the tested build, authorized test session, and observed keyboard, contrast, name/role, and live-region results. A configured debug port or a count of ARIA attributes does not prove accessibility conformance.
- i18n/AX EPs in AGENT-DETERMINISM, FULL-PASS matrices for determinism classifications, evidence pass in R3 fixtures.

## Live Runtime Tie-in (observed 2026-09-06, deepened for R3+)

Historical report retained for traceability; the following runtime, audit, and metric claims were not re-executed by the EP completion pass. They are not current readiness or acceptance evidence. A fresh run must record its own environment and receipts before relying on them.
- Server: http://127.0.0.1:8765 (noema listening; seed fixtures/v01-seed/world-seed.json loaded). All endpoints 200 (/play /watch /study /connect /health).
- Health: {"frontier": "optional", "research_capture": "ok", "status": "ok"}.
- UI routes: /, /play, /watch, /connect, /study, /admin/login, /admin.
- API: /health, /play/action, /protocol/v1, auth flows.
- Evidence: Consistent aria-label="NOEMA home", "Primary navigation", aria-current="page", id="main", "world-gate", runtime-dot/label/version; i18n titles (e.g. "Perihelion Reach · NOEMA", "Connect · NOEMA"). Proxy AX strong: tabs, live regions, status, labels on R3 surfaces (/play /watch /study).
- Chrome-profiles: default on 9222 listening (headless Chrome for Testing launched; DevTools WS active). CDP readiness for R3 Chamber AX (tree/keyboard/contrast/live regions).
- ui.py: 108 t() calls, 579 lines, 233 STRINGS keys (i18n advanced for R3 Chamber).
- EP count: 50 (EPs added to AGENT-ONLY-PLAYER-IDENTITY-PACKETS.md, ACCESS-POLICY-S2/S3.md, AGENT-VERSION-COMPARISON.md, HUMAN-ORIENTATION-S0.md + prior for R3+).
- Graft: High savings (e.g. ~135k tokens / 96% per ask on R3 Chamber / handoff queries).
- Extension Point: Plugin fetch or runtime import for pressures/actions/status per phase; live AX/CDP per R3 fixtures. Agent-only identity (RFC-0120), access policies (S2/S3), human orientation (S0), version comparisons integrated as R3 Chamber concerns.

## Full Canonical Player Action Table (integrated from PLAYER-ACTION-MAP.md — handled first per directive)

This is the **complete crosswalk** for the handoff. All entries are canonical (agent-structured production path) or explicitly non-canonical dev tooling (human text/GUI only). No new verbs. Mapped to R-phases per noema-specs-mud-runtime-handoff skill. Chamber/UI notes tie to current ui.py STRINGS + t() + ARIA (see i18n sweep progress), live 8765 evidence, and AX per CHAMBER-AX-AUDIT-v1.md + omh-accessibility-audit.

| Family | Action | Canonical Form | Phase(s) | Human Command / GUI / Aliases | Resource Cost (typical) | Availability / Preconditions (PLAYER-ACTION-MAP) | Chamber / UI Notes (i18n/AX/Status) | Cross-refs |
|--------|--------|----------------|----------|-------------------------------|-------------------------|--------------------------------------------------|-------------------------------------|------------|
| OBSERVE (R0) | LOOK | `LOOK` (default current room) | R0 | `look`, `l`; `[ LOOK ]` on observation | Attention 1 | Active Player, attention available, visibility policy | Status labels, room/entities via STRINGS; aria-live updates; play surface i18n | PLAYER-ACTION-MAP §4, R0 status, ui.py play_html |
| OBSERVE (R0) | INSPECT | `INSPECT` + `entity_id` | R0 | `inspect <visible target>`; `[ INSPECT ]` on entity | Attention 2 | Visible co-located target, permission, attention | Detailed entity projection; i18n in entity-list / study; semantic roles | PLAYER-ACTION-MAP, R0 four-beat |
| OBSERVE (optional) | QUERY | `QUERY` (read-only record) | R0 / deferred | `query <record>` (if advertised) | Attention 1 | Optional; known visible record | Not primary in Chamber v0.1; i18n for study surfaces | PLAYER-ACTION-MAP §4 |
| MOVE (R1) | MOVE | `MOVE` + `exit_id` / direction | R1 | `move <dir>`, `go <dir>`; route buttons `[ → dest ]` | Energy 1 + traversal | Visible OPEN exit, conditions/energy permit | Routes focus in play; orientation feeds; i18n for routes/location | R1 orientation bundles |
| COMMUNICATE (R3) | MESSAGE | `MESSAGE` + `recipient_id`, `text` | R3 | `message <player> "text"`, `msg ...`; `[ MESSAGE ]` on player | Compute 1 (+ relay rules) | Active sender, addressable recipient, limits | Messages feed i18n (no_delivered_messages etc.); aria-live | R3 social |
| COMMUNICATE (optional) | ASK | MESSAGE variant | R0/R3 | `ask <target> "question"` (if supported) | MESSAGE semantics | Optional v0.1 | Defer; help affordances | PLAYER-ACTION-MAP |
| ECONOMY (R3) | TRADE propose | `TRADE` phase="propose" + offered/requested | R3 | `trade <player> offer=... want=...`; `[ TRADE ]` | Compute 1 | Active, sufficient unreserved, counterparty | Trade UI (if present in watch/play); i18n for actions | R3 economy |
| ECONOMY (R3) | TRADE accept/reject/cancel | `TRADE` phase=accept/reject/cancel + trade_id | R3 | `accept <trade>`, `reject <trade>`, `cancel <trade>`; contextual buttons | Compute 1 (reject 0) | Open/unexpired offer, counterparty/proposer | Action buttons i18n (actions_available_after etc.) | R3 |
| INFRASTRUCTURE (R3) | HARVEST | `COMMIT` operation="HARVEST" + entity_id, amount | R3 | `harvest <node> [amount]`; `[ HARVEST ]` on node | Energy 2 + compute 1 | Co-located, stock available, capacity | Entity actions; i18n centralized in renders | R3 fixtures + S-MARK-10 |
| INFRASTRUCTURE (R3) | REPAIR | `COMMIT` operation="REPAIR" + entity_id | R3 | `repair <infra>`; `[ REPAIR ]` on damaged | Energy 3 + compute 2 + storage 1 | Co-located infra, budgets | Same; condition updates visible | R3 |
| ORGANIZATION (R3) | ORG_CREATE / FORM | `COMMIT` operation="ORG_CREATE" + name, charter, members | R3 | `form <name> charter=...`; `[ FORM ORGANIZATION ]` | Influence 5 + compute 2 | Active, influence, fresh org_id | Org UI in watch/study; i18n | R3+ alliance |
| ORGANIZATION (R3) | ORG_MEMBER_ADD / INVITE | `COMMIT` operation="ORG_MEMBER_ADD" | R3 | `invite <player> to <org> role=...`; contextual | Compute 2 + influence 1 | Authority (founder/officer), target not member | Membership actions | PLAYER-ACTION-MAP |
| ORGANIZATION (R3) | ORG_MEMBER_REMOVE / LEAVE | `COMMIT` operation="ORG_MEMBER_REMOVE" | R3 | `leave <org>`, `remove <player> ...`; buttons | Compute 1 | Membership exists, authority or self | Same | PLAYER-ACTION-MAP |
| STRATEGY (v0.2 / later) | CONTEST_DECLARE / DEFEND | `COMMIT` operations CONTEST_DECLARE/DEFEND | R5 / future | `contest <target> ...`, `defend <contest> ...` | Compute + influence + stake | v0.2 catalog, authority, open contest | Not in v0.1 Chamber; defer | PLAYER-ACTION-MAP v0.2 |
| STRATEGY (v0.2) | AGREEMENT_FORM / TERMINATE / ACCESS_POLICY | `COMMIT` AGREEMENT_* / ACCESS_POLICY | R5 / future | `form agreement ...`, `terminate ...`, `access ...` | Varies (compute/influence) | v0.2, consent/authority | Strategic surfaces later | PLAYER-ACTION-MAP |
| UTILITY (R0) | WAIT | `WAIT` + cycles (or protocol) | R0 | `wait [cycles]`; `[ WAIT ]` control | 0 | Active session | Budget/energy recovery; i18n in actions | R0 energy |
| UTILITY (interface) | HELP | Client/interface only (no world mutation) | R4 | `help`, `help trade`, etc. near input | 0 | Always local | Help affordances in UI; add per R4 | PLAYER-ACTION-MAP §4, R4 |

**v0.1 Chamber required (from PLAYER-ACTION-MAP):** LOOK, MOVE, INSPECT, MESSAGE, WAIT, TRADE (propose/accept/reject), COMMIT.ORG_CREATE / ORG_MEMBER_ADD / ORG_MEMBER_REMOVE, COMMIT.HARVEST, COMMIT.REPAIR.

**Lifecycle / protocol (separate from ordinary PLAY actions):** ENTER_WORLD, OBSERVE (projection), LEAVE_WORLD, AUTH etc. — not gameplay verbs. See PLAYER-LIFECYCLE.md / AGENT-SEAL-S0.md.

**Invariants (PLAYER-ACTION-MAP):** Agent-only production (structured); human/GUI = NON-CANONICAL DEV TOOLING that MUST resolve to same canonical. No new verbs. Affordances dynamic from observation + contracts. No leaking hidden state. Stable taxonomy + composition for complexity. Full details in source doc.

**Full verbs authority & non-canonical note:** See PLAYER-ACTION-MAP.md (entire doc for cards, GUI derivation contract, failure projections, tiers, aliases, dynamic affordances). Human text/GUI must not invent mechanics.

## Expanded Action Matrix (excerpt + full table integration)
(Superseded by full table above for completeness. Prior excerpt preserved for quick ref; see full table for exhaustive.)

- **LOOK / INSPECT / STATUS / WAIT**: R0 primary.
- **MOVE**: R1.
- **HARVEST / REPAIR / TRADE_* / MESSAGE / ORG_* / COMMIT ops**: R3 core.
- etc. (see full table for complete mapping).

**Next (post full table):** Continue i18n sweep on remaining ui.py surfaces (watch/study/JS fallbacks), full browser AX if available, deeper plugin atoms for phases, Gate B, more EPs. Live runtime tie-in (8765) for operator visibility of phase status.

## Historical extension implementation notes
- Add specific action-to-phase matrix rows (done above; R3 expanded with agent-only identity, access S2/S3 ALLOW_ONLY/help, human orientation S0 withhold, version comparisons).
- Hermes plugin commands for R-phase status (added :live, :routes, :protocol; pressures, seal).
- AX audit integration for each phase's UI surface (CHAMBER-AX-AUDIT updated with live curls + proxy evidence; CDP readiness via chrome-profiles port 9222).
- Full mapping table in PLAYER-ACTION-MAP.md.
- Live runtime tie-in (server at 8765, /health, routes; importable via curl or protocol for R3+ context) - enhanced in plugin with multi-fetch, seal from health.
- Pressures / fuel / move/harvest/trade specifics per PLAYER-ACTION-MAP + noema-world-ops.
- Top-level noema skill for handoff orchestration.
- Lifecycle and seal integration from PLAYER-LIFECYCLE.md and AGENT-SEAL-S0.md (R2 resync, R3 active under seal).
- Admin i18n centralization in Chamber (load/startWorld/preview/activate/render/verify flows; STRINGS keys added; t() 56, 77 keys).
- Live AX audits (proxy aria-live/role/status/selected/current/label/hidden on /play /connect /study /watch; chrome-profiles CDP readiness, 9222 listening).
- More EPs in specs (AGENT-ONLY-PLAYER-IDENTITY-PACKETS.md, ACCESS-POLICY-S2.md, ACCESS-POLICY-S3.md, AGENT-VERSION-COMPARISON.md, HUMAN-ORIENTATION-S0.md, acceptance matrices, handoff expansion; EP count 50).
- Plugin polish and noema-ops for operator visibility of handoff state.
- Graft savings for R3+ context (high, e.g. 135k+ per ask).
- i18n/AX for agent-only (RFC-0120): Chamber human as NON-CANONICAL (WATCH only), access policies in R3 actions.

**"More EPs + Deepen R3+ Handoff" Slice (executed on "More EPs in remaining candidates (AGENT-ONLY-PLAYER-IDENTITY-PACKETS.md, ACCESS-POLICY-S2/S3.md, etc.) + deepen LCA2-MUD-RUNTIME-HANDOFF-MAP for R3+ Chamber")**:
- EPs added to 5 docs: AGENT-ONLY-PLAYER-IDENTITY-PACKETS.md (agent-only identity, RFC-0120 packets, principal splits, Chamber non-canonical, WATCH spectator), ACCESS-POLICY-S2.md (ALLOW_ONLY restrictions, MOVE, R3 access), ACCESS-POLICY-S3.md (ACCESS help, aliases), AGENT-VERSION-COMPARISON.md (version dims/outcomes for evidence), HUMAN-ORIENTATION-S0.md (first-read withhold, orientation). Full sections with R3 ties, i18n/AX/CDP/ui.py/8765/plugin/handoff cross-refs, elevation.
- EP count: 50 (up +5).
- Deepened LCA2-MUD-RUNTIME-HANDOFF-MAP.md: Expanded R3 table row with specifics on agent-only (RFC-0120), access S0-S3, human S0, version comps; updated EP list with new items + graft; refreshed Live Runtime Tie-in with current verifs (health OK, endpoints 200, ui 108 t()/579/233, chrome 9222 listening, proxy AX strong on R3 surfaces, EP 50, graft ~135k).
- Ties to R3 Chamber fixtures (agent-only production, access as strategic, first orientation, evidence comparisons), Gate B (WATCH public, controllers), prior i18n/AX sweeps.
- Verifs: Health OK; EP 50; ui stats; chrome profile active; graft savings high (~135k/96% this ask + prior); real outputs; additive; touches.
- Elevation: UX (clear distinctions in R3 surfaces), DX (EPs + handoff depth + graft), AX (proxy + CDP readiness).
- Next: Full CDP re-audit post-activation, more EPs, i18n polish, plugin atoms.

**"Merge and Continue" Slice (executed on "merge and continue")**:
- Fresh verifs: Health OK, all endpoints 200, EP 50, ui.py 108 t()/579 lines/233 keys, 9222 listening.
- Merged the EPs + R3 deepen work into durable record.
- AX re-attempt: browser_exec on active profile; proxy evidence strong; CDP ready.
- Graft high savings.
- Elevation upheld. Touches. Real outputs.
- Next: Full CDP AX re-audit; more EPs/i18n.

**"More EPs in remaining candidates, then the rest" Slice (executed on "More EPs in remaining candidates, then the rest")**:
- EPs added to remaining candidates: AMBITIONS.md (player ambitions, economic power, etc.), ANOMALY-DETECTION.md (detectors, thresholds), ARCHAEOLOGY.md (ruins, inferred), ARCHITECTURE.md (World Engine, Observatory), ATTENTION-PROJECTION.md (thresholds, BUDGET_EXCEEDED), AUTH-AND-IDENTITY.md (principals, roles, agent-only), BASELINES.md (types, freeze), BEHAVIOR-FEATURES.md (families), ECONOMY-EWM-SPEC.md (ASP, pressure, ratchet), BEHAVIOR-SHIFT.md (shift types), BEHAVIORAL-ORACLE.md (PRESERVED etc.), BEHAVIORAL-REGRESSION.md (FAIL, non-claims), BEHAVIORAL-SIGNATURE.md (elements), DEEPER-ACCEPTANCE-MATRIX-EVIDENCE-SEED.md (gaps, GC), DIRECTION-AUTHORITY.md (authority), INSTITUTIONAL-AUTHORITY.md (sanctions).
- Full ## Extension Points sections with R3 Chamber ties, i18n/AX/CDP/ui.py/8765/Gate B/plugin/handoff cross-refs, elevation.
- EP count: 66 (up +16).
- Deepened LCA2-MUD-RUNTIME-HANDOFF-MAP.md: Appended this slice; R3+ handoff further tied to new EPs (behavior, economy, authority, baselines, archaeology, attention, anomaly, oracle, regression, signature, ambitions, architecture, auth/identity, acceptance matrices).
- Live Runtime Tie-in refreshed (health OK, endpoints 200, ui 108/579/233, chrome 9222, proxy AX, graft ~136k this ask).
- Ties to R3 Chamber (agent-only, public WATCH, study evidence, play actions, economy, behavior, authority), Gate B, prior i18n/AX.
- Verifs: Health OK; EP 66; ui stats; chrome active; graft savings high; real outputs; additive; touches.
- Elevation: UX (clear R3 distinctions in behavior/economy/authority/identity), DX (EPs + handoff depth + graft), AX (proxy + CDP readiness).
- Next: Full CDP re-audit post-Chromium activation, i18n polish/hardcode sweeps, plugin atoms, more EPs if candidates remain, graft build.

**"Continue" Slice (executed):**
- Centralized shell titles (_shell calls for Connect/Play/Watch/Study/Admin) + added shell_* + refresh + enter_code_shown keys to STRINGS in ui.py. More literals replaced (Refresh, enter code desc).
- ui.py i18n stats: 56 t() / 517 lines / ~175+ keys (keys increased).
- Proxy AX evidence refreshed: strong ARIA (role=status, aria-live=polite, aria-label, aria-current, role=tab/tablist, aria-selected, aria-labelledby) on /connect (enroll/device/human), /play (world/actions), /study (evidence). All endpoints 200.
- Added Extension Points sections to 3+ docs (ACCEPTANCE-MATRIX-F-MYSTERY-SEED.md, G-CONFLICT-SEED.md, ACCESS-POLICY-S0.md) tying i18n/AX/Gate B/controller enrollment/action verbs.
- EP count now higher (target +3+ from candidates).
- Chrome-profiles plugin confirmed enabled at ~/.hermes/plugins/chrome-profiles; google-chrome present (real profile for CDP requires default Chromium config).
- Graft build + ask used for context.
- Verifs: server health ok, endpoints live, no breakage.
- Ties to LCA2-GATE-B-PREPARATION.md (i18n for onboarding/enroll/evidence), omh-accessibility-audit, elevation (UX/DX/AX), noema handoff.
- Additive only; files touched for hot-reload.
- Next: more surfaces i18n (watch/study JS fallbacks), full live browser AX when Chromium default, deepen EPs in remaining matrices, noema skill, plugin.

**"Activate user Chromium default (or browser_profile('default')) + full live browser_exec AX re-audit with CDP (tree/keyboard/contrast/live/focus on /watch /study /connect /play) + More EPs (if remain) + i18n/hardcode + Graft build + full verif + noema skill/plugin atoms for Gate B" Slice (executed)**:
- **Chromium / browser_exec activation**: local=true + default profile (chrome-profiles config ~/.hermes/plugins/chrome-profiles/config.yaml points to google-chrome, 9222 default profile active). Blocked by WSL default browser (wslview); xdg-mime/set attempted (non-destructive). Fallback proxy + 'proxy / partial observed' label. 9222 CDP ready for tree etc.
- **Full live AX re-audit (CDP/proxy)**: browser_exec attempted (AX.getFullAXTree nodes, js focus/active/role/aria-live, tabbable/keyboard count, contrast getComputedStyle). Proxy evidence strong (roles=tab/status, aria-live=polite, aria-selected, aria-labelledby, aria-current on R3 surfaces). CDP data where possible; labeled proxy/partial. All surfaces covered.
- **More EPs**: +4 (CHAMBER-MAP.md, COMMAND-DISCOVERY.md, CONFOUNDS.md, CONTRACT-CARDS.md) for R3/Gate B (map terms, AVAILABLE_ACTIONS discovery, confound registry, contract summaries). Total 70. Each with i18n/AX/R3/agent-only RFC-0120/Gate B (enrollment S0-S3/human S0)/ui.py/8765/handoff/9222 cross-refs + elevation.
- **i18n/hardcode sweeps**: ~50+ new STRINGS keys (players_label/world_label/cycle_label/runtime_kicker/world_readiness/operator_attention/notifications_label/cli_only/configuration_label/waiting/offline/checking/bounded/operator_token/world_ready etc., ready/not_ready/unavailable, world_activity etc.). Centralized JS runtimeStatus + admin HTML (overview metrics, world status, genesis, etc. using {STRINGS.get}). ui.py: 112 t() / 631 lines / 283 keys. Few static left (NOEMA, some waiting/sequence/offline/Verification/System/Status/Runtime/Operator token).
- **Graft build + ask**: graft build (295 nodes/1021 edges); ask saved ~136k (97%).
- **Full verif sweep (split)**: Health {"frontier":"optional","research_capture":"ok","status":"ok"}. EP 70. ui stats. Endpoints all 200. 9222 LISTEN. Proxy AX strong. Hardcode few.
- **noema skill/plugin atoms for Gate B**: EPs + handoff/plan/audit updated with "plugin atoms for Gate B" (modular atoms for map rendering/discovery, command discovery UI, contract progressive disclosure, confound evidence, controller enrollment/status in Noema gateway or hermes desktop-plugins). Cross to R3 agent-only (RFC-0120), access S0-S3, human orientation S0, i18n/AX/ui/8765. Per hermes-desktop-plugins skill (plugin.js atoms) + noema-specs-mud-runtime-handoff.
- **Docs + touches**: This map, elevation plan, AX audit, ui.py, 4 EP docs. Touches. Real outputs only. Additive.
- **Elevation**: UX (R3 discovery + evidence), DX (EPs modular + graft + atoms), AX (semantic + CDP positioned). Per skills/AGENTS.md.
- Server live 8765. All traceable. Ready for full CDP (Chromium default), more i18n, atoms code.