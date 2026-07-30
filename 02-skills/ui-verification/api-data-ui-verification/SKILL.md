---
name: api-data-ui-verification
description: >-
  Verify user-facing behavior across UI, API, and data evidence for Conative
  release readiness. Use when a testcase needs proof that visible UI state,
  network/API response, persisted data, logs, or trace evidence agree. Not for:
  API-only contract verification - use qa-api-verification.
---

# API / Data / UI Verification

## Purpose

Produce reproducible evidence that a feature works across the user interface,
API boundary, and data layer without relying on visual checks alone.

## Inputs

- Testcase Matrix rows or release scope
- Environment, build/version, URL, account role
- API spec or observed network calls when available
- Data source/query/log/trace access if approved
- Risk IDs and expected business rules

## Workflow

1. Read `03-knowledge/qa-intelligence/standards/evidence-standard.md`.
   Read `03-knowledge/governance/information-security-policy.md` when handling
   authentication, customer data, artifacts, repositories, or external transfer.
   If the target is live or customer-connected, also read
   `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`.
2. For each selected testcase, identify the evidence layers required:
   - UI state: visible result, navigation, validation, loading/error state.
   - API/network: request, status, response body, headers, timing.
   - Data: created/updated/deleted record, aggregation, report metric, or fixture state.
   - Logs/traces: error-free path, expected service calls, useful trace ID if available.
3. Execute the smallest safe verification.
   Do not execute create, update, or delete behavior on live data until a
   developer confirms a fresh backup and restore ownership. Never mutate an
   existing customer record.
4. Capture sanitized evidence paths or inline summaries.
5. Separate Observed facts from suspected cause.
6. Mark each case `Passed`, `Failed`, or `Blocked` with reason.

## Output

| Case ID | Risk ID | UI evidence | API evidence | Data/log evidence | Result | Notes |
|---|---|---|---|---|---|---|

## Quality Rules

- Do not expose credentials, tokens, OTPs, real PII, or production identifiers.
- Never store plaintext passwords, tokens, cookies, session state, or other
  authentication material. Use approved secret references and redact evidence.
- Do not turn observed current behavior into expected behavior unless requirement-approved.
- If a data check is unavailable, record the limitation and residual risk.
- For dashboards/reports, validate both visible value and source/API evidence when possible.
- Prefix every report, purchase order, view, or other named persistent test
  entity created on a Conative live database with `CBI Test`.

## Done When

- Every verified case maps to a testcase, risk, environment/build, and evidence.
- Failures have expected vs actual, reproducible steps, and owner action.
- Blocked items name the missing access, data, or requirement decision.
