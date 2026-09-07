# Historical Decay

## Scope

Bounded, versioned decay for: artifacts, records, institutions (activity/memory), infrastructure condition, institutional memory accessibility.

## Non-scope

**Do not decay canonical event history.** Only surviving in-world evidence decays.

## Forgetting

```text
world no longer contains accessible evidence
≠
event never happened
```

The world can forget. The ledger cannot.

Profiles: [`historical-decay.v06.json`](../specs/historical-decay.v06.json). Transitions are cycle-thresholded and deterministic.

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** Decay-profile documentation can add examples of evidence becoming inaccessible while the underlying event remains verifiable. Keep cycle-thresholded deterministic profiles distinct from erasing canonical history or retroactively changing what happened.
- **Compatibility and validation.** For a proposed profile revision, compare replay at each threshold and inspect surviving versus inaccessible evidence for every affected entity kind. Promote semantic changes through accepted authority and versioned historical-decay profiles with migration expectations; never implement a new profile by deleting ledger rows.
