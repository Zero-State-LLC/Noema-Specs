# v0.2 Frontier — Data Model Delta

Storage-neutral research + genome entities. World entities remain v0.1 ([DATA-MODEL.md](../../DATA-MODEL.md)).

## New / expanded entities

| Entity | Domain | Schema |
|--------|--------|--------|
| SituationGenome | research/world-condition description | `situation-genome/0.2` |
| NoveltyVector | fixed-point axis scores | novelty-axes/0.2 |
| CapabilityPrimitive | research only | CAPABILITY-PRIMITIVES |
| FrontierRequest | research | frontier-request.schema.json |
| FrontierCandidate | research | frontier-candidate.schema.json |
| FrontierPlan | research | frontier-plan.schema.json |
| FrontierAuditRecord | research | frontier-audit-record.schema.json |
| FrontierReplayContext | research | frontier-replay-context.schema.json |
| MutationOperator | catalog | mutation-operator / mutation-catalog.v02.json |
| NoiseApplication | observation | noise-model/0.2 |
| ContradictionSet | observation/research | CONTRADICTORY-EVIDENCE |

## ID patterns (additions)

| ID | Pattern example |
|----|-----------------|
| `genome_id` | `genome.frontier.scarcity-conflict.1` |
| `candidate_id` | `fdc-` + hex(SHA-256(...)) |
| `request_id` | `fdrq.v02.001` |
| `plan_id` | `fdplan.v02.001` |
| `contradiction_set_id` | `cset.v02.001` |
| `noise_id` | existing event catalog form |

## Lineage

Frontier plans reference: `director_version`, `world_version`, input digests, genome digests, seed digests. World history is never rewritten; v0.2 appends prospectively ([MIGRATION.md](MIGRATION.md)).


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Data-model examples can clarify lineage joins among Frontier requests, candidates, plans, genomes, noise applications, and contradiction sets. Keep research/world-condition descriptions separate from the unchanged v0.1 World entities and preserve storage-neutral identifiers.

- Additional entities, digest ingredients, or identifier semantics require the owning schema/catalog version and migration review. Existing plans retain director/world versions and input/genome/seed digests; v0.2 appends prospectively rather than rewriting historical World records.

- Validate referential closure and version compatibility for a full request-to-plan example, including malformed candidate identifiers and mismatched genome digests. Confirm observation noise or research annotations do not change canonical entity identity and that the old v0.1 world fixture remains readable.
