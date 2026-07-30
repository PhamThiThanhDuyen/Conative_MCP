---
knowledge_id: CP-WORKFLOW-CATALOG
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: TBD
authority: source-derived
scope: documented Conative workflows
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Workflow Catalog

All entries were source-verified on `2026-07-26`. A documented workflow may stop
before a destructive or state-changing submission; inspect `verification-gaps.md`
before treating it as end-to-end verified.

| Product area | Workflow | Documented outcome | Canonical source path |
|---|---|---|---|
| Dashboard | Start Replenishment from the Dashboard | Open relevant Replenishment Flow results from an inventory-risk card and review a PO preview | `docs/product/workflows/restock-from-dashboard.md` |
| Inventory Buying | Review a PO Preview from Replenishment Flow | Select a SKU-bearing result and review recommended order quantity before confirmation | `docs/product/workflows/create-purchase-order-from-replenishment-flow.md` |
| Inventory Buying | Choose a Replenishment Export PO Option | Review all-variant and selected-variant export choices | `docs/product/workflows/export-replenishment-purchase-order.md` |
| Inventory Buying | Prepare Target Coverage Days Change | Enable the required forecasting mode and open the bulk update dialog | `docs/product/workflows/set-target-coverage-days.md` |
| Inventory Buying | Prepare Bulk Reorder Quantity Change | Select variants and open the bulk reorder-quantity dialog | `docs/product/workflows/update-reorder-quantity.md` |
| Inventory Control | Start a Purchase Order | Open the PO form and review available fields and controls before saving | `docs/product/workflows/create-purchase-order.md` |
| Inventory Control | Import Purchase Orders | Review upload steps and formats before selecting a file | `docs/product/workflows/import-purchase-orders.md` |
| Inventory Control | Prepare a Transfer Order | Review required data for warehouse-to-warehouse movement | `docs/product/workflows/prepare-transfer-order.md` |
| Inventory Control | Prepare a Shipment | Choose a PO or transfer-order source and review required shipment fields | `docs/product/workflows/prepare-shipment.md` |
| Inventory Control | Review Shipment Details | Inspect source, dates, warehouse, supplier, and item quantities | `docs/product/workflows/review-shipment-details.md` |
| Inventory Control | Investigate Inventory Balances | Review warehouse totals, item balances, movement records, and history | `docs/product/workflows/investigate-inventory-balances.md` |
| Inventory Control | Review Supplier Profile | Review overview, purchase orders, and linked items without mutation | `docs/product/workflows/review-supplier-profile.md` |
| Inventory Control | Review Item Import Requirements | Review stages, template, and supported file requirements before upload | `docs/product/workflows/review-item-import-requirements.md` |
| Inventory Control | Review Shipment Import Requirements | Review stages, template, and supported file requirements before upload | `docs/product/workflows/review-shipment-import-requirements.md` |
| Data Management | Check Data Sync Health | Review summaries, source activity, and visible sync sequence | `docs/product/workflows/check-data-sync-health.md` |
| Data Management | Review Data Integration Actions | Review source actions and Shopify settings without changing a connection | `docs/product/workflows/review-data-integration-actions.md` |
| AI Assistance | Run an AI Agent Action | Start a predefined action and review its response in Connie | `docs/product/workflows/run-an-ai-agent-action.md` |
| AI Assistance | Prepare an AI Agent Report Schedule | Review timing, recipient, prompt, and instruction fields before creation | `docs/product/workflows/prepare-an-ai-agent-report-schedule.md` |
| AI Assistance | Ask Connie | Send a free-form question and review the answer or recovery guidance | `docs/product/workflows/ask-connie.md` |
