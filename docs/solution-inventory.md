# AI solution inventory — phase 1

Snapshot date: 2026-09-27.

This phase inventories currently exploitable AI solutions for the embedded-software business taxonomy. It deliberately assigns **no MetaScore, ranking, winner or tier**.

## Coverage

The catalog now includes generic coding agents and IDEs, GitLab review products, embedded static-analysis/MCP tools, requirements/ALM AI, ASPICE/traceability agents, architecture-modeling AI, TARA/cybersecurity AI, HIL/SIL test agents, document/diagram/meeting AI, telemetry-grounded debugging agents, AI DevOps/workflow platforms, enterprise knowledge/search, sovereign/private model backends and self-hosted runtimes.

The canonical catalog is split under `data/solutions/`; `data/solutions/index.json` gives counts and relationship semantics.

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

## Next phase

For every task × candidate solution, collect evidence for capability/success, active human intervention, autonomous runtime, service/API price, setup/integration burden, data path/sovereignty and reproducibility.

Each observation/source remains separate. Comparable observations may then be aggregated with explicit weighting for task relevance, evidence quality and uncertainty. MetaScore is rebuilt only after that evidence phase.
