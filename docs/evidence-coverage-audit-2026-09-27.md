# Evidence coverage audit — 2026-09-27

## Snapshot

The meta-analysis currently preserves **286 evidence records** in four deliberately separate layers:

- 200 historical exact model × harness/surface × configuration observations;
- 70 direct product benchmark / field / case-study / capability observations;
- 10 cross-product family benchmarks used only to update priors;
- 6 practitioner/user signals kept as weak E-grade context.

The current `product-task-v1.2` scorer evaluates **4389 solution × task pairs** across all 86 business tasks.

## Current empirical coverage

- 69/86 tasks have at least one direct product evidence row.
- 59/86 tasks have at least one candidate whose P(success) is no longer primarily prior-driven.
- 24/86 tasks benefit from at least one cross-product family benchmark.
- 4154 of 4389 candidate pairs still have prior-driven P(success). This is visible, not hidden.

Global MetaScore confidence remains intentionally conservative:

- C: 11 pairs;
- D: 703 pairs;
- E: 3,675 pairs.

No product pair is promoted to global A/B confidence merely because one benchmark is strong. Success, active-human time and monetary cost must all be sufficiently grounded.

## Better-covered zones

The strongest public evidence currently clusters around:

- **Faire une revue de Merge Request GitLab** (`verify-mr`): 13 empirically supported success candidates, 14 candidates with direct product evidence.
- **Investiguer un bug intermittent / difficile à reproduire** (`debug-intermittent`): 10 empirically supported success candidates, 5 candidates with direct product evidence.
- **Refactorer du code embarqué sans changer le comportement** (`dev-refactor`): 6 empirically supported success candidates, 10 candidates with direct product evidence.
- **Produire / vérifier du code sous coding rules (MISRA, CERT, AUTOSAR, règles client)** (`verify-coding-rules`): 3 empirically supported success candidates, 16 candidates with direct product evidence.
- **Diagnostiquer performance, mémoire ou contraintes temps réel** (`debug-performance`): 9 empirically supported success candidates, 3 candidates with direct product evidence.
- **Relire une conception / implémentation sous l’angle cybersécurité** (`cyber-review`): 3 empirically supported success candidates, 14 candidates with direct product evidence.
- **Automatiser une tâche d’ingénierie en Python / shell** (`ci-automation`): 7 empirically supported success candidates, 6 candidates with direct product evidence.
- **Analyser un crash, fault, watchdog ou coredump** (`debug-crash`): 8 empirically supported success candidates, 3 candidates with direct product evidence.
- **Transformer une réunion en compte rendu technique exploitable** (`collab-meeting`): 6 empirically supported success candidates, 6 candidates with direct product evidence.
- **Diagnostiquer puis corriger un bug embarqué** (`debug-embedded`): 7 empirically supported success candidates, 2 candidates with direct product evidence.
- **Diagnostiquer et corriger un build cassé** (`ci-build`): 8 empirically supported success candidates, 0 candidates with direct product evidence.
- **Diagnostiquer et corriger une CI GitLab / runner Docker** (`ci-gitlab`): 8 empirically supported success candidates, 0 candidates with direct product evidence.
- **Diagnostiquer un problème d’interface hardware / software** (`debug-hw-sw`): 6 empirically supported success candidates, 2 candidates with direct product evidence.
- **Backporter un correctif upstream vers notre version** (`upstream-backport`): 6 empirically supported success candidates, 2 candidates with direct product evidence.
- **Créer un correctif dans un grand projet upstream (Zephyr/Linux/SDK)** (`upstream-contribute`): 6 empirically supported success candidates, 2 candidates with direct product evidence.

This reflects where public, comparable evaluation ecosystems actually exist: coding agents, code review, deep research, meeting intelligence, observability/debugging and some workflow/testing tasks.

## Tasks without direct product evidence

The following 17 tasks still lack a direct product observation even though candidate solutions are mapped:

- `dev-driver-datasheet` — Implémenter un driver absent à partir de la datasheet (55 candidates)
- `upstream-search` — Chercher un problème connu / fix upstream (35 candidates)
- `verify-prevalidation` — Préparer le software avant passage à l’équipe de validation (63 candidates)
- `cyber-vuln` — Analyser une vulnérabilité / CVE et son applicabilité produit (45 candidates)
- `safety-impact` — Analyser l’impact safety d’un changement software (47 candidates)
- `ci-build` — Diagnostiquer et corriger un build cassé (47 candidates)
- `ci-gitlab` — Diagnostiquer et corriger une CI GitLab / runner Docker (48 candidates)
- `ci-create` — Créer ou modifier une pipeline GitLab CI (47 candidates)
- `ci-docker` — Créer / maintenir un environnement Docker de build et test (44 candidates)
- `ci-toolchain` — Diagnostiquer SDK, dépendances ou toolchain de développement (44 candidates)
- `release-prepare` — Préparer une release software / firmware (37 candidates)
- `doc-datasheet` — Analyser une datasheet / reference manual / errata (49 candidates)
- `doc-vendor-diff` — Comparer versions de documentation / SDK fournisseur (44 candidates)
- `learn-operational` — Devenir opérationnel sur une technologie nouvelle (53 candidates)
- `learn-path` — Construire un parcours de formation technique personnalisé (44 candidates)
- `learn-coach` — Se faire coacher / interroger pour consolider une compétence (44 candidates)
- `research-version` — Analyser les nouveautés d’une version et leur impact pour nous (52 candidates)

