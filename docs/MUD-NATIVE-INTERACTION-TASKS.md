# MUD-Native Interaction — Tasks

**Implements:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md)  
**Plan:** [MUD-NATIVE-INTERACTION-PLAN.md](MUD-NATIVE-INTERACTION-PLAN.md)  
**Craft companion / backlog:** [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md)

Use test-first, dependency-ordered work. Do not reopen frozen canonical verbs, Genesis, or settlement semantics.

## S0 — Deterministic parser (NON-CANONICAL DEV TOOLING)

**RFC-0120:** hosted human PLAY is retired. S0 remains only for offline tests, fixture authoring, and operator diagnostics. Production agents MUST NOT depend on this parser. Production continuation is A3/A4 (structured observation + `AVAILABLE_ACTIONS`).

### T0.1 Inventory current human command parsing
- Inspect current Worker human command path, parser helpers, action mapper, tests.
- Record all accepted aliases and current error behavior.
- No code change unless required for test harness.

### T0.2 Define parser result contract
- Add pure result types: resolved / ambiguous / unsupported / invalid.
- Include source input and canonical resolved action where applicable.
- Tests first.

### T0.3 Normalize movement aliases
- Add `e/east/go east/walk east/move east` equivalence for legal directions.
- Test unsupported/hidden/nonexistent exits.
- AC: 1, 4, 5, 6.

### T0.4 Normalize inspect phrases
- Add `look X/look at X/inspect X/inspect the X`.
- Exact local labels before prefixes.
- AC: 2, 3, 4, 5.

### T0.5 Add message phrase normalization
- Only when recipient is observable/known and unambiguous.
- Do not expose private identity lookup.
- Regression-test canonical MESSAGE semantics.

### T0.6 Add ambiguity state
- Session-local, bounded, observation-fingerprinted.
- Invalidates on material room/observation change.
- AC: 3.

### T0.7 Add unknown-command suggestions
- Suggestions from current legal affordances only.
- No hidden entity leakage.
- AC: 4, 5.

### T0.8 Agent bypass regression
- Assert structured agent protocol does not call human parser.
- AC: 6.

## S1 — Canonical room grammar

### T1.1 Create RoomPresentationModel
- Read-only, derived from authorized Player observation.
- No reducer dependency.

### T1.2 Stable room ordering
- Room name → description → optional pressure → HERE → EXITS → **STATUS** → HAPPENED → command.
- Stable HERE/EXIT ordering.
- AC: 7–10.

### T1.3 Remove default runtime leakage
- Keep IDs/cycle/sequence/controller/settlement/research labels behind Advanced/debug only.
- AC: 8.

