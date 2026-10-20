---
name: execute-ops-summary-workflow
description: Run both Conative GraphQL summary APIs in Postman and record their verified statuses in the matching GraphQLV2 Google Sheets tabs. Use when the user asks to run the full Execute OPS workflow.
metadata:
  short-description: Run APIs and record OPS summary results
---

# Execute OPS Summary Workflow

Run the API checks, then record each successful result in its matching sheet tab.

## 1. Get the inputs

Use values already provided in the conversation. Ask once for any missing items:

- `Org` (for example, `Melinda`)
- `from_date`
- `to_date`
- `from_source` (for example, `shopify`)

Do not guess values. Confirm that `from_date` is not later than `to_date`.

## 2. Run the APIs

Follow [`run-opensearch-postman-api/SKILL.md`](../run-opensearch-postman-api/SKILL.md) with those inputs. Run `Summary_Variant` and `Summary_Product` as described there. Keep the two responses separate and preserve their metric labels, check markers, and failure details.

## 3. Record the results

For each API that completed successfully, follow [`record-graphql-results-to-sheet/SKILL.md`](../record-graphql-results-to-sheet/SKILL.md) using that API's response and the same input values:

- Record `Summary_Variant` in `Sales_by_variant`.
- Record `Summary_Product` in `Sales_by_product`.

Run the recording workflow separately for each API response so each tab gets its own run column. Do not record a response for an API request that failed. If one API fails, continue with the other if it succeeded, then report the failed API as blocked.

The recording workflow may write only explicit pass/fail markers or results supported by an approved comparison rule. Never infer a status from a metric value alone. Leave unconfirmed statuses blank and report them as undetermined.

## 4. Report completion

Summarize each API and sheet separately: request outcome, destination tab, statuses written, failed-cell notes, and skipped or blocked metrics. Confirm that each sheet edit was saved and read back. Do not claim a result was recorded if verification failed.
