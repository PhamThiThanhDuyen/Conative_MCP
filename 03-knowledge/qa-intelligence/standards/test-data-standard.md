# Conative Test Data Standard

## Principles

- Test data must be unique, traceable, deterministic when seeded, and free of real PII.
- Never store credentials, passwords, tokens, cookies, OTPs, private keys, or
  session state as plaintext. Reference them through approved secret-store,
  protected CI/CD variable, or local environment-variable names only.
- Every fixture needs an expected outcome and cleanup plan.
- Follow `../../governance/information-security-policy.md` for authentication
  storage, project-information boundaries, and GitLab handling.

## Data Matrix

| Data ID | Category | Setup/seed | Input/state | Secret reference | Expected | Cleanup |
|---|---|---|---|---|---|---|

## Required Categories

| Category | Required examples |
|---|---|
| Positive | Valid required fields, valid optional fields, supported locale/timezone |
| Negative | Missing required, invalid type, invalid format, duplicate, unauthorized |
| Boundary | `min-1`, `min`, `min+1`, `max-1`, `max`, `max+1`, zero, first/last page |
| Edge | Unicode, whitespace, special chars, very long input, null, empty array/object |
| Security | XSS-like, SQL-like, mass-assignment fields, unsafe IDs |

## Naming

For non-live environments, use traceable automation prefixes:

```text
auto_<feature>_<case-id>_<timestamp>
```

Examples:

- `auto_order_CREATE_001_20260729`
- `auto_api_user_20260729@example.test`

For a Conative live database, the live naming rule overrides the `auto_` format.
Every named persistent test entity, including reports, purchase orders, and
views, must start with `CBI Test`. Follow
`live-environment-testing-standard.md`.

## Cleanup

- Tests that create data should delete or isolate it.
- If cleanup is unsafe or unavailable, record residual data risk.
- Shared seeded data must be read-only unless the test owns reset behavior.
- On a live database, do not modify customer-owned data and do not treat manual
  cleanup as a substitute for the required developer-managed backup and restore.
