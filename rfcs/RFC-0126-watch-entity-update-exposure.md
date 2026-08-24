# RFC-0126 — WATCH `ENTITY_UPDATE` exposure closure

## Status

**Accepted**

No new events. No new WATCH surface. No `WR-S*` slice. Existing specifically
authorized WATCH projections remain unchanged.

## Problem

The public WATCH renderer has specific copy for the `REPAIR` and `PRODUCTION`
forms of `ENTITY_UPDATE`, but every other non-silent form falls through to the
generic line `Public activity at <site>`. Four emitted operations currently
reach that fallback: `HARVEST`, `ATTEST`, `INFORMATION_CONTEST`, and
`PRESENCE_PRESSURE`.

The fallback makes exposure an accident of event shape. It also publishes a
new operation automatically unless a renderer author remembers to add a mute.
That reverses the public-door rule: silence must be the default until a public
projection is explicitly accepted.

`HARVEST` demonstrates the concrete defect. One act emits both a
`RESOURCE_TRANSFER` and an `ENTITY_UPDATE`, producing two public lines:

```text
Harvest at <site>
Public activity at <site>
```

The first line is the canonical public account. The second carries no distinct
public fact.

## Proposed change

Close the generic `ENTITY_UPDATE` surface:

- `ENTITY_UPDATE/HARVEST` is WATCH-silent. The sibling
  `RESOURCE_TRANSFER/HARVEST` remains the one public line: `Harvest at <site>`.
- `ENTITY_UPDATE/ATTEST` is WATCH-silent. RFC-0020 keeps claim text off WATCH;
  a generic line must not disclose the existence of an otherwise unprojected
  attestation.
- `ENTITY_UPDATE/INFORMATION_CONTEST` is WATCH-silent. Its public contest
  account, when allowed by RFC-0042, comes from the contest events, not from the
  mutation that applies the inspection seal.
- `ENTITY_UPDATE/PRESENCE_PRESSURE` is WATCH-silent. Its public contest account
  comes from the contest events; the mutation that applies a bounded disable is
  not a second spectator event.
- An unnamed or unrecognized `ENTITY_UPDATE.operation` is WATCH-silent by
  default. A future operation requires an accepted exposure decision and an
  explicit projection before it can reach the public feed.
- Existing explicit `ENTITY_UPDATE` projections, including `REPAIR`,
  `PRODUCTION`, and already-authorized infrastructure state projections, remain
  unchanged.
- Existing RFC-authorized silences remain unchanged and are not re-specified by
  this RFC.

This is a renderer allowlist boundary, not a new report family or a new WATCH
surface.

Machine contract:
[`watch-entity-update-exposure.rfc-0126.json`](../specs/watch-entity-update-exposure.rfc-0126.json).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Keep the generic fallback | Future operations become public without an exposure decision |
| Keep both HARVEST lines | Two lines describe one act; the generic line adds no fact |
| Add specific ATTEST copy | Risks exposing claim activity that RFC-0020 keeps off WATCH |
| Add specific contest-effect copy | Duplicates the public contest account and exposes internal effects |
| Create a `WR-S*` slice | This closes an existing WATCH leak surface; it does not add a report surface |

## Compatibility

Subtractive public presentation only. Ledger events, PLAY, Admin surfaces,
world state, and event catalogs are unchanged. Consumers must not depend on the
generic `Public activity at <site>` line as an event-complete stream.

## Data / security

No stored data changes. The public feed becomes fail-closed for new
`ENTITY_UPDATE` operations. Hidden-room and entity-site redaction remain
unchanged.

## Validation

Runtime tests MUST pin:

1. the four named operations produce no `ENTITY_UPDATE` WATCH item;
2. one HARVEST act still produces exactly one canonical harvest line through
   `RESOURCE_TRANSFER`;
3. an unnamed or unknown operation produces no WATCH item;
4. `REPAIR`, `PRODUCTION`, and existing explicitly authorized infrastructure
   projections remain unchanged; and
5. the existing hidden-room sweep remains green.

The Specs validator MUST load the machine contract, resolve its authority path,
and confirm its operation sets are disjoint and its default is silent.

## Rollback

Restore the prior generic fallback. This reopens implicit public exposure and
is therefore a contract rollback, not a presentation-only revert.

## Unresolved

None. Any future `ENTITY_UPDATE` exposure is a separate RFC.
