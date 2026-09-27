# MetaScore

## Goal

The MetaScore answers:

> **For this task T, is this AI configuration economically more attractive than doing the task without AI, and by how much?**

It is computed independently for every configuration × task.

## Variables

- **P(success)** — estimated probability that one attempt meets the task Definition of Done.
- **C_API** — variable model/API/service cost per attempt.
- **T_human,AI** — active human minutes per attempt: prompting, guidance, answering agent questions, necessary monitoring, review, normal corrections/relaunches.
- **R_human** — reference human cost, currently 50 €/h.
- **C_human** — estimated cost of doing the task without AI.

Initial installation/setup and autonomous agent wall-clock are excluded from human active time.

## Equations

```text
C_attempt = C_API + (T_human,AI / 60) × R_human
C_success_AI = C_attempt / P(success)

MetaScore = 100 × C_human / (C_human + C_success_AI)
```

## Interpretation

- 0 — configuration cannot perform the task
- < 50 — human is economically preferable
- 50 — break-even
- > 50 — AI is economically preferable
- ≈ 67 — AI costs about half as much
- 80 — AI costs about one quarter as much
- 90 — AI costs about one ninth as much

Evidence quality, simplicity, autonomy and wall-clock are **not** separate MetaScore weights.
