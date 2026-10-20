# Round 2 Comparison Rules

## Source and scope

Field mappings below were read from the `Field compare` tab (columns A:D, rows 1:72) of the source workbook [`MCP_Task2_DataCoverage_Checklist.xlsm`](https://docs.google.com/spreadsheets/d/1fNGCNLP8LXFuNxhuzPbXGQEu1uanFLeO/edit?gid=1825555923#gid=1825555923), supplied for this task. The tab headers are `ID`, `Group`, `Claude`, and `QE API`.

This table is a field-name mapping reference. It does not, by itself, approve business meaning, formulas, expected values, or a tolerance. Confirm the requested field and scope from the selected test case and use the existing execution guidance in `../../Conative MCP/execute-compare-data-conative-MCP-with-QE.md`.

## Organization, channel, and source mappings

The following values were read from the workbook's `Source` tab, columns A:D, rows 1:29. One organization may have multiple channel/source rows; use the row matching the testcase scope. Preserve the source spelling and `from_source` value when configuring or interpreting the QE API request.

### Approximate website organization names

The following are user-provided approximate name correspondences to help recognize an organization as it may appear on its website. They are aliases for identification only; they are not verified by the `Source` tab and do not replace the exact organization selected in Claude, the organization returned by `signIn`, or the live workbook's organization-specific column headers.

| Workbook / workflow organization | Approximate website name |
|---|---|
| Melinda | Melinda Maria |
| Naked | Naked Cashmere |

Use the workflow organization as the canonical label for comparison and spreadsheet lookup. Before using an approximate name to resolve an organization, confirm the actual organization in the live Claude/Postman context with the user; if it is ambiguous, stop and clarify. Do not infer that the website name, connector organization, QE organization, or spreadsheet column is equivalent based only on this table.

| Organization | Priority | Channel | QE API `from_source` |
|---|---|---|---|
| Melinda | High | Shopify | `shopify` |
| Melinda | High | Nuorder | `nu-order` |
| Chanluu | Immediate | Shopify | `shopify` |
| Annmarie | Low | Shopify | `shopify` |
| Annmarie | Low | AMZ | `amazon` |
| Mizmooz | High | Magento | `magento` |
| Mizmooz | High | Amazon Seller Central - US | `Amazon Seller Central - US` |
| Mizmooz | High | Macy's US | `Macy's US` |
| Mizmooz | High | QVC Drop Ship US | `QVC Drop Ship US` |
| AS98 | Normal | Magento | `magento` |
| AS98 | Normal | Amazon Seller Central - US | `Amazon Seller Central - US` |
| Naked | Low | Shopify | `shopify` |
| Bando | Low | Shopify | `shopify` |
| Ippo | Low | Shopify | `shopify` |
| Qalo | Low | Shopify | `shopify` |
| Qalo | Low | AMZ | `amazon` |
| Homesick | Low | Shopify | `shopify` |
| Purley | Low | Shopify | `shopify` |
| Purley | Low | AMZ | `amazon` |
| Noonday | High | Shopify | `shopify` |
| Noonday | Low | Wholesale | `wholesale` |
| Darlac | Low | AMZ | `amazon` |
| Bearchop | Low | AMZ | `amazon` |
| HP | Low | Shopify | `shopify` |
| HP | Low | AMZ | `amazon` |
| Magnolia | Low | Shopify | `shopify` |
| Milanova | Low | Shopify | `shopify` |
| Uncle Todd | Low | AMZ | `amazon` |

The previously inspected `Claude Task 2 Checklist-R2` tab exposed `Actual Melinda` and `Note Melinda`; it did not establish equivalent headers for other organizations or verify the channel-specific Note and Version headers now required by the result workflow. Do not assume those columns exist or write to another organization's cells; resolve the live workbook/tab and authorized `Actual <org>`, `Note <org> - <channel>`, and `Version <org> - <channel>` columns before recording a case.

## Field mappings in the source

| Group | Claude field/label | QE API field/path |
|---|---|---|
| *(blank in source)* | Total count | `pagination.total` |
| Product information | Variant Title | `variant_title` |
| Product information | SKU | `sku` |
| Product information | Product ID | `product_id` |
| Product information | Variant ID | `variant_id` |
| *(blank in source)* | Category name | `categories[].name` |
| Product information | Color | `color` |
| Product information | Barcode | `barcode` |
| Product information | Product Status | `status` |
| Product information | Days On Site | `days_on_site` |
| Product information | Default Color | `is_default_color` |
| Product information | Price | `price` |
| Product information | Compare At Price | `compare_at_price` |
| Product information | Cost Per Item | `cost_per_item` |
| Sales | Gross Sales | `gross_sales` |
| Sales | Gross Quantity | `gross_quantity` |
| Sales | % Of Revenue | `percent_of_revenue` |
| Sales | Return Value | `return_value` |
| Sales | Return Quantity | `return_quantity` |
| Sales | Return Rate | `return_rate` |
| Sales | Total Sales | `total_sales` |
| Sales | Sales Per Day | `units_per_day` |
| Sales | Sales Days Left (ATS) | `days_of_stock` |
| Sales | Sell Through | `sell_through` |
| Sales | Net Sales | `net_sales` |
| Sales | Net Quantity | `net_quantity` |
| Sales | Tax | `tax` |
| Sales | Discount Value | `discount_value` |
| Sales | Channel | `distribution_channels` |
| Sales | Product Grade | `product_grade` |
| Sales | Gross Profit | `gross_profit` |
| Sales | Gross Margin | `gross_margin` |
| *(blank in source)* | Refund Value | `refund_value` |
| *(blank in source)* | Store Credit Value | `store_credit_value` |
| *(blank in source)* | Exchange Quantity | `exchange_quantity` |
| *(blank in source)* | Store Credit Quantity | `store_credit_quantity` |
| AI | Next 90-Day Sales (AI) | `sales_forecast` |
| AI | Reorder Quantity (AI) | `reorder_quantity` |
| AI | Sales Days Left (AI) | `days_of_stock_ai` |
| AI | Sales Days Left AI (Stock) | `days_of_stock_ai_on_hand` |
| AI | AI Confidence | `ai_confidence` |
| Marketing | Product Views | `product_views` |
| Marketing | Conversion Rate | `conversion_rate` |
| Marketing | Ad spend | `ad_spend` |
| Marketing | Ad click | `ad_clicks` |
| Inventory | Stock | `stock` |
| Inventory | % Stock | `stock_percentage` |
| Inventory | On Order | `on_order` |
| Inventory | ATS | `ats` |
| Inventory | Total Inventory Value (ATS) | `total_inventory_value` |
| Inventory | Replenishable | `replenishable` |
| Inventory | ROP | `rop` |
| Inventory | Received Quantity | `received_qty` |
| Inventory | Received Quantity (%) | `received_qty_percent` |
| Inventory | Ordered Quantity | `ordered_qty` |
| Inventory | Ordered Quantity (%) | `ordered_qty_percent` |
| Inventory | Week Of Supply | `week_of_supply` |
| *(blank in source)* | Vendor name | `vendors[].name` |
| Inventory | Lead Time | `lead_time_days` |
| Inventory | Days Of Stock | `days_of_stock_on_hand` |
| *(blank in source)* | FC Transfer Quantity | `in_transit_stock` |
| *(source row is malformed)* | *(Claude field missing)* | `collections[].name` |

## Fields with no QE API mapping in the source

The following Claude labels appear in the source with the QE API cell blank. Do not infer a path or compare them through a similarly named field until the API/domain owner confirms the mapping:

- Sales Per Day (In Stock)
- Sales Per Day (Out Of Stock)
- 90-Day Sales (Rule-based)
- Trend
- Turnover Rate
- Position

## Incomplete or inconsistent source rows

- Several rows have a blank `Group` value. They are shown above as `*(blank in source)*`; the group has not been inferred.
- Some `ID` cells are repeated or contain values that do not follow the apparent sequence. Treat `ID` as source metadata, not as a unique field key. Identify mappings by the Claude label and QE API field/path.
- The row containing `collections[].name` has no Claude label; a nearby cell contains the note `Filed không có trong config column`, and subsequent rows contain numeric values without field labels. These rows are not usable as confirmed field mappings.
- Rows 70–72 contain only numeric values in the `ID`/`Group` area and no Claude label or QE API path. They are not usable as field mappings.
- The source does not define type-specific normalization, percentage/ratio representation, rounding, units, date/time handling, null behavior, or a general numeric tolerance. Resolve these per approved test case or owner decision; do not create a tolerance from examples in the workbook.

## Comparison procedure

1. Identify the exact Claude field requested by the test case and find its QE API path in the mapping table above.
2. If the field is unmapped, has an incomplete mapping, or has multiple plausible meanings, stop and report `REVIEW_REQUIRED` or the workbook's approved blocked status. Do not guess.
3. Confirm the two outputs represent the same requested field. Record dataset, grain, channel/source, filters, date range, timezone, and other scope details as context when returned. Follow the case's approved rule for scope; do not silently alter either query to force a match.
4. Compare returned values using the case's explicit comparison criteria. For numeric values, the existing Conative comparison workflow permits ignoring display separators and requires exact numeric equality unless the test case explicitly defines a tolerance. Do not silently apply rounding or unit/currency conversions.
5. For list/object results, compare the requested mapped fields for each corresponding item. Use a stable key specified by the testcase or approved rule; if no matching key is specified, do not assume list order establishes item identity.
6. Record source values, mapped field names/paths, observed scope, difference, and status in the run report. Do not claim a root cause unless evidence supports it.

## Status interpretation

Use the exact status tokens and cells allowed by the spreadsheet contract and selected test case. Under the existing comparison workflow, `PASS` means both values are available and satisfy the approved comparison rule; `FAIL` means both values are available and differ. If a value is missing, a request fails, the field is unmapped, or the comparison rule is unresolved, do not report `PASS` or `FAIL`; use an allowed blocked/review status or leave the result unchanged and report the blocker.
