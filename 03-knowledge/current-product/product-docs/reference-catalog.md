---
knowledge_id: CP-REFERENCE-CATALOG
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: TBD
authority: source-derived
scope: documented Conative reference values
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Reference Catalog

## Purchase Order Fields And Statuses

Canonical source: `docs/product/reference/purchase-orders/fields-and-statuses.md`

Visible Purchase Order list fields:

- PO ID
- PO Number
- Vendor
- Warehouse
- Created Date
- Expected Arrival Date
- Status
- Received Status
- Action

Observed list status values:

- `Draft`
- `Open`
- `Canceled`

Additional selectable filter labels:

- `Pending approval`
- `Partially Received`
- `Received`
- `Closed`
- `Rejected`

Received-status filter labels:

- `Not Received`
- `Received`
- `Over Received`
- `Under Received`

## Boundary

The meanings, calculations, and transition rules for these status values were not
verified. Presence in a filter proves only that the label is selectable, not that
the state is reachable or valid for every scope.

The canonical reference currently lacks `document_type: reference` and a stable
`doc_id`; its validator reports these as migration warnings.
