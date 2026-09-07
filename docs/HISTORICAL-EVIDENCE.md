# Historical Evidence

## Sources

`EVENT_LEDGER` · `SNAPSHOT` · `ARTIFACT` · `WITNESS_RECORD` · `INSTITUTION_ARCHIVE` · `INFRASTRUCTURE_STATE` · `AGREEMENT` · `WORLD_REPORT`

## Quality

`PRIMARY` · `SECONDARY` · `FRAGMENTARY` · `CORRUPTED` · `INACCESSIBLE`

Quality classifies evidence; it does not invent truth.

## Accessibility

- `accessible_to_agents`: whether ordinary PLAY observation may use it
- `hidden_from_ordinary_observation`: true for pure ledger internals not discoverable as in-world evidence

Archaeology uses accessible evidence only. Hidden ledger history MUST NOT leak into ordinary agent knowledge snapshots.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Evidence-source seam:** Extend examples of the listed source and quality classes with accessible and inaccessible variants. A fragmentary archive, corrupted witness record, and primary ledger event can describe the same subject without agreeing or becoming interchangeable truth.
- **Compatibility boundary:** New source/quality values or accessibility semantics require the corresponding versioned historical-evidence contract. Preserve immutable provenance and append corrections or superseding references instead of upgrading the original record's credibility in place.
- **Validation expectations:** Trace every reconstructed assertion to its evidence, test agent-accessible evidence separately from hidden ledger internals, and verify that inaccessible material contributes neither ordinary knowledge nor existence hints. Quality and availability should remain distinguishable; missing evidence is not evidence of absence.
