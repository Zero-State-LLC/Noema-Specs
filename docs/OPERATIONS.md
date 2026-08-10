# Operations

Normative small ops surface for v0.1 reference deployments. Runtime CLI names MAY vary in presentation but MUST provide equivalent semantics.

## Commands

```bash
noema backup
noema restore <bundle>
noema verify
```

| Command | MUST |
|---------|------|
| `noema backup` | Produce a portable bundle of world durable state, event ledger, snapshots, runtime manifest, and non-secret configuration digest |
| `noema restore <bundle>` | Restore into a clean compatible environment; refuse incompatible version lineage without explicit migration flags |
| `noema verify` | Run the verification checklist below and exit non-zero on any failure |

## `noema verify` checklist

`noema verify` MUST check at minimum:

1. Resolved config validity (parses; validates against [deployment-config.schema.json](../specs/deployment-config.schema.json))
2. Database connectivity
3. Schema version (migrations applied; match expected product pin)
4. Spec compatibility (`spec_version` / protocol / catalog pins)
5. Ledger integrity (digest chain, no gaps)
6. Snapshot integrity (heads reachable; digests match)
7. Object/blob storage availability (filesystem adapter acceptable in local mode)
8. Seed / replay fixture load (when present)
9. Runtime manifest integrity ([runtime-manifest.schema.json](../specs/runtime-manifest.schema.json))

Successful completion MUST print:

```text
NOEMA VERIFY: PASS
```

Fixture: [examples/deployment/verify-pass.example.txt](../examples/deployment/verify-pass.example.txt)

## Backup contents (minimum)

- `world_id`, `world_version`, product/spec/protocol/catalog pins
- Event ledger from genesis (or declared snapshot + delta range)
- Latest and genesis-linked snapshots
- Runtime manifest at backup time
- Non-secret configuration digest (never secret values)
- Object/blob references required for restore

Secrets (auth keys, provider keys, DB passwords) MUST NOT be embedded in public bundles. Operators MAY store encrypted secret sidecars out of band.

## Restore rules

1. Target environment MUST be version-compatible with the bundle’s runtime manifest.
2. Restore MUST NOT invent a new genesis for an existing `world_id` + `world_version`.
3. After restore, `noema verify` MUST pass.
4. Replay under ADR-005 MUST remain `EQUIVALENT` for the restored Chamber state when fixtures are included.

## Upgrade and rollback

### Application upgrade

Application lifecycle and **world lifecycle are separate**.

A code deployment / process restart MUST NOT:

- reset the world;
- reset economy/resources;
- recreate agents;
- erase faction or organization history;
- reset cycles;
- erase ledger history.

A code deployment MUST NOT silently change the meaning of an existing world.

### Version pinning

Every world MUST be pinned to explicit lineage including at minimum:

```text
world_id
world_version
product_version
spec_version
world_rules_version
agent_protocol_version
event_catalog_version
seed or seed digest
configuration digest
current cycle
ledger head
snapshot head
```

Machine-readable form: [runtime-manifest.schema.json](../specs/runtime-manifest.schema.json).

### Incompatible rules

An incompatible `world_rules_version` (or event catalog semantics change) MUST:

1. **fail closed** on boot against an existing world, or
2. require an **explicit migration** to a new `world_version` with recorded provenance.

Silent semantic adoption is forbidden.

### Rollback

1. Roll back application binaries/images to a build compatible with the world’s pinned versions.
2. If a failed migration partially applied, restore from the pre-migration backup bundle.
3. Run `noema verify`.
4. Do not “fix” history by truncating the ledger except via an RFC-approved disaster procedure with explicit claim labels.

## Health surfaces

| Path | Meaning |
|------|---------|
| `/health` | Process is up |
| `/ready` | DB reachable, schema current enough to serve, world loadable |
| `/version` | Product, spec, protocol, and world pins (aligned with runtime manifest fields) |

## Persistence invariant (BRE-like continuity)

NOEMA is a persistent strategic world. Structural continuity is inspired by long-running BBS strategy games such as Barren Realms Elite:

- factions/organizations persist;
- resources persist;
- production persists;
- infrastructure persists;
- strategic consequences accumulate across cycles;
- history survives process restart and application upgrades.

This is a **structural** reference, not a literal clone.

## Conformance

Ops behavior is covered by C14–C17 in [v0.1 Conformance](v0.1-CONFORMANCE.md).
