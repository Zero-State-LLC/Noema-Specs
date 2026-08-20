# GC8-S5 — Lockout WAIT rest

Authority: [RFC-0117](../rfcs/RFC-0117-lockout-wait-rest.md). Catalog: [`economy-catalog.lockout-wait.json`](../specs/economy-catalog.lockout-wait.json).

WAIT already rests attention/compute. This slice rests a Player who has **energy 0 and storage 0** so cargo-full + zero-energy is not a permanent lock.

| Before WAIT | After WAIT |
|-------------|------------|
| energy 0 and storage 0 | energy 2, storage 1 |
| any other pair | unchanged by this slice |

No new verbs. HARVEST still costs energy 2 + compute 1 + free storage. Cargo MOVE still costs 2. WATCH silent. PLAY MAY say `If you have no energy and no free storage, wait.`
