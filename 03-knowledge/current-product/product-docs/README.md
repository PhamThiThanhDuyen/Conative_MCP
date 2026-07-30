---
knowledge_id: CP-PRODUCT-DOCS-INDEX
knowledge_type: current-product
source: SRC-CURRENT-PRODUCT-DOCS
owner: QA knowledge owner
authority: source-derived
scope: user-visible Conative behavior
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Product Docs Knowledge Index

This directory contains normalized QA knowledge derived from the canonical
Conative `product-docs` repository. It is not a raw copy of the documentation.

## Read Order

1. `source-index.md` for provenance and source version.
2. `capability-map.md` for product areas and cross-capability relationships.
3. `feature-catalog.md` for current visible capabilities.
4. `workflow-catalog.md` for current documented user journeys.
5. `reference-catalog.md` and `observed-data-contracts.md` for observed fields,
   values, and file constraints.
6. `../mappings/observed-product-mappings.md` for source-derived visible mappings.
7. `knowledge-coverage-report.md` for knowledge found and owner inputs still needed.
8. `verification-gaps.md` before designing tests or deciding release readiness.

## Interpretation Rule

This knowledge establishes what has been documented as currently implemented or
observed. It does not establish intended correctness. Compare material expected
results with an approved business contract.
