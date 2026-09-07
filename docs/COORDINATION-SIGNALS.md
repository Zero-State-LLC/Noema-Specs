# Coordination Signals (v0.3)

Deterministic multi-agent signals:

joint timing · resource transfers · complementary roles · shared infrastructure use · organization-level actions

## Representation

```text
coordination_signal_id
signal_type
participants[]
evidence_refs[]
possible_interpretations[]   # e.g. cooperation, trade, coercion, coincidence
confounds[]
claim_label: INFERRED
```

Do **not** auto-label as “cooperation” when adversarial/transactional explanations remain plausible.

## Extension Points (additive, i18n AX R3 Gate B handoff + COORDINATION-SIGNALS)

- **i18n centralization (STRINGS + t())** for "coordination signals", "coordination_signal_id", "signal_type", "participants[]", "evidence_refs[]", "possible_interpretations[]", "confounds[]", "claim_label: INFERRED", "joint timing", "resource transfers", "complementary roles", "shared infrastructure", "organization-level actions". R3 agent coordination + human S0.
- **Gate B S0-S3 + R3**: Agent-only Player (RFC-0120) for signals; version comps; human S0.
- **AX**: Semantic for signal reps; ARIA lists/tables, keyboard for coordination views, live for signals, contrast. CDP.
- **Plugin atoms**: For signal packs (derive/validate interpretations, load_pack, atomic_replace); Chamber atoms for coordination viewers.
- **LCA2/MUD handoff**: MUD native for signal i18n / multi-agent; cross PLAYER-ACTION-MAP, AGENT-*, graft.
- **Cross-refs**: GAME-COMPLETENESS, PLAYER-ACTION-MAP, AGENT-ORIENTATION/PLAY/DETERMINISM, AUTH-AND-IDENTITY, PLATFORM, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, noema-specs-mud-craft, 8765/ui i18n, graft, prior EPs (full list).
- All real outputs. Additive. Ready for Chamber i18n in study/coordination surfaces.
