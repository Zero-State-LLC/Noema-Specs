# Command Discovery

**Authority.** First-world contract for how an **Agent Player** discovers what they can do. Humans do not inhabit ([RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md)). Structured `AVAILABLE_ACTIONS` is the production discovery path. Human `HELP` / forgiving parser, if retained, is **NON-CANONICAL DEV TOOLING**.

This is not a second command catalog. Canonical verbs, aliases, costs, and consequences remain [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) and [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).

Related: [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [PLAY.md](PLAY.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [EXPERIENCE.md](EXPERIENCE.md) · [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md).

---

## Principle

Onboarding happens through structured observation, `AVAILABLE_ACTIONS`, and progressive disclosure — not a tutorial wall.

```text
observation
  → WHERE / HERE / EXITS / STATUS / HAPPENED
  → AVAILABLE_ACTIONS
  → first meaningful action
  → visible consequence
```

Implementations MUST NOT generate new canonical verbs from theme, lore, or runtime content ([PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)).

---

## Agent Player discovery

First screen MUST make these answers available without an external manual:

```text
WHERE AM I?
WHAT IS HERE?
WHAT MATTERS HERE?
WHAT CAN I DO?
WHAT JUST HAPPENED?
```

Discovery layout (illustrative):

```text
AVAILABLE HERE
inspect relay
repair relay
move east

MORE
help
help trade
help organizations
```

| Term | First-world rule |
|---|---|
| `AVAILABLE HERE` | Derived `AVAILABLE ACTION`s for this observation. Required on first entry. |
| `MORE` / `help` | Bounded list of `KNOWN COMMAND`s and topics. MUST NOT dump the full dictionary on first entry. |
| `help <topic>` | Progressive disclosure for trade, organizations, movement, and similar known topics. |
| Contextual control | Same semantics as the matching command. |
| `UNSUPPORTED` | Omit. |
| `NOT_OBSERVABLE` | Do not reveal with a disabled control. |

`HELP` is client/interface only: no event, no cost, no world mutation.

Optional `QUERY` / `ASK` appear only if the deployment advertises them.

---

## Agent discovery

Structured agents MUST NOT parse the human command grammar.

They discover through:

```text
protocol negotiation
capability advertisement
AVAILABLE_ACTIONS
structured observations
```

First `OBSERVE` MUST NOT add a thesis or dump the full verb dictionary. Local `AVAILABLE_ACTIONS` only. [AGENT-ORIENTATION-S0.md](AGENT-ORIENTATION-S0.md).

Same canonical actions as humans. See [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md), [AGENT-HARNESS.md](AGENT-HARNESS.md), and [protocols/agent-protocol-v1.md](../protocols/agent-protocol-v1.md).

---

## Acceptance

1. A new human can find a meaningful available action from the first screen without a tutorial.
2. `help` does not dump the entire verb list.
3. Agents receive `AVAILABLE_ACTIONS` / capabilities, not MUD help text as a requirement.
4. Discovery never invents verbs or fake affordances.

---

## Non-goals

- A second action taxonomy
- Scripted quests
- Runtime-generated verbs

## Extension Points

Non-normative contextual-discovery and diagnostic seams.

- Extend AVAILABLE_ACTIONS presentation from authenticated observations, carrying only supported canonical actions, visible targets and known permitted preconditions. Progressive disclosure may group known topics but cannot reveal NOT_OBSERVABLE targets through disabled controls or invent thematic verbs.
- Interpret historical human-action examples and acceptance wording above under RFC-0120: human HELP/parser tooling is non-canonical, and only Agent Players inhabit. Controller enrollment does not itself make an action available; ACCESS S0–S3 are policy slices, not discovery privileges.
- Compatibility/promotion: pin PLAYER-ACTION-MAP/ACTION-CONTRACTS and retain structured discovery for agents without human-grammar parsing. Localization may change descriptions and help captions, not action identifiers, aliases or costs; new discovery views need projection-parity evidence before adoption.
- Verification proposal: compare first observation in quiet, permission-limited and target-absent rooms; assert no full dictionary dump, hidden target or thesis. HELP should emit no event or charge. Check stale affordance rejection and keyboard-readable diagnostic lists without creating a human gameplay submit path.
