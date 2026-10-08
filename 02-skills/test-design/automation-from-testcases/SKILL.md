---
name: automation-from-testcases
description: Run test cases in a way that can be checked and proven. Find the environment, build/version, accounts and data first, run each step in order, record the actual result, compare it with the expected result, and set a status (Pass, Fail, Blocked or Not Run) with evidence (logs, screenshots, request/response, timestamps). Use this skill whenever the user gives test cases, test scripts or a test suite and wants to run, execute, verify, regression test, smoke test, UAT, record test results, or make a test report. Also use it when they say "run test case", "execute test cases", "verify this test", "mark Pass/Fail", "automation from test cases", "chạy test case", or "thực thi test", even if they do not name the skill. If the tests cannot be run directly, the skill makes a checklist for a QA person to run by hand instead of guessing results.
---

# Automation From Testcases

Goal: turn test cases into results that anyone can check. A test result is only useful if another person can look at the evidence and agree with it. So the main rule is: **no evidence, no Pass.**

## Core rules

1. **Pass needs evidence.** Give Pass only when you saw an actual result (command output, response, screenshot, log, a value read from the UI or database) that matches the expected result. "The code looks right" or "the last step worked" is not evidence.
2. **Be honest about limits.** If you do not have the tools, access or environment to run a test, say so and switch to manual checklist mode. Never pretend you ran a test or make up a result.
3. **Do not change shared data or environments.** Tests can create, edit or delete data. Other people may depend on shared environments (staging, UAT, shared databases). Only change things when the user clearly allows it (see "Data safety").
4. **Record what really happened,** even when it is a surprise or not part of the test case. Extra observations (console errors, slow responses, warnings) go in Notes.

## Process

### Step 1: Check the input (pre-flight)

Before running anything, find out the items below. If something important is missing, ask the user once (keep it short) or write down your assumption.

| Item | What to find out |
|---|---|
| Test case | ID, title, precondition, steps, expected result, test data |
| Environment | URL/host, type (local, dev, staging, UAT, prod), shared or private |
| Build/version | Build number, commit/tag, deploy date, and how to confirm it (About page, `/version`, header, footer) |
| Account and permissions | Which role to use, how credentials are given (never put passwords in the report) |
| Data | Data that must already exist, data that will be created, how to clean up |
| Tools | Browser automation, API client, shell, DB client, log access: which ones really exist in this session |

**Verify, do not just trust.** If you can, confirm that the running build matches what the user said. A wrong version is a common reason for false Fail and false Pass. If you cannot confirm it, write "version not verified" in the report.

After pre-flight, choose an **execution mode**:
- **Direct**: you have the tools and access to run the steps. Run them for real.
- **Partial**: you can run some steps (for example the API works but there is no UI access). Run what you can and put the rest in a manual checklist.
- **Manual (guided)**: you cannot run anything. Make a checklist using `references/manual-checklist.md` and leave the cases as `Not Run`.

Tell the user which mode you chose and why before you start.

### Step 2: Safety check before running

For each test case, scan the steps and mark the ones with side effects: creating, editing or deleting data; sending real emails, SMS or notifications; payments; config changes; password resets; locking accounts; running background jobs.

- **Private or isolated** environment, or the user **clearly allowed it**: you can run it. Still write down any data you created so it can be cleaned up.
- **Shared** or **unknown** environment and the step has side effects: **stop at that step**. Ask for permission, or mark it `Blocked` with the reason "needs approval to change data". Read-only steps can still run.
- **Production**: by default run read-only steps only. Do not run write steps unless the user clearly asks.
- Never use real customer data as test data unless you have permission.

### Step 3: Run the steps in order

Run each step in the same order as the test case. For each step:

1. Write down the **time** it started (timestamp, with time zone if it matters).
2. Do exactly what the step says. Do not skip steps or "improve" them.
3. Write down the **actual result** of the step: what you saw, not what you expected.
4. Collect evidence using `references/evidence-checklist.md` when your tools allow it.
5. If the step has its own expected result, compare it right away.

