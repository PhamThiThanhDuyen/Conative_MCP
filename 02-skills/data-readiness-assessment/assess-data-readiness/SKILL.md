---
name: assess-data-readiness
description: >-
  Assess whether required data is available, understood, governed, and safe
  enough for a Conative QA activity. Use before data, API, UI, migration,
  report, dashboard, or integration verification when missing access, schema,
  ownership, freshness, reference values, lineage, or test data may block work.
---

# Assess Data Readiness

## Inputs

- Feature, release, dataset, and environment scope
- Data sources, owners, access method, and refresh expectations
- Schema, keys, mappings, reference values, and business rules when available
- Privacy classification and intended test operations

## Steps

1. Read the data quality standard, information security policy, test data
   standard, and live environment testing standard under `03-knowledge/`.
2. Inventory every required source, dataset, field group, owner, consumer, and
   environment. Label evidence as `Confirmed`, `Observed`, or `Unknown`.
3. Assess access, availability, schema, keys, expected volume, freshness,
   reference values, mappings, lineage, ownership, privacy, and testability.
4. Identify whether the test needs read-only access or mutation. For live data,
   block create/update/delete work until developer backup and restore ownership
   are confirmed.
5. Record missing inputs as blockers or risks. Do not invent a schema, mapping,
   formula, threshold, or expected value.
6. Classify the scope as `Ready`, `Conditionally Ready`, or `Not Ready`, with
   conditions and owners.
7. Generate the artifact using `assets/data-readiness-assessment-template.md`.

## Outputs

- Data Readiness Assessment
- Readiness decision, blockers, conditions, owners, and source traceability

This skill does not execute data quality checks or certify business correctness.
