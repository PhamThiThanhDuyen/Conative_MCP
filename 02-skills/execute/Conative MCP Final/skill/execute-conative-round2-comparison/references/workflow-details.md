# Round 2 End-to-End Execution Details

## 1. Load the testcase and its contract

Use the exact testcase ID provided by the user. In Claude Task 2 Checklist-R2, locate one unique row and read the complete Prompt cell, Expected result, Steps, preconditions, channel, and current organization-specific result cells. Do not summarize, normalize, or fill missing prompt text. Confirm the canonical organization supplied by the user against the live Claude organization and the organization returned by Postman signIn. Resolve result columns by exact header. An approximate organization alias does not replace this live confirmation.

Read sheet-column-contract.md, comparison-rules.md, and comparison-report-template.md before selecting fields or writing results. The Expected result defines which metrics and explicit behaviors the case expects.

## 2. Submit the prompt in Claude

Open Claude in the in-app browser. If conative-claude is connected, disconnect only that connector and verify it is disconnected, then reconnect it for this execution using the setup skill. Follow the user's exact organization choice and connection procedure. Use the connector setup skill for connector name, URL, login help, organization selection, consent scope review, and connection verification.

Select only the exact organization the user supplied. Before granting access, inspect the live consent scope and obtain user confirmation for that scope. Never enter passwords, OTPs, or secrets on the user's behalf when the workflow requires user interaction. Submit only the exact testcase Prompt, once. Do not create a query, rewrite the request, or ask Claude to perform exploratory work. Allow only in-scope Conative tool calls needed to answer the prompt. Capture the values and timerange shown in Claude, including additional returned fields for the later mapping check.

## 3. Run the QE API request after Claude

Do not start the QE API request until Claude has answered the exact testcase Prompt and its requested values and timerange have been captured. Then run the matching QE request below once.

Use Postman My workspace, Conative collection, Conative MCP QE folder, and Conative environment. Follow execute-api-QE.md to inspect signIn and chooseOrg, target the exact organization, derive source and date inputs, select productList for product prompts or variantList for variant prompts, inspect the current request body, and run once.

Before sending stored credentials to the login endpoint, confirm the user has authorized that specific transmission. Keep credentials and tokens ephemeral and out of notes/evidence. Resolve dates from the prompt and request timezone. Use the source spelling and from_source value in comparison-rules.md. Default sort_field to gross_sales only when the request needs sorting and the prompt does not name a field. Omit the active-status filter unless the prompt explicitly asks for active status. Do not save changes to the collection or alter its definition to force a result. Stop if the target is wrong, the request is not read-only, or required inputs cannot be derived.

Capture the returned response fields, status, date range, timezone, source/channel scope, filters, grain, and visible warnings as useful context.

## 4. Compare mapped values

Use confirmed Claude-to-QE paths from comparison-rules.md. Compare every relevant Claude value that has a confirmed QE mapping and is within the testcase Expected result or the user's explicit request. Skip any returned field with no confirmed mapping. Do not infer a similarly named QE field. An unmapped extra field is neither a mismatch nor a blocker.

For numeric values, ignore display separators and require exact numeric equality unless the testcase defines a tolerance. Do not convert units or currencies. For text values, compare the same mapped field. For lists or objects, match items only by a stable key required by the testcase or approved rules, not by list order alone.

Check explicit Expected result conditions, such as a requested timerange, against the Prompt. Record channel, source, filters, date range, timezone, grain, and scope differences as context. Do not silently modify either query to force a match.

## 5. Status and Note cell

PASS requires the mapped expected values to match and any explicit Expected result conditions to hold. FAIL requires an available mapped value to differ or an explicit expected condition to be demonstrably unmet. A missing value for a mapped field, failed request, unresolved scope, or no remaining mapped expected field cannot be reported as PASS or FAIL. Use an allowed blocked/not-run/N/A value if the live validation permits it; otherwise leave the result unchanged and report the limitation. HTTP success alone does not establish PASS.

Only write when the user asks to record/update the result. Confirm the exact row, organization-specific headers, cell validation, and current contents first. Write only Actual <org> and Note <org>. Do not overwrite an existing result unless the user explicitly asked to rerun or update it.

Follow comparison-report-template.md. Every idea in Note must be on a separate line beginning with a hyphen and a space, including PASS, FAIL, and blocked notes. For PASS, include each compared metric with its value and the Claude timerange. For FAIL, include both source values, Difference calculated as Claude minus QE API, the Claude timerange, and an evidence-based root cause or Unknown. For blocked/incomplete outcomes, do not use a pass/fail note. Keep useful scope context when available. Do not include unmapped fields as blockers.

Read the cells back and confirm the workbook saved. Report testcase ID, organization, status, cell addresses, mapped fields and values, relevant scope, and skipped unmapped fields when useful. Keep credentials, tokens, cookies, session state, and unnecessary customer data out of the report.
