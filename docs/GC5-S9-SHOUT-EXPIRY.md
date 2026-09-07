# GC5-S9 — shout cycle expiry

**Status:** Executable specification. Runtime authorized with RFC-0080.  
**Parent:** [GC5-S4-SHOUT.md](GC5-S4-SHOUT.md) · [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0080](../rfcs/RFC-0080-shout-expiry.md)  
**Does not open:** SHOUT verb · other-surface expiry · MESSAGE_EXPIRED · help advertising · WATCH ticker  
**Next:** [GC5-S10-BOARD-EXPIRY.md](GC5-S10-BOARD-EXPIRY.md)

S9 makes a shout take world-time. A public shout is still last 1, then gone after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All surfaces | **REJECT.** Shout only |
| Duration ≠ 1 | **REJECT.** |
| `MESSAGE_EXPIRED` | **REJECT.** Silent drop |
| SHOUT verb | **REJECT.** |
| Help shout | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s9` |
| Catalog | `communication-catalog/gc5-s9` |
| Verb | existing `MESSAGE` |
| Surface | `SHOUT` |
| Keep | last 1 shout |
| Expire | 1 committed cycle |
| Events | existing `MESSAGE` only |
| PLAY | shout line absent after expiry |
| WATCH | silent |
| Help | still omits shout / BOARD |

---

## Out of S9

```text
SHOUT verb
notice cycle expiry is [GC5-S11-NOTICE-EXPIRY.md](GC5-S11-NOTICE-EXPIRY.md)
channel cycle expiry is [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md)
trade-notice cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
MESSAGE_EXPIRED
Chamber help shout
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop a public-room shout after 1 committed cycle, keep last-1 overwrite, and reject hidden-room shout. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Retention seam:** Extend replay fixtures around last-1 overwrite and the next committed-cycle expiry of public SHOUT content. Wall-clock passage and delivery retries should not be used as substitutes for the declared world-cycle rule.
- **Compatibility boundary:** RFC-0080 and communication-catalog/gc5-s9 pin a one-cycle projection lifetime, not ledger erasure or a new expiry event. Other surfaces already have their own linked expiry slices; do not generalize S9 into a shared policy that changes their contracts.
- **Validation expectations:** Compare pre-expiry and post-commit observations, two shouts in one cycle, replay from a snapshot, and hidden-room refusal. Check that the line disappears while source MESSAGE history remains, with no MESSAGE_EXPIRED, WATCH ticker, or newly advertised verb.
