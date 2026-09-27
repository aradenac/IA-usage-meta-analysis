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
