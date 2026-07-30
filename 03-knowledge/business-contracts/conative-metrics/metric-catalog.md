---
knowledge_id: BC-CONATIVE-METRIC-CATALOG
knowledge_type: business-contract
source: SRC-CONATIVE-DATA-DICTIONARY
owner: BA/Data owner TBD
authority: source-derived
scope: Conative product, sales, AI forecast, inventory, and marketing metrics
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Metric Catalog

Readiness meanings:

- `usable`: source provides a direct formula or the field is descriptive.
- `partial`: formula exists but requires unresolved shared semantics or inputs.
- `missing`: no calculation rule is provided for a calculated metric.
- `conflict`: definition and formula materially disagree.

All entries inherit the source and authority in the frontmatter. Readiness does
not mean BA/Data approval.

## Product Information

| Metric ID | Field / metric | Source definition | Source formula | Readiness |
|---|---|---|---|---|
| MTR-PROD-001 | Title | Customer-facing product name | Descriptive field | usable |
| MTR-PROD-002 | SKU | Unique retailer-assigned alphanumeric identifier for a product or variation | Descriptive field | usable |
| MTR-PROD-003 | Product Status | Current selling state, such as Active, Draft, Archived, or Inactive | Descriptive field; allowed-value contract absent | partial |
| MTR-PROD-004 | Category | Product classification used for organization, filtering, and performance comparison | Descriptive field | usable |
| MTR-PROD-005 | Days on Site | Days since first publication until today | `Current date - First published date` | partial |
| MTR-PROD-006 | Product Grade | Grade based on cumulative percentage of revenue contribution | A: `0 < cumulative revenue % < threshold 1`; B: `threshold 1 <= cumulative revenue % < threshold 2`; C: `cumulative revenue % >= threshold 2` or `= 0` | partial |

## Sales

| Metric ID | Field / metric | Source definition | Source formula | Readiness |
|---|---|---|---|---|
| MTR-SALES-001 | Gross Sales | Sales before discounts and returns | `gross_qty * price` | partial |
| MTR-SALES-002 | Gross Quantity | Units before discounts and returns | `SUM(gross quantity)` in selected time range | partial |
| MTR-SALES-003 | Total Sales | Net Sales plus shipping income and taxes | `gross_sales - discount - return + tax + shipping_charges` | partial |
| MTR-SALES-004 | % of Revenue | Item contribution to total revenue | `(Gross Sales / Total Gross Sales) * 100` | partial |
| MTR-SALES-005 | Return Value | Value of returned product | `return_qty * price` | partial |
| MTR-SALES-006 | Return Quantity | Total returned units | `SUM(item.return_qty)` for `calendar_start_date` through `calendar_end_date` | partial |
| MTR-SALES-007 | Return Rate | Rate at which a product is returned | `return_qty / gross_qty` | partial |
| MTR-SALES-008 | Units Per Day | Average units sold per day | `gross_qty / Days on Site within selected time range` | partial |
| MTR-SALES-009 | Units Per Day (In Stock) | Average units sold on days with stock above zero | `gross_qty sold on days stock > 0 / count(days stock > 0)` | partial |
| MTR-SALES-010 | Units Per Day (Out of Stock) | Average units sold on days with sales while stock is negative | `gross_qty sold on days sales > 0 and stock < 0 / count(days sales > 0 and stock < 0)` | partial |
| MTR-SALES-011 | Sell Through | Units sold relative to units sold plus current stock | `Gross Quantity / (Gross Quantity + Current Stock) * 100` | partial |
| MTR-SALES-012 | Net Sales | Gross Sales less Returns and Discounts | `Gross Sales - Returns - Discounts` | partial |
| MTR-SALES-013 | Net Quantity | Units sold excluding returned units | `Gross Quantity - Return Quantity` | usable |
| MTR-SALES-014 | Discount Value | Deduction from usual product cost | `SUM(discount amounts)` | partial |
| MTR-SALES-015 | Gross Profit | Net Revenue less COGS and Operating Expenses | `Net Sales - Cost` | conflict |
| MTR-SALES-016 | Gross Margin | Defined in prose as Net Revenue less COGS | `(Net Sales - Cost) / Net Sales * 100` | conflict |

## AI Forecast

| Metric ID | Field / metric | Source definition | Source formula | Readiness |
|---|---|---|---|---|
| MTR-AI-001 | Trend | Whether Units per Day rises, falls, or remains stable over the selected range | Slope of Units per Day over selected range | partial |
| MTR-AI-002 | Sales Forecast (Forecasting Range) | Predicted sales quantity in the configurable forecasting range | Not provided | missing |

