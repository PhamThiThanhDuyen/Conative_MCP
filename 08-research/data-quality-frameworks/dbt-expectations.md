# dbt Expectations Benchmark

- Primary sources:
  - https://hub.getdbt.com/metaplane/dbt_expectations/latest
  - https://github.com/metaplane/dbt-expectations
- Reviewed: 2026-07-30

## Concepts Worth Adopting

- Package reusable generic data tests close to transformed warehouse models.
- Express table, column, multi-column, aggregate, and cross-table expectations
  as declarative configuration.
- Let the existing dbt execution graph and artifacts carry execution context.
- Keep custom business tests available when reusable generic tests are not enough.

## Conative Mapping

Conative adopts reusable declarative checks and source-to-target comparisons.
It does not assume Conative uses dbt, nor does it embed dbt macros in skills.
Tool-specific implementations belong in replaceable scripts.
