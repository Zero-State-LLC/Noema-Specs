# Versioning

## Version domains

- Product: NOEMA 0.1.0
- World: `world/v1`
- Agent protocol: `agent-protocol/v1`
- MUD command protocol: `mud-command/v1`
- Event schema: `event-schema/v1`
- Replay protocol: `replay-protocol/v1`
- Capability ontology: `capability-ontology/0.1`
- Phenomena ontology: `phenomena-ontology/0.1`
- Dataset: `atlas-2026.1`

## Rules

Implementation repositories MUST declare compatible spec versions. Schema-breaking changes require version bumps. Ontology changes do not automatically bump network protocols. Dataset releases are immutable. Reproducibility Bundles record all versions.

## Compatibility

Additive schema fields may be allowed only when `additionalProperties` and version negotiation permit them. Protocol-breaking changes require a new protocol version and migration plan.
