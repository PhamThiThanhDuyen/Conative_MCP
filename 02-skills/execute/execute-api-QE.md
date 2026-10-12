---
name: execute-api-qe
description: Run the saved variantList request in the Conative MCP QE Postman collection, inspect the actual request body and API response, and report the result for QE comparison workflows.
---

# Execute QE API Request: variantList

## Purpose

Run the existing `variantList` request in Postman and capture the query sent in its body plus the response returned by the QE API. Use the saved request as the source of truth; do not recreate or silently change its payload.

## Workflow

1. Open Postman and select **My Workspace**.
2. Open the **Conative** collection, then the **Conative MCP QE** folder, and select **variantList**.
3. Inspect the request before running it:
   - Confirm the method and URL shown in Postman.
   - Open **Body** and read/capture the current JSON query exactly as configured. Note relevant fields such as entity grain, channel scope, time range, filters, sorting, pagination, and options.
   - If the request is missing required setup or its target differs from the intended QE environment, stop and report the issue instead of guessing.
4. Click **Send** once. Do not save edits to the collection unless the user explicitly asked to change the saved request.
5. Wait for the response and capture the status code, response body, and any visible runtime warnings or errors. For large responses, capture the summary and the specific fields relevant to the comparison; preserve the full response in Postman when available.
6. Report both the request query and response facts. Keep the exact time range, timezone, channel scope, metric/field names, and units/currency explicit so the result can be compared with Claude or another expected result.

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
- Request: **variantList**

The saved request body may change over time. Always inspect the current body in Postman before each run and describe what was actually sent.
