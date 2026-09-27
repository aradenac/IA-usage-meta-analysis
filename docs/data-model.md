# Data model

The current site remains standalone, but the embedded datasets are mirrored into JSON so future collection can update data independently.

## Main files

- `tasks.json` — business tasks, benchmark-family weights and economic workload priors.
- `task-info.json` — task definitions, inclusions/exclusions, examples, DoD, sector/tool/format/action/confidentiality metadata.
- `task-domains.json` — activity-domain taxonomy.
- `observations.json` — benchmark and field-signal observations.
- `sources.json` — source registry.
- `scaleway-models.json` — current Scaleway-oriented model catalog embedded in the study.
- `harness-matrix.json` — measured/documented model × harness compatibility evidence.
- `surface-info.json` — user-facing harness/API/bridge/runtime/eval-only glossary.
- `model-notes.json` — contextual model descriptions.
- `data-policy.json` — public/internal/client-sensitive data handling categories.

## Next refactor

The next technical step should make `site/index.html` load these JSON files rather than duplicating all data inline, while preserving a build/export that can still produce a single-file offline report.
