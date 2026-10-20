# Claude and QE API Comparison — Round 2

## Run information

- Run ID:
- Run time and timezone:
- Google Sheet execution date for `Version <org> - <channel>`: `<Mon d, yyyy>` (example: `Oct 16, 2026`)
- Test case ID:
- Organization:
- Channel/source:
- Environment alias:
- Postman collection/request:
- Status: `PASS` / `FAIL` / `PARTIAL` / `BLOCKED`

## Compared result

- Expected field(s) and confirmed QE mapping(s):
- Claude value(s):
- QE API value(s):
- Difference (Claude − QE API, numeric only):
- Claude timerange:
- Expected result conditions and outcome:
- Unmapped expected field(s):
- Scope/context (dataset, grain, channel/source, filters, date range, timezone):
- Comparison rule/reference:
- Evidence references:
- Root cause (evidence-based; otherwise `Unknown` for a failure):
- Blocker/limitation:

## Single Note format for `Note <org> - <channel>`

Use this exact set of lines for every status. Each line starts with `- `. Fill
non-applicable fields with `N/A`; use `Not available` for a required value that
could not be obtained and explain the limitation on the final line. For numeric
values, calculate Difference as **Claude − QE API**. For text/categorical values,
write `Not numeric` and describe whether values match. For BLOCKED cases do not
present unavailable results as completed comparisons.

```text
- Status: <PASS | FAIL | PARTIAL | BLOCKED> <xuống hàng>
- Compared field(s): <field and confirmed QE mapping(s), or N/A> <xuống hàng>
- Claude value(s): <value(s), or Not available> <xuống hàng>
- QE API value(s): <value(s), or Not available> <xuống hàng>
- Difference (Claude − QE API): <numeric difference, Not numeric,  Not calculated, or N/A> <xuống hàng>
- Claude timerange: <returned timerange, Not stated, or Not available> <xuống hàng>
- Expected result conditions: <conditions and outcome, or N/A> <xuống hàng>
- Unmapped expected field(s): <field(s), or N/A> <xuống hàng>
- Scope/context: <observed scope, or Not available> <xuống hàng>
- Root cause: <evidence-based cause, Unknown, or N/A> <xuống hàng>
- Blocker/limitation: <specific limitation, or N/A> <xuống hàng>
```

## Status rules and precedence

Apply these rules in order; a demonstrated failure takes precedence over other
limitations:

1. `FAIL`: at least one available mapped value differs under the approved rule,
   or an explicit Expected result condition is demonstrably unmet.
2. `BLOCKED`: comparison cannot be completed because a required value is
   unavailable, a request fails, scope/rules are unresolved, or no expected field
   remains comparable. Use this when there is no demonstrated failure and the
   missing input prevents a reliable conclusion.
3. `PARTIAL`: mapped checks are complete and otherwise pass, but at least one
   expected field has no confirmed QE mapping. List skipped expected fields.
4. `PASS`: every expected field has a confirmed mapping, all required values
   match, and all explicit Expected result conditions hold.

An unmapped non-expected extra field is skipped and does not change status. An
unmapped expected field can never receive PASS. HTTP success alone is not PASS.
Write a status to the workbook only if its live validation permits that token;
otherwise leave status and Note cells unchanged and report the limitation.

## Google Sheet Version column

Whenever recording a result in Google Sheets, also write the execution date to
the exact `Version <org> - <channel>` column for the same testcase row. Format
the date in English as `MMM d, yyyy` (for example, `Oct 16, 2026`) using the
execution date in the run's stated timezone. Verify that the complete header
matches both organization and channel and that the target cell is authorized for
update. Treat the status, Note, and Version date as one result update: if any
required header or write permission is missing or ambiguous, do not write a
partial result; report the blocker. Read all updated cells back and confirm the
workbook saved.

## Evidence handling

- Keep Claude and QE API values separately identifiable.
- Record scope details and visible warnings when available.
- Do not include credentials, tokens, cookies, session state, or unnecessary
  customer data.
- Store evidence only in an approved, access-controlled destination.
