# Evidence collection progress — 2026-09-27

This file is the recovery checkpoint for the ongoing public-evidence meta-analysis.

## Current repository state

Source of truth: `data/evidence/index.json`.

- historical model × harness × configuration observations: **209**
- direct product observations: **207**
- cross-product / family observations: **36**
- practitioner/user signals: **6**
- total preserved evidence records: **458**
- business tasks: **86**
- solution catalog entries: **157**
- scored task × solution pairs: **4393**
- pairs with direct product evidence: **394**
- pairs with empirical success evidence: **267**
- pairs supported by a family-level empirical prior: **2432**
- tasks with direct product evidence: **86/86**
- tasks with empirical success evidence: **63/86**

Current scorer: **product-task-v1.6**.

## Interpretation

Coverage is now broad, but not uniformly strong.

Direct product evidence exists for all task families, yet some tasks still have no empirical success-rate evidence and therefore remain prior-driven for P(success). Family-level evidence can improve a prior but must not be mistaken for direct product measurement.

The current global confidence distribution remains deliberately conservative:

- C: 16
- D: 1717
- E: 2660

A high MetaScore with weak confidence is a benchmark priority, not a proven recommendation.

## Current weak targets

Tasks still lacking empirical success evidence are listed programmatically in `data/evidence/index.json`. The highest-priority research targets are:

1. requirements generation/review/decomposition and change impact;
2. safety/cyber threat/compliance work;
3. release preparation and release-note workflows;
4. technical-manual/datasheet analysis;
5. learning/tutoring workflows;
6. HIL/SIL and specialist embedded verification where only capability evidence exists.

## Persistence rule

All new findings are committed incrementally:

1. raw/public evidence record;
2. task-family relevance/transfer rule if needed;
3. coverage/index refresh;
4. scorer refresh only after evidence and mapping are persisted;
5. this checkpoint is updated after material batches.

No important evidence should exist only in chat context.
