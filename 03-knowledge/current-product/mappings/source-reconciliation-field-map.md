---
knowledge_id: CP-SOURCE-RECONCILIATION-FIELD-MAP
knowledge_type: current-product
source: SRC-QA-COMPARED-FIELDS
owner: Data/API owner TBD
authority: source-derived
scope: legacy Conative UI, response, and source-system reconciliation mappings
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Source Reconciliation Field Map

These are historical mappings extracted from the supplied QA guide. They have
not been verified against the current API or product. Use them to locate evidence,
not as proof of intended business behavior.

## Sales Summary

| UI field | Conative response field | Shopify Sales by product | Mapping state |
|---|---|---|---|
| Gross Sales | `summary.gross_sales` | Gross sales | source-stated |
| Gross Quantity | `summary.gross_quantity` | Ordered quantity | source-stated |
| Return Value | `summary.return_amount` | Returns | source-stated |
| Return Quantity | `summary.return_quantity` | Returned quantity | source-stated |
| Net Sales | `summary.net_sales` | Net sales | source-stated |
| Net Quantity | `summary.net_quantity` | Net quantity | source-stated |
| Total Sales | `summary.total_sales` | Total sales | source-stated |
| Tax | `summary.tax_amount` | Tax | source-stated |
| Discount Value | `summary.discount_amount` | Discounts | source-stated |

## Dashboard And GAP

| UI field | Legacy Conative field / endpoint | Mapping state |
|---|---|---|
| Gross Quantity | `gross_quantity` at `/analytic/products` | source-stated |
| Sales Per Day | `sales_per_day` at `/analytic/products` | source-stated |
| Sales Day Left | `sales_day_left` at `/analytic/products` | source-stated |
| Total Inventory Value | `total_inventory_value` at `/analytic/products` | source-stated |
| Stock | `stock` at `/analytic/products` | source-stated; conflicts with ATS paragraph below |
| Price | `price` at `/analytic/products` | source-stated |
| ROP | `rop` at `/analytic/products` | source-stated |
| Sell Through | `sell_through` at `/analytic/products` | source-stated |
| Return Rate | `return_rate` at `/analytic/products` | source-stated |
| Product Gross Sales | `gross_sale` at `/analytic/products` | source-stated; singular naming needs verification |
| % of Revenue | `percent_of_revenue` at `/analytic/products` | source-stated |
| Product Views | `product_view` at `/analytic/products` | source-stated |
| Conversion Rate | `conversion_rate` at `/analytic/products` | source-stated |
| Date Since Stockout | `date_since_stockouts` at `/analytic/gap/date-since-stockouts` | source-stated |
| Collection-filtered count | `total_products_count` in analytical product response | source-stated |

## Known Mapping Conflicts

| Mapping issue ID | Source statement | Treatment |
|---|---|---|
| MAP-CONFLICT-001 | ATS UI maps to response `stock`; Stock UI maps to `on_order`; On Order UI maps to `ats` | Likely transposed labels. Do not use until verified against a current response and UI. |
| MAP-CONFLICT-002 | Reorder Quantity paragraph points to `sell_through` at `/analytic/common/prediction/value` | Likely copied mapping. Reorder field name is absent and must be verified. |
| MAP-CONFLICT-003 | Percentage-of-Revenue paragraph maps Summary Gross Sales to `summary.gross_quantity` and labels it Gross Quantity | Formula requires sales value; verify likely `summary.gross_sales`. |
| MAP-CONFLICT-004 | Gross Margin heading gives `Gross Profit = Gross Profit / Net Sales` | Left side likely should be Gross Margin; percentage scaling and zero handling are absent. |
| MAP-CONFLICT-005 | Day on Site mapping and formula are struck through and link to changed logic | Retired rule; do not execute. |

## AI Endpoint History

The source includes AI endpoints and authentication examples, but explicitly
marks the entire Data AI procedure as no longer used. Credentials have been
removed from this knowledge. Do not execute those endpoints from this document.
