---
name: sum-org-report-status
description: Summarize Passed and Failed fields by org and channel from dated OPS/GraphQL Summary columns, and place the report under a specified ticket's Report section when requested.
metadata:
  short-description: Summarize org report status
---

# Sum org report status

Create a compact status report from the `Sales_by_variant` tab of the GraphQLV2 workbook. Use this skill when asked to aggregate org/channel Summary results for a check date or record that aggregation under a ticket's `Report` section.

## Source and scope

- Read the current instructions in `/Users/duyenpham/Documents/Work/Automation/Conative_MCP/02-skills/OPS/demo-summary-status/references/graphqlv2-sales-by-variant-status-reference.md` and follow its snapshot/status guidance.
- Workbook: [GraphQLV2](https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit), tab `Sales_by_variant` (sheet ID `1386744145`). Use connected Google Sheets tools to read the live sheet.
- Select only columns whose headers are `Summary` results for the exact requested check date. Do not mix check dates, timeranges, orgs, or channels. Preserve the complete header scope when identifying the report.
- Derive org and channel from each selected header. Include each matching org/channel once per distinct Summary column; if more than one timerange exists for the same org/channel, report each separately so snapshots are not merged.
- Count field rows only. Exclude the header and the `Total count` aggregate row. Count exact `Passed` and `Failed` cells separately; blank and `N/A` cells are not passes or failures. Preserve other recorded statuses (such as `Stuck` or `In testing`) in a separate `Other` line if present rather than folding them into either count.
- For failed fields, use the display name from the catalog (`Name`, column C); use the API key (column D) only if the display name is missing. List every failed field once for its corresponding org/channel/summary column.

## Report format

Use a level-three Markdown heading for every org. Under each org, use nested bullets in this order: Channel → Summary → Passed and Failed counts. Nest failed field names under Failed. For example:

```markdown
### DEMO 1
- Channel: Shopify
  - Summary
    - Passed: 16
    - Failed: 2
      - Gross Profit
      - Stock
```

Include timerange or check date context when it helps distinguish multiple Summary columns for the same channel. Do not invent a status for missing cells.

## Recording under a ticket's Report section

- Only update a ticket when the user explicitly asks to record the summary and identifies the destination ticket or provides an unambiguous current ticket context.
- Locate the `Report` heading in the ticket Description and add the summary below it. Preserve the ticket title, all pre-existing Description sections, and all content outside the Report section.
- If the `Report` heading is absent or the requested placement is ambiguous, do not replace the Description; ask for the needed placement detail.
- Verify the saved ticket shows the org headings, nested lists, counts, and failed field names. Report the ticket link and any statuses that could not be counted as Passed/Failed.
