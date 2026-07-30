# Conative API Verification Standard

## Evidence States

| State | Meaning | Allowed status |
|---|---|---|
| Confirmed | Approved spec, AC, contract, config, or owner decision | Ready |
| Observed | Seen in current environment but not approved as expected behavior | Discovery only |
| Assumed | Proposed behavior awaiting approval | Blocked - Awaiting requirement |
| Defect candidate | Observed behavior conflicts with confirmed expectation | Ready for triage |

## Required Matrix Columns

| ID | Skill Area | Endpoint/Operation | Requirement/Risk ID | Scenario | Data ID | Expected | Evidence | Result | Status |
|---|---|---|---|---|---|---|---|---|---|

## Required Coverage

- Auth: missing token, expired token, invalid token, role boundary, refresh flow.
- REST: status code, response body, headers, CRUD lifecycle, pagination/filtering.
- GraphQL: query, mutation, variables, errors array, public schema/introspection diff.
- Schema: response shape, required fields, nullable fields, enum values, formats.
- Business rules: approved domain outcomes only; block unknown rules.
- Error handling: malformed body, validation errors, not found, conflict, rate limit.
- Security: IDOR/BOLA, injection-like input, mass assignment, sensitive data exposure.
- Performance: response-time budget, payload size, concurrent/burst behavior.
- Contract: old vs new spec, consumer impact, breaking/non-breaking classification.

## Evidence Rules

- Store sanitized request/response evidence. Never expose credentials, tokens, OTPs,
  production PII, or secret values.
- Record environment, build/version, base URL, timestamp, account role, and command.
- Link every finding to one endpoint/operation, one requirement/risk, and one owner.
- Separate failed verification from blocked verification.
- Blocked items do not count as pass/fail for release confidence.

## Severity Guide

| Severity | API release meaning |
|---|---|
| Critical | Data loss, auth bypass, public breaking change, P0 business flow blocked |
| High | Major endpoint unusable, schema break for known consumer, security exposure |
| Medium | Non-critical endpoint failure, degraded performance, recoverable contract drift |
| Low | Documentation mismatch, minor header/copy issue, non-blocking observability gap |

