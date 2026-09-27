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
| Requirements | 6 | pending | |
| Architecture | 6 | pending | includes diagram task |
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
