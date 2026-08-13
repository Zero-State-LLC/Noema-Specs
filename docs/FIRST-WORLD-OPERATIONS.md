# First-World Operations

**Authority.** Operational envelope for NOEMA's first persistent production world: **Perihelion Reach**.

This document pins the approved candidate and shows where CREATE / RUN / PLAY / WATCH / STUDY / ADMINISTER / MAINTAIN / RECOVER / AUDIT are specified. It does not add gameplay, Genesis profiles, story seeds, or a second world.

Related: [GENESIS.md](GENESIS.md) · [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [WORLD-SERVICES.md](WORLD-SERVICES.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [OPERATIONS.md](OPERATIONS.md) · [PLATFORM.md](PLATFORM.md).

---

## Approved first world (do not change)

```text
World:
Perihelion Reach

world_id:
world.perihelion-reach

Profile:
FRACTURED_OLD_WORLD

Story Seeds:
OLD_TRADE_NETWORK
LOST_ARCHIVE

World Seed:
17011984

Approved Genesis ID:
genesis.ef578f4ffceeccd0

Approved Cycle 0 digest:
sha256:ec53fcdc38b7984e54f954c71bb73a863dfe33634a4c7581108a0cb1072b79a6
```

This is the first-world production candidate. Implementations MUST NOT substitute a different profile, seed pair, world seed, or genesis id and still call the result Perihelion Reach.

v0.6 conformance fixtures that use **Aster Reach** / `genesis.aster-reach.a` remain fixtures. They are not this production world.

PLAY MUST NOT expose the profile, story seeds, or world seed. Players inhabit the resulting world only ([GENESIS.md](GENESIS.md), [PLAY.md](PLAY.md)).

---

## What first-world operations must be able to do

```text
CREATE      Genesis preview → accept → activate this candidate
RUN         Host the activated world on the pinned platform
PLAY        Humans and agents enter as Players
WATCH       Spectators observe settled public projections
STUDY       Authorized research on isolated / consented paths
ADMINISTER  Admin Live + governed interventions
MAINTAIN    PAUSED windows, compatible deploys, verify
RECOVER     Incident classes, restore, fail closed
AUDIT       Ledgered events, intervention receipts, verify
```

If any of those verbs is ambiguous, the defect is in the cited document below — not a missing gameplay system.

First-play structure:

```text
ENTER
  ↓
WHERE AM I?
  ↓
WHAT MATTERS HERE?
  ↓
AVAILABLE HERE
  ↓
ACTION
  ↓
CONSEQUENCE
  ↓
NEXT DECISION
```

Discovery contract: [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md).

---

## Discoverability

Reuse existing authority. New documents exist only where deleting them would leave first-world operation unsafe or unimplementable.

```text
WORLD
├── Chamber                  CORE-GAME-LOOP, CHAMBER-MAP
├── Geography                GEOGRAPHY
├── Resources                RESOURCE-ECONOMY
├── Institutions             INSTITUTIONS
├── World Services           WORLD-SERVICES
├── Trade                    ACTION-CONTRACTS (TRADE)
├── Strategy                 STRATEGIC-CONFLICT, STRATEGIC-KNOWLEDGE
├── Deep Time                DEEP-TIME
└── Genesis                  GENESIS, GENESIS-PROFILES, STORY-SEEDS

PLAYER
├── Identity                 AUTH-AND-IDENTITY
├── Controllers              AUTH-AND-IDENTITY, AGENT-GATEWAY
├── PLAY                     PLAY
├── Player Action Map        PLAYER-ACTION-MAP
├── Dynamic Affordances      PLAYER-ACTION-MAP
├── Human Play               HUMAN-PLAY
├── Agent Play               AGENT-PLAY, AGENT-ONBOARDING
├── Player Lifecycle         PLAYER-LIFECYCLE
├── Onboarding               PLAYER-ONBOARDING
└── Command Discovery        COMMAND-DISCOVERY, PLAYER-ACTION-MAP

OBSERVATION
├── WATCH                    WATCH, SPECTATOR, SPECTATOR-ONBOARDING
├── Partial Observability    PARTIAL-OBSERVABILITY
└── Evidence / History       HISTORICAL-EVIDENCE, EVENT-CATALOG, REPLAY

RESEARCH
├── Frontier                 FRONTIER-DIRECTOR
├── Observatory              OBSERVATORY
├── Lab                      EXPERIMENT-LAB
├── Compiler                 PHENOMENON-COMPILER
└── LEARN                    LEARN

ADMIN / OPERATIONS
├── Admin Identity           AUTH-AND-IDENTITY, ADMIN-LIVE-OPERATIONS
├── Admin Live               ADMIN-LIVE-OPERATIONS
├── World Operations         WORLD-OPERATIONS
├── Player Management        PLAYER-LIFECYCLE, OPERATOR-INTERVENTIONS
├── Research Management      STUDY, RESEARCH-WORKFLOW (authorized)
├── Operator Interventions   OPERATOR-INTERVENTIONS
├── Backup / Restore         OPERATIONS
├── Evidence                 OPERATIONS (receipts), REPRODUCIBILITY
├── Audit                    ADMIN-LIVE-OPERATIONS, SECURITY-SEQUENCES
├── Incident Recovery        INCIDENT-RECOVERY
└── First-World Operations   this document
    └── Spec freeze              FIRST-WORLD-SPEC-FREEZE

PLATFORM
├── Cloudflare               PLATFORM
├── Durable Objects          PLATFORM
├── Supabase                 PLATFORM, AUTH-AND-IDENTITY
├── Auth                     AUTH-AND-IDENTITY
├── Settlement               PLATFORM, INCIDENT-RECOVERY
├── Security                 SECURITY, SECURITY-SEQUENCES
└── Deployment               DEPLOYMENT, OPERATIONS
```

---

## Pre-live checklist

Before production Genesis of Perihelion Reach, operators MUST be able to:

1. Preview the approved inputs and obtain Cycle 0 digest `sha256:ec53fcdc38b7984e54f954c71bb73a863dfe33634a4c7581108a0cb1072b79a6` for `genesis.ef578f4ffceeccd0`.
2. Confirm PLAY, WATCH, and Admin Live redaction (no profile / seed / story-seed IDs on Player or public WATCH).
3. Take a verify-passing backup.
4. Activate once; refuse ordinary reseed afterward.
5. Enter as a human-controlled Player and as an agent-controlled Player to the same world.
6. Run `noema verify` (or hosted equivalent) to `NOEMA VERIFY: PASS`.
7. Show Admin Live pulse for `ACTIVE` + healthy settlement.
8. Demonstrate `PAUSED` rejects mutating PLAY and resume returns `ACTIVE`.
9. Demonstrate settlement-bound fail-closed and ledger-mismatch `RECOVERY_REQUIRED` in a non-production rehearsal.

Activation remains a human operator decision. Specs do not auto-activate production.

---

## Hosted runtime pin

First-world hosted shape:

```text
Cloudflare Pages / Workers / Durable Objects
Supabase Auth / Postgres / Storage
one NoemaWorldDO for world.perihelion-reach
```

Local Chamber compose remains valid for offline conformance. It is not a second production world.

---

## Acceptance

1. The first production world identity is exactly the pin in this document.
2. Aster Reach fixtures are unchanged and non-authoritative for that pin.
3. CREATE through AUDIT each have a cited first-world authority.
4. No new gameplay system is required to operate the world.

---

## Non-goals

- v0.8 / new verbs / new Genesis profiles / new story seeds
- Multi-world orchestration
- Changing the approved candidate
- Treating rehearsal hosts as a second source of world truth
