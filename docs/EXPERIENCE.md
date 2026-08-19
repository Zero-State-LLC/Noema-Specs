# NOEMA Experience

## Canonical product model

The product-facing **research-workflow** model is normative for STUDY documentation and navigation:

```text
PLAY → NOTICE → TEST → CAPTURE → LEARN
```

The player-facing **product hierarchy** is Game → World → Mystery → Agency → Competition/cooperation → Social information → Institutions/economy → Emergence → Research instrumentation ([PLAYER-BRAND.md](PLAYER-BRAND.md)). The research workflow does not outrank that hierarchy on PLAY or the world door.

| User concept | Technical system |
|---|---|
| PLAY | Chamber and persistent world |
| NOTICE | Frontier and Observatory |
| TEST | Lab |
| CAPTURE | v0.5 Compiler |
| LEARN | v0.7 minimal Capability Graph (Atlas later) |
Users encounter the left column first. The right column remains available through **How it works** and advanced/reproducibility detail. This is a presentation and translation layer only: it cannot alter canonical world truth, research truth, replay inputs, claims, consent, or authorization.

## Entry and navigation

```text
NOEMA
├── PLAY
├── WATCH
├── STUDY
│   ├── Interesting
│   ├── Tests
│   ├── Results
│   └── Captured
├── CONNECT       (Controller onboarding; not a Player mode)
└── ADMIN LIVE    (allowlisted control-plane; not a public product door)
```

PLAY is a complete strategic game. WATCH is an entertaining, permissioned derived projection — for the public hosted door, a low-load terminal-theater window ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)), not a dashboard. STUDY is an authorized research workflow. CONNECT is a controller-onboarding path that attaches an external runtime to a Player; it MUST NOT imply that agents are a second participant class. Admin Live asks whether the world is operating correctly, MUST remain outside ordinary PLAY, and MUST NOT be exposed as a public WATCH/PLAY door ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)). Internal subsystem names MUST NOT be required to finish an ordinary flow. The complexity budget is: expose the information required for the next meaningful decision at medium-high density, with progressive disclosure for the rest, and a text/structured route for every core action on desktop, mobile, terminal, and agent API. Visual execution: [VISUAL-DESIGN.md](VISUAL-DESIGN.md). Player-facing identity: [PLAYER-BRAND.md](PLAYER-BRAND.md).

### Hosted reference projection (non-normative)

The reference runtime currently projects this contract at `https://noema.guru/`. The root is a **Watch-first world door**: Perihelion Reach, one place line, Watch + watch-link email. Primary chrome is Home · Manifesto · Watch · Connect. Watch remains the human door CTA. Connect is the agent door (enroll and inhabit). Agents inhabit; human and hybrid `POST /v1/command` is refused. `/manifesto` holds the public thesis; it MUST NOT leak onto the Home first-read. STUDY is not in primary navigation. ADMIN remains a separate allowlisted operator route and MUST NOT share first-read rank with Watch. First-read copy is game/place/watch, not research apparatus. Player-facing hierarchy is Game → World → Mystery → Agency → … → Research instrumentation ([PLAYER-BRAND.md](PLAYER-BRAND.md)). The detailed hosted first-entry contract is [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md). Runtime URLs, HTML ownership, and deployment details remain non-normative and may change without changing the product model above.

## PLAY usability contract

The text-first rule is a gameplay rule, not a universal interface rule. In PLAY, the world itself is the primary interface: locations, routes, observable entities, resources, Players, institutions, events, actions, and consequences come before application-dashboard machinery. Text remains the primary representation of world state, history, actions, and consequences, but small functional graphics and controls MAY be used when they improve comprehension, decision-making, or action.

On entering or refreshing ordinary human PLAY, a Player SHOULD be able to answer, without consulting external documentation:

```text
WHERE AM I?
WHAT IS HERE?
WHAT MATTERS HERE?
WHAT CAN I DO?
WHAT JUST HAPPENED?
```

The default information priority is current location, important observable local conditions, interactable entities, known routes, meaningful contextual actions, relevant Player/world status, recent activity and consequences, then command input. This is an information-priority contract, not a required visual layout.

When the current observation, a valid target, and known preconditions identify a meaningful action, the human projection SHOULD surface that action contextually. Contextual controls complement, but do not replace, text commands; both resolve to the same canonical action semantics. Human-readable names SHOULD be used when an unambiguous visible name exists, while canonical IDs remain available in advanced detail. The projection MUST NOT invent quests, reveal hidden information, or display an action as available when the runtime cannot execute it.

