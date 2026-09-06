# MUD-Native Interaction — Technical Plan

**Implements:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md)  
**Craft companion:** [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md)  
**Tasks:** [MUD-NATIVE-INTERACTION-TASKS.md](MUD-NATIVE-INTERACTION-TASKS.md)  
**Constraint:** additive to the hosted Worker and frozen canonical world/action contracts.

## 1. Architecture decision

Do not put parser convenience inside world reducers.

```text
Agent Controller (structured)
  ↓
Canonical Action Mapper
  ↓
Existing admission/auth/budget/precondition path
  ↓
NoemaWorldDO / canonical settlement
```

Production inhabit is Agent Player only (RFC-0120). A Human Input Adapter, if retained for offline tests or operator diagnostics, is **NON-CANONICAL DEV TOOLING** and MUST NOT be a hosted admission path.

Presentation projections remain read-only:

```text
World state/events
  ├── Player observation → room grammar / traces
  └── Public projection → WATCH / homepage proof
```

## 2. Expected runtime boundaries

Inspect current equivalents before creating new modules. Prefer these conceptual boundaries:

```text
workers/noema/src/
  presentation/
    command-parser.ts
    command-aliases.ts
    command-help.ts
    room-view.ts
    world-traces.ts
    accessibility.ts
  watch.ts
  landing.ts
  actions.ts
  world-actions.ts
```

Do not force these exact paths if the current runtime has a cleaner existing boundary.

## 3. S0 — Parser normalization

Implement a pure deterministic parser library with:
- tokenization;
- keyword normalization;
- direction aliases;
- safe article removal;
- preposition handling;
- verb alias mapping;
- local target resolver;
- ambiguity result type;
- no mutation.

Suggested result type:

```ts
type ParseResult =
  | { kind: "resolved"; action: CanonicalAction; source: string }
  | { kind: "ambiguous"; candidates: Candidate[]; source: string }
  | { kind: "unsupported"; suggestions: string[]; source: string }
  | { kind: "invalid"; reason: string; source: string };
```

The parser must accept an explicit observation/affordance input. It may not query hidden world state directly.

### Tests
- table-driven equivalence cases;
- property test: equivalent aliases resolve to same canonical action;
- negative cases for hidden/non-local entities;
- ambiguity never calls mutation path;
- structured agent route bypasses parser.

## 4. S1 — Room grammar

Refactor human Chamber rendering around a normalized read-only `RoomPresentationModel`.

Suggested shape:

```ts
type RoomPresentationModel = {
  roomName: string;
  description: string;
  pressure?: string;
  here: PresentedEntity[];
  exits: PresentedExit[];
  happened?: string;
  localActions: string[];
};
```

Build only from current authorized Player observation.

No reducer or settlement code may depend on this model.

### Ordering
Pin deterministic ordering for HERE and EXITS. Use world-defined order where meaningful; otherwise explicit stable sort.

### Consequence translation
Create bounded mapping from action outcome/error class to world-native sentence. Keep machine code separately available for debug.

## 5. S2 — Contextual HELP + ambiguity UX

`help`, `help <topic>`, `help all` remain client/interface-only.

Add session-local ambiguity state:
- stores candidate references;
- stores observation/version fingerprint;
- TTL/bounded lifetime;
- invalidates when room/observation materially changes.

Never persist ambiguity state as world truth.

## 6. S3 — Environmental traces

Create a read-only trace projector.

```ts
Canonical state/events
→ eligible public/player-visible trace facts
→ trace projection
→ room presentation
```

Each projected trace carries internal provenance fields for verification:

```ts
{
  trace_id,
  kind,
  text,
  source_event_ids?,
  source_state_ref?,
  visibility
}
```

Public output may omit internal IDs while tests/admin/debug can verify them.

Start with one or two existing canonical families, preferably repair/construction/public notice, before generalizing.

No synthetic history generation.

## 7. S4 — Aliases/macros

Storage belongs outside world truth:
- account preference, browser storage, or existing Player preference surface;
- never Durable Object canonical state solely because command preference exists.

Alias expansion occurs before parser resolution.

Macros expand into a queue of ordinary human commands. Each step must re-resolve against the latest observation.

Hard bounds:
- max macro steps;
- max alias depth;
- recursion detection;
- no self-recursive alias;
- stop on failure/ambiguity/world-blocked/auth failure;
- no hidden retry.

## 8. S5 — Accessibility mode

Add one preference consumed by room/WATCH renderers.

Validate:
- semantic headings;
- explicit exits;
- no action available only through canvas/glyph;
- aria-live bounded;
- reduced-motion;
- keyboard-only use;
- mobile 375×812;
- desktop 1100px+.

## 9. S6 — WATCH narrative hierarchy

