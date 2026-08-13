# Mastery and Specialization (GC1)

**Status:** Product authority for Player mastery. P0. Phase GC-A.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [PROGRESSION.md](PROGRESSION.md) · [AMBITIONS.md](AMBITIONS.md)  
**Must not become:** [CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md) · [LEARN.md](LEARN.md) · [CAPABILITY-CANDIDATES.md](CAPABILITY-CANDIDATES.md)

This document is **not** an executable package. The first implementable slice is [GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md) under Draft [RFC-0004](../rfcs/RFC-0004-derived-mastery-projection.md). Recognition, benefits, and new events remain **SPEC GAP**.

---

## Thesis

A Player becomes somebody by **demonstrated practice**, not by selecting a class or accruing a global score.

```text
repeated world-native work
  → proficiency evidence
  → recognized specialization
  → richer affordances under the same verbs
```

Forbidden:

```text
one XP bar
one intelligence / consciousness score
research capability confidence as a Player stat
class selected at entry that locks the verb set
```

---

## Settled product answers

| Question | Settlement |
|----------|------------|
| Selected, earned, inferred, or hybrid? | **Hybrid.** Proficiency is **inferred** from demonstrated activity. Specialization **emerges** when evidence crosses a versioned threshold. A Player MAY declare a **focus** (soft intent). Focus is not a class lock and grants no verbs. |
| Can one Player hold several? | **Yes.** Multiple recognized specializations are legal. A bounded active-focus set (versioned; recommended 1–3) receives maintenance credit. Others decay more quickly. |
| What prevents one optimal specialization? | Opportunity cost, maintenance, local geography, diminishing returns across too many tracks, and complementary interdependence ([ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)). |
| Can competence degrade? | **Yes, slowly.** Inactivity reduces proficiency toward a floor of historical evidence. Short sessions MUST still contribute. Decay MUST NOT erase historical recognition records. |
| Can institutions recognize competence? | **Yes**, as institutional memory or office eligibility ([INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md), [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)). Recognition is not automatic class grant. |
| Can Players teach or certify one another? | **Teach:** joint work and records can produce evidence for the learner. No instant skill transfer. **Certify:** only an institution with that bounded authority may issue a recognition record. Private boasts are messages, not world competence. |
| Canonical vs derived? | **Evidence is canonical** (ledgered actions and resulting records). **Proficiency aggregates are rebuildable derived state** unless a later RFC proves a canonical cache is required for replay cost. **Recognition records** (institutional or emergent labels) are canonical once issued. |
| How does mastery affect affordances without exploding verbs? | Same verbs; richer **parameters**, **success quality**, **cost bands**, **access to restricted targets**, and **authority eligibility**. |

---

## Proficiency identity

A **proficiency track** is a named practice dimension grounded in existing or later canonical actions.

A track is **not** a Player class. It has:

| Field | Meaning |
|-------|---------|
| `track_id` | Stable machine identity (versioned catalog) |
| `practice_family` | Conceptual family from [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) |
| `evidence_classes` | Which successful (and optionally failed) actions count |
| `visibility` | What the Player, others, institutions, WATCH, and STUDY may see |

Candidate labels (examples, **not** a frozen class list):

```text
Surveyor
Broker
Archivist
Logistician
Mediator
Engineer
Explorer
Strategist
Steward
Investigator
Diplomat
Operator
```

These names MAY be used as **recognition labels** when evidence supports them. An implementation MUST NOT treat the list as a closed character-creation menu. A later catalog MAY add, split, or retire labels without adding verbs.

---

## Evidence required

Countable evidence MUST be world-native and already (or later) ledgered. Examples:

