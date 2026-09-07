# GC8-S5 — Lockout WAIT rest

Authority: [RFC-0117](../rfcs/RFC-0117-lockout-wait-rest.md). Catalog: [`economy-catalog.lockout-wait.json`](../specs/economy-catalog.lockout-wait.json).

WAIT already rests attention/compute. This slice rests a Player who has **energy 0 and storage 0** so cargo-full + zero-energy is not a permanent lock.

| Before WAIT | After WAIT |
|-------------|------------|
| energy 0 and storage 0 | energy 2, storage 1 |
| any other pair | unchanged by this slice |

No new verbs. HARVEST still costs energy 2 + compute 1 + free storage. Cargo MOVE still costs 2. WATCH silent. PLAY MAY say `If you have no energy and no free storage, wait.`


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- WAIT examples can cover the lockout boundary after cycle-commit side effects, as pinned by RFC-0117, rather than relying only on the request-time budget pair. Storage continues to mean free capacity, not carried cargo.

- Retain the existing catalog grant of energy 2 and storage 1 only for the simultaneous zero pair. Later cargo-fuel rules need their own precedence and version evidence; this section does not introduce passive regeneration, alter WAIT quorum, or retune HARVEST/MOVE.

- Validate both-zero, energy-only-zero, storage-only-zero, and neither-zero cases, plus a cycle side effect that changes eligibility. Verify one application per successful WAIT, replay-equivalent balances, unchanged node stock from this rest, and no WATCH disclosure.
