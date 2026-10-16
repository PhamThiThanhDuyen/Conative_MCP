---
name: execute-conative-round2-comparison
description: Execute a requested Round 2 testcase end to end from checklist inspection through Claude and QE comparison and authorized result recording. Not for connector setup alone.
---

# Execute a Conative Round 2 Comparison

Run one user-selected testcase from the Claude Task 2 Checklist-R2 workbook through the exact Claude prompt, the matching QE API request, mapped-field comparison, and authorized result recording. Use the testcase Expected result as the comparison contract.

Before execution, read:

- ../../references/sheet-column-contract.md for row selection and allowed result cells.
- ../../references/comparison-rules.md for confirmed field and organization/source mappings.
- ../../assets/comparison-report-template.md for the report structure and Note format.
- ../access-claude-connect-org-success/SKILL.md when Claude needs connection or reconnection.
- references/workflow-details.md for the end-to-end operating steps.
- ../../../Conative MCP/execute-api-QE.md for the saved Postman requests and runtime inputs.
- ../../../Conative MCP/execute-compare-data-conative-MCP-with-QE.md for existing comparison and live-data guidance.

## Core workflow

1. Match the exact testcase ID to one unique row. Read Prompt, Expected result, Steps, preconditions, channel, and current organization-specific Actual/Note cells. Preserve the full Prompt verbatim.
2. Confirm the organization in the user instruction and live Claude/Postman context. Follow the connection skill if setup is required. Send only the exact Prompt once in Claude. Do not ask Claude to compose or create a query. Capture Claude's response and tool trace before proceeding.
3. After the Claude response is captured, run the corresponding read-only QE request once with inputs derived from the Prompt and approved mappings. Inspect the saved request and resolved runtime inputs first. Do not save collection edits.
4. Compare all relevant returned fields that have confirmed QE mappings. Skip unmapped fields; their presence alone does not block PASS. Apply exact numeric equality unless the testcase specifies a tolerance. Check explicit Expected result conditions.
5. Update only authorized Actual <org> and Note <org> cells when the user asks to record results. Use only a status allowed by the live cell validation. Each Note idea must be on its own line and begin with a hyphen and a space.
6. Read the cells back, confirm the workbook saved, and report the compared fields and any skipped unmapped fields.

If no mapped expected field remains, do not claim PASS or FAIL without comparable data. Use an allowed N/A/blocked status or leave the result unchanged and report the limitation. Do not invent mappings, alter prompts/expected results, change saved Postman requests, mutate business data, or edit other rows/cells.
