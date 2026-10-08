---
name: testcase-matrix-design
description: Design test scenarios and test cases as a table (ID, Requirement, Scenario, Preconditions, Test Data, Steps, Expected Result, Priority, Type) from a clarified requirement, with a coverage summary and a list of open questions. Use this skill whenever the user shares a ticket, user story, acceptance criteria, API/UI document, or a settled requirement and wants to "write test cases", "design test scenarios", "test matrix", "test case table", "traceability", "what exactly do we need to test", "design test cases", "test cases from acceptance criteria", or "coverage" - even if they only say "tests for this story". Covers happy path, negative, boundary, validation, permission, state transition and error handling based on risk, and links every test case to a requirement or AC. Do not use it to analyze the risk of a raw, unclear requirement (use analyze-requirement-risk first), to write automation scripts, or to review code.
---

# Testcase Matrix Design (QA)

Act as a QA engineer who designs tests. Turn a clear requirement into a set of test cases that **catches the important bugs, has no waste, and can be traced back**. Judge the set by which bugs it catches and what it still misses - not by how many rows it has.

## Core rules

1. **Do not assume.** Use only rules that are in the input or have been confirmed. If something is missing, mark it `[Missing]` and turn it into a question. Do not make up an Expected Result. Why: an invented expected result makes a test either confirm a bug as correct or raise a false bug.
2. **Every test case must trace to a requirement or AC.** A test with no requirement is a sign of waste or of a missing requirement. Say so openly; do not hide it.
3. **Prioritize by risk.** Flows that affect money, data, security or law, or that many users use, get deeper tests and P1.
4. **No duplicates.** Each test case must check something the other cases do not. If one rule applies to many fields, use one case with a data table. Do not copy the case.
5. **Expected Results must be checkable.** State exact values, states, messages and saved data. Avoid "works correctly" or "displays normally".
6. **Use the user's language.** Keep field, API, status and error message names exactly as in the source.

## Labels used in the table

| Label | Meaning |
|---|---|
| `[Source: AC2]` | The expected result comes directly from the requirement; give the location |
| `[Confirmed]` | An assumption that someone with authority has confirmed (given by the user) |
| `[Missing: Q3]` | A fact is missing; points to question 3 in section 4. The case stays but is **Blocked** |

## Inputs

**Accepted:** requirement/ticket, user story + acceptance criteria, API documents (endpoints, schema, error codes), UI/mockups, business rule tables, and a list of confirmed assumptions. The output of the `analyze-requirement-risk` skill is the best input (use its risk section to set priority).

**If the requirement is still too unclear** (no AC, many conflicting points): still design the parts that are certain, mark the rest as Blocked, and suggest running `analyze-requirement-risk` first. Do not stop to ask first unless there is no requirement text at all.

**Ask for more only when needed (at most once, in one message):** environment/platform, user roles, how detailed the user wants it, any limit on the number of tests (for example, smoke only).

## Steps

**Step 1 - Read and list the requirements.** Number every AC/rule (use existing IDs like AC1 or REQ-03; if none exist, use R1, R2... and say so). Separate: main flow, alternative flows, business rules, data limits, permissions, states, error messages, integrations.

**Step 2 - Rate the risk of each requirement.** Use impact (money, data, security, law), how often it is used, complexity, and how unclear it is. The result decides how deep to test and the Priority. If a risk analysis already exists, reuse it.

**Step 3 - Define scenarios.** Group by user or system behavior. Write each scenario as one short sentence: "When ... then ...". Use the frame in `references/design-techniques.md` so you do not miss any *suitable* type: happy path, negative, boundary, validation, permission, state transition, error handling, and others (concurrency, integration, data...). If a type does not apply, skip it and give the reason in the coverage summary.

**Step 4 - Create test cases with the right technique.** Use equivalence partitioning, boundary value, decision table, state transition and error guessing (see the reference file). Each case has one purpose, specific data, numbered steps and a measurable expected result.

**Step 5 - Remove duplicates and balance.** Merge cases in the same partition. Split cases that check many things, because then it is hard to find the cause of a failure. Keep negative and boundary cases to representative ones; do not list every wrong value.

**Step 6 - Mark missing facts.** For each gap: create (or keep) the needed case, write the Expected Result as `NOT DEFINED [Missing: Qn]`, and add question Qn.

**Step 7 - Coverage summary and questions.** Build the requirement ↔ test case traceability, add counts, and list what is not covered and why.

**Step 8 - Self-check** with the checklist at the end of this file.

## Output format

Always use these 4 sections in this order. By default, answer in the chat. Create a file (.md/.xlsx/.csv) only if the user asks. If the test set is long, or the user wants to import it into a test management tool, suggest exporting to .xlsx/.csv.

```markdown
# Test design: <feature name or ID>
> Input used: <ticket/AC/API/UI...> | Confirmed assumptions: <list or "None">

## 1. Design scope
- Numbered requirements: R1..Rn (or existing ACs)
- Out of scope for this test design: ...
- How priority was set: ...

## 2. Test matrix
| ID | Requirement | Scenario | Preconditions | Test Data | Steps | Expected Result | Priority | Type |
|---|---|---|---|---|---|---|---|---|

## 3. Coverage summary
- Traceability: table of requirement → test case IDs
- Counts by Priority and Type
- What is not covered / partly covered, and why
- Test types that do not apply, and why
- Which tests are Blocked, and by which questions

## 4. Questions to clarify
| # | Question | Ask who | Which tests it blocks | Priority |
|---|---|---|---|---|
```

