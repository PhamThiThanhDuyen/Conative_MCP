# Round 2 Google Sheet Contract

## Canonical source and tabs

- Use only the native Google Sheet [MCP_Conative_Task2_DataCoverage_Checklist_Final](https://docs.google.com/spreadsheets/d/1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ/edit), spreadsheet ID `1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ`.
- This is the sole testcase and result workbook until the user explicitly replaces it. Do not use XLSX/XLSM copies, including older exports or similarly named workbooks.
- Resolve workbook metadata before reading or writing. Use exact tab names: `Claude Task 2 Checklist-R2` for testcase prompts and result cells; `Field compare` for field mappings/status aggregation; `Source` for organization/channel/source mappings. These tabs were verified in the canonical file.
- Read testcase rows only from `Claude Task 2 Checklist-R2`. Match the exact `TC ID` once and read the complete row contract, including Prompt and Expected result. Write completed results to that testcase's organization/channel-specific columns on the same tab.
- Use `Field compare` and `Source` only for their stated mapping purposes. Re-read current values from this same workbook when the relevant mapping or source scope is needed.

## Observed header and result columns

Headers are on row 1 of `Claude Task 2 Checklist-R2`. The current live header row includes:

| Column | Exact header | Contract |
|---|---|---|
| A | `TC ID` | Exact testcase key; read-only. Select one unique row. |
| B | `Nhóm` | Testcase group/category; read-only. |
| C | `Channel` | Channel/scope; read-only. |
| D | `Test Case` | Short testcase description; read-only. |
| E | `Điều kiện trước` | Preconditions; read-only. |
| F | `Prompt` | Full prompt to send verbatim; read-only. |
| G | `Steps` | Test instructions; read-only. |
| H | `Expected result` | Comparison contract; read-only. |
| I | `Priority` | Priority; read-only. |
| O | `Actual Chanluu - Shopify` | Observed status destination for Chanluu/Shopify. |
| P | `Note Chanluu - Shopify` | Observed detailed comparison note for Chanluu/Shopify. |
| Q | `Version Chanluu - Shopify` | Observed run date/time destination for Chanluu/Shopify. |
| R | `Evidence ChatGPT` | Do not write unless separately authorized. |
| S | `Evidence Claude` | Do not write unless separately authorized. |
| T | `So sánh / Kết luận` | Do not write unless separately authorized. |
| U | `Bug ID` | Do not write unless separately authorized. |

The header read also showed Melinda Shopify and Nuorder Actual/Note/Version columns. For any organization/channel, resolve the exact complete headers from the live header row; never assume fixed positions or write to a nearby organization/channel's columns. The Chanluu/Shopify headers above are observed in this file, but verify them and live validation before each result update.

## Read, write, and version rules

- Read `TC ID`, `Channel`, `Test Case`, `Điều kiện trước`, the full `Prompt`, `Steps`, `Expected result`, and the selected organization's current result cells before execution.
- A user-provided testcase ID, organization, and execution request authorize testcase intake. Do not ask the user to repeat row data already present in the canonical Sheet.
- Before writing, verify the exact row, organization/channel, current contents, exact Actual/Note/Version headers, write scope, and live validation. Write the three result cells together. If any required header or permission is missing/ambiguous, write none.
- Use only status tokens allowed by the live cell validation. Do not overwrite existing results unless the user explicitly requested rerun/update.
- Each Note line begins `- ` and follows `assets/comparison-report-template.md`. Do not imply a completed comparison when blocked.
- Format Version as `MMM d, yyyy hh:mm AM/PM`, using Asia/Ho_Chi_Minh local execution time (example: `Oct 22, 2026 04:09 PM`).
- Read the three cells back and confirm the Google Sheet saved before moving to the next testcase.
- Save evidence screenshots only when the user requests bug creation. Then follow the bug workflow; routine test execution does not create screenshot files.

## Credential and data handling

Never write credentials, tokens, cookies, or session state into cells, notes, evidence links, or prompts. Follow `../../../../03-knowledge/governance/information-security-policy.md`.
