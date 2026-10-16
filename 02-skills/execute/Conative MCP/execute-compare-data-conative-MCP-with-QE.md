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
3. **Ask Claude the case prompt.** Submit the exact organization prompt using the existing Conative connector. Read the answer and available tool trace; allow only in-scope calls needed for the query. Capture Claude's value for the same requested field and its timerange before proceeding. Other metadata is context only.
4. **Read and run the QE request.** After capturing Claude's answer, follow `execute-api-QE.md` to inspect and run the saved Postman request. Note its query and environment; use this run's response as QE's value. Do not edit the request. If it cannot return the requested value, report the blocker rather than changing the query.
5. **Compare values.** Identify the data field named or implied by the case prompt and compare Claude's value with QE's value. For numbers, ignore display separators and compare the numeric values exactly; use a tolerance only when the test case explicitly defines one. Ignore units and currency. Do not make status depend on date/time metadata, channel, filters, aggregation, grain, or other scope details. For text or categorical data, compare the corresponding value for the same requested field. Record any visible context differences as observations, not as a reason to fail.
6. **Determine status.** Use `PASS` when Claude's requested data value equals QE's value. Use `FAIL` when both values are available and differ. If Claude's value cannot be obtained or the QE request fails, follow the workbook's allowed blocked/not-run status; if none is available, leave the status cell unchanged and report the blocker. HTTP success alone is not a pass. Do not overwrite an existing result unless the user asks to rerun or update it.
7. **Record the result and evidence.** Write the exact status token into the requested organization's Actual cell. For every completed comparison, including PASS, write the following five-line template in that row's organization-specific Note cell. Replace `<name field>` with the requested field name and each placeholder with the value returned by that source:

   ```text
   - QE return <name field> = <data return in QE>
   - Claude return <name field> = <data return in Claude>
   - Difference = <data return in QE> - <data return in Claude>
   - Timerange return in Claude = <Claude timerange>
   - Root cause (if failed): <root cause or N/A>
   ```

   Calculate Difference as QE minus Claude for numeric values. For matching text or categorical values, state that they match rather than inventing a numeric difference. Include the requested field name with its value. Use the timerange Claude returned; if Claude gives no timerange, write `Not stated`. For PASS, write `N/A` on the Root cause line. For FAIL, describe the cause only when supported by evidence; otherwise write `Unknown`. Every nonempty line must begin with `- `. If any line contains a semicolon, split immediately after each semicolon, keeping it at the end of the preceding line and starting the next segment with `- `. Keep secrets and unnecessary customer data out of cells. If execution is blocked or a value is missing, leave the status unchanged when no allowed blocked/not-run token exists, and report the blocker in chat; do not write an evidence note that implies a completed comparison. Do not edit prompts, expected results, request definitions, or neighboring rows.
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
