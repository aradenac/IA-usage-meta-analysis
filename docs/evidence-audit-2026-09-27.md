# Evidence meta-analysis audit — 2026-09-27

## Current state

The public-evidence meta-analysis now contains:

- **209** historical model × harness × configuration observations;
- **207** direct product observations, including capability-only rows;
- **36** cross-product family benchmark observations;
- **6** practitioner/user signals;
- **458** preserved evidence records in total;
- **4,393** scored solution × task pairs across 86 business tasks;
- **394** task-solution pairs with directly relevant product evidence;
- **2,432** pairs whose fallback prior is informed by a task-family benchmark;
- **267** pairs with enough empirical success evidence not to be primarily prior-driven.

All **156 active solution entries** have at least one primary product/project source. Continue is retained only as historical evidence.

## Evidence tiers by solution

The current per-solution audit is stored in `data/evidence/coverage-by-solution.json`.

The coverage tiers are intentionally not rankings:

- direct quantitative success evidence;
- direct quantitative effort/relative evidence;
- historical harness quantitative evidence;
- qualitative field evidence;
- capability-only evidence.

A capability-only product is not considered unstudied: its workflow has been verified, but no defensible public performance estimate was found.

## Method

See `docs/evidence-meta-analysis-methodology.md`.

The scorer is reproducible through `scripts/build_product_task_scores.py`.

The model keeps three confidence dimensions separate:

1. P(success);
2. active-human effort;
3. monetary cost.

The overall MetaScore confidence is conservatively the weakest of these inputs. Current global MetaScore confidence is:

- C: **16 pairs**
- D: **1717 pairs**
- E: **2660 pairs**

No A/B global MetaScore is claimed yet. In many cases success is well benchmarked but human-effort transfer or enterprise contract pricing remains uncertain.

## Important empirical corrections

### Agentic coding

Terminal-Bench 4.0 is now represented separately from older Terminal-Bench versions. TB4 contains 66 tasks, uses calibrated resources, removes saturated/problematic tasks and requires fresh runs.

Current official TB4 results include materially lower resolution rates than older saturated/less difficult suites for several current model+harness pairs. This prevents older Terminal-Bench results from being mistaken for present frontier-task success.

The corpus also preserves contradictory productivity evidence: simpler controlled GitHub Copilot experiments show time savings, while METR found a slowdown for experienced developers working in mature repositories with early-2025 tools.

### Code review

Direct product evidence now includes Martian Code Review Bench, PR-Review-Bench, Bito's truth set, Augment's public benchmark and field-resolution signals. F1/issue-coverage measures are used only as approximate success proxies; comment volume/noise is preserved separately through practitioner signals.

### Requirements engineering

Generic requirement review remains weak: a 2026 expert/INCOSE benchmark found roughly 47% recall for the best tested generic model.

In contrast, task-specific approaches are materially stronger:

- ProReFiCIA: 85.7% recall on unseen industrial requirements, 95.8% with domain RAG;
- LusGen: traceability accuracy up to 88.4%;
- itemis ANALYZE customer/reference evidence shows large traceability/ASPICE effort reductions;
- QVscribe has both review-time evidence and a weaker long-term customer estimate of issue catch rate.

This justifies separate priors for review, traceability and change-impact analysis instead of one generic “requirements AI” prior.

### HIL / verification

AutoHIL reports approximately 84–90% functional correctness and 81–90% executability on industrial ECU HIL workflows.

Commercial CANoe and ecu.test agent workflows are therefore considered functionally plausible but do not inherit AutoHIL's measured probability as direct product performance.

Parasoft contributes direct productivity evidence for static-analysis remediation and AI-assisted test workflows; VectorCAST remains strong capability evidence pending a comparable public success benchmark.

### Static analysis and security remediation

Direct product evidence now includes:

- Snyk DeepCode AI;
- Semgrep remediation;
- Veracode Fix;
- Mend SAST third-party validated remediation;
- Parasoft productivity outcomes;
- Checkmarx effort claims.

Klocwork and Coverity expose useful AI/MCP workflows but no comparable public success-rate benchmark was found; they remain capability-supported, not success-proven.

### Functional safety

