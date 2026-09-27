# Evidence meta-analysis and task scoring methodology

Snapshot: 2026-09-27.

This document defines how heterogeneous public evidence is collected and transformed into task-level estimates. It extends `docs/methodology.md`, `docs/evidence-grading.md`, `docs/metascore.md` and `docs/pricing-methodology.md`.

## 1. Unit of analysis

The business output remains:

**solution/configuration × task T**

A solution may be:

- an exact model + harness + configuration already observed in a benchmark;
- a coding surface with several possible models;
- a specialist engineering product;
- a research/document/search/meeting application;
- an enterprise agent/workflow platform;
- a model/API/runtime backend.

Exact historical model × harness × configuration rows are never deleted or replaced by product-level estimates.

## 2. Preserve observations, do not collapse sources early

One candidate may have multiple evidence rows.

Every evidence row should preserve, where available:

- source and publication date;
- benchmark/dataset/protocol;
- product/model/harness/configuration;
- evidence family;
- sample size;
- raw metric and metric semantics;
- whether the metric is probability-like;
- cost/runtime/human-time information;
- source independence cluster;
- source grade;
- task relevance;
- limitations and transfer assumptions.

Contradictory observations are preserved. They are not removed merely because another source is newer or more favorable.

## 3. Evidence classes

### Benchmark / controlled evaluation

Preferred evidence. Examples: Terminal-Bench, Aider Polyglot, SWE-bench, Martian Code Review Benchmark, Qodo PR-Review-Bench, literature-search retrieval benchmarks.

### Field benchmark

Same product used on real repositories, incidents, meetings or enterprise queries with an explicit protocol and ground truth.

### Case study / operational measurement

Real deployment with quantitative outcomes, but weaker controls and often vendor selection bias.

### Capability evidence

Official documentation proving that a workflow exists. It affects functional fit and confidence, but **does not create a success probability by itself**.

### User/practitioner signal

Community reports, practitioner comparisons and qualitative field experience. Kept as weak E-grade evidence. Positive and negative reports are both retained.

## 4. Grades

The existing A–E scale is retained:

- A — primary/reproducible measurement with strong protocol;
- B — close empirical measurement with limited transfer;
- C — empirical proxy, vendor-run evaluation or case study with material limitations;
- D — derived estimate / significant transfer;
- E — anecdote / weak field signal / fallback prior.

Vendor-run numbers are not automatically rejected. Their vendor involvement is recorded and normally caps the effective grade unless independently reproduced.

## 5. Independence and double counting

A blog post, whitepaper and product page describing the same experiment count as one evidence cluster.

Repeated measurements on the same benchmark snapshot are correlated and their aggregate influence is capped.

A current independent benchmark can coexist with an older vendor benchmark: both are preserved, but they are not treated as two fully independent samples if they reuse the same underlying dataset.

## 6. New evidence families

Product-specific evidence is mapped to business tasks through a separate relevance matrix rather than distorting the original coding-benchmark taxonomy.

Examples:

- code-review-specialist;
- requirements-quality;
- requirements-traceability;
- requirements-to-test;
- static-analysis-remediation;
- hil-test-agent;
- enterprise-search;
- deep-research;
- literature-search;
- documentation-assistant;
- meeting-intelligence;
- observability-investigation;
- workflow-agent;
- threat-modeling.

The original coding families remain unchanged.

## 7. From raw evidence to P(success)

### 7.1 Probability-like evidence

Pass rate, issue/root-cause accuracy, recall/F1 when it directly approximates the task Definition of Done, and similar empirical rates can contribute to P(success).

They are still discounted by task relevance and evidence quality.

### 7.2 Relative or non-probability metrics

Metrics such as:

- precision@k;
- pairwise preference ratios;
- relative productivity improvement;
- ROI;
- wall-clock speedup;
- coverage increase;

are **not** interpreted as P(success) directly.

They may:

- adjust a prior modestly;
- inform active-human-time estimates;
- inform cost;
- increase/decrease confidence;
- remain display-only evidence.

### 7.3 Capability-only evidence

A product claiming a feature such as “generate test from requirement” proves fit, not success probability. When no empirical performance evidence exists, the score remains prior-driven and confidence stays low.

## 8. Product-level success prior

For product-level candidates with no direct benchmark, the initial prior is based on how the product relates to task T:

- native workflow: 0.68;
- direct normal use: 0.58;
- connected workflow: 0.52;
- custom workflow: 0.48;
- backend only: 0.40.

These are fallback priors, not product ratings.

Specialist products receive no automatic bonus simply because they are specialist. Their benefit must come from task fit, direct empirical evidence, lower human effort, or lower cost.

## 9. Aggregation

For probability-like observation i:

`w_i = quality_weight × task_relevance × sample_factor × independence_factor`

Quality weights:

- A = 1.00
- B = 0.80
- C = 0.60
- D = 0.40
- E = 0.20

Sample factor is logarithmic and capped so huge telemetry datasets do not erase protocol uncertainty.

The aggregated probability is a shrinkage estimate:

`P = (prior_strength × prior + Σ(w_i × p_i)) / (prior_strength + Σw_i)`

