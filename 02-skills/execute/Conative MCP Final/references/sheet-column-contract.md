# Round 2 Test Case Sheet Contract

## Source inspected

- I allow access and open browser-in-app this google sheet https://docs.google.com/spreadsheets/d/1fNGCNLP8LXFuNxhuzPbXGQEu1uanFLeO/edit?gid=2109707194#gid=2109707194 (`Claude Task 2 Checklist-R2` sheet)

## Column map

Headers are on row 1, columns A:O. Use the exact header text; do not depend on column position if headers are present.

| Column | Exact header | Contract |
|---|---|---|
| A | `TC ID` | Testcase key. Read-only; select a row by exact, unique ID. |
| B | `Nhóm` | Testcase group/category. Read-only. |
| C | `Channel` | Channel/scope value. Read-only. |
| D | `Test Case` | Short testcase description. Read-only. |
| E | `Điều kiện trước` | Preconditions, including any organization context. Read-only. |
| F | `Prompt` | Prompt to send to Claude. Read the full cell value exactly, including line breaks or repeated prompts; do not rewrite or infer missing text. |
| G | `Steps` | Test instructions. Read-only. |
| H | `Expected result` | Expected behavior/result. Read-only. |
| I | `Priority` | Test priority. Read-only. |
| J | `Actual Melinda` | Organization-specific status output for `Melinda` under the user's result-update workflow. Write `PASS` or `FAIL` only when the live cell validation/workbook contract permits that token. Do not assume this column exists for another organization. |
| K | `Note Melinda` | Note field named for organization `Melinda`. Do not write here unless the user explicitly authorizes the target cell and the approved note format is known. |
| L | `Evidence ChatGPT` | ChatGPT evidence reference. Read-only unless separately authorized. |
| M | `Evidence Claude` | Claude evidence reference. Read-only unless separately authorized. |
| N | `So sánh / Kết luận` | Comparison/conclusion field. This is not a separately named status column. Read-only unless separately authorized. |
| O | `Bug ID` | Bug reference. Read-only unless separately authorized. |

The inspected sheet does not have a column explicitly named `QE API result`, `Claude result`, or `Status`. For the user's result-update workflow, `Actual <org name>` is the status destination and `Note <org name>` carries the comparison details; `Actual Melinda` and `Note Melinda` are the only such organization-specific headers observed on this tab. `PASS` and `FAIL` are the comparison-rule tokens, but the live cell validation/allowed values were not verified during this inspection. Confirm that the selected cell permits the token before writing. Before working for a different organization, inspect the live headers and identify its matching columns; do not assume `Melinda` columns apply.

## Observed testcase coverage

The inspected tab included testcase IDs `T2-COV-001` through `T2-COV-008` and `T2-COV-026`. Their categories cover product/variant aggregate and top-list prompts, no-data and unsupported-field cases, completeness/repeatability checks, and a brand breakdown case. This is an observed sample, not a promise that these are the only rows or IDs in the workbook.

For testcases `T2-COV-001` through `T2-COV-008`, the prompts are in column F. `T2-COV-008` has two repeated requests in its prompt cell; preserve and execute both as written when that testcase is selected. `T2-COV-026` includes organization context in its precondition and a comparison prompt; use its full prompt cell and respect that row's stated context.

## Row selection and use

- Ask the user for the exact testcase ID when it has not already been selected. Match it in `TC ID`; if it is missing or not unique, stop and clarify.
- Read the selected row's `Prompt` (F), `Channel` (C), `Điều kiện trước` (E), and any other needed case instructions before running it. Prompt-specific values take precedence over assumptions; never invent dates, channels, organizations, or metrics.
- Keep the workbook read-only when using it as an input to Claude or Postman. A request to execute a testcase does not by itself authorize editing the workbook; use the result-update Skill only when the user requests recording a completed comparison.
- Before updating, verify the organization-specific target headers, exact row, current cell contents, allowed status tokens, and write scope. Write status to `Actual <org name>` and details to `Note <org name>` only. Do not overwrite an existing result without explicit rerun/update direction.
- The workbook's owner, approved writable columns, allowed status tokens, and evidence-storage policy were not established by this inspection and remain unconfirmed.

## Credential and data handling

Never write credentials, tokens, cookies, or session state into cells, notes, evidence links, or prompts. Keep only the minimum project data needed for the approved workflow and follow `../../../../03-knowledge/governance/information-security-policy.md`.
