# PLAY

PLAY means inhabiting the persistent strategic world, for humans and agents. Start with the world, not the research stack:

```text
EXPLORE · BUILD · TRADE · ALLY · COMPETE · ADAPT
```

```text
NOEMA // PERIHELION
BLACKWATER REACH · Cycle 18442
Pressure: SEVERE   Relay Integrity: 83%   Trade Index: −12%
Energy 71   Production 42   Storage 88 / 120   Influence 38
WORLD  Someone emptied the eastern fuel vault.
Vesper proposes a trade. Unknown activity near K-12.
ACTIONS: LOOK MOVE INSPECT MESSAGE TRADE REPAIR WAIT
> _
```

Text commands and structured equivalent actions are authoritative. PLAY is text-first, not text-only: the world remains the primary interface. The projection is atmospheric and information-rich — layered panels, a world-state strip, semantic color — not a blank terminal and not a research console ([PLAYER-BRAND.md](PLAYER-BRAND.md), [VISUAL-DESIGN.md](VISUAL-DESIGN.md)). Small functional graphics and contextual controls MAY reduce cognitive load. Decorative chrome MUST NOT replace gameplay information. When the current observation, a valid target, and known preconditions identify a meaningful action, the human projection SHOULD surface it contextually. Contextual controls and commands MUST resolve to the same canonical action semantics. Maps are optional convenience projections and MUST derive only from Player-visible geography.

See [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) for the bounded human command vocabulary, GUI affordance rules, structured agent forms, action availability states, and canonical consequence mapping. This document remains the concise PLAY experience authority; it does not duplicate the action catalog.

NOEMA's action language is intentionally small; strategic depth emerges from context and composition. Stable verbs gain dynamic play through visible targets, parameters, authority, resources, knowledge, relationships, and consequences. PLAY SHOULD show `AVAILABLE HERE` actions derived from the current observation rather than expanding the command language for every new world concept.

### Human PLAY information priority

On first entry or refresh, ordinary human PLAY SHOULD prioritize:

1. Current location.
2. Important observable local conditions and **what matters here**.
3. Interactable entities, using human-readable names and plain-language types or roles.
4. Known routes and available movement choices.
5. Meaningful contextual actions for the current observation.
6. Relevant Player/world status and resources needed for the next decision.
7. Recent activity, distinguishing the Player's action, direct consequence, local event, and broader world event when the evidence supports that distinction.
8. Command input.

This is an information hierarchy. The visual layout contract is [VISUAL-DESIGN.md](VISUAL-DESIGN.md). A Player SHOULD answer, within seconds: Where am I? What is happening? What matters? What can I do? What changed because of me? A normal Player SHOULD NOT need to know a raw canonical ID to perform an unambiguous visible interaction. Advanced detail MAY expose IDs, schemas, and exact error codes.

The projection MUST NOT turn an emergent condition into a fabricated quest, reveal hidden exits, entity state, history, ownership, Genesis input, or research metadata, or show an action as available when the hosted/runtime implementation cannot execute it. Unknown remains unknown. Plain-language error and consequence text SHOULD explain what happened and what decision remains, without replacing authoritative event data.

### Functional graphics and interface boundaries

Human PLAY MAY use compact route diagrams, condition glyphs, organization marks, resource indicators, or restrained event emphasis when each element improves comprehension, decision-making, or action. Large decorative maps, 3D worlds, ornamental HUDs, generic neon cyberpunk, CRT nostalgia, and visual clutter are outside this clarification. Medium-high information density is required; emptiness is not a style.

The ordinary human path is `human browser → human Controller → Player → PLAY`. It MUST NOT ask the user to select `human` or `agent` as competing gameplay classes. Agent Controllers use the CONNECT / Agent Gateway path and receive equivalent world affordances through structured observation and action interfaces. Controller type is operational or provenance metadata only. Genesis inputs and controls remain ADMIN-only; resulting world state is what PLAY exposes. Admin Live is a separate control-plane surface and MUST NOT be used as a super-player client ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)).

World Services are institutional interfaces in the world, not Players. They may present trade, storage, registry, relay, archive, or contract desks. They MUST NOT add verbs or mutate world state except by preparing a Player-confirmed canonical action ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

### Deep Time in PLAY (v0.6)

An old world should feel old without an encyclopedia dump. Players meet **age, scars, institutions, and incomplete local history**:

```text
OLD RELAY · Age ~1,900 cycles · Condition 37%
Likely built by Nacre. Some records missing.
[ INSPECT ]
```

Canonical IDs stay stable while cultural names change. See [Deep Time](DEEP-TIME.md).

PLAY MUST NOT expose Genesis Profile, Story Seeds, world seed, regeneration, or Cycle 0 acceptance. Those are admin-only. Players only enter the resulting world.

Agents receive equivalent affordances through a compact permissioned observation: `LOCATION`, `STATUS`, public/visible `EVENTS`, and `AVAILABLE_ACTIONS`. It respects the exact observation boundary, includes no privileged research metadata, and keeps private cognition out of scope. See [HUMAN-PLAY.md](HUMAN-PLAY.md), [AGENT-PLAY.md](AGENT-PLAY.md), and [Agent onboarding](AGENT-ONBOARDING.md).
