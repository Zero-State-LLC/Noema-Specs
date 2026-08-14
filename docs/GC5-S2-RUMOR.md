# GC5-S2 — Rumor Provenance

**Status:** Executable specification. Runtime authorized with RFC-0028.  
**Parent:** [GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md) · [GC5-S1-DELAY.md](GC5-S1-DELAY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0028](../rfcs/RFC-0028-rumor-provenance.md)  
**Does not open:** `RUMOR` / `SHOUT` / `BOARD` verbs · rumor score · truth scanner · `event-catalog/0.3` · GC1-S2 benefits · Chamber help advertising

S2 is the smallest increment that still satisfies scenario E’s *rumor* shape: uncertain information travels with a source lineage. It is not world truth.

---

## Doctrine

```text
CLAIM
→ COMMUNICATION
→ RECEIPT
→ RETELLING
→ SOURCE LINEAGE
→ INVESTIGATION / CONTRADICTION / CORROBORATION
→ REVISED BELIEF
```

```text
RUMOR ≠ TRUTH
RUMOR ≠ WORLD EVENT
RUMOR ≠ HIDDEN BACKEND KNOWLEDGE
RUMOR ≠ REPUTATION SCORE
```

| Temptation | Verdict |
|------------|---------|
| `RUMOR` / `SPREAD_RUMOR` | **REJECT.** Reuse `MESSAGE` |
| `RUMOR_*` events | **REJECT** |
| Gossip / truth score | **REJECT** |
| Omniscient true/false label | **REJECT** |
| Copies counted as witnesses | **REJECT** |
| Infer `LIED` from contradiction | **REJECT** |
| Auto-update stale claim to current truth | **REJECT** |

Pressures: **uncertainty** and **distance** (delay/failure still apply).

---

## Model (table-removal)

No first-class Rumor entity. A claim is Information:

| Field | Meaning |
|-------|---------|
| `claim_id` | Stable `claim.<hex>` |
| `originator_ref` | First in-world author (cannot be forged) |
| `subject_ref` | Optional entity or named subject |
| `content` | Authored text (bounded) |
| `created_cycle` | Origin cycle |
| `derived_from` | Prior claim if this is a material change or correction |
| `origin_class` | `PLAYER_MESSAGE` \| `INSTITUTION_NOTICE` \| `RECONSTRUCTION` |
| `visibility` | `PRIVATE` \| `INSTITUTIONAL` \| `PUBLIC` |
| `origin_claim_id` | Root of the lineage (self if origin) |

A transmission is a delivery of that claim:

| Field | Meaning |
|-------|---------|
| `transmission_id` | Stable |
| `claim_id` | Claim delivered |
| `sender_ref` | Actual sender |
| `recipient_ref` | Actual recipient |
| `message_id` | Existing `MESSAGE` id |
| `parent_transmission_id` | Immediate prior hop, if known |
| `received_cycle` | Delivery cycle |
| `source_sender_ref` | Immediate sender (same as `sender_ref`) |

Knowing a claim does not own it. Copying does not remove it from prior holders.

---

## Origin

Valid: Player-authored claim on `MESSAGE`; institutional public notice; a Player retelling a reconstruction they can see (content is still Player-authored).

Invalid: backend hidden truth, research annotation, admin-only observation, LLM-invented fact.

`originator_ref` is the acting Player (or org for a notice). Sender cannot set another Player as originator.

---

## Transmission

Ordinary `MESSAGE` without claim fields remains a private DM and does **not** create a claim.

A claim is created or retold when `MESSAGE` carries `as_claim`, `subject_ref`, or `parent_claim_id`.

Human aliases (not Chamber help):

```text
report <player> "text" [about <subject>]
pass <player> <claim_id>
repeat <player> "text" from <claim_id>
share <player> <claim_id>
```

All reduce to `MESSAGE`.

| Delivery | Claim effect |
|----------|----------------|
| Same-cycle `MESSAGE_DELIVERED` | Recipient holds the claim this cycle |
| Delayed (GC5-S1) | Originator holds at send; recipient holds at `deliver_at_cycle` |
| `UNREACHABLE` | No events, no debit, no claim, no transmission |

No rumor fast lane.

---

## Retelling / drift

Sender must already hold the parent claim (originated or received).

| Retelling text vs parent `content` | Result |
|------------------------------------|--------|
| Equal after trim | New transmission of the **same** claim |
| Materially different | New claim, `derived_from=parent`, new originator=sender, `origin_claim_id` stays the parent’s root |

