# RFC-0042 — GC7-S3 Information Contest Form

## Status

**Accepted**

Specification-only until hosted. One new form string. No `event-catalog/0.3`. No new verbs. No HP. Chamber help still omits CONTEST.

## Problem

[STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md) lists information as a contest target but left the form as SPEC GAP. An implementer would invent `SCAN`, leak hidden archive facts through contest UI, rewrite `archive_claim` as a second writer, or mutate `event-catalog/0.2`.

## Proposed change

Accept GC7-S3:

- One added form: `INFORMATION_CONTEST`
- Target: a **visible** `ARTIFACT` already in the contest room (a public record)
- Missing or non-visible target is `NOT_FOUND` (same as any missing object — no hidden/not-hidden distinction)
- Visible non-record is `FORBIDDEN`
- `INFORMATION_WAR` and other unknown strings stay `FORM_FORBIDDEN`
- Success/partial emits existing `ENTITY_UPDATE` sealing further `INSPECT` for a published number of cycles
- World `archive_claim` is **not** rewritten. ATTEST remains the claim writer
- WATCH / contest projection: public form + public target when already observable. No hidden ids, no claim contents
- Institution `acting_for` uses office profile `ACCESS_RESTRICTED_ARCHIVE`
- `event-types.0.2.json` contest_form enum is **not** mutated. `CONTEST_DECLARED` / `CONTEST_RESOLVED` MAY carry this form at the conflict-catalog layer

Catalog: [`conflict-catalog.gc7-s3.json`](../specs/conflict-catalog.gc7-s3.json).  
Slice: [GC7-S3-INFORMATION-CONTEST.md](../docs/GC7-S3-INFORMATION-CONTEST.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| No form; compose ATTEST + ACCESS_CONTEST only | Leaves information off the contest target list |
| Mutate `event-catalog/0.2` or open `0.3` | Catalog increment for a form string |
| `SCAN` / leak unread claims | Hidden-fact leak |
| Contest rewrites `archive_claim` | Second writer |
| Chamber help lists contest | RFC-0011 help pin |

## Compatibility

Additive form. The four v0.2 forms and S0–S2 rules unchanged. `contest-rules/0.2.0` digest arithmetic unchanged.

## Data / security

Sealed `INSPECT` fails closed without returning claim text. Prior discovery evidence is not wiped.

## Validation

`check_gc7_s3`: public artifact ACCEPT; missing `NOT_FOUND`; non-record `FORBIDDEN`; `INFORMATION_WAR` `FORM_FORBIDDEN`; hidden-in-projection `LEAK`; no new verbs/events/HP.

## Rollback

Treat `INFORMATION_CONTEST` as `FORM_FORBIDDEN` (S0 four forms).

## Unresolved

Broader information warfare (forced publication, claim flip). Broader conflict-of-interest beyond GC7-S2.
