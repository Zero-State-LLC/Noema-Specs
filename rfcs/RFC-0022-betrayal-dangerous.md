# RFC-0022 — GC3-S1 Dangerous from Contest or Breach

## Status

**Accepted**

Closes the GC3-S0 betrayal SPEC GAP. No reputation integer. No new verbs. No `event-catalog/0.3`. Does not thaw `AGREEMENT_FORM`.

## Problem

[GC3-FIRST-SLICE.md](../docs/GC3-FIRST-SLICE.md) left `dangerous` waiting on formal breach. An implementer would invent a reputation score, treat `TRADE_REJECTED` as betrayal, or leak hidden contest methods.

## Proposed change

Accept GC3-S1:

- Derived directed victim→actor edges
- Evidence: `CONTEST_RESOLVED` (hosted path), plus `AGREEMENT_BROKEN` / `CRIME_DETECTED` when those events exist
- One distinct evidence id → self line `You have found {name} dangerous.`
- Trade reliability stays a separate GC3-S0 count
- WATCH and third parties empty
- `TRADE_REJECTED` still ignored

Catalog: [`social-memory-catalog.gc3-s1.json`](../specs/social-memory-catalog.gc3-s1.json).  
Slice: [GC3-S1-BETRAYAL.md](../docs/GC3-S1-BETRAYAL.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Subtract from reliable count | Collapses contradiction into one number |
| `TRADE_REJECTED` → deceptive | Legal decline |
| WATCH dangerous title | Leak / presentation |
| Thaw `AGREEMENT_FORM` in this RFC | Separate v0.2 verb; not required for hosted contest path |
| New REMEMBER verb | Verb inflation |

## Compatibility

Additive derived projection. GC3-S0 trade lines unchanged. GC7-S0 `CONTEST_RESOLVED` is the hosted evidence source.

## Data / security

Rebuildable cache. Lines must not include amounts, hidden ids, contest form, or detection method.

## Validation

`check_gc3_s1`: contest resolve creates dangerous for the defender only; reject trades ignored; third party/WATCH empty; no forbidden tokens.

## Rollback

Omit the danger projection. GC3-S0 trade memory remains.

## Unresolved

Closed later: institutional expectation [RFC-0035](RFC-0035-institution-edges.md); decay/rehab [RFC-0036](RFC-0036-decay-rehab.md); published trade caution [RFC-0037](RFC-0037-trade-friction.md). Auto-refuse stays rejected.
