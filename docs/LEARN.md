# LEARN

LEARN is the researcher surface for organizing **reproduced behaviors** and their evidence-backed relationships.

It completes the ordinary product loop after CAPTURE:

```text
PLAY → NOTICE → TEST → CAPTURE → LEARN
```

## Ordinary questions

```text
What behaviors have we reproduced?
Which agents/versions reproduce this?
What conditions does it depend on?
Where does it generalize?
Where does it fail?
What changed between versions?
What remains untested?
```

Researchers MUST NOT need graph theory. Default language is plain English.

## Simple behavior view (canonical)

```text
LEARN

Shared-ledger coordination

Reproduced by
• Agent 2.1
• Agent 2.2

Depends on
• messaging
• shared ledger

Works in
• high-scarcity scenario
• moderate-scarcity scenario
• alternate region

Fails when
• messaging is removed

Not yet tested
• different social topology

Evidence
7 captured tests

[ VIEW EVIDENCE ]
[ COMPARE VERSIONS ]
```

Every line MUST derive from machine edges/nodes and their `evidence_refs`. Simple views cannot strengthen claim labels.

## Progressive disclosure

| Level | Example |
|---|---|
| 1 Simple | Depends on messaging. |
| 2 Researcher | Messaging ablation caused the behavior to disappear in 5/5 runs. |
| 3 Advanced | `edge_type=FAILS_WITHOUT`, condition_ref, source lab result |
| 4 Reproducibility | captured test IDs, digests, versions, audit refs |

Same relationship. Different depth.

## Index

```text
LEARN — Reproduced behaviors
• Shared-ledger coordination
• …
```

Simple sort: recent · most evidence · agent/version. No required taxonomy categories.

## Agent/version view

Distinguish carefully:

```text
reproduced
not reproduced
not tested
```

Never present untested as failed.

## Dependency / generalization

Phrase within **tested boundary**. Compiler removals do not imply universal independence. Untested contexts are not failures.

## Boundaries

- Researcher-only default surface
- No PLAY coupling
- Optional WATCH discovery card is not required for v0.7
- Authority: [CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md)
