# Agent Determinism Classification

`DETERMINISTIC` permits exact behavior equivalence with pinned inputs. `SEED_CONTROLLED` permits it only with pinned seeds and no recorded stream divergence. `NONDETERMINISTIC` remains studyable with declared wider bands/more repetitions. `UNKNOWN` disallows exact behavioral equivalence and needs conservative analysis. Classification is pinned in experiment/run identity. Nondeterminism never automatically invalidates a study.

