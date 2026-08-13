# GC7 thaw readiness — 2026-08-13

**Status:** Not authorized. This document does **not** thaw `CONTEST_DECLARE`.  
**Authority:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md)  
**Prerequisite:** [RFC-0019](../rfcs/RFC-0019-hosted-world-time.md) hosted WAIT-quorum cycle commit.

| Topic | Status |
|-------|--------|
| Rhythm table | Spec-ready. Existing v0.2 forms/verbs only |
| World-time | RFC-0019. Needed for `expires_cycle` / `CONTEST_RESOLVE` |
| Durable commitments | RFC-0016/0017. SQL may still be unapplied |
| Hosted verbs | `CONTEST_DECLARE` / `CONTEST_DEFEND` still `NOT_IMPLEMENTED` |
| `CONTEST_RESOLVE` | World/scheduler only. Not a Player command |
| Help | Must omit CONTEST even after a later thaw (S0 out-of-list) |
| Also frozen | `AGREEMENT_FORM`, `ACCESS_POLICY`, WED, Genesis reseed |

GC10 remains separately frozen (schedule cycle 4; do not reseed). Isolated `CONTEST_DECLARE` → `CONTEST_RESOLVED` is the smallest later thaw. Do not implement HP, `SCAN`/`ATTACK`, or `event-catalog/0.3`.
