# AI solution inventory — phase 1

Baseline snapshot: 2026-09-27. Explicit task-by-task refresh completed: 2026-09-28.

This phase inventories currently exploitable AI solutions for the embedded-software business taxonomy. It deliberately assigns **no MetaScore, ranking, winner or tier**.

## Coverage

The catalog now includes generic coding agents and IDEs, GitLab review products, embedded static-analysis/MCP tools, requirements/ALM AI, ASPICE/traceability agents, architecture-modeling AI, TARA/cybersecurity AI, HIL/SIL test agents, document/diagram/meeting AI, telemetry-grounded debugging agents, AI DevOps/workflow platforms, enterprise knowledge/search, sovereign/private model backends and self-hosted runtimes.

The canonical catalog is split under `data/solutions/`; `data/solutions/index.json` gives counts and relationship semantics.

After the explicit re-audit of every business task, the current catalog contains **210 unique solution/product/backend entries** and **4,838 current task→solution links** across all **86 tasks**. The refresh added 53 current entries beyond the 157-solution pre-audit baseline.

## Task relationship labels

- **native**: first-class workflow for the task.
- **direct**: usable directly in the normal product interface.
- **connected**: requires a supported connector, MCP server or integration.
- **custom_workflow**: requires orchestration, scripting or a custom agent.
- **backend**: model/API/runtime substrate rather than a turnkey user experience.

These labels describe exploitability, not performance.

## Boundaries

Evaluation-only benchmark scaffolds remain evidence sources but are never daily-use solution candidates.

Reqtify, OpenFastTrace, GitLab, Jira, Confluence, SharePoint, PlantUML, Mermaid and Draw.io are engineering tools or data surfaces. They become part of an AI solution only through native features, files, APIs, connectors, MCP or custom workflows.

Backends are separate from front ends. A private model deployment can be paired with a coding harness, Open WebUI, an orchestration platform or a company-specific workflow.

Specialized engineering tools are also kept distinct from generic harnesses. A solution such as Klocwork, Coverity, itemis ANALYZE/SECURE, CANoe or ecu.test may expose deterministic defects, traceability graphs, risk models or test-bench state to an LLM. That context is part of the solution and must be represented when evidence is later compared.

## Historical configuration preservation

The solution inventory does not replace the historical model × harness × configuration dataset.

The configuration catalog keeps:

- 138 observed historical configurations;
- 42 compatibility-only historical combinations;
- 15 specialist provider/API configurations.

Historical/evaluation-only rows remain available as evidence even when their execution surface is not a recommendation candidate.

## Task-by-task refresh

The availability inventory has now been re-audited explicitly for all 86 tasks. The durable research log is `docs/task-solution-refresh-2026-09-27.md`; newly accepted entries live in `data/solutions/task-refresh-2026-09-27.json`, and their task mappings are merged into `data/task-solution-map/all-current.json`.

The deployed standalone site consumes a generated snapshot of those canonical files through `site/solution-inventory.js`.

## Next phase

The 53 newly added solution entries are availability/relevance additions only; they have not been retroactively assigned performance or economic scores. For every task × candidate solution, collect evidence for capability/success, active human intervention, autonomous runtime, service/API price, setup/integration burden, data path/sovereignty and reproducibility.

Each observation/source remains separate. Comparable observations may then be aggregated with explicit weighting for task relevance, evidence quality and uncertainty. MetaScore is rebuilt only after that evidence phase.
