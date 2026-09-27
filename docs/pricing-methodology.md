# Enterprise pricing methodology

Snapshot date: 2026-09-27.

Pricing is stored independently from capability/performance evidence. The goal is to preserve the commercial **cost function** of each solution so that later ROI/MetaScore calculations can model realistic company scenarios instead of comparing unlike headline prices.

## Principles

1. Prefer current official vendor pricing/documentation.
2. Never replace an unpublished enterprise price with an invented vendor price.
3. `public_price = null` means exactly that: no public monetary amount was found for that commercial offer.
4. If a useful monetary approximation is needed for later sensitivity analysis, keep it in `estimated_enterprise_cost`, never in `plans`.
5. Keep fixed access cost separate from variable usage cost.
6. Explicitly state whether inference/model cost is included, partially included, BYOK/external, or not applicable.
7. Preserve the billing unit: seat, active contributor, organization/workspace, token, credit, page, query, execution, compute hour, GPU hour, etc.
8. Prices are stored before taxes/VAT unless the source explicitly says otherwise.
9. Enterprise contracts may be negotiated below list price; list price is therefore a reproducible baseline, not necessarily the expected procurement price.
10. Hardware, implementation services and prerequisite software subscriptions are excluded unless explicitly stated.

## Pricing evidence classes

### A — current official exact price

Score: 0.95–1.00.

Current official source publishes monetary amounts and billing units applicable to the product or an enterprise-usable plan.

### B — current official partial price

Score: 0.80–0.94.

Official source defines the pricing mechanics and some monetary rates, but an enterprise tier, add-on, region or negotiated element remains unpublished.

### C — official commercial model, no public amount

Score: 0.60–0.79 for the pricing model itself.

Official source confirms the licensing/usage structure (for example per-user, per-project, custom enterprise, credits, BYOK) but does not publish a usable monetary amount.

The monetary-estimate confidence is normally much lower than the model confidence.

### D — market-anchored estimate

Score: 0.35–0.59.

No current public price. Estimate is anchored to public prices of comparable products in the same category and/or older vendor evidence.

### E — coarse sensitivity estimate

Score: 0.15–0.34.

Only a wide range can be justified. Such values must not directly drive a ranking; they are intended for sensitivity analysis.

## Separate confidence dimensions

Every record has:

- `pricing_model_confidence`: confidence that the billing mechanism is represented correctly;
- `monetary_confidence`: confidence in the monetary amounts used for ROI calculations;
- `grade`: evidence grade for the strongest current pricing evidence.

A quote-only solution may therefore have a high pricing-model confidence and a low monetary confidence.

## Commercial-model vocabulary

Common values include:

- `open_source`
- `seat_subscription`
- `active_contributor_subscription`
- `workspace_subscription`
- `organization_subscription`
- `project_subscription`
- `usage_based`
- `token_usage`
- `credit_usage`
- `execution_usage`
- `page_usage`
- `query_usage`
- `compute_usage`
- `gpu_hour`
- `custom_contract`
- `perpetual_or_term_license`
- `hybrid_fixed_plus_usage`

A solution can use several at once.

## Inference-cost vocabulary

- `included`: hosted-model cost is included in the plan within stated limits;
- `included_quota_plus_overage`: included allowance, then metered overage;
- `vendor_usage`: model cost is metered by the product/vendor;
- `byok_external`: platform charge and model-provider charge are separate;
- `mixed`: several modes exist;
- `self_host_compute`: software may be free but compute/operations are external;
- `not_applicable`: product does not expose a separable model-cost component;
- `unknown`.

## Estimates

For quote-only products, `estimated_enterprise_cost` is deliberately broad. It includes:

- low / typical / high;
- currency;
- billing unit and period;
- basis text;
- whether the estimate is comparable to a seat price, a team/workspace price, or an organization/platform contract.

These estimates are **not vendor prices**.

Category bands are used only when no better evidence exists. They are meant to support later Monte Carlo/sensitivity calculations and must carry low monetary confidence.

## Future ROI normalization

The dataset is designed to support scenarios such as:

- 10, 50, 200 or more engineers;
- light / normal / intensive AI usage;
- fixed-seat versus active-contributor billing;
- included usage versus overage;
- BYOK versus bundled inference;
- SaaS versus self-hosted/private deployment;
- negotiated enterprise discount ranges.

The future MetaScore should use expected total cost under a declared scenario, not the cheapest advertised entry plan.