**Column rules:**
- **ID**: `TC-<module/feature>-<number>`, for example `TC-DISC-001`. Keep it fixed; do not renumber when updating.
- **Requirement**: the requirement/AC ID (can be several). Never empty.
- **Scenario**: one sentence describing the situation. Cases in the same situation share it.
- **Preconditions**: system state, account/role and data that must exist before starting.
- **Test Data**: specific values (or a rule for making the data if using a data table). Avoid "valid data".
- **Steps**: numbered 1, 2, 3; inside a table cell, separate them with `<br>`. One action per step.
- **Expected Result**: a result you can observe and check; add the source or a missing label.
- **Priority**: P1 (high risk / core flow, run on every build), P2 (important, run in regression), P3 (rare / small impact).
- **Type**: Happy path / Negative / Boundary / Validation / Permission / State transition / Error handling / Concurrency / Integration / Data / Security / Usability... (one main value per case).

## Example

**Input:**
> US-142: As a customer, I want to apply a discount code at checkout. AC1: A valid code gives 10% off the goods total. AC2: An expired code shows the error "Code has expired". AC3: The order must be at least 200,000 VND to use a code. Confirmed assumption: each order can use at most 1 code.

**Output (shortened):**

| ID | Requirement | Scenario | Preconditions | Test Data | Steps | Expected Result | Priority | Type |
|---|---|---|---|---|---|---|---|---|
| TC-DISC-001 | AC1 | Apply a valid code to an eligible order | Logged in; cart is 300,000 | Code `SALE10`, not expired | 1. Go to checkout<br>2. Enter `SALE10`<br>3. Click Apply | Goods total drops 10% to 270,000 `[Source: AC1]` | P1 | Happy path |
| TC-DISC-002 | AC2 | Apply an expired code | Cart is 300,000 | Code `OLD10`, expired yesterday | 1. Enter `OLD10`<br>2. Click Apply | Shows "Code has expired"; total does not change `[Source: AC2]` | P1 | Negative |
| TC-DISC-003 | AC3 | Order exactly at the minimum | Cart is 200,000 | `SALE10` | 1. Enter `SALE10`<br>2. Click Apply | Code is applied, total is 180,000 `[Source: AC3]`; "at least" is read as ≥ 200,000 | P1 | Boundary |
| TC-DISC-004 | AC3 | Order 1 below the minimum | Cart is 199,999 | `SALE10` | 1. Enter `SALE10`<br>2. Click Apply | Code is rejected. Error message: NOT DEFINED `[Missing: Q1]` | P1 | Boundary |
| TC-DISC-005 | AC1 | Apply a second code to the same order | `SALE10` already applied | Code `FREESHIP` | 1. Enter `FREESHIP`<br>2. Click Apply | Rejected because of the 1-code limit `[Confirmed]`; message: NOT DEFINED `[Missing: Q2]` | P2 | Negative |

**Coverage summary (shortened):** AC1 → 001, 005; AC2 → 002; AC3 → 003, 004. Not covered: rounding of odd amounts after a 10% discount (rule missing, Q3), and using the same code in two tabs at once (no requirement yet; suggest adding after the PO answers). Permission does not apply (only the customer role exists). Blocked: 004, 005.

**Questions:** Q1 - What is the error message when the order is below the minimum? (BA, blocks TC-DISC-004). Q2 - What is the message when a second code is applied? (BA, blocks TC-DISC-005). Q3 - How are odd discount amounts rounded? (PO, blocks all price cases with odd values).

## Test case quality checklist (run before giving the result)

**Each test case**
- [ ] Has a matching Requirement/AC; there are no "orphan" tests
- [ ] Has one main purpose; if it fails, you know where the bug is
- [ ] Preconditions are enough for someone else to run it without guessing
- [ ] Test Data is specific (real values or a rule for making data), with boundary values for boundary cases
- [ ] Steps are numbered, one action each, and do not depend on other test cases (unless stated)
- [ ] Expected Result is measurable: values, states, messages, saved data; has a source label or `[Missing: Qn]`
- [ ] Priority and Type are filled in and fit the risk

**The whole set**
- [ ] Every requirement/AC has at least one test case, or is clearly listed as not covered with a reason
- [ ] Happy path, negative, boundary, validation, permission, state transition and error handling were all considered; any skipped type has a reason
- [ ] No two cases check the same thing; repeated data is put in a data table
- [ ] P1 focuses on high risk; not every case is P1
- [ ] No invented expected results: every gap is `[Missing: Qn]` and has a matching question
- [ ] Every Blocked test is listed in the coverage summary with its question number
- [ ] The coverage summary has a traceability table, Priority/Type counts and what is not covered
- [ ] The language matches the user; field names, states and messages stay as in the source