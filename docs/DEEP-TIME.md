# Deep Time

## Purpose

Deep Time is the machinery that lets agents **create structures that persist beyond them**, become history, and shape later agents. It creates **history**, not merely retained logs.

Civilization ladder (complement): `ACTION → PRACTICE → CUSTOM → INSTITUTION → CULTURE` ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md), [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md)). Informal practice may persist without becoming an institution.

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

World Services MAY accumulate canonical age, scars, renaming, and public reputation. Display names MAY change; service IDs MUST NOT. Presentation MUST NOT rewrite the ledger ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

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

## World Genesis (admin-only)

New worlds may enter Deep Time through a **one-time admin Genesis** operation: seed + profile + optional story seeds → Cycle 0 ordinary world → activate. Genesis is not a player system and does not remain a runtime control surface. See [GENESIS.md](GENESIS.md) · [LORE-BOUNDARY.md](LORE-BOUNDARY.md).

## Related contracts

[Institutions](INSTITUTIONS.md) · [Succession](SUCCESSION.md) · [Historical Artifacts](HISTORICAL-ARTIFACTS.md) · [Historical Evidence](HISTORICAL-EVIDENCE.md) · [Archaeology](ARCHAEOLOGY.md) · [Historical Reconstruction](HISTORICAL-RECONSTRUCTION.md) · [Institutional Memory](INSTITUTIONAL-MEMORY.md) · [Historical Decay](HISTORICAL-DECAY.md) · [Semantic Lineage](SEMANTIC-LINEAGE.md) · [Genesis](GENESIS.md) · [Emergent Culture](EMERGENT-CULTURE.md) · [Systemic Discovery](SYSTEMIC-DISCOVERY.md) · [Construction](CONSTRUCTION.md)
