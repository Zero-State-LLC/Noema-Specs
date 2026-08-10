# Situation Genome

A **portable, versioned description of world conditions and pressures**, not a scripted solution or expected agent behavior.

Machine authority: [`specs/situation-genome.v02.schema.json`](../specs/situation-genome.v02.schema.json) (`situation-genome/0.2`).
Legacy samples may use `situation-genome/1.0` ([situation-genome.schema.json](../specs/situation-genome.schema.json)).

## MUST NOT encode

* required agent action;
* desired research result;
* hidden “correct answer”;
* capability label as world truth;
* forced outcome.

Capability targets in the genome are **research planning metadata**, never player-visible objectives.

## Required fields (`situation-genome/0.2`)

| Field | Type | Notes |
|-------|------|--------|
| `schema_version` | const `situation-genome/0.2` | |
| `genome_id` | string ID | stable |
| `genome_version` | string | content version |
| `parent_genome_id` | string\|null | mutation lineage |
| `world_rules_version` | string | e.g. `world/v1` |
| `template_id` | string | source template |
| `mutation_lineage` | array | ordered operator applications |
| `affected_rooms` | string[] | room_ids |
| `affected_entities` | string[] | entity_ids |
| `participants` | object | eligibility / agent_ids optional |
| `resource_conditions` | object | fixed-point pressures / node targets |
| `information_distribution` | object | who may know what (policy ids) |
| `social_topology` | string + optional graph digest | |
| `temporal_structure` | object | duration, deadlines (cycles) |
| `goal_structure` | object | world incentives, not agent mandates |
| `constraints` | string[] | containment / safety |
| `noise_model` | object | ref noise-model/0.2 |
| `contradictory_evidence` | object | contradiction_set refs |
| `tool_availability` | string[] | verbs/tools permitted in situ |
| `risk_class` | integer 0–4 | higher = riskier |
| `control_role` | enum | `none` \| `positive-control` \| `negative-control` \| `regression` |
| `novelty_vector` | object | 9 axes millipoints 0–1000 |
| `seed_streams` | object | named streams |
| `visibility_policy` | object | player vs research |
| `duration_cycles` | integer ≥ 0 | 0 = until natural end |
| `termination` | object | conditions |
| `provenance` | object | author, created_cycle, digests |
| `content_digest` | `sha256:…` | of canonical genome sans digest field |

## Content digest

```text
content_digest = "sha256:" + hex(SHA-256(canonical_json(genome without content_digest)))
```

Canonical JSON: UTF-8, sorted keys, no insignificant whitespace.

## World entry

Genomes become world-affecting only via `SITUATION_INJECTED` (+ follow-on events). See [releases/v0.2/ARCHITECTURE.md](releases/v0.2/ARCHITECTURE.md).
