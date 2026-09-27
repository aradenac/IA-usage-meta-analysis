# Second-pass solution inventory audit — 2026-09-27

## Result

The availability inventory is considered **sufficiently broad to freeze phase 1** and move to evidence collection.

Current state:

- 128 unique solution/product/backend entries;
- all 86 business tasks mapped;
- 33–68 unique candidates per task (48.3 average);
- 0 invalid solution references;
- 0 discontinued/legacy products in active task mappings;
- 0 evaluation-only scaffolds in active task mappings;
- 138 exact historical observed model + harness/surface + configuration combinations preserved;
- 42 additional historical compatibility-only combinations preserved;
- 15 specialist provider API configurations preserved.

## Second-pass additions

The audit specifically filled gaps in:

- modern coding agents and IDEs;
- GitLab merge-request AI review, including self-hostable choices;
- embedded C/C++ verification and safety-critical testing;
- requirements engineering and Automotive SPICE;
- enterprise search and internal knowledge;
- sovereign/private AI deployment;
- technical-document retrieval and documentation platforms;
- scientific/technical research;
- PDF/document intelligence;
- diagram generation;
- meeting transcription/recap;
- cybersecurity remediation and threat modeling;
- agent/workflow orchestration.

## Important embedded-specific additions

- VectorCAST 2026 / Reqs2x for AI-assisted requirements-to-code mapping and executable requirement-based tests.
- Parasoft C/C++test 2026.1 MCP workflows for C/C++ static analysis remediation, tests, MC/DC coverage and coding-rule workflows.
- Kapa.ai as a technical-knowledge retrieval layer. The Zephyr Project itself exposes a Kapa assistant and MCP endpoint grounded in Zephyr documentation, source code, issues and pull requests.
- Dedicated GitLab review choices such as Cursor Bugbot, CodeAnt, Kodus/Kody, DeepSource and community PR-Agent.
- QRA QVscribe/ReqWriter, KlugSpice, ReqDrive, Reqi and Modern Requirements for requirements/process workflows.

## Lifecycle cleanup

- Continue is retained only as historical metadata after joining Cursor, and is removed from active mappings.
- Roo Code remains excluded because it shut down in 2026.
- Flowise is recorded as sunsetting rather than a long-term new-deployment candidate.
- Benchmark/evaluation scaffolds remain evidence only.

## Historical evidence preservation

Existing observations were not rewritten into product marketing categories. They are preserved exactly in `data/configurations/`.

A benchmark row using an evaluation scaffold can still inform a model estimate, but the scaffold itself cannot appear as “what should I use?” in a user-facing recommendation.

## Freeze criterion

The final broad searches across coding, GitLab review, requirements/ASPICE, safety/security, embedded verification, enterprise knowledge, documentation, research, meetings and sovereign deployment primarily surfaced products that fit already represented families rather than revealing a missing major family.

This does **not** mean every niche vendor in the market has been enumerated. It means the inventory is broad enough for the next evidence phase: adding another marginal product is now less valuable than measuring and filtering the existing candidates.

New products can still be appended later without changing the data model.
