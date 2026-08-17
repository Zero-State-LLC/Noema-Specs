# GC7-S3 — Information Contest Form

**Status:** Executable specification. Runtime authorized with RFC-0042.  
**Parent:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)  
**RFC:** [RFC-0042](../rfcs/RFC-0042-information-contest.md)  
**Does not open:** `event-catalog/0.3` · HP · `SCAN` · claim rewrite  
**Next:** [GC7-THAW-PLAY.md](GC7-THAW-PLAY.md)

S3 lets Players contest a **public record** already visible in the room. The engine does not leak hidden facts. Sealing blocks new `INSPECT`; it does not change ledgered `archive_claim`. Chamber help for the existing aliases is [GC7-THAW-PLAY.md](GC7-THAW-PLAY.md).

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Fifth form as HP / SCAN / INFORMATION_WAR | **REJECT.** One named form only |
| Target hidden rooms or unread private claims | **REJECT.** Visible `ARTIFACT` only |
| Distinct error for hidden vs missing | **REJECT.** Both `NOT_FOUND` |
| Contest writes `archive_claim` | **REJECT.** ATTEST remains the writer |
| New events | **REJECT.** `ENTITY_UPDATE` seal |
| Help lists contest | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc7-s3` |
| Catalog | `conflict-catalog/gc7-s3` |
| Form | `INFORMATION_CONTEST` |
| Target | `ENTITY` that is a visible `ARTIFACT` |
| Follow-on | `ENTITY_UPDATE` `inspect_restricted_until` |
| Seal | SUCCESS 8 cycles · PARTIAL 4 cycles |
| Office profile (`acting_for`) | `ACCESS_RESTRICTED_ARCHIVE` |

### Stake pins (hosted; `contest-config.v02.json` unchanged)

| Pin | Value |
|-----|--------|
| Minimum stake | energy 6 · influence 8 · compute 2 |
| Success threshold | 100 millipoints |
| Partial threshold | −30 millipoints |
| Max duration | 8 cycles |

### Fail-closed

| Situation | Code |
|-----------|------|
| Unknown form (`INFORMATION_WAR`, …) | `FORM_FORBIDDEN` |
| Target not in this room / not visible | `NOT_FOUND` |
| Visible but not an `ARTIFACT` | `FORBIDDEN` |
| Projection contains hidden / claim / HP | `LEAK` |
| `INSPECT` while sealed | `FORBIDDEN` (no claim text) |

---

## Out of S3

```text
event-catalog/0.3
SCAN ATTACK HP
forced publication / claim flip
Chamber help
```

---

## Runtime rule

Hosted Chamber MUST accept `INFORMATION_CONTEST` on existing `CONTEST_DECLARE`. Help still omits CONTEST. Isolated tests only.
