# Structured data

These JSON files mirror the datasets currently embedded in `site/index.html`.

The HTML remains the executable standalone snapshot. The JSON layer is now the persistent source for future evidence collection and will progressively become the authoritative input to the site.

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
- `task-solution-map/index.json` plus domain mapping files.

The inventory currently contains **86 exploitable AI solution surfaces/platforms/backends** mapped to all **86 business tasks**. This phase contains no ranking or MetaScore.

`solutions.json` is an earlier monolithic snapshot retained temporarily for compatibility; the split files above are authoritative.
