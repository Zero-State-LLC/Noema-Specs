# Projection: Civic Exchange

**Seed:** `room.civic-exchange`  
**Roles:** trade, starting_position  
**Attention:** full (illustrative)  
**Scenario beat:** fresh LOOK after ENTER_WORLD (no prior HAPPENED)

---

## Human PLAY (Feature B)

```text
Civic Exchange

Central meeting and trade hub. High visibility.

PRESSURE
Open floor — no local infrastructure under strain. Good place to meet and trade.

HERE
(no one else here)
(no local interactables)

EXITS
north — Relay Quarter
east — Transit Ring
west — Storage District
down — Archive (access token required)

STATUS
energy 80 · attention 8 · compute 64 · storage 16 · influence 40

HAPPENED
You take in Civic Exchange.

AVAILABLE HERE
look
wait
walk north
walk east
walk west
```

`help` / `help trade` remain under MORE (Feature C); not dumped on first paint.

---

## Notes

- Archive exit keeps the seed `ACCESS_TOKEN` condition as plain language; it does not reveal how to obtain the token if that is not yet observable.
- Empty HERE is honest when seed `entity_ids` is empty and no co-located Players.
- Social density becomes PRESSURE/HERE content when other Players are present — not invented in this snapshot.
- First-paint actions prefer movement to asymmetric rooms (Relay / Foundry via Transit) over empty wait, per Feature C preference order.