## Reference scoring normalization currently used

The pricing catalog stores the vendor's commercial function. The current `product-task-v1.2` scorer then needs one reproducible reference scenario in order to allocate a fixed subscription to a task.

This normalization is a **scenario assumption**, not an accounting rule and not a claim about the contract a company would actually sign.

### Reference organization

Current point scenario:

- 50 users / engineers;
- 80 AI-eligible engineering hours per licensed user per month;
- low-cost sensitivity: 120 AI-eligible hours/month;
- high-cost sensitivity: 40 AI-eligible hours/month.

For a task whose human-only reference duration is `H` hours:

`allocated fixed license cost = normalized monthly per-user cost / 80 × H`

Sensitivity bounds use 120 h/month for the low allocated cost and 40 h/month for the high allocated cost.

This allocation prevents a 20 €/month seat from being treated as either “free” or as a full 20 € charge on every task.

### Reference plan selection

When several current public non-metered plans exist, the current baseline scorer selects an enterprise-usable public purchase path in this preference order:

1. Enterprise when an exact public amount exists;
2. Business;
3. Team / Teams;
4. Standard;
5. Pro;
6. Premium / Core / Max / Starter;
7. free/open-source only when no paid enterprise-usable public plan is applicable.

A custom Enterprise row with no published amount does not erase a lower public Business/Team price. The public plan remains a reproducible baseline, while the custom contract remains represented separately as an uncertainty.

Organization/workspace/team/site subscriptions are divided by the 50-user reference organization. Project subscriptions are divided by 10 reference users/project in the current point scenario.

This rule is intentionally simple. A later scenario optimizer should select the economically valid tier from team size, included quotas, minimum seats and negotiated terms rather than using this baseline heuristic.

## Quote-only sensitivity bands

When no usable vendor amount exists, the following coarse ranges were used as **initial sensitivity priors only**. Individual records may use a more specific range where better evidence exists.

| Category | Low | Typical | High | Unit |
| --- | ---: | ---: | ---: | --- |
| Sovereign/private AI platform | $100k | $500k | $2m | organization/year |
| Specialist HIL/SIL engineering tool | $5k | $15k | $50k | engineering seat/year |
| Embedded static analysis / verification | $1k | $3k | $8k | engineering seat/year |
| Requirements / ALM / compliance platform | $25k | $100k | $300k | organization/year |
| AppSec/security AI | $25 | $80 | $200 | contributing developer/month |
| Enterprise knowledge/workflow/observability/DevOps platform | $25k | $100k | $300k | organization/year |
| Documentation/meeting/research SaaS | $15 | $40 | $100 | user/month |
| Architecture/modeling add-on | $1k | $3k | $10k | engineering seat/year |
| General developer AI tooling | $20 | $60 | $150 | user/month |

These values are never written into vendor `plans`; they live only in `estimated_enterprise_cost` with low monetary confidence.

## Variable inference and BYOK

For products with published token/page/compute rates, task cost uses the published unit price and the task workload model.

For BYOK or self-hosted products:

1. prefer an empirical API cost measured for the same harness on relevant historical observations;
2. otherwise use the current generic sensitivity proxy of **$2/M input tokens + $10/M output tokens**;
3. widen that external-inference proxy to roughly **0.35×–3×** in the sensitivity interval.

The generic proxy is a fallback cost prior, not a model recommendation.

Self-hosted/open-source software therefore has zero software-license cost but not zero TCO.

## FX normalization

The scoring snapshot uses ECB reference rates for **2026-09-25**:

- 1 EUR = 1.1403 USD;
- 1 EUR = 7.6551 CNY.

All converted values keep the original currency and source in the pricing record. FX affects only the economic scenario.

## Prerequisites and bundles

The scorer must apply the catalog's `commercial_bundle_id`, `marginal_cost_rule` and `prerequisite_costs` before evaluating a stack.

Examples:

- one Microsoft 365 Copilot entitlement can cover several catalog capabilities;
- one JetBrains AI entitlement can cover Junie and AI Assistant;
- an open-source harness may require separately priced model inference;
- Sentry Seer, Grafana AI, Datadog Bits, New Relic Autopilot, Dynatrace Assist and similar add-ons require their underlying observability platform.

The current per-solution score is therefore a **marginal single-solution scenario**. A future portfolio optimizer must cost the shared prerequisite/bundle once across all tasks that use it.
