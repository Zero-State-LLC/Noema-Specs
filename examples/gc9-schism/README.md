# GC9-S2 inheritance and schism fixtures

Executed by `check_gc9_s2`. Authority:
[GC9-S2-INHERITANCE-SCHISM.md](../../docs/GC9-S2-INHERITANCE-SCHISM.md) /
[RFC-0125](../../rfcs/RFC-0125-practice-inheritance-and-schism.md).

| Fixture | Pins |
|---|---|
| `inherited-beyond-founders.json` | Founders stop at cycle 5, a successor repairs at cycle 7 — inherited |
| `founders-only-no-inheritance.json` | Every actor is an originator; nobody succeeded them |
| `concurrent-practice-not-inheritance.json` | A co-practitioner is not an heir while the founders keep going |
| `schism-rival-accounts.json` | Two practitioners, two public claims — the only positive schism |
| `single-account-no-schism.json` | One public account divides nobody |
| `unattributed-accounts-no-schism.json` | Rival accounts by non-practitioners are commentary |
| `same-author-revision-no-schism.json` | One practitioner revising themselves is not a division |
| `private-accounts-no-schism.json` | Unpublished accounts cannot split a practice |
| `not-a-tradition-no-marks.json` | Marks cannot attach below `TRADITION` |
| `dormant-no-marks.json` | A dormant tradition carries no live marks |

The check additionally fails if any catalog non-derivation reason is never
exercised, if a projected line names an agent or entity, or if GC9-S1 expected
output changes.
