---
knowledge_id: BC-CONATIVE-3-INDEX
knowledge_type: business-contract
source: SRC-BA-CONATIVE-3-SERVICES-USE-CASES
owner: Frank Tran (document author); approval owner TBD
authority: provided
scope: Conative 3.0 services and use cases
target_release: Conative 3.0
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Conative 3.0 Business Requirements

Normalized knowledge from the BA-authored document `Conative 3.0 - Services &
Use cases`. The source describes intended behavior, but no explicit approval
evidence was supplied. Treat it as `provided` and require BA/PO confirmation
before using a disputed rule as the sole basis for a defect or release decision.

## Contents

1. `source-index.md`: immutable source identity, size, hash, and provenance.
2. `service-catalog.md`: service-level scope and documented priority.
3. `use-case-catalog.md`: discoverable index of documented use cases.
4. `search-contracts.md`: normalized cross-product search requirements.
5. `contract-quality-gaps.md`: inconsistencies, stale markers, and approval gaps.
6. `decisions/`: scoped owner decisions that resolve source conflicts.

## Authority Boundary

- BA-authored intent: available and traceable.
- BA/PO approval: not evidenced in the supplied file.
- Current implementation: use `03-knowledge/current-product/` instead.
- Differences between this source and current Product Docs are requirement
  conflicts to review, not automatic defects.

## Read Protocol

1. Start with `service-catalog.md` and `use-case-catalog.md`.
2. Read an existing normalized domain contract such as `search-contracts.md`.
3. When more detail is required, open only the source line range registered for
   the target UC; do not load the complete 49,521-word source by default.
4. Normalize newly used rules into a focused domain contract and retain UC IDs
   and source line references.
5. Check `contract-quality-gaps.md` and approval status before creating a Ready
   expected result.
