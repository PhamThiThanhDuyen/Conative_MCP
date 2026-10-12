---
name: execute-compare-data-conative-mcp-with-qe
description: Execute a spreadsheet-backed Conative MCP data coverage case by asking the connected Claude organization for the requested value, running the saved QE API request, comparing the data values, and recording the outcome in the requested Actual and Note cells.
---

# Execute and Compare Conative MCP Data with QE

## Purpose and boundary

Use this workflow to execute one **Claude Task 2 Checklist** data case, compare Claude's requested value with QE, and record the outcome for an organization. Value equality alone determines PASS or FAIL. Units, currency, dates, channel, filters, aggregation, and grain are context only. This workflow does not authorize new access, request edits, data mutations, or edits to other cases.

## Workflow

1. **Load the case.** Open the workbook and checklist sheet. Match the case ID, then read the row's title, preconditions, test data, steps, expected result, organization prompt, Actual, Note, and current values. Confirm organization-specific columns by header. If required details are ambiguous or missing, report the gap.
2. **Check access and environment.** Confirm Claude is connected to the requested organization and QE targets the intended environment. Follow repository security and live-data policies. Keep secrets and unnecessary customer data out of prompts, notes, and evidence. Pause for new access approval. Do not mutate live/customer data without required backup and restore gates.
3. **Read the QE request definition.** Follow `execute-api-QE.md` to inspect and run the saved Postman request. Note its query and environment; use this run's response as QE's value. Do not edit the request. If it cannot return the requested value, report the blocker rather than changing the query.
4. **Ask Claude the case prompt.** Submit the exact organization prompt using the existing Conative connector. Read the answer and available tool trace; allow only in-scope calls needed for the query. Capture Claude's value for the same requested field. Other metadata is context only.
5. **Compare values.** Identify the data field named or implied by the case prompt and compare Claude's value with QE's value. For numbers, ignore display separators and compare the numeric values exactly; use a tolerance only when the test case explicitly defines one. Ignore units and currency. Do not make status depend on date/time metadata, channel, filters, aggregation, grain, or other scope details. For text or categorical data, compare the corresponding value for the same requested field. Record any visible context differences as observations, not as a reason to fail.
6. **Determine status.** Use `PASS` when Claude's requested data value equals QE's value. Use `FAIL` when both values are available and differ. If Claude's value cannot be obtained or the QE request fails, follow the workbook's allowed blocked/not-run status; if none is available, leave the status cell unchanged and report the blocker. HTTP success alone is not a pass. Do not overwrite an existing result unless the user asks to rerun or update it.
7. **Record the result and evidence.** Write the exact status token into the requested organization's Actual cell. For every completed comparison, including PASS, write a concise evidence note in that row's organization-specific Note cell. Include the metric/field, Claude value, QE value, equality or difference, QE request status, and relevant query context such as channel, filter, date range, and timezone when available. For FAIL, clearly state both values and the mismatch. Units and scope details may be recorded as context but do not affect status. Keep secrets and unnecessary customer data out of cells. If execution is blocked or a value is missing, leave the status unchanged when no allowed blocked/not-run token exists, and report the blocker in chat; do not write an evidence note that implies a completed comparison. Do not edit prompts, expected results, request definitions, or neighboring rows.
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
