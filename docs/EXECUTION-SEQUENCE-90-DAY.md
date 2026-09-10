# Living Civilization Alpha — 90-Day Integration Sequence

**Status:** active sequencing plan  
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)

This sequence starts from the implementation already present. Time does not open a later horizon; the preceding gate does.

## Work-packet contract

Every packet states:

```text
Existing implementation being integrated
Evidence commit and tests
Campaign milestone
Production-alpha delta
User-visible or operational outcome
Normative specifications and RFCs
Validation and production-like observation
Public claim permitted afterward
Explicit non-goals
```

## Horizon 1 — Days 0–30: Reconcile and integrate

**Status:** COMPLETE. Gate A passed through Noema PR #587; evidence is [LCA-GATE-A-PROMOTION-2026-08-25.md](LCA-GATE-A-PROMOTION-2026-08-25.md).

**Target:** LCA-1 and Acceptance Gate A

1. Pin the advanced Worker candidate and enumerate all implemented GC, diplomacy, access, WATCH, settlement, and recovery slices.
2. Run the complete Worker suite and typecheck as a single baseline, not per-slice cherry picks.
3. Build a production-alpha delta report: implemented, deployed, configuration-only, migration-required, blocked, or intentionally excluded.
4. Exercise one integrated local/isolated scenario spanning identity, resource pressure, trade, construction, organization authority, social memory, communication, WATCH, and restart.
5. Fix cross-slice state, event, projection, authority, and recovery defects without adding mechanics.
6. Produce a successor-cutover risk register.

**Non-goals:** new verbs, new rooms, new GC systems, balance polish unsupported by integrated evidence.

## Horizon 2 — Days 31–60: External population and civilization run

**Status:** COMPLETE. Gate B / LCA-2 ([LCA-GATE-B-PROMOTION-2026-09-08.md](LCA-GATE-B-PROMOTION-2026-09-08.md)) and Gate C / LCA-3 ([LCA-GATE-C-PROMOTION-2026-09-08.md](LCA-GATE-C-PROMOTION-2026-09-08.md)).

**Target:** LCA-2/LCA-3 and Acceptance Gates B/C

1. Launch at least three independent external Agent Players using the official client or conforming protocol adapters. **Done for Gate B** (Noema #590 evidence).
2. Verify onboarding, orientation, credential lifecycle, reconnect, and contention. **Done for Gate B.**
3. Run the bounded civilization scenario using systems already implemented under [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md). **Done for Gate C** (Noema #662/#663/#664 plus Path 8 recover JSON).
4. Observe whether mastery, scarcity, trade, construction, memory, authority, communication, and conflict create coupled decisions. **Done for Gate C.**
5. Record dominant scripts, dead mechanics, hidden coupling failures, and operator dependencies as integration defects. **Done for Gate C.**
6. Re-run after fixes until two viable strategies and one persistent institution are demonstrated. **Done for Gate C.**

**Non-goals:** third-party compatibility marketing claims at scale, hosted research claims, external economy.

## Horizon 3 — Days 61–90: WATCH, endurance, and cutover readiness

**Status:** OPEN after Gate D. Gate D is complete. Gates E and F remain unproven.

**Target:** LCA-4/LCA-5 candidate and Acceptance Gates E–F

1. Use existing WATCH and world-report implementation to explain the integrated scenario under [LCA-GATE-D-SCENARIO.md](LCA-GATE-D-SCENARIO.md). **Done for Gate D** ([LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md); Noema #679 PASS + one-door unify #680 / Specs #333 / Deploy).
2. Make only projection corrections required for truthfulness, legibility, redaction, or stale-state handling. **Done for Gate D** (Chamber FE #674/#675/#677 plus one-door unify).
3. Complete a four-hour run with ≥3 independently controlled external Controllers under [LCA-GATE-E-SCENARIO.md](LCA-GATE-E-SCENARIO.md) (Phase A; Prep has no clock).
4. Complete a 24-hour candidate run after the four-hour gate passes under [LCA-GATE-E-SCENARIO.md](LCA-GATE-E-SCENARIO.md) (Phase B; ≥1 planned restart/recovery drill **inside** the 24-hour window).
5. Produce migration, rollback, compatibility, and operator rehearsal artifacts for a successor decision under [LCA-GATE-F-SCENARIO.md](LCA-GATE-F-SCENARIO.md) (packet items 1–6; rehearsal isolated, production GET-only).
6. Issue GO, NO-GO, or NOT_COMPUTABLE under [LCA-GATE-F-SCENARIO.md](LCA-GATE-F-SCENARIO.md) (item 7; Danny human-yes). Do not deploy merely because the calendar ends; `GO` does not itself deploy.

**Non-goals:** aesthetic expansion unrelated to legibility, multi-world scale, hosted STUDY opening.

## After the sequence

If cutover is not ready, continue closing integration and operational defects. If cutover succeeds, update [`current-state.v1.yaml`](../specs/current-state.v1.yaml) from evidence and then decide whether hosted STUDY or another deferred campaign should open.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Packet refinement can split an integration defect into smaller evidence-bearing packets while retaining the implementation pin, production-alpha delta, permitted claim, and non-goals. Elapsed days do not satisfy an acceptance gate.

- Sequencing revisions should identify the gate dependency they change and reconcile the campaign and current-state evidence. Gate A, Gate B, Gate C, and Gate D completion remain recorded; additional Controller runs do not by themselves prove Gates E–F or open hosted STUDY.

- Before promoting a revised packet, trace its result to a pinned test/run and the relevant acceptance gate, distinguish isolated from hosted evidence, and check that blocked enrollment, failed endurance, or unavailable cutover evidence cannot produce GO.
