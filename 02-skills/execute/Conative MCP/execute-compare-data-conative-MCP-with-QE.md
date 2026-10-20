---
name: execute-compare-data-conative-mcp-with-qe
description: Execute a spreadsheet-backed Conative MCP data coverage case by asking the connected Claude organization for the requested value, running the saved QE API request, comparing the data values, and recording the outcome in the requested Actual and Note cells.
---

# Execute and Compare Conative MCP Data with QE

## Purpose and boundary

Use this workflow to execute one **Claude Task 2 Checklist** data case, compare Claude's requested value with QE, and record the outcome for an organization. Value equality alone determines PASS or FAIL. Units, currency, dates, channel, filters, aggregation, and grain are context only. This workflow does not authorize new access, request edits, data mutations, or edits to other cases.

## Workflow

1. **Load the case.** Open the workbook and checklist sheet. Match the case ID, then read the row's title, preconditions, test data, steps, expected result, organization prompt, Actual, Note, Version, and current values. Confirm organization-specific columns by exact header. If required details are ambiguous or missing, report the gap.
2. **Check access and environment.** Confirm Claude is connected to the requested organization and QE targets the intended environment. Follow repository security and live-data policies. Keep secrets and unnecessary customer data out of prompts, notes, and evidence. Pause for new access approval. Do not mutate live/customer data without required backup and restore gates.
3. **Ask Claude the case prompt.** Submit the exact organization prompt using the existing Conative connector. Read the answer and available tool trace; allow only in-scope calls needed for the query. Capture Claude's value for the same requested field and its timerange before proceeding. Other metadata is context only.
4. **Read and run the QE request.** After capturing Claude's answer, follow `execute-api-QE.md` to inspect and run the saved Postman request. Note its query and environment; use this run's response as QE's value. Do not edit the request. If it cannot return the requested value, report the blocker rather than changing the query.
5. **Compare values.** Identify every expected field named or implied by the case prompt and compare available Claude and QE values using confirmed mappings. For numbers, ignore display separators and compare exactly; use a tolerance only when the testcase explicitly defines one. Do not convert units or currency. Check explicit Expected result conditions. Compare like-for-like scope and record scope differences; do not silently alter queries. Skip fields without a confirmed mapping, but an unmapped expected field prevents PASS.
6. **Determine status.** Use the canonical status rules and Note format in `../Conative MCP Final/assets/comparison-report-template.md`. `FAIL` applies to a demonstrated mapped-value mismatch or an explicitly unmet Expected result condition. `BLOCKED` applies when required values are unavailable, a request fails, scope/rules are unresolved, or no expected field remains comparable. `PARTIAL` applies when mapped checks are complete and otherwise pass but an expected field is unmapped. `PASS` requires every expected field to be mapped, all values to match, and every explicit Expected result condition to hold. A demonstrated failure takes precedence over other limitations. Use only tokens permitted by live workbook validation; otherwise leave cells unchanged and report the limitation. Do not overwrite existing results unless the user asks to rerun or update them.
7. **Record the result and evidence.** When the user requests recording, update the exact authorized `Actual <org>`, `Note <org> - <channel>`, and `Version <org> - <channel>` cells together. Write the execution date to Version as `MMM d, yyyy` (example: `Oct 16, 2026`) using the run's stated timezone. Use the single Note format in `../Conative MCP Final/assets/comparison-report-template.md` for PASS, FAIL, PARTIAL, and BLOCKED. Every numeric Difference is Claude − QE API. If a required header or write permission is missing or ambiguous, do not write a partial result; report the blocker. Read all updated cells back and verify the workbook saved. Keep secrets and unnecessary customer data out of cells. Do not edit prompts, expected results, request definitions, or neighboring rows.
8. **Verify and report.** Read back the edited cells and confirm the workbook saved. Report case ID, organization, status, cell addresses, compared values, and relevant context. Link the workbook and Claude/Postman evidence when available.

## Evidence and failure handling

- Keep reproducible evidence: prompt source, QE query/status/value/warnings, Claude answer/trace, compared values, and edited cells.
- Preserve the original failed observation; do not rerun repeatedly until a green result appears. A rerun is a new attempt and must use its own current Claude and QE outputs.
- If Claude cannot access the organization, the QE request fails, or either requested value is missing, state the blocker. Do not fabricate a result or a root cause.
- If the workbook is an Office file opened in a browser, use the visible workbook interface or an approved file reader/editor. Do not convert or replace the source file.

## Related guidance

- QE request discovery and execution: `execute-api-QE.md`.
- Spreadsheet case execution, result status mapping, security, and saved-cell verification: `SKILL.md` in this directory.
- Repository security and live-data policy: `../../03-knowledge/governance/information-security-policy.md` and `../../03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`.
