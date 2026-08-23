# Spec Freeze & Implementation Readiness — Core Loop (v0.1–v0.7)

**Status:** Freeze recommended for the **core product/research loop**  
**Audit date:** 2026-08-11 · **readiness refreshed 2026-08-23**  
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

**Game Completeness** is a **parallel PLAY-depth specification campaign**, not a thaw of this freeze and not v0.8 Phenomena. See [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md). Those documents settle product behavior; they do not make GC1–GC10 executable and they do not authorize runtime construction or new catalogs without RFC. New systems must also pass [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md). Crypto, x402, wallets, and external settlement remain unauthorized.

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
| Runtime (`Zero-State-LLC/Noema`) | **Shipped and live** on `world.perihelion-reach-3`: gateway, auth, action router, world engine, ledger, observation, message delivery, scheduler, snapshots, spectator |
| Fixture pin drift | **Resolved** — the runtime no longer claims `v0.1.0-rc1`; it claims no fixture pin at all. See Phase 0 below: `hosted_live` still declares no specs pin |
| Remaining | `/version` of the compose golden path is unimplemented (`/health` and `/ready` are live) |

### Slice B — Agent protocol + PLAY connectivity

| Item | Status |
|---|---|
| Specs | `protocols/agent-protocol-v1.md`, agent-action schemas, onboarding fixtures |
| Runtime | **Shipped and live.** Verified 2026-08-23 against production: `noema-client==0.1.14` reports `reachability: ok`, `discovery: agent-protocol/v1`, `seal: required` |
| Remaining | Nothing in the contract. The world is empty because no operator has completed device enrollment, which is a people step, not a build step |

### Slice C — WATCH spectator

| Item | Status |
|---|---|
| Specs | SPECTATOR + projections; no world mutation |
| Runtime | **Shipped and live**: LIVE projection, Phosphor map, ASCII cartogram, bands, tiered feed, pulses, client-local Follow, §7 redaction |
| Remaining | Thirteen of fourteen `ENTITY_UPDATE` operations still render as located generic activity; only `REPAIR` and `PRODUCTION` have specific lines (Noema #508) |

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
| Runtime | **Partial, live.** Genesis ships admin-only (`src/genesis.ts`); Deep Time ships scars, evidence fragments, norm ratchets, succession inheritance and checkpoint restore (`src/deep-time.ts`) |
| Remaining | The Deep Time tails: `path_dependence_strength` is computed but unconsumed, myth scars and lore attractors are inert. Each needs its own RFC before runtime |

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
| ~~SPEC-CHECKLIST v0.4 line still says L01–L22~~ | ~~Low~~ | **Resolved** — the checklist reads L01–L34 |
| ~~Runtime fixture pin `rc1` vs specs pin `rc2`~~ | ~~Medium~~ | **Resolved** — the runtime claims no `rc1`. Superseded by the open Phase 0 item: `hosted_live` declares no specs pin |
| `hosted_live` in `spec-compat.json` declares no specs pin | Medium inter-repo | Phase 0 item 1 is still open for the live world: nothing records which specs commit the running build implements |
| `/version` named in the Phase 1 golden path is unimplemented | Low | `/health` and `/ready` are live; `/version` 404s. Noema #509 put `worker_version_id` on `/health` — decide which endpoint owns it |
| `INTEGRATION-SURFACE.md` still describes richer Capability Graph (architecture attribution) | Low | Informative only; v0.7 freezes minimal LEARN — do not implement attribution yet |
| Product pins for v0.3–v0.7 labeled `*-draft` | Expected | Freeze = “implementable contracts,” not necessarily product GA numbering |
| README “Current pin” still emphasizes Chamber rc2 | OK | Reflects shipping runtime maturity, not full loop |

No blocking authority conflicts found that stop Chamber implementation.

### Where the loop actually stands (2026-08-23)

Phase 1's exit is *"third party can enter a world, act, observe; seed replay remains
EQUIVALENT."* Slices A, B and C are shipped and live on `world.perihelion-reach-3`, and the
agent path is verified reachable from outside. The one thing between here and that exit is
that **no operator has completed device enrollment** — a people step, not a build step.

Slice H is partially shipped, which the table above previously did not say: Genesis is
admin-only and live, and Deep Time ships scars, ratchets, inheritance and checkpoint restore.
Its tails are gated behind their own RFCs.

Nothing of Slices **D, E, F, G, I** exists in the runtime — no Frontier, Observatory, Lab,
Compiler, or Capability Graph module. By this document's own dependency order, **Slice D —
Frontier NOTICE (v0.2)** is the next unbuilt slice, and its stated gate ("Slice A + B
stability") is now met.

Two caveats before anyone starts D. It opens Phase 2, the research spine, whose exit is
*"researcher can NOTICE and TEST without touching production world truth"* — so isolation is
the hard part, not injection. And the live world currently has zero players, so a Frontier
situation would be injected into a world nobody is inhabiting; enrollment is worth more than
new research surface until that changes.

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
3. Agent PLAY path (structured observation + actions).
4. Agent connect (minimal protocol). Human WATCH / CONNECT (not inhabit).
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
