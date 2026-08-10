# Versioning

## Version domains

- Product: NOEMA 0.1.0
- Spec pin: Noema-Specs release / pin (e.g. `0.1.0`, `v0.1.0-rc2`)
- World rules: `world/v1`
- World instance: `world_id` + `world_version`
- Agent protocol: `agent-protocol/v1`
- MUD command protocol: `mud-command/v1`
- Event schema: `event-schema/v1`
- Event catalog: `event-catalog/0.1`
- Replay protocol: `replay-protocol/v1`
- Capability ontology: `capability-ontology/0.1`
- Phenomena ontology: `phenomena-ontology/0.1`
- Dataset: `atlas-2026.1`

## Runtime pinning

Running instances MUST expose a [runtime manifest](../specs/runtime-manifest.schema.json) binding product, spec, world rules, protocol, catalog, seed digest, configuration digest, cycle, ledger head, and snapshot head. Application upgrades MUST NOT silently change world semantics; incompatible rules require explicit migration or a new `world_version`. See [DEPLOYMENT.md](DEPLOYMENT.md) and [OPERATIONS.md](OPERATIONS.md).

## Rules

Implementation repositories MUST declare compatible spec versions. Schema-breaking changes require version bumps. Ontology changes do not automatically bump network protocols. Dataset releases are immutable. Reproducibility Bundles record all versions.

## Compatibility

Additive schema fields may be allowed only when `additionalProperties` and version negotiation permit them. Protocol-breaking changes require a new protocol version and migration plan. Making previously required manifest fields optional (minimal registration) is a compatible relaxation for clients; servers MUST continue to accept full advanced manifests.
