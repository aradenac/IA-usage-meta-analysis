# Evidence collection progress — 2026-09-27

This file is the recovery checkpoint for the ongoing public-evidence meta-analysis.

## Current repository state

Source of truth: `data/evidence/index.json`.

- historical model × harness × configuration observations: **209**
- direct product observations: **207**
- cross-product / family observations: **41**
- practitioner/user signals: **6**
- total preserved evidence records: **463**
- business tasks: **86**
- solution catalog entries: **157**
- scored task × solution pairs: **4393**
- pairs with direct product evidence: **394**
- pairs with empirical success evidence: **267**
- pairs supported by a family-level empirical prior: **2762**
- tasks with direct product evidence: **86/86**
- tasks with empirical success evidence: **63/86**

Current scorer: **product-task-v1.7**. The current evidence batch has been rescored.

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

## Latest incremental batch

Committed after the checkpoint:

- TM-Bench v2 threat-modeling benchmark;
- 2026 academic six-tool threat-elicitation benchmark against novice/expert human baselines;
- FDE-Bench deployment-configuration benchmark;
- DeployBench fresh-machine research-artifact deployment benchmark;
- XL-DocBench strict reproducible long-document release.

These records are already in `data/evidence/public-family-observations.json`. Score regeneration is intentionally batched and is marked pending in `data/evidence/index.json`.

## v1.7 rescore

Evidence batch rescored across **4393** task × solution pairs.

- direct-product-evidence pairs: **394**
- family-prior-supported pairs: **2762**
- empirical-success pairs: **267**
- meta confidence: D=2046, E=2331, C=16
- tasks with family-prior support: **55/86**

The scorer is now synchronized with the persisted evidence corpus.

## Latest embedded-firmware batch

- Added EmbedEval Sonnet 4.6 pass@1: 68.0% on 233 cases, n=3 per case, Wilson 95% CI 64.4–71.3%.
- Added implicit-vs-explicit prompt gap support (~95% explicit vs ~60% implicit domain-knowledge prompts).
- Stored as family-level embedded-development evidence, not direct product evidence.
- Next scorer version marked pending: **product-task-v1.8**.

## AutoHIL industrial HIL benchmark

Committed ISSTA 2026 AutoHIL evidence:

- ACU in-house HIL: 90.33% script executability, 89.69% functional correctness;
- ASDM on dSPACE: 81.31% executability, 84.00% functional correctness;
- 64 new functional defects reported across the two industrial ECUs and patched by supplier technicians.

This is family-level HIL evidence, not evidence that CANoe/ecu.test/VectorCAST themselves attain those rates. v1.8 rescore remains pending.
