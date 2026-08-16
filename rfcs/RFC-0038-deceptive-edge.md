# RFC-0038 — GC3-S6 Deceptive as a Distinct Edge

## Status

**Accepted**

Specification-only. No new verbs. `TRADE_REJECTED` stays ignored. Does not replace GC3-S1 danger.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) lists `deceptive` as a derived band but left the distinct edge as SPEC GAP. RFC-0007 / RFC-0022 **REJECT** `TRADE_REJECTED` → deceptive. An implementer would treat a legal decline as a lie, or collapse deceptive into danger.

## Proposed change

Accept GC3-S6:

- Distinct directed subject→object edge, separate from S1 danger
- Evidence (closed):
  - `AGREEMENT_BROKEN`: every other `party_id` → `broken_by` (same event may also credit S1 danger)
  - Contradicted public `ATTEST`: two `visibility=PUBLIC` attestations on the same `subject_entity_id` with opposite `archive_claim`; the earlier attester is the object
- `TRADE_REJECTED`, `CONTEST_DECLARED`, `CONTEST_RESOLVED`, `MESSAGE` do **not** credit deceptive
- Self PLAY: `You have found {name} deceptive.`
- WATCH only via GC3-S2 when the evidence is already public; this catalog stays `watch_projection: false`

Catalog: [`social-memory-catalog.gc3-s6.json`](../specs/social-memory-catalog.gc3-s6.json).  
Slice: [GC3-S6-DECEPTIVE.md](../docs/GC3-S6-DECEPTIVE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `TRADE_REJECTED` → deceptive | Legal decline (RFC-0007 / RFC-0022) |
| Merge into S1 danger | Collapses promise-breaking into hostility |
| MESSAGE text as public lie | Private; recipient-only |
| New LIE / ACCUSE verb | Verb inflation |

## Compatibility

Additive derived projection. S1 `AGREEMENT_BROKEN` → danger remains.

## Data / security

Rebuildable. No amounts, hidden ids, or claim method text in the line.

## Validation

`check_gc3_s6`: public agreement break → deceptive; rejected trade → empty; contradicted public ATTEST → deceptive for the first attester; WATCH empty on this slice.

## Rollback

Omit the deceptive projection. S1 danger and S2 public bands remain.

## Unresolved

None. Remaining SOCIAL-MEMORY SPEC GAP list is closed by RFC-0034–0038.
