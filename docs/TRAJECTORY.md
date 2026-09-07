# Trajectory (v0.3)

A **versioned, content-addressed ordered research view** over canonical records.

Machine authority: [`specs/trajectory.v03.schema.json`](../specs/trajectory.v03.schema.json) (`trajectory/0.3`).
Legacy samples may use `trajectory/1.0` ([trajectory.schema.json](../specs/trajectory.schema.json)).

## Required fields (`trajectory/0.3`)

| Field | Notes |
|-------|--------|
| `trajectory_id` | stable ID |
| `trajectory_version` | content version |
| `world_id`, `world_version` | lineage |
| `agent_id`, `agent_version` | focal agent (multi-agent lists optional) |
| `start_cycle`, `end_cycle` | inclusive window |
| `event_refs` | ordered event_ids (not full mutable copies) |
| `observation_refs` | observation_ids |
| `action_refs` | action_ids when known |
| `message_refs` | message_ids |
| `tool_call_refs` | tool request ids |
| `world_context_refs` | snapshot/regime digests |
| `experiment_id` | optional |
| `frontier_genome_id` | optional |
| `consent_basis` | research consent record id/digest |
| `visibility_partition` | `research` \| `restricted` \| `exportable` |
| `feature_version` | feature catalog pin for derived views |
| `kind` | see types below |
| `digest` | content digest |

## Kinds

| kind | Meaning |
|------|---------|
| `complete` | full available history for agent/world in range |
| `bounded_window` | fixed [start,end] |
| `rolling` | declared rolling length ending at end_cycle |
| `episode` | segment with explicit segment_id |
| `redacted` | fields/refs omitted per consent |
| `invalid` | fails schema or lineage checks |

Missing intervals MUST be explicit (`missing_intervals[]`), never silently filled.

## Rules

* Reference canonical evidence; do not copy mutable state as truth.
* Digest = `sha256:` of canonical JSON without `digest` field.
* Consent fail-closed for research capture.

## Extension Points

Non-normative future guidance; no current scope or acceptance claim changes.

### Trajectory builders and legacy readers

Additional builders can derive bounded or multi-agent views while preserving canonical reference ordering, explicit missing_intervals and consent partitions. Never fill missing evidence with inferred records or copy mutable state as historical truth.

Keep trajectory/0.3 distinct from legacy trajectory/1.0 and version content when the selected references or interpretation changes. Validate canonical JSON digest exclusion of digest itself, interval boundaries, redaction, unresolved references and denied consent; a legacy reader must not silently reinterpret an old sample as the newer schema.
