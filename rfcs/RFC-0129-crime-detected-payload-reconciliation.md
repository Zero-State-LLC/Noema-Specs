# RFC-0129 — Reconcile `CRIME_DETECTED` payload with the GC3 evidence contracts

## Status

**Draft**

Proposed, not accepted. It amends a closed catalog payload, which is a product
decision. See [Decision required](#decision-required).

Closes `B7a` in [SPEC-GAP-REGISTER-2026-08-25.md](../docs/SPEC-GAP-REGISTER-2026-08-25.md).
Amends the `event-catalog/0.2` pin in the manner of [RFC-0127](RFC-0127-trade-cancelled-catalog.md).
Does not open `event-catalog/0.3`. Does not change Chamber `event-catalog/0.1` (24 types).
Does not add a `CRIME_DETECTED` producer, a verb, Genesis, or a detection algorithm.
Does not retune the published −3 / −8 / −15 ladder.

## Relationship to the GC7 proposal note

[RFC-PROPOSAL-GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION.md](RFC-PROPOSAL-GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION.md)
was created on `main` from
[GC7-CRIME-PAYLOAD-VICTIM-SEED.md](../docs/GC7-CRIME-PAYLOAD-VICTIM-SEED.md)
after this RFC was drafted. Both address `B7a`, so one of them has to be the
authority for that row.

That note is a framing proposal: it names the same contradiction and offers the
same two exits the register lists — declare the fields, **or** make
`PUBLIC_HISTORY` plus a derived victim the single canonical form — without
choosing between them. This RFC takes the first exit and specifies it: which two
properties, what types, why optional, and how the two Accepted definitions of
"public" are made co-extensive rather than one being dropped.

It therefore **supersedes** that note, which is marked accordingly. Nothing in
the note is contradicted; the framing, boundaries, and citations carry over.
Anyone preferring the second exit should reject this RFC and say so on the row,
rather than keeping two live artifacts for one gap.

## Problem

Three **Accepted** authorities reference fields on `CRIME_DETECTED` that no
machine schema provides. The payload is `additionalProperties: false`, and so is
the event envelope.

| Authority | References | Machine schema |
|---|---|---|
| [GC3-S1-BETRAYAL.md](../docs/GC3-S1-BETRAYAL.md) §Evidence — "named `victim_id` → `subject_id` only (no omniscient public mark)" | `victim_id` | absent from payload |
| [GC3-S2-WATCH-PUBLIC.md](../docs/GC3-S2-WATCH-PUBLIC.md) §Bands — public "only `visibility=PUBLIC`" | `visibility` | absent from payload |
| [RFC-0094](RFC-0094-crime-report.md) §Proposed change — public means `flags` includes `PUBLIC_HISTORY` **or** host `visibility` is `PUBLIC` | `visibility` on the host event | absent from [`world-event.schema.json`](../specs/world-event.schema.json), which is also `additionalProperties: false` |

The payload can only ever carry `flags: ["PUBLIC_HISTORY"]`.

**Two Accepted authorities therefore define "public" for the same event
differently.** GC3-S2 gates the public danger band on `visibility=PUBLIC` alone.
RFC-0094 gates world-report lines on `PUBLIC_HISTORY` **or** `visibility=PUBLIC`.
A record carrying only `PUBLIC_HISTORY` — the one shape the closed payload
permits — is public for the world report and not public for social memory, by
specification. That divergence is the defect this RFC must close, not merely the
two missing properties.

The hosted Worker implements the slice contracts. The payload is therefore the
outlier, and a schema-valid crime record cannot produce the memory effects its
own Accepted slices specify. Consumers split three ways:

| Consumer | Gate | Implements | Fires today |
|---|---|---|---|
| `social-memory.ts` dyadic danger edge | requires `victim_id` | GC3-S1 | **No** |
| `social-memory.ts` public danger band | `visibility === "PUBLIC"` | GC3-S2 | **No** |
| `world-actions.ts` `public_social_events` | `visibility === "PUBLIC"` | GC3-S2 pattern | **No** |
| `world-reports.ts` crime lines | `visibility` **or** `PUBLIC_HISTORY` | RFC-0094 | Yes |
| `watch-live.ts` projection | `visibility` **or** `PUBLIC_HISTORY` | RFC-0094 pattern | Yes |

No consumer is wrong on its own terms. Each implements the authority that governs
it; the authorities disagree.

[EVENT-CATALOG-AUDIT.md](../docs/EVENT-CATALOG-AUDIT.md) recorded that adding
`visibility` or `victim_id` was outside its scope, so the omission is deferred
rather than overlooked. Nothing produces `CRIME_DETECTED` in either plane today,
so no ledger data depends on the current shape.

## Proposed change

Add two optional properties to `CRIME_DETECTED_payload`. Both mirror conventions
already in `event-catalog/0.2`.

```json
"victim_id": { "type": "string", "pattern": "^[A-Za-z0-9_.:-]+$" },
"visibility": { "enum": ["PARTIES", "PUBLIC"] }
```

- **`victim_id` is optional.** GC3-S1 credits the *named* victim only. A crime
  with no named victim carries no dyadic edge, which is the existing behavior.
- **`visibility` is optional and mirrors `AGREEMENT_BROKEN_payload`** — the
  nearest analogue, a hostile event feeding the same danger memory through the
  identical runtime gate. Absent means not public. This is fail-closed and is
  what all five consumers already implement.
- **`PUBLIC_HISTORY` keeps its ladder meaning, and the two definitions of
  "public" are reconciled by making them co-extensive.** RFC-0002 lists public
  history as a sanction tier, distinct from whether the event is publishable. A
  producer that sets either `PUBLIC_HISTORY` or `visibility: "PUBLIC"` MUST set
  both. RFC-0094's `or` then selects the same records as GC3-S2's stricter test,
  so both Accepted definitions stay literally true and can never disagree. This
  is the one rule that closes the divergence without amending either RFC.

Required fields, the severity and category enums, the flags enum, and every other
property are unchanged. The catalog stays at 32 types; no type is added or removed.

**No runtime change is required.** After this amendment the existing Worker
consumes the canonical payload correctly at all five sites, because each already
reads exactly these fields.

## Alternatives rejected

| Alternative | Why not |
|---|---|
| Make `PUBLIC_HISTORY` plus a derived victim the single canonical representation | Requires amending two **Accepted** GC3 slice contracts and changing three runtime consumers, and requires pinning a new deterministic victim-derivation rule. It contradicts accepted authority to avoid a payload edit that no ledger data depends on |
| Open `event-catalog/0.3` | RFC-0127 set the precedent that a 0.2 omission is amended in place. Nothing here adds or removes a type |
| Leave the contradiction and forbid a future producer | The gap is already registered as blocking; deferring it again does not make the three Accepted authorities satisfiable |
| Amend GC3-S2 or RFC-0094 so only one definition of "public" survives | Both are Accepted and each is correct for its own surface. Making the two tests co-extensive preserves both texts and needs no RFC amendment |
| Fix it in the runtime by relaxing the consumers | The runtime is not wrong. Relaxing consumers would make them diverge further from the slice contracts |

## Conformance

On acceptance:

1. Apply the two properties to `specs/event-types.0.2.json`.
2. Add a schema-valid fixture carrying `victim_id` and `visibility: "PUBLIC"`,
   and one carrying neither.
3. Add a conformance case feeding the exact schema-valid fixture through dyadic
   danger memory, the public danger band, `public_social_events`, world reports,
   and the WATCH projection — the failure this RFC exists to prevent is a record
   that validates and then produces nothing.
4. Assert the co-extensiveness rule in both directions: `PUBLIC_HISTORY` without
   `visibility: "PUBLIC"` is invalid, and `visibility: "PUBLIC"` without
   `PUBLIC_HISTORY` is invalid.
5. Assert that GC3-S2's gate and RFC-0094's gate select the same set of records
   for every fixture — the divergence must be untestable after this lands.

## Non-goals

This RFC reconciles a payload. It does **not** resolve the rest of the crime gap,
which stays registered and open:

| Row | Still open |
|---|---|
| `B7b` | detection has no normative algorithm; published constants have no runtime referent |
| `B7c` | detection and sanction are conflated — RFC-0002 calls the event "not automatic guilt broadcast" while the payload requires an influence debit |
| `B7d` | formal enforcement has no cost, jurisdiction, or accountable steward |
| `B7e` | rehabilitation is severity-blind and counts ordinary trades where SOCIAL-MEMORY.md says "restitution trades" |

Design input for those rows is recorded non-normatively in
[Research Assimilation — Crime](../docs/RESEARCH-ASSIMILATION-2026-08-25-CRIME.md)
and [NOTES-CRIME-DETECTION-EVIDENCE.md](../docs/research/NOTES-CRIME-DETECTION-EVIDENCE.md).

## Decision required

Two questions belong to a human, not to an implementer:

1. **Accept the amendment at all.** It edits a closed catalog payload. The
   argument for is that three Accepted authorities are currently unsatisfiable,
   two of them disagree about what "public" means, and no ledger data depends on
   the present shape; the argument against is that a closed catalog should stay
   closed until a producer actually needs it.
2. **Whether `visibility` should carry `"default": "PARTIES"`.**
   `AGREEMENT_FORMED_payload` declares that default; `AGREEMENT_BROKEN_payload`
   does not. This RFC follows `AGREEMENT_BROKEN` as the nearer analogue, so absent
   is fail-closed by consumer behavior rather than by declared default.

Until both are settled this RFC stays **Draft**, and `specs/event-types.0.2.json`
is unchanged by the PR that introduces it.
