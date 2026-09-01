# Notes — Crime Detection as an Evidence Path

**Status:** non-normative research-to-spec sketch
**Scope:** a possible future GC7 continuation that would give `CRIME_DETECTED` a producer
**Does not change:** RFC-0002, RFC-0042, RFC-0123, `contest-config.v02.json`, `event-types.0.2.json`, the published sanction ladder, PLAY, WATCH, or runtime behavior
**Proposes no numbers.** The research inputs are game-theoretic and do not calibrate NOEMA constants.

Recorded from [Research Assimilation — Crime](../RESEARCH-ASSIMILATION-2026-08-25-CRIME.md). Continuation is governed by rows `B7b`–`B7e` of [SPEC-GAP-REGISTER-2026-08-25.md](../SPEC-GAP-REGISTER-2026-08-25.md).

## Existing authority

[RFC-0002](../../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) already states that an unauthorized act is not a detected crime, that detection requires a witness, a sensor at condition ≥ 50, investigation, or self-report, and that `CRIME_DETECTED` is "not automatic guilt broadcast." [STRATEGIC-EVENT-COUPLING.md](../STRATEGIC-EVENT-COUPLING.md) already draws detection as a conditional follow-on (`→ CRIME_DETECTED? (if detection path succeeds)`). [contest-config.v02.json](../../specs/contest-config.v02.json) already publishes per-form base detectability.

The doctrine is therefore written. What is absent is the function that turns those inputs into a decision.

## Shape a future RFC would need to pin

Deterministic replay is existing doctrine, so any detection decision must be reproducible from ledger inputs and a seed — never from wall-clock randomness.

```text
contest form base detectability
  + independent witness count      (copies of one report are not new witnesses)
  + witness observability
  + sensor coverage and condition
  + investigation investment
  + self-report
  − concealment investment
  + seeded deterministic perturbation
  → evidence score vs. an explicit threshold
```

Two properties the papers make non-optional:

- **Independence, not volume.** [OCEAN](https://arxiv.org/abs/cs/0307012) and [witness credibility](https://arxiv.org/abs/2009.06470) both fail when repeated copies of one report are counted as corroboration. Second-hand reports should be able to open an investigation and should not be able to create a detection record.
- **Distinguishable error modes.** [Incomplete reputation information](https://arxiv.org/abs/2509.09181) shows missed detection, mistaken assessment, and failed execution have different consequences. A single error term is not sufficient, and any RFC should state its false-positive and false-negative expectations rather than leaving them implicit.

## Detection versus adjudicated sanction

The payload currently requires `influence_delta` and `influence_applied`, which makes every detection record a sanction record. The witness-credibility literature places exactly this coupling at the origin of reporting distortion.

Two shapes are available to a future RFC. Both are open; this note does not choose.

| Shape | Detection record | Sanction |
|---|---|---|
| Separated | evidence-bearing observation, no influence fields required | later governed review applies influence / access / org consequence |
| Gated | emitted only above a strong deterministic evidence threshold | remains attached, and the event is described honestly as confirmed detection rather than suspicion |

The separated shape changes a closed catalog payload and therefore needs an `event-catalog` amendment in the manner of RFC-0127. The gated shape does not, but it must not describe a low-confidence observation as a confirmed crime.

## Enforcement cost

[Sustainable institutionalized punishment](https://arxiv.org/abs/1204.3888) and [corruption under institutional punishment](https://arxiv.org/abs/2202.13104) both make free, frictionless, incorruptible enforcement a modelling error. The Player-paid path in [RFC-0123](../../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md) already charges 1 influence; the world-administered path charges nothing.

A future RFC would need to name who pays for investigation, adjudication, and restriction — attention, compute, influence, or institutional treasury — and which office or world service holds jurisdiction and leaves an auditable evidence trail. `ORG_REVIEW_ELIGIBLE` is a flag today, not a governance model.

## Exclusion and rehabilitation

[Social exclusion](https://arxiv.org/abs/1211.2838) supports temporary scoped restriction over fines, but only while monitoring is cheap; once it is costly, exclusion-based cooperation destabilizes. Existing temporary `ACCESS_RESTRICTED` is therefore well founded and should acquire a monitoring cost rather than more reach.

[Recipient norms](https://arxiv.org/abs/2405.05903) supports forgiveness and warns against stigma contagion. NOEMA has no contagion rule and must not gain one: a Player must never be penalized for trading with a publicly dangerous Player.

Existing rehabilitation is already victim-specific — `rehab_trades: 3` counts trades with the harmed counterparty after the hostile cycle. The open question is narrower than "make it less mechanical": whether severity should change the evidence required. **Corrected 2026-08-31:** this note previously also asked whether ordinary trades should count "where SOCIAL-MEMORY.md says restitution trades". That framing was wrong — [RFC-0036](../../rfcs/RFC-0036-decay-rehab.md) pins "3 distinct `TRADE_ACCEPTED`" and no authority pins a restitution trade type.

## Explicitly out of scope

Organized crime. [Hysteresis in criminal organizations](https://arxiv.org/abs/2403.03720) argues that countermeasures should disrupt agreements, routes, holdings and coordination rather than amplify individual punishment — but that composes existing institutions and presupposes a working first loop. It is not a first repair.
