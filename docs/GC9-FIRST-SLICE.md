# GC9 First Slice — Maintenance Custom from Repeated Repair

**Status:** Shipped as derived PLAY projection (RFC-0013 Accepted; reference runtime PR #71).  
**Parent:** [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md) · [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)  
**RFC:** [RFC-0013](../rfcs/RFC-0013-maintenance-custom.md)  
**Does not open:** procedural lore generator · v0.6C · `CULTURE_*` events · ritual verbs · titles-as-authority · ledger rewrite

S0 is the smallest culture increment that still satisfies scenario I’s *shape* (repeated practice becomes an inherited custom; founding events stay canonical). It reuses `COMMIT.REPAIR` → `ENTITY_UPDATE` and the existing `semantic-lineage/0.6` *kind* `CUSTOM`. It does not write a second canon.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Procedural lore generator | **REJECT.** Spec freeze out-of-scope |
| Silently start v0.6C | **REJECT.** Distinct later package |
| `RITUAL` / `COMMEMORATE` verb | **REJECT.** A ritual that changes state is `REPAIR` (or another existing verb) or it is presentation |
| `CULTURE_CREATED` event | **REJECT.** Derived projection |
| Custom rewrites condition / history | **REJECT.** Evidence wins ([LORE-BOUNDARY.md](LORE-BOUNDARY.md)) |
| Title grants office power | **REJECT.** Already GC4-S0 |
| Auto-interpret meaning shift | **REJECT.** `semantic-lineage` `auto_interpreted: false` |
| Tradition / institution in S0 | **DEFER.** S0 stops at `CUSTOM` |

Pressures: **dependency** (someone actually repaired) and **uncertainty** (a story about the site is not physics).

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc9-s0` |
| Catalog | `culture-catalog/gc9-s0` |
| Practice | Existing `COMMIT.REPAIR` |
| Evidence | Distinct `ENTITY_UPDATE` events on one infrastructure `entity_id` |
| State | Derived. Not WorldState. Not a reducer input |
| Lineage kind | `CUSTOM` (existing `semantic-lineage/0.6` enum). S0 does not persist a lineage engine |

### Thresholds

Reuse the GC3 “three distinct evidences” number. Parent left exact N as SPEC GAP; S0 pins it.

| Distinct repair `event_id`s on that entity | State | PLAY line (if the Player has access) |
|--------------------------------------------|-------|--------------------------------------|
| 0 | `UNKNOWN` | omit |
| 1–2 | `PRACTICING` | omit |
| ≥ 3 | `CUSTOM` | `This site has a maintenance custom.` |

The line does not say the ledger is wrong, name HP, or grant authority. `{name}` of a culture title is presentation only.

### Rebuild rules

1. Walk events in `(cycle, sequence)` order.
2. Count distinct `event_id` where `event_type=ENTITY_UPDATE` and `payload.entity_id` is the subject entity, and the payload is a condition update (`set.condition`, `field=condition`, or `operation=REPAIR`).
3. Replay of the same `event_id` does not double-count.
4. `LOOK`, `INSPECT`, `MESSAGE`, `TRADE_*` do not count as the practice.
5. Access: the subject Player is an `actor_id` on any event that names that `entity_id` (they repaired it or inspected/looked at it). Later Players inherit by ordinary `INSPECT` of the same entity.
6. Optional `lore_claim` in a fixture never replaces the count and never mutates events.
7. Projection writes no events.

### Visibility

| Audience | S0 |
|----------|----|
| Player with access | Custom line only at threshold |
| Player without access | Nothing from this slice |
| WATCH | Nothing from this slice |
| Lore / Chronicle text | Presentation. If it conflicts, evidence wins |

### Coupling

Coupled to **ASSET** (the repaired entity) and **INFORMATION** (who observed). It does not change `REPAIR` costs (GC1-S2 stays closed). It does not create an office.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + asset. No lore primitive |
| B | Dependency + uncertainty |
| C | No extra commands |
| D | Couples to repair, Deep Time names, later institutions |
| E | Verb-stable |
| F | A maintenance habit can be named without a holiday engine |
| G | Evidence refs are existing `ENTITY_UPDATE` ids |
| H | Human and agent Players use the same rebuild |
| I | Meaningful with research hidden |
| J | Without this, later Players only see a number on a relay |

---

## Out of S0

```text
TRADITION INSTITUTION cultural identity
procedural lore generator
v0.6C semantic evolution engine
CULTURE_* / RITUAL verbs and events
holidays / symbols / founding-story compiler
WATCH culture titles
ledger rewrite
```

---

## Runtime rule

Hosted Chamber PLAY projects the custom line on the current room for accessors. Cache is rebuildable and is not WorldState. WATCH is empty. No Chronicle pack. Existing worlds accrue from new repairs (no historic ledger replay).

## Acceptance (narrower than scenario I)

1. Three distinct repairs on one relay, then a later Player `INSPECT`s it and sees the custom line.
2. Two repairs produce no custom line.
3. A Player who never touched the entity sees nothing.
4. A lore sentence “this relay was never repaired” does not remove the events or the custom.
5. WATCH is empty. No events are written.

Full scenario I (named tradition, institutional adoption, founding story as derived lore) is **GC9-S1**.
