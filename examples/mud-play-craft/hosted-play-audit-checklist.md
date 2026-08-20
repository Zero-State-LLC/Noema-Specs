# Hosted PLAY audit checklist (craft C9)

**Status:** Advisory / non-normative.  
**Authority pointer:** [MUD-PLAY-CRAFT.md](../../docs/MUD-PLAY-CRAFT.md) §7c  
**Targets:** local Worker, isolated hosted world, or operator-authorized Perihelion observe — **no reseed**, no Genesis ops.

Tick items during a short inhabit. Record build/sha and date. Failures are runtime debts, not automatic Specs defects.

## Setup

- [ ] Seal + controller path documented (`/.well-known/noema-agent.json` or local equivalent)
- [ ] World `ACTIVE` / `HEALTHY` (or note INCIDENT and stop mutation)
- [ ] Fresh observation after ENTER or resume

## Feature B room stack

- [ ] ROOM NAME visible
- [ ] DESCRIPTION present and free of live Player lists / stock tables
- [ ] PRESSURE room-local only (no other-room report bleed)
- [ ] HERE lists co-located Players/entities with names before raw enums
- [ ] EXITS show direction and known destination names
- [ ] STATUS shows energy + ≥1 other budget without a side rail
- [ ] HAPPENED answers tried / ok|fail / changed / next (or equivalent)
- [ ] AVAILABLE HERE / max-3 first paint ⊆ real affordances

## C5 — MOVE orientation

- [ ] Successful MOVE shows destination orientation without a mandatory second LOOK
- [ ] Attention does not debit LOOK when orientation was bundled on MOVE
- [ ] Failed MOVE does not show destination as entered

## C4 — Failures

- [ ] `BUDGET_EXCEEDED` names the scarce budget in plain language
- [ ] Empty harvest does not invite thrash as the only hint
- [ ] `SETTLEMENT_RESYNC` (if seen) retries once or explains safe retry — not INCIDENT panic
- [ ] Machine codes available in Advanced/debug

## C6 — Client (official / harness)

- [ ] Single automatic idempotent retry on RESYNC
- [ ] No retry loop on FORBIDDEN / hard INCIDENT

## C7 — Practice

- [ ] At most three self practice lines when PRACTICING
- [ ] GC1 wording only; no counts/XP
- [ ] No other Player’s practice; WATCH clean of mastery

## C8 — Short session

- [ ] Within ≤10 meaningful acts, at least one rank 1–4 mark path is possible (REPAIR/TRADE/MESSAGE/INSPECT upgrade)
- [ ] Session is not only MOVE/WAIT thrash

## Horizon lock

- [ ] No new verbs discovered as required
- [ ] No quest narrator
- [ ] No research capability labels in PLAY

## Sign-off

| Field | Value |
|-------|--------|
| Date | |
| Surface (local / isolated / perihelion) | |
| Build / sha | |
| Auditor | |
| Blockers | |
