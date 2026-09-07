# Hosted multiplayer contention — first-accepted harvest

**Status:** Executable specification. Specs-only until hosted tests land.  
**RFC:** [RFC-0113](../rfcs/RFC-0113-hosted-multiplayer-contention.md)  
**Does not open:** new verbs · live chat · cycle-freeze scheduler · stock split · Genesis change

Hosted Perihelion serializes `POST /v1/command` on one World Durable Object. The first legal `HARVEST` or `REPAIR` that settles wins remaining stock or the repair. The next command reads the new world.

## Doctrine

| Temptation | Verdict |
|------------|---------|
| First-accepted on the Durable Object | **ACCEPT.** |
| Frozen-cycle sort as hosted | **REJECT.** Later RFC |
| Split the pile | **REJECT.** |
| Live chat / websocket | **REJECT.** Fights the relay |
| New CHAT verb | **REJECT.** `MESSAGE` is mail |

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `hosted-mp-s0` |
| Resolution | first-accepted |
| Miss | `FORBIDDEN` · Not enough stock available. |
| Budget on miss | unchanged |
| Coordination | existing `MESSAGE` (same-room same-cycle; cross-room relay bands) and shout |
| WATCH | existing harvest line; no amounts |

Stock is finite `stock_amount`. Grade is SOUND/WORN from condition. Regen is the existing production tick.

## Extension Points

Non-normative future guidance; no new behavior is authorized here.

Serialized contention fixtures are the extension seam for hosted-mp-s0, not a frozen-cycle scheduler implementation. Preserve first-accepted settlement on one World Durable Object, finite stock and unchanged budgets on a miss. Different ordering or stock splitting needs separate accepted authority and compatibility tests. Validate two legal contenders against the same remaining stock, the second reading committed state, repair contention and WATCH omitting amounts; specs-only status needs retained hosted test evidence before promotion.
