# GC7 — first-world CONTEST help

**Status:** Executable specification. Runtime authorized with RFC-0095.  
**Parent:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [GC7-S3-INFORMATION-CONTEST.md](GC7-S3-INFORMATION-CONTEST.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0095](../rfcs/RFC-0095-contest-play-thaw.md)  
**Does not open:** WED/ATTEST help · HP · SCAN/ATTACK · event-catalog/0.3 · AGREEMENT_FORM  
**Next:** WED / ATTEST help stay parked

Chamber PLAY may name CONTEST. The operations are the ones already hosted.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New CONTEST verb | **REJECT.** |
| Help WED / ATTEST | **REJECT.** |
| HP / SCAN / ATTACK | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc7-thaw-play` |
| Catalog | `conflict-catalog/gc7-thaw-play` |
| Help CONTEST | true |
| Help WED / ATTEST | false |
| New verbs | none |
| WATCH | unchanged |

---

## Runtime rule

Hosted Chamber MUST list CONTEST on `help` and list existing contest/defend/withdraw aliases on `help contest`. MUST still omit WED and ATTEST. Isolated tests only. No Genesis change.

## Extension Points

Non-normative help parity and command-discovery regression seams.

- Extend help renderers for CONTEST and existing contest/defend/withdraw aliases, preserving canonical tokens while translating explanation. Compare general help and help contest so discoverability never advertises an unavailable action form.
- Preserve omission of WED/ATTEST, no new verbs, unchanged WATCH, no HP/SCAN/ATTACK or AGREEMENT_FORM expansion. Help visibility is not new action authority or an instruction to fight.
- Compatibility/promotion: pin conflict-catalog/gc7-thaw-play/RFC-0095 with GC7 S0/S3 and PLAYER-ACTION-MAP; do not infer additional thaws from this one accepted help change.
- Verification proposal: snapshot both help paths across supported renderers/locales, assert canonical aliases and negative tokens, and compare dispatch to existing operations in isolated fixtures. Keyboard and accessible help navigation must preserve neutral descriptions and add no private conflict facts or research thesis.
