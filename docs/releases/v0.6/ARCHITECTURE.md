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
