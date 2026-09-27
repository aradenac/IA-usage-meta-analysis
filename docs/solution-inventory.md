# AI solution inventory — phase 1

Snapshot date: 2026-09-27.

This phase inventories currently exploitable AI solutions for the embedded-software business taxonomy. It deliberately assigns **no MetaScore, ranking, winner or tier**.

## Coverage

The catalog includes coding agents, code-review products, general assistants, deep-research tools, enterprise knowledge/search agents, requirements/ALM AI, cybersecurity and threat-modeling AI, diagram/document/meeting AI, workflow platforms, sovereign/private model backends and self-hosted runtimes.

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

## Next phase

For every task × candidate solution, collect evidence for capability/success, active human intervention, autonomous runtime, service/API price, setup/integration burden, data path/sovereignty and reproducibility. MetaScore is rebuilt only after that evidence phase.
