# v0.6 Deep Time: Data Model Delta

| Record | Schema | schema_version |
|---|---|---|
| Institution | `specs/institution.schema.json` | `institution/0.6` |
| InstitutionLineage | `specs/institution-lineage.schema.json` | `institution-lineage/0.6` |
| SuccessionRecord | `specs/succession-record.schema.json` | `succession-record/0.6` |
| HistoricalArtifact | `specs/historical-artifact.schema.json` | `historical-artifact/0.6` |
| HistoricalClaim | `specs/historical-claim.schema.json` | `historical-claim/0.6` |
| HistoricalReconstruction | `specs/historical-reconstruction.schema.json` | `historical-reconstruction/0.6` |
| SemanticLineage | `specs/semantic-lineage.schema.json` | `semantic-lineage/0.6` |
| HistoricalName | `specs/historical-name.schema.json` | `historical-name/0.6` |
| WorldScar | `specs/world-scar.schema.json` | `world-scar/0.6` |
| HistoricalEvidence | `specs/historical-evidence.schema.json` | `historical-evidence/0.6` |

Catalogs: `historical-significance.v06.json`, `historical-decay.v06.json`.

Identity continuity classes: `SAME_ENTITY_EVOLVED` · `SUCCESSOR_ENTITY` · `NEW_ENTITY` · `DISPUTED_IDENTITY`.

## Genesis (minimal)

| Record | Schema | Notes |
|---|---|---|
| GenesisProfile | `specs/genesis-profile.schema.json` | 3 profiles in `genesis-profiles.v06.json` |
| StorySeed | `specs/story-seed.schema.json` | closed set in `story-seeds.v06.json` |
| GenesisResult | `specs/genesis-result.schema.json` | admin Cycle 0 identity + refs |

Cycle 0 live state reuses ordinary world seed/state/snapshot contracts — not a parallel world model.
