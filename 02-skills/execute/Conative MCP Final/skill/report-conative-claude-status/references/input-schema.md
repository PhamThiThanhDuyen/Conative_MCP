# Normalized report input

Build the snapshot from live connector reads after resolving headers. Each grain array contains one status for every named Claude field row in scope, in sheet order. Use exact PASSED/FAILED tokens; blank cells become "" or null. Exclude API-only rows with no Claude label. Missing reads are errors, not empty arrays or NOT RUN results.

```json
{
  "organizations": [
    {"name": "Org A", "sources": [
      {"name": "Shopify", "product": ["PASSED", ""], "variant": ["PASSED", null]}
    ]}
  ],
  "bugs": [{"id": "12345", "title": "Verified ticket title"}],
  "testcases": [
    {
      "org": "Org A", "source": "Shopify", "tc_id": "T2-COV-001",
      "actual": "FAIL", "ticket_ids": ["12345"],
      "failure_evidence": "Current Note demonstrates the mapped count mismatch."
    }
  ],
  "limitations": [],
  "bug_scan_complete": true
}
```

`organizations` must be nonempty. Org names and source names within their org must be unique. Both grain arrays must exist and have equal length. An empty array is valid only for a verified zero-field scope.

`bugs` is the ticket-title catalog, not the affected-org list. IDs are decimal OP IDs, optionally prefixed with #. A null title becomes `Chưa xác minh title`; conflicting verified titles require investigation. Referenced IDs missing from the catalog still appear with an unverified title. Catalog-only tickets with no current failing testcase are omitted.

`testcases` is required. Include every current FAIL found by the complete Actual-column scan; PASS/other rows may also be supplied to demonstrate that old references are excluded. Each `(org, source, tc_id)` must be unique and within the report scope. FAIL records require concrete `failure_evidence` from the corresponding current Note. `ticket_ids` contains only explicit IDs read there; it is not a guess based on the metric or ticket title.

For a verified same-defect case with no explicit ticket, add:

```json
"matched_tickets": [{
  "ticket_id": "12345",
  "ticket_reference": "https://devtak.cbidigital.com/work_packages/12345",
  "reason": "Ticket Actual/Expected and this testcase demonstrate the same specific failure behavior and compatible scope."
}]
```

The agent must verify the semantic match using `bug-evidence.md`; the renderer only validates evidence structure. It rejects a match to a different ticket when the testcase already contains an explicit ticket reference.

For an explicit link that conflicts with the observed defect, keep its ID in `ticket_ids`, also list it in `excluded_ticket_ids`, and supply a precise `limitation`. Excluded IDs do not determine affected orgs. Set `bug_scan_complete: false` until the ambiguity is resolved.

The renderer derives ticket orgs from accepted FAIL records, independent of Field compare's rollup. A legacy `bugs[].orgs`, if present, is ignored. Existing inputs must add `testcases` evidence before regeneration. Unlinked current failures and conflicting field summaries are disclosed as limitations.

`bug_scan_complete` is explicit; false requires a precise entry in `limitations` or a testcase limitation. Use false for unreadable or ambiguous org/source Actual/Note columns, incomplete row coverage, or unresolved links. N/A Ticket OP is a verified absence of a link, not proof of no bug. Keep scratch files local and return the user's report format; do not create another Sheet, Page, ticket, or message destination.
