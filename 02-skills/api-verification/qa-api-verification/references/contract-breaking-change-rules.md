# Contract Comparison And Breaking Change Rules

## Inputs

- Previous OpenAPI/GraphQL schema/contract.
- Current release candidate OpenAPI/GraphQL schema/contract.
- Known consumer list and critical flows.
- Versioning and deprecation policy.

## Breaking Changes

Treat these as breaking unless explicitly versioned or approved:

- Removed endpoint, operation, GraphQL field, argument, mutation, or type.
- Changed method/path, required parameter, request body shape, or auth requirement.
- Removed response field used by consumers.
- Changed field type, enum values narrowed, nullable changed to non-null.
- Changed success/error status code without documented migration.
- Error response shape changed for a known consumer.
- Pagination/filtering contract changed.
- Rate-limit or header contract changed in a way that breaks clients.

## Usually Non-Breaking

- Optional response field added.
- Enum value added when clients are tolerant.
- Description/documentation update.
- New endpoint added.
- Nullable field widened from non-null to nullable only if consumers tolerate null.

## Report Fields

| Change ID | Contract area | Old | New | Breaking? | Consumer impact | Severity | Owner | Action |
|---|---|---|---|---|---|---|---|---|

## Recommendation Rules

- No-Go when a critical/high breaking change affects an active consumer and no migration
  or versioning path exists.
- Conditional Go when breaking change is behind a version, flag, or confirmed unused
  consumer path and owner accepts residual risk.
- Go when only non-breaking additions exist and verification evidence passes.

