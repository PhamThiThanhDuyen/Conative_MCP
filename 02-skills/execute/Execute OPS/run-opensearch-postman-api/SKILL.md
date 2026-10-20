---
name: run-opensearch-postman-api
description: Run the Conative GraphQL Summary_Variant and Summary_Product APIs in Postman for a user-provided organization, date range, and source. Use when the user asks to run these API checks; use record-graphql-results-to-sheet to write verified results to the GraphQLV2 workbook.
metadata:
  short-description: Run Conative GraphQL summary APIs in Postman
---

# Run Conative GraphQL Summary APIs

Run the requested read-only data checks and return their results for the spreadsheet skill.

## Inputs

Before running, collect all four values:

- `Org` (for example, `Melinda`)
- `from_date`
- `to_date`
- `from_source` (for example, `shopify`)

Do not guess missing values. Confirm that `from_date` is not later than `to_date` and preserve the date format expected by the saved requests.

## Run in Postman

Use the Postman in-app browser and follow this path:

1. Select workspace `DUYENQA_GraphQL`.
2. Select environment `OpenSearch_Duyen`. 
3. Open collection `Duyen_GraphQL_Live` → folder `Final`.
4. Open `SignIn` → `Login`. Inspect the saved request and run it once with `Send`. Do not display or copy credentials or tokens into chat or evidence.
5. From the `SignIn` response, find the organization whose name exactly matches `Org`. Use its organization ID in the `Choose_Org` request URL after `/auth/switch-organization/`, then click `Send`. If the organization is missing or ambiguous, stop and report it.
6. In environment `OpenSearch_Duyen`, find and set `from_date`, `to_date`, and `from_source` to the user's exact values, then save the environment ensure value has been saved. Do not change other variables.
7. Open `Final` → `Summary_Variant` and run its `Query` request once. Open Console to capture the response, status, and errors.
8. Open `Final` → `Summary_Product` and run its `Query` request once. Open Console to capture the response, status, and errors.

Inspect each request's method, target, and body before sending. Stop if a request is not the expected Conative environment or is not read-only. Do not edit or save collection requests. Keep auth material ephemeral and redact it from screenshots, notes, and reports. If sign-in requires entering credentials that are not already safely configured, pause rather than exposing or saving them.

## Result handoff

For each API, report the request name, organization, input dates/source, HTTP status, returned metrics, and any explicit green/pass or red/fail markers and associated error text. Preserve metric labels and values exactly. Do not infer pass/fail from a value alone. If the API provides no explicit check marker and there is no approved expected-value rule, say that status cannot be determined. Keep the two API results separate:

- `Summary_Variant` → `Sales_by_variant`
- `Summary_Product` → `Sales_by_product`

Use `record-graphql-results-to-sheet` only when the user asks to record the run.
