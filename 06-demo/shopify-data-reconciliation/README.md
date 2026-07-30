# Shopify Data Reconciliation Demo

This demo uses `verify-data-quality` to compare read-only Conative values with
Shopify `Sales by product` values for an explicitly matched organization, store,
date range, timezone, currency, channel, and grain.

Start with the worked example in `00-presentation/USER_GUIDE.md` and the governed
procedure in:

- `03-knowledge/qa-intelligence/heuristics/source-data-reconciliation.md`
- `03-knowledge/business-contracts/conative-metrics/metric-catalog.md`
- `03-knowledge/business-contracts/conative-metrics/metric-quality-gaps.md`
- `03-knowledge/qa-intelligence/standards/data-quality-standard.md`

Runtime output belongs under `runs/<run-id>/` and is ignored by Git because it
may contain tenant, customer, session, screenshot, or report evidence. Publish a
sanitized example separately only after the required security and approval review.

Expected run artifacts:

1. `01-preflight.md`
2. `02-reconciliation-scope.md`
3. `03-reconciliation-result.md`
4. `04-evidence-package.md`
5. `05-gaps-and-recommendations.md`

The legacy `<5%` difference is a demo heuristic, not an approved business
threshold. Never report official Pass/Fail from that heuristic alone.