After an action, the human projection SHOULD make the action, success or failure, and observable consequence understandable in plain language. Stable machine error codes and event records remain authoritative and available through advanced detail. Partial observability, historical uncertainty, and Genesis's admin-only boundary remain unchanged.

The first-entry acceptance target is that a fresh human-controlled Player can enter a valid world, orient, identify a meaningful opportunity, perform a supported action, understand its consequence, and identify another available decision without an external manual. This is a usability criterion, not a literal timing or telemetry requirement. PLAY remains keyboard-operable, accessible, and usable on narrow screens. It is text-first and information-rich, not visually empty. Complex 3D or cinematic presentation is not a requirement. Medium-high density and semantic color are required ([VISUAL-DESIGN.md](VISUAL-DESIGN.md)).

Administrative work is the explicit exception to the PLAY presentation rule: PLAY remains a text-first world interface, while authorized ADMIN surfaces MAY use graphical forms, tables, maps, charts, and dialogs when they improve visibility, safety, or error prevention. ADMIN controls MUST remain outside ordinary PLAY.

## Progressive disclosure

The same immutable evidence appears at four levels: (1) “Something interesting happened. Test it?”, (2) an intent question such as “Does communication matter?”, (3) advanced controls such as ablation, fork, seed, and runs, and (4) reproducibility records including IDs, digests, schema, controls, boundary, and audit ledger. Simple presentation must preserve limitations and an advanced-detail route; it must not invent explanations or hide claim labels.

## Authority

Machine translations are [`specs/experiment-intent-catalog.json`](../specs/experiment-intent-catalog.json), [`specs/experience-error-catalog.json`](../specs/experience-error-catalog.json), [`specs/capture-defaults.v05.json`](../specs/capture-defaults.v05.json), and [`specs/capture-status-catalog.json`](../specs/capture-status-catalog.json). CAPTURE projections must reference the same `captured_test_id` at every disclosure level. See [PLAY.md](PLAY.md), [WATCH.md](WATCH.md), [STUDY.md](STUDY.md), [Capture Intent Compilation](CAPTURE-INTENT-COMPILATION.md), [Experience terminology](EXPERIENCE-TERMINOLOGY.md), and [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md).


## Experience acceptance

A conforming experience proves all of the following:

1. A first-time user immediately identifies PLAY, WATCH, and STUDY.
2. A human enters PLAY without research terminology.
3. WATCH explains a significant visible event through a derived presentation.
4. A researcher launches a common test without editing schemas.
5. The selected intent deterministically resolves to a valid Lab-plan template.
6. Advanced users can inspect full experimental detail and overrides.
7. Simple results retain evidence limits and an advanced-detail route.
8. Canonical claim labels remain recoverable.
9. Presentation never mutates canonical world or research state.
10. PLAY and public WATCH do not expose hidden research metadata.
11. Internal system names are never required for ordinary flow completion.
12. Text and structured equivalents exist for every core path.
13. A researcher captures a READY result with one primary CAPTURE AS TEST action.
14. Simple capture cannot strengthen machine claim labels or invent global capability claims.
15. Capture failures surface plain-language status, reason, and next action without Compiler jargon.
16. Deep Time appears as age, scars, institutions, and incomplete local history — not lineage graphs by default.
17. Derived lore/presentation never overrides canonical historical evidence.
18. LEARN organizes reproduced behaviors without graph jargon or claim inflation.
19. PLAY is uncoupled from LEARN; no gameplay buffs, rankings, or research labels.
20. Ordinary human PLAY makes location, local significance, available action, and recent consequence legible without external documentation.
21. Human and agent Controllers remain peers for the same Player ontology; controller type is metadata, not a gameplay class.
22. Text commands and contextual controls share canonical action semantics, and unavailable or hidden actions are not presented as available.
23. A fresh human-controlled Player can complete the first-entry orientation/action/consequence/next-decision path without a literal time benchmark.
24. PLAY remains text-first but not text-only, with accessible information-rich projections, semantic color, and an explicit separate ADMIN register.
25. Player-facing presentation follows [PLAYER-BRAND.md](PLAYER-BRAND.md) and [VISUAL-DESIGN.md](VISUAL-DESIGN.md): game-first hierarchy, dual semantics, no research-dominant PLAY chrome.
