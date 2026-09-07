# v0.7 LEARN: Data Model Delta

| Record | Schema | schema_version |
|---|---|---|
| BehaviorNode | `specs/behavior-node.schema.json` | `behavior-node/0.7` |
| CapabilityEdge | `specs/capability-edge.schema.json` | `capability-edge/0.7` |
| CapabilityGraph (optional disposable) | `specs/capability-graph.schema.json` | `capability-graph/0.7` |

Domain pin: `capability-graph/0.7`.

Edge types (closed): `OBSERVED_IN` · `REPRODUCED_BY` · `DEPENDS_ON` · `FAILS_WITHOUT` · `GENERALIZES_TO` · `DIFFERS_ACROSS_VERSION`.

Target classes: `AGENT_VERSION` · `CONDITION` · `CONTEXT` · `BEHAVIOR`.

Relationship status: `SUPPORTED` · `CONTESTED` · `INSUFFICIENT`.

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** The data-model guide can add examples of contested and insufficient capability relationships and disposable graph reconstruction.
- **Unchanged invariants:** The six edge types, four target classes, and three relationship statuses remain closed under capability-graph/0.7.
- **Compatibility, promotion, and verification:** Additional relationships or fields require a versioned schema/domain change with migration behavior, not prose-only vocabulary expansion. Validate nodes and edges, reject unknown enums, and verify rebuilding the optional graph preserves evidence-linked relationships.
