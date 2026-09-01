# RFC-PROPOSAL: GC7 Crime Rehabilitation Severity and Restitution Alignment (B7e)

**Status:** Minimal draft proposal, **two premises corrected 2026-08-31**. Bounded. Design/research only. No contract, catalog, verb, or exposure change.

**Correction.** Two of the four bullets below rest on a misreading that originated in the `B7e` register row, not in this note — the row has been corrected at source. Recorded here so the proposal is not reviewed on a false basis:

1. *"Restitution trades are strictly victim-specific (per existing SOCIAL-MEMORY.md 'restitution trades' pinning …)"* — **there is no such pinning.** [RFC-0036](RFC-0036-decay-rehab.md) is the authority and pins "3 distinct `TRADE_ACCEPTED` with that object **after** the last danger/deceptive evidence id". The "restitution trades" phrases in [SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) and [GC3-S4-DECAY-REHAB.md](../docs/GC3-S4-DECAY-REHAB.md) row F are illustrative prose, not requirements. Adopting a distinct restitution trade type would **contradict Accepted RFC-0036**, which is a spec change this note does not claim to make.
2. *"Ordinary trades with non-victim parties do not count toward rehabilitation for a given incident."* — **already true.** `rehabbedHostile()` counts `trade.edges[other]`, i.e. only trades with the harmed counterparty. This bullet proposes existing behavior and would read to a reviewer as a needed change.

**What survives, and is the whole of `B7e`:** severity-awareness. Rehabilitation requires the same 3 trades whether it clears a `MINOR` policy violation or `MAJOR` sabotage, and no authority ties the requirement to `CRIME_DETECTED.severity`. RFC-0036 chose 3 deliberately to match the S0 reliable floor, so any change must argue against that choice rather than treat the number as an oversight.

**Parent gap:** SPEC-GAP-REGISTER-2026-08-25 B7e (PARTIALLY_CLOSED residual in GC7 crime).

**Source:** SPEC-GAP-REGISTER-2026-08-25.md (B7e) + GC7 crime seeds + SOCIAL-MEMORY.md

**Proposed:**
- Rehabilitation requirements must be severity-aware (tie required evidence/restitution trades to the specific CRIME_DETECTED severity or impact).
- Restitution trades are strictly victim-specific (per existing SOCIAL-MEMORY.md "restitution trades" pinning and catalog.gc3-s4).
- Ordinary trades with non-victim parties do not count toward rehabilitation for a given incident.
- Avoids severity-blind counting and reputation laundering risks while preserving bounded forgiveness mechanics.

**Scope / Boundaries:** Extends GC7 crime + GC3 SOCIAL-MEMORY authority. No global reputation scalar. No stigma contagion. Research input only. Smallest viable alignment unit for B7e.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B7e), GC7-CRIME-PAYLOAD-VICTIM-SEED.md / other GC7 seeds, SOCIAL-MEMORY.md, social-memory-catalog.gc3-s4.json, RFC-0002, GAME-COMPLETENESS-PLAN.md (GC7), PR #305 + main continuation.

**Readiness:** Smallest unit. Ready for review to align rehabilitation with per-incident evidence and victim focus.

---
**Verification note:** Draft only; does not mutate specs.
