# Projection: Foundry Corridor

**Seed:** `room.foundry-corridor`  
**Entities:**  
- `entity.foundry-production` — production_node, condition 55, available 6/20, regen 1/cycle  
- `entity.foundry-ore-node` — resource node, available 8/24, regen 1/cycle  
**Attention:** full (illustrative)  
**Scenario beat:** LOOK after arriving from Transit Ring (north of this room is not a seed exit; entry via south←Transit Ring)

---

## Human PLAY (Feature B)

```text
Foundry Corridor

Production-focused corridor. Resource nodes and production infrastructure.

PRESSURE
Ore and production stock are finite here. Empty nodes will not feed a thrash loop.

HERE
foundry-production (infrastructure, condition: worn, stock 6/20)
foundry-ore-node (resource node, stock 8/24)

EXITS
south — Transit Ring
west — Generator Hall (costs 1 energy)

STATUS
energy 78 · attention 6 · compute 64 · storage 16 · influence 40

HAPPENED
You reach Foundry Corridor.

AVAILABLE HERE
inspect foundry-ore-node
harvest foundry-ore-node
inspect foundry-production
```

First-paint max 3: inspect/harvest on the fuller node · inspect production. REPAIR on production may appear when affordances allow (condition 55).

---

## Empty-node failure (illustrative HAPPENED)

```text
HAPPENED
You try to harvest foundry-ore-node.
FAIL — nothing left to take.
Nothing changes.
Try: inspect foundry-production · walk south · wait.
```

(Does not rewrite GC8 harvest magnitudes; craft only.)

---

## Notes

- Stock lines are **live** state and belong in HERE/PRESSURE, not in static DESCRIPTION (seed description stays production-focused prose only).
- Two resource-bearing targets create local asymmetry vs Civic Exchange (empty HERE).
- WEST exit shows seed energy traversal cost.
- S-MARK-10 path here: HARVEST success (rank weak vs REPAIR) or REPAIR on `foundry-production` when legal.
