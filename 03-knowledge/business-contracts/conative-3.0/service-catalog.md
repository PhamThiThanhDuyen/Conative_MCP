---
knowledge_id: BC-CONATIVE-3-SERVICES
knowledge_type: business-contract
source: SRC-BA-CONATIVE-3-SERVICES-USE-CASES
owner: Frank Tran (document author); approval owner TBD
authority: provided
scope: Conative 3.0 service inventory
target_release: Conative 3.0
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Service Catalog

The source places the service list under `High priority`, but does not provide a
separate priority value or ranking for each service.

| Service | Documented scope | Detailed UC coverage |
|---|---|---|
| User Service | Sign up, sign in, forgot/update password, update name, column configuration | UC 1.1-1.5; column configuration appears under report UCs |
| Organization Service | Create/switch organization, members, roles, invitation, removal, leave | UC 2.1-2.7 |
| Report Service | Create/update/share/search/filter/delete custom reports and export | UC 3.x plus report-specific UC 4.x |
| Data Service | Product performance, low stock, category/collection/price-range sales, mappings, grouping, chart API, filters | UC 4.x, UC 11.x, UC 12.x, UC 14 |
| Setting Service | Organization/user defaults including timezone, lead time, price range, columns, category | UC 13.1-13.2 only; remaining listed settings lack dedicated UCs |
| Integration Service | Shopify, Google Ads/Analytics, Facebook, file sync | UC 6.1-6.5 |
| Authorization Service | Authorization capability named but not separately defined | No dedicated UC group |
| Notification Service | Notification capability named but not separately defined | No dedicated UC group |
| Payment & Subscription Service | Trial, payment, payment methods, cancellation, history, discount | UC 9.1-9.6 |
| Purchase Order Modules | PO list/detail/search/filter/create/upload/receive/edit/export/delete/sync | UC 10.x |
| Tenancies Service | Service named without detailed scope | No dedicated UC group |
| Event Service | Service named without detailed scope | No dedicated UC group |

## Interpretation

The list is a capability inventory, not evidence that every listed service was
implemented or approved for one release. Use the detailed UC status and current
Product Docs before defining release scope.
