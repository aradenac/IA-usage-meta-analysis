# Evidence grading

Evidence quality is deliberately separate from economic value.

## Grades

- **A** — direct, primary, reproducible measurement with strong protocol transparency.
- **B** — close empirical measurement with minor transfer or protocol limitations.
- **C** — empirical proxy transferred from a similar context/task.
- **D** — derived estimate or significant transfer with large uncertainty.
- **E** — weak signal: anecdote, small community bake-off, practitioner report, or fallback prior.

## Effective task grade

A source can be high quality in itself but weak for a particular business task if semantic relevance is poor.

The current engine therefore distinguishes:

- source grade;
- task relevance;
- effective confidence.

A benchmark that measures isolated algorithmic coding must not directly create a high success estimate for a long repo-level engineering activity merely because the raw score is high.

## Weak signals

Weak evidence is kept rather than cherry-picked away. Positive and negative field signals should both be preserved with their context and biases.

Confidence does **not** multiply or reduce the MetaScore. Read results as, for example:

- MetaScore 85 / confidence B → attractive and reasonably supported.
- MetaScore 85 / confidence E → potentially attractive; high priority for internal benchmarking.
