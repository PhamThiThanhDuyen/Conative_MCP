# Usage Examples

## Trigger phrases

**English**
- "Run these test cases against staging and report results"
- "Execute test cases TC-LOGIN-001 to TC-LOGIN-010 and record the results"
- "Run a regression/smoke test from this test case file"
- "Verify this test case and attach evidence"
- "Record the test results and compare actual with expected"
- "Make a test execution report for build 2.14.3"
- "I cannot run these, make a checklist for QA to run by hand"
- "Mark each case Pass/Fail/Blocked with evidence"
- "What evidence do I need before I can mark this Pass?"

**Vietnamese**
- "Chạy giúp mình các test case này trên staging"
- "Thực thi test case rồi ghi kết quả"
- "Tạo checklist để QA chạy tay"

---

## Example 1: Direct run (API tools available)

**Input**
> Run TC-API-012 on staging (https://staging.example.com), build 2.14.3.
> Step: POST /orders with product SKU-TEST-01, quantity 2.
> Expected: HTTP 201, body has `orderId`, `status = "PENDING"`, total = 200,000 VND.
> Account: qa_buyer (given through an environment variable). Staging is a private QA environment and creating test orders is allowed.

**How to handle it**
1. Pre-flight: confirm the build with `GET /version` → returns `2.14.3` ✔; private environment, writing allowed ✔.
2. Run the step and save the request/response (token hidden).
3. Compare each part of the expected result.

**Output**

| Field | Content |
|---|---|
| ID | TC-API-012 |
| Status | **Fail** |
| Expected result | HTTP 201; has `orderId`; `status = PENDING`; total = 200,000 VND |
| Actual result | HTTP 201; `orderId = ORD-88231`; `status = PENDING`; **total = 220,000 VND** |
| Evidence | `evidence/TC-API-012/step1_response_20261007-141530.json` (request/response, token hidden); timestamp 14:15:30 (GMT+7); build confirmed as 2.14.3 through `/version` |
| Notes | 3 of 4 parts match. The total is 20,000 VND higher, maybe because of a fee or tax. Not confirmed with the spec. Order `ORD-88231` was created on staging and needs cleanup. |
| Next step | Log a bug (total is different from expected) or confirm the expected result with the BA; cancel order `ORD-88231` |

---

## Example 2: Partial run

**Input**
> Run TC-CHECKOUT-005 (UI + API). I can only give you an API token. I do not have a UI account yet.

**How to handle it**
- **Partial** mode: run the API steps; put the UI steps in a manual checklist.
- The API steps can have evidence, but the whole case **cannot be Pass** yet because UI evidence is missing.

**Output (short)**

| Field | Content |
|---|---|
| ID | TC-CHECKOUT-005 |
| Status | **Not Run** (partly done: API steps 1–3 match, UI steps 4–6 not run) |
| Actual result | Steps 1–3: match expected (see evidence). Steps 4–6: not done |
| Evidence | `evidence/TC-CHECKOUT-005/step1-3_*.json` |
| Notes | No UI account, so the success message on the screen was not confirmed |
| Next step | QA runs steps 4–6 using the attached checklist, or a UI account is provided |

---

## Example 3: Cannot run directly

**Input**
> Here are 15 test cases for a mobile app. Please run them.

**How to handle it**
Say it clearly: "In this session I do not have a device, emulator or access to the app, so I cannot run these cases and cannot confirm the actual results." Then:
- Mark all 15 cases `Not Run`.
- Give a manual checklist (`manual-checklist.md`) with pre-flight and a table for each case.
- Point out cases with vague expected results (for example "the app feels smooth") so they can be clarified before running.
- You may offer an Appium/Maestro script, and say clearly that it **has not been run, so it proves nothing**.

---

## Example 4: Blocked because of a shared environment

**Input**
> Run TC-USER-021: delete the user account `user_demo` on UAT.

**How to handle it**
UAT is shared, the "delete account" step has side effects, and the user did not allow data changes. Do not run the delete step.

**Output (short)**

| Field | Content |
|---|---|
| ID | TC-USER-021 |
| Status | **Blocked** |
| Expected result | The account is deleted and cannot log in again |
| Actual result | The delete step was not done. Step 1 (log in as `user_demo` to confirm it exists) was run: success |
| Evidence | `evidence/TC-USER-021/step1_login_*.png` |
| Notes | `user_demo` may be used by another team on UAT; deleting it would affect them |
| Next step | Confirm that deleting `user_demo` is allowed, or provide a separate test account |

---

## Example 5: A correct Pass

**Input**
> TC-LOGIN-001: log in with the correct email/password → go to the Dashboard page, and the user name is shown in the top right.

**Output (short)**

| Field | Content |
|---|---|
| ID | TC-LOGIN-001 |
| Status | **Pass** |
| Expected result | Go to Dashboard; user name is shown in the top right |
| Actual result | Redirected to `/dashboard`; top right shows "QA Buyer" |
| Evidence | `TC-LOGIN-001_step3_dashboard_20261007-142010.png` (URL and name visible), no errors in the console |
| Notes | Chrome 129, build 2.14.3 (confirmed on the About page) |
| Next step | None |

**Why this is a valid Pass:** both parts of the expected result (redirect, name shown) have evidence you can see, and the build was confirmed.

---

## What not to do

- ❌ "Login seems to work, so Pass." → no actual result or evidence.
- ❌ Marking the whole run Pass because "the earlier cases passed".
- ❌ Marking Fail for a case that could not log in because the service was down (that is Blocked).
- ❌ Running delete/edit steps on shared staging without asking.
- ❌ Pasting a full token or password into the report.