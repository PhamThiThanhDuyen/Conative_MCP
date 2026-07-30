---
name: automation-from-testcases
description: >-
  Convert approved Conative manual/API/UI test cases into maintainable
  automation with verified locators, deterministic test data, evidence capture,
  narrow execution, and auto-heal/recheck notes. Use when test cases are ready
  and the next step is Playwright/Selenium/API automation.
---

# Automation From Testcases

## Purpose

Turn review-approved test cases into executable automation without losing
traceability to requirement, risk, data, and evidence.

## Inputs

- Approved Testcase Matrix
- Target app/API URL and environment
- Existing test framework and helper conventions
- Auth/session strategy
- Test data requirements

## Workflow

1. Inspect existing tests, helpers, auth/session handling, and reports folder.
   Read `03-knowledge/governance/information-security-policy.md` before handling
   credentials, auth state, customer data, artifacts, or repository output.
   If the target is live or customer-connected, read
   `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`
   before selecting or executing cases.
2. Select automation candidates from Ready cases only.
3. For UI cases, verify locators against real DOM; prefer user-facing locators.
4. For API cases, reuse `qa-api-verification` patterns for schema/status/header checks.
5. Generate deterministic test data with cleanup.
   On live databases, use only QA-owned `CBI Test` entities and do not execute a
   mutation without developer backup confirmation and a named restore owner.
6. Implement the narrowest maintainable test and helper changes.
7. Run the smallest relevant command.
8. If failures are automation issues, fix and re-run. If business behavior conflicts
   with confirmed requirements, record a defect candidate.
9. Package run evidence using `evidence-package`.
   Keep project output local or in the approved private Conative GitLab only; do
   not transmit it elsewhere without explicit authorization.

## Output

| Case ID | Automation file | Data fixture | Command | Result | Evidence | Notes |
|---|---|---|---|---|---|---|

## Done When

- Automated cases map back to testcase IDs and risk IDs.
- Test data is deterministic, traceable, and sanitized.
- The selected command passes or the remaining failure is documented as product risk.
- Evidence is captured for pass/fail/blocked status.
- Live mutation runs include backup and developer restore confirmation; otherwise
  they remain Blocked.
