# Structured data

These JSON files are the persistent data layer behind the standalone report.

`site/index.html` still embeds the historical scoring datasets, while `site/solution-inventory.js` is generated from the canonical solution inventory and current task mappings so the deployed site can expose the current availability landscape independently from older scored evidence.

## Files

- `tasks.json` — business tasks, economic priors and benchmark-family mappings.
- `task-info.json` — task definitions, examples, exclusions, Definition of Done, tools, formats, sectors and confidentiality.
- `task-domains.json` — business activity domains.
- `observations.json` — normalized benchmark and field observations.
- `sources.json` — source registry.
- `scaleway-models.json` — Scaleway-oriented catalog/pricing metadata captured by the study.
- `harness-matrix.json` — model × harness compatibility/evidence matrix.
- `surface-info.json` — glossary/classification of harnesses, APIs, bridges, runtimes and eval-only runners.
- `model-notes.json` — contextual model descriptions.
- `data-policy.json` — data-sensitivity categories.
- `manifest.json` — dataset counts/status.

## Rule

Evaluation-only scaffolds can inform evidence but must never appear as a user-facing “solution to choose”.


## AI solution inventory

The current availability-only inventory is canonical under:

- `solutions/index.json` — inventory manifest and relationship semantics;
- `solutions/coding.json`;
- `solutions/general-enterprise.json`;
- `solutions/alm-security.json`;
- `solutions/document-diagram-meeting.json`;
- `solutions/backends.json`;
- `solutions/task-refresh-2026-09-27.json` — additions from the explicit 86-task re-audit;
- `task-solution-map/index.json` plus domain mapping files;
- `task-solution-map/all-current.json` — merged current mapping used to generate the site inventory snapshot.

The task-by-task refresh completed on 2026-09-28 contains **210 exploitable AI solution surfaces/platforms/backends** mapped to all **86 business tasks**, with **4,838** current task→solution links. Availability/relevance mapping remains separate from ranking and MetaScore.

`solutions.json` is an earlier monolithic snapshot retained temporarily for compatibility; the split files above are authoritative.