Refactor current WATCH feed selection into read-only editorial buckets:

```text
NOW
RECENTLY
WORLD
```

Reuse existing salience tiers for selection only.

For causal chains, require an explicit causal relation field or deterministic derivation rule approved in specs. Do not infer from timestamp adjacency.

Retain raw/bounded Recent feed under progressive disclosure if useful.

## 10. S7 — Homepage live-world proof

Homepage consumes a small public WATCH-safe endpoint/projection.

Requirements:
- timeout/failure fallback;
- no blocking hero render on data;
- bounded line count;
- no private fields;
- no dependency on authenticated Player state.

## 11. Compatibility

Must preserve:
- `/v1/command` canonical semantics;
- Agent Protocol;
- existing canonical action schemas;
- settlement/replay;
- current auth boundaries;
- Genesis;
- public WATCH redaction.

Human command strings may become more permissive without changing the canonical action envelope.

## 12. Performance

- parser: synchronous/pure for normal commands;
- help/alias expansion: no network call;
- trace lists bounded per room;
- WATCH processing bounded by recent event window;
- no new heavyweight frontend framework;
- preserve current HTML/asset budgets.

## 13. Feature gating and rollback

Each slice S0–S7 must be independently disableable until accepted.

Rollback must restore the previous presentation/input behavior without:
- database rollback of world truth;
- replay changes;
- reseed;
- settlement changes.

Trace schema additions, if any, must be additive and backward compatible.

## 14. Validation

For every slice:
1. unit tests;
2. hosted Worker tests;
3. canonical-action conformance;
4. redaction/security regression;
5. agent protocol regression;
6. desktop/mobile human QA when UI changes;
7. no Genesis/reseed;
8. spec/runtime cross-artifact check.

## 15. Deployment order

```text
S0 parser
→ S1 room grammar
→ S2 help/ambiguity
→ S3 traces
→ S4 aliases/macros
→ S5 accessibility
→ S6 WATCH narrative
→ S7 homepage proof
```

Do not parallelize S0–S2 in production because they share the same human command/room surface. S3 can be developed behind a disabled projection flag once its provenance model is settled.

## Extension Points

- **i18n / localization**: Centralize human command strings, help text, aliases, error messages, trace labels, and MUD surface strings in dev Chamber ui.py (t()/STRINGS) and any command parsers. Agent protocol remains canonical machine (no i18n there). Ties to AGENT-ORIENTATION-S0/S1/S2.md, ui.py sweeps, and TERMINOLOGY.md. Human-facing only for discoverability.
- **R3 / RFC-0120 agent-only player identity**: MUD native interaction is primarily for human dev / operator surfaces. Post-R3 hosted agent-only Players use protocol (no direct MUD parser). Handoff to AGENT-ONLY-PLAYER-IDENTITY.md, AGENT-GATEWAY.md, OFFICIAL-AGENT-CLIENT.md. Traces may be exposed to agents via WATCH / queries only.
- **Gate B (LCA-2)**: MUD S slices (esp. parser, traces, accessibility) support independent external Agent Players in Gate B by providing reliable human command surface for onboarding / testing. Cross-ref AGENT-HARNESS.md, AGENT-ONBOARDING.md, LCA-GATE-B-*.md. Evidence must include redacted transcripts.
- **AX (accessibility)**: S5 accessibility slice is core. Ensure semantic markup, ARIA roles/labels for command input, traces, help. CDP audits (keyboard, contrast, live regions) on Chamber 8765. High-contrast, reduced-motion. Ties to omh-accessibility-audit, prior AX work on ui.py.
- **Plugin atoms / DX**: Atoms or Hermes plugins for MUD trace visualization, command history, help expansion. Use graft for related nodes. Follow hermes-desktop-plugins + omh-frontend patterns. Easy extension for new S slices.
- **LCA2 / MUD handoff / R3+**: MUD feeds native human interaction for LCA civilization evidence (Gate C+). Parser/trace provenance supports replay and agent handoff. Update MUD plan + CORE-GAME-LOOP.md + AGENT-PLAY.md. No new verbs; composition only.
- **Graft / efficiency**: graft ask "MUD parser traces i18n AX Gate B" for savings (maintains 97%+ token reduction per AGENTS.md).
- **Handoff matrix**: Update NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN.md, AGENT-ORIENTATION-*.md, LCA-GATE-C-SCENARIO.md when S slices advance. Validate per noema-specs-mud-craft workflow (branch, validate, push, "merge and continue").
- **Validation / rollback**: Each S slice independently testable. Full validation includes unit, hosted, conformance, redaction, agent protocol, QA. No Genesis changes.

All extensions preserve canonical action contracts and event ledger. No silent invention. Game-first. Additive. Update this section first.
