# GC5-S4 — MESSAGE shout surface

**Status:** Executable specification. Runtime authorized with RFC-0062.  
**Parent:** [GC5-S3-BOARD.md](GC5-S3-BOARD.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0062](../rfcs/RFC-0062-message-shout.md)  
**Does not open:** SHOUT/BOARD verbs · long-range shout · help advertising · hidden shouts  
**Next:** [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md)

S4 adds one MESSAGE surface. A shout is heard in the public room. It is not a shout verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| SHOUT / BOARD verb | **REJECT.** |
| Long-range / adjacent shout | **REJECT.** |
| Hidden-room shout | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help shout | **REJECT.** |
| Change board last-3 | **DEFER** to [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md). |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s4` |
| Catalog | `communication-catalog/gc5-s4` |
| Verb | existing `MESSAGE` |
| Surface | `SHOUT` only |
| Place | current public room |
| Cost | compute 1 |
| Keep | last 1 shout |
| Events | `MESSAGE` only |
| PLAY | `A shout: {text}.` |
| WATCH | silent |
| Help | still omits board / SHOUT |

---

## Out of S4

```text
SHOUT verb
long-range shout
WATCH ticker
Chamber help shout
```

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend MESSAGE rendering with the current public room’s last shout and provenance-safe text escaping. Retain the difference between a local audible message surface and ordinary direct/long-range delivery so a shout is not mistaken for a global broadcast.

### Compatibility and promotion

RFC-0062 adds surface=SHOUT, not a new verb. Preserve compute 1, last-1 retention, public same-room restriction, and silent WATCH. Later retention slices are separate pins; localization must not turn message content into executable instructions or broaden its audience.

### Verification before adoption

Test same-room observation, adjacent-room exclusion, hidden-room refusal, overwrite, and repeated idempotent submission. Include markup and prompt-injection-like message text as inert content. Verify no WATCH ticker, additional event type, or cross-room leak appears and later retention fixtures do not rewrite S4’s baseline.

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=SHOUT` in a public room and keep the last 1 shout for PLAY. Isolated tests only. Help unchanged. No Genesis change.