Default `prior_strength = 2`.

Relative/non-probability evidence can alter the resulting estimate by at most ±10% unless a documented transfer rule exists.

## 10. Human effort

The existing per-task `humanAI`, `humanAIlo`, `humanAIhi`, `humanNo`, `humanNolo`, `humanNohi` baselines remain the starting point.

Direct empirical time-saving evidence may change active-human time only when it measures substantially the same work.

Wall-clock agent speedups do not count as active-human savings unless the source demonstrates that the engineer is actively occupied for that time.

## 11. Reference cost scenario

MetaScore still uses the existing human reference:

- human labor rate: **50 €/h**.

For fixed subscriptions a per-task allocation requires an explicit scenario. The default reference scenario is:

- 50 engineers/users;
- 80 AI-eligible engineering hours per licensed user per month;
- sensitivity: 40 / 80 / 120 hours;
- 12 months/year;
- organization contracts spread across 50 reference users unless the contract is naturally project/workspace based.

A seat subscription is therefore not “free per task”. Its fixed cost is amortized over the declared AI-eligible workload.

Open-source software similarly has zero license cost but can still carry model/API, compute and operations cost.

## 12. FX snapshot

For cross-currency normalization, use an explicit dated FX snapshot.

Current reference:

- ECB 2026-09-25: 1 EUR = 1.1403 USD.
- ECB 2026-09-25: 1 EUR = 7.6551 CNY.

FX is an economic scenario input, not evidence of product quality.

## 13. MetaScore

The economic formula remains unchanged:

`C_attempt = C_service/API + active_human_hours × 50 €`

`C_success_AI = C_attempt / P(success)`

`MetaScore = 100 × C_human / (C_human + C_success_AI)`

where:

`C_human = humanNo_hours × 50 €`

Interpretation:

- 0: task not feasible;
- <50: human-only path cheaper under the scenario;
- 50: break-even;
- >50: AI path cheaper;
- 80: AI expected cost ≈ one quarter of human cost.

Evidence quality remains orthogonal to MetaScore.

## 14. Uncertainty

Each task score stores:

- point estimate;
- lower/upper sensitivity estimate;
- effective evidence grade;
- evidence coverage;
- number of independent empirical clusters;
- whether success, human time or cost is prior-driven.

A high MetaScore with grade E is therefore explicitly a **benchmark priority**, not a proven recommendation.

## 15. Output rule

Task rankings must not silently compare incomparable purchase scopes.

The scorer must:

- apply pricing bundle rules;
- avoid double counting shared seats;
- add prerequisites when not already owned;
- add BYOK/model/compute cost where applicable;
- expose the declared company/usage scenario.



## 16. Family-level empirical priors

Version `product-task-v1.2` adds a second layer between the generic relationship prior and direct product evidence.

Some public benchmarks evaluate a **class of workflow** rather than one catalog product. Examples include:

- AutomationBench for multi-application workflow agents;
- AutoHIL and HIL-GPT for HIL test-generation/assistance;
- academic requirements-quality benchmarks;
- requirements-to-test generation studies;
- architecture traceability benchmarks;
- threat-modeling research benchmarks.

These observations are stored in `data/evidence/public-family-observations.json`.

They may modify the relationship prior, but they are never presented as direct performance of CANoe, ecu.test, Zapier, QVscribe, itemis or another vendor.

The current family-prior update is deliberately weaker than direct product evidence:

- only task relevance >= 0.20 is considered;
- source grade and sample factor still apply;
- correlated observations from the same family are capped;
- total influence from one family is capped at 0.75 weight;
- the generic relationship prior keeps strength 2.

This means a strong family benchmark can move a prior materially without allowing an unbenchmarked product to inherit the benchmark score verbatim.

## 17. Separate confidence dimensions

A single confidence grade was found to hide important distinctions. Version `product-task-v1.1+` therefore exposes:

- `success_grade`;
- `human_time_grade`;
- `cost_grade`;
- `meta_confidence_grade`.

The global MetaScore confidence is conservatively the weakest of the three input dimensions.

Example: a product may have a C-grade case study showing a strong time saving while P(success) still relies on an E-grade prior. Its point MetaScore may be attractive, but the global confidence remains E.

## 18. Product scores versus configuration scores

Product-level scores answer:

> Which purchasable solution is economically promising for task T?

Historical model × harness × configuration scores answer:

> If I already choose this execution surface, which exact model/configuration is preferable?

The product layer must not erase the configuration layer. For coding agents in particular, harness and model interactions remain material and are retained in `data/configurations/` and `data/observations.json`.

## 19. Current scoring implementation

The current product scoring snapshot is version `product-task-v1.2`.

It produces:

- all solution × task candidate scores;
- point/optimistic/pessimistic MetaScore;
- point/low/high expected cost per successful result;
- P(success) and its evidence trail;
- active-human-time estimate and evidence trail;
- allocated service/license/API cost;
- direct product observations;
- family-prior observations;
- independence-cluster counts;
- explicit flags for prior-driven success/time/cost.

The canonical index is `data/task-scores/index.json`.
