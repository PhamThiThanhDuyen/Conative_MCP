---
knowledge_id: QA-STD-DATA-QUALITY
knowledge_type: qa-intelligence
source: 08-research/data-quality-frameworks/capability-synthesis.md
owner: QE owner
authority: advisory
scope: global data verification
target_release: not-applicable
status: active
last_verified: 2026-07-30
supersedes: []
---

# Data Quality Standard

## Check Contract

Every data check must define:

- stable check ID and linked risk or requirement
- dataset, table, field, partition, and environment scope
- quality dimension and plain-language expectation
- approved threshold or comparison rule
- severity and accountable owner
- execution method and evidence location
- result status and observed metric

Allowed result statuses are `Passed`, `Warning`, `Failed`, `Error`, and `Blocked`.
`Error` means the check could not execute correctly; `Blocked` means required
knowledge, data, access, or approval is unavailable. Neither is a pass.

## Quality Dimensions

| Dimension | Question |
|---|---|
| Schema | Are fields, types, required columns, and structural contracts correct? |
| Completeness | Are required records and values present? |
| Validity | Do values satisfy approved formats, ranges, and domain rules? |
| Uniqueness | Are keys and uniqueness constraints respected? |
| Referential integrity | Do relationships resolve to valid records? |
| Consistency | Do equivalent values reconcile across sources, APIs, UI, and reports? |
| Freshness | Is data updated within the approved time boundary? |
| Volume | Is row or event volume within an approved range or baseline? |
| Distribution/anomaly | Has the shape or behavior changed beyond an approved tolerance? |

## Rules

1. Expectations come from approved knowledge or an explicitly labeled baseline.
2. Fixed thresholds and change-over-time thresholds must name their source.
3. Store metrics and a bounded, sanitized failure sample; do not expose customer
   data merely to prove a failure.
4. Reconciliation must name both sides, join keys, aggregation grain, tolerance,
   and treatment of missing or duplicate records.
5. A framework implementation is replaceable. The check contract and artifact
   remain stable across SQL, Python, dbt, Deequ, Soda, or Great Expectations.
6. Live mutations follow the live environment testing standard and use the
   `CBI Test` prefix for QA-created persistent entities.