When something goes wrong:
- A system error (500 response, wrong UI) is a result to record. Do not quietly retry until it turns green. You may retry **once** to see if the error is stable or flaky, and record both runs.
- An environment, tool or access problem (cannot log in, service down, missing data) makes the dependent steps `Blocked`, not `Fail`.
- A precondition that is not met makes the case `Blocked`. Say which precondition.

### Step 4: Compare actual with expected

Compare point by point. An expected result often has several parts (a message is shown, data is saved correctly, a status changes). Check **each part**. Give Pass only if **all** parts match.

- Small differences still count: a typo in a message, a wrong date format, a rounding error. Record them. The user decides how serious they are, not you.
- If the expected result is vague or cannot be checked ("the system works normally"), do not read it in a generous way. Write down what is unclear, say how you understood it, and mark `Blocked` or ask if you cannot decide.
- If actual matches expected but you notice odd behavior outside the test case, the case is still Pass. Put what you saw in Notes.

### Step 5: Set the status

Use only these four statuses:

| Status | When | Required |
|---|---|---|
| **Pass** | All steps were run and every expected result matches the actual result | Evidence for each main expected result |
| **Fail** | The case was run and actual is **different** from expected | Description of the difference + evidence + the step where it happened |
| **Blocked** | The case cannot be run or finished because of something outside the test case | The reason it is blocked and what is needed to unblock it |
| **Not Run** | The case has not been run (out of scope for this session, manual mode, no time) | The reason |

Rules for hard cases:
- If any step fails, the case is **Fail**, even if later steps could not run. Say which steps did not run.
- If you do not have enough evidence for Pass but saw no bug, it is **not Pass**. Use `Blocked` (if something is in the way) or `Not Run` (if you did not do it). Say exactly which evidence is missing.
- Fail vs Blocked: Fail means the product behaved wrongly. Blocked means you could not test the product. Calling a Blocked case Fail makes a fake bug. Calling a Fail case Blocked hides a real bug.

### Step 6: Report

For **each case**, give all of these fields (use `assets/report-template.md`):

- **ID**: test case ID
- **Status**: Pass / Fail / Blocked / Not Run
- **Expected result**: copied from the test case
- **Actual result**: what you saw, in specific words
- **Evidence**: a clear reference (screenshot file name, log lines with timestamp, request/response with sensitive data hidden, artifact path). If there is none, write "None" and the reason
- **Notes**: extra observations, assumptions, flaky behavior, data created that needs cleanup
- **Next step**: a specific action: log a bug, rerun after X, ask for access Y, QA runs part Z by hand

Start the report with an **environment summary** (environment, build/version and how it was verified, account/role used, execution mode, run time) and a **summary table** with the count of Pass/Fail/Blocked/Not Run. End with a list of data created or changed (if any) for cleanup, and a list of points the QA person must decide.

## When you cannot run the tests directly

Say it at the start, not at the end: "In this session I do not have [tool/access] to run [type of test], so I cannot confirm the actual results." Then:

1. Mark the related cases `Not Run`.
2. Make a manual checklist using `references/manual-checklist.md`: pre-flight, each step with expected result, a place to write the actual result, the evidence to capture, and a status box.
3. Offer what you can do in this session (review test case quality, find vague expected results, suggest test data, write a script for the user to run). Say clearly that a script that has not been run proves nothing.

When you write an automation script (Playwright, Cypress, pytest, Postman/Newman, etc.) for the user to run: the script must **assert** the expected results clearly, save a screenshot or log when it fails, and not contain hard-coded credentials. Remind the user that a script that was not run gives no result.

## Sensitive information

- Do not put passwords, tokens, API keys, card numbers or real personal data in the report. Hide them in requests, responses and screenshots, for example `Authorization: Bearer ****`.
- Refer to accounts by role or test username, never with the password.
- If evidence accidentally contains sensitive data, warn the user instead of passing it on.

## Reference files

Read these when needed:
- `references/evidence-checklist.md`: evidence checklist by test type (UI, API, DB, log, performance) and naming/storage rules.
- `references/manual-checklist.md`: manual checklist template for when you cannot run directly.
- `references/examples.md`: full usage examples: direct run, partial run, cannot run, Blocked case, Fail case.
- `assets/report-template.md`: report template for each case and the summary table.