---
knowledge_id: CP-OBSERVED-PRODUCT-MAPPINGS
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: QA knowledge owner
authority: verified-current-behavior
scope: visible navigation, branch, field, and action mappings
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Observed Product Mappings

| Mapping ID | Source | Destination/result | Evidence boundary | Canonical source |
|---|---|---|---|---|
| MAP-001 | Dashboard stock risk actions | Replenishment Flow and PO preview | Destination observed; filter rule and PO result unknown | `docs/product/workflows/restock-from-dashboard.md` |
| MAP-002 | Replenishment selected results | PO preview | Preview observed; confirmation and saved PO unknown | `docs/product/workflows/create-purchase-order-from-replenishment-flow.md` |
| MAP-003 | Shipment source = Transfer Order | Transfer order ID, Ship from, Ship to | Required UI indicators only | `docs/product/workflows/prepare-shipment.md` |
| MAP-004 | Shipment source = Purchase Order | PO Number, Warehouse, Supplier | Required UI indicators only | `docs/product/workflows/prepare-shipment.md` |
| MAP-005 | Shipment Schedule action | Request status Scheduled | Request behavior documented; saved transition unknown | `docs/product/features/inventory-control/shipments.md` |
| MAP-006 | Shipment Mark as In transit action | Request status In Transit | Request behavior documented; saved transition unknown | `docs/product/features/inventory-control/shipments.md` |
| MAP-007 | AI Agent Run | Connie processing and response | Response depends on action and connected data | `docs/product/workflows/run-an-ai-agent-action.md` |
| MAP-008 | Data Monitoring source record | Source Sync Sequence | Zero-model empty sequence observed; populated sequence unknown | `docs/product/workflows/check-data-sync-health.md` |

These mappings describe user-visible relationships only. Source-to-target field
mappings, API-to-database mappings, formula lineage, consumer mappings, and
event/state transition mappings are not present in Product Docs.
