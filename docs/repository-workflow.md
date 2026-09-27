# Repository workflow

This repository is now the persistent source of truth for the study.

## Current transition state

`site/index.html` is still a standalone single-file application with embedded datasets.

The same datasets are mirrored under `data/`. During the next refactor, the normal development form should load structured JSON, while a build/export step may continue to produce a standalone HTML snapshot.

## Evidence additions

When adding evidence:

1. preserve the original source URL and date;
2. record exact model, surface/harness and configuration;
3. record benchmark/task/protocol/version/sample size;
4. preserve raw score/cost/runtime before interpretation;
5. record task relevance and evidence grade;
6. document caveats and transfer assumptions;
7. never turn an eval-only scaffold into a user-facing recommendation.

## Internal benchmarks

Internal tests should be stored under `evidence/internal-tests/` with enough metadata to recompute:

- P(success)
- API/service cost per attempt
- active human time
- autonomous wall-clock
- intervention count/type

while respecting company/client data classification.
