---
name: conative-mcp-final
description: Connect the Claude app to the Conative MCP staging connector for a user-selected organization, then run and document an explicitly requested Round 2 Claude versus QE API comparison. Use for Conative MCP setup and comparison work in this skill package; do not use for Claude Code or unrelated MCP/API work.
---

# Conative MCP Final

## Source of truth

The native Google Sheet `MCP_Conative_Task2_DataCoverage_Checklist_Final` (ID `1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ`) is the sole Round 2 testcase and result workbook until the user explicitly replaces it. Use the exact tabs `Claude Task 2 Checklist-R2` (testcase reading and result writing), `Field compare` (mappings/aggregation), and `Source` (organization and channel mappings). Do not use XLSX/XLSM copies.

## Workflow

1. Check the in-app browser for Claude. Open https://claude.ai visibly if needed; let the user sign in. Reuse a valid connection to the requested organization. Disconnect and reconnect only if the connection is absent, expired, or points to the wrong organization. For setup, follow [`access-claude-connect-org-success/SKILL.md`](skill/access-claude-connect-org-success/SKILL.md). Review live consent scope with the user before granting access, and verify Claude's connected organization before comparison.
2. Open Postman browser in app and follow [`execute-api-QE.md`](execute-api-QE.md) to run signIn and chooseOrg, target the exact organization, derive source and date inputs, select productList for product prompts or variantList for variant prompts, inspect the current request body, and run once. For `Next <x>-Day Sales (AI)`, set `forecast_time.from` to today's execution date and `forecast_time.to` to today plus `x` calendar days; do not reuse the historical sales period. Preserve the saved request's complete `fields` array exactly. Resolve `from_source` using the exact value in the approved mapping (for example, `shopify`, not a display label such as `Shopify Conative`). Build an unsaved request-local body overlay: omit a saved active-status filter unless the prompt explicitly asks for active status, and preserve other filters. Apply derived inputs only for this run; do not save request or environment changes. Keep credentials and tokens ephemeral; do not save collection edits or expose them in notes/evidence. Capture the returned response fields, status, date range, timezone, source/channel scope, filters, grain, and visible warnings as useful context.
3. Run the exact testcase Prompt once in Claude, capture its completed response and tool trace, then run the matching read-only QE request once. Compare each testcase fully before moving to the next one. Save Claude/QE screenshots only when the user requests bug creation; then put them under `evidence/round2/<testcase-id>/<run-timestamp>/` and embed them in the bug Description under Actual result with clear labels. Do not store screenshots for routine testcase runs.
4. Read [`sheet-column-contract.md`](references/sheet-column-contract.md) before using the Round 2 test case sheet, and [`comparison-rules.md`](references/comparison-rules.md) before mapping or comparing fields. Apply the single status and Note contract in [`comparison-report-template.md`](assets/comparison-report-template.md): PASS requires every expected field to be mapped, comparable values to match, and explicit Expected result conditions to hold; use PARTIAL when mapped checks pass but an expected field is unmapped; use FAIL for a demonstrated mismatch; use BLOCKED when execution or comparison cannot be completed. Report blockers without inventing results.
5. Keep the comparison report in the structure defined by [`comparison-report-template.md`](assets/comparison-report-template.md). Update spreadsheet cells only when the user explicitly requests recording results and the live workbook contract authorizes those exact cells and values.

## Workbook intake

Read metadata first and use exact tab names: `Claude Task 2 Checklist-R2` for testcase intake and Actual/Note/Version updates, `Field compare` for mappings and field-status aggregation, and `Source` for organization/channel/source mappings. Verify the named tab exists before use. Match one unique testcase ID and read its full Prompt, Steps, Expected result, Channel, preconditions, and current organization/channel result cells. Resolve writable headers by exact text and check live validation before writing. If sign-in is needed, use the normal user-facing flow. If metadata or a required tab cannot be read, report the access issue; do not infer from another file.

## Boundaries

- The connector setup targets the Conative staging MCP endpoint and the organization the user chooses. Never choose an organization or grant OAuth access without the user's required confirmation of the live consent scope.
- Do not run a comparison as an implied consequence of connecting. A connection request alone authorizes setup and verification only.
- Do not write credentials, tokens, cookies, session state, or unnecessary customer data to reports, spreadsheets, prompts, logs, or evidence. Store project artifacts only in approved local or access-controlled destinations.
- This Skill does not cover Claude Code, general API comparison, or spreadsheet updates outside the explicitly requested and authorized Round 2 result workflow.


## End-to-end testcase execution

For a user-requested Round 2 execution from checklist intake through Claude, QE API, comparison, and result recording, follow [skill/execute-conative-round2-comparison/SKILL.md](skill/execute-conative-round2-comparison/SKILL.md). Unmapped expected fields may be skipped for field-level comparison, but any such field prevents PASS; use PARTIAL if the mapped checks otherwise pass. Use the same status and Note contract in the report and workbook.
## Field Compare status aggregation

When the user asks to aggregate completed testcase results into Product/Variant status cells on `Field compare`, follow [skill/record-conative-field-compare-status/SKILL.md](skill/record-conative-field-compare-status/SKILL.md). It attributes `FAILED` to specific fields using Root cause and field-level comparison evidence, rather than propagating a testcase-level failure to every compared field.
