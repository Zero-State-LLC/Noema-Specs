# v0.6 Deep Time: Examples

Package: [`examples/v06-deep-time/`](../../../examples/v06-deep-time/)

Multi-era Nacre Relay Stewardship scenario (Eras 1–6): institution, succession, decay, archaeology, contested claims, revival with reinterpretation.

**Genesis:** `genesis-result-a.json` (FRACTURED_OLD_WORLD + OLD_TRADE_NETWORK + LOST_ARCHIVE, activated) and `genesis-result-b.json` (same profile/seeds, different seed → different valid Cycle 0). Player entry vs admin preview.

Experience mirrors under `examples/experience/deep-time-*.json`.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Example maintenance can add source-linked detail to the Nacre Relay Stewardship eras, especially succession, missing archives, contested claims, and revival with reinterpretation. Keep the scenario illustrative and distinguish institutional belief from canonical history.

- Retain the original profile/story-seed and schema pins for genesis-result-a and genesis-result-b. New fixture revisions preserve reproducible old outputs and do not activate deferred Deep Time mechanics, rewrite earlier eras, or authorize preview to create/reseed a production world.

- Validate same-input/seed determinism and different-seed validity against the Genesis profile bounds. Check era-to-era lineage, unresolved contradictions, admin preview versus Player entry, and experience mirrors that preserve the underlying claim status rather than inventing a definitive historical narrative.
