# Data Model

## Canonical entities

User, Agent, AgentVersion, AgentManifest, World, WorldVersion, Room, Entity, Organization, Institution, Artifact, WorldEvent, Observation, Action, Message, ToolCall, BeliefUpdate, Prediction, SelfReport, Trajectory, SituationGenome, Experiment, Replication, Perturbation, Ablation, Counterfactual, Capability, CapabilityEvent, CapabilityBoundary, Phenomenon, PhenomenonCase, ReproducibilityBundle, and DatasetRelease.

## IDs and lineage

IDs MUST be stable, namespaced where useful, and never reused for different records. Every research-relevant record SHOULD point to world version, agent version, protocol version, schema version, seed, parent experiment where applicable, timestamp/cycle, and provenance source.

## Append-only preference

Research-critical events SHOULD use append-only ledgers. Corrections are new events that supersede or invalidate prior records without deleting lineage.

## Public/private separation

Agent private metadata, research metadata, and public world-visible metadata are separate data classes. Dataset releases MUST preserve this partition.
