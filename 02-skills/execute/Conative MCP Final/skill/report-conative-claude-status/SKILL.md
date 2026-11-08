---
name: report-conative-claude-status
description: Report Claude field-comparison status for Conative organizations and sources from the canonical Field compare sheet, with Product/Variant counts and deduplicated OP bug references. Use for reporting existing results, not executing tests or updating status cells.
---

# Report Conative Claude Status

Produce a Vietnamese report with exactly three top-level sections: `TỔNG QUAN`, `CHI TIẾT`, and `BUGS`, using [the report template](assets/report-template.md).

## Source and scope

Use native Google Sheet `1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ`, tab `Field compare`. Read live metadata and headers first. Resolve the `Claude` column band, each organization/source group, and its `Product`/`Variant` subcolumns; exclude `Codex (ChatGPT)`. Preserve live names and order, including groups without a `Status` prefix. Default to every group in the Claude band unless the user limits scope. Do not infer organizations outside that band.

Count each row with a nonblank Claude field label once per source and grain, including unmapped labels. Read the label from the live field header (`Field` or `Claude`) and its QE API mapping; exclude API-only rows with no Claude label. Resolve columns by headers, not fixed letters. Duplicate labels, conflicting groups, or ambiguous grain require a scoped limitation rather than guessed totals.

## Counting and rollup

- `PASSED` becomes report `PASS`; `FAILED` becomes `FAIL`.
- In both TỔNG QUAN and CHI TIẾT, display source FAIL as `🔴 FAIL` and source PASS as `🟢 PASS`. Keep `NOT RUN` neutral. These markers affect presentation only; preserve status tokens, counts, organization labels, and bug records.
- For each Product/Variant: `TOTAL = PASS count + FAIL count`. These are recorded field statuses, not testcase counts or all supported fields.
- Report blank cells separately as `CHƯA CÓ STATUS`; do not infer untested, blocked, inapplicable, PASS, or FAIL. Report other nonblank tokens separately as unrecognized; they do not contribute to TOTAL.
- Source: any FAILED cell means `FAIL`; otherwise at least one PASSED means `PASS`; otherwise `NOT RUN`.
- ORG: any source FAIL means `FAIL`; otherwise at least one source PASS means `PASS`; otherwise `NOT RUN`. Retain every source, including NOT RUN sources. PASS describes recorded results and does not assert complete coverage.
- Show PASS and FAIL count lines when their count is positive; show both when both occur. If TOTAL is zero, show `NOT RUN`. Keep Product and Variant separate.

## Bugs

Follow [the bug evidence workflow](references/bug-evidence.md). Scan the complete `Claude Task 2 Checklist-R2` testcase population for every selected organization/source, resolving exact Actual/Note columns. Current testcase results determine affected organizations; ticket titles/descriptions and Field compare notes may omit organizations.

Use current `Actual = FAIL` plus the corresponding Note as failure evidence. Search every organization's testcases for each ticket's demonstrated failure behavior, including cases with no Ticket OP reference. Confirm matching behavior and relevant scope from Actual/Expected, Difference, and Root cause; a shared metric alone does not establish the same defect. Keep ambiguous matches unresolved. Do not count stale ticket references on PASS, blank, blocked, or unresolved cases.

Read ticket titles and failure details through available read-only OP access or exact verified records. Build normalized `testcases` evidence, explicit ticket links, and confirmed defect matches; the renderer derives each ticket's ORG list from those cases. An organization can be affected even when its Field compare status is blank or PASS. Preserve the field-status summary and mark stale/conflicting evidence as a limitation. Do not change Sheets or tickets during reporting.

## Produce and verify

Read [input and evidence rules](references/input-schema.md), build the normalized snapshot, and run `python3 scripts/build_report.py INPUT.json --output REPORT.md` in an approved local scratch directory. Return the report in chat unless the user requests a saved artifact. Link the canonical workbook and identify the read time in local Vietnam time in the report introduction.

Check totals, both levels of rollup, source/grain isolation, bug deduplication, and unresolved evidence. This workflow reads existing statuses; it does not run Claude/QE, write Sheets, create bugs, or send the report elsewhere. For requested recalculation/writeback, use the aggregation skill as a separate authorized workflow.
