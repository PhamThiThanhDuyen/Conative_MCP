---
name: qa-api-verification
description: >-
  Verify REST and GraphQL APIs for Conative release readiness, including auth,
  schema, business rules, error handling, security, performance, contract
  comparison, breaking-change detection, evidence reporting, and fix
  recommendations. Use when: "verify API release," "API go/no-go," "REST
  verification," "GraphQL verification," "OpenAPI contract diff," "breaking
  change check." Not for: UI-only browser flows - use api-data-ui-verification
  or Playwright UI skills. Related: testcase-matrix-design, go-no-go-report,
  residual-risk-assessment.
license: MIT
metadata:
  author: Conative
  version: "0.1"
  category: automation
---

<objective>
Prevent API releases from passing with only happy-path smoke checks. This skill
turns an API scope into evidence: endpoint coverage, auth boundaries, schema
validation, business-rule checks, error/security/performance assertions,
contract-diff findings, and a Conative-ready go/no-go recommendation.
</objective>

## Quick Route

| Situation | Route |
|---|---|
| Swagger/OpenAPI only | REST + schema validation + contract baseline |
| Old and new OpenAPI specs | Contract comparison + breaking-change detection |
| GraphQL endpoint | GraphQL query/mutation + introspection diff |
| Existing API test failures | Evidence report + fix recommendation |
| Release gate | Full workflow + report validator |

## Discovery Questions

Check repo docs, `.agents/qa-project-context.md`, existing API specs, and Conative
task context first. Ask only what is still missing:

- API type and source: REST OpenAPI, GraphQL schema, manual endpoint list, or mixed.
- Environment: base URL, build/version, branch, release scope, and test account policy.
- Live-data classification: read-only versus create/update/delete scope, backup
  confirmation, and restore owner when the environment is live or customer-connected.
- Auth: JWT, API key, OAuth2, session cookie, service token, roles, token refresh.
- Contract baseline: old spec, current spec, consumer expectations, or Pact broker.
- Business rules: approved domain rules and owner; do not infer missing rules.
- Thresholds: response-time budget, payload-size limit, rate-limit policy, security scope.

## Core Principles

1. **Verify contracts, not implementation details.** Assert status, response
   shape, headers, auth boundaries, and public business outcomes. Avoid internal
   database assumptions unless a data-validation requirement explicitly needs it.
2. **Do not invent domain rules.** Separate Confirmed, Observed, Assumed, and
   Open Question. Block affected cases when the expected behavior is not approved.
3. **Every failure needs reproducible evidence.** Record request, sanitized
   headers, payload, response, status, timing, environment, build, and trace/log
   links where available.
4. **Breaking changes are release risks.** Removed fields, changed requiredness,
   narrowed enum values, removed operations, status-code drift, and auth changes
   must be called out before go/no-go.
5. **Security and performance are part of API readiness.** Include auth bypass,
   IDOR/BOLA, injection-like payloads, mass assignment, sensitive data exposure,
   response time, payload size, and burst behavior when in scope.

## Workflow

1. Load `references/api-verification-standard.md`.
   Load `03-knowledge/governance/information-security-policy.md` when handling
   authentication, customer data, project artifacts, repositories, or external
   transmission.
   For live or customer-connected targets, also load
   `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`.
2. Load only the protocol references needed for the scope:
   - REST/GraphQL/schema: `references/rest-graphql-patterns.md`
   - Security/performance: `references/security-performance-rules.md`
   - Contract/breaking changes: `references/contract-breaking-change-rules.md`
3. Build an Endpoint/Operation Catalog with method/path or GraphQL operation,
   auth requirement, request schema, response schema, business rule, and risk ID.
4. Produce a Verification Matrix covering:
   - `skill-auth-verification`
   - `skill-rest-verification`
   - `skill-graphql-verification`
   - `skill-schema-validation`
   - `skill-business-rule-validation`
   - `skill-error-handling-validation`
   - `skill-security-validation`
   - `skill-performance-validation`
   - `skill-contract-comparison`
   - `skill-breaking-change-detection`
5. Execute or design the smallest useful verification. Prefer existing project
   test runners and scripts; otherwise document executable requests and expected
   assertions.
   Do not execute a live mutation without developer backup confirmation and a
   named restore owner. Mutate only QA-owned `CBI Test` records, never customer data.
6. Fill `assets/api-verification-report-template.md`.
7. If contract inputs exist, fill `assets/contract-diff-report-template.md`.
8. Add fix recommendations using `assets/fix-recommendation-template.md`.
9. Run `python scripts/validate_api_verification_report.py <report.md>` and fix
   every error before handoff.

## Output

- API Verification Report
- Endpoint/Operation Catalog
- Verification Matrix
- Evidence Package
- Contract Diff / Breaking Change Report when applicable
- Fix Recommendation list
- Go/No-Go input with residual API risks

## Human Gates

- QA confirms assumptions and blocked domain rules.
- API/backend owner confirms business-rule expectations.
- Security owner confirms security scope for destructive or burst tests.
- Developer confirms the fresh backup before live mutations and confirms database
  restoration after the run.
- QA/release owner signs final go/no-go recommendation.

## Anti-Patterns

**Happy-path-only API readiness.** One `200 OK` per endpoint does not prove a
release is safe. Add negative, auth, schema, header, and edge coverage.

**Hardcoded credentials or tokens.** Tokens expire and secrets leak. Use
environment references and sanitize all evidence.

**External project-data disclosure.** Keep code, contracts, payloads, evidence,
and reports local or in the approved private Conative GitLab. Do not upload them
to another destination without explicit authorization.

**Schema spot checks.** `toHaveProperty` is not enough for release gates. Use
OpenAPI/AJV/Zod/GraphQL introspection/Pact-style verification where possible.

**Unreviewed breaking-change labels.** Treat compatibility as evidence-based:
show old vs new contract, consumer impact, severity, owner, and mitigation.

## Verification

Run the report validator:

```powershell
python scripts/validate_api_verification_report.py <report.md>
```

If automation was generated or modified, run the narrowest API test command from
the target project, for example:

```bash
npx playwright test tests/api
python -m pytest tests/api
schemathesis run ./openapi.yaml --url https://staging.example.com --checks all
```

## Done When

- API report has scope, environment/build, catalog, matrix, evidence, results,
  residual risks, and owner actions.
- Each Ready verification row maps to requirement/risk/endpoint/evidence.
- Blocked rows name the missing decision and are excluded from pass-rate.
- Contract/breaking-change findings include consumer impact and release severity.
- Evidence is sanitized and reproducible.
- Validator passes without errors.

## Related Skills

- **testcase-matrix-design** - use before this skill when requirement coverage
  and test data still need to be designed.
- **release-readiness** / **go-no-go-report** - use after this skill to make the
  release recommendation.
- **security-testing** - use for deeper OWASP/API security assessment beyond
  release-gate coverage.
