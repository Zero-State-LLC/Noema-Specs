# RFC-0020 — Archive-Claim Attestation (later COMMIT.ATTEST)

## Status

**Accepted**

Specification-only. Does **not** implement runtime. Does **not** thaw Chamber help. Does **not** reseed Genesis. Does **not** make `INSPECT` a writer.

## Problem

RFC-0015 named archive-claim fields. RFC-0018 named the writers (`ENTITY_CREATE` / allowlisted `ENTITY_UPDATE`) and forbade `INSPECT`. Perihelion still has no fields, so hosted GC6 stays silent. The remaining SPEC GAP was *which Player action* may emit that allowlisted update. An implementer would parse flavor text or ship a destroyed-relay pack.

## Proposed change

One later `COMMIT` operation: `ATTEST`.

| Field | Contract |
|-------|----------|
| Wire | `COMMIT` + `operation=ATTEST` |
| Human adapter (later) | `attest <artifact> subject=<entity_id> claim=DESTROYED\|OPERATING` |
| Target | Visible co-located `ARTIFACT` |
| Writes | Both `archive_subject_entity_id` and `archive_claim` together |
| Claim set | `DESTROYED` \| `OPERATING` only |
| Events | Existing `BUDGET_CONSUMED` then allowlisted `ENTITY_UPDATE` |
| Not a writer | `INSPECT`, `LOOK`, World Services, WATCH, Admin flavor, Genesis |
| Immutability | First successful set is immutable (RFC-0018) |
| Help | Omit `ATTEST` even after a later thaw (same S0 out-of-list rule as BUILD/CONTEST) |
| Cost (pinned for the later pass) | attention 2 (same as `INSPECT`; fail closed before debit) |

Players must name subject and claim. The adapter MUST NOT infer them from labels or room text.

Failure codes for the later pass: `NOT_COLOCATED`, `NOT_FOUND`, `FORBIDDEN` (not an ARTIFACT / already set / unpaired fields), `BUDGET_EXCEEDED`.

No `QUEST`, `DISCOVER`, or `event-catalog/0.3`.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `INSPECT` writes the claim | RFC-0018 |
| Flavor-text parse | RFC-0015 |
| Genesis DESTROYED pack | First-world freeze |
| New `RECORD` / `DISCOVER` verb | Verb per noun |
| GC2 CONSTRUCT of an archive artifact | GC2-S0 classes are the four infrastructure types only |

## Compatibility

Additive later operation on existing `COMMIT`. Frozen v0.1 required help unchanged. GC6 mapper already reads the fields.

## Data / security

No wallet fields. Hidden rooms are not attest targets. WATCH stays empty of claim text.

## Validation

`check_rfc_0020`: Accepted; `ATTEST` on `COMMIT`; `INSPECT` not a writer; no Genesis pack; runtime not authorized here.

## Rollback

Leave unused. `COMMIT.ATTEST` stays unsupported. GC6 remains silent on Perihelion.

## Unresolved

Exact later cost if Chamber attention economy is retuned. Amendment of an immutable claim (separate RFC).
