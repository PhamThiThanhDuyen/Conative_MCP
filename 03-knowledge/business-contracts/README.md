# Business Contracts

Store BA/PO-approved definitions of intended Conative behavior. This is the
primary expected-result source for the target release and stated scope.

Business contracts may include requirements, acceptance criteria, business
rules, formulas, permissions, state transitions, client exceptions, and API
expectations. Every contract must identify its owner, approval status, scope,
target release, and source.

Use `business-contract-template.md` for new contracts. Keep drafts clearly marked
and never treat them as approved expected behavior.

## Registered Contracts

- `conative-3.0/`: normalized BA-provided Conative 3.0 services and use cases.
  Approval evidence is currently missing, so its authority remains `provided`.
- `conative-metrics/`: normalized Conative metric definitions and formulas from
  the Data Dictionary. Ownership and approval evidence are still required.
