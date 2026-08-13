# World Event Director (GC10)

**Status:** Product authority for bounded PLAY-world pressure. P2. Phase GC-D.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Named but unspecified in:** [GAME-DESIGN.md](GAME-DESIGN.md) · [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) · [INFRASTRUCTURE.md](INFRASTRUCTURE.md)  
**Distinct from:** [FRONTIER-DIRECTOR.md](FRONTIER-DIRECTOR.md) (research NOTICE) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) (control plane) · [INTERVENTIONS.md](INTERVENTIONS.md) (Lab taxonomy)

v0.1 already requires a small deterministic pressure schedule. This document is that missing authority. It does **not** implement Frontier, Lab perturbations, or Admin world-edit.

**Doctrine:** pressure changes existing conditions. A relay failure must propagate through movement, communication, trade, territory, conflict, institutions, and history — not open a relay-crisis minigame ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)).

---

## Thesis

The World Event Director (WED) applies **authorized, bounded, deterministic** condition changes so the world stays uncertain and the social machine stays under pressure.

Every perturbation MUST be:

```text
authorized
bounded
deterministic
logged
provenance-backed
replayable
auditable
```

It MAY alter conditions.

It MUST NOT force a desired Player response or research outcome.

```text
WED changes conditions
Players choose responses
Research observes divergence
```

---

## Authority split

| System | Mutates production world? | Purpose |
|--------|---------------------------|---------|
| World Event Director | Yes, conditions only, via cataloged pressure events | PLAY pressure |
| Frontier Director | Yes, conditions only, research-scheduled situations | NOTICE / information gain |
| Operator interventions | Control plane / recovery / pre-activation Genesis | Ops |
| Lab interventions | Isolated forks only | TEST |

If a pressure could be expressed as an existing scheduled degradation, prefer that. WED is the **named steward** of such schedules plus rare authorized injects.

First-world Admin Live MUST NOT expose WED as “spawn content” ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)).

---

## Operator authority

Who may activate a non-schedule pressure:

| Actor | Allowed |
|-------|---------|
| Versioned world schedule (seeded) | Yes — default Chamber pressure |
| Authorized operator with preview → confirm | Yes — bounded classes below |
| Player | No |
| LLM / free text | No |
| STUDY user | No (use Lab forks) |
| Frontier Director | Separate system; MUST NOT silently share WED IDs |

Activation path:

```text
preview (deterministic projected condition delta)
  → authorization check
  → activate
  → ledgered pressure event + audit receipt
```

Rollback: if the event class is marked reversible, a compensating event exists. If irreversible (scar, destroyed evidence access), rollback is **forbidden**; recovery is Player-facing (`RESTORE`, repair, rebuild).

---

## Allowed event classes (product)

Closed families. Exact type IDs are SPEC GAP (may reuse existing degradation / `SITUATION_INJECTED` patterns where already cataloged).

```text
resource scarcity
infrastructure failure
resource migration (node regen shifts rooms)
communication outage
artifact emergence (discoverable object, not a quest)
environmental shift (room/exit condition tags)
institutional crisis (dormancy pressure, not forced dissolution)
new discovery (makes an existing hidden-but-legal site more findable without leaking it in GUI)
unknown signal (uncertain public/local notice; not an oracle)
```

Forbidden:

- forced Player objectives;
- research-target labels in PLAY;
- granting resources to a favored Player;
- rewriting history;
- creating uncatalogued entities.

---

## Scope, duration, cooldown

| Field | Rule |
|-------|------|
| Scope | Named rooms, infrastructure IDs, resource nodes, or communication paths. No “the whole lore” |
| Duration | Finite cycles or until a cataloged repair/restore |
| Cooldown | Versioned per class so the Director cannot storm the world |
| Intensity | Integer bands; no float drama |

Starting-conditions mild schedule (pressure after a few cycles) remains the default Chamber behavior.

---

## Visibility

| Surface | Rule |
|---------|------|
| PLAY | World-native symptoms (shortage, dark relay, delayed messages). No “Event: Scarcity #4” exam language |
| WATCH | Public symptoms and public pressure events permitted by spectator policy |
| STUDY / research annotation | May label the pressure class in the research partition. MUST NOT leak that label into PLAY |
| Audit receipt | Operator/research: who authorized, preview digest, event ids, seed contribution |

---

## Replay

Seed + Director version + ordered activations determine all WED effects. Preview of the same inputs MUST match activation. Replaying the ledger without operator injects MUST NOT invent injects.

---

## SPEC GAP

```text
pressure catalog vs reuse of existing events
preview / receipt schema
schedule config (Chamber defaults)
authorization roles
fixtures: scarcity + divergent Player responses + replay
conformance: no forced outcome; PLAY has no research labels
rollback / irreversible handling table
```

Do not invent a second Frontier schema. If `SITUATION_INJECTED` can carry a WED class, prefer extension by RFC over a parallel catalog.

---

## Acceptance (scenario J)

An authorized operator (or the seeded schedule) introduces a bounded scarcity or relay outage. Different Players hoard, repair, trade, or relocate. The pressure is replayable. Research can observe the divergence. PLAY never sees a required “correct” response.
