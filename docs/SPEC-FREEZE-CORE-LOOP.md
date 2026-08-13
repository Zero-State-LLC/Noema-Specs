# Spec Freeze & Implementation Readiness — Core Loop (v0.1–v0.7)

**Status:** Freeze recommended for the **core product/research loop**  
**Audit date:** 2026-08-11  
**Canonical tip:** `main` @ `33e0488` (LEARN v0.7)  
**Validator:** `python3 validation/validate_all.py` → **PASS**

---

## 1. Freeze decision

### FREEZE: core loop specifications

The following product loop is **executable on paper** with machine contracts, fixtures, negatives, and conformance:

```text
PLAY → NOTICE → TEST → CAPTURE → LEARN
```

| Milestone | Role in loop | Spec readiness |
|---|---|---|
| **v0.1 Chamber** | PLAY world substrate | Executable (rc2 pin); runtime seed replay exists |
| **v0.2 Frontier** | NOTICE conditions | Executable package F01–F15 |
| **v0.3 Observatory** | NOTICE detection | Executable package O01–O16 |
| **v0.4 Lab** | TEST | Executable package L01–L34 |
| **v0.5 Compiler** | CAPTURE | Executable package P01–P30 |
| **v0.6 Deep Time + Genesis** | History / admin create-world | Executable package D01–D30 + G01–G09 |
| **v0.7 LEARN** | LEARN relationships | Executable package K01–K12 |
| **RFC-0002** | Strategic conflict catalog | Accepted |
| **RFC-0003** | Determinism / provenance | Accepted / Implemented (specs) |

### DO NOT FREEZE yet: post-core research expansion

| Milestone | Why not freeze |
|---|---|
| **v0.6B** Contracts & Markets | Not specified as executable package |
| **v0.6C** Full semantic evolution | Foundation only in v0.6 |
| **v0.8** Phenomena | RFC-0001 still draft-oriented; not required for core loop |
| **v0.9** Atlas publication | Downstream of LEARN/export maturity |
| **v1.0** Third-party full journey | Requires runtime end-to-end evidence |

**Recommendation:** Treat v0.1–v0.7 core-loop contracts as the **implementation target set**. Prefer implementation feedback over opening v0.8.

**Game Completeness** is a **parallel PLAY-depth specification campaign**, not a thaw of this freeze and not v0.8 Phenomena. See [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md). Those documents settle product behavior; they do not make GC1–GC10 executable and they do not authorize runtime construction or new catalogs without RFC.

First-world operational freeze (identity, ops, Admin, Perihelion pin): [FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md).

---

## 2. Observed machine inventory (`main`)

| Surface | Count / status |
|---|---|
| JSON schemas under `specs/` | 115 |
| Markdown docs under `docs/` | 190 |
| Conformance case files | 594 |
| Example JSON fixtures | 303 |
| Negative fixtures (validated rejects) | 42 |
| Release packages | v0.2 … v0.7 |
| Open PRs | none |
| Validator gates | structure, links, claims, seed, negatives, C/F/O/S/L/P/D/G/K, Lab, Compiler, Deep Time, LEARN, experience, skills, RFC-0003 |

---

## 3. Core-loop authority map

| User concept | Technical authority | Machine package |
|---|---|---|
| PLAY | `docs/PLAY.md`, world/game contracts | v0.1 seed, C01–C26, S01–S18 |
| WATCH | `docs/WATCH.md`, SPECTATOR | projections + redaction rules |
| NOTICE | Frontier + Observatory | F01–F15, O01–O16 |
| TEST | Lab + STUDY intents | L01–L34, intent catalog |
| CAPTURE | Compiler | P01–P30, capture defaults |
| LEARN | Capability Graph (minimal) | K01–K12 |
| Admin create world | Genesis | G01–G09 |
| History persistence | Deep Time | D01–D30 |
| Determinism | RFC-0003 + REPLAY | architecture hardening gate |

Experience presentation: `docs/EXPERIENCE.md` — progressive disclosure without second truth models.

