# Enterprise pricing audit — 2026-09-27

## Coverage

Pricing has now been modeled for **all 157 solution entries** in the availability inventory.

Current evidence state:

- 90 solutions have at least one current public monetary price captured;
- 30 are classified as **public exact** for the represented purchase path;
- 41 are **public partial**: at least one rate is public but Enterprise, overage, region, model or negotiated terms remain variable;
- 67 are **contact-sales** solutions with no usable public enterprise amount captured;
- 18 have an explicit zero software-license/open-source path with external inference/compute cost;
- 1 legacy/transition record is retained for historical continuity;
- every contact-sales / estimate-only record has a low-confidence sensitivity range;
- every record has a cost function, source, inference-cost treatment and confidence assessment.

There are no remaining unclassified pricing records.

## Important distinction: price evidence versus cost estimate

The catalog never writes an estimate into a vendor-price field.

For sales-led products, the record keeps:

1. the observed commercial model (seat, organization contract, term/perpetual license, usage, etc.);
2. `public_price: false`;
3. a broad low/typical/high `estimated_enterprise_cost`;
4. low monetary confidence;
5. an explicit note that the estimate is not a vendor quote.

This lets later ROI analysis include the product without manufacturing false pricing precision.

## Confidence

Confidence is deliberately two-dimensional:

- **pricing-model confidence**: how sure we are about the billing mechanism;
- **monetary confidence**: how sure we are about the actual monetary amount.

A quote-only product can therefore have a relatively high model confidence but low monetary confidence.

Evidence grades currently distribute as:

- A: 81
- B: 18
- C: 58

The old grade-E fallback bucket has been eliminated by the final targeted pass: each previously weak record now has at least a concrete official commercial model or stronger source.

## Cost functions represented

The catalog supports, among others:

- seat/user subscriptions;
- active-contributor subscriptions;
- organization/workspace/project subscriptions;
- token PAYG;
- pooled AI credits;
- per-agent/per-workflow execution;
- per-page document processing;
- per-query/search charging;
- GPU/compute-hour charging;
- open-source software + external inference/operations;
- fixed access + metered overage;
- custom enterprise contracts;
- specialist engineering term/perpetual licenses.

This is necessary because headline monthly prices are not economically comparable across these products.

## Anti-double-counting

The catalog includes **17 commercial bundle/prerequisite groups**.

Examples:

- ChatGPT Business/Enterprise and Codex can share one OpenAI seat entitlement;
- Microsoft 365 Copilot, Researcher and Teams Copilot capabilities can share one seat;
- Google Workspace Gemini, NotebookLM and Google Meet AI notes can be part of one Workspace entitlement;
- Junie and JetBrains AI Assistant use the same JetBrains AI subscription/credits;
- Mistral Vibe Code and Vibe Work can share one Mistral Team/Enterprise entitlement;
- Rovo can have zero incremental license cost on an eligible Atlassian subscription;
- open-source coding harnesses must add model/API or self-hosted compute rather than being treated as truly zero-TCO.

These rules will prevent the future MetaScore/TCO engine from summing overlapping products as if each required an independent subscription.

## Important public-pricing examples

The catalog captures current enterprise-usable cost functions such as:

- Cursor Teams: seat subscription plus on-demand usage;
- GitHub Copilot Business/Enterprise: seat + pooled AI credits + $0.01 overage credit;
- Kiro: seat tier + $0.04 extra credits;
- Augment: flat workspace fee for up to 50 seats + LLM/context/compute usage;
- ChatGPT Business: Standard/Premium seat options with Enterprise/flexible-credit alternatives;
- n8n: workspace/execution tiers rather than per-step or per-user billing;
- Copilot Studio: prepaid or PAYG Copilot Credits;
- Kilo Code and Kodus: platform fee separated from model-provider inference;
- Scaleway: token-priced serverless inference versus GPU-hour dedicated deployment;
- Sentry Seer: active-contributor add-on;
- Grafana Assistant: active AI user + token overage;
- Elastic Agent Builder: execution + optional managed-LLM token usage;
- Modern Requirements Copilot4DevOps: public add-on tiers with 2M/30M/100M-token allowances; base Modern Requirements licensing remains a prerequisite.

## Next use in the MetaScore

Do **not** convert this catalog directly into one universal “price score.”

The next calculation layer should evaluate total cost for declared company scenarios, for example:

- 10 / 50 / 200 engineers;
- light / normal / intensive AI usage;
- percentage of active versus licensed users;
- shared pools versus individual quotas;
- SaaS versus BYOK/private hosting;
- existing prerequisite licenses already owned by the company;
- negotiated-price uncertainty.

For quote-only solutions, cost uncertainty should propagate into ROI uncertainty rather than disappear behind a point estimate.