Do not overwrite the earlier claim text. Similarity is exact trimmed text, not an LLM.

A correction is a derived claim. It does not rewrite or delete the prior claim.

---

## Uncertainty

Derived labels (projection; not a score):

| Label | Rule |
|-------|------|
| `REPORTED` | Default for a held claim |
| `CORROBORATED` | ≥ 2 **independent** origins (distinct `origin_claim_id`) same `subject_ref` and same trimmed content |
| `CONTESTED` | ≥ 2 independent origins same `subject_ref` and different content |
| `STALE` | `world.cycle - created_cycle ≥ 8` (time, not truth) |

`CORROBORATED` is not canonical truth. A false claim may be widely repeated.

Three transmissions of one origin remain **one** source.

Contradiction ≠ deception. Do not emit `LIED` / `DECEIVED`.

Do not scan world state to mark every claim true or false.

---

## Visibility

| Surface | Sees |
|---------|------|
| PLAY (holder) | Content, immediate sender, known ancestor claim ids they hold, derived label. Not research. |
| PLAY (non-holder) | Nothing of a PRIVATE claim |
| WATCH | PUBLIC/INSTITUTIONAL consequence pulses only. No DM text, no private sender, no hidden chain |
| STUDY | May name classes in the research partition |

A private source stays private even if a later derived claim is public. Do not leak hidden identities through backend lineage.

Anonymous posting is **not** added. Unknown source is only valid when the holder has no parent (`source = UNKNOWN` for an origin they did not receive).

---

## WATCH

No salience score. Pulses:

| Pulse | When |
|-------|------|
| `A report is circulating.` | Any PUBLIC or INSTITUTIONAL claim exists |
| `Conflicting accounts are circulating.` | ≥ 2 independent PUBLIC/INSTITUTIONAL origins, same subject, different content |

Must not include private sender, private MESSAGE text, hidden source chain, research confidence, or admin metadata.

---

## Coupling

**GC5-S0/S1:** same bands and delay. Failed send does not propagate.

**GC3:** rumor does not write a reputation scalar.

**GC6:** a reconstruction may later cite a held claim; S2 does not add that evidence kind.

**GC9:** repeated claims may later become tradition; S2 does not implement tradition.

**GC4:** `PUBLISH_NOTICE` may originate an INSTITUTIONAL/PUBLIC claim. Official ≠ fact.

---

## Identity / idempotency

Same `MESSAGE` idempotency key → same transmission, no duplicate claim.

A new key is a new deliberate send even if text matches.

`message_id` uniquely identifies a transmission.

---

## Security

- `claim_id` does not grant access. Holder set is originator + delivered recipients.
- Cross-world claim refs are `NOT_FOUND`.
- Forged `originator_ref` ignored / rejected.
- Research/admin origin rejected.
- Player text cannot invoke tools.
- Holding a claim grants no authority.

---

## A–J

| Test | Result |
|------|--------|
| A | Information + existing MESSAGE. No rumor primitive |
| B | Uncertainty + distance |
| C | No extra canonical verb |
| D | Couples to delay, notice, later reconstruction |
| E | `MESSAGE` stays the verb |
| F | Courier / verification habits can form |
| G | Send and delivery remain attributable |
| H | Human and agent same rights and timing |
| I | Meaningful with STUDY hidden |
| J | Without this, “rumor provenance” is an unpinned sentence |

---

## Out of S2

```text
RUMOR / SPREAD_RUMOR / SHOUT / BOARD
RUMOR_CREATED / RUMOR_SPREAD
gossip score / truth probability
omniscient misinformation detector
LLM rumor generator
prediction market / rumor marketplace
GC1-S2 accuracy bonus
crypto / Genesis reseed
```

---

## Runtime rule

Hosted Chamber applies claim linkage on existing `MESSAGE` when claim fields are present, and on `PUBLISH_NOTICE`. Help still omits rumor aliases. Do not reseed Genesis.

## Acceptance

1. A tells B a claim; B holds it after delivery.
2. B retells unchanged to C; C’s claim_id equals A’s; lineage shows A as origin.
3. B changes the text; C receives a derived claim; A’s content is unchanged.
4. Two hops from one origin are not two independent witnesses.
5. Two different originators, same subject and text → `CORROBORATED`, still not truth.
6. Delayed long-range delivers the claim on the S1 schedule.
7. `UNREACHABLE` creates no claim for the recipient.
8. WATCH has no private DM text. PLAY does not call the claim “known truth.”
9. Human and agent Players have the same hold/retell/delay rules.
