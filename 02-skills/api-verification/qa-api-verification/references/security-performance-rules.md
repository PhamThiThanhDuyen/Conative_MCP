# Security And Performance Rules

## Security Checks

| Area | Required release-gate checks |
|---|---|
| Auth bypass | Missing token, expired token, tampered token, lower role on higher role endpoint |
| IDOR/BOLA | User A cannot access or mutate User B resource by changing ID |
| Injection | SQL-like, XSS-like, command-like input is rejected or safely sanitized |
| Mass assignment | Extra admin/system fields are ignored or rejected |
| Sensitive data | Response never includes password, token, secret, hash, internal stack trace |
| Content type | Unsupported media type rejected with deterministic status |
| Malformed body | Invalid JSON/body returns controlled 400/422, not 500 |
| Rate limit | Burst behavior follows documented policy and exposes retry guidance if applicable |

Do not run destructive, high-volume, or intrusive security tests without explicit scope
and environment approval.

## Performance Checks

- Response time: compare to approved SLA or baseline; if missing, record as open question.
- Payload size: check large list/detail endpoints for payload budget.
- Burst behavior: concurrent requests should not produce 5xx for supported load.
- Timeout behavior: slow dependency or timeout returns controlled error.
- Regression: compare current release candidate to previous baseline when available.

## Evidence

- Record request count, duration, p50/p95 when available, response codes, and payload size.
- Keep raw logs sanitized.
- Call out environment limitations: shared staging, cold cache, rate-limit protections,
  missing production-scale data, or unstable third-party dependencies.

