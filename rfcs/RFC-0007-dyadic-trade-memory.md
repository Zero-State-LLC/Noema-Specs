# RFC-0007 — GC3-S0 Dyadic Trade Memory

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog` expansion. No reputation scalar. No runtime implementation in this RFC.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) forbids `reputation = 72` but left weights, edge rebuild, and leak rules as SPEC GAP.

## Proposed change

Accept GC3-S0: derived directed Player→Player edges counted from distinct `TRADE_ACCEPTED` trades. Thresholds 1 = `TRADED`, 3 = `RELIABLE`. Self PLAY lines only. WATCH empty.

Catalog: [`social-memory-catalog.gc3-s0.json`](../specs/social-memory-catalog.gc3-s0.json).  
Slice: [GC3-FIRST-SLICE.md](../docs/GC3-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Reputation integer | Doctrine + parent spec |
| New REMEMBER verb | Verb inflation |
| TRADE_REJECTED → deceptive | Legal decline is not betrayal |
| WATCH titles in S0 | Leak / presentation |

## Compatibility

Additive derived projection. v0.1 TRADE already exists.

## Data / security

Rebuildable cache. Projection must not include amounts, stock, or hidden entity ids. Private edges are subject-only.

## Validation

`check_gc3_s0`: three-trade reliable line; rejected trades ignored; third party and WATCH empty; no forbidden tokens in lines.

## Rollback

Omit the projection.

## Unresolved

GC3-S1: `AGREEMENT_BROKEN` / `CRIME_DETECTED` → `dangerous` without naming hidden methods.
