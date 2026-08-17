# ACCESS_POLICY S3 — Chamber ACCESS help

**Status:** Executable specification. Runtime authorized with RFC-0104.  
**Parent:** [ACCESS-POLICY-S2.md](ACCESS-POLICY-S2.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0104](../rfcs/RFC-0104-access-policy-help.md)  
**Does not open:** WED/ATTEST help · YOUR POSITION · event-catalog/0.3 · new modes  
**Next:** ACCESS_POLICY S0–S3 is the hosted family. WED / ATTEST help stay parked. Do not invent S4.

S3 lets Chamber PLAY name ACCESS. The operations are the ones already hosted in S0–S2.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New ACCESS verb | **REJECT.** |
| Help WED / ATTEST | **REJECT.** |
| Advertise ACCESS_POLICY schema name | **REJECT.** Player line is ACCESS. |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `access-policy-s3` |
| Catalog | `access-policy-catalog/s3` |
| Help ACCESS | true |
| Help WED / ATTEST | false |
| New verbs | none |
| Modes | DENY · CLEAR · ALLOW_ONLY (unchanged) |
| WATCH | unchanged |

---

## Runtime rule

Hosted Chamber MUST list ACCESS on `help` and list existing deny / clear / allow aliases on `help access`. MUST still omit WED, ATTEST, and the schema name ACCESS_POLICY. Isolated tests only. No Genesis change.
