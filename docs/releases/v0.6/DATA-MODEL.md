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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Record seam:** Extend examples connecting institutions, succession, artifacts, claims, reconstructions, names, scars, and evidence through their existing v0.6 schema identities. Keep continuity classifications explicit when a name changes or a successor differs from the original entity.
- **Compatibility boundary:** Added record fields or continuity classes need versioned schema/catalog authority and migration handling. Genesis remains the minimal admin Cycle 0 identity layered over ordinary state/snapshot contracts; no new profile, story seed, or parallel world model is authorized here.
- **Validation expectations:** Validate the listed record types and their cross-references, replay lineage/succession ordering, and test disputed identity plus inaccessible historical evidence. Check that renaming preserves stable IDs, reconstructions do not overwrite sources, and Genesis identifiers/inputs remain outside ordinary Player observations.
