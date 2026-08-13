# GC7 First Slice — Existing Contest Rhythm

**Status:** Executable specification. Not a runtime implementation.  
**Parent:** [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md)  
**Does not open:** `event-catalog/0.3` · new contest forms · `SCAN` / `ATTACK` · hit-point combat · character death · versioned withdraw

S0 is the smallest conflict increment that still satisfies scenario G’s *shape* (recon, commit, resolve, recover) by **composing** verbs and events that already exist in `event-catalog/0.2`. It does not rewrite [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md), [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md), or `action-contracts.v02.json`.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Second conflict canon | **REJECT.** Extend v0.2 |
| Mutate `event-catalog/0.2` | **REJECT.** Completeness plan forbids it here |
| Fifth contest form / information-target form | **DEFER** (SPEC GAP; needs its own RFC) |
| `SCAN` / `ATTACK` / HP bar | **REJECT.** No combat subsystem |
| Character death / irreversible underclass | **REJECT.** [LOSS-RECOVERY.md](LOSS-RECOVERY.md) |
| Versioned withdraw | **DEFER** |
| Contest UI names hidden entities | **REJECT.** Coarse public signals only |
| Block Chamber PLAY on GC7 | **REJECT.** Parent: implement v0.2 first; do not block first-world play |

Pressures: **scarcity** (stakes are reserved resources), **distance** (declare is co-located), **dependency** (defense, agreements, infra condition), **uncertainty** (score is not previewed as an oracle).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc7-s0` |
| Catalog | `conflict-catalog/gc7-s0` |
| Event catalog | `event-catalog/0.2` (unchanged) |
| Rules | `contest-rules/0.2.0` (unchanged) |
| Forms | The existing four only |

### Closed forms

```text
RESOURCE_SEIZURE
INFRASTRUCTURE_DISRUPTION
ACCESS_CONTEST
PRESENCE_PRESSURE
```

A fifth string is `FORM_FORBIDDEN`.

### Stage → existing verbs

| Stage | Allowed (closed) | Must not become |
|-------|------------------|-----------------|
| RECON | `LOOK`, `INSPECT` | `SCAN` |
| POSITION | `MOVE`, `ACCESS_POLICY` | Teleport / engage |
| PRESSURE | `TRADE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` | Auto-damage aura |
| COUNTER | `CONTEST_DEFEND`, `REPAIR`, `AGREEMENT_FORM`, `MOVE` | Perfect parry stat |
| ESCALATE | `CONTEST_DECLARE`, `AGREEMENT_FORM` | Unavoidable war flag |
| COMMIT | `CONTEST_DECLARE` | Character death |
| RESOLVE | `CONTEST_RESOLVE` (world/scheduler, not a Player verb) | Real-time HP |
| RECOVER | `REPAIR`, `TRADE`, `HARVEST`, `MOVE`, `ORG_MEMBER_ADD`, `AGREEMENT_FORM` | Permanent underclass |

`CONTEST_RESOLVE` remains the existing world/scheduler operation. Players do not gain a `RESOLVE` command.

A legal contest need not visit every stage. S0 proves the full rhythm **can** be composed from this table. Isolated `CONTEST_DECLARE` → `CONTEST_RESOLVED` remains the v0.2 package.

### Events (existing only)

| Moment | Types |
|--------|-------|
| Commit | `CONTEST_DECLARED` |
| Resolve | `CONTEST_RESOLVED` then coupling follow-ons already named in [STRATEGIC-EVENT-COUPLING.md](STRATEGIC-EVENT-COUPLING.md) |

No `HIT` / `DAMAGE` / `DEATH` / `SCANNED` types.

### Projection

WATCH / contest notices may show public form, public target when that target is already observable, and banded stakes. They MUST NOT include hidden entity ids, private holdings, `known_truth_relationship`, or HP.

### Arithmetic

Unchanged. Implementations MUST use [CONTEST-RESOLUTION.md](CONTEST-RESOLUTION.md). This slice does not retune millipoints.

---

## A–J

| Test | Result |
|------|--------|
| A | Resource + asset + location + organization + agreement + information. No HP primitive |
| B | All four pressures |
| C | No extra Player commands; `CONTEST_RESOLVE` stays world-side |
| D | Couples to infra, trade, access, crime, recovery |
| E | Verb-stable |
| F | A repair-and-agreement habit can form after loss without a war engine |
| G | `CONTEST_*` events remain attributable |
| H | Human and agent Players use the same forms |
| I | Meaningful with research hidden |
| J | Without this, v0.2 is a package with no playable rhythm pin |

---

## Out of S0

```text
event-catalog/0.3
fifth contest form / information-target form
SCAN ATTACK HIT KILL
HP / health bars
character death
versioned withdraw
institution-as-party details
Chamber PLAY advertising CONTEST as required first-world help
```

---

## Runtime rule

This document does not thaw first-world Chamber contest play. Hosted `CONTEST_DECLARE` remains outside the required first-world verb set until an implementation pass is authorized. Do not block Genesis PLAY on GC7.

## Acceptance (narrower than scenario G)

1. A RECON→RECOVER sequence that only uses the stage table is accepted.
2. `ATTACK` / `SCAN` is `VERB_FORBIDDEN`.
3. A fifth form string is `FORM_FORBIDDEN`.
4. A contest projection containing `hidden` is `LEAK`.
5. `character_dead` is `DEATH_FORBIDDEN`.

Full scenario G (two groups, economic pressure, skillful recovery) remains a later composition of this table plus existing v0.2 trajectories.
