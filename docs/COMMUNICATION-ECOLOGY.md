# Communication Ecology (GC5)

**Status:** Product authority for civilization-scale communication. P1. Phase GC-B.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Preserves:** `MESSAGE` as the stable verb ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)).  
Hosted coordination uses this verb (mailbox) and existing shout/board surfaces. Do not add a live-chat protocol. [HOSTED-MP-CONTENTION.md](HOSTED-MP-CONTENTION.md).
**Does not replace:** [WORLD-REPORTS.md](WORLD-REPORTS.md) (derived news) · [OBSERVATION.md](OBSERVATION.md)

This package expands **surfaces, routing, and failure** around `MESSAGE`. It does not create `SHOUT`, `BOARD`, or `RUMOR` verbs unless an RFC proves a distinct transition that `MESSAGE` + target/scope cannot express.

**Doctrine:** communication is information + infrastructure, not a minigame ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)).

GC5-S0 machine pins: [GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md) · [RFC-0009](../rfcs/RFC-0009-relay-message-delivery.md).  
GC5-S1 delay pins: [GC5-S1-DELAY.md](GC5-S1-DELAY.md) · [RFC-0021](../rfcs/RFC-0021-relay-message-delay.md).  
GC5-S2 rumor pins: [GC5-S2-RUMOR.md](GC5-S2-RUMOR.md) · [RFC-0028](../rfcs/RFC-0028-rumor-provenance.md).  
GC5-S3 board pins: [GC5-S3-BOARD.md](GC5-S3-BOARD.md) · [RFC-0054](../rfcs/RFC-0054-message-board.md).  
GC5-S4 shout pins: [GC5-S4-SHOUT.md](GC5-S4-SHOUT.md) · [RFC-0062](../rfcs/RFC-0062-message-shout.md).  
GC5-S5 board retention pins: [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md) · [RFC-0063](../rfcs/RFC-0063-board-retention.md).  
GC5-S6 institution notice pins: [GC5-S6-NOTICE.md](GC5-S6-NOTICE.md) · [RFC-0064](../rfcs/RFC-0064-institution-notice.md).  
GC5-S7 org channel pins: [GC5-S7-CHANNEL.md](GC5-S7-CHANNEL.md) · [RFC-0065](../rfcs/RFC-0065-org-channel.md).  
GC5-S8 trade notice pins: [GC5-S8-TRADE-NOTICE.md](GC5-S8-TRADE-NOTICE.md) · [RFC-0066](../rfcs/RFC-0066-trade-notice.md).

---

## Thesis

Communication infrastructure MUST be able to produce, deterministically:

```text
information asymmetry
coordination advantage
regional isolation
delayed information
rumor propagation
communication failure
```

without nondeterministic hand-waving.

Relay condition, route existence, and addressability are world state. They are not flavor text.

---

## Surfaces

All surfaces are **projections or addressability classes** of `MESSAGE` (and existing reports/archives), unless marked later-RFC.

| Surface | Addressability | Default visibility |
|---------|----------------|--------------------|
| Direct message | One Player | Private to parties |
| Organization channel | Org members (current) | Members; history may persist for members |
| Public board | Room or designated board entity | Locally observable |
| Trade notice | Public or market-local | Public within scope |
| Institution notice | Issued by scoped office | Institution-defined audience |
| Local notice | Current room / adjacent if relay allows | Local |
| Contract / agreement text | Parties + authorized auditors | Parties |
| Rumor | No guaranteed recipient; provenance required | Uncertain; never presented as fact |
| Relay-dependent long-range | Requires path of relays above a condition band | As addressed, subject to delay/failure |
| Archive | Stored message/document retrieve via `INSPECT` / optional `QUERY` | Permissioned |

World Reports remain a **derived** cycle product, not a Player-composed board.

---

## Settled routing semantics

