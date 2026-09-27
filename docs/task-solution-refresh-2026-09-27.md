# Task-by-task solution refresh — 2026-09-27

## Objective

Re-audit the exploitable AI solution landscape **task by task** for all 86 business tasks, and make newly verified relevant tools visible on the website as soon as they are accepted.

This file is the durable progress ledger for the working PR. It exists specifically so the research can continue across multiple sessions without relying on conversational context.

## Working rules

1. Process every task explicitly; do not infer that coverage of one task proves coverage of a neighboring task.
2. Prefer first-party/vendor documentation for product existence, current status and supported workflows.
3. A solution is added only when there is a concrete path from the product to the task:
   - `native`: first-class workflow;
   - `direct`: usable in the normal product interface;
   - `connected`: supported connector/MCP/integration required;
   - `custom_workflow`: orchestration or scripting required;
   - `backend`: model/API/runtime substrate only.
4. Do not rank products during this pass. Availability/relevance inventory is separate from evidence-based scoring.
5. Every newly accepted solution must be added to the canonical data and to the deployed site's inventory view in the same working PR.
6. Record rejected/obsolete/insufficiently supported candidates so they are not repeatedly rediscovered.

## Baseline discovered before Web re-audit

- Business tasks: **86**
- Canonical solution inventory (`data/solutions/index.json`): **157**
- The deployed site was **not consuming** the canonical solution inventory or `task-solution-map/all-current.json`; it still exposed mainly the historical model × harness candidate universe.
- First corrective action: surface the canonical inventory on the website before adding newly researched products.

## Progress

| Domain | Tasks | Status | Notes |
| --- | ---: | --- | --- |
| Requirements | 6 | complete | 6/6 tasks explicitly searched; 8 newly verified current solutions added and published to site snapshot. |
| Architecture | 6 | complete | 6/6 tasks explicitly searched; 8 additional current solutions added. |
| Development | 9 | pending | |
| Debug / upstream | 10 | pending | |
| Verification | 12 | pending | includes HIL/results/coding-rules |
| Safety / cyber | 10 | pending | |
| CI / tooling / release | 8 | pending | |
| Documentation | 5 | pending | |
| Collaboration | 8 | pending | |
| Learning / research | 12 | pending | |

## Change log

- 2026-09-27 — initialized durable task-by-task research ledger.
- 2026-09-27 — identified site/catalog drift: canonical inventory has 157 solutions while the site does not expose it.

## Requirements-domain audit

Status: **complete (6/6 tasks searched explicitly)**.

New solutions accepted during this pass:

- **Valispace / ValiAssistant** — generation, refinement, decomposition, parameterized requirements and traceability.
  - https://www.valispace.com/ai/
  - https://docs.valispace.com/vhd/introduction-to-valispace
- **Innoslate AI** — requirements/MBSE AI assistant, quality checks, traceability matrix and verification-oriented AI tools.
  - https://specinnovations.com/innoslate/artificial-intelligence-in-mbse
  - https://specinnovations.com/trust-center/ai
- **reqSuite rm + AI assistance** — quality checks, rewrite/refinement, trace-link suggestions and project-context change-impact questions.
  - https://www.reqsuite.io/en/blog/ai-assistance-reqsuite
- **Trace.Space** — agentic requirements, traceability, coverage and change-impact analysis for complex engineering.
  - https://www.trace.space/
  - https://www.trace.space/product
- **SPREAD Requirements Manager** — requirements extraction/classification, prior-program matching, conflict/gap detection and lifecycle traceability, explicitly positioned for automotive engineering.
  - https://www.spread.ai/requirements-manager
  - https://www.spread.ai/solutions/automotive
- **RequirementMatrix AI** — specialist agents for quality, consistency, dependencies, testability, standards and requirement-change review.
  - https://reqmatrix.com/
- **Arc** — requirements, architecture, tests, verification evidence and agent-assisted dependency/change maintenance for complex space systems.
  - https://www.archelps.com/
- **ModelgraphX** — AI-enabled systems/risk engineering linking requirements to safety analyses and verification evidence; especially relevant to later safety/cyber tasks.
  - https://www.modelgraphx.com/

Already-present solutions re-confirmed rather than duplicated include Modern Requirements Copilot4DevOps, QRA QVscribe/ReqWriter, ReqDrive, Reqi REX, KlugSpice, Codebeamer AI, IBM Engineering AI Hub, Jama Connect Advisor, Polarion Copilot and Visure Vivia.

Not added during this domain pass:
- medical-device-specific products whose primary scope is outside the current Automotive / Industrial IoT / common taxonomy were not automatically promoted merely because they have requirement AI features;
- research prototypes and low-maturity community prompt/skill packages were not treated as production solution surfaces.

Change log:
- 2026-09-27 — website now consumes a generated snapshot of the canonical solution inventory and current task mappings.
- 2026-09-27 — requirements domain completed; inventory increased from 157 to 165 solutions.

## Architecture-domain audit

Status: **complete (6/6 tasks searched explicitly)**.

New solutions accepted during this pass:

- **Dalus AI-Native MBSE** — SysML v2, requirements, trade studies, verification and an AI Copilot that creates structured architectures; MCP exposes the live model to assistants.
  - https://dalus.io/
  - https://dalus.io/features/mcp-workflows
- **Visual Paradigm AI Modeling** — AI-assisted UML generation and iterative architecture modeling across class, sequence, component, deployment and related diagram types.
  - https://www.visual-paradigm.com/features/uml-diagram-generator/
- **Softagram Analyzer + MCP** — repository-derived architecture/dependency model, blast-radius and structural analysis, exposed to AI agents through MCP; supports C/C++ among its language set.
  - https://softagram.com/en/softagram-analyzer/mcp
- **CodeAtlas** — live architecture maps plus MCP and evidence-gated AI review.
  - https://www.codeatlas.live/
  - Caveat: its published language list currently does not include C/C++, so its embedded applicability is limited to supported stacks.
- **JigsawML Architectural Intelligence** — interactive code/cloud architecture maps, dependency understanding and architectural change/drift analysis.
  - https://www.jigsawml.com/
- **Striff** — architecture-aware pull-request review using deterministic structural checks plus AI explanations.
  - https://striff.io/
  - Caveat: its current supported-language list does not include C/C++.
- **ArchTect** — VS Code C4/Structurizr architecture-as-code environment with AI and MCP workflows.
  - https://marketplace.visualstudio.com/items?itemName=nicobit.c4archtect
- **SPREAD Product Explorer** — engineering product/architecture graph across functions, components, signals, requirements and software with natural-language interrogation and source traceability.
  - https://www.spread.ai/product-explorer

Previously added requirements-domain products such as Valispace, Innoslate, Trace.Space and ModelgraphX were also mapped to architecture tasks where their first-party product capabilities substantiate that use.

Low-maturity research prototypes and small GitHub-only architecture experiments were not promoted to production solution status merely because they mention LLM architecture generation.

Change log:
- 2026-09-27 — architecture domain completed; canonical inventory increased from 165 to 173 solutions.
- 2026-09-27 — website snapshot regenerated from the 173-solution canonical inventory.