| Track (example) | Evidence classes |
|-----------------|------------------|
| Explorer | Distinct rooms observed; hidden or condition-gated exits discovered |
| Surveyor | Repeated `INSPECT` of nodes, infrastructure, routes; recorded estimates later confirmed |
| Engineer | Successful `REPAIR`; later construction/upgrade ops ([CONSTRUCTION.md](CONSTRUCTION.md)) |
| Broker | Completed `TRADE` as proposer or acceptor; failed-but-legal negotiations do not count as success |
| Logistician | Movement of traded or harvested lots across rooms/routes |
| Archivist | Documents created, archives inspected, reconstructions contributed |
| Diplomat | Formal agreements formed and kept; mediated membership or access |
| Strategist | Contests declared/defended with recovery; no reward for suicide rushes |
| Steward | Infrastructure kept above a condition band; institutional custodianship |
| Investigator | Contradictions examined via ordinary `INSPECT` / archive access |
| Mediator | Successful dispute-adjacent agreements without being a contest party |
| Operator | World Service desks used to complete Player-confirmed canonical actions |

Failed actions MAY count as **practice attempts** at a lower weight if and only if they were legal attempts (not `FORBIDDEN` spam). Exact weights are **SPEC GAP**.

Research observations, Lab results, LEARN edges, and capability candidates are **never** mastery evidence.

---

## Lifecycle

```text
UNTRACKED
  → PRACTICING          (evidence exists, below recognition)
  → RECOGNIZED          (emergent or institutional label)
  → MAINTAINED          (recent qualifying work)
  → LATENT              (below maintenance; historical label remains)
  → (optional) REVIVED  (new qualifying work restores MAINTAINED)
```

| Transition | Gate (product) | Numeric pin |
|------------|----------------|-------------|
| UNTRACKED → PRACTICING | First qualifying success | SPEC GAP |
| PRACTICING → RECOGNIZED | Versioned evidence threshold + not a single-cycle spike | SPEC GAP |
| RECOGNIZED → MAINTAINED | Default on recognition | — |
| MAINTAINED → LATENT | No qualifying work for a versioned inactivity window | SPEC GAP |
| LATENT → MAINTAINED | New qualifying work | SPEC GAP |

A declared **focus** does not skip PRACTICING. It MAY slightly reduce the inactivity window for that track (versioned). It MUST NOT grant recognition.

---

## Decay and short sessions

- Decay applies to **derived proficiency**, not to the event ledger.
- Historical recognition (“was recognized as Surveyor in Cycle 80”) remains evidence.
- A Player who acts once every several cycles MUST still accumulate evidence.
- Decay MUST be slow enough that a human session of ordinary length is net-positive if it contains qualifying work.
- There is no death-of-competence: floors are historical, not zeroed identity.

---

## Specialization emergence and visibility

Emergence is **inferred**, then optionally **recognized**.

| Audience | What they may see |
|----------|-------------------|
| Self (PLAY) | Own practicing/recognized/latent labels; coarse own-track standing; never research scores |
| Other Players | Only **public** recognition or what they have evidence to infer (repeated observed work). No hidden proficiency leak |
| Institution | Recognition it issued, plus evidence it is authorized to hold |
| WATCH | Public recognition events and public work, never private track totals |
| STUDY | May capture trajectories of practice. MUST NOT project research capability confidence as a Player stat |

GUI / HELP MUST NOT reveal a hidden specialization an observer could not know from the current observation ([PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) `NOT_OBSERVABLE`).

---

## World-native benefits and limits

Benefits (closed families; exact magnitudes SPEC GAP):

| Benefit family | Example | Verb impact |
|----------------|---------|-------------|
| Quality | Repair restores more condition; survey estimates tighter | Same `REPAIR` / `INSPECT` |
| Cost band | Slightly lower energy/attention on practiced work | Same verb, versioned cost table |
| Parameter access | Engineer may attempt a harder upgrade parameter once GC2 exists | Same verb + parameter |
| Target access | Archivist may `INSPECT` a restricted archive class they are authorized for | Authority + target, not a new verb |
| Eligibility | Office or contract requires recognized track | [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) |

Limits:

