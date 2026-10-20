---
name: record-graphql-results-to-sheet
description: Record verified Conative GraphQL summary API results in the matching Google Sheets status tab, adding a dated run column and a note for failed metrics. Use after Summary_Variant or Summary_Product has been run and the user asks to write the results.
metadata:
  short-description: Record GraphQL API results in Google Sheets
---

# Record GraphQL Results in Google Sheets

Write one completed API run to the GraphQLV2 workbook. Use the API response as evidence; do not invent a result.

## Source and destination

Open the result workbook in the in-app browser or with the connected Google Drive/Sheets tools:

[GraphQLV2](https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit)

Choose the tab by the API that was run:

- `Summary_Variant` → `Sales_by_variant`
- `Summary_Product` → `Sales_by_product`

Confirm the exact tab and the metric label/key columns before editing. Match each returned API metric to the corresponding row using its defined field name/key. Do not rely on row order or a partial name match. If a metric cannot be matched uniquely, leave it unchanged and report the issue.

## Add a run column

1. Find the header whose text equals `AI Chat` after trimming leading and trailing spaces. The live workbook has `AI Chat` on `Sales_by_variant` and `AI Chat ` (one trailing space) on `Sales_by_product`. Require exactly one match.
2. Insert one new column immediately before that column. Preserve the other columns and existing data.
3. Set the new column header to three lines:

   `<Org> - <from_source> Summary`

   `<from_date> - <to_date>`

   `Kiểm tra ngày <today>`

   Use the user's dates/source and today's date in the user's local timezone. Use actual line breaks between lines.
4. If the trimmed header is missing or appears more than once, stop and report the issue. Do not insert a column elsewhere.

## Record results

For each metric with a clear API check marker, write `Passed` for green/pass and `Failed` for red/fail in its matched row under the new run column. Leave metrics absent from the response untouched. A value by itself does not prove pass or fail; only use an explicit API marker or an approved comparison rule. If neither exists, leave that metric blank and report why.

For each `Failed` metric, add a cell note to that status cell using the sheet's **Insert → Note** action. Put the relevant failure message/details returned by the API in the note. Do not add notes to passed cells. Do not include credentials, tokens, or unnecessary customer data.

## Verify and report

Read back the new header, every changed status, and each failed-cell note. Confirm the sheet saved. Report the API/tab, header, metric statuses, failed notes, and any skipped or ambiguous metrics. If insertion or a write cannot be verified, say so and do not claim completion.
