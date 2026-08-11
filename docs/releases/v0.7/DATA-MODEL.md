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
