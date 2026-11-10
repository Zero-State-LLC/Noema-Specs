# MUD Play Craft — Specs closeout

**Status:** Specs-complete for craft C1–C9 (C2 remains sketch-only until optional wire RFC).  
**Date:** 2026-08-20  
**Companion:** [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md)  
**Interaction campaign:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)  
**Fixtures:** [examples/mud-play-craft/](../examples/mud-play-craft/)  
**RFC-0120:** production inhabit is Agent Player only. Retain world-true craft (HERE, EXITS, STATUS, HAPPENED, traces, WATCH, Home). Retire human parser / Chamber / HELP / aliases as production Player requirements; mark them **NON-CANONICAL DEV TOOLING** if kept. Continuation is A0–A10, not S0–S7 as hosted human PLAY.

**Does not:** reopen Genesis, add verbs, change harvest magnitudes, extend research experience-error catalog, or require Perihelion reseed.

---

## 1. Specs seal

| Craft ID | Specs state | Runtime dependency |
|----------|-------------|--------------------|
| C1 Chamber projections | **Done** — examples | Manual QA / presentation tests |
| C2 Agent layer sketch | **Sketch only** | Wire RFC **only if** existing observation cannot expose layer semantics |
| C3 STATUS strip | **Done** — Feature B + T1.6 | PLAY adapter / `room-view` |
| C4 Four-beat + PLAY errors | **Done** — T1.4 + PLAYER-ACTION-MAP §7 | PLAY adapter; keep codes in Advanced |
| C5 Post-MOVE orientation | **Done** — §7a + ATTENTION-PROJECTION | MOVE response bundle (prefer no ledger change) |
| C6 SETTLEMENT_RESYNC retry | **Done** — client §12.1 + harness §9 | `noema-client` / harness only |
| C7 Practice crumbs | **Done** — GC1-S0 lines under STATUS | Already-hosted derived projection placement |
| C8 S-MARK-10 | **Done** — T1.7 | Presentation/acceptance test harness |
| C9 Hosted audit checklist | **Done** — advisory | Ops/runtime audit; not Specs law |

**Specs work on this companion is complete** when this closeout is on `main`. Further Specs edits are bugfixes, C2 RFC (optional), or Native Interaction S0–S7 implementation specs already filed as tasks — not more craft horizon expansion.

---

## 2. Relationship to runtime progress

```text
SPECS (this repo)                    RUNTIME (Zero-State-LLC/Noema + client)
─────────────────                    ──────────────────────────────────────
MUD-PLAY-CRAFT C1–C9  ──────────►   presentation / adapter / client work
MUD-NATIVE-INTERACTION tasks ────►   parser, room grammar, HELP, traces
GC / core freezes (done)  ───────►   already partially hosted; do not reopen
```

### Timing rules

1. **Do not block Specs completeness on runtime.** Craft and Native Interaction tasks are implementable now from docs + fixtures.
2. **Do not block runtime on further craft specs.** Prefer implementing T1.4 / T1.6 / MOVE bundle / RESYNC from current docs.
3. **Native Interaction S0 (parser) and S1 (room grammar)** may proceed **in parallel** with craft presentation work; S1 SHOULD absorb STATUS (T1.6) and four-beat HAPPENED (T1.4).
4. **C5 MOVE bundle:** implement as observation/presentation first. Open an RFC **only if** event catalog or double LOOK debit cannot be avoided.
5. **C2 wire fields:** defer until a structured agent proves it cannot recover Feature B layer semantics from current observations. Sketch stays non-normative until then.
6. **C6** is client/harness-only — can ship without world DO changes if the server already returns `SETTLEMENT_RESYNC`.
7. **C7** is placement of **already-specified** GC1-S0 lines (RFC-0004 hosted) — no new mastery mechanics.
8. **Perihelion:** audit with C9 checklist; **no reseed**, no Genesis ops, no Recover-for-craft.

### Suggested runtime phases (non-normative order)

| Phase | Work | Specs pins | Parallel? |
|-------|------|------------|-----------|
| **A0** | Agent-only authority + identity migration (RFC-0120) | this closeout + AGENT-ONLY-PLAYER-IDENTITY | Specs first |
| **A1** | Principal model split | AUTH-AND-IDENTITY | After A0 |
| **A2** | Controller enrollment / binding hardening | CONNECT / RFC-0116 | After A1 |
| **A3** | Agent observation contract (WHERE/HERE/EXITS/STATUS/HAPPENED/AVAILABLE ACTIONS) | C3–C5 · T1.2 · T1.6 | After A0 |
| **A4** | Structured action discovery | AGENT-PLAY · COMMAND-DISCOVERY | With A3 |
| **A5** | Agent harness / headless conformance | C6 · RFC-0116 | With A2 |
| **A6** | Feature D first family: repair plate + scar projector provenance. No `TRACE` verb. Cite [MUD-NATIVE-INTERACTION-TASKS.md](MUD-NATIVE-INTERACTION-TASKS.md) S3 runtime mapping | Native Interaction traces | After A3 |
| **A7** | WATCH spectator intelligence | WATCH-LIGHTWEIGHT-SPECTATOR | Parallel after A0 |
| **A8** | Home live-world proof | HOSTED-FIRST-ENTRY | With A7 |
| **A9** | Research / admin isolation cleanup | STUDY · ADMIN-LIVE | After A1 |
| **A10** | Human PLAY retirement / dead-code cleanup | HUMAN-PLAY as DEV TOOLING | After A1–A5 |

