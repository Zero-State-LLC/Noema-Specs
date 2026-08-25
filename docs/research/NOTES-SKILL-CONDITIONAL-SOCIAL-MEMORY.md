# Notes — Skill-Conditional Social Memory

**Status:** non-normative research-to-spec sketch
**Scope:** possible future GC3 continuation only if Living Civilization Alpha Gate C shows that existing dyadic memory does not affect later decisions
**Does not change:** RFC-0007, RFC-0022, RFC-0034–RFC-0039, current social-memory schemas, PLAY, WATCH, or runtime behavior

The relay delivery matrix is already closed by Accepted RFC-0009 and RFC-0021. This note therefore does not create a duplicate communication RFC. It records a different, explicitly conditional research direction for a future GC3 RFC.

## Research input

[Skill-conditional trust](https://arxiv.org/abs/2606.14200) models reliability relative to a skill or context rather than as one universal score. [AgentReputation](https://arxiv.org/abs/2605.00073) emphasizes context match, verification regime, and recency. These are design inputs only. They are not evidence that a NOEMA Player is trustworthy, capable, conscious, or aligned.

## Existing authority

[Social Memory](../SOCIAL-MEMORY.md) already requires evidence-backed directed edges, contradictory evidence, coarse certainty, observation boundaries, and no scalar reputation. [Mastery and Specialization](../MASTERY-SPECIALIZATION.md) already defines ledger-derived practice tracks without XP or classes.

A possible future composition is:

```text
subject Player
  → evidence-backed descriptor
  → object Player
  → bounded practice context
```

Examples in prose might distinguish “reliable in relay repair” from “reliable in trade settlement.” They must not collapse into a universal `trust = 72` value.

## Trigger

Do not open an RFC merely because the research is interesting. A future RFC is warranted only if a Gate C evidence pack shows all of the following:

1. existing GC3 edges are present and correctly rebuilt;
2. social memory nevertheless fails to change a later decision;
3. the failure is caused by evidence from materially different practices being conflated;
4. a bounded practice context would change a consequential choice without adding a verb or leaking hidden information.

Otherwise, defer.

## Candidate Draft RFC questions

A future Draft RFC would need to pin:

- the closed context vocabulary or deterministic mapping from existing practice families;
- which public, party-visible, or institution-authorized evidence families contribute;
- whether context is part of a canonical edge key or a rebuildable projection;
- certainty and contradiction behavior within one context;
- whether and how evidence may transfer between nearby contexts;
- decay, rehabilitation, replay, idempotency, migration, and visibility;
- PLAY wording that remains world-native and non-scalar;
- conformance fixtures for context match, mismatch, contradiction, sparse evidence, and hidden-evidence rejection.

## Invariants

- No global or cross-context scalar reputation.
- No auto-accept, auto-refuse, hidden price, or universal trust leaderboard.
- No proficiency or research capability score becomes a social-memory input by assertion.
- Private messages remain private evidence for their recipient and do not become WATCH.
- WATCH remains limited to already-public breach or cooperation evidence authorized by accepted projection rules.
- A descriptor does not grant a verb, bypass authorization, reveal a hidden specialization, or establish motive.
- Humans remain HumanPrincipals, not Players or social-memory subjects in the world model.

## Possible acceptance fixtures

Names only, for a future RFC:

```text
repair-reliable-trade-unknown.json
trade-reliable-repair-contested.json
context-mismatch-no-transfer.json
public-breach-context-specific.json
private-message-watch-silent.json
sparse-evidence-unknown.json
contradictory-evidence-contested.json
rebuild-and-restart-equivalent.json
```

## Deferred questions

Cross-context borrowing, institutional cards, anti-sybil analysis, and Observatory calibration belong to later RFC or STUDY work. None is part of Gate C, and none becomes hidden world truth.
