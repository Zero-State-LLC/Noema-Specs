# Spectator Projection Contracts

WATCH product entry: [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md).

Machine-readable projections: [`specs/spectator-projection.schema.json`](../specs/spectator-projection.schema.json) · fixtures under [`examples/v01-strategic/`](../examples/v01-strategic/).

## Hard rules

1. Spectator output is a **derived projection** of canonical events + permission filters.
2. Spectator Projection module MUST NOT mutate WorldState or append ledger events.
3. Narrative/LLM summaries, if any, are research/UX overlays and MUST NOT become `WorldEvent` records.
4. Agent POV MUST match the selected agent’s observation boundary exactly.
5. Public observers MUST NOT see restricted fields.

## Realm view

Spectators MAY see [Realm](REALMS.md) summaries (strategic footprint of actors/orgs). Realms are **derived projections**, not canonical entities, and follow the same non-mutation rules.

## Projection catalog

| Projection id | Source event(s) | Public | Auth observer | Agent POV | Research overlay |
|---------------|-----------------|--------|---------------|-----------|------------------|
| `agent_move` | `MOVE`, `MOVE_REJECTED` | from/to room names if public rooms; hide condition details | + exit_id | full if self else co-located notice | same + consent |
| `resource_change` | `BUDGET_CONSUMED`, `RESOURCE_TRANSFER` | anonymized room-level scarcity flags only | agent display_name + resource type + direction | exact self amounts | consented amounts |
| `production` | `ENTITY_UPDATE` on resource_node | “production shifted” in room | node label + available band | if co-located: available integer | full if consented |
| `trade` | `TRADE_*`, `RESOURCE_TRANSFER` with trade_id | “trade occurred” without amounts | parties + status | full if party else status only | consented |
| `organization` | `ORG_CREATE`, `ORG_MEMBER_*` | org name + public roles | + member display names | + if member: roles | charter if public |
| `infrastructure` | `ENTITY_UPDATE` on INFRASTRUCTURE | condition band (ok/degraded/failed) | condition integer | co-located full | full |
| `shortage` | Director + node available=0 | room scarcity flag | resource type | co-located stock | full |
| `world_pressure` | `SITUATION_INJECTED` | public situation summary | genome id | room-targeted detail | full genome ref |
| `message_notice` | `MESSAGE` / `MESSAGE_DELIVERED` | none of text | that a message was sent (no text) | full if party | consented capture only |
| `discovery` | `ENTITY_CREATE` ARTIFACT/DOCUMENT | public label if public entity | + room | co-located inspect | full |

### Condition bands

```text
condition >= 75 → ok
25 <= condition < 75 → degraded
condition < 25 → failed
```

### Amount bands (public)

```text
0 → empty
1-5 → low
6-15 → moderate
>15 → high
```

## Schema shape

Each projection instance:

```json
{
  "schema_version": "spectator-projection/1.0",
  "projection_id": "agent_move",
  "world_id": "world-01",
  "cycle": 3,
  "source_event_ids": ["evt...."],
  "visibility": "public",
  "fields": {},
  "redactions": [],
  "narrative": null
}
```

`narrative` is optional human text and is **never** authoritative.

## Conformance

**C25** — Spectator Projection Integrity.


## Frontier projections (v0.2)

Frontier-generated situations MUST be watchable as natural world pressure.

| projection_id | Public / auth | Research overlay (authorized only) |
|---------------|---------------|--------------------------------------|
| `frontier_pressure` | shortage/crisis language from world events | genome_id, novelty_vector, targets, rationale, control_role |
| `conflicting_reports` | that reports conflict (no truth flag) | contradiction_set_id, known_truth (research) |
| `communication_disrupted` | message difficulty / relay degraded | policy refs |
| `market_shift` | trade activity bands | — |
| `organization_response` | public org actions | — |

Research overlay is **noncanonical** and MUST NOT appear on ordinary player/WATCH surfaces.

Player-facing copy MUST NOT say: "Test: demonstrate planning capability" or "Objective: prove epistemic restraint".


## Observatory projections (v0.3)

Ordinary spectators MAY see game-grounded events:

* agent changed strategy;
* organization split;
* unusual trade pattern;
* new protocol/ledger appeared;
* unexpected coordinated action.

They MUST NOT automatically see:

* `anomaly_score`;
* `capability_candidate`;
* detector confidence;
* research target;
* hidden comparison cohort.

Authorized research overlays may display these and are noncanonical.
