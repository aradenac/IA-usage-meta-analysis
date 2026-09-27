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
| Development | 9 | complete | 9/9 tasks explicitly searched; 9 additional current solution surfaces added. |
| Debug / upstream | 10 | complete | 10/10 tasks explicitly searched; 3 new connected/observability solutions added; embedded agents remapped. |
| Verification | 11 | complete | 11/11 tasks explicitly searched; corrected baseline count from 12 to 11; 4 industrial verification solutions added. |
| Safety / cyber | 10 | complete | 10/10 tasks explicitly searched; 8 product-security, safety and assessment solutions added. |
| CI / tooling / release | 8 | complete | 8/8 tasks explicitly searched; 4 agentic CI/container solutions added and existing tools remapped. |
| Documentation | 5 | complete | 5/5 tasks explicitly searched; no net-new mature product required, but current embedded/agentic tools were remapped. |
| Collaboration | 8 | complete | 8/8 tasks explicitly searched; Loom AI and Zoom AI Companion added, Atlassian workflows revalidated. |
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

## Development-domain audit

Status: **complete (9/9 tasks searched explicitly)**.

New solutions accepted during this pass:

- **Embedder** — purpose-built firmware agent combining repository, datasheet/reference-manual/errata, schematic, compiler, debugger and live-board context. It writes part-specific drivers and closes build→flash→test/debug loops on real hardware.
  - https://embedder.com/
  - https://embedder.com/news/migrate-from-freertos-to-zephyr-with-ai
- **Hydron** — embedded/system-software coding assistant with a hardware knowledge graph, spec-cited code generation, codebase/datasheet/BSP grounding and HIL/debug workflows.
  - https://www.hydron.sh/
  - https://docs.hydron.sh/get-started/overview/
- **MPLAB AI Coding Assistant** — Microchip-specific VS Code assistant with Agent Mode, codebase/terminal tools and an MCP server exposing device datasheets, board guides, compiler docs and examples.
  - https://www.microchip.com/en-us/tools-resources/develop/mplab-tools-vs-code/mplab-ai-coding-assistant
  - https://developerhelp.microchip.com/xwiki/bin/view/software-tools/ides/extensions/ai-coding-assistant/
- **IOcomposer** — embedded C/C++ IDE with AI grounded in the installed SDK/project and integrated build→flash→debug loop; currently strongest on Nordic bare-metal targets.
  - https://iocomposer.io/
- **TuyaOpen IDE** — VS Code/Cursor embedded AI workflow that creates projects/firmware from natural language with board/pin context and integrates build, flash, logs, cloud Agent and app generation.
  - https://docs.tuyaopen.ai/docs/ide
- **ByteAsk** — C/C++-specialized terminal agent with compiler/test/sanitizer/debugger/profiler tools and grounded standards/datasheet corpora.
  - https://www.byteask.ai/
- **fw-context MCP** — compiler-aware local MCP code intelligence for embedded C/C++ firmware, useful as a connected context layer for coding agents.
  - https://pypi.org/project/fw-context-mcp/
- **Refact.ai** — current autonomous coding agent with C/C++/Python support, BYOK and self-hosted deployment; added as a missing general direct coding surface.
  - https://refact.ai/
- **QodeAssist** — Qt Creator C++/QML AI assistant with completion, inline refactoring, project-aware tools, build/terminal access and MCP.
  - https://github.com/Palm1r/QodeAssist

Not promoted:
- single-purpose or near-zero-adoption GitHub prototypes were kept out when a more mature production surface covers the same task family;
- ordinary embedded IDE/configuration tools without an AI workflow were not counted merely because they generate code deterministically.

Change log:
- 2026-09-27 — development domain completed; canonical inventory increased from 173 to 182 solutions.
- 2026-09-27 — website snapshot regenerated from the 182-solution canonical inventory.

## Debug / upstream-domain audit

Status: **complete (10/10 tasks searched explicitly)**.

New solutions accepted:

- **Memfault AI + MCP** — embedded fleet metrics/logs/traces/issues with AI Issue Insights for root cause/scope/next steps, plus an MCP server for agent access to fleet data.
  - https://docs.memfault.com/docs/platform/ai-features
- **J-Link MCP** — community MCP bridge exposing J-Link flash/debug/RTT/crash-state operations to agents.
  - https://marketplace.visualstudio.com/items?itemName=Klievan.jlink-mcp
- **OpenOCD MCP Server** — community MCP bridge for flashing, stepping, register/memory inspection, breakpoints, watchpoints and ELF-symbol-aware target access through standard OpenOCD probes.
  - https://github.com/microhenrio/openocd-mcp

Important existing/new capabilities mapped rather than duplicated:

- **JetBrains AI Assistant / CLion 2026.2.2** now has a dedicated Cortex-M HardFault AI skill backed by MCP debugger tooling; its `debug-crash` relation was upgraded to native.
  - https://blog.jetbrains.com/clion/2026/09/hard-fault-debugging/
