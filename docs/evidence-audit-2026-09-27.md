# Evidence meta-analysis audit — 2026-09-27

## Scope

This audit tracks the public-evidence phase that follows the solution and pricing inventories.

The objective is not to manufacture a ranking from sparse data. The objective is to preserve all available evidence, separate direct product performance from family-level capability, quantify uncertainty, and then build task-specific economic scores.

## Current evidence layers

The repository now distinguishes four evidence layers:

1. **Historical model × harness × configuration observations**
   - retained in `data/observations.json`;
   - used only when a current product maps credibly to the same execution surface;
   - never replaced by a product-level average.

2. **Direct product evidence**
   - stored in `data/evidence/public-product-observations.json`;
   - includes controlled benchmarks, field benchmarks, customer telemetry, case studies and capability-only observations;
   - product evidence is tagged with an independence cluster to avoid double counting the same experiment.

3. **Cross-product family evidence**
   - stored in `data/evidence/public-family-observations.json`;
   - used to correct the fallback prior for a task family;
   - never attributed as if it were a direct benchmark of a commercial product.

4. **Public practitioner/user signals**
   - stored in `data/evidence/public-user-signals.json`;
   - retained as E-grade qualitative evidence;
   - positive and negative observations are both preserved.

## Method

The full methodology is documented in:

- `docs/evidence-meta-analysis-methodology.md`
- `docs/evidence-grading.md`
- `docs/metascore.md`
- `docs/pricing-methodology.md`

The scoring pipeline is reproducible through:

- `scripts/build_product_task_scores.py`

The scorer keeps success probability, active-human effort and monetary cost as separate evidence dimensions.

## Important empirical corrections discovered during the evidence phase

### Workflow agents

AutomationBench tests realistic end-to-end tasks across 47 tools using deterministic final-state verification.

Current public/private benchmark results show that even strong systems remain around roughly 42–50% success on complex multi-app workflows.

**Implication:** the generic native-workflow prior must not be interpreted as evidence that a workflow agent succeeds on most complex automations.

### Requirements review

A 2026 requirements-quality benchmark based on expert/INCOSE ground truth found that the best tested generic LLM recovered only about 47% of expert-identified issues, with non-trivial false flags.

**Implication:** generic LLM review of engineering requirements remains assistive, not autonomous.

### Requirements change-impact analysis

ProReFiCIA achieved 85.7% recall on an unseen industrial requirements dataset and 95.8% with domain RAG while requiring engineers to review only a small fraction of the requirements set.

**Implication:** requirement-impact analysis is substantially more mature when retrieval and task-specific structure are added.

### HIL test generation

AutoHIL, evaluated on industrial ECUs, reported approximately 84–90% functional correctness and 81–90% script executability.

**Implication:** domain-grounded HIL generation is a more credible family prior than generic coding-agent benchmarks for physical-bench test authoring.

### Architecture generation

R2ABench shows a strong asymmetry: current systems recover architecture entities materially better than relationships. Public summaries report node F1 around 0.57 but edge F1 around 0.13, with hallucinated dependencies as a dominant failure mode.

**Implication:** attractive syntax/PlantUML validity must not be confused with reliable architecture reasoning.

### Extra-long technical/professional documents

XL-DocBench uses expert-verified evidence across professional documents up to thousands of pages. The best public system remains around 44% overall accuracy.

**Implication:** large-context support alone is not evidence of reliable document reasoning. Retrieval, evidence selection and abstention remain major failure points.

### Security compliance

TrustBench reports strong average results on structured SOC 2 compliance detection, but the hardest judgment-heavy tasks remain far weaker.

**Implication:** structured gap detection appears viable; materiality/ambiguity judgment still requires human review.

### Coding productivity

The corpus deliberately preserves conflicting evidence:
- controlled GitHub Copilot experiments on simpler greenfield tasks show large time savings;
- METR's randomized study of experienced developers in their own mature repositories found a 19% slowdown with early-2025 tools;
- later METR follow-up signals suggest improvement, but the authors caution that selection effects make precise current estimates uncertain.

**Implication:** coding ROI is task- and context-dependent. One global “AI coding productivity multiplier” is invalid.

## Capability evidence versus success evidence

Many specialist engineering products expose strong deterministic context:
- static-analysis findings;
- traceability graphs;
- requirements databases;
- HIL/SIL execution state;
- security models;
- architecture models.

Official documentation can establish that the workflow exists, but a feature page alone cannot establish a probability of success.

Such rows remain useful for functional fit and prioritizing internal benchmarks, but do not create P(success).

## Current weaknesses

The weakest evidence remains concentrated in:

- ASPICE compliance outcomes;
- safety impact analysis;
- architecture review beyond architecture-generation benchmarks;
- release preparation and release-note correctness;
- technical coaching/learning transfer to experienced engineers;
- product-specific HIL benchmarks for commercial tools;
- product-specific threat-model quality for commercial TARA platforms;
- product-specific enterprise-workflow success under engineering data and permissions.

These rows should remain D/E until stronger evidence or internal experiments exist.

## Internal benchmark priorities

The highest-value internal experiments are those where:

1. a product has strong functional fit;
2. public evidence is sparse;
3. the business task is frequent or expensive;
4. product cost is material;
5. competing solutions have similar point estimates.

Priority examples:

- Vector CANoe AI vs ecu.test agent on representative HIL requirements;
- itemis ANALYZE / existing traceability workflow on project-realistic ASPICE evidence;
- QVscribe / requirements copilots on the company's requirement templates;
- Klocwork / Coverity / Parasoft AI remediation on embedded C/C++ rule sets;
- architecture/model assistants on real Enterprise Architect or PlantUML artifacts;
- workflow agents on Jira/GitLab/SharePoint processes with real permission boundaries;
- long-document assistants on actual datasheets/reference manuals and internal technical specifications.

## Interpretation rule

A high MetaScore with low evidence confidence means:

> economically attractive under the current assumptions and a high-priority candidate for validation.

It does **not** mean:

> proven to be the best solution.

