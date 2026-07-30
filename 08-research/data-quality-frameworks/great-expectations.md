# Great Expectations Benchmark

- Primary sources:
  - https://docs.greatexpectations.io/docs/core/define_expectations/
  - https://docs.greatexpectations.io/docs/core/run_validations/create_a_validation_definition/
  - https://docs.greatexpectations.io/docs/core/trigger_actions_based_on_results/run_a_checkpoint/
- Reviewed: 2026-07-30

## Concepts Worth Adopting

- An expectation is a verifiable assertion; related expectations form a suite.
- A validation definition binds a concrete data batch to an expectation suite.
- Checkpoints coordinate validations and result-driven actions.
- Validation results are durable inputs for evidence and release decisions.

## Conative Mapping

| Framework concept | Conative capability |
|---|---|
| Expectation | Data Verification check contract |
| Expectation Suite | Check Catalog for a named scope |
| Batch + Validation Definition | Dataset/environment scope in the report |
| Validation Result | Data Verification Report result row |
| Checkpoint action | Evidence & Diagnosis or Release Intelligence handoff |

Conative adopts the separation of assertion, execution scope, and result. It does
not copy GX object models or require GX as the execution engine.
