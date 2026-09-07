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

GC6-S0 PLAY pin for archive vs live `INSPECT`: [GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md). Archive-record source: [RFC-0015](../rfcs/RFC-0015-archive-record-source.md).

Schema: [`specs/contradiction-set.schema.json`](../specs/contradiction-set.schema.json).

## Extension Points

Non-normative extension guidance; accepted authority controls.

- **Evidence seam:** Extend contradiction fixtures linking observations/messages, source identities, and open/resolved/abandoned status. Retain competing signals and their provenance rather than replacing the losing signal with a corrected record.
- **Invariants:** `known_truth_relationship` remains research-only; the Agent Player receives only the relationship knowable through ordinary observation, usually unresolved. A popular rumor or deceptive message cannot rewrite world truth.
- **Compatibility:** Reuse contradiction-set schema and GC6 archive/live INSPECT contracts. Resolution viewers or pack loaders are research tooling, not new verbs, hidden oracle endpoints, or authority to atomically replace canonical history.
- **Verification:** Pair stale sensor/current state and archive/live disagreement fixtures; inspect agent and research projections separately, including unauthorized research access. Resolve one set without changing its source records and confirm agents are not automatically told the correct member.
- **Presentation:** Localize uncertainty/status explanations, preserve IDs, and offer accessible evidence links. A proposed CDP check or fixture pack is not an observed runtime receipt.
