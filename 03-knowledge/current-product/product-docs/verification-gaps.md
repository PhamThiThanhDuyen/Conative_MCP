---
knowledge_id: CP-VERIFICATION-GAPS
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: QA owner
authority: source-derived
scope: gaps explicitly preserved by current product documentation
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Product Documentation Verification Gaps

These are not confirmed defects. They are behavior boundaries that the canonical
product documentation explicitly leaves unverified. Use them to route QA work and
BA questions.

| Gap ID | Area | Unverified behavior | Risk | Primary source paths |
|---|---|---|---|---|
| VG-001 | Access control | Role-specific visibility and permissions across Inventory Control and Data Management | Tests may incorrectly generalize one signed-in context to all roles | `start-here/inventory-control.md`, `features/inventory-control/shipments.md`, `features/data-management/*.md` |
| VG-002 | Dashboard and analytics | Metric formulas, refresh timing, background processing, channel applicability, and ABC grade assignment | Wrong numbers or stale data may drive inventory decisions | `features/dashboard.md` |
| VG-003 | Data Monitoring | Summary formulas, time boundaries, refresh behavior, status meaning, and sync-sequence transitions | Health indicators may be misinterpreted | `features/data-management/data-monitoring.md`, `workflows/check-data-sync-health.md` |
| VG-004 | Replenishment | Validation, save/discard, refresh persistence, selection persistence across pages, hidden variants, reset AI suggestion, and empty states | Reorder recommendations or user changes may be lost or misunderstood | `features/inventory-buying/replenishment-flow.md` |
| VG-005 | Reorder and coverage | Bulk update limits, persistence, and downstream effect of Reorder Quantity or Target Coverage Days on forecast and reorder results | Direct risk of incorrect purchasing quantity | `workflows/update-reorder-quantity.md`, `workflows/set-target-coverage-days.md` |
| VG-006 | Purchase Orders | Form validation, successful save, resulting status, approval behavior, and downstream effects | Core buying flow is not end-to-end established | `workflows/create-purchase-order.md`, `workflows/create-purchase-order-from-replenishment-flow.md` |
| VG-007 | Purchase Order import | Template columns, mapping, validation, duplicates, and import results | Bulk data may fail or create incorrect records | `workflows/import-purchase-orders.md` |
| VG-008 | Export | Download name, format, columns, values, scope, and completion behavior | Exported purchasing or supplier data may be incomplete or incorrect | `workflows/export-replenishment-purchase-order.md`, `features/inventory-control/suppliers.md` |
| VG-009 | Transfer and shipment lifecycle | Creation validation, saved state, shipment transitions, source-order updates, and downstream inventory effects | Stock movement and availability may diverge | `workflows/prepare-transfer-order.md`, `workflows/prepare-shipment.md`, `features/inventory-control/shipments.md` |
| VG-010 | Inventory balances | Quantity formulas, status rules, tab reconciliation, refresh timing, and meanings of reserved SO/TO values | Users may trust unreconciled inventory numbers | `features/inventory-control/items.md`, `workflows/investigate-inventory-balances.md` |
| VG-011 | Integrations | Connect/disconnect prerequisites, authorization, validation, confirmation, and post-change refresh | Source may appear available without being operational | `features/data-management/data-integrations.md`, `workflows/review-data-integration-actions.md` |
| VG-012 | AI schedules | Schedule creation, delivery, editing, pause/resume, deletion, and populated-state behavior | Reports may not be created or delivered as expected | `features/ai-assistance/ai-agents.md`, `workflows/prepare-an-ai-agent-report-schedule.md` |
| VG-013 | Master data and BOM | Supplier metric formulas, component stock/cost/lead-time calculations, vendor relationship, BOM costing and production rules | Master-data relationships or calculations may be wrong | `features/inventory-control/suppliers.md`, `components.md`, `bills-of-material.md` |
| VG-014 | Item and shipment imports | Template columns, mapping, validation, duplicate handling, and import results | Inventory-affecting bulk imports remain unproven | `workflows/review-item-import-requirements.md`, `workflows/review-shipment-import-requirements.md` |

## QA Handling

1. Check for an approved business contract before defining expected results.
2. Convert a gap into test cases only within a named environment, organization,
   role, data setup, and build.
3. Record observed behavior as current-product evidence.
4. Classify a difference as a defect only when an approved expectation exists.
5. Return unresolved formulas, permissions, transitions, and exceptions to BA/PO
   as requirement gaps.
