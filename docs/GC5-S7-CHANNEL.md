# GC5-S7 — MESSAGE org channel

**Status:** Executable specification. Runtime authorized with RFC-0065.  
**Parent:** [GC5-S6-NOTICE.md](GC5-S6-NOTICE.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0065](../rfcs/RFC-0065-org-channel.md)  
**Does not open:** CHANNEL/NOTICE verbs · membership leak · help advertising · hidden channels · cycle expiry  
**Next:** [GC5-S8-TRADE-NOTICE.md](GC5-S8-TRADE-NOTICE.md)

S7 adds one MESSAGE surface. Current members may leave a note on the organization. It is not a channel verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| CHANNEL verb | **REJECT.** |
| Distinct outsider / unknown errors | **REJECT.** Same `NOT_ADDRESSABLE`. |
| Public broadcast | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help channel | **REJECT.** |
| Hidden-room send | **REJECT.** |
| Unlimited history | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s7` |
| Catalog | `communication-catalog/gc5-s7` |
| Verb | existing `MESSAGE` |
| Surface | `CHANNEL` only |
| Authority | current org member |
| Place | organization record; hidden rooms may not send |
| Cost | compute 1 |
| Keep | last 1 note per org |
| Events | `MESSAGE` only |
| PLAY | `A channel note in {org}: {text}.` (members only) |
| Fail | `NOT_ADDRESSABLE` for unknown org and non-member |
| WATCH | silent |
| Help | still omits CHANNEL |

---

## Out of S7

```text
CHANNEL verb
membership roster on PLAY / WATCH
cycle expiry
Chamber help CHANNEL
```

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=CHANNEL org_id=…` from a current member, keep the last 1 note on that org for member PLAY, reject hidden-room send, and use one non-leaking fail for unknown org and non-member. Isolated tests only. Help unchanged. No Genesis change.