R0–R5 remain historical runtime sequencing for craft C1–C9. They MUST NOT be read as a hosted human PLAY campaign. Native Interaction S0 (human parser) is no longer a production Player requirement.

### Runtime out of scope for this closeout

```text
Genesis / reseed / force-supersede
new canonical verbs
GC1 mechanical benefits beyond existing hosted slices
boards/SHOUT unless separate GC5 RFC
research experience-error catalog changes
crypto / x402
```

---

## 3. Definition of done

### Specs (this closeout)

- [x] C1–C9 documented (C2 sketch)
- [x] Feature B order includes STATUS
- [x] Native Interaction tasks T1.4 / T1.6 / T1.7 / T1.8
- [x] Client/harness RESYNC rules
- [x] Fixtures under `examples/mud-play-craft/`
- [x] Horizon lock explicit
- [x] Runtime sequencing recorded here

### Runtime (tracked in Noema repo — not this file’s gate)

- [x] R0 presentation on Worker PLAY / chamber
- [x] R1 MOVE orientation bundle
- [x] R2 client RESYNC single retry
- [x] R3 isolated proof + optional C9 tick-through
- [ ] R4 Native Interaction deeper slices per tasks file

### Evidence disposition, 2026-11-10 (non-normative)

The R0–R3 checks above reconcile historical sequencing only with the bounded evidence below. They do not change the 2026-08-20 Specs seal, C2 sketch-only status, RFC-0120 retirement, or A0–A10 phases. No fresh runtime tests or hosted execution were performed for this reconciliation, and these pins do not certify present `main`.

