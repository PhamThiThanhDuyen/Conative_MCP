---
knowledge_id: BC-CONATIVE-METRICS-INDEX
knowledge_type: business-contract
source: SRC-CONATIVE-DATA-DICTIONARY
owner: BA/Data owner TBD
authority: source-derived
scope: Conative product, sales, AI forecast, inventory, and marketing metrics
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Conative Metrics

Normalized metric knowledge derived from the Conative Data Dictionary Google
Sheet. This package gives QA and future agents a discoverable metric catalog
without treating incomplete formulas as approved truth.

## Read Order

1. Read `source-index.md` to confirm source scope and authority.
2. Find the metric in `metric-catalog.md` by stable metric ID or display name.
3. Check its definition and formula readiness before designing an expected result.
4. Read `metric-quality-gaps.md` when readiness is not `usable`.
5. Treat unresolved behavior as a requirement gap; never invent formula details.

## Contents

| File | Purpose |
|---|---|
| `source-index.md` | Source identity, extraction boundary, and authority |
| `metric-catalog.md` | Normalized definitions, formulas, and readiness |
| `metric-quality-gaps.md` | Missing inputs, ambiguities, and approval questions |

## Authority Boundary

- The Google Sheet is the named source for this package.
- The catalog is `source-derived`, not independently verified against code, UI,
  API, database, or client data.
- No approval owner, approval date, release, grain, or general calculation policy
  was available in the source.
- A formula marked `usable` is sufficiently explicit for initial test design, but
  remains subject to source authority and the gaps listed for shared semantics.
