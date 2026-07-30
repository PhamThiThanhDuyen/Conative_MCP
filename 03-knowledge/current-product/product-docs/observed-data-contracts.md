---
knowledge_id: CP-OBSERVED-DATA-CONTRACTS
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: QA knowledge owner
authority: verified-current-behavior
scope: observed user-visible fields, values, and file constraints
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Observed Data Contracts

These are UI-observed contracts from the 39 canonical Product Docs pages. They
support test discovery and data readiness, but do not prove backend validation
or intended business correctness.

## File Constraints

| Area | Operation | Visible formats | Visible maximum | Source |
|---|---|---|---:|---|
| Purchase Orders | Import | CSV, XLSX | 10 MB | `docs/product/workflows/import-purchase-orders.md` |
| Items | Import | CSV, XLSX | 10 MB | `docs/product/workflows/review-item-import-requirements.md` |
| Shipments | Import | CSV, XLSX | 10 MB | `docs/product/workflows/review-shipment-import-requirements.md` |
| Purchase Orders | Attachment | PDF, DOCX, XLSX, PNG, JPG | 5 MB | `docs/product/workflows/create-purchase-order.md` |
| Transfer Orders | Attachment | PDF, DOCX, XLSX, PNG, JPG | 5 MB | `docs/product/features/inventory-control/transfer-orders.md` |
| Shipments | Attachment | PDF, DOCX, XLSX, PNG, JPG | 5 MB | `docs/product/features/inventory-control/shipments.md` |
| Bills of Material | Upload BOM | Unknown | Unknown | `docs/product/features/inventory-control/bills-of-material.md` |

All three observed import dialogs expose `Upload file -> Map columns -> Import`.
Template columns, mapping rules, duplicate handling, validation messages, and
import outcomes were not observed.

## Required Create-Form Inputs

| Object | Required fields observed | Source |
|---|---|---|
| Purchase Order | PO Number, Vendor, Warehouse, Expected arrival date | `docs/product/workflows/create-purchase-order.md` |
| Transfer Order | Transfer Order ID, Ship from, Ship to, Expected Arrival | `docs/product/features/inventory-control/transfer-orders.md` |
| Shipment, common | Shipping Label, Expected ship date, Expected arrival date | `docs/product/features/inventory-control/shipments.md` |
| Shipment from Transfer Order | Transfer order ID, Ship from, Ship to | `docs/product/workflows/prepare-shipment.md` |
| Shipment from Purchase Order | PO Number, Warehouse, Supplier | `docs/product/workflows/prepare-shipment.md` |
| Warehouse | Warehouse ID, Warehouse Name, Type, Status, Address 1, City, State | `docs/product/features/inventory-control/warehouses.md` |
| Supplier | Supplier Name, Address Line 1, City, State, Country | `docs/product/features/inventory-control/suppliers.md` |
| Bill of Materials | Variant SKU, Component SKU, Count per variant | `docs/product/features/inventory-control/bills-of-material.md` |

The docs establish required indicators only. Validation rules, uniqueness,
server-side enforcement, saved state, and defaults remain unverified.

## Observed Values And Conditional Inputs

| Area | Field/control | Observed values or behavior | Scope |
|---|---|---|---|
| Shipment creation | Submit action -> request status | Schedule -> Scheduled; Mark as In transit -> In Transit | CB/I DEMO7 |
| Shipment list | Status | In Transit, Delivered | CB/I DEMO7 |
| Warehouse list | Status | Active, Inactive | Observed workspace |
| Product Performance | Distribution Channel | Shopify, Amazon | CB/I DEMO7 |
| Product Performance | Analysis level | Products, Variants, Lot code | CB/I DEMO7; other tenants may differ |
| Product Performance | Search identifiers | Shopify: Title, SKU, Barcode; Amazon also exposes ASIN | CB/I DEMO7 |
| AI Agent schedule | Frequency | Daily, Weekly, Monthly | CB/I DEMO7 |
| AI Agent schedule | Conditional field | Weekly: Mon-Sun; Monthly: Day of month; Daily: no extra frequency field | CB/I DEMO7 |
| AI action | Out-of-stock Time Range | 30-365 days; observed default 90 | CB/I DEMO7 |
| AI action | High-potential Level | product or variant; observed default product | CB/I DEMO7 |
| AI action | High-potential Time Range | 30-365 days; observed default 30 | CB/I DEMO7 |

Purchase Order statuses and received-status labels remain in
`reference-catalog.md` as the canonical normalized reference.

## Integration Catalog Snapshot

| Group | Observed sources |
|---|---|
| E-Commerce | Shopify, Magento |
| Marketplace | Amazon Seller |
| Wholesale eCommerce | NuOrder |
| Analytics & Advertising | Facebook Ads, Amazon Ads, Google Ads, Google Analytics, Edgemesh |
| ERP | ApparelMagic, NetSuite, Shiphero |
| Notification | Slack |

`Connect`, `Disconnect`, and `Manage` are observed action labels, not guaranteed
connection states. The source page is
`docs/product/features/data-management/data-integrations.md`.
