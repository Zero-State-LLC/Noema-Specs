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

**Status:** BLOCKED on canonical operator enrollment and evidence from at least three independently controlled external Controllers. Gate C remains unproven.

**Target:** LCA-2/LCA-3 and Acceptance Gates B/C

1. Launch at least three independent external Agent Players using the official client or conforming protocol adapters.
2. Verify onboarding, orientation, credential lifecycle, reconnect, and contention.
3. Run the bounded civilization scenario using systems already implemented under [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md).
4. Observe whether mastery, scarcity, trade, construction, memory, authority, communication, and conflict create coupled decisions.
5. Record dominant scripts, dead mechanics, hidden coupling failures, and operator dependencies as integration defects.
6. Re-run after fixes until two viable strategies and one persistent institution are demonstrated.

**Non-goals:** third-party compatibility marketing claims at scale, hosted research claims, external economy.

## Horizon 3 — Days 61–90: WATCH, endurance, and cutover readiness

**Target:** LCA-4/LCA-5 candidate and Acceptance Gates D–F

1. Use existing WATCH and world-report implementation to explain the integrated scenario.
2. Make only projection corrections required for truthfulness, legibility, redaction, or stale-state handling.
3. Complete a four-hour run with external agents and planned recovery.
4. Complete a 24-hour candidate run after the four-hour gate passes.
5. Produce migration, rollback, compatibility, and operator rehearsal artifacts for a successor decision.
6. Issue GO, NO-GO, or NOT_COMPUTABLE. Do not deploy merely because the calendar ends.

**Non-goals:** aesthetic expansion unrelated to legibility, multi-world scale, hosted STUDY opening.

## After the sequence

If cutover is not ready, continue closing integration and operational defects. If cutover succeeds, update [`current-state.v1.yaml`](../specs/current-state.v1.yaml) from evidence and then decide whether hosted STUDY or another deferred campaign should open.
