# Evidence Sample: API Failure

Synthetic example only.

## Scope

- Case ID: API-USER-004
- Risk ID: RISK-AUTH-002
- Environment/build: staging / build `2026.07.29-rc1`
- Endpoint: `GET /api/admin/users/{id}`

## Expected

Viewer role receives `403 Forbidden` when accessing admin user detail.

## Actual

Viewer role receives `200 OK` with user detail fields.

## Evidence

| Evidence ID | Type | Sanitized details |
|---|---|---|
| EVD-001 | Request | `GET /api/admin/users/user-b`, role=`viewer`, token masked |
| EVD-002 | Response | Status `200`, body contains `id`, `email`, `role` |
| EVD-003 | Rule | Permission rule requires admin role |

## Finding

- Severity: High
- Pattern: Auth boundary failure / possible IDOR
- Owner: Backend/API owner
- Recheck: Repeat request with viewer token after fix; expect `403`.
