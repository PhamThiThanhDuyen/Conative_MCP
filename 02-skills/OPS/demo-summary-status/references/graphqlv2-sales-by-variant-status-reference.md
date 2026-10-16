# GraphQL V2 — Sales by Variant Status Reference

## Source

- Workbook: [GraphQLV2](https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit)
- Tab: `Sales_by_variant` (sheet ID `1386744145`)
- Scope: field/configuration catalog and cross-tenant GraphQL/OPS verification status for the Sales by Variant response.

Use the linked tab as the source of truth for field names, API keys, types, implementation notes, and recorded verification outcomes. The sheet is a dated status matrix; its values should not be presented as current without checking the latest available snapshot.

## How to read the catalog

The first columns describe the response fields:

| Column | Meaning |
| --- | --- |
| ID | Field/reference ID where assigned. Blank IDs often indicate nested fields, unassigned fields, or placeholders. |
| Group | Functional area, such as Product information, Sales, AI, Marketing, or Inventory. |
| Name | Display label for the field. |
| Key | API/GraphQL key used for the field. |
| Type | Expected data type, when documented. |
| Priority (Neec confirm) | Priority/confirmation marker from the source sheet. Preserve the source value; confirm ambiguous values with the owner. |
| Status dev | Development status marker. |
| Fixed | Whether the source marks the field as fixed. |
| Metric group | Reporting/metric grouping. |
| Note | Field-specific implementation or data caveats. |
| Note ngày 14/01/2026 | Follow-up notes recorded for the January 14, 2026 check, often including ticket IDs. |

Columns to the right contain dated OPS and GraphQL comparisons for individual tenants/environments, with paired summary columns in some cases. Use the column heading (tenant/system and date) as the scope of each result. Do not combine results across tenants or dates.

## Status interpretation

Keep the exact status from the sheet when summarizing:

- `Passed`: the recorded check passed for that column's scope.
- `Failed`: the recorded check failed; consult the field's notes and related ticket references.
- `Failed of live`: the check is recorded as failing against live data.
- `Failed Live - Staging, Data - Live`: the sheet records a mismatch involving staging and live data; retain this distinction instead of shortening it to a generic failure.
- `Stuck`: the recorded check is stuck.
- `In testing`: the check is still in testing.
- `N/A` or blank: no applicable result or no recorded value; do not treat either as a pass.

A summary column may represent an aggregate/status for the preceding tenant or comparison. Read its header and values together rather than assuming every adjacent column is a summary.

## Examples of source notes

The inspected rows include notes about differences in category/vendor array lengths between staging and data service, null-versus-zero behavior for Compare At Price, stock-dependent differences, and references such as tickets 53483–53521. These are examples from the source sheet, not an exhaustive issue list. Preserve ticket IDs and the original meaning when carrying a note into a demo summary.

The sheet also contains field placeholders and repeated or blank IDs. Use the field name and API key alongside the ID to identify a row; do not assume IDs are unique or complete.

## Demo-summary guidance

When preparing a demo or status summary:

1. Identify the exact tenant/environment column and its snapshot date.
2. Report only the requested fields or groups.
3. Preserve status wording and distinguish `N/A`, blanks, and failures.
4. Include relevant row notes and ticket IDs when explaining a failure.
5. State the snapshot date. Do not describe an older snapshot as current/live status.
6. Link back to the workbook for verification.

## Snapshot caveat

The workbook metadata reports a large grid, while the tab itself is a multi-tenant status matrix with dated headings. This reference describes the visible structure and interpretation of the source tab; it does not replace refreshing or validating the underlying data.
