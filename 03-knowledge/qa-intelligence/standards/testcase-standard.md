# Conative Testcase Standard

Use this standard when designing or reviewing manual, hybrid, or automation-ready
test cases.

## Required Testcase Columns

| ID | Priority | Type | Technique | Requirement/Risk ID | Preconditions | Test data | Steps | Expected result | Automation | Status |
|---|---|---|---|---|---|---|---|---|---|---|

## Required Techniques

- Equivalence partitioning for valid/invalid input classes.
- Boundary value analysis for limits, lengths, dates, amounts, pagination, retry counts, and time windows.
- Decision tables when two or more conditions drive an outcome.
- Negative and edge coverage for validation, permissions, empty states, loading/error states, data consistency, and security input.
- UI execution order: top-to-bottom, left-to-right for manual execution.

## Status Rules

| Status | Meaning |
|---|---|
| Ready | Requirement, data, and expected result are known |
| Ready - Manual | Good manual case; automation not required or not stable |
| Ready - Automation candidate | Stable assertions and setup exist |
| Blocked - Awaiting requirement | Expected behavior not approved |
| Blocked - Missing fixture | Data/environment missing |
| Blocked - Awaiting live backup | A live-data mutation lacks developer backup confirmation or a restore owner |
| Blocked - Awaiting restore confirmation | Live mutation testing finished but database restoration is not confirmed |
| Out of scope | Explicitly excluded from current release |

Blocked cases must not be counted as pass/fail.

## Live Environment Safety

For live or customer-connected environments, classify every case as `Read-only`
or `Mutation`. Apply `live-environment-testing-standard.md` to every mutation
case. Test steps must name the backup gate, `CBI Test` fixture, restore owner, and
post-test restore confirmation.

## Expected Result Rules

- Expected results must be deterministic and observable.
- Avoid vague phrases like "works correctly", "according to design", or "as expected" without a linked rule/source.
- When a limit is unknown, use symbolic values like `N-1/N/N+1` and mark affected cases blocked.
