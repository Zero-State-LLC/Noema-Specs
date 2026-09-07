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

## Extension Points (additive, i18n AX R3 Gate B handoff + CONTRADICTION / EVIDENCE)

- **i18n centralization (STRINGS + t())** for "contradiction set", "contradiction_set_id", "member_refs", "source_identities", "known_truth_relationship", "agent_visible_relationship", "research_visible_relationship", "resolution_status" (open | resolved | abandoned), "two witnesses disagree", "stale sensor", "rumor vs public record", "deceptive message", "GC6-S0 PLAY pin", "archive vs live INSPECT", "Archive-record source", "RFC-0015". R3 agent contradiction handling + human S0.
- **Gate B S0-S3 + R3**: Agent-only Player (RFC-0120) for evidence signals; version comps; human S0.
- **AX**: Semantic for contradiction sets/lists; ARIA roles for tables/status, keyboard for inspect/archive, live regions for resolution updates, contrast. CDP.
- **Plugin atoms**: For contradiction packs (derive set, validate resolution, load_pack, atomic_replace); Chamber atoms for contradiction viewers, evidence tools.
- **LCA2/MUD handoff**: MUD native `INSPECT` / parser i18n for contradiction terms; cross GC6-FIRST-SLICE, PLAYER-ACTION-MAP, AGENT-*, graft.
- **Cross-refs**: GC6-FIRST-SLICE.md, RFC-0015, GAME-COMPLETENESS, PLAYER-ACTION-MAP, AGENT-ORIENTATION/PLAY/DETERMINISM, AUTH-AND-IDENTITY, PLATFORM, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, noema-specs-mud-craft, 8765/ui i18n, graft, prior EPs (CAPTURE/DIPLOMACY/ECONOMIC/DEEP-TIME/EMERGENT/COMPILATION + full list).
- All real outputs. Additive. Ready for Chamber i18n in study/evidence surfaces.