- Benefits NEVER unlock a new wire verb.
- Benefits NEVER bypass authorization, visibility, or budgets.
- Benefits NEVER read hidden information the Player has not earned.
- A recognized Broker is not automatically wealthy. A recognized Strategist is not automatically a contest winner.

---

## Cross-specialization interaction

Complementary tracks SHOULD create interdependence (acceptance H). A lone Player MAY practice several tracks and remain viable, but peak outcomes SHOULD favor exchange with others ([GAME-BALANCE.md](GAME-BALANCE.md)).

Conflicting tracks are not forbidden. Reckless contest behavior MAY produce social-memory descriptors that make diplomatic recognition harder ([SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)). That is coupling, not a class restriction.

---

## Human / agent parity

Controller type is not a caste. A human and an agent who perform the same qualifying work under the same world state MUST accumulate equivalent evidence. Faster agent action rates remain bounded by existing budgets and scheduler rules ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [SCHEDULER.md](SCHEDULER.md)).

---

## Deep Time

- Evidence and recognition records persist beyond the Player’s presence.
- Successors do **not** inherit proficiency scores.
- Teaching and institutional certification are the only legal transfer paths, and they create **new** evidence for the learner.
- Historical labels may appear in archives and reports without rewriting the ledger ([DEEP-TIME.md](DEEP-TIME.md)).

---

## Event production

Preferred first implementation: **no new catalog types**. Rebuild proficiency from existing events (`LOOK`, `INSPECT`, `HARVEST`, `REPAIR`, `TRADE_*`, org and contest events).

Candidate later events (RFC required; no silent `event-catalog/0.3`):

```text
PROFICIENCY_REBUILT          (derived, maybe not a world event)
SPECIALIZATION_RECOGNIZED    (public or institution-scoped)
SPECIALIZATION_LATENT
FOCUS_DECLARED               (if focus is ledgered)
```

Until accepted, implementations MUST NOT emit uncatalogued world events.

---

## Replay, idempotency, migration

| Concern | Rule |
|---------|------|
| Replay | Derived proficiency MUST rebuild identically from seed + ordered events + versioned catalog |
| Idempotency | Replayed actions MUST NOT double-count |
| Failure | Illegal or budget-failed actions do not grant success evidence |
| Migration | A new track catalog version MUST declare how old evidence maps; unmapped evidence stays historical and uncounted |
| Version behavior | Track catalog ID is part of replay identity |

---

## PLAY / WATCH / research / security

| Surface | Rule |
|---------|------|
| PLAY | Show own practice and public recognitions in world language (“known as a careful surveyor”), never XP |
| WATCH | Public recognitions and public work only |
| STUDY | Trajectories of practice are capturable; no Player-facing research score |
| Security | Private track totals are Player-private. Affordances MUST NOT leak others’ hidden proficiency |

---

## SPEC GAP

### Closed for GC1-S0 ([GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md))

```text
S0 track ids (explorer, surveyor, broker, engineer)
derived-only (not WorldState)
focus disabled
benefits disabled (magnitude = 0)
no new event types
S0 PLAY lines
WATCH = none
PRACTICING at count >= 1; recognition disabled
```

### Still open (blocks GC1-S1 and any mechanical benefit)

```text
recognition thresholds and anti-spike rule
decay / latent windows
focus as ledgered declaration (if ever)
benefit magnitudes
event types if recognition is ledgered
JSON catalog + schema
fixtures and conformance (recommended M01)
S1 PLAY/WATCH recognition strings
```

An implementation MAY ship GC1-S0 derived self-lines after RFC-0004 is Accepted. It MUST NOT ship recognition or mechanical benefits until those remaining gaps are closed.

---

## Acceptance (scenario A)

A Player enters without a class, repeats `INSPECT` / `REPAIR` / `TRADE` work, crosses a recognition threshold, and gains a quality or eligibility benefit under the same verbs, with no global intelligence score and no research metric on the PLAY surface.