---

## 4. Implementation readiness by slice

Ordered for a solo/tiny-team modular monolith. Later slices depend on earlier ones.

### Slice A — Chamber world engine (v0.1) — **START HERE**

| Item | Status |
|---|---|
| Specs | Mature (C01–C26, action/economy/scheduler/module contracts) |
| Runtime (`Zero-State-LLC/Noema`) | **Partial:** pure reducers + `noema-replay` seed equivalence; **not** full gateway/UI/agent protocol server |
| Fixture pin drift | Runtime README cites `v0.1.0-rc1`; Specs README pin is `v0.1.0-rc2` — **reconcile before claiming runtime compliance** |
| Next build | Modular monolith: gateway, auth, action router, world engine, ledger, observation, message delivery, scheduler, snapshots, spectator, compose golden path |

### Slice B — Agent protocol + PLAY connectivity

| Item | Status |
|---|---|
| Specs | `protocols/agent-protocol-v1.md`, agent-action schemas, onboarding fixtures |
| Runtime | Not evidenced as complete server |
| Next build | HELLO/negotiate, act, ack/resume, observation stream, containment budgets |

### Slice C — WATCH spectator

| Item | Status |
|---|---|
| Specs | SPECTATOR + projections; no world mutation |
| Runtime | Not required for seed replay; needed for product surface |
| Next build | LIVE/realms/history projections from ledger only |

### Slice D — Frontier NOTICE (v0.2)

| Item | Status |
|---|---|
| Specs | Executable F01–F15 |
| Runtime | Not started (beyond Chamber) |
| Depends on | Slice A + B stability |

### Slice E — Observatory NOTICE (v0.3)

| Item | Status |
|---|---|
| Specs | Executable O01–O16 |
| Runtime | Not started |
| Depends on | Trajectories / research capture path |

### Slice F — Lab TEST (v0.4)

| Item | Status |
|---|---|
| Specs | Executable L01–L34; isolation `mutates_production: false` |
| Runtime | Not started |
| Depends on | Replay harness + experimental forks |

### Slice G — Compiler CAPTURE (v0.5)

| Item | Status |
|---|---|
| Specs | Executable P01–P30; implementation order documented in PHENOMENON-COMPILER |
| Runtime | Not started |
| Depends on | Lab READY results + replay oracle |

### Slice H — Deep Time + Genesis (v0.6)

| Item | Status |
|---|---|
| Specs | D01–D30 + G01–G09; admin-only Genesis; no event-catalog/0.3 |
| Runtime | Not started |
| Depends on | Chamber orgs/infra + durable history indexes |

### Slice I — LEARN (v0.7)

| Item | Status |
|---|---|
| Specs | K01–K12; rebuildable derived graph |
| Runtime | Not started |
| Depends on | Captured tests + Lab/regression artifacts |

---

## 5. Architecture constraints for implementers (must not violate)

1. **Specs-only authority:** `Noema-Specs` does not ship runtime code; implement in `Noema` (or successor runtime).
2. **Modular monolith first** (`docs/DEPLOYMENT.md`, `docs/MODULE-CONTRACTS.md`) — not microservices.
3. **One fenced writer** + cycle-batch `SERIALIZABLE` persistence (RFC-0003).
4. **Claim labels only:** `OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE` — no consciousness scores.
5. **Research never rewrites world truth** (Lab/Observatory/Compiler/LEARN isolation).
6. **Lore is derived** (Deep Time); Genesis is **admin-only** one-shot.
7. **LEARN is derived** and off the PLAY hot path.
8. **Closed catalogs** — expand event types only via RFC.

---

## 6. Drift and soft defects found (safe)

