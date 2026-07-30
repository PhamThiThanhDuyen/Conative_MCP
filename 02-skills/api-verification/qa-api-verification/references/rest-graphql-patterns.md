# REST, GraphQL, And Schema Patterns

Adapted from benchmark patterns in `petrkindlmann/qa-skills` and
`anhtester/codex-testing-kit`; rewrite expected values to approved Conative
domain rules before use.

## REST Verification

- Happy path: exact status code, content type, response schema, key business fields.
- CRUD lifecycle: create, read, update, delete, verify deleted.
- PUT vs PATCH: PUT replacement behavior; PATCH partial update behavior.
- Pagination/filtering: first page, empty/out-of-range page, invalid page size,
  sort field, combined filters, unsafe search text treated as text.
- Headers: content-type, cache-control, retry-after, rate-limit headers, CORS when relevant.

## Field-Level Negative Data

For each request-body field, test independently before combined negatives:

| Field type | Checks |
|---|---|
| string | missing, empty, whitespace, min/max, special chars, Unicode, XSS-like, SQL-like |
| email | malformed, missing domain, duplicate when unique, max length |
| number | string type, negative, zero, min/max, overflow, decimal for integer |
| boolean | string boolean, null, 1/0 if unsupported |
| date | invalid format, impossible date, timezone boundary |
| enum | outside enum, wrong case, empty |
| array | empty, too many items, wrong item type, duplicate item |
| object | missing nested required field, extra field, null nested object |
| file | MIME type, empty file, oversize, unsafe filename |

## GraphQL Verification

- Query with variables returns `data` and no unexpected `errors`.
- Mutation verifies created/updated object and cleanup if it writes data.
- Invalid query returns `errors[]` with a deterministic message/category.
- Permission boundary returns authorization error without leaking data.
- Introspection diff catches removed public fields/resolvers before release.

## Schema Validation Options

- Use AJV/OpenAPI-aware validation when JSON Schema/OpenAPI exists.
- Use Zod or equivalent shared schema when the app already owns runtime schemas.
- Use GraphQL introspection snapshots for public schema drift.
- Use Schemathesis for OpenAPI property-based checks when an executable staging API exists.