| Historical check | Bounded disposition and immutable evidence |
|------------------|--------------------------------------------|
| R0 | D3a/A3 hosted **Agent observation presentation**, not revived human PLAY. The matched receipt records R0 **9/9**. Field presence is not full R4 grammar, accessibility, or comprehension acceptance. |
| R1 | Noema [PR #384](https://github.com/Zero-State-LLC/Noema/pull/384), merged `8930f41dcf06a699ee85a58b52ee2ef6acbab073`: [MOVE tests](https://github.com/Zero-State-LLC/Noema/blob/8930f41dcf06a699ee85a58b52ee2ef6acbab073/workers/noema/test/r1-move-orientation.test.ts) demonstrate a success bundle without LOOK cost and rejection without a destination bundle. Deployment pin [PR #385](https://github.com/Zero-State-LLC/Noema/pull/385), merged `fe867afc5f84b798a8c8f4204c07d1f9d4083085`, records source `8930f41dcf06a699ee85a58b52ee2ef6acbab073`, Worker `a54f35e0-ca24-470e-9acf-bb1279d7e662`. |
| R2 | Harness [PR #544](https://github.com/Zero-State-LLC/Noema/pull/544), merged `d3031cf8181891987a5ba5cd7d0ec67c6ecb8cb1`: [tests](https://github.com/Zero-State-LLC/Noema/blob/d3031cf8181891987a5ba5cd7d0ec67c6ecb8cb1/tests/test_harness_s0.py#L396-L432) demonstrate one retry with the same key/request and twice-RESYNC surfacing as non-incident. Official client source `16ec5d1f472295055439975f88567a43fe6ee3b0`: [tests](https://github.com/scrimshawlife-ctrl/noema-client/blob/16ec5d1f472295055439975f88567a43fe6ee3b0/tests/test_client.py#L215-L259) and [transport](https://github.com/scrimshawlife-ctrl/noema-client/blob/16ec5d1f472295055439975f88567a43fe6ee3b0/src/noema_client/transport.py#L194-L267) demonstrate the same `idempotency_key` and `client_action_sequence`, exactly two calls, then stop. This is source/test evidence, not a new execution result. |
| R3 | The [ordered runner](https://github.com/Zero-State-LLC/Noema/blob/5cebeca42dc745dca9ff3942eb4dc8515d4ad5ba/workers/noema/scripts/acceptance-733.mjs#L624-L662) checks canonical SQL before isolated reset, then checks same-version independent-principal trace readback after reset. Actual Chrome/WATCH observation belongs to the same matched cohort, not a mixture of failed runs. No fresh post-reset SQL query is claimed. C9 is optional and **not_covered**, not passed. |

**Shared R0/R3 receipt:** immutable Noema pin `e6a71ad8d0a114c73bb23eb77531251030117e02`, [hosted report](https://github.com/Zero-State-LLC/Noema/blob/e6a71ad8d0a114c73bb23eb77531251030117e02/docs/ISOLATED-733-SAME-WORLD-HOSTED-20261106.md) and [machine receipt](https://github.com/Zero-State-LLC/Noema/blob/e6a71ad8d0a114c73bb23eb77531251030117e02/docs/ISOLATED-733-SAME-WORLD-HOSTED-20261106.json). Historical run `20261106t083808z` (2026-11-06), source `5cebeca42dc745dca9ff3942eb4dc8515d4ad5ba`, Worker version `aa693ac2-c059-4388-9ce8-d25a90d7f975`: G1 **14/14**, G2 **15/15**, AC17 **8/8**, R0 **9/9**, G3 **eight true booleans**, `all_required_passed=true`.

**R4 remains unchecked.** Follow the existing [TX.2 matrix contract](MUD-NATIVE-INTERACTION-TASKS.md#tx2-runtimespec-matrix) and the [pinned runtime matrix](https://github.com/Zero-State-LLC/Noema/blob/e6a71ad8d0a114c73bb23eb77531251030117e02/docs/R4-NATIVE-INTERACTION-MATRIX-20261102.md). At that pin its **49 rows** remain **31 IMPLEMENTED_UNVERIFIED + 17 IMPLEMENTING + 1 NOT_STARTED + 0 VERIFIED**. Dated tracker disposition (2026-11-10): Noema S0–S7 [#778](https://github.com/Zero-State-LLC/Noema/issues/778), [#779](https://github.com/Zero-State-LLC/Noema/issues/779), [#780](https://github.com/Zero-State-LLC/Noema/issues/780), [#781](https://github.com/Zero-State-LLC/Noema/issues/781), [#782](https://github.com/Zero-State-LLC/Noema/issues/782), [#783](https://github.com/Zero-State-LLC/Noema/issues/783), [#784](https://github.com/Zero-State-LLC/Noema/issues/784), and [#785](https://github.com/Zero-State-LLC/Noema/issues/785) are OPEN except **#780 CLOSED for accepted bounded S2**, not whole-R4 acceptance. [#837](https://github.com/Zero-State-LLC/Noema/issues/837) remains OPEN without reopening #780. G5 [#777](https://github.com/Zero-State-LLC/Noema/issues/777) is separately reserved and untouched. These are existing trackers, not new duplicate work.

**Parent disposition remains separate:** [#733](https://github.com/Zero-State-LLC/Noema/issues/733) and [#775](https://github.com/Zero-State-LLC/Noema/issues/775) remain OPEN under explicit owner hold. [PR #810](https://github.com/Zero-State-LLC/Noema/pull/810), merged `8a49c308061787153b7b5ba93f067b5d7b5816a5`, published the four-document package. `reviewDecision=REVIEW_REQUIRED` and `reviews=[]` do not establish submitted approval or authorize closing those issues.

---

## 4. Handoff links

| Need | Open |
|------|------|
| Craft rules | [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) |
| Room order / features | [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) |
| Implementable tasks | [MUD-NATIVE-INTERACTION-TASKS.md](MUD-NATIVE-INTERACTION-TASKS.md) |
| Example rooms | [examples/mud-play-craft/](../examples/mud-play-craft/) |
| Hosted audit | [hosted-play-audit-checklist.md](../examples/mud-play-craft/hosted-play-audit-checklist.md) |
| Official client RESYNC | [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md) §12.1 |
| Harness failure class | [AGENT-HARNESS.md](AGENT-HARNESS.md) §9 |
| Practice lines | [GC1-FIRST-SLICE.md](GC1-FIRST-SLICE.md) |
| Attention / MOVE | [ATTENTION-PROJECTION.md](ATTENTION-PROJECTION.md) |

---

## 5. Change control after seal

- **Bugfix** to craft/examples: ordinary docs PR.
- **New PLAY verb or cost change:** RFC + freeze review — not a craft doc edit alone.
- **C2 promoting sketch → wire:** RFC with schema + fixtures + agent parity tests.
- **Runtime-only behavior** that matches this closeout: no Specs PR required; cite this file + craft sections in the runtime PR.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Prospective evidence maintenance can append dated runtime receipts mapped to C1–C9 and current A0–A10 handoff phases. Preserve the 2026-08-20 specs seal and C2 sketch-only status; stale R0–R5 checkboxes are historical sequencing, not renewed human PLAY requirements.

- Presentation bugfixes belong to the craft companion and Native Interaction tasks. C2 wire promotion still needs its own RFC, schema, fixtures, and agent parity proof; no new verb, Genesis operation, or reopened craft campaign follows from this extension.

- Check successor receipts against Feature B ordering, MOVE observation behavior, and the client-only SETTLEMENT_RESYNC retry boundary. Distinguish fixture/schema checks from hosted observation and label absent runtime proof; current evidence must respect RFC-0120 agent-only identity rather than rehabilitate the historical human parser path.