- **Embedder** and **Hydron** were mapped across embedded crash, intermittent, performance and HW/SW debugging because they drive live targets and hardware-aware diagnostics.
- **MPLAB AI Coding Assistant**, **IOcomposer**, **ByteAsk** and **fw-context MCP** were mapped where their documented device/toolchain/debug capabilities apply.

No separate TRACE32 “AI” product was added: current Lauterbach sources substantiate advanced debug/trace capabilities but not a distinct LLM/agent product surface. Likewise, ordinary tracing/profiling tools were not relabeled as AI without a documented AI workflow.

Change log:
- 2026-09-27 — debug/upstream domain completed; inventory increased from 182 to 185 solutions.
- 2026-09-27 — website snapshot regenerated from the 185-solution inventory.

## Verification-domain audit

Status: **complete (11/11 tasks searched explicitly)**.

New solutions accepted:

- **BTC TestStack + AI Assistant/MCP** — certified C/C++ unit/integration verification with requirements-based tests, coverage/MC/DC, formal verification, built-in AI assistance and MCP actions for external agents.
  - https://www.btc-embedded.com/products/btc-teststack
- **BTC TestAgent** — AI-driven system-level HIL/vHIL tester: requirement extraction/formalization → generated tests → symbolic validation → HIL execution → automated verdict and feedback loop.
  - https://www.btc-embedded.com/products/btc-testagent
  - Current availability note: initial 2026 rollout is limited to selected partner customers.
- **Cantata 26.04 + Test Automation Skill** — safety-oriented C/C++ unit/integration testing with AI-assisted test generation, coverage-gap analysis and iterative refinement through Claude Code, Codex, OpenCode and GitHub Copilot integrations.
  - https://www.qa-systems.com/tools/cantata
  - https://www.qa-systems.com/resources
- **TASKING Toolchain Agentic AI Workflows** — 2026 embedded compile/debug/test toolchain integration for agentic V&V via MCP, aimed at safety/security-critical automotive, industrial and related systems.
  - https://www.tasking.com/content/tasking-integrates-modern-ai-technology-to-enable-robust-software-verification-and-validation-vv/

Existing Parasoft C/C++test 2026.1, VectorCAST 2026 + Reqs2x, Vector CANoe AI/MCP, tracetronic ecu.test agent and the static-analysis AI/MCP products were re-confirmed rather than duplicated.

The canonical task file actually contains **11** verification tasks, not 12; the progress ledger has been corrected accordingly.

Change log:
- 2026-09-27 — verification domain completed; canonical inventory increased from 185 to 189 solutions.
- 2026-09-27 — website snapshot regenerated from the 189-solution inventory.

## Safety / cyber-domain audit

Status: **complete (10/10 tasks searched explicitly)**.

New solutions accepted:

- **Cybellum Product Security Platform** — AI-driven SBOM/product-risk/vulnerability workflow for connected-device manufacturers, with contextual triage, remediation guidance, PSIRT and automated compliance evidence for CRA, ISO/SAE 21434 and IEC 62443.
  - https://cybellum.com/platform/
- **C2A Security EVSec + AutoSynth AI** — automotive/cyber-physical TARA, attack trees, continuous risk and regulatory work products, with AI-generated threat analyses and MCP/A2A agent integration.
  - https://c2a-sec.com/platform/
- **Finite State Product Security OS** — firmware/binary/source-grounded SBOM, exploitability/reachability analysis, VEX, threat/security-design context and continuous audit-ready evidence for connected products and CRA-style obligations.
  - https://finitestate.io/platform
- **Assessoris** — AI-assisted Automotive SPICE and ISO/SAE 21434 audit/assessment workspace, reading project work products and drafting evidence-cited findings.
  - https://assessoris.com/
- **Ketryx for Automotive** — ISO 26262 / ASPICE / UN R155 compliance overlay with automated traceability, safety-case evidence and process enforcement integrated into existing engineering tools.
  - https://www.ketryx.com/industries/automotive
- **Conformly.AI** — multi-agent analysis of ISO 26262, ASPICE and ISO/SAE 21434 work products, including gap findings, remediation plans, safety-case sections and compliance reports.
  - https://www.conformly.ai/
- **Auriga Nexus** — automotive-fenced AI suite spanning requirements, architecture, ISO 26262/ASPICE workflows, TARA/ISO 21434, test automation and traceable evidence across the V-cycle.
  - https://www.auriga-nexus.com/
  - https://www.auriga-nexus.com/products/auriga-shield
- **Siemens Questa One ISO 26262 Functional Safety** — AI-powered end-to-end functional-safety verification workflow covering systematic/random failure analysis, safety metrics and safety-case support.
  - https://www.siemens.com/en-us/products/ic/questa-one/functional-safety/iso-26262/

