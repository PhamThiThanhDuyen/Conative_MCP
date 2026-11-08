# Determine affected organizations from current testcases

## Complete scan

1. Read canonical workbook metadata and both tabs' headers. Take the report's org/source scope from the Claude band in `Field compare`. Resolve every exact `Actual <org> - <source>` and `Note <org> - <source>` pair in `Claude Task 2 Checklist-R2`; never use another pair or the shared Bug ID column.
2. Read the bounded TC ID column and all selected Actual columns across their existing row bounds. Check unique TC IDs and retain scan coverage. Do not restrict the scan to FAILED Field compare cell notes: those are pointers, not an exhaustive testcase index.
3. Inspect the complete corresponding Note for every current `Actual = FAIL`. Resolve Note/Actual contradictions before claiming a current bug. PASS, blank, blocked, partial, on-hold, or unknown Actual values do not demonstrate a current failure, even when an old Note still has a ticket reference.

## Link failures to tickets

- Extract explicit Ticket OP IDs or explicit ticket links. Ignore N/A, None, dashes, parent-ticket IDs in explanatory text, and TC IDs. Discover candidate tickets from the complete testcase scan, not just a previous report.
- Read each candidate ticket's title and Actual/Expected details. Its org list may be incomplete; use it to understand the defect, not to limit org coverage.
- Search all current failing testcase Notes for the demonstrated failure behavior, including rows with blank/N/A Ticket OP. Compare the mapped field, failure mode, expected condition, and relevant grain/source/time/filter scope. Values can differ by organization; distinguish a comparable defect pattern from a different behavior on the same metric.
- Add an unlinked org only after the testcase independently demonstrates the same observed failure. Record `matched_tickets` with the ticket ID, exact ticket reference, and a concrete match reason. This establishes a report association, not a shared backend root cause. Preserve Unknown causes.
- Do not automatically attach a case already linked to a different ticket. Duplicate/related-ticket ambiguity needs review. A conflicting explicit Ticket OP link is unresolved: preserve the raw reference as an excluded ID with a limitation; do not silently reassign it.
- An unmapped catalog/behavior testcase can establish a bug association when its explicit expected condition fails; Product/Variant resolution is not required for the BUGS org list. Keep field-status counting separate.

## Output and limitations

Supply normalized testcase evidence using `input-schema.md`. The renderer derives each ticket's affected orgs from current failing cases; an old or blank Field compare status must not suppress a supported association. Keep the existing TỔNG QUAN/CHI TIẾT values unchanged and disclose such inconsistencies. Merge confirmed orgs across sources; display each ticket once. Keep TC IDs, source, link type, and match rationale in the working evidence for verification.

List current failures without a verified ticket as unlinked, not "no bugs". Missing scan access or ambiguous links make the bug scan incomplete; describe the exact gap. If a title is inaccessible, use `Chưa xác minh title`. Report-only work does not authorize ticket edits or checklist writeback.