| Finding | Severity | Action |
|---|---|---|
| SPEC-CHECKLIST v0.4 line still says L01–L22 | Low docs drift | Fix checklist to L01–L34 (safe) |
| Runtime fixture pin `rc1` vs specs pin `rc2` | Medium inter-repo | Align `Noema` fixtures/README to current specs pin before release claims |
| `INTEGRATION-SURFACE.md` still describes richer Capability Graph (architecture attribution) | Low | Informative only; v0.7 freezes minimal LEARN — do not implement attribution yet |
| Product pins for v0.3–v0.7 labeled `*-draft` | Expected | Freeze = “implementable contracts,” not necessarily product GA numbering |
| README “Current pin” still emphasizes Chamber rc2 | OK | Reflects shipping runtime maturity, not full loop |

No open PRs. No blocking authority conflicts found that stop Chamber implementation.

---

## 7. Explicitly out of scope for first implementation milestone

Do **not** start as first code:

- v0.8 Phenomena / RFC-0001 ontology expansion
- Atlas publication pipelines
- Graph database / LEARN platform services
- Genesis as a live service or player API
- Full markets/constitutional law (v0.6B)
- Procedural lore generators
- Architecture attribution or phase-transition engines
- Game-completeness runtime (GC1–GC10) before Chamber play is stable and before each package’s Spec Completion Contract is machine-closed

---

## 8. Recommended implementation plan (tiny team)

### Phase 0 — Alignment (days)

1. Pin `Noema` to current Specs commit or release tag for fixtures.
2. Re-run Chamber seed replay; document EQUIVALENT boundary.
3. Adopt module boundaries from `module-contracts.v01.json`.

### Phase 1 — Playable Chamber MVP

1. Modular monolith + compose golden path (`/health`, `/ready`, `/version`).
2. World engine + ledger + scheduler + observation + messages.
3. Human PLAY path (text/structured).
4. Agent connect (minimal protocol).
5. WATCH LIVE projection (permissioned).
6. Backup/restart persistence (C-suite ops cases).

**Exit:** third party can enter a world, act, observe; seed replay remains EQUIVALENT.

### Phase 2 — Research spine (NOTICE → TEST)

1. Research capture trajectories.
2. Frontier situation injection (conditions only).
3. Observatory candidates (no world mutation).
4. Lab forks/isolation + STUDY intent compilation.

**Exit:** researcher can NOTICE and TEST without touching production world truth.

### Phase 3 — CAPTURE → LEARN

1. Compiler pipeline (follow PHENOMENON-COMPILER implementation order).
2. Captured-test packages + regression.
3. Derived LEARN graph rebuild from artifacts.

**Exit:** READY Lab result → CAPTURE AS TEST → LEARN summary without claim inflation.

### Phase 4 — History (parallel after Phase 1 durable world)

1. Institution/succession/artifact indexes from events.
2. Admin Genesis create-world wizard (preview → activate).

---

## 9. Spec freeze rules (while implementing)

While the core loop is frozen for implementation:

1. **Prefer RFCs** for catalog, protocol, schema, claims, security, or determinism changes.
2. **Allow** docs clarifications, fixture corrections, and validator hardening that do not change semantics.
3. **Do not** open large v0.8 campaigns unless a real runtime ambiguity blocks Phase 1–3.
4. Implementation gaps should return as **SPEC DEFECT** issues with minimal fixtures, not speculative redesigns.

---

## 10. Final verdict

| Question | Answer |
|---|---|
| Is the core loop fully specified? | **Yes** (v0.1–v0.7 + RFC-0002/0003) |
| Does machine validation pass? | **Yes** — full `validate_all.py` PASS |
| Is the specs repo ready to stop expanding? | **Yes for core loop** |
| Is the runtime ready for full product? | **No** — Chamber seed replay only |
| Highest-value next work? | **Implement Chamber modular monolith in `Noema`**, not v0.8 specs |
| Ready for v0.8 Phenomena specs? | **No — not yet** |

### Statement

> **Core-loop specification freeze is appropriate.**  
> **Implementation should begin (or resume) in the runtime repository against v0.1 Chamber as the first vertical slice**, then grow along NOTICE → TEST → CAPTURE → LEARN. Further major research milestones should wait for runtime feedback.