Existing itemis SECURE, IriusRisk Jeff AI, ThreatModeler Nexus, ModelgraphX, KlugSpice and engineering-ALM products were re-confirmed and not duplicated.

Research prototypes such as AutoTARA were not promoted into the production inventory merely because they demonstrate LLM-assisted TARA; product maturity and a concrete exploitable surface remain required.

Change log:
- 2026-09-28 — safety/cyber domain completed; canonical inventory increased from 189 to 197 solutions.
- 2026-09-28 — website snapshot regenerated from the 197-solution inventory.

## CI / tooling / release-domain audit

Status: **complete (8/8 tasks searched explicitly)**.

New solutions accepted:

- **Docker Gordon** — GA Docker-native AI agent for Dockerfile generation, failed-build/container diagnosis and approved Docker actions in Docker Desktop and `docker ai`.
  - https://docs.docker.com/ai/gordon
- **GitHub Agentic Workflows** — public-preview natural-language automations compiled into hardened GitHub Actions workflows, with Copilot, Claude, Codex or Gemini engines and explicit permissions/safe outputs.
  - https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows
- **Buildkite AI Agents + MCP** — Buildkite agent skills, remote/local MCP tools and agentic pipeline steps for build failure analysis, pipeline maintenance, logs/tests and CI automation.
  - https://buildkite.com/docs/platform/ai-agents
  - https://buildkite.com/docs/apis/mcp-server
- **CircleCI MCP + Agent Skills** — hosted/CLI MCP and reusable skills for failed-build diagnosis, config optimization, test/log analysis and workflow reruns/cancellation.
  - https://circleci.com/docs/guides/toolkit/circleci-mcp-overview/
  - https://circleci.com/docs/guides/toolkit/circleci-agent-skills/

Existing products were also remapped where current first-party capabilities had advanced:
- **GitHub Copilot** now supports CI investigation and GitHub Actions agentic automation.
- **Atlassian Rovo** now drafts Jira release notes natively.
- Embedded-specific agents (Embedder, Hydron, MPLAB AI Coding Assistant, TASKING) were mapped to build/toolchain diagnosis where their toolchain-aware workflows apply.

Change log:
- 2026-09-28 — CI/tooling/release domain completed; inventory increased from 197 to 201 solutions.
- 2026-09-28 — website snapshot regenerated from the 201-solution inventory.

## Documentation-domain audit

Status: **complete (5/5 tasks searched explicitly)**.

This pass found **no net-new mature product** that materially improved the already broad documentation inventory. The useful change was to map current engineering-specific tools that had been added in earlier domains:

- **GitHub Agentic Workflows** → code-documentation maintenance and documentation drift automation.
- **Auriga Nexus / ArchTect / Visual Paradigm AI / Dalus / Softagram / SPREAD Product Explorer** → architecture documentation and architecture-derived artifacts.
- **Embedder / Hydron / MPLAB AI Coding Assistant** → datasheet/reference-manual analysis and vendor-document grounding.
- **fw-context MCP** → connected code context for documentation generation/synchronization.

Important lifecycle correction:
- **Swimm's old continuous-documentation/autosync product** is no longer counted as a current standalone documentation solution. Its 2026 offering has shifted toward agentic modernization services/platform work. This is now recorded in `data/solution-exclusions.json`.

Very small community-only documentation-drift tools were reviewed but not promoted because they did not meet the maturity threshold already applied elsewhere in the inventory.

Change log:
- 2026-09-28 — documentation domain completed; inventory remains at 201 solutions.
- 2026-09-28 — website snapshot regenerated with updated documentation mappings.

## Collaboration-domain audit

Status: **complete (8/8 tasks searched explicitly)**.

New solutions accepted:

- **Loom AI for Meetings + Atlassian workflows** — records Zoom/Meet/Teams, generates summaries/action items, creates Confluence meeting-note pages, turns videos into Jira work items and—with Rovo—suggests ready-to-approve Jira updates from meeting transcripts.
  - https://www.atlassian.com/software/loom/ai-meeting
  - https://support.atlassian.com/loom/docs/use-loom-with-jira-and-confluence
- **Zoom AI Companion / ZoomMate** — meeting summaries/questions/live notes, action items and tasks, workflow automation, Jira actions, and meeting-asset access from ChatGPT/Claude/Slack.
  - https://news.zoom.com/zoom-agentic-ai/
  - https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0080221

Atlassian Rovo's 2026 Jira/Confluence features were revalidated rather than duplicated: native creation/refinement of Jira work items, release notes, AI teammates/agents in Jira, Loom-to-Jira updates, and context-rich Confluence content generation.

Microsoft 365 Copilot remains the native SharePoint-oriented choice already present in the inventory; no separate SharePoint-only product was added without a distinct current solution surface.

Change log:
- 2026-09-28 — collaboration domain completed; canonical inventory increased from 201 to 203 solutions.
- 2026-09-28 — website snapshot regenerated from the 203-solution inventory.
