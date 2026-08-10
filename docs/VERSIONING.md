# Versioning

## Version domains

- Product: NOEMA `0.1.0` (Chamber), `0.2.0` (Frontier), `0.3.0` (Observatory)
- Spec pin: Noema-Specs release / pin (e.g. `v0.1.0-rc2`, `v0.2.0-draft`)
- World rules: `world/v1`
- World instance: `world_id` + `world_version`
- Agent protocol: `agent-protocol/v1`
- MUD command protocol: `mud-command/v1`
- Event schema: `event-schema/v1`
- Event catalog: `event-catalog/0.1` (24 types), `event-catalog/0.2` (31 types; RFC-0002)
- Contest rules: `contest-rules/0.2.0`
- Agreement rules: `agreement-rules/0.2.0`
- Replay protocol: `replay-protocol/v1`
- Situation genome: `situation-genome/0.2` (legacy samples may use `1.0`)
- Frontier director: `frontier-director/0.2`
- Novelty axes: `novelty-axes/0.2`
- Mutation catalog: `mutation-catalog/0.2`
- Noise model: `noise-model/0.2`
- Trajectory: `trajectory/0.3` (legacy samples may use `1.0`)
- Behavior features: `behavior-features/0.3`
- Observatory: `observatory/0.3`
- Anomaly detectors: `anomaly-detectors/0.3`
- Capability ontology: `capability-ontology/0.1`
- Phenomena ontology: `phenomena-ontology/0.1`
- Dataset: `atlas-2026.1`

## Runtime pinning

Running instances MUST expose a [runtime manifest](../specs/runtime-manifest.schema.json) binding product, spec, world rules, protocol, catalog, seed digest, configuration digest, cycle, ledger head, and snapshot head. Application upgrades MUST NOT silently change world semantics; incompatible rules require explicit migration or a new `world_version`. See [DEPLOYMENT.md](DEPLOYMENT.md) and [OPERATIONS.md](OPERATIONS.md).

## Rules

Implementation repositories MUST declare compatible spec versions. Schema-breaking changes require version bumps. Ontology changes do not automatically bump network protocols. Dataset releases are immutable. Reproducibility Bundles record all versions.

## Compatibility

Additive schema fields may be allowed only when `additionalProperties` and version negotiation permit them. Protocol-breaking changes require a new protocol version and migration plan. Making previously required manifest fields optional (minimal registration) is a compatible relaxation for clients; servers MUST continue to accept full advanced manifests.

Changing Frontier scoring constants, mutation semantics, novelty axis definitions, or canonicalization rules MUST create a new relevant version identity (`director_version` / axes / catalog pin). See [releases/v0.2/MIGRATION.md](releases/v0.2/MIGRATION.md).
