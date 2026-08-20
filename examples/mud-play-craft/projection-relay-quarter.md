# Projection: Relay Quarter

**Seed:** `room.relay-quarter`  
**Entity:** `entity.relay-main` (INFRASTRUCTURE, infra_type relay, condition 70, power_stability 0.7)  
**Attention:** full (illustrative)  
**Scenario beat:** LOOK on arrival from Civic Exchange (south)

---

## Human PLAY (Feature B)

```text
Relay Quarter

Primary communication infrastructure. Early degradation pressure.

PRESSURE
The main relay is only holding steady — long-range messages may delay or fail if it worsens.

HERE
relay-main (infrastructure, condition: worn)

EXITS
south — Civic Exchange
east — Generator Hall
down — Infrastructure Vault (costs 1 energy)

STATUS
energy 79 · attention 7 · compute 64 · storage 16 · influence 40

HAPPENED
You reach Relay Quarter from the south.

AVAILABLE HERE
inspect relay-main
repair relay-main
walk south
```

First-paint max 3 (Feature C): inspect strained relay · repair · obvious return exit.

---

## After REPAIR (same room, illustrative HAPPENED)

```text
HAPPENED
You repair relay-main.
OK — condition improves (worn → serviceable).
energy −2 · attention −1.
Try: inspect relay-main · wait · walk south.
```

(Exact energy costs remain ACTION-CONTRACTS / deployment; numbers here are craft-shaped placeholders.)

---

## Notes

- Condition **band** “worn” is presentation of seed integer `70` under full attention; reduced attention may omit the integer (ATTENTION-PROJECTION).
- PRESSURE ties MESSAGE ecology (GC5) to local infra without adding a SHOUT/board verb.
- DOWN exit surfaces seed `traversal_cost.energy: 1` as plain language.
- No global world-report lines (e.g. Foundry stock) appear in this room’s PRESSURE.
