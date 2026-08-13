# Contradictory Evidence (v0.2)

Present mutually inconsistent **signals** without corrupting world truth.

## Examples

* two witnesses disagree;
* stale sensor vs current infrastructure state;
* rumor vs public record;
* deceptive message vs LOOK/INSPECT observation.

## Contradiction set

```text
contradiction_set_id
member_refs[]          # observation_ids and/or message_ids
source_identities[]
known_truth_relationship   # research-only: which members match world truth, if known
agent_visible_relationship # what agents are told (usually "unresolved")
research_visible_relationship
resolution_status      # open | resolved | abandoned
```

## Critical rule

The engine MUST NOT automatically tell the agent which signal is correct unless world rules make that knowable through ordinary observation.

`known_truth_relationship` is research partition only.

GC6-S0 PLAY pin for archive vs live `INSPECT`: [GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md).

Schema: [`specs/contradiction-set.schema.json`](../specs/contradiction-set.schema.json).
