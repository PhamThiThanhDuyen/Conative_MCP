# Data Quality Capability Synthesis

## Decision

Only four frameworks receive deep benchmark coverage:

1. Great Expectations
2. Soda Core
3. AWS Deequ
4. dbt Expectations

They inform two Conative capabilities without becoming dependencies:

| Capability | Stable responsibility | Artifact |
|---|---|---|
| Data Readiness Assessment | Decide whether required data, knowledge, access, ownership, and safety conditions are sufficient to begin verification | Data Readiness Assessment |
| Data Verification | Define and execute approved checks, preserve metrics and evidence, and report failures and residual gaps | Data Verification Report |

## Shared Pattern

`Expectation -> Scope -> Metric -> Threshold -> Result -> Evidence -> Action`

The normalized check contract covers schema, completeness, validity, uniqueness,
referential integrity, consistency/reconciliation, freshness, volume, and
distribution/anomaly. Framework syntax, runtime, and storage remain replaceable.

## Explicit Non-Goals

- Do not clone any framework folder hierarchy or API.
- Do not make an execution framework part of business knowledge.
- Do not combine readiness assessment with verification execution.
- Do not interpret an execution error or missing expectation as a pass.
