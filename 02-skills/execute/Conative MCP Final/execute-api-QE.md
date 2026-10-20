---
name: execute-api-qe
description: Select the requested Conative organization in Postman, then run the existing productList or variantList QE API request with runtime inputs derived from the testcase prompt.
---

# Execute QE API Request

Use this workflow after capturing Claude's answer for a user-selected testcase.
It selects the target organization in QE, runs one matching read-only list
request, and captures the request and response for comparison. Use the saved
Postman requests as the source of truth; do not save collection or environment
changes unless the user explicitly requests that change.

## Postman location

- Workspace: **My Workspace**
- Collection: **Conative**
- Folder: **Conative MCP QE**
- Environment: **Conative**
- Requests: **signIn**, **chooseOrg**, **productList**, **variantList**

## Steps

1. **Sign in and identify the organization.** Open `signIn` in the Conative
   collection and select **Run/Send**. Before sending stored credentials to the
   login endpoint, confirm that the user authorized this specific transmission.
   Keep credentials and returned tokens ephemeral; never copy them into notes,
   evidence, chat, or project files. From the response, find the organization
   whose name exactly matches the organization required by the testcase/user
   instruction, and capture its organization ID for the next step. If there is
   no exact match, more than one plausible match, or the response does not
   provide an ID, stop and report the blocker instead of choosing an organization.

2. **Switch to that organization.** Open `chooseOrg`. In the request URL, enter
   the organization ID immediately after `/switch-organization/` (following the
   saved request's URL pattern), then select **Run/Send**. Confirm the response
   indicates the requested organization was selected. Do not continue if the
   selected organization is absent, different, or cannot be verified. Do not
   expose or retain any access token returned by this call.

3. **Set runtime inputs and run the matching data request.** Read the exact
   testcase prompt and choose the request by the requested entity grain:
   `productList` for product(s), `variantList` for variant(s). If the grain is
   ambiguous, stop and clarify. Set the following values in the active
   **Conative** environment for this run only:
   - `from_source`: use the exact organization/channel mapping in
     `references/comparison-rules.md` (for example, Shopify is `shopify` and
     Nuorder is `nu-order`). Do not infer a source from organization name alone.
   - `from_date` and `to_date`: derive from the prompt as `YYYY-MM-DD`, using the
     request's configured timezone and existing end-date inclusivity convention.
     Resolve relative periods using the execution date and record the resolved
     boundaries. Stop if the period or timezone cannot be resolved.
   - `sort_field`: when the prompt requests a top-N/ranking and the selected
     request uses this variable, set it to the requested metric field and
     preserve the requested direction using the existing direction parameter.
     If a total prompt requires a sort value and names no field, use
     `gross_sales`; this parameter default does not change the requested metric.
     Do not invent or add a sort field if the request does not require one.

   Inspect the selected request's current method, URL, and body before running.
   Confirm the active environment resolves all required variables to the values
   derived above. Prepare an unsaved, request-local runtime body overlay: omit a
   literal active-status filter when the prompt does not explicitly request active
   status, and preserve any other filters. Keep the active-status filter only when
   the prompt explicitly asks for active status. Resolve `from_source` using the
   exact approved mapping value (for example, `shopify`); do not pass a UI/display
   label such as `Shopify Conative`. Override the environment values for source,
   dates, and sorting for this run only. Do not save environment or collection
   changes. Do not stop merely because the saved template contains an active
   filter or a display-label source; apply this one-run overlay. Stop only if the
   remaining required scope cannot be expressed within these rules or the request
   is not read-only. Run the request once.

## Capture and report

- Capture the request name, method/URL, query/body, resolved runtime values,
  environment alias, status code, response values, and visible warnings/errors.
- Record source/channel, date boundaries, timezone, filters, sorting, pagination,
  grain, and units/currency when available so the result can be compared fairly.
- Treat this run's response as evidence. HTTP success alone does not establish a
  passing comparison. Report failures and missing data without changing the
  request to force a match.
- Keep secrets, tokens, cookies, session state, and unnecessary customer data out
  of reports and evidence.
