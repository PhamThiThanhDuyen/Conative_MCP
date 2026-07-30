---
name: go-no-go-report
description: >-
  Produce an evidence-based Conative Go/No-Go release recommendation using
  completed verification results, residual risks, blockers, owner actions, and
  recheck conditions.
---

# Go / No-Go Report

## Purpose

Make the final QA release recommendation from evidence, not feelings.

## Inputs

- Risk Map
- Testcase Matrix
- API Verification Report
- Evidence Package
- Residual Risk Assessment
- Open P0/P1 defects and blocked assumptions

## Workflow

1. Read `03-knowledge/qa-intelligence/standards/release-decision-standard.md`.
2. Summarize scope, build, environment, and evidence completeness.
3. Count Passed / Failed / Blocked and separate blocked from failed.
4. Highlight Critical/High residual risks and owner actions.
5. Choose recommendation:
   - `Go`
   - `Conditional Go`
   - `No-Go`
6. Add recheck condition and named approver/owner.

## Decision Rules

- `No-Go`: open Critical failure, unaccepted High breaking change, auth/security bypass,
  data integrity risk, P0/P1 flow blocked, or missing evidence for a critical path.
- `Conditional Go`: known Medium/High risk has owner acceptance, mitigation, rollback or
  monitoring, and a clear recheck trigger.
- `Go`: critical paths verified, no release-blocking defects, residual risks accepted,
  and evidence is complete enough for the release scope.

## Output

Use `04-templates/go-no-go.md`.

## Done When

- Recommendation has concrete evidence.
- Every required owner action is named.
- Recheck condition is testable.
- Human review/sign-off is recorded.
