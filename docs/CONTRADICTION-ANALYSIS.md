# Contradiction Analysis (v0.3)

Builds on [CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md) (v0.2).

## Outputs (research)

* unresolved contradictory observations  
* agent behavior under contradiction (actions taken, sources used)  
* source-selection patterns  
* correction / non-correction after conflict  
* persistence despite counterevidence  

## Forbidden as direct observation

> Agent believed source A.

Allowed:

> Agent continued using source A after three conflicting observations.

Belief claims require explicit governed self-report/belief records.

## Extension Points

Non-normative source-comparison and research annotation seams.

- Extend analysis records linking conflicting observations to subsequent actions, cited sources and correction/non-correction windows. Keep unresolved conflict representable; an analysis plugin cannot resolve world truth or overwrite contradictory source records.
- Preserve the distinction between observed continued source use and inferred belief. A belief claim needs an explicit governed self-report/belief record; absent evidence remains unknown, not proof of stubbornness or private cognition.
- Compatibility/promotion: version source-selection rules and observation windows so agent-version comparisons remain bounded. Permissioned STUDY access is independent of Controller enrollment and ACCESS slice numbers; never insert research conflict annotations or hidden sources into PLAY.
- Verification proposal: compare a trace that corrects after counterevidence, one that continues using a source, and one with no observable subsequent choice. Assert only the supported output is emitted and both sides' provenance remains linked. A keyboard-readable source comparison should label unresolved status and uncertainty in text, with localized captions that do not upgrade inference to observation.