SAFARI provides an important negative correction. Across 3,000 industrial HARA cases, frontier LLMs generated plausible narratives but remained weak on categorical ISO 26262 reasoning, with best ASIL macro-F1 around 0.261.

Safety-impact scores must therefore remain human-in-the-loop and low-confidence unless a specialized tool is validated on company data.

### Vulnerability remediation

Two deliberately conflicting benchmarks are retained:

- an execution-calibrated study on 922 JavaScript vulnerability patches reports only 23% fixed by the best tested model;
- VulnBench reports substantially higher judge-based pass rates on a curated 200-CVE protocol.

The discrepancy is informative: judge-only evaluation can overestimate real repair when functional preservation is enforced.

### Architecture

R2ABench shows that systems identify architecture nodes much better than relationships (public summaries around 0.57 node F1 vs ~0.13 edge F1).

ArchBench-style trace-link recovery can be much stronger (~0.86 weighted F1) when the problem is constrained to architecture↔source traceability.

### Long-document reasoning

XL-DocBench demonstrates that context-window size is not equivalent to reliable long-document reasoning: the best public system remains around 44% overall accuracy on expert-verified professional documents.

Mistral OCR/document parsing has strong current extraction benchmarks, but OCR quality is kept distinct from downstream reasoning success.

### Deep research / enterprise knowledge

DeepSearchQA, BrowseComp, HLE and DRACO provide direct or relative evidence for Perplexity, ChatGPT/Researcher and Claude-family research systems.

Enterprise-product field evidence now also includes Rovo, NotebookLM/Gemini, Kapa and Glean. Large customer time-saving claims are treated as human-effort evidence, not correctness.

### Meetings

Granola, tl;dv, Fireflies, Fathom, Otter and Read have comparative transcription/action-item evidence. The derived composite is documented and remains grade C because the source is not a standardized independent benchmark.

### Workflows

AutomationBench materially lowers the family prior for complex multi-app autonomous workflows: current systems remain around 42–50% end-to-end success on the benchmark.

Vendor case studies from Zapier, Workato and Harness provide useful field/effort evidence but do not override AutomationBench as a general success prior.

### Release engineering

ReleaseEval provides a large benchmark for release-note generation (94,987 examples), but public evidence for complete release preparation remains sparse. Industry survey evidence also shows persistent human-review burden for AI-generated software.

### Learning / tutoring

Randomized evidence supports benefits from structured AI tutoring, but LongTutor shows continuing weakness in longitudinal diagnosis and adaptive teaching. Generic chat capability should not be treated as proof of effective technical coaching.

## Current weak zones

The most valuable remaining public evidence gaps are:

- product-specific HIL success rates for CANoe and ecu.test;
- product-specific architecture/modeling quality for Enterprise Architect/Kernaro;
- current Klocwork/Coverity AI remediation accuracy;
- product-specific ASPICE compliance correctness;
- release preparation beyond release-note generation;
- company-context workflow agents under real Jira/GitLab/SharePoint permissions;
- technical-learning outcomes for experienced engineers rather than students;
- exact enterprise prices for specialist engineering tools.

## Internal benchmark priorities

Public evidence is now broad enough that internal benchmarking should focus on high-value unresolved comparisons rather than generic model bake-offs:

1. CANoe AI vs ecu.test agent on representative HIL requirements.
2. itemis ANALYZE vs current traceability/ASPICE workflow on real project artifacts.
3. QVscribe / Codebeamer AI / IBM Engineering AI Hub / Polarion on company requirement templates.
4. Klocwork / Coverity / Parasoft / Mend / Semgrep on embedded C/C++, MISRA/CERT and representative defects.
5. Kernaro / generic coding agents on real Enterprise Architect or text-as-code architecture changes.
6. Workflow agents on Jira/GitLab/SharePoint with real permission boundaries and deterministic final-state verification.
7. Long-document tools on actual datasheets, reference manuals and customer/internal specifications.

## Interpretation

A high MetaScore with D/E confidence means “economically attractive under current assumptions and worth validating”, not “proven best”.

Point estimates should always be read together with the pessimistic/optimistic interval and the three component confidence grades.
