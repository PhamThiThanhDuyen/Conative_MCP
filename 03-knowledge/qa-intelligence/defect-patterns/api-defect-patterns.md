# API Defect Patterns

| Pattern | Signal | Evidence to capture |
|---|---|---|
| Schema drift | Field removed/type changed/nullability changed | Old/new contract, response sample, consumer impact |
| Auth boundary failure | 401/403 missing or wrong role can access | Token role, request, response, endpoint permission |
| IDOR/BOLA | User accesses another user's resource by ID | User A/B setup, IDs masked, status/body |
| Validation gap | Invalid payload accepted or wrong error shape | Payload, expected rule, response details |
| Mass assignment | System/admin field accepted from client | Payload, persisted result, response |
| Sensitive data exposure | Password/hash/token/internal stack in response | Sanitized response, endpoint, severity |
| Data inconsistency | UI/API/report/database disagree | UI value, API response, data/log evidence |
| Performance regression | Latency/payload/burst exceeds baseline | Timing, payload size, concurrent run summary |
