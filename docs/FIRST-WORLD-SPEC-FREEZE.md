# First-World Specification Freeze

```text
NOEMA FIRST-WORLD SPECIFICATION

STATUS:
THAWED 2026-08-20 — test-build operator authorized continued implementation
RFC-0120 identity remains law. Core-loop v0.1–v0.7 still changes by RFC.
```

**Authority.** First-world operational freeze is **thawed** (2026-08-20). This is not the core-loop research freeze in [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md). RFC-0120 (only agents are Players) remains constitution.

```text
core-loop freeze
≠
first-world operational freeze
```

Related: [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md).

The [Game Completeness](GAME-COMPLETENESS-PLAN.md) campaign MAY now land on Perihelion when an RFC says so. This thaw does not itself add verbs, reseed, or expand rooms.

---

## Authority set

| Surface | Owner |
|---|---|
| Machine contracts | `specs/` + protocols |
| Action semantics | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) |
| Adapter / command crosswalk | [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) |
| PLAY experience | [PLAY.md](PLAY.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) |
| Headless agent play | [AGENT-HARNESS.md](AGENT-HARNESS.md) |
| Official client distribution | [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md) (architecture clarification; no gameplay thaw) |
| Player brand / visual presentation | [PLAYER-BRAND.md](PLAYER-BRAND.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md) · [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md) |
| Identity | [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) |
| World lifecycle | [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) |
| Admin observation | [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) (IA, redaction, observational default; not a new milestone) |
| Privileged mutation | [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) |
| Degraded / recovery | [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) |
| Perihelion pin | [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) |
| World Services | [WORLD-SERVICES.md](WORLD-SERVICES.md) |
| Operator Digests | [OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md) |
| This freeze | this document |

Do not create competing semantic ownership.

---

## Freeze scope

```text
Core loop v0.1–v0.7
Player ontology (agent-only; RFC-0120 unfreeze of this row only)
PLAY UX (Agent Player inhabit; hosted human PLAY retired)
Player Action Map
Stable action taxonomy
Dynamic affordances
Human Play (WATCH/CONNECT; inhabit retired — RFC-0120)
Agent Play
Headless Agent Harness (implementation-ambiguity closure; no new verbs)
Identity/Auth
Hosted platform
Genesis
Deep Time
Admin Live
World Operations
Player Lifecycle
Operator Interventions
Incident Recovery
Player Onboarding
First-World Operations
Perihelion Reach production pin
World Services
Operator Digests
Player brand / visual presentation (presentation only; does not thaw verbs)
```

Freeze does **not** mean every runtime adapter is complete. It means implementation follows settled authority rather than continuing product design.

---

## First-world pin (do not regenerate)

```text
World:
Perihelion Reach

Profile:
FRACTURED_OLD_WORLD

Story Seeds:
- OLD_TRADE_NETWORK
- LOST_ARCHIVE

World Seed:
17011984

Genesis ID:
genesis.ef578f4ffceeccd0

Cycle 0 digest:
sha256:ec53fcdc38b7984e54f954c71bb73a863dfe33634a4c7581108a0cb1072b79a6
```

These values are implementation/operations authority for the first production world. Aster Reach fixtures remain non-authoritative examples.

---

## What freeze means

New specification work before first live play is allowed only for:

```text
SPEC DEFECT
SECURITY DEFECT
DETERMINISM DEFECT
IMPLEMENTATION AMBIGUITY
OPERATIONAL BLOCKER
PROVEN PLAYER-USABILITY DEFECT
```

Do not reopen design because another feature would be interesting.

Player-facing brand and visual design ([PLAYER-BRAND.md](PLAYER-BRAND.md), [VISUAL-DESIGN.md](VISUAL-DESIGN.md)) closed an **IMPLEMENTATION AMBIGUITY** / **PROVEN PLAYER-USABILITY DEFECT** in presentation. That work does not thaw verbs, Genesis, or world rules. Frontend identity work follows those documents; it does not invent a new aesthetic during coding.

RFC-0120 closed a **SPEC DEFECT** / **SECURITY DEFECT**: constitution still treated humans as Players while hosted inhabit was already agent-only, and human JWT still resolved to a Player principal. That RFC unfreezes **Player ontology** and **Identity/Auth** only for that defect. It does not thaw verbs, Genesis, Perihelion Reach, or settlement.

---

## What freeze does not mean

The freeze does not prohibit:

```text
runtime implementation
bug fixes
tests
deployment work
UI implementation against existing authority
auth implementation
hosted action parity
Admin GUI implementation
operational verification
```

It prohibits uncontrolled expansion of product semantics before first-world evidence exists.

---

## Deferred (not rejected)

```text
v0.8
new canonical Player verbs
dynamic runtime verb generation
new Genesis Profiles
new Story Seeds
multi-world orchestration
market order book
complex government simulation
large procedural lore system
graph database requirement
microservices
dedicated streaming infrastructure
ORG_CREATE human org_id allocation rule
QUERY record-family expansion
ASK answer-linking
World Service replacement mechanics
Banker / shopkeeper / extra services
```

---

## Runtime handoff (non-normative)

Recommended order after freeze:

```text
1. merge Player UX readiness
2. production Player authentication
3. agent-controller enrollment/auth
4. hosted Tier 1 action parity
5. Admin Live implementation
6. world lifecycle / PAUSED support
7. settlement fail-closed bound
8. session takeover / lifecycle parity
9. production Genesis gate
10. explicit human activation
```

### Tier 1 hosted actions

```text
LOOK  MOVE  INSPECT  MESSAGE  WAIT  TRADE  HARVEST  REPAIR
```

Semantics remain [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) / [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).

### Tier 2 / 3 may lag hosted parity

```text
ORG_CREATE  ORG_MEMBER_ADD  ORG_MEMBER_REMOVE
CONTEST_DECLARE  CONTEST_DEFEND
AGREEMENT_FORM  AGREEMENT_TERMINATE
ACCESS_POLICY
```

Specs remain authoritative. Implementation lag does not remove them from the design.

---

## Acceptance

1. First-world implementation does not invent product, identity, ops, recovery, or admin behavior.
2. Further pre-launch Specs work is defect-driven only.
3. Next repository: `Zero-State-LLC/Noema`.
