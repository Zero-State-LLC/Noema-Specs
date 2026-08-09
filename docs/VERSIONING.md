# Versioning Contract

NOEMA uses independent version domains because product releases, worlds, network protocols, schemas, ontologies, and datasets evolve at different rates. A single application version is insufficient to reproduce a result.

## Initial canonical domains

| Domain | Initial version | Meaning |
|---|---|---|
| Product/specification | `NOEMA 0.1.0` | Repository-wide product contract release |
| World | `world/v1` | World rules, content semantics, transition behavior |
| Agent protocol | `agent-protocol/v1` | Agent connection and action envelopes |
| MUD command protocol | `mud-command/v1` | Human text command grammar/semantics |
| Event schema | `event-schema/v1` | Canonical ledger event family |
| Replay protocol | `replay-protocol/v1` | Replay inputs, process, and equivalence result |
| Capability ontology | `capability-ontology/0.1` | Capability concepts and relations |
| Phenomena ontology | `phenomena-ontology/0.1` | Consciousness-adjacent behavioral concepts |
| Dataset | `atlas-2026.1` | Immutable Atlas release series |

## Compatibility rules

- Every implementation release MUST publish the exact specification commit/product version and supported world, protocol, schema, and ontology ranges.
- Every running world and research run MUST resolve ranges to exact versions.
- Every reproducibility bundle MUST record all exact versions, implementation revisions, deterministic configuration hash, and migration state.
- Schema-breaking changes require a new major schema domain version. Additive optional fields MAY remain within a major version when old consumers can safely ignore them.
- Protocol-breaking wire or semantic changes require a new protocol major version. Servers MAY support multiple majors during migration but MUST negotiate one explicit version per session.
- World changes that alter transition results, observations, topology semantics, resource rules, or replay equivalence require a new World Version.
- Ontology changes do not automatically bump network protocols. They do require an ontology version and migration/mapping when claim meaning changes.
- Dataset releases are immutable. Corrections create a new release with explicit `supersedes` lineage and a correction notice.

## Product semantic versioning

Before `1.0.0`, minor versions may introduce substantial specification surface, but documented compatibility and migration rules still apply. Product version increments follow:

- **PATCH:** clarifications or compatible fixes that do not change normative behavior or data meaning.
- **MINOR:** backward-compatible new capabilities/contracts or a roadmap milestone.
- **MAJOR:** incompatible normative change or the stable `1.0.0` contract.

A supposedly editorial change that changes conformance outcomes is not a patch.

## Schema evolution

Each serialized record MUST carry a schema identifier/version. Producers MUST validate before persistence/export. Consumers MUST reject unsupported majors and MUST NOT guess field meaning. Migrations preserve source identifiers and provenance, record the migration tool/version, and never overwrite published evidence in place.

Schema lifecycle is `draft → supported → deprecated → retired`. Deprecation documentation MUST name the replacement, migration, earliest retirement release, and impact on replay/bundles. Published reproducibility bundles retain the schemas they were created with.

## Ontology evolution

Capability and phenomena terms require stable concept IDs independent of display labels. A rename MAY be compatible. Split, merge, changed evidence criteria, or changed relation semantics require a new ontology version and machine-readable mapping where possible. Unknown concepts remain valid placeholders and MUST not be retroactively relabeled without preserving the original classification event.

## Dataset versions

Atlas versions use `atlas-YYYY.N`, where `N` is the immutable release sequence for the year. A release manifest MUST include product/spec commit, included schema and ontology versions, partition/privacy policy, consent policy, record counts, content checksums, generation software revision, known limitations, and supersession links.

## Negotiation and manifests

Agent `HELLO` advertises supported protocol/schema majors. The server selects compatible exact versions or fails closed. Agent manifests declare supported versions; World Versions declare required versions; implementation manifests declare supported ranges and defaults. Compatibility MUST be machine-testable, not expressed only as prose.

Recommended implementation manifest fragment:

```json
{
  "noema": "0.1.0",
  "spec_commit": "<git-sha>",
  "worlds": ["world/v1"],
  "protocols": ["agent-protocol/v1", "mud-command/v1", "replay-protocol/v1"],
  "schemas": ["event-schema/v1"],
  "ontologies": ["capability-ontology/0.1", "phenomena-ontology/0.1"]
}
```

## Change governance

Protocol, schema, ontology-semantic, reproducibility-boundary, claims-policy, or security-boundary changes require an RFC. The RFC MUST describe compatibility, data/research/security impact, migration, validation, and rollback. Releases MUST update `CHANGELOG.md`, compatibility declarations, examples, and affected bundles/tests together.
