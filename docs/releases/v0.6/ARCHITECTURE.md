# v0.6 Deep Time: Architecture Delta

## Product surfaces

| Mode | Deep Time experience |
|---|---|
| PLAY | Old places, scars, institutions, incomplete local history |
| WATCH | Timeline drama: foundings, successions, collapses, discoveries |
| STUDY | Longitudinal questions about persistence, succession, reconstruction |

## Machine stack

```text
Event ledger + snapshots (canonical)
  → institutions / succession / artifacts / scars (derived records)
  → historical evidence + claims
  → reconstruction / archaeology (agent-visible)
  → experience projections (simple → reproducibility)
```

## Progressive disclosure

Same underlying history at four levels (simple scar/age → player history → lineage/provenance → digests/version pins).

## Event catalog

No new closed catalog version in this package. Succession and institution records are evidence-grounded derived structures. Catalog expansion requires RFC (see [SUCCESSION.md](../../SUCCESSION.md)).

## Admin-only Genesis (one-time)

```text
ADMIN CREATE WORLD
  → Profile (3)
  → optional Story Seeds
  → Seed
  → Preview
  → Activate
  → CYCLE 0 ordinary world
  → PLAY (no Genesis surface)
```

Genesis is not a runtime subsystem. After activation, configuration is immutable; another Genesis run means another world. Reuse Chamber + Deep Time contracts for Cycle 0 content. See [GENESIS.md](../../GENESIS.md).

## RFC-0003

Reuse `noema-jcs/1`, content hashing, state lineage, receipts, catalog admission, recovery fencing.

## Extension Points

Non-normative prospective guidance; this section neither changes release scope nor authorizes execution.

### Historical projection adapters

Future PLAY, WATCH and STUDY readers can offer different levels of disclosure from the same ledger/snapshot lineage. Names, reconstructions and significance remain derived; neither an interpretation nor an Admin Story Seed becomes public world truth.

Preserve noema-jcs/1, receipts, recovery fencing and accepted exposure rules. New event semantics require an RFC; new Genesis means a distinct world, not a running-history edit. Validate public versus authorized views, conflicting claims, replay-stable derivations and immutable post-activation configuration.
