# Methodology

## Unit of analysis

The target unit is:

**AI solution/configuration × engineering task T**

A solution can be a model + coding harness, an API/service, or a general-purpose AI application with tools.

## Evidence

Each observation keeps, where available:

- benchmark and version/protocol;
- task/evidence family;
- model, harness/surface and configuration;
- raw score and score semantics;
- cost and runtime;
- sample size;
- source and effective evidence grades;
- task relevance;
- notes and comparability caveats.

Evaluation-only scaffolds/runners are valid **evidence sources** but must not appear as user-facing recommendations.

## Reliability

Reliability is orthogonal to economic value:

- A — direct/reproducible primary measurement
- B — close empirical measurement
- C — empirical proxy transferred from a similar context
- D — derived/transferred estimate with large uncertainty
- E — weak/anecdotal signal

A high MetaScore with confidence E means “potentially very profitable, high priority to benchmark”, not “proven”.

## Business-task taxonomy

The visible taxonomy is tailored to embedded-software work. It includes sector applicability, tools/platforms, formats/artifacts, actions expected from AI, technology/process context and typical data sensitivity.

The upstream/system-engineering profession itself is out of scope; system/customer documents are inputs to software activities.
