---
knowledge_id: BC-CONATIVE-3-SEARCH
knowledge_type: business-contract
source: SRC-BA-CONATIVE-3-SERVICES-USE-CASES
owner: Frank Tran (document author); approval owner TBD
authority: provided
scope: Custom Reports, Product Performance, Category, Collection, PO, Inventory Planner, Replenishment Flow, and Gap Analysis search
target_release: Conative 3.0
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Search Business Contracts

## Shared Search Pattern

Several use cases define this intended pattern:

1. User focuses the search field.
2. System proposes five recently searched entities.
3. User enters a supported identifier or chooses a recent suggestion.
4. System returns entities matching the query.
5. A no-match path displays a dedicated empty message.

The source repeatedly uses `search gần đúng` (fuzzy/partial search) but does not
define normalization, ranking, tokenization, case sensitivity, or match fields.

## Contract Matrix

| Rule ID | Use case | Input | Provided expected behavior | Source lines |
|---|---|---|---|---:|
| BR-SEARCH-001 | UC 3.6 Custom Report | Report name | Search reports the user created or may view; fuzzy report-name match; Admin or Member; show close CTA and five recent reports | 1865-1916 |
| BR-SEARCH-002 | UC 4.1.2 Product Performance | Shopify Product Title, SKU, Barcode | Five recent suggestions; fuzzy matching; Product view returns products and Variant view returns variants | 2039-2100 |
| BR-SEARCH-003 | UC 4.2.1 Sales by Category | Category name | Five recent category suggestions and matching category results | 3524-3577 |
| BR-SEARCH-004 | UC 4.3.1 Sales by Collection | Collection name | Five recent collection suggestions and matching collection results | 3788-3841 |
| BR-SEARCH-005 | UC 10.4 Purchase Orders | PO Number, PO ID, SKU | Fuzzy matching; SKU returns POs containing a corresponding line item | 5893-5940 |
| BR-SEARCH-006 | UC 11.3 Sales by Month | Variant Title, SKU, Barcode | Five recent suggestions; fuzzy matching; return variant data | 6784-6835 |
| BR-SEARCH-007 | UC 11.7 Replenishment Flow | Variant Title, SKU, Barcode | Five recent suggestions; fuzzy matching; return variant data | 7000-7053 |
| BR-SEARCH-008 | UC 12.2 Gap Analysis | Product Title, Variant Title, SKU, Barcode | Five recent suggestions; fuzzy matching; Product view returns products and Variant view returns variants | 7666-7724 |

## No-Result Messages

The historical analytics, Inventory Planner, Replenishment Flow, and Gap Analysis
use cases provide this intended message:

`SORRY! No data found - Please try searching other keywords or adjusting your filter`

UC 10.4 instead provides `You don't have any purchase order yet`, which can be
confused with a base empty-list state. UC 3.6 says only `no report found` without
an exact message.

For the **current Replenishment Flow search only**, decision
`BC-CONATIVE-3-DEC-RFS-EMPTY` supersedes the UC 11.7 message and selects the
Product Docs text:

`No replenishment results for this search`

## Approval And Conflict Rule

These rules are BA-provided but not evidenced as approved. The Replenishment
no-result conflict is resolved by `BC-CONATIVE-3-DEC-RFS-EMPTY`; other source
conflicts still require scoped owner review before defect classification.
