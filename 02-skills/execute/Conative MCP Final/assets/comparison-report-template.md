# Claude and QE API Comparison — Round 2

## Run information

- Run ID:
- Run time and timezone:
- Test case ID:
- Organization:
- Environment alias:
- Postman collection/request:
- Status:

## Compared result

- Metric/field:
- Claude value:
- QE API value:
- Difference (Claude − QE API, when numeric):
- Timerange returned by Claude:
- Comparison rule/reference:
- Evidence references:
- Root cause, if failed (evidence-based; otherwise `Unknown`):

## Note `<name org>` cell content

Write the following content to the selected organization's `Note <name org>` cell, using the exact organization-specific header and only when that cell is authorized for update. **Each non-empty idea must start on its own line with `- `.** Apply this format to every note type, including PASS, FAIL, and blocked/incomplete notes.

### If the testcase passes and the Claude and QE API data are equal

```text
- <name metric> khớp: <data return>
- Timerange return in Claude = <data return>
```

### If the testcase fails and the Claude and QE API data are not equal

```text
- Failed <name metric>: Claude = <data return>, QE API = <data return>, Difference = <data return Claude> - <data return QE API>
- Root cause: <root cause>
- Timerange return in Claude = <data return>
```

For a numeric metric, calculate `Difference` as Claude minus QE API. For non-numeric values, describe the observed difference without inventing arithmetic. State a root cause only when supported by evidence; otherwise write `Unknown`. Use the time range Claude actually returned; if Claude returned none, write `Not stated`.

## Blocked or incomplete comparison

If Claude or QE API does not return the requested value, the field mapping is unresolved, or the request fails, do not use either pass/fail note. Follow the spreadsheet's allowed blocked/not-run behavior; if no allowed token exists, leave the status and Note cells unchanged and report the blocker.

## Evidence handling

- Keep the original Claude and QE API values distinguishable in the report.
- Record dataset, grain, channel/source, filters, date range, and timezone as context when available.
- Do not include credentials, tokens, cookies, session state, or unnecessary customer data.
- Store evidence only in an approved, access-controlled destination.
