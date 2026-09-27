# Evidence collection progress — 2026-09-27

This file is the recovery checkpoint for the ongoing public-evidence meta-analysis.

## Current repository state

Source of truth: `data/evidence/index.json`.

- historical model × harness × configuration observations: **223**
- direct product observations: **228**
- cross-product / family observations: **57**
- practitioner/user signals: **17**
- total preserved evidence records: **525**
- business tasks: **86**
- solution catalog entries: **157**
- current task × solution mapping links: **4393**
- raw pairs with direct product evidence: **421**
- raw pairs with direct product probability-like evidence: **206**
- raw pairs supported by a family-level quantitative prior: **3073**
- tasks with direct product evidence: **86/86**
- tasks with family-level quantitative prior support: **61/86**

Published scorer output is currently **product-task-v1.7**. The enlarged evidence corpus is marked for **product-task-v1.8** regeneration with `python3 scripts/build_product_task_scores.py`.

The raw coverage counts above are deliberately distinct from scorer-qualified empirical-success counts: the scorer applies relevance, shrinkage, independence clustering and grade thresholds.

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

## Reliable test-generation batch

SWE-Mutation (ACL Findings 2026) is now preserved at two levels:

- family prior: generated-test VRR 40.4% at the best published configuration and RDR 71.71% support signal;
- 14 exact model × harness observations across Mini-SWE-Agent and Claude Code for seven models.

Historical exact-configuration corpus is now **223 observations**. Family corpus is **49 observations**. v1.8 rescore is pending.

## PILLAR GO reproducible threat-modeling metrics

Extracted directly from the public replication CSVs for Claude Sonnet 4.5 multi-agent across three LINDDUN GO systems:

- accuracy: 0.697 / 0.727 / 0.727; mean ≈ **0.717**;
- F1: 0.792 / 0.842 / 0.809; mean ≈ **0.814**.

Mean accuracy is stored as the conservative probability-like family signal; F1 is support-only. This gives `cyber-threat` a quantitative threat-modeling family prior while preserving the privacy→general-TARA transfer caveat.

## Evidence-count reconciliation

Source files were re-counted rather than trusting stale index counters:

- historical configuration observations: **223**
- direct product observations: **207**
- family observations: **51**
- practitioner/user signals: **17**
- total preserved records: **498**

The index now derives from these source-file counts; v1.8 remains pending.

## HardSecBench embedded security batch

Added a dedicated `embedded-secure-code-generation` family instead of mixing security with generic embedded correctness.

HardSecBench (IJCAI 2026): **924 tasks**, including **325 firmware-C** tasks and 76 CWE categories. Across the 18 published model rows, median single-attempt functional pass is ≈ **88.2%** while median security pass is only ≈ **33.6%**. The security median is used as a family-level probability-like prior; the functional/security gap is support-only.

Current source-record count: **502**. v1.8 rescore remains pending until this evidence batch is a little larger.

## Direct-product benchmark batch

New persisted direct evidence:

- Kiro CLI: 5,778-trial AA-style replication, best composite 65.6% with GPT-5.6 Sol and strong model-selection sensitivity;
- SonarQube remediation lineage: SWE-bench / current agent migration evidence;
- Microsoft Security Copilot: phishing-triage RCT retained without forcing a product-security P(success) transfer;
- RealDocBench: Azure Document Intelligence 79.6%, Mistral OCR 4 81.3%, AWS Textract 54.0% per-question QA accuracy.

Current source-file counts: historical=223, product=215, family=57, user=17, total=**512**. v1.8 is still pending while the direct-product pass continues.


## Latest 2026-09-27 evidence expansion

The latest batch strengthened previously weak areas without converting capability claims into fake success rates.

- **Threat modeling:** IriusRisk customer evidence reports 50% less time per threat model and roughly doubled annual model throughput; PILLAR GO and TM-Bench remain the quantitative family-level success evidence.
- **CI / DevOps:** Harness vendor/customer evidence reports 85% faster pipeline onboarding, 7× faster issue resolution and 50% less pipeline debugging time. These are human-time/wall-clock signals, not direct success probabilities.
- **Static-analysis remediation:** current/lineage evidence for Snyk DeepCode, Semgrep, Veracode and Sonar is retained separately; Sonar's September 2026 update is stored as a relative resolution/cost change rather than an absolute success rate.
- **Documentation / knowledge:** Mintlify's 2,400-test docs benchmark and Kapa.ai's Logitech deployment add quantitative retrieval/answer-quality evidence. Kapa's >99% figure is grade C because the detailed audit sample/protocol is not public.
- **Enterprise search:** Rovo's reported 60% product-speed improvement is stored as wall-clock evidence only.
- **Code review:** GitHub's July 2026 workflow-tuning result is stored as roughly 20% lower review cost at maintained quality, not as an independent success probability.
- **HIL / testing:** AutoHIL and SWE-Mutation provide A-grade family priors, while CANoe/ecu.test/VectorCAST product records remain capability evidence unless a product-specific public success benchmark exists.
- **Requirements / ASPICE / secure embedded:** Smart Evidence Management, automotive requirement-rule verification, HardSecBench and SAKE now supply quantitative family evidence for several previously prior-only task classes.

### Rebuild status

A GitHub Actions workflow was briefly tested to automate regeneration, but GitHub did not allocate a runner (the job failed before any step; `runner_id=0`). The workflow was removed immediately so CI remains clean. The canonical reproducible mechanism is still:

```bash
python3 scripts/build_product_task_scores.py
```

No v1.8 scores are claimed until that script is actually executed against the current corpus.
