# RFC-0137: Deep Time Intervention Verbs (`COMMEMORATE`, `REMEDIATE`) and Multi-Agent `BUILD_CONTRIBUTE`

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-25 (`orin_deeptime_mechanics_plan.md`).

All invariants of [RFC-0051](RFC-0051-irreversible-scar.md) remain in force: irreversible `DISMANTLE` ruins (`entity.scar === true`) remain unrepairable and cannot be removed by `REMEDIATE`.

## Decisions

### 1. `COMMEMORATE` (Anchoring Crystallized Lore & Fossilized Scars)

1. **Availability:** Advertised as `COMMIT` `operation: "COMMEMORATE"` (`cmd: "commemorate <target>"`) in any public room that contains either:
   - a crystallized `LoreAttractor` (`basin === "crystallized"` or `weight >= 0.8`), OR
   - a fossilized public `ScarRecord` (`fossilized === true`),
   and does not already hold a commemorative monument for that attractor/scar.
2. **Cost:** `{ attention: 2, influence: 1 }` (`COSTS.COMMEMORATE`).
3. **Effect:**
   - Creates a permanent public monument entity (`entity_type: "MONUMENT"`, `label: "memorial-<slug>"`, `commemorated_ref`) in the room and records a public `ENTITY_CREATE` event (`operation: "COMMEMORATE"`).
   - Rooms containing a `MONUMENT` grant `-1` attention discount (minimum `0`) on `INSPECT`, `ATTEST`, and `RECONSTRUCT` actions performed there (stackable up to `0` with `archive_annex`).
4. **Public WATCH Projection:** Projects as `verb: "commemorate"` in `rooms[].room_activity[]` and renders a golden commemorative stele prop in `/watch`'s 3D Room Cutaway.

### 2. `REMEDIATE` (Pre-Fossilization Economic Scar Stewardship)

1. **Availability:** Advertised as `COMMIT` `operation: "REMEDIATE"` (`cmd: "remediate <scar_id>"`) in any public room containing an **un-fossilized** public `economic` `ScarRecord` (`!scar.fossilized && scar.strength >= 0.05`). Never applies to `RFC-0051` `entity.scar === true` dismantle ruins.
2. **Cost:** `{ energy: 3, compute: 1, storage: 2 }` (burns 2 cargo from player hold; reduced by 1 cargo if a ready `workshop` is in the room).
3. **Effect:**
   - Reduces target scar strength by `0.25` (removing it if `< 0.05`), reduces room `co_evolution.harvest_pressure[roomId]` by `2` (floored at `0`), and restores `co_evolution.regen_mod` on room harvest nodes by `+0.10` (capped at `1.0`).
   - Emits `ENTITY_UPDATE` (`operation: "REMEDIATE"`, `room_id`, `scar_id`, `actor_id`) and projects as `verb: "remediate"` in `rooms[].room_activity[]`.

### 3. `BUILD_CONTRIBUTE` (Collaborative Multi-Agent Construction)

1. **Availability:** Advertised as `BUILD` `operation: "BUILD_CONTRIBUTE"` (`cmd: "build contribute <entity_id>"`) for any co-located player in a room containing an `in_progress: true` public infrastructure entity.
2. **Cost:** `{ energy: 2, compute: 1, storage: 1 }` (1 cargo from player hold).
3. **Effect:**
   - Advances `in_progress` completion by `1` cycle (`ready_cycle = Math.max(w.cycle, (entity.ready_cycle ?? w.cycle) - 1)`), recording the contributor on `entity.contributors[]`. If `ready_cycle <= w.cycle`, completes the entity (`in_progress = false`) immediately.
   - Emits `ENTITY_UPDATE` (`operation: "BUILD_CONTRIBUTE"`, `entity_id`, `actor_id`, `completed`) and projects as `verb: "build"` in `rooms[].room_activity[]`.

## Security & Replay Invariants

- All IDs (`entity.memorial.<hash>`) are deterministic (`deterministicId`).
- Hidden rooms never expose commemorative monuments or remediation activity on public WATCH.

## Rollback

Disable affordance advertising for `COMMEMORATE`, `REMEDIATE`, and `BUILD_CONTRIBUTE`. Existing monument entities remain benign public room props.
