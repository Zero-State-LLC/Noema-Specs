# Notion ↔ Specs Reconciliation (2026-08-13)

**Status:** Cross-cutting assimilation authority. Not a release tag. Not v0.8.  
**Companion to:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) · [PLATFORM.md](PLATFORM.md) · [ARCHITECTURE.md](ARCHITECTURE.md)  
**Does not replace:** GC1–GC10 first slices, frozen v0.1–v0.7 machine contracts, or subsystem owners listed below.

This pass reconciles accumulated Notion doctrine with the current repository. It is **specification assimilation and drift-repair**, not a runtime implementation and not a platform migration.

```text
Architecture-design frontier PAUSED after this document.
Next frontier when explicitly resumed:
canonical reducer registry + mutation ownership map.
```

Do not continue into new architecture doctrine from this file.

---

## Hosted stack (unchanged)

```text
Cloudflare Pages + Workers + Durable Objects
Supabase Auth + PostgreSQL + Storage
```

Do not propose Render, Vercel, Convex, Redis, Kafka, Kubernetes, a separate game-server fleet, or another database here. An infrastructure change requires proof that this stack cannot satisfy a required invariant.

### Complementary authorities (the material repair)

```text
DO (NoemaWorldDO)
= authoritative coordinator for active live ordering and process execution

POSTGRES
= durable canonical record required to reconstruct, recover, audit, and continue the world
```

A valid world commitment, reservation, agreement, authority grant, settled state transition, or scheduled semantic obligation MUST NOT exist only in unrecoverable DO-local memory.

The world may execute through a DO. Durable canonical commitments and settled truth must be persisted in Supabase. Bounded fail-closed persistence backlog remains [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Queues and alarms wake settlement; they are not the sole record of future semantic obligations.

```text
CACHE ≠ TRUTH
RESEARCH STORE ≠ TRUTH
TRANSIENT DO MEMORY ≠ SOLE DURABLE TRUTH
UI ≠ RULE ENGINE
```

---

## Audit matrix

| Doctrine | Verdict | Existing owner | Action |
|----------|---------|----------------|--------|
| A Core completeness / five loops | ALIGNED | [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md), [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md), GC1–GC10 | Preserve |
| B Complexity / primitives / pressures | ALIGNED | [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) | Preserve |
| C Human–agent social parity | ALIGNED | [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md), [CONTEXT.md](../CONTEXT.md) | Preserve; restated below |
| D Labor / employment / delegation | PARTIAL | [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md), [DIPLOMACY.md](DIPLOMACY.md), GC4-S0 | Doctrine here. No `EMPLOYMENT` engine |
| E Law / arbitration | PARTIAL | [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), GC7-S0, [DIPLOMACY.md](DIPLOMACY.md) | Doctrine here. No court engine |
| F Privacy / knowledge pathways | PARTIAL | [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md), [OBSERVATION.md](OBSERVATION.md), ADR-002 | Doctrine here. No new surveillance subsystem |
| G Epistemic decay | PARTIAL | [HISTORICAL-DECAY.md](HISTORICAL-DECAY.md), [LORE-BOUNDARY.md](LORE-BOUNDARY.md), GC9-S0 | Doctrine here |
| H Measurement without contamination | ALIGNED | [RESEARCH-METHOD.md](RESEARCH-METHOD.md), GC10-S0, LEARN | Preserve |
| I Operator governance | PARTIAL | [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md), [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) | Receipt fields here. Do not replace the four first-world classes |
| J System invariants | PARTIAL | RFC-0003, ADRs, [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) | Consolidated here |
| K Canonical action algebra | FROZEN_VERSION_BOUNDARY | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) | Forward candidate only. No enum rewrite |
| L Player action contract / REJECTED≠FAILED | PARTIAL / FROZEN_VERSION_BOUNDARY | ACTION-CONTRACTS, WORLD-ENGINE | Forward distinction. Keep `*_REJECTED` event names |
| M Event taxonomy / receipts | PARTIAL | [EVENT-CATALOG.md](EVENT-CATALOG.md) | Conceptual families. No catalog 0.3 |
| N State / projection / hosted split | CONFLICT (unqualified DO=truth) | ARCHITECTURE, PLATFORM | **Repaired** in this pass |
| O Aggregate / concurrency | MISSING as a map | implied by WORLD-ENGINE / DATA-MODEL | Doctrine here. No new tables |
| P World time / scheduler | PARTIAL | [SCHEDULER.md](SCHEDULER.md), [GAME-CYCLE.md](GAME-CYCLE.md) | Clarified here |
| Q Canonical schema spine | PARTIAL | [DATA-MODEL.md](DATA-MODEL.md) | Conceptual mapping. No Class/XP/Quest tables |
| R Invariant enforcement map | MISSING as a table | scattered | Table here |

