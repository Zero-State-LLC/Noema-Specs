# Behavioral Signature

Machine representation of captured behavior. Prose equality alone is not a behavior test.

## Components

- feature IDs
- event motifs
- action relationships
- resource relationships
- communication patterns
- artifact usage
- temporal constraints
- coordination structure

Recorded on [`captured-test`](../specs/captured-test.schema.json) and used by the [over-minimization guard](OVER-MINIMIZATION.md).

## Extension Points

Non-normative extension guidance; accepted authority controls.

- **Signature seam:** Extend captured-test fixtures with linked feature IDs, event motifs, action/resource relationships, communication, artifact, temporal, and coordination components relevant to the captured behavior.
- **Invariants:** Prose equality is not behavioral equivalence. A reduced test remains subject to the over-minimization guard; removing a causal or temporal relationship cannot be masked by retaining the same narrative description.
- **Compatibility:** Reconcile signature changes with the captured-test schema and its pinned feature definitions. Preserve prior evidence and distinguish a revised signature from an equivalent serialization; no world action or public exposure follows from a signature update.
- **Verification:** Pair two identically worded tests with different event/coordination structure and a minimization that deletes a required motif. Confirm the accepted guard catches lost behavior; replay an unchanged signature as the positive case.
- **Research view:** A permissioned signature diff can present retained/removed components and evidence links in accessible text. Controller identity alone grants no captured-test access, and WATCH receives no signature merely because it describes public events.
