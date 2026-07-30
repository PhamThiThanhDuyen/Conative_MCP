---
knowledge_id: SRC-CURRENT-PRODUCT-DOCS
knowledge_type: current-product
source: Conative product-docs repository
owner: TBD
authority: verified-current-behavior
scope: user-visible Conative behavior
target_release: current
status: active
last_verified: 2026-07-30
supersedes: []
---

# Conative Product Docs Source Index

## Primary Source

- Repository URL: `https://gitlab.cbidigital.dev/conative/knowledges/product-docs.git`
- Kit submodule: `00-sources/product-docs`
- Canonical content: `00-sources/product-docs/docs/product/`
- Repository commit: `b375c3b0407dd5335aa082121c58368cdbb94ee0`
- Commit date: `2026-07-27T00:16:10+07:00`
- Commit subject: `docs: expand current product documentation`
- Source working tree during ingest: clean
- Product documents: 39 Markdown files
- Source `last_verified`: `2026-07-26`
- Ingest date: `2026-07-30`
- Access mode: read-only

## Validation

`npm run docs:validate` completed with 0 errors and 8 warnings.

Warnings cover missing migration metadata on the Purchase Order reference and
semantic-visual assessment for six complex workflows. They do not invalidate the
source, but they remain documentation-quality follow-ups.

## Normalized Outputs

- `capability-map.md`: product areas and current relationships.
- `feature-catalog.md`: normalized feature inventory.
- `workflow-catalog.md`: normalized workflow inventory.
- `reference-catalog.md`: observed reference values and limitations.
- `verification-gaps.md`: high-value unverified behavior for QA follow-up.

## Usage

Use this source to establish currently documented user-visible behavior and a
regression baseline. Follow source paths back to the canonical repository when
detailed steps, screenshots, or exact wording are required.

Do not use this source alone to decide whether current behavior is business-correct.
Compare it with an approved business contract when one exists.