Future economy (crypto, x402, wallets, `$NOEMA`, external settlement): already **DEFER** in [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md). Unchanged.

---

## Cross-cutting doctrine (A–R, compact)

### A. Completeness

Five nested loops remain those in [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md). GC1–GC10 first slices stay the executable specification pins.

> The real benchmark is not whether an agent can win Noema. It is whether an agent can become somebody inside Noema.

### B. Complexity

[COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) remains the rejection test: causes not industries; seven primitives; four pressures; noun emergence, verb stability.

### C. Social parity

```text
PLAYER = canonical world actor
CONTROLLER = human / agent / hybrid implementation of agency
20 subagents ≠ 20 Players
```

Controller type may be socially visible. It does not change authority or mechanics. Natural language never silently mutates the world.

### D. Labor / delegation

A Player can owe work or hold an office without becoming property.

```text
PLAYER IDENTITY ≠ EMPLOYMENT ≠ ROLE ≠ DELEGATION ≠ OWNERSHIP
```

Model work as Agreement + obligation + optional GC4 grant + duration + exit rule. Resignation revokes authority. Do not add an employment industry.

### E. Law / arbitration

```text
CANONICAL FACTS ≠ LEGAL INTERPRETATION ≠ SOCIAL JUDGMENT
```

Arbitration is delegated authority, not an omniscient court. No universal crime/morality score. Precedent starts as Information.

### F. Privacy / knowledge

```text
CANONICAL TRUTH ≠ KNOWN ≠ ACCESSIBLE ≠ OBSERVABLE ≠ PUBLIC
```

Every Player-visible fact must answer: *why does this Player know this?* Valid: observed, received, accessed, shared, canonically intercepted, inferred. Invalid: “because the backend knows it.”

### G. Epistemic decay

```text
HISTORY ≠ ACCESSIBLE RECORD ≠ LIVING KNOWLEDGE
```

The ledger does not forget. Civilizations can. Research must not auto-rescue lost gameplay knowledge.

### H. Measurement membrane

Research observes traces, not conclusions. No universal intelligence score. Research labels never mutate world state ([GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md)).

### I. Operator causation

```text
PLAYER CAUSATION ≠ SYSTEM CAUSATION ≠ OPERATOR CAUSATION
```

First-world intervention *classes* stay [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md): `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY`.

Causal *receipt* fields for a consequential operator action:

```text
operator action id · actor · time/cycle · class · reason
target · pre/post refs · authority · incident/experiment ref
```

Map receipt “class” onto the existing four; do not invent a second closed taxonomy. World Steward ([WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md)) changes conditions, not desired Player behavior.

Rollback repairs invalid state, not undesirable history.

### J. Invariants (families)

Identity: IDs immutable; Player ≠ Controller ≠ Account; Institution ≠ current officers; forks are new identities.  
Rights: ownership ≠ control ≠ access ≠ beneficiary; no delegation escalation; text claims never create authority (GC4-S0).  
Economy: no unexplained create/destroy; no double commitment; reservations conserved.  
Time/events: monotonic world time; settled actions final; append-only semantic history; version-aware replay.  
Epistemic: claim ≠ fact; visibility ≠ authority; research never leaks into PLAY.

```text
SAME INITIAL STATE + SAME VALID INPUT EVENTS + SAME RULE VERSIONS = SAME WORLD
```

### K. Action algebra (forward only)

