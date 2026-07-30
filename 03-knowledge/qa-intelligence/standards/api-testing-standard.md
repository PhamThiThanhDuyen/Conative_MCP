# Conative API Testing Standard

Use for REST, GraphQL, schema, auth, error, security, performance, and contract
verification.

## Minimum API Assertions

- Exact HTTP status code or GraphQL error/data contract.
- Response schema, not only spot-checked fields.
- Key business fields tied to approved rules.
- Error response details for negative cases.
- Headers: content-type and any cache/rate-limit/security headers in scope.
- Response time or payload budget when a threshold exists.

## REST Coverage

- Happy path per operation.
- Field-level validation for request bodies.
- Auth missing/invalid/expired/insufficient role.
- CRUD lifecycle when resource operations exist.
- Pagination, filtering, sorting, and search for list endpoints.
- Idempotency for PUT/DELETE where applicable.

## GraphQL Coverage

- Query with variables.
- Mutation with cleanup.
- Invalid query returns deterministic `errors[]`.
- Authorization boundary does not leak data.
- Introspection or schema diff for public field removals.

## Contract Coverage

Breaking unless approved/versioned:

- Removed endpoint/field/type/operation.
- Required field added to request.
- Field type changed.
- Enum narrowed.
- Nullable changed to non-null.
- Auth requirement changed.
- Error/status/header contract changed for active consumers.

## Security Release-Gate Checks

- Auth bypass.
- IDOR/BOLA.
- Injection-like input.
- Mass assignment.
- Sensitive data exposure.
- Malformed body should not produce uncontrolled 500.
- Rate-limit behavior when policy exists.
