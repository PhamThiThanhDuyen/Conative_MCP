---
name: execute-api-qe
description: Select and run productList or variantList in the Conative MCP QE Postman collection based on the entity asked about in the prompt, inspect the actual request body and API response, and report the result for QE comparison workflows.
---

# Execute QE API Request: productList or variantList

## Purpose

Run the existing QE API request that matches the entity asked about in the test prompt, and capture the query sent in its body plus the response returned by the QE API. Use `productList` for questions about products and `variantList` for questions about variants. Use the saved request as the source of truth, and resolve its runtime parameters from the test prompt before sending.

## Workflow

1. Open Postman and select **My Workspace** and enviroment **Conative**.
2. Read the test prompt to identify the entity, then open the matching request under the **Conative** collection > **Conative MCP QE** folder:
   - If the prompt asks about a product or products, select **productList**.
   - If the prompt asks about a variant or variants, select **variantList**.
   - Choose based on the entity grain the prompt asks for. If it is unclear whether the prompt needs products or variants, stop and report the ambiguity rather than choosing a request by guesswork.
3. Resolve the selected request's parameters from the test prompt:
   - If the prompt asks about Shopify, set `{{from_source}}` to `shopify`.
   - If the prompt asks about Nuorder/NuORDER, set `{{from_source}}` to `nu-order`.
   - Derive `{{from_date}}` and `{{to_date}}` from the period requested in the prompt and enter them as `YYYY-MM-DD` dates. For relative periods such as “last month” or “this year,” resolve the date boundaries using the execution date and the request's configured timezone, and record the resolved dates. Treat the end date according to the request's existing inclusivity convention.
   - Apply a status filter only when the prompt explicitly requests active status. For a prompt that says “active” or “status active,” include `{"field":"status","op":"eq","value":"active"}`. If the prompt does not ask for active status, remove/omit that status filter for this run.
   - If the prompt asks for a top-N list or ranking by a metric/field and the request exposes `{{sort_field}}`, set it to the field named in the prompt. For example, “top 10 products by gross sales” uses `gross_sales`; a ranking by gross quantity uses `gross_quantity`. Preserve the requested direction (highest/lowest) using the request's existing sort-direction parameter when available.
   - If the prompt asks “What was the total …” and does not specify a sort field, default `{{sort_field}}` to `gross_sales`. This default only fills the request parameter; it does not change the requested metric or the total aggregation.
   - Set these as request/runtime parameter values for this run; do not save changes to the collection. If the source or date range cannot be determined from the prompt and request configuration, stop and report what needs clarification rather than guessing.
4. Inspect the request before running it:
   - Confirm the method and URL shown in Postman.
   - Open **Body** and read/capture the current JSON query exactly as configured. Note relevant fields such as entity grain, channel scope, time range, filters, sorting, pagination, and options.
   - Verify that the request resolves `{{from_source}}`, `{{from_date}}`, and `{{to_date}}` to the values derived above. Capture those resolved values along with the rest of the query.
   - When applicable, verify that the request resolves the status filter and `{{sort_field}}` according to the prompt. If the saved request cannot express the requested status or ranking without changing its definition, stop and report the limitation; do not edit the saved request to force a match.
   - If the request is missing required setup or its target differs from the intended QE environment, stop and report the issue instead of guessing.
5. Click **Send** once. Do not save runtime parameter values or other edits to the collection unless the user explicitly asked to change the saved request.
6. Wait for the response and capture the status code, response body, and any visible runtime warnings or errors. For large responses, capture the summary and the specific fields relevant to the comparison; preserve the full response in Postman when available.
7. Report both the request query and response facts. Keep the resolved source, exact time range, timezone, channel scope, metric/field names, and units/currency explicit so the result can be compared with Claude or another expected result.

## Comparison guidance

- Compare like-for-like: same metric, date boundaries, timezone, channel/store scope, filters, and aggregation. A combined-channel response does not establish a channel-specific result.
- Treat the response actually returned by this run as evidence. Do not substitute earlier Postman output or historical Claude results.
- If the expected value or scope is ambiguous, report the mismatch/uncertainty; do not alter the query to force a match.
- If the request fails, report the HTTP status and relevant error/warning. Do not mark a downstream test as passed based only on a successful HTTP status.
- When this request is part of a spreadsheet test, update only the exact requested Actual and Note cells after the comparison has been completed and verified. Follow the parent `SKILL.md` rules for status mapping, blocked cases, and read-back verification.

## Known request location

- Workspace: **My Workspace**
- Collection: **Conative**
- Folder: **Conative MCP QE**
- Request: Select **productList** for product questions or **variantList** for variant questions, as described in the workflow.

The saved request body may change over time. Always inspect the current body in Postman before each run and describe what was actually sent.