These are priority targets for additional public research and/or internal benchmarking.

## Tasks without empirical success evidence

The following 27 tasks currently have no candidate with sufficiently close probability-like empirical evidence:

- `req-system-impact` — Analyser une exigence système et en déduire les impacts software; direct evidence rows for 1 candidate(s), family-prior coverage for 52.
- `req-write-sw` — Rédiger ou améliorer des exigences software; direct evidence rows for 1 candidate(s), family-prior coverage for 51.
- `req-review` — Relire et challenger des exigences; direct evidence rows for 1 candidate(s), family-prior coverage for 52.
- `req-decompose` — Décomposer les exigences système vers le software / composants; direct evidence rows for 2 candidate(s), family-prior coverage for 52.
- `req-traceability` — Vérifier la traçabilité exigences → design → code → tests; direct evidence rows for 3 candidate(s), family-prior coverage for 52.
- `req-change-impact` — Analyser l’impact d’un changement d’exigence; direct evidence rows for 1 candidate(s), family-prior coverage for 54.
- `upstream-search` — Chercher un problème connu / fix upstream; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `cyber-impact` — Analyser les impacts cybersécurité d’une fonctionnalité / changement; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `cyber-vuln` — Analyser une vulnérabilité / CVE et son applicabilité produit; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `cyber-threat` — Faire une analyse de menaces ciblée / abuse cases; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `safety-impact` — Analyser l’impact safety d’un changement software; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `process-aspice` — Vérifier la conformité d’un travail au process ASPICE / cycle en V; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `process-evidence` — Préparer les preuves pour une revue / audit / gate; direct evidence rows for 3 candidate(s), family-prior coverage for 50.
- `release-prepare` — Préparer une release software / firmware; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `release-notes` — Produire des release notes depuis GitLab / Jira / commits; direct evidence rows for 4 candidate(s), family-prior coverage for 40.
- `doc-datasheet` — Analyser une datasheet / reference manual / errata; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `doc-vendor-diff` — Comparer versions de documentation / SDK fournisseur; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `learn-explain` — Comprendre rapidement une technologie inconnue; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `learn-operational` — Devenir opérationnel sur une technologie nouvelle; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `research-docs` — Analyser et synthétiser une grosse documentation technique; direct evidence rows for 4 candidate(s), family-prior coverage for 0.
- `research-multidoc` — Répondre à une question à partir de plusieurs documents / sources internes; direct evidence rows for 4 candidate(s), family-prior coverage for 0.
- `learn-path` — Construire un parcours de formation technique personnalisé; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `learn-coach` — Se faire coacher / interroger pour consolider une compétence; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `research-version` — Analyser les nouveautés d’une version et leur impact pour nous; direct evidence rows for 0 candidate(s), family-prior coverage for 0.
- `arch-diagram` — Créer / mettre à jour des diagrammes techniques assistés par IA; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `cyber-compliance` — Vérifier la conformité cyber d’un design / produit par rapport au référentiel applicable; direct evidence rows for 1 candidate(s), family-prior coverage for 0.
- `cyber-artifacts` — Produire / maintenir les artefacts cybersécurité projet; direct evidence rows for 1 candidate(s), family-prior coverage for 0.

Some of these tasks already have useful time-saving/capability evidence. That does not justify fabricating a success rate.

## Evidence gaps that public research is unlikely to close fully

Several embedded/regulatory activities have little or no independent public benchmark ecosystem:

- ASPICE compliance/evidence preparation;
- software-safety impact analysis;
- product-specific CVE applicability;
- customer/vendor document-diff analysis;
- release readiness under a company's own gates;
- hardware/software debugging on proprietary boards;
- detailed architecture work against confidential product constraints.

For those tasks, the highest-value next evidence source will eventually be a small internal benchmark suite using real sanitized artifacts and explicit Definition-of-Done checks.

## Interpretation rule

A high point MetaScore with D/E global confidence means:

> economically promising under current assumptions, but not yet proven.

It must not be interpreted as a recommendation supported by strong evidence.

The companion field `top_with_direct_or_success_evidence` in `data/task-scores/index.json` should be preferred over the unrestricted point-estimate ordering when making decisions before internal validation.
