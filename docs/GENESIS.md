# World Genesis (v0.6)

## Purpose

Genesis is a **bounded, admin-only, one-time world-creation operation**. It produces a valid Cycle 0 NOEMA world with enough inherited texture for PLAY, then permanently gets out of the way.

```text
WORLD SEED
  → GENESIS PROFILE
  → optional STORY SEEDS
  → bounded prehistory generation
  → CYCLE 0 SNAPSHOT
  → ACTIVATE
  → normal Chamber + Deep Time runtime
```

Genesis is **not** a gameplay system, player surface, agent API, background service, or always-running subsystem.

## Complexity rule

> Prefer the smallest architecture that preserves the intended behavior.

Do not add subsystems, schemas, version domains, services, workflows, state machines, or catalogs unless omitting them leaves real implementation ambiguity.

## Access invariant (normative)

Only an authorized **ADMIN / operator** may:

- create a world
- select Genesis Profile and Story Seeds
- set or generate `world_seed`
- override permitted Genesis defaults
- run Genesis / regenerate before activation
- accept/reject generated Cycle 0
- activate the world

**Players, spectators, researchers, and agents MUST NOT invoke or modify Genesis.**

Reuse the simplest existing admin/operator authorization. Do not create a separate Genesis permissions platform.

| Role | Genesis |
|---|---|
| ADMIN | configure, preview, regenerate, activate |
| PLAYER | play resulting world only |
| AGENT | play resulting world only |
| SPECTATOR | watch resulting world only |
| RESEARCHER | study behavior; no Genesis mutation via STUDY alone |

## Administrative lifecycle

```text
ADMIN → CREATE WORLD → choose profile → optional story seeds
  → generate seed → PREVIEW → ACCEPT → ACTIVATE WORLD → CYCLE 0
```

`PREVIEW` is a Genesis step. It is **not** a `World.status` value. After activation, live status is `ACTIVE` / `PAUSED` / `INCIDENT` / `ARCHIVED` ([WORLD-OPERATIONS.md](WORLD-OPERATIONS.md), [WORLD-ENGINE.md](WORLD-ENGINE.md)). First production candidate: [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md).

After activation:

```text
Genesis configuration = immutable
```

- Regeneration before activation with changed claim-bearing inputs → **new `genesis_id`**
- Do not silently overwrite an accepted Genesis result
- Genesis **cannot** be rerun against an active world
- Another Genesis run after activation = **another world**

## Inputs (primary)

```text
world_seed
genesis_profile
story_seeds[]
```

Plus ordinary version/provenance fields required for determinism (`deep-time/0.6`, chamber world rules, `noema-jcs/1`).

## Prehistory representation (chosen)

```text
Genesis history records (bounded, content-addressed)
  → Cycle 0 settlement into ordinary world seed / snapshot
  → ordinary event ledger thereafter
```

Reuse Chamber mechanics for resources, infrastructure, orgs, ownership, and Deep Time contracts for institutions, artifacts, scars, and names. No Genesis-specific duplicates.

Bounded process only: short deterministic transitions or predeclared historical templates executed through canonical mechanics. **No** long-running prehistory simulation, Genesis actor ecology, or separate scheduler.

## Cycle 0 output

One ordinary valid NOEMA world state (reuse [`world-seed`](../specs/world-seed.schema.json) / world-state / snapshot contracts). May include: resource distribution, working/damaged infrastructure, ruins, active/dormant institutions, historical artifacts, old relationships, historical names, incomplete knowledge, unresolved tensions.

No special Genesis-only live state may remain after activation. Cycle 0 MUST pass normal world validation.

Machine result: [`genesis-result.schema.json`](../specs/genesis-result.schema.json).

## Determinism

Same `(world_seed, genesis_profile, story_seeds, rules versions)` → same Cycle 0. No hidden randomness.

## Player / WATCH / STUDY boundaries

- PLAY never exposes profile, story seeds, world seed, regeneration, or Cycle 0 acceptance. Players see consequences only.
- **WATCH** may show derived world age / known sites / surviving institutions — not admin Story Seeds or undiscovered history.
- **STUDY** may analyze behavior; Genesis inputs are world provenance only when authorized and MUST NOT be hidden “what to discover” hints.

## Lore boundary

```text
taxonomy ≠ story seeds ≠ simulated prehistory ≠ lore
```

Genesis provides historical material. Final lore is later/derived. See [DEEP-TIME.md](DEEP-TIME.md).

## Deferred (explicit)

complex Genesis actors · large historical populations · long-running prehistory · story-seed constraint solver · NL seed compiler · procedural lore · full cultural/semantic evolution · Genesis service/DB/workers/APIs · player/agent Genesis endpoints.

## Related

[Genesis Profiles](GENESIS-PROFILES.md) · [Story Seeds](STORY-SEEDS.md) · [Deep Time](DEEP-TIME.md) · [RFC-0003](../rfcs/RFC-0003-deterministic-contract-hardening.md)
