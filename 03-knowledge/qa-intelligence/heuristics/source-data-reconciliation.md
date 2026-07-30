---
knowledge_id: QA-SOURCE-DATA-RECONCILIATION
knowledge_type: qa-intelligence
source: SRC-QA-COMPARED-FIELDS
owner: QA/Data owner TBD
authority: source-derived
scope: read-only reconciliation between Conative and Shopify, NuORDER, or Amazon
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Source Data Reconciliation

Use this guide to compare Conative data with a connected commerce source. The
supplied source fully describes only Shopify checks. NuORDER and Amazon are
blocked pending their referenced OpenProject content and approved mappings.

## Mandatory Safety

- Perform read-only UI, export, or GET requests by default.
- Never change customer records, integration settings, collections, inventory,
  purchase orders, or source configuration during reconciliation.
- Never place credentials in URLs, Markdown, screenshots, scripts, or reports.
- Resolve credentials from an approved local encrypted secret store at runtime.
- For any unavoidable live mutation, follow the live-environment backup,
  authorization, restore, and reporting standard.
- Prefix any report, purchase order, or view created on a Conative live database
  with `CBI Test`.

## Required Inputs

| Input | Requirement |
|---|---|
| Organization / tenant | Explicit; never infer from an example account |
| Source channel | Shopify, NuORDER, or Amazon |
| Environment | Conative environment and source environment |
| Time range | Same start, end, timezone, and boundary rule on both sides |
| Grain | Summary, product, or variant |
| Join key | Stable source product ID or variant ID; SKU only with uniqueness evidence |
| Metrics | Named list linked to the Conative metric catalog |
| Tolerance | Approved metric-specific threshold and denominator policy |
| Credentials | Runtime reference only; no plaintext value in artifacts |

## Common Procedure

1. Record tenant, channel, environments, time range, timezone, grain, currency,
   filters, sync timestamp, and Conative build or API version.
2. Confirm the source sync is complete and both systems cover the same channels,
   locations, products, statuses, and date boundaries.
3. Obtain Conative data and source data without mutation. Prefer exports or
   authenticated read-only APIs for row-level checks.
4. Normalize identifiers, numeric types, signs, currencies, timestamps, nulls,
   duplicate rows, and aggregation grain before comparing.
5. Check key uniqueness on both sides before joining. Report one-to-many or
   unmatched records separately; do not hide them with `VLOOKUP` first-match behavior.
6. Reconcile record counts, missing keys, duplicate keys, and each requested metric.
7. Calculate signed difference and absolute difference. Calculate percentage
   difference only when the approved denominator and zero behavior are known.
8. Classify each result as Pass, Fail, Requirement Gap, Source Data Gap, Sync Lag,
   or Not Comparable and retain evidence from both sides.

## Shopify Summary Check

Open Shopify Admin for the authorized store, then use **Analytics > Reports >
Sales by product**. Select the exact Conative time range and compare its Summary
row with Conative Dashboard Summary.

| Conative metric | Conative response field | Shopify report field |
|---|---|---|
| Gross Sales | `summary.gross_sales` | Gross sales |
| Gross Quantity | `summary.gross_quantity` | Ordered quantity |
| Return Value | `summary.return_amount` | Returns |
| Return Quantity | `summary.return_quantity` | Returned quantity |
| Net Sales | `summary.net_sales` | Net sales |
| Net Quantity | `summary.net_quantity` | Net quantity |
| Total Sales | `summary.total_sales` | Total sales |
| Tax | `summary.tax_amount` | Tax |
| Discount Value | `summary.discount_amount` | Discounts |

`Ordered quantity` and `Returned quantity` may require enabling hidden Shopify
report columns. The source uses a global difference target below 5%, but does not
define the percentage denominator, zero behavior, currency handling, or approval.
Treat 5% as a legacy heuristic until an owner approves a metric-specific rule.

## Shopify Product / Variant Check

1. Export Conative data for the selected period and grain with title, source
   product or variant ID, and all requested metrics.
2. Export Shopify **Sales by product** for the same period with matching source
   ID, title, and report fields.
3. Validate uniqueness and aggregate duplicate transaction/report rows to the
   intended grain before joining.
4. Join using product ID at product grain or variant ID at variant grain.
5. Produce Conative value, Shopify value, signed difference, absolute difference,
   percentage difference, and status for every key.
6. Report missing-on-Conative, missing-on-Shopify, duplicate-key, and nonnumeric
   rows separately.

The legacy document demonstrates `VLOOKUP(..., FALSE)`. For reusable checks,
prefer a query, dataframe join, or spreadsheet lookup that exposes duplicate and
missing keys instead of silently selecting the first match.

## Shopify Collection Checks

| Check | Conative side | Shopify side | Expected comparison |
|---|---|---|---|
| Collection count | Count values exposed by the Collection filter or read-only collection API | Count both custom and smart collections with complete pagination | Counts equal after applying the same eligibility rules |
| Collection identity | Collection ID and name from Conative | IDs and titles from custom plus smart collections | IDs and names reconcile; same names do not replace ID matching |
| Product position | Filter Dashboard by collection and inspect Position | Read collection-product relation from Shopify API | Match by collection ID plus product ID; API position is preferred over Shopify UI order |
| Product count | Dashboard pagination or `total_products_count` from the analytical product response | Products count for the same Shopify collection | Counts equal with the same collection and eligibility rules |

Shopify REST collection endpoints in the source use API version `2023-04` and a
maximum page size of 250. That version is historical. Resolve the currently
approved API/version and cursor pagination rules before execution.

## Shopify Gross Profit Check

At variant grain, the legacy source calculates:

```text
Cost = Ordered Quantity * Cost per Item
Gross Profit = Net Sales - Cost
```

Obtain Net Sales and Ordered Quantity from Shopify **Sales by product**, filtered
by Variant ID. Obtain Cost per Item from the exact Shopify variant, preferably by
stable product and variant IDs. At product grain, sum variant Gross Profit only
after confirming all variants are included exactly once.

The source calculates Gross Margin as `Gross Profit / Net Sales` at the displayed
grain and calls it a Conative formula check rather than a Shopify comparison.
Both formulas remain subject to the conflicts in the metric catalog.

## Dashboard And Gap Checks

The source also contains legacy examples for ATS, Sales Per Day, Sales Day Left,
inventory value, ROP, Sell Through, Reorder Quantity, Return Rate, percentage of
revenue, Conversion Rate, Expected Stockout Days, Opportunity Cost, Days Since
Stockout, and Balance. Use them only as supporting QA history:

- resolve the expected formula from `business-contracts/conative-metrics/`;
- use `current-product/mappings/source-reconciliation-field-map.md` for observed
  endpoint names and known mapping defects;
- do not use the struck-through Data AI procedure; the source explicitly says it
  is no longer used;
- mark exact-value cases blocked when the metric catalog says `missing` or
  `conflict` and no approved decision exists.

## Artifact Minimum

Each reconciliation artifact must contain scope, source timestamps, join keys,
row counts, duplicates, unmatched keys, metric formulas, tolerance, result table,
evidence links, known limitations, and an explicit no-mutation statement.

## Channel Coverage

| Channel | Source coverage | Execution status |
|---|---|---|
| Shopify | Summary, export, collections, profit, Dashboard, and GAP examples | Draft usable after credential, freshness, and contract review |
| NuORDER | Only OpenProject work package `#50173` is referenced | Blocked: instructions and mappings absent |
| Amazon | Only OpenProject work package `#32737` is referenced | Blocked: instructions and mappings absent |
