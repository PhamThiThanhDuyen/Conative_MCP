# Conative Generic Rules

These are generic QA rules only. Client/module-specific business rules must be
recorded in a dedicated rule register.

## Generic Rules

| Rule ID | Rule | Applies to |
|---|---|---|
| GEN-001 | Do not treat observed current behavior as expected behavior without an approved source. | All testing |
| GEN-002 | Blocked assumptions are excluded from pass/fail counts. | Test reporting |
| GEN-003 | Release evidence must include environment/build and recheck condition. | Evidence |
| GEN-004 | Secrets, tokens, OTPs, and real PII must be masked in artifacts. | Evidence |
| GEN-005 | API breaking changes require consumer-impact assessment. | API release |
| GEN-006 | Critical/High residual risks require owner acceptance before Conditional Go. | Release |
