---
name: conative-mcp-bug-report
description: Create a clear, evidence-backed bug report for a Conative MCP discrepancy observed in OP, comparing Claude output with QE output and preserving the query context and screenshots.
---

# Create a Conative MCP Bug on OP

Use this skill when a user asks to report a bug in Conative MCP on OP, especially when Claude's returned data differs from the Query Engine (QE).

## Goal

Prepare a complete bug report using the exact sections and fields below. Use the user's evidence as provided. Do not invent values, timestamps, prompt text, QE request details, results, or attachments. If required information is missing, gather it from the available conversation or connected evidence; ask the user only for details that cannot be recovered.

## Report requirements

### Title

Use this format:

`[MCP][<org name>] - <short description of the issue>`

The description should identify the discrepancy, for example: `Lệch data <name field> ở Claude thấp hơn hoặc cao hơn so với QE`.

### Description formatting (required)

In the OP rich-text editor, format the description as follows:

- `Thông tin`, `Actual result`, and `Expected result` must each be a real **Heading 3** block (not Markdown heading characters pasted as plain text).
- Every content item beneath each Heading 3 must be a bulleted list item.
- In the `QE` details, do not include a `fields` property or list of requested fields. Preserve the QE request properties that are present, such as `entity_grain`, `distribution_channel_scope`, `time`, `filters`, `sort`, and `pagination`; do not add `fields`.
- Format the QE request JSON with the editor's **Insert code snippet** feature. Do not use a Markdown fenced code block as a substitute for the editor's code snippet.

Include an **Thông tin** section with:

- `org`: organization name.
- `from source`: source name.
- `prompt`: exact prompt used for the check.
- `Thời gian kiểm tra`: date and time when the check was performed, including timezone when known.
- `QE`: QE request details, preferably the request body as submitted. Show each available field:
  - `entity_grain`
  - `distribution_channel_scope`
  - `time`
  - `filters`
  - `sort`
  - `pagination`

Preserve the exact values and structure from the request. Mark unavailable fields as `Chưa cung cấp`; do not infer defaults.

### Actual result

Describe the observed discrepancy and state both values explicitly:

- `Claude`: value or response returned by Claude.
- `QE`: corresponding value or response returned by QE.
- Include the Claude and QE screenshots as separate attachments when available. Label each attachment clearly. If an image is unavailable, state `Chưa đính kèm` rather than implying it exists.

Keep units, precision, date range, filters and aggregation context visible when they affect the comparison. Do not claim the values are comparable if their scopes differ; call out the mismatch.

### Expected result

Describe the behavior or result expected from Conative MCP. When the issue is a data discrepancy, state that Claude should return a result consistent with QE for the same source, time range, grain, filters, sorting and pagination. Specify the expected value if it is supported by evidence. If it is unknown, leave a clear placeholder for the reporter rather than choosing Claude's or QE's value.

## Output template

Use the OP rich-text editor and apply the actual block formatting described above. This outline shows the content and hierarchy; it is not a literal Markdown block to paste as plain text:

- **Heading 3: Thông tin**
  - org: `<org name>`
  - from source: `<source name>`
  - prompt: `<exact prompt>`
  - Thời gian kiểm tra: `<date/time and timezone if known>`
  - QE: `<request name/details>`
  - Insert the QE request body as a code snippet using the editor's **Insert code snippet** feature. Include available request properties (`entity_grain`, `distribution_channel_scope`, `time`, `filters`, `sort`, `pagination`) and omit `fields`.
- **Heading 3: Actual result**
  - `<Describe the observed discrepancy and comparison scope>`
  - Claude = `<returned value>`
  - QE = `<corresponding returned value>`
  - Hình ảnh Claude: `<attachment or "Chưa đính kèm">`
  - Hình ảnh QE: `<attachment or "Chưa đính kèm">`
- **Heading 3: Expected result**
  - Claude = QE `<corresponding returned value of QE>`

## Quality checks

Before submitting or handing off the report:

1. Confirm the title uses the requested prefix and organization name.
2. Confirm Claude and QE values are paired for the same metric and retain units/precision.
3. Include the original prompt and check timestamp; include the available QE request properties, omitting `fields`.
4. Include both labeled screenshots when available.
5. Mark missing evidence plainly; do not fabricate or silently omit it.
6. Keep the report in Vietnamese unless the user asks for another language.
7. Verify the editor shows Heading 3 blocks, bulleted content and a QE JSON code snippet before submitting.

This skill prepares report content. Create the issue in OP only when the user explicitly requests submission and the required OP access is available.
