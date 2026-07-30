# API Specs And Contracts

Store API contracts and contract-change evidence here. Do not store secrets,
tokens, or private production payloads.

## Files To Add

| File | Purpose |
|---|---|
| `openapi-current.yaml` / `.json` | Current release candidate contract |
| `openapi-baseline.yaml` / `.json` | Previous approved contract |
| `graphql-schema-current.graphql` | Current GraphQL schema |
| `graphql-schema-baseline.graphql` | Previous GraphQL schema |
| `contract-diff-<date>.md` | Human-readable diff and release impact |
| `consumer-map.md` | API consumers and compatibility expectations |

## Consumer Map Template

| Consumer | Owner | API area | Criticality | Contract source | Compatibility notes |
|---|---|---|---|---|---|

## Contract Change Template

| Change ID | Area | Old | New | Breaking? | Consumer impact | Owner | Decision |
|---|---|---|---|---|---|---|---|

## Usage

- `qa-api-verification` reads this folder before classifying breaking changes.
- Missing baseline means contract comparison is blocked, not skipped silently.
