# Plan: Spark + Orin Nano NVIDIA Stack Path

## Technical Approach

- Spark: Deploy Noema offline chamber as the authoritative world. Optional Omniverse libraries + Isaac Sim for a structured twin. Optional Cosmos3-Nano via vLLM or NIM for generative observations.
- Orin Nano: TensorRT Edge-LLM or optimized container for Cosmos3-Edge reasoner (INT4). Agent wrapper process that issues commands to the Spark endpoint.
- Networking: Existing Orin-to-Spark LAN path. Baseline latency measurement required.
- DAG: WorldEngine → ActionRouter → Ledger. ObservationEngine reads Ledger (no write). AgentInference (Orin) depends only on ObservationEngine responses. No reverse edges. No cycles.

## Dependencies

- Existing Noema chamber and reducers (unchanged).
- LAN connectivity between Spark and Orin Nano.
- Quantized Cosmos3-Edge reasoner build compatible with Orin Nano 8 GB.

## Implementation Strategy

1. Baseline chamber and LAN on Spark (runtime later).
2. Agent wrapper and Edge reasoner on Orin Nano (runtime later).
3. Additive schema fields and labeling in chamber.
4. Optional twin wiring.
5. Conformance cases.
6. Inception evidence capture.

Runtime deployment waits for Spark availability. Spec artifacts are complete now.
