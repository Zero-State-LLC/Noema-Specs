# Spec: Spark + Orin Nano NVIDIA Physical AI Integration Path

**Status:** SPECULATIVE: direction without implementation authority ([current-state](../current-state.v1.yaml) `spark_orin_nvidia_stack`). A local or offline research topology; it does not change the hosted Platform in [CONTEXT.md](../../CONTEXT.md) and is not part of the active Campaign ([Population and Study Readiness](../../docs/POPULATION-AND-STUDY-READINESS.md)).

**SPEC DEFECT (open, if promoted):** "Spark runs the Noema chamber as the sole writer of WorldState" conflicts with the Platform authority (Durable Objects own live serialization; Postgres owns the durable canonical record). Resolve before any promotion.

## Overview

Noema agents inhabit a world whose canonical state runs on one DGX Spark while agent inference and local reasoning run on one Orin Nano. The path integrates the NVIDIA Physical AI stack (optional Omniverse twin, Cosmos models) for generative observations and Inception evidence without violating single-writer invariants.

This specification is additive. Existing Noema contracts remain unchanged.

## Requirements

1. Spark runs the Noema chamber as the sole writer of WorldState via pure reducers.
2. Orin Nano runs a quantized Cosmos3-Edge reasoner (or equivalent VLM) for agent planning.
3. Agents on Orin Nano send commands over LAN to the Spark Noema endpoint.
4. Spark returns observation projections (ledger digest, optionally augmented by Omniverse or Cosmos).
5. Research layers (Frontier, Observatory, Lab) may consume projections but MUST NOT mutate WorldState.
6. All predictions from Cosmos or Omniverse are non-authoritative and labeled INFERRED.

## Normative Behavior

- WorldEngine on Spark is the only component that mutates WorldState.
- ObservationEngine reads the ledger and may attach optional projection sources.
- Agent processes on Orin Nano depend only on observation responses; they hold no write authority.
- Hardware topology is configuration, not world state.

## State Model Additions

- NodeRole: enum [spark-world, orin-agent]
- ObservationSource: enum [ledger, cosmos_nano, omniverse, hybrid]
- NodeStatus: health, memory_utilization, model_loaded

## Schema Additions

- Observation.projection_source: ObservationSource (optional)
- Agent.endpoint: URI (command target on Spark)
- Optional agent_node_id on commands for provenance

## Positive Example

Orin Nano agent loads Cosmos3-Edge INT4, issues LOOK or MOVE to Spark chamber, receives Observation with projection_source=ledger (or hybrid if twin active), continues local planning.

## Negative Example

Orin Nano attempts direct WorldState mutation: rejected. Cosmos prediction written as authoritative event: rejected. Cycle where observation engine depends on agent inference that depends on observation: forbidden.

## Acceptance Criteria

- Single-writer invariant holds under concurrent Orin Nano agents.
- Command/observation round-trip latency is measurable and logged.
- Quantized Edge reasoner on Orin Nano produces valid action candidates within 8 GB.
- Spark memory headroom remains sufficient for Noema plus optional Nano or Omniverse.
- Labels distinguish OBSERVED (ledger) from INFERRED (Cosmos/Omniverse).

## Failure Behavior

- Orin Nano unreachable: agents queue or degrade to local-only; Spark continues.
- Cosmos inference timeout: fall back to ledger-only observation.
- Memory pressure on either node: surface as NodeStatus, do not crash ledger.

## Observability

- Spark: Noema metrics + optional Cosmos/Omniverse utilization.
- Orin Nano: tok/s, power, model load.
- Cross-node: round-trip latency, labeled claim counts (OBSERVED vs INFERRED).

## Security

- LAN-only for this path; no public exposure of Spark chamber.
- Agents authenticate via existing Noema mechanisms.
- Tool calls from agents to Spark are mediated.

## Version / Migration

Additive only. Existing Noema v0.x contracts unchanged. New fields optional.

## Non-Goals

- Replacing Noema reducers.
- Full Cosmos Super on either node.
- Changes to the public hosted path.
- Consciousness metrics or new world mechanics.

## Labels

OBSERVED: hardware split and Noema invariants. INFERRED: specific Cosmos quantization performance on Orin Nano. Spec status: ready for implement once Spark is available.
