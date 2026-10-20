# Round 2 End-to-End Execution Details

## 1. Load the testcase and its contract

Use the exact testcase ID provided by the user. In Claude Task 2 Checklist-R2, locate one unique row and read the complete Prompt cell, Expected result, Steps, preconditions, channel, and current organization-specific Actual/Note/Version cells. Do not summarize, normalize, or fill missing prompt text. Confirm the canonical organization supplied by the user against the live Claude organization and the organization returned by Postman signIn. Resolve result columns by exact header. An approximate organization alias does not replace this live confirmation.

Read sheet-column-contract.md, comparison-rules.md, and comparison-report-template.md before selecting fields or writing results. The Expected result defines which metrics and explicit behaviors the case expects.

## 2. Submit the prompt in Claude

Open Claude in the in-app browser. If conative-claude is connected, disconnect only that connector and verify it is disconnected, then reconnect it for this execution using the setup skill. Follow the user's exact organization choice and connection procedure. Use the connector setup skill for connector name, URL, login help, organization selection, consent scope review, and connection verification.

Select only the exact organization the user supplied. Before granting access, inspect the live consent scope and obtain user confirmation for that scope. Never enter passwords, OTPs, or secrets on the user's behalf when the workflow requires user interaction. Submit only the exact testcase Prompt, once. Do not create a query, rewrite the request, or ask Claude to perform exploratory work. Allow only in-scope Conative tool calls needed to answer the prompt. Capture the values and timerange shown in Claude, including additional returned fields for the later mapping check.

## 3. Run the QE API request after Claude

Do not start the QE API request until Claude has answered the exact testcase Prompt and its requested values and timerange have been captured. Then run the matching QE request below once.


Use Postman My workspace, Conative collection, Conative MCP QE folder, and Conative environment. Follow `../../../execute-api-QE.md` to run signIn and chooseOrg, target the exact organization, derive source and date inputs, select productList for product prompts or variantList for variant prompts, inspect the current request body, and run once.

Before sending stored credentials to the login endpoint, confirm the user has authorized that specific transmission. Keep credentials and tokens ephemeral and out of notes/evidence. Resolve dates from the prompt and request timezone. Use the source spelling and from_source value in comparison-rules.md. Default sort_field to gross_sales only when the request needs sorting and the prompt does not name a field. Omit the active-status filter unless the prompt explicitly asks for active status. Do not save changes to the collection or alter its definition to force a result. Stop if the target is wrong, the request is not read-only, or required inputs cannot be derived.

Capture the returned response fields, status, date range, timezone, source/channel scope, filters, grain, and visible warnings as useful context.

## 4. Compare mapped values

Use confirmed Claude-to-QE paths from comparison-rules.md. Compare every relevant expected Claude value that has a confirmed QE mapping and is within the testcase Expected result or the user's explicit request. Skip any field with no confirmed mapping and list it as unmapped; do not infer a similarly named QE field. An unmapped extra field that is not expected is neither a mismatch nor a blocker. An unmapped expected field prevents PASS and leads to PARTIAL when mapped checks otherwise pass.

For numeric values, ignore display separators and require exact numeric equality unless the testcase defines a tolerance. Do not convert units or currencies. For text values, compare the same mapped field. For lists or objects, match items only by a stable key required by the testcase or approved rules, not by list order alone.

Check explicit Expected result conditions, such as a requested timerange, against the Prompt. Record channel, source, filters, date range, timezone, grain, and scope differences as context. Do not silently modify either query to force a match.

## 5. Status and Note cell

Use the canonical status definitions and single Note format in `../../../assets/comparison-report-template.md`. PASS requires every expected field to have a confirmed mapping, all compared values to match, and every explicit Expected result condition to hold. FAIL requires a demonstrated mapped-value mismatch or a demonstrably unmet explicit Expected result condition. PARTIAL applies when at least one expected field is unmapped, mapped checks are complete, and no demonstrated failure exists. BLOCKED applies when a required value is unavailable, a request fails, scope or comparison rules are unresolved, or no expected field remains comparable. A demonstrated failure takes precedence over PARTIAL/BLOCKED. HTTP success alone does not establish PASS.

Only write when the user asks to record/update the result. Confirm the exact row, organization-specific headers, cell validation, and current contents first. Update `Actual <org>`, exact `Note <org> - <channel>`, and exact `Version <org> - <channel>` cells together. Write the execution date to Version as `MMM d, yyyy` (example: `Oct 16, 2026`) using the run's stated timezone. Do not overwrite an existing result unless the user explicitly asked to rerun or update it. If a required header or write permission is missing/ambiguous, or live validation does not permit the applicable status token, leave the result cells unchanged and report the limitation.

Follow `../../../assets/comparison-report-template.md` for one Note format across PASS, FAIL, PARTIAL, and BLOCKED. Every Note line begins `- `. For every numeric comparison, Difference is Claude − QE API. Include compared values, Claude timerange, unmapped expected fields where relevant, scope context, and evidence-based root cause (or `Unknown` when a failure has no established cause). Do not imply a completed comparison in a BLOCKED note.

Read all three updated cells back and confirm the workbook saved. Report testcase ID, organization, status, cell addresses, execution date written to Version, mapped fields and values, relevant scope, and skipped unmapped fields when useful. Keep credentials, tokens, cookies, session state, and unnecessary customer data out of the report.
