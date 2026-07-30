---
name: verify-data-quality
description: >-
  Define and execute traceable data quality checks, then generate a Data
  Verification Report with metrics, failures, evidence, and residual gaps. Use
  for dataset, pipeline, import, migration, integration, dashboard, report, or
  reconciliation testing after data readiness is established.
---

# Verify Data Quality

## Inputs

- Ready or conditionally ready data scope
- Approved business expectations, schema, mappings, and reference values
- Source/target access, query or tool capability, and approved thresholds
- Risk IDs, environment/build, baseline, and evidence location

## Steps

1. Read `03-knowledge/qa-intelligence/standards/data-quality-standard.md` and
   applicable governance, business contract, current-product, and domain knowledge.
2. Build a check catalog. Each check must have an ID, data scope, dimension,
   expectation, threshold, severity, source, owner, and evidence method.
3. Cover applicable dimensions: schema, completeness, validity, uniqueness,
   referential integrity, consistency/reconciliation, freshness, volume, and
   distribution/anomaly.
4. Execute checks with the available replaceable script, query, or framework.
   Record `Passed`, `Warning`, `Failed`, `Error`, or `Blocked`; never turn an
   unknown expectation into a passing check.
5. Capture sanitized metrics and failing-row samples or references. Keep secrets,
   customer data, and project artifacts within approved storage boundaries.
6. Separate observed failure from suspected cause and link findings to risks.
7. Generate the artifact using `assets/data-verification-report-template.md`.

## Outputs

- Data Verification Report
- Check catalog, execution results, evidence, findings, and residual gaps

Tool syntax belongs in replaceable scripts or tool-specific references, not in
this skill.
