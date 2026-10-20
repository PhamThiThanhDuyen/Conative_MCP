# Round 2 Test Case Sheet Contract

## Source inspected

- I allow access and open browser-in-app this google sheet https://docs.google.com/spreadsheets/d/1fNGCNLP8LXFuNxhuzPbXGQEu1uanFLeO/edit?gid=2109707194#gid=2109707194 (`Claude Task 2 Checklist-R2` sheet)

## Column map

Headers are on row 1. The sheet's note columns are scoped by both organization and channel; use the exact header text and do not depend on column position when headers are present. The observed A:O map below is the previously inspected layout and may be stale after the sheet structure update.

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
| J | `Actual Melinda` | Organization-specific status output for `Melinda` under the user's result-update workflow. Write only the applicable `PASS`, `FAIL`, `PARTIAL`, or `BLOCKED` token when live cell validation/workbook contract permits it. Do not assume this column exists for another organization. |
| K | `Note Melinda` | Previously observed organization-level note field. It does not identify a channel and is not a valid destination when the sheet provides a channel-specific note header. |
| L | `Evidence ChatGPT` | ChatGPT evidence reference. Read-only unless separately authorized. |
| M | `Evidence Claude` | Claude evidence reference. Read-only unless separately authorized. |
| N | `So sánh / Kết luận` | Comparison/conclusion field. This is not a separately named status column. Read-only unless separately authorized. |
| O | `Bug ID` | Bug reference. Read-only unless separately authorized. |

The inspected sheet does not have a column explicitly named `QE API result`, `Claude result`, or `Status`. For the user's result-update workflow, `Actual <org name>` is the status destination. Note headers follow `Note <org name> - <channel name>` and carry comparison details for that specific organization-channel pair. Version headers must match `Version <org name> - <channel name>` and store the execution date. A single organization may have multiple channels, so never write to a generic organization-only Note or Version column when channel-specific headers are present. `Note Melinda` above records the prior observed structure only; verify current live headers before writing and select exact Note and Version headers whose organization and channel both match the selected testcase. Match complete header strings, including spelling and spacing; do not use partial matches. If a required exact header is absent or duplicated, stop and clarify rather than choosing a nearby column. The comparison contract defines `PASS`, `FAIL`, `PARTIAL`, and `BLOCKED`; live cell validation/allowed values were not verified during the prior inspection. Confirm that the selected status cell permits the applicable token before writing. Do not infer channel from organization: take it from the selected testcase's `Channel` cell and confirm its organization context from the testcase/preconditions or user instruction.

## Observed testcase coverage

The inspected tab included testcase IDs `T2-COV-001` through `T2-COV-008` and `T2-COV-026`. Their categories cover product/variant aggregate and top-list prompts, no-data and unsupported-field cases, completeness/repeatability checks, and a brand breakdown case. This is an observed sample, not a promise that these are the only rows or IDs in the workbook.

For testcases `T2-COV-001` through `T2-COV-008`, the prompts are in column F. `T2-COV-008` has two repeated requests in its prompt cell; preserve and execute both as written when that testcase is selected. `T2-COV-026` includes organization context in its precondition and a comparison prompt; use its full prompt cell and respect that row's stated context.

## Row selection and use

- Ask the user for the exact testcase ID when it has not already been selected. Match it in `TC ID`; if it is missing or not unique, stop and clarify.
- Read the selected row's `Prompt` (F), `Channel` (C), `Điều kiện trước` (E), and any other needed case instructions before running it. Prompt-specific values take precedence over assumptions; never invent dates, channels, organizations, or metrics.
- Keep the workbook read-only when using it as an input to Claude or Postman. A request to execute a testcase does not by itself authorize editing the workbook; use the result-update Skill only when the user requests recording a completed comparison.
- Before updating, verify the exact testcase row, organization, `Channel` value, current contents, allowed status tokens, write scope, and exact `Actual <org>`, `Note <org> - <channel>`, and `Version <org> - <channel>` headers. Write the status, canonical Note, and execution date together. Format the Version date as `MMM d, yyyy` (example: `Oct 16, 2026`) using the run's stated timezone. Treat these as one update: if any required header or write permission is missing or ambiguous, do not write a partial result. Do not overwrite an existing result without explicit rerun/update direction.
- The workbook's owner, approved writable columns, allowed status tokens, and evidence-storage policy were not established by this inspection and remain unconfirmed.

## Credential and data handling

Never write credentials, tokens, cookies, or session state into cells, notes, evidence links, or prompts. Keep only the minimum project data needed for the approved workflow and follow `../../../../03-knowledge/governance/information-security-policy.md`.
