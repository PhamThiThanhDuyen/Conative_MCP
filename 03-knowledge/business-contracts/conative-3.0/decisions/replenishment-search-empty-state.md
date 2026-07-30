---
knowledge_id: BC-CONATIVE-3-DEC-RFS-EMPTY
knowledge_type: business-contract
source: Conative owner decision, 2026-07-30; SRC-CURRENT-PRODUCT-DOCS
owner: Conative QA owner
authority: provided
scope: Replenishment Flow search no-result state
target_release: current
status: active
last_verified: 2026-07-30
supersedes:
  - UC 11.7 historical no-result message in SRC-BA-CONATIVE-3-SERVICES-USE-CASES
---

# Replenishment Search Empty-State Decision

## Decision

For the current Replenishment Flow search, use the Product Docs message as the
expected no-result text:

`No replenishment results for this search`

## Superseded Text

The Conative 3.0 BA document UC 11.7 contains the historical text:

`SORRY! No data found - Please try searching other keywords or adjusting your filter`

Do not use that historical text as the current Replenishment Flow expected
result. Retain it only for source traceability and historical comparison.

## Scope Boundary

This decision resolves only the Replenishment Flow search empty state. It does
not automatically resolve Product Performance, Sales by Month, Gap Analysis,
Category, Collection, Purchase Order, or Custom Report empty messages.