### T1.4 Consequence translation
- Map success/failure/partial/wait to concise world-native sentence.
- Prefer four-beat craft (tried / ok|fail / changed / next) from [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §5.
- Preserve machine error code in debug state.
- PLAY plain-language table in craft §5.2 (not research experience-error catalog).
- AC: 9.

### T1.5 Mobile/desktop room QA
- 375×812 and desktop reference width.
- Room, one legal action, and consequence understandable without dashboard rail.

### T1.6 STATUS strip (craft C3)
- Render compact budgets after EXITS (energy, attention, compute, storage, influence).
- Human one-liner or expanded STATUS block; structured observation carries same budget keys.
- No HP/XP/research scores; no new resources.
- Optional flags only when session already knows them (`energy_floor_risk`, `play_blocked`).
- Spec: [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §4.
- Tests: LOOK/MOVE surface energy + ≥1 other budget without side panel.

### T1.7 Short-session mark scenario S-MARK-10 (craft C8)
- Manual or automated presentation test on Chamber seed.
- ≤10 meaningful acts → at least one rank 1–4 durable/informational mark legible in HAPPENED and/or Feature D trace.
- Not a score, achievement, or research metric.
- Spec: [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §6.
- No Genesis change.

### T1.8 Chamber projection examples (craft C1)
- Non-normative fixtures under `examples/mud-play-craft/`.
- Three rooms: Civic Exchange, Relay Quarter, Foundry Corridor — Feature B order including STATUS.
- Seed-backed names/exits/entities only; no invented quest content.
- Optional agent layer sketch JSON (not wire schema).
- QA: DESCRIPTION without live lists; room-local PRESSURE; AVAILABLE HERE ⊆ visible affordances.

## S2 — Contextual discovery and HELP

### T2.1 Local action selector
- Max 3 first-paint suggestions.
- Observation-derived only.
- AC: 11, 14.

### T2.2 Humanize labels
- Concrete phrasing that maps to canonical commands.
- No new verbs.

### T2.3 Contextual `help`
- Concise room-aware default.
- Zero-cost/non-mutating.
- AC: 12, 13.

### T2.4 `help <topic>` and `help all`
- Explicit deeper disclosure.
- Existing action authority only.

### T2.5 Ambiguity clarification UX
- Numeric/unique-name selection.
- Revalidate against current observation before execution.

## S3 — Environmental traces

### T3.1 Select initial trace families
- Prefer existing repair/construction/public notice families with strong provenance.
- No new world event solely for presentation.

### T3.2 Define trace projection schema
- kind/text/visibility + source event/state refs internally.
- Read-only projection.

### T3.3 Project first trace family
- Visible after originating Player leaves.
- AC: 15, 16.

### T3.4 Staleness/update rules
- Deterministic invalidation when source state changes.
- AC: 17.

### T3.5 Trace redaction/security tests
- Hidden/private source data never leaks.

### T3.6 Integrate traces into room prose/HERE
- Bounded output.
- No duplication flood.

### Runtime mapping (Feature D first family)

Production inhabit is Agent Player only (RFC-0120). S3 is a **read-only projector**
(`projectRoomTraces`) over existing residue. No `TRACE` verb.

| Family | Canonical source | Public kind | After originator `LEAVE_WORLD` |
|--------|------------------|-------------|-------------------------------|
| Scar | `entity.scar` (GC10 dismantle leftover) or genesis `entity_type=RUIN` | `scar` | yes |
| Repair plate | `ENTITY_UPDATE` operation=REPAIR stamps `last_repair_cycle` + `last_repair_handle` | `construction` | yes |
| Unfinished work | `entity.in_progress` | `construction` | yes |
| Unclaimed work | GC2 `unclaimed` infrastructure (abandoned after 12 steward-idle cycles) | `construction` | yes |
| Public notices | existing room `board` / `shout` / `institution_notice` / `trade_notice` | `notice` | yes, until expiry |
| Public rumor | GC5 PUBLIC claim whose `subject_ref` is this room or an entity here | `notice` | yes |
| Org insignia | `owner_id` of live infrastructure names an org | `notice` | yes |
| Vacant-office memorial | VACANT office of an org that has a mark in this room | `notice` | yes |

Internal `source_state_ref` is test/debug only. Public `Observation.location.traces`
stays `{ kind, text, visibility }`. Hidden rooms/entities never project. Cap 3.

WATCH and Home may project the same public scar / repair-plate / unfinished-work /
unclaimed-work / public-rumor / insignia / memorial families (never board, shout,
inbox, private rumor, or private LOOK/MESSAGE). Spectators see residue after the
originator `LEAVE_WORLD`. No `TRACE` verb. Genesis `RUIN` is a scar source; live
Perihelion does not need a reseed for that projector.

## S4 — Aliases and macros

### T4.1 Choose preference storage
- Browser/account preference; outside world truth.
- Document decision.

### T4.2 Alias CRUD + expansion
- Deterministic.
- Recursion/depth protection.
- Reserved-command protection.
- AC: 18.

### T4.3 Macro queue
- Hard step bound.
- Sequential.
- Re-resolve each step against current observation.

### T4.4 Stop conditions
- ambiguity;
- failure;
- blocked world;
- auth failure;
- observation invalidation.
- AC: 20.

### T4.5 Settlement/audit regression
- Each macro step is an ordinary canonical action.
- AC: 19.

## S5 — Accessibility mode

### T5.1 Add low-noise preference
- Client/account preference only.

### T5.2 Room renderer low-noise path
- Explicit exits/text meanings.
- Reduce decorative glyph repetition.

### T5.3 WATCH low-noise path
- Canvas never required.
- Semantic text remains complete.

### T5.4 Screen-reader/keyboard QA
- Bounded aria-live.
- Reduced motion.
- AC: 21, 22.

## S6 — WATCH narrative hierarchy

### T6.1 Define NOW/RECENTLY/WORLD selectors
- Bounded and deterministic.
- Public projection only.

### T6.2 Render hierarchy
- Preserve optional raw recent feed under disclosure.

### T6.3 Causal relation contract
- Use explicit relation or approved deterministic derivation only.
- Never temporal proximity.
- AC: 24.

### T6.4 WATCH privacy regression
- Private LOOK/MESSAGE/research data absent.
- AC: 23.

### T6.5 Spectator comprehension QA
- Can identify what is happening now and recent change without reading all events.

## S7 — Homepage live-world proof

### T7.1 Define bounded home projection
- Consume WATCH-safe data only.
- Max bounded lines.

### T7.2 Add resilient fetch/render
- Failure fallback keeps homepage usable.
- AC: 25.

### T7.3 Privacy and first-read QA
- No private data, research metrics, IDs, or runtime machinery.

### T7.4 Performance regression
- Preserve current hosted HTML/asset budgets.

## Cross-cutting

### TX.0 Craft companion backlog
Horizon-locked craft from [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md):
- **Specs-complete** C1–C9 (C2 sketch-only) — [MUD-PLAY-CRAFT-CLOSEOUT.md](MUD-PLAY-CRAFT-CLOSEOUT.md) for runtime phases R0–R5.
- Native Interaction implementation continues via S0–S7 tasks below; S1 SHOULD include T1.4 / T1.6 (four-beat + STATUS).
- Do not expand craft horizon here; file runtime PRs against Noema / client citing closeout phases.

### TX.1 Specs reconciliation
Update/cross-link:
- `README.md`
- `docs/MUD-DESIGN-CANON.md`
- `docs/MUD-PLAY-CRAFT.md`
- `docs/COMMAND-DISCOVERY.md`
- `CHANGELOG.md`
- any applicable acceptance/checklist map.

### TX.2 Runtime/spec matrix
For each S0–S7 mark:
- NOT_STARTED
- IMPLEMENTING
- IMPLEMENTED_UNVERIFIED
- VERIFIED

### TX.3 Security gate
Required before each production slice:
- no hidden entity leakage;
- no auth-role escalation;
- no macro bypass;
- no private WATCH/home leakage.

### TX.4 Determinism gate
Equivalent human strings must map to the same canonical action and event effect as the direct canonical form.

### TX.5 No-reseed gate
No task may require Perihelion reseed or Genesis change.

## Completion gate

Complete only when all 25 acceptance criteria in the parent spec pass and:

> A new human can enter a room, understand it, express ordinary intent naturally, act through existing canonical mechanics, see the consequence, and encounter durable evidence of other Players — while an agent Controller continues using the same structured canonical world with no parser dependency.