| Concern | Rule |
|---------|------|
| Addressability | Recipient or surface must be in-scope **at send time** under current observation/org/institution/relay state |
| Scope | `MESSAGE.parameters` carry surface/scope; unknown scope → fail closed |
| Locality | Local surfaces ignore distant relays. Long-range requires a relay path |
| Delivery | Same-cycle local delivery remains as current `MESSAGE_DELIVERED` before observation projection |
| Latency | Long-range or damaged-relay paths MAY deliver on a later cycle. Delay is a deterministic function of path condition, not RNG theater |
| Ordering | Per existing scheduler and message-delivery rules. Delayed messages keep send-cycle identity |
| Failure | No path, recipient unknown, scope forbidden, budget fail → typed failure. No silent drop without a failure event or sender-visible reason **that does not leak hidden topology** |
| Retry | Sender may resend; new idempotency key. Delayed-in-flight messages are not double-delivered |
| Retention | Versioned per surface. Archives outlive channels. Deletion of a Player-visible copy MUST NOT erase the ledger |
| Deletion | Soft-hide for the requester only, unless a later moderation scope exists |
| Privacy | Private DM text stays private. Public boards are public. Institution notices follow office scope |
| Public/private projection | WATCH sees public surfaces and delivery pulses permitted by spectator policy, never DM text |
| Organization authority | Channel post/moderation requires membership or office scope ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)) |
| Relay dependency | Relay condition bands map to: full / delayed / local-only / failed. Exact table is SPEC GAP |
| Historical archiving | Opt-in or institution policy copies to archive entities ([DEEP-TIME.md](DEEP-TIME.md)) |
| Searchability | `INSPECT` / optional `QUERY` on archives the Player may access. No omniscient search |
| Partial observability | Failure reasons use coarse codes (`UNREACHABLE`, `DELAYED`, `NOT_ADDRESSABLE`) that do not reveal hidden rooms or hidden members |
| False / uncertain information | Allowed in Player text. The engine does not certify truth |
| Rumor provenance | A rumor surface MUST carry `source_class` (player, report, archive fragment, unknown) and MUST present uncertainty |
| Moderation / system authority | No free-form Admin edit of Player speech. Control-plane removal is [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) only |

---

## Rumors

Rumors are **not** World Reports and **not** lore canon.

```text
Player or damaged archive / conflicting report
  → rumor record with provenance + uncertainty
  → others may INSPECT or hear via local/relay surfaces
  → beliefs diverge
  → investigation uses ordinary actions ([SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md))
```

The engine MUST NOT upgrade a rumor to fact because it is popular.

---

## Infrastructure coupling

| Relay / route state | Communication effect |
|---------------------|----------------------|
| High condition path | Same-cycle or low-delay long-range |
| Degraded | Added cycle delay |
| Broken / missing | Long-range fail; local still works |
| New `route_link` / restored relay ([CONSTRUCTION.md](CONSTRUCTION.md)) | Path recalculated next eligible cycle |

This is the substrate for acceptance scenario E. Ordinary `MESSAGE` semantics (schema, budgets, idempotency) do not change; **delivery outcome** changes with world state.

---

## SPEC GAP

```text
GC5-S0 closed: local = same room; long-range needs best live relay condition ≥ 25
GC5-S1 closed: long-range ≥ 50 same-cycle; 25–49 delay 1 cycle; < 25 UNREACHABLE
GC5-S2 closed: rumor is claim + MESSAGE lineage; no RUMOR verb / score
GC5-S3 closed: MESSAGE surface=BOARD; public room; last 3; WATCH silent
GC5-S4 closed: MESSAGE surface=SHOUT; public room; last 1; WATCH silent
GC5-S5 closed: MESSAGE board last 5; shout last 1 unchanged; WATCH silent
GC5-S6 closed: MESSAGE surface=NOTICE; occupied PUBLISH_NOTICE; public room last 1; WATCH silent
GC5-S7 closed: MESSAGE surface=CHANNEL; current members; last 1; unknown/outsider NOT_ADDRESSABLE; WATCH silent
GC5-S8 closed: MESSAGE surface=TRADE_NOTICE; public room last 1; WATCH silent; no auto-TRADE
cycle-based expiry closed: S9 shout · S10 board · S11 notice · S12 channel · S13 trade notice (1 committed cycle)
```

Prefer extending `MESSAGE` parameters over a new verb.

---

## Acceptance (scenario E)

A relay’s condition falls below the versioned band. Long-range messages to another region are delayed or fail with a non-leaking reason. Local `MESSAGE` still works. Repair or reconstruction restores the prior delivery class. Replay matches.
