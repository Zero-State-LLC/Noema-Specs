# GC4 Crime and Expulsion — Design Note (Continuation 2026-08)

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parent:** [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC4) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)

**Related:** [RESEARCH-ASSIMILATION-2026-08-25-CRIME.md](RESEARCH-ASSIMILATION-2026-08-25-CRIME.md), [GC7-CRIME-DETECTION-SANCTION-SEED.md](GC7-CRIME-DETECTION-SANCTION-SEED.md), [GC7-CRIME-ENFORCEMENT-SEED.md](GC7-CRIME-ENFORCEMENT-SEED.md), PR #305

**Gap:** How institutions use CRIME_DETECTED or contest outcomes for role removal, expulsion, or temporary exclusion (per existing "crime/expulsion rule" language).

**Research inputs (2026-08-25):**
- Per-incident evidence and first-hand observation preferred over aggregated or second-hand.
- Temporary scoped exclusion preferred while monitoring/enforcement is cheap.
- Enforcement financing and jurisdiction matter; free institutional punishment is fragile.
- No stigma contagion; rehabilitation focus.
- Hysteresis for organized patterns deferred.

**Proposed design framing (for future RFC slice):**
- Institutions with appropriate role-definition authority MAY define ledgered rules linking specific CRIME_DETECTED (or CONTEST_RESOLVED) to:
  - ROLE_VACATED or role removal.
  - Temporary ACCESS_RESTRICTED scoped to the institution.
  - Succession triggers.
- Must be versioned, auditable, with due process path (investigation or contest).
- Ties to GC3 social memory (public descriptors feed institutional memory).
- Bounded: fail-closed, jurisdiction-limited, reversible where possible.

**Boundaries:** Extends INSTITUTIONAL-AUTHORITY without new verbs or catalog. Complexity doctrine. Research inputs only. Aligns with RFC-0002 detection (not guilt) and 2026-08-25 emphasis on credible evidence loops.

**Citations:** As above + GC4-FIRST-SLICE.md, RFC-0008, 2026-08-25 crime assimilation, PR #305.

Smallest viable unit for GC4 completion. Ready for operator review or RFC-00xx slice.

## Extension Points

Non-normative jurisdiction and due-process proposal seams.

- Extend candidate rule packets with incident evidence, office/role authority, jurisdiction, financing, duration, appeal/contest path and restoration conditions. Compare removal, temporary exclusion and succession separately; a CRIME_DETECTED record denotes detection, not guilt or an automatic sanction.
- Preserve inputs-only status and no stigma contagion. The proposed event names and role-removal examples here do not authorize new catalogs or live institutional punishment. Private social-memory descriptors cannot become public institutional evidence merely because the historical framing calls them public.
- Compatibility/promotion: reconcile this seed against accepted INSTITUTIONAL-AUTHORITY and crime/conflict decisions before proposing a scoped RFC; closed enforcement choices are not reopened by this note. Any rule change needs versioned authorization, event and visibility contracts, not an i18n handoff into PLAY.
- Verification proposal: prepare cases for weak/second-hand evidence, wrong jurisdiction, vacant authority, unfunded enforcement and expired exclusion, plus an appeal that preserves incident history. Keep candidate, approved and rejected sanctions distinguishable in the design review. No case described here is evidence that a runtime sanction executed.
