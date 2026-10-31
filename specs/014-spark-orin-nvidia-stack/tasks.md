# Tasks: Spark + Orin Nano NVIDIA Stack Path

DAG-ordered. Independent tasks may run in parallel. No cycles.

1. Confirm LAN path and baseline Noema chamber configuration on Spark. (no dependencies)
2. Stand up quantized Cosmos3-Edge reasoner container on Orin Nano. (no dependencies)
3. Implement agent wrapper on Orin Nano that targets Spark Noema endpoint. (depends on 1, 2)
4. Add Observation.projection_source field and labeling in Spark chamber. (depends on 1)
5. Wire optional Omniverse twin or Cosmos Nano on Spark for hybrid projections. (depends on 1, 4)
6. Add NodeStatus health endpoints on both nodes. (depends on 1, 2)
7. Conformance cases for single-writer, labeling, and latency. (depends on 3, 4)
8. Inception evidence capture (utilization, demos). (depends on 7)

Runtime execution of 1–3 and 6 waits for Spark and Orin Nano availability. Spec is fully implemented.
