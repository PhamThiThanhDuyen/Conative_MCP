# Evidence Checklist

Good evidence answers three questions: **What?** (the result you saw), **When?** (timestamp), **Where?** (environment/build). If one is missing, other people find it hard to check.

## 1. General information (all test types)

- [ ] Test case ID and the step number
- [ ] Time of the action (date, time, time zone)
- [ ] Environment (URL/host) and build/version, and how the version was verified
- [ ] Account/role used (no password)
- [ ] Test data used (record IDs, input values)
- [ ] Browser/device/OS and version (for UI tests)
- [ ] Run number (run 1, run 2 if you retried to check for flaky behavior)

## 2. UI tests

- [ ] Screenshot **before** and **after** the important action (message, status or value is clearly visible)
- [ ] Screenshot at the moment of failure (if Fail), with the URL/address bar if possible
- [ ] Browser console log (errors/warnings) during the run
- [ ] Network tab: failed requests (4xx/5xx) and the main request of the step
- [ ] Video/trace (Playwright trace, Cypress video) if the tool supports it
- [ ] Exact message text (copy it word for word, do not rephrase)

## 3. API tests

- [ ] Request: method, URL, relevant headers (token hidden), body
- [ ] Response: status code, relevant headers, body (sensitive data hidden)
- [ ] Response time (ms) if the test has a performance requirement
- [ ] Correlation/request ID or trace ID to find server logs
- [ ] Check each assertion: status, schema, field values, error message
- [ ] Data state after the request (GET again or query) for tests that write data

## 4. Data checks (DB / target system)

- [ ] The query used (read-only) and its result
- [ ] Values before and after the action
- [ ] Number of records affected
- [ ] Run `SELECT` only. Do not run `INSERT/UPDATE/DELETE` on shared environments without permission

## 5. Server / system logs

- [ ] Relevant log lines with timestamp and level (ERROR/WARN)
- [ ] Full stack trace if there is an exception
- [ ] The time range and filter used (so others can repeat it)
- [ ] If you cannot view logs, write "Log access not available" instead of leaving it empty

## 6. Performance / non-functional

- [ ] Tool and load settings (number of users, duration, ramp-up)
- [ ] Numbers: avg/p95/p99, throughput, error rate
- [ ] Charts or raw result files
- [ ] Resource usage (CPU/RAM) if you have access

## Naming and storing

- Name files so they can be traced back: `<TC-ID>_step<N>_<description>_<YYYYMMDD-HHMMSS>.png`
  Example: `TC-LOGIN-003_step4_error-message_20261007-141530.png`
- Group evidence by case: `evidence/<TC-ID>/`
- In the report, refer to the file name or path. Do not only write "screenshot taken"
- Keep original evidence unchanged. If you hide sensitive data, add a note "hidden"

## Hiding sensitive data

Hide these before putting evidence in a report: passwords, tokens/JWT, API keys, session cookies, card numbers, national ID numbers, real emails/phone numbers, addresses. Use `****` or `[REDACTED]` and keep the structure so it is still readable.

## When you cannot collect evidence

Do not leave it blank. Write:
- The type of evidence you could not collect (for example: server log)
- The reason (no access, tool does not support it, environment does not allow it)
- The effect: the case **cannot be Pass** if evidence for the main expected result is missing. Use Blocked or Not Run, and say what is needed to add it