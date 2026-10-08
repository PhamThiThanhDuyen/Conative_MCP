# Test type frame and design techniques

Read this in Step 3-4. For each requirement, ask: which of these types *apply*? If a type does not apply, give the reason in the coverage summary. Do not create cases just to fill the list.

## Test type frame (Type)

| Type | Question to ask | Example |
|---|---|---|
| Happy path | Does the normal successful flow work? | Apply a valid code to an eligible order |
| Negative | Does the system reject or handle wrong data or actions correctly? | Expired code, missing required field |
| Boundary | Are values at the edge (below, on, above) handled correctly? | 199,999 / 200,000 / 200,001; length 7/8/9 |
| Validation | Is each data check right (format, length, characters, required)? | Bad email format, special characters, spaces at the start/end |
| Permission | Does each role see and do only what it should? | A user without permission calls the API, or reads another user's data |
| State transition | Do valid state changes work and invalid ones get blocked? | Delivered → Cancel |
| Error handling | When the system or a dependency fails, are the user and data safe? | Payment gateway timeout, network lost midway, API returns 500 |
| Concurrency | Can parallel or repeated actions break data? | Double click, two tabs, retry |
| Integration | Does data move correctly between systems? | Webhook, sync |
| Data | Old data, migration, saving and reading correctly | Records created before the feature launched |
| Security | Basic weaknesses related to the requirement | Injection, IDOR, leaking sensitive data |
| Usability / UI | Display, messages, loading and empty states | Empty screen, long text |

Choose only types that have a reason in the requirement or the risk. An API with no UI does not need Usability. A feature with only one role may only need a "not logged in" Permission check.

## Techniques

**Equivalence partitioning:** split input values into groups that the system treats the same way. Pick one example from each group (valid and invalid). This is the main way to avoid duplicates.

**Boundary value:** for a limit [min, max], try min-1, min, min+1, max-1, max, max+1 when risk is high. When risk is low, test just next to the edge on each side. If the requirement does not say whether the edge is included, ask - that is a question, not an assumption.

**Decision table:** when several conditions combine into different results (role × state × code type). Each valid column that is truly different is one case. Write down impossible columns and drop them.

**State transition:** draw the states and changes. Test every valid change, and a few examples of invalid changes. Watch the final states and "stuck" states.

**Error guessing:** from experience: empty, null, very long values, Unicode / accented characters, special characters, repeated clicks, lost network, old data. Add only when related to the requirement.

**Data-driven table:** when one rule applies to many values, write **one** test case and put the values in Test Data (a small table or a list) instead of many similar rows.

## Setting Priority

- **P1:** affects money, data, security or law, or is a core flow for many users; a failure blocks users completely. Run on every build / smoke test.
- **P2:** important feature with a workaround, or a common side flow. Run in regression.
- **P3:** rare cases, cosmetic, small impact. Run when there is time or before a big release.
If a risk analysis exists, start from it: High risk → P1, Medium → P2, Low → P3, then adjust for each case.

## Signs of a weak test set
- Many cases differ only by one value in the same partition
- Expected results like "the system handles it correctly"
- Everything is P1, or nothing is P1
- Negative cases with no specific message or result, because the author guessed
- A late case depends on an early case without saying so