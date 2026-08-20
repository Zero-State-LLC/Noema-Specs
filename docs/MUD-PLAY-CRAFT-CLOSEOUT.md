# MUD Play Craft — Specs closeout

**Status:** Specs-complete for craft C1–C9 (C2 remains sketch-only until optional wire RFC).  
**Date:** 2026-08-20  
**Companion:** [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md)  
**Interaction campaign:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)  
**Fixtures:** [examples/mud-play-craft/](../examples/mud-play-craft/)  
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
| **R0** | STATUS budgets strip; four-beat HAPPENED; PLAY plain failures; practice lines under STATUS | C3, C4, C7 · T1.4 · T1.6 | Yes with S0 parser |
| **R1** | MOVE success includes destination orientation; no second LOOK attention | C5 · ATTENTION-PROJECTION | After or with R0 |
| **R2** | Official client + harness: one idempotent RESYNC retry | C6 | Anytime server emits code |
| **R3** | Chamber fixture QA + S-MARK-10 smoke + C9 checklist on isolated world | C1, C8, C9 | After R0 |
| **R4** | Native Interaction S2+ (HELP, traces, aliases, a11y, WATCH narrative) | Features C–F tasks | After S1 room grammar stable |
| **R5** | Optional C2 wire RFC + schema if agents still parse prose | C2 | Only if needed |

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

- [ ] R0 presentation on Worker PLAY / chamber
- [ ] R1 MOVE orientation bundle
- [ ] R2 client RESYNC single retry
- [ ] R3 isolated proof + optional C9 tick-through
- [ ] R4 Native Interaction deeper slices per tasks file

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
