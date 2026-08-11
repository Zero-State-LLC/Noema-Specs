# Deep Time

## Purpose

Deep Time is the machinery that lets agents **create structures that persist beyond them**, become history, and shape later agents. It creates **history**, not merely retained logs.

Canonical conceptual loop:

```text
ACT → BUILD → ORGANIZE → INSTITUTIONALIZE → PERSIST
  → DECAY / CHANGE → INHERIT → INTERPRET → ADAPT
```

Executable package: [releases/v0.6/](releases/v0.6/).

## Lore boundary (normative)

> Lore is a derived presentation of accumulated world history. Lore is not canonical world truth.

```text
WORLD EVENTS → HISTORY → ARTIFACTS → INTERPRETATIONS → CULTURAL MEMORY → LORE
```

If derived lore conflicts with canonical evidence, **canonical evidence wins**. v0.6 MUST NOT create a separate authored lore canon.

## Separated layers (MUST remain distinct)

| Layer | What it is | Authority |
|---|---|---|
| Current world state | Live reducer state | World engine |
| Historical world state | Prior states reconstructible from ledger/snapshots | Event ledger + snapshots |
| Historical evidence | Surviving in-world artifacts, archives, scars | Artifact/institution records |
| Agent belief about history | What an agent observed or inferred | Observations / reconstructions |
| Derived historical summary / lore | Presentation for PLAY/WATCH/STUDY | Non-authoritative projection |

```text
WORLD EVENT HISTORY
  ↓
HISTORICAL STATE
  ↓
EVIDENCE / ARTIFACTS
  ↓
AGENT INTERPRETATION
  ↓
DERIVED PRESENTATION
```

Interpretation MUST NOT rewrite history. The world can forget accessible evidence; the **canonical ledger cannot**.

## Usability

Ordinary PLAY:

```text
This institution is old.
This place has history.
This artifact came from somewhere.
This rule existed before me.
This organization survived its founders.
```

Advanced detail may expose lineage graphs, digests, succession machines, and reconstruction rules.

## Related contracts

[Institutions](INSTITUTIONS.md) · [Succession](SUCCESSION.md) · [Historical Artifacts](HISTORICAL-ARTIFACTS.md) · [Historical Evidence](HISTORICAL-EVIDENCE.md) · [Archaeology](ARCHAEOLOGY.md) · [Historical Reconstruction](HISTORICAL-RECONSTRUCTION.md) · [Institutional Memory](INSTITUTIONAL-MEMORY.md) · [Historical Decay](HISTORICAL-DECAY.md) · [Semantic Lineage](SEMANTIC-LINEAGE.md)
