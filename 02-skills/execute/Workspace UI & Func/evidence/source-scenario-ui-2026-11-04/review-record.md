# Scenario_UI source update — 2026-11-04

Source: user instruction in the current chat: thay nguồn test case thành sheet Scenario_UI.
Author: Codex. Classification: behavioral (default testcase source). Decision: draft / needs-review; no installation, publication, or approval promotion.

Updated root skill, testcase intake, execution flow, source index and sheet column contract to use Scenario_UI in the existing Workspace workbook. ReportConative and Prompt remain supporting sources. Preserved the previous source name as history; removed its gid from the current source link. Scenario_UI gid, headers and validation have not been verified live and must be resolved from metadata before use.

## Baseline and validation

- Root size baseline: PASS, 225 words / 23 lines; after: PASS, 223 words / 23 lines.
- Intake size baseline: PASS, 251 words / 11 lines; after: PASS, 266 words / 11 lines. No warnings or failures.
- OpenAI quick validator could not run because the available Python runtime lacks PyYAML; frontmatter was unchanged.
- Changes are limited to the five files listed above; no script or API behavior changed. Existing Markdown link targets were preserved except the old testcase gid link, now a workbook link pending metadata resolution.
- Offline walkthrough, normal: with Scenario_UI available, intake selects that tab and reads its actual headers before bounded TC lookup.
- Offline walkthrough, missing input: an unverified gid/header cannot be filled with the former TC_Gen Report UI gid/columns; read live metadata and report an unresolved source if necessary. An explicitly requested alternative tab remains supported.
- Walkthrough is self-evaluation, not live end-to-end evidence or independent reviewer approval. No Google Sheet, testcase run, QE request or DevTak ticket was changed.

Qualified reviewer/content owner review remains pending before promotion under the repository change-approval policy.