Frozen wire verbs for frozen versions stay [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md). Human aliases (`REPAIR`, `HARVEST`, …) already map through [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md).

Do not add BETRAY, LIE, TRUST, BANK, COURT, TEACH, SPY as canonical verbs.

### L. Action contract / REJECTED ≠ FAILED

Forward distinction:

```text
REJECTED = never validly entered the world (normally no mutation)
FAILED   = valid committed action reached non-success (may consume and inform)
```

v0.1/v0.2 already emit `MOVE_REJECTED` / `TRADE_REJECTED`. Those **names stay**. Implementations MUST NOT silently retarget those types to a new `FAILED` catalog.

### M. Events vs receipts vs audit

```text
ACTION ≠ EVENT
WORLD EVENT ≠ PLATFORM AUDIT
CANONICAL FACT ≠ RESEARCH INTERPRETATION
```

Rejected actions may have receipts and no world events. No `event-catalog/0.3` in this pass.

### N–O. Projection and aggregates

```text
CANONICAL EVENT HISTORY
↕ reconciliation
DURABLE AUTHORITATIVE WORLD RECORD + PLAYER KNOWLEDGE
↓ visibility / access filter
↓ semantic projection
↓ human or agent rendering
```

Prefer a Postgres transaction when all touched state can settle locally. Use the World DO when ordered concurrent submissions, response windows, or fairness-sensitive serialization matter. If stale data could authorize an invalid mutation, require authoritative current state.

### P. World time

```text
WORLD TIME ≠ PLATFORM CLOCK ≠ WORKER EXECUTION TIME
```

Worker delay cannot extend authority, erase commitments, shift deadlines, change same-cycle ordering, or grant extra regeneration. Prefer half-open `[start_cycle, end_cycle)` where practical.

### Q. Schema spine (conceptual)

Persist only what would lose identity, durable commitment, Player knowledge, or provenance if deleted. Map onto existing DATA-MODEL / institution / agreement / event records.

Do **not** add canonical Class, XP, TrustScore, ReputationScore, Quest, Bank, Market, Court, or IntelligenceMetric tables. GC3 forbids a reputation scalar. GC6 forbids a quest engine. GC8 forbids currency/order book.

### R. Enforcement layers

```text
DATABASE     prevents impossible structure
REDUCER      prevents invalid meaning
TRANSACTION  prevents partial truth
DURABLE OBJECT  prevents unfair ordering
SCHEDULER    prevents temporal ambiguity
AUDIT        detects systemic drift
```

One canonical writer per invariant-sensitive field. No hidden gameplay state machines in DB triggers.

| Invariant | Primary enforcement |
|-----------|---------------------|
| ID uniqueness / world isolation | Postgres |
| Resource nonnegative / conservation | Postgres + reducer / transaction |
| Ownership exclusivity | Postgres + transaction |
| Authority scope / no escalation | reducer |
| Agreement version / assent | Postgres + reducer |
| No double commitment / idempotency | transaction + Postgres + reducer |
| Contest / same-cycle ordering | Durable Object + settlement |
| Event/state atomicity | Postgres transaction |
| Player visibility | projection |
| Research/game boundary | service + permissions |
| Replay equivalence | CI / reconciliation |

---

## Frozen-version conflicts left unchanged

| Item | Why left |
|------|----------|
| `LOOK` / `TRADE` / `COMMIT.*` wire verbs | Frozen v0.1 required set |
| `MOVE_REJECTED` / `TRADE_REJECTED` type names | Frozen catalog 0.1/0.2 |
| Operator classes `CONTROL_PLANE` / … / `RECOVERY` | First-world freeze; map receipts onto them |
| Hosted mutations centralized in `NoemaWorldDO` | Do not bypass; qualify durability only |
| GC1–GC10 first-slice catalogs | Already Accepted RFCs |

No superseding RFC is opened in this pass. Accepted RFC-0002…RFC-0014 remain.

---

## Pause

```text
Architecture-design frontier PAUSED.
Next frontier when explicitly resumed:
canonical reducer registry + mutation ownership map.
```
