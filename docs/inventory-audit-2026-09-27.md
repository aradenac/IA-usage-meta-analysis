# Extended solution inventory audit — 2026-09-27

## Result

The earlier 128-solution freeze was too early. Two additional gap-directed passes found several material families that matter directly to embedded-software engineering. Those gaps are now integrated.

Current state:

- 157 unique solution/product/backend entries;
- all 86 business tasks mapped;
- 4,340 unique task → candidate links;
- 35–70 unique candidates per task (50.5 average);
- 0 invalid solution references;
- 0 discontinued/legacy products in active task mappings;
- 0 evaluation-only scaffolds in active task mappings;
- 138 exact historical observed model + harness/surface + configuration combinations preserved;
- 42 additional historical compatibility-only combinations preserved;
- 15 specialist provider API configurations preserved.

## What the extra passes changed

The most important correction is methodological: specialized engineering products must not be collapsed into the same category as generic LLM harnesses.

Several products now expose deterministic engineering context to AI agents:

- Perforce Klocwork 2026.2 exposes static-analysis defects and remediation guidance through MCP.
- Black Duck Coverity 2026 adds an MCP scan surface and AI-assisted triage.
- itemis ANALYZE exposes the engineering traceability graph through MCP and combines AI reasoning with deterministic trace/compliance checks.
- itemis SECURE applies AI to TARA, attack trees, vulnerability impact and governed cybersecurity artifacts.
- Kernaro Assist operates directly on live Sparx Enterprise Architect models.
- Vector CANoe 20 SP2 exposes agents/skills/MCP for SIL/HIL workflows, including requirement → CAPL test → execute → analyze → correct → rerun.
- tracetronic ecu.test agent generates test steps from test-workspace context and supports early trace-analysis workflows.

These are distinct solution classes because the LLM is grounded in structured engineering state that a generic code/chat harness does not possess by default.

## Additional current products added

The extended passes also added:

- Tabby for self-hosted coding assistance;
- Bito for GitLab/GitLab Self-Managed code review;
- Warp as an agentic terminal/development environment;
- Fern, ReadMe, Redocly and Document360 for AI-native technical documentation/search;
- Notion AI Meeting Notes, Google Meet Gemini notes and Granola Enterprise for meeting capture;
- Guru for permission-aware enterprise knowledge search;
- Make AI Agents, Zapier Agents, Workato AIRO/GO and Tines AI Agent for enterprise workflow orchestration;
- Elastic Agent Builder, Sentry Seer, Datadog Bits, New Relic Autopilot, Grafana AI and Dynatrace Assist for telemetry-grounded investigation;
- Harness AI / Autonomous Worker Agents for governed AI in software-delivery pipelines.

## Existing important embedded-specific products retained

Earlier passes remain intact, notably:

- VectorCAST 2026 / Reqs2x for AI-assisted requirements-to-code mapping and executable requirement-based tests;
- Parasoft C/C++test 2026.1 MCP workflows for static-analysis remediation, tests, MC/DC coverage and coding rules;
- Kapa.ai / Zephyr's Kapa surface for source/docs/issues/PR-grounded technical retrieval;
- QRA QVscribe/ReqWriter, KlugSpice, ReqDrive, Reqi and Modern Requirements for requirements/process workflows;
- dedicated GitLab review choices such as Cursor Bugbot, CodeAnt, Kodus/Kody, DeepSource and community PR-Agent.

## Lifecycle cleanup

- Continue is retained only as historical metadata after joining Cursor, and is removed from active mappings.
- Roo Code remains excluded because it shut down in 2026.
- Flowise is recorded as sunsetting rather than a long-term new-deployment candidate.
- Benchmark/evaluation scaffolds remain evidence only.

## Historical evidence preservation

Existing observations were not rewritten into product-marketing categories. Every previously collected model × harness/surface × configuration record remains preserved in `data/configurations/`.

A benchmark row using an evaluation scaffold can still inform a model estimate, but the scaffold itself cannot appear as “what should I use?” in a user-facing recommendation.

The three configuration inventories remain separate:

1. 138 actually observed historical configurations;
2. 42 compatibility-only historical combinations;
3. 15 specialist provider/API configurations.

This separation prevents availability evidence from being mistaken for measured performance evidence.

## Updated freeze criterion

After adding the missing embedded static-analysis, engineering-graph/TARA, architecture-modeling, HIL/SIL, observability and AI-DevOps families, further broad searches increasingly return alternatives inside already represented families rather than a missing task class.

That is the appropriate stopping condition for phase 1. It is not a claim that every niche vendor in the market has been enumerated. New products can still be appended without changing the data model.

The next high-value phase is evidence collection: preserve each benchmark/observation separately, document task comparability, then aggregate only with explicit relevance, evidence-quality and uncertainty weights.
