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

## Extension Points

Non-normative help-presentation seams for the closed RFC-0104 slice.

- Extend an ACCESS help renderer from the accepted S0–S2 operations, preserving the public ACCESS name and deny/clear/allow aliases. Localization belongs to explanations and accessible names, not wire tokens or parser semantics.
- S3 is the help slice, not a privileged Controller security level. Help neither grants an occupied office nor bypasses enforcement; humans may inspect permitted documentation or non-canonical development tooling but do not issue Player actions.
- Compatibility/promotion: retain the accepted help listing and WATCH behavior. WED, ATTEST, ACCESS_POLICY schema-name advertising, new modes and an invented S4 remain outside this seam.
- Verification proposal: snapshot help and help access for the supported aliases; assert omitted names remain absent and help creates no world event or cost. Test missing translations, keyboard focus and screen-reader reading order independently from command authorization.
