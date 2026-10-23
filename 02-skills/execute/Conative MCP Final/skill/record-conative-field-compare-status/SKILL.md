---
name: record-conative-field-compare-status
description: Aggregate completed Conative testcase Actual and Note results into Product/Variant status cells on the Field compare sheet, attributing failures only to the fields identified by Root cause or field-level mismatch evidence.
---

# Record Conative Field Compare Status

Use this skill when the user asks to summarize results already recorded in `Claude Task 2 Checklist-R2` into the `Field compare` sheet. This is a field-level aggregation workflow; it does not execute Claude prompts or QE API requests.

## Read the workbook and resolve exact columns

1. Use only the canonical native Google Sheet ID `1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ`; do not use an XLSX/XLSM copy. Read metadata and verify exact tabs `Claude Task 2 Checklist-R2` and `Field compare` exist. Resolve columns from live headers, not fixed positions.
2. In `Claude Task 2 Checklist-R2`, locate the exact `Actual <org> - <source>` and `Note <org> - <source>` headers for the requested organization and source. Match the complete header text. If either is missing or duplicated, stop without writing.
3. In `Field compare`, locate the exact `Status <org> - <source>` group and its `Product` and `Variant` subcolumns. Resolve the live columns and metric rows from their headers. If the target group, subheaders, or mapping row is ambiguous, stop and report it.
4. Read the mapping row fields, especially the Claude metric label and QE API field/path. For each checklist row, use the exact `Actual` and corresponding `Note` columns selected above. Do not use another organization's/source's result cells.
5. Read `references/sheet-column-contract.md`, `references/comparison-rules.md`, and `assets/comparison-report-template.md` when needed to resolve the workbook layout, metric mapping, or meaning of the Note fields.

## Match testcase fields and grain

- A testcase is relevant to a metric only when that metric appears in its `Compared field(s):` entry in the selected Note. Match the field's exact Claude label, QE API mapping, or an explicit equivalent stated in that entry. Do not match incidental mentions elsewhere in the note, such as channel scope or explanatory prose.
- Treat `pagination.total` as the `Total count` metric only when it is reported as a compared/count result. A mention marked as context, result count, or pagination metadata alone does not establish a Total count metric comparison.
- Determine Product versus Variant from the testcase's `Test Case` and full `Prompt`. Keep their outcomes separate. If the requested grain cannot be resolved, do not write a status for that case; report the ambiguity.
- A field can appear in either grain's testcase even if its label describes an identifier or title. Attribute it to the testcase's grain, as indicated by the prompt.

## Attribute failures per field

A testcase's overall `Actual = FAIL` does not make every field in `Compared field(s)` fail.

1. Read the testcase's `Root cause` and the field-level outcome in `Difference (Claude − QE API)` and `Expected result conditions`.
2. Mark a field as failed only when the Root cause attributes the discrepancy to that field. Use the Difference/expected-condition details to confirm which mapped field differs. A cause may describe the field semantically rather than repeat its exact API name, for example, a wrong variant label identifies the variant title/label field.
3. If a testcase compares several fields and the Root cause identifies one failing field, mark only that field `FAILED`. Treat other fields as passing only when the Note explicitly shows their values match or their expected condition passed.
4. If Root cause is `Unknown` but the Difference or expected-condition text uniquely identifies a mismatching field, mark only that demonstrably mismatching field `FAILED`; preserve `Unknown` as the cause and do not infer why it differs.
5. If a testcase is `FAIL` but no field-level mismatch can be attributed from Root cause and the comparison details, classify that testcase/field as unresolved. Do not mark every field failed and do not use unresolved evidence to claim `PASSED`.
6. For `Actual = PASS`, count a relevant field as passing only when it is included in `Compared field(s):` and the Note records that the comparison/condition passed. Ignore blank, blocked, or unrecognized Actual values; report them as unresolved rather than treating them as pass or fail.

## Aggregate and update statuses

For each metric and grain with at least one relevant testcase:

- Write `FAILED` if one or more relevant testcases demonstrate that this specific field failed.
- Write `PASSED` only when all relevant testcases for this field/grain are resolved as passing and none demonstrate a field-level failure.
- If any relevant testcase is unresolved and no demonstrated failure settles the status, leave the target status cell unchanged and report the unresolved testcase IDs.
- Do not change cells for a grain with no relevant testcase.

Before writing, read the target cells and live cell validation. Confirm the values `PASSED` and `FAILED` are allowed. Update only the target Product/Variant status cells. Do not modify mapping fields, prompts, or checklist Actual/Note values.

For each `FAILED` status cell, add a cell note containing the TC ID(s) that demonstrate failure for that field and grain. If several cases apply, list each distinct TC ID separated by line breaks. Read existing cell notes first: preserve unrelated note text; replace only notes previously written by this workflow when recalculating results. If a cell changes to `PASSED`, remove only a stale note that consists solely of TC IDs previously written by this workflow; preserve other notes.

Write status values and applicable notes in one batch where possible. Read every changed status and note back from the live sheet to verify the update. If validation, headers, mapping, or write permissions are ambiguous, do not write a partial update.

## Report

Summarize which Product/Variant statuses changed, the TC IDs responsible for each `FAILED` field, and any unresolved cases left untouched. State that testcase-level `FAIL` was not propagated to unrelated fields.
