---
knowledge_id: CP-KNOWLEDGE-COVERAGE
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: QA knowledge owner
authority: source-derived
scope: all 39 canonical Product Docs Markdown pages
target_release: current
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Product Docs Knowledge Coverage Report

## Audit Scope

All 39 Markdown files under `docs/product/` were searched: 1 product overview,
3 product-area overviews, 15 feature pages, 19 workflow pages, and 1 reference
page. The source version and complete file list are in `source-index.md`.

## Knowledge Found And Normalized

| Knowledge needed | Product Docs result | Normalized location |
|---|---|---|
| Product capability and feature map | Found | `capability-map.md`, `feature-catalog.md` |
| User-visible workflows | Found | `workflow-catalog.md` |
| Visible PO fields/status labels | Found, partial | `reference-catalog.md` |
| File formats and size limits | Found for PO/item/shipment imports and PO/TO/shipment attachments | `observed-data-contracts.md` |
| Required create-form fields | Found for selected PO, TO, shipment, warehouse, supplier, and BOM forms | `observed-data-contracts.md` |
| Visible channels, identifiers, integration sources, and AI options | Found for verified tenant/workspace | `observed-data-contracts.md` |
| Navigation, branch, action, and visible result mappings | Found, partial | `../mappings/observed-product-mappings.md` |
| Known current-product limitations | Found | `verification-gaps.md` |

## Knowledge Not Present: Input Required

| Gap | Needed input | Suggested owner | Blocks |
|---|---|---|---|
| Roles and permissions | Role-permission matrix by module/action/environment | BA/PO + Engineering | Access-control expectations |
| Metric and calculation rules | Approved formulas, grain, rounding, timezone, null handling, and examples | BA/PO + Data | Dashboard, analytics, inventory, supplier, replenishment checks |
| State machines | Allowed states, transitions, triggers, rejection rules, and side effects for PO/TO/shipment/import/sync | BA/PO + Engineering | Lifecycle and breaking-change tests |
| API contracts | OpenAPI/GraphQL schemas, auth rules, examples, errors, consumers, and baselines | Engineering | API and contract verification |
| Architecture and data lineage | Service map, source-to-target flows, storage, refresh jobs, dependencies, evidence points | CTO/Engineering/Data | Failure isolation and reconciliation |
| Field mappings | Import templates, source-to-target fields, UI/API/DB names, transformations, defaults | BA + Data/Engineering | Import, migration, integration, reconciliation tests |
| Reference/master data | Approved enumerations, IDs, UOM list, status meanings, tenant/channel applicability | BA/PO | Validity and boundary tests |
| Business exceptions | Duplicate, partial, cancellation, over/under receipt, recovery, retry, and conflict rules | BA/PO | Negative and edge-case coverage |
| Non-functional targets | Performance, volume, freshness, availability, retention, and alert thresholds | CTO/Engineering/PO | Performance and data health decisions |
| Safe test fixtures | QA accounts, tenant/role coverage, synthetic datasets, setup/cleanup and restore owners | QA + Engineering | Repeatable execution on shared/live environments |

## Handling Rule

Do not infer the missing items from screenshots, labels, examples, or observed
tenant values. Route them through Requirement Engineering and keep affected
checks `Blocked` or `Conditionally Ready` until an accountable owner supplies an
approved source.
