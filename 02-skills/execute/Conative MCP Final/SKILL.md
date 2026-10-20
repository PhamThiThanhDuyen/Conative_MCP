---
name: conative-mcp-final
description: Connect the Claude app to the Conative MCP staging connector for a user-selected organization, then run and document an explicitly requested Round 2 Claude versus QE API comparison. Use for Conative MCP setup and comparison work in this skill package; do not use for Claude Code or unrelated MCP/API work.
---

# Conative MCP Final

## Workflow

1. Check the in-app browser for Claude. If no Claude tab is open, open https://claude.ai in a visible in-app browser tab and inspect the page; a missing tab is not a blocker. If sign-in is required, let the user complete it. For a new or expired Conative connection, follow [`access-claude-connect-org-success/SKILL.md`](skill/access-claude-connect-org-success/SKILL.md) when that file is available. Confirm the live consent scope with the user before granting access. Do not begin a comparison until Claude visibly reports connected to the user's selected organization.
2. Open Postman browser in app and follow [`execute-api-QE.md`](execute-api-QE.md) to run signIn and chooseOrg, target the exact organization, derive source and date inputs, select productList for product prompts or variantList for variant prompts, inspect the current request body, and run once. Resolve `from_source` using the exact value in the approved mapping (for example, `shopify`, not a display label such as `Shopify Conative`). Build an unsaved request-local body overlay: omit a saved active-status filter unless the prompt explicitly asks for active status, and preserve other filters. Apply derived inputs only for this run; do not save request or environment changes. Keep credentials and tokens ephemeral; do not save collection edits or expose them in notes/evidence. Capture the returned response fields, status, date range, timezone, source/channel scope, filters, grain, and visible warnings as useful context.
3. Run a data comparison only when the user requests one. Identify the exact test case ID; if not supplied, ask for it. Use the existing Claude comparison workflow at `../../Conative MCP/execute-compare-data-conative-MCP-with-QE.md` and the QE API steps in [`execute-api-QE.md`](execute-api-QE.md).
4. Read [`sheet-column-contract.md`](references/sheet-column-contract.md) before using the Round 2 test case sheet, and [`comparison-rules.md`](references/comparison-rules.md) before mapping or comparing fields. Apply the single status and Note contract in [`comparison-report-template.md`](assets/comparison-report-template.md): PASS requires every expected field to be mapped, comparable values to match, and explicit Expected result conditions to hold; use PARTIAL when mapped checks pass but an expected field is unmapped; use FAIL for a demonstrated mismatch; use BLOCKED when execution or comparison cannot be completed. Report blockers without inventing results.
5. Keep the comparison report in the structure defined by [`comparison-report-template.md`](assets/comparison-report-template.md). Update spreadsheet cells only when the user explicitly requests recording results and the live workbook contract authorizes those exact cells and values.

## Workbook access without asking the user to paste rows

- First use the connected Google Drive/Sheets tools for the source workbook. If the file is an Office workbook (for example `.xlsm`) and native Sheets range tools reject it, do not ask the user to copy/paste the testcase row yet.
- Use an already-open in-app browser tab for the workbook when one exists. If none exists, open the workbook URL from the source contract in a visible in-app browser tab; do not treat the absence of a pre-opened tab as an access failure. If the URL is unavailable, locate the named workbook through Drive before asking the user for a link.
- Read the Office workbook through its visible browser UI as a read-only source. Find the exact worksheet tab and testcase ID using the visible UI. Read the entire selected row needed by the workflow: TC ID, Channel, Test Case, preconditions, full Prompt, Steps, Expected result, and organization-specific Actual/Note/Version cells. Record no changes during intake.
- Navigate by the sheet name box or the sheet's visible Find UI, then inspect each relevant cell's displayed/formula-bar value. Do not infer row contents from neighboring cases or previously observed samples. Confirm the ID appears exactly once on the selected worksheet.
- If opening the workbook requires sign-in, use the normal user-facing sign-in flow without handling passwords, OTPs, or secrets for the user. If the browser cannot access the workbook after opening it, report the specific access error and ask for access repair or the exact row contents. Never convert, replace, or edit the source workbook just to make it readable.
- A user-provided testcase ID, organization, and execution request are sufficient to begin intake. Do not ask the user to restate workbook data that is available in the open browser. Ask only for missing information that is not available from the workbook or live app state, or for confirmation that a separate workflow explicitly requires.

## Boundaries

- The connector setup targets the Conative staging MCP endpoint and the organization the user chooses. Never choose an organization or grant OAuth access without the user's required confirmation of the live consent scope.
- Do not run a comparison as an implied consequence of connecting. A connection request alone authorizes setup and verification only.
- Do not write credentials, tokens, cookies, session state, or unnecessary customer data to reports, spreadsheets, prompts, logs, or evidence. Store project artifacts only in approved local or access-controlled destinations.
- This Skill does not cover Claude Code, general API comparison, or spreadsheet updates outside the explicitly requested and authorized Round 2 result workflow.


## End-to-end testcase execution

For a user-requested Round 2 execution from checklist intake through Claude, QE API, comparison, and result recording, follow [skill/execute-conative-round2-comparison/SKILL.md](skill/execute-conative-round2-comparison/SKILL.md). Unmapped expected fields may be skipped for field-level comparison, but any such field prevents PASS; use PARTIAL if the mapped checks otherwise pass. Use the same status and Note contract in the report and workbook.
