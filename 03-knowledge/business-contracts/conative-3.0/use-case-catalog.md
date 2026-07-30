---
knowledge_id: BC-CONATIVE-3-USE-CASES
knowledge_type: business-contract
source: SRC-BA-CONATIVE-3-SERVICES-USE-CASES
owner: Frank Tran (document author); approval owner TBD
authority: provided
scope: Conative 3.0 use-case inventory
target_release: Conative 3.0
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Use-Case Catalog

Use this index to discover relevant BA intent, then read the source section and
`contract-quality-gaps.md` before converting it into expected test behavior.

## UC 1 - User

- UC 1.1 Sign up and create first organization, source line 166.
- UC 1.2 Sign in, line 299.
- UC 1.3 Forgot password, line 414.
- UC 1.4 Update password, line 524.
- UC 1.5 Update user's name, line 598; heading only, no detailed contract.

## UC 2 - Organization

- UC 2.1 Switch organizations in one account, line 600.
- UC 2.2 Create organization, line 650.
- UC 2.3 View organization members, line 756.
- UC 2.4 Update roles and permissions, line 780.
- UC 2.5 Invite user, line 829.
- UC 2.6 Remove user, line 944.
- UC 2.7 Leave organization, line 990.

## UC 3 - Custom Reports

- UC 3.1.1-3.1.5 Create from template, Product Performance, Dashboard, Sales by Category, or Sales by Collection, lines 1044-1480.
- UC 3.2.1 Update report and UC 3.2.2 Rename report, lines 1483-1618.
- UC 3.3.1 Manage permission and UC 3.3.2 Remove access, lines 1619-1732.
- UC 3.4 View list, UC 3.5 Delete, UC 3.6 Search, and UC 3.7 Filter, lines 1733-1992.

## UC 4 - Analytics And Reports

- UC 4.1.1-4.1.11 Product Performance view, search, time range, advanced filter,
  product/variant columns and tables, detail pages, and export, lines 1995-3218.
- UC 4.1.12-4.1.16 are struck out and must not be treated as active.
- UC 4.1.17-4.1.18 Dashboard donut charts, lines 3473-3521.
- UC 4.2.1-4.2.4 Sales by Category search, time range, columns, and export, lines 3524-3785.
- UC 4.3.1-4.3.4 Sales by Collection search, time range, columns, and export, lines 3788-4042.
- UC 4.4.1 Understock report, lines 4043-4141.
- UC 4.5.1-4.5.3 Overstock report, export, and advanced filter, lines 4142-4577.

## UC 6 - Integrations

- UC 6.1 Integration progress, line 4578.
- UC 6.2 Shopify connection, line 4639.
- UC 6.3 Facebook connection, line 4742.
- UC 6.4 Google connection, line 4808; explicitly marked Updating.
- UC 6.5 OceanX Bridge file sync, line 4895.

## UC 9 - Subscription And Billing

- UC 9.1 Free trial, UC 9.2 payment, UC 9.3 payment method, UC 9.4 cancellation,
  UC 9.5 billing history/export, and UC 9.6 discount, lines 5125-5701.

## UC 10 - Purchase Orders

- UC 10.1 PO list and UC 10.2 PO detail, lines 5702-5864.
- A second UC 10.2 covers Archive PO and is marked Pending, lines 5865-5892.
- UC 10.4 Search and UC 10.5 Filter, lines 5893-5993.
- UC 10.6.1 manual creation and UC 10.6.2 upload, lines 5994-6276.
- UC 10.7.1 receive item, UC 10.7.2 update vendor, and UC 10.7.3 update warehouse, lines 6277-6476.
- UC 10.8 Export, UC 10.9 Delete, and UC 10.10 Shiphero sync, lines 6477-6675.

## UC 11 - Inventory Planner

- UC 11.1-11.4 Sales by Month view, filter, search, and Target Sales, lines 6676-6876.
- UC 11.5-11.7 Replenishment Flow view, filter, and search, lines 6877-7053.
- UC 11.8-11.10 Reorder Quantity, Days of Stock, and Lead Time updates, lines 7054-7277.
- UC 11.11 Export and UC 11.12 column configuration, lines 7278-7452.

## UC 12 - Gap Analysis

- UC 12.1 View report, UC 12.2 Search, UC 12.3 time range, UC 12.4 columns,
  and UC 12.5 advanced filter, lines 7455-7889.

## UC 13 And 14 - Settings And ABC

- UC 13.1 Forecasting Settings and UC 13.2 Replenishment Settings, lines 8001-8106.
- UC 14 ABC Analysis, lines 7890-8000; it appears before UC 13 in the source.

## Coverage Count

The source contains 100 active-looking `UC` headings when group headings and
malformed `deUC`/`reUC` labels are included. This is a discovery count, not a
count of approved, complete, unique use cases.