## Inventory

| Metric ID | Field / metric | Source definition | Source formula | Readiness |
|---|---|---|---|---|
| MTR-INV-001 | Reorder Quantity (AI) | Recommended reorder after forecast demand, current stock, and incoming stock | `MAX(Override Quantity OR Forecasted Sales from Today - (Stock + On Order), 0)` | partial |
| MTR-INV-002 | Days of Stock (ATS) | Days current and incoming stock can cover using average sales velocity | `(Stock on Hand + Incoming Stock on Order) / Units Per Day` | partial |
| MTR-INV-003 | Days of Stock (On Hand) | Days current stock can cover using average sales velocity | `Stock on Hand / Units Per Day` | partial |
| MTR-INV-004 | Days of Stock (AI) | Forecast-based days until stockout | If AI Stockout Date exists: `AI Stockout Date - Current Date`; if AI Not Yet: maximum forecast value; otherwise blank | partial |
| MTR-INV-005 | Days of Stock AI (Available) | Forecast-based days until stock on hand runs out | If AI Stock Date exists: `AI Stock Date - Current Date`; if AI Not Yet: maximum forecast value; otherwise blank | partial |
| MTR-INV-006 | Total Inventory Value (ATS) | Value of current and incoming inventory using item price | `(Stock + On Order) * Price` | partial |
| MTR-INV-007 | Total Inventory Value (Stock) | Value of currently stocked inventory | `Stock * Price` | partial |
| MTR-INV-008 | ROP | Minimum inventory needed to cover Lead Time | Not provided | missing |
| MTR-INV-009 | XX-Day Sales (Rule-based) | Sales quantity in the preceding configurable period aligned to forecasting range | Not provided | missing |
| MTR-INV-010 | Adjusted Qty (Product Level) | Final product order quantity after MOQ adjustment | `Reorder Qty + Additional Qty allocated to meet MOQ` | partial |
| MTR-INV-011 | Adjusted Qty (Variant Level) | Variant quantity after MOQ excess is distributed by sales contribution | `Reorder Qty + (Extra Qty due to MOQ * Variant Sales Contribution %)` | partial |
| MTR-INV-012 | Stock | Sellable inventory from the ecommerce platform across active locations | Descriptive aggregate; calculation and source mapping absent | partial |
| MTR-INV-013 | On Order | Supplier quantity ordered but not fully received | `SUM(Ordered Qty - Received Qty - Cancelled Qty)` for open POs | partial |
| MTR-INV-014 | ATS | Expected available quantity including current and incoming inventory | `Stock + On Order` | usable |
| MTR-INV-015 | Next Arrival Date | Nearest expected incoming inventory arrival date | Not provided | missing |
| MTR-INV-016 | Next Arrival Quantity | Quantity in the nearest expected incoming inventory | Not provided | missing |
| MTR-INV-017 | FBA Available | Sellable inventory stored and fulfilled by Amazon | Source field or aggregation not provided | partial |
| MTR-INV-018 | FBM Available | Sellable Amazon inventory stored and fulfilled by merchant | Source field or aggregation not provided | partial |
| MTR-INV-019 | Total Amazon Available | Total sellable inventory across FBA and FBM | `FBA Available + FBM Available` | usable |
| MTR-INV-020 | FBA Inbound Qty | Quantity shipped to Amazon but not yet received or available | Source statuses and aggregation not provided | partial |
| MTR-INV-021 | FBA FC Transfer Quantity | Units moving between Amazon fulfillment centers | Source statuses and aggregation not provided | partial |
| MTR-INV-022 | Recommended Inbound Quantity | Recommended quantity to send to FBA based on velocity, lead time, and buffers | Not provided | missing |
| MTR-INV-023 | Recommended Shipment Date to FBA | Recommended ship date to prevent FBA stockout | Not provided | missing |

## Marketing

| Metric ID | Field / metric | Source definition | Source formula | Readiness |
|---|---|---|---|---|
| MTR-MKT-001 | Product Views | Product detail page views in selected period | Source fields and deduplication not provided | partial |
| MTR-MKT-002 | Conversion Rate | Percentage of visitors who ordered after visiting store or product page | `(Gross Qty / Product Views) * 100` | conflict |
| MTR-MKT-003 | Ads Spend | Advertising cost charged by connected ad platforms in selected period | Source fields, currency policy, and aggregation not provided | partial |
| MTR-MKT-004 | Ads Click | Ad clicks directed to store or product page | Source fields and deduplication not provided | partial |
