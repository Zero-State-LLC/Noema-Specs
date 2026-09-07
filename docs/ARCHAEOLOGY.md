# Archaeology

## Definition

> Reconstructing prior world state from incomplete surviving evidence.

It is **not** magical access to the full canonical event ledger.

## Discoverable surfaces

Ruins, old infrastructure, archival fragments, abandoned stores, historic maps, damaged records, old agreements, markers.

## Observation contract

Agents observe:

- estimated age bands (when exact cycle not evidenced)
- visible marks / conditions
- missing ownership records
- possible interpretations labeled `INFERRED` / `SPECULATIVE`

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend reconstruction views with explicit links between an accessible ruin, surviving mark or archive fragment, estimated age band, and the interpretation it supports. Missing ownership or uncertain chronology should remain visible gaps, not be filled from the complete ledger.

### Compatibility and promotion

Archaeology remains Agent Player knowledge, not an omniscient history browser. Preserve agent_knowledge_only and hidden_ledger_not_exposed on reconstruction outputs. Additional display treatments cannot widen artifact permissions or introduce a new discovery action; research access is separately authorized.

### Verification before adoption

Compare two Players with different surviving evidence and confirm their possible reconstructions differ appropriately. Test missing dates, damaged records, and conflicting accounts; retain INFERRED/SPECULATIVE distinctions. Check that exact cycles, owners, and hidden ledger events never appear merely because an operator can see them.

Exact hidden history is exposed only when evidence allows it.

## Output

Agent-facing reconstructions are [historical reconstructions](HISTORICAL-RECONSTRUCTION.md) with `agent_knowledge_only` and `hidden_ledger_not_exposed: true` when produced from archaeology.
