# Manual QA Test Design Standard

## Contents

1. Evidence and requirement states
2. UI execution order
3. Equivalence partitioning
4. Boundary value analysis
5. Decision tables
6. Test data design
7. Testcase writing
8. Cross-cutting coverage
9. Traceability and readiness
10. Review checklist

## 1. Evidence and requirement states

Classify every expected behavior:

| State | Meaning | Allowed testcase status |
|---|---|---|
| Confirmed | Explicit BRD/AC/design/config contract | Ready |
| Observed | Reproduced on the current environment | Discovery evidence; not automatically expected |
| Assumed | Proposed behavior without approval | Blocked – Awaiting requirement |
| Defect candidate | Observed behavior conflicts with confirmed requirement | Ready for reproduction/triage |

Give each confirmed requirement and assumption a stable ID. Never convert observed behavior into expected behavior without evidence.

## 2. UI execution order

Build a UI inventory before cases. Traverse:

1. page shell and global messages;
2. topmost region;
3. each row from left to right;
4. each following region from top to bottom;
5. modal/drawer content in its visual order;
6. post-action state and navigation;
7. cross-cutting checks last.

For responsive layouts, preserve semantic order even when controls collapse into menus. Record desktop and mobile order when they differ.

## 3. Equivalence partitioning

Partition inputs and state so members are expected to behave alike. Include at least:

- presence: empty, whitespace-only, populated;
- format: valid, malformed, unsupported-but-well-formed;
- state: active, inactive, pending, expired, deleted, locked;
- data source: manual, rule-based, fallback, empty, error;
- permissions/session: guest, authorized, unauthorized, expired, revoked;
- links/media: valid internal, valid external, missing, malformed, unsafe, unavailable;
- API: success with data, success empty, client error, server error, timeout, malformed response;
- security input: ordinary text, XSS-like, injection-like, CRLF, oversized input.

Assign IDs such as `EP-FEATURE-01`. Map each partition to a fixture and at least one testcase. Prefer one representative per stable partition; add more only when risk differs.

## 4. Boundary value analysis

Apply BVA wherever behavior changes at a threshold.

| Boundary kind | Required values |
|---|---|
| Minimum/maximum length | `min−1, min, min+1, max−1, max, max+1` |
| Configured count/limit N | `0, 1, N−1, N, N+1` |
| Fixed maximum 3 | `0, 1, 2, 3, 4` |
| Start/end time | `start−1s, start, start+1s, end−1s, end, end+1s` |
| Retry/lock threshold K | `0, 1, K−1, K, K+1` |
| Timeout T | `T−1s, T, T+1s` |
| Breakpoint B | `B−1px, B, B+1px` |
| Numeric zero | `−1, 0, 1` plus business min/max |
| Page boundary | first, second, penultimate, last, beyond last |

Do not choose arbitrary numbers when the threshold is unknown. Use symbols and mark affected cases blocked until the requirement/configuration is supplied.

## 5. Decision tables

Create a decision table when two or more conditions jointly determine an outcome. Use one column per rule or one row per rule, but keep the convention consistent.

Procedure:

1. List independent conditions.
2. List mutually exclusive actions/outcomes.
3. Enumerate meaningful combinations.
4. Remove impossible combinations and state why.
5. Collapse combinations only when outcomes are provably identical.
6. Assign rule IDs such as `DT-FEATURE-01-R1`.
7. Map every rule to a testcase.

Common decision tables:

- enabled × valid data × fallback;
- account exists × password correct × account state × lock state;
- authenticated × protected route × safe return URL;
- manual/rule-based × result available × fallback available;
- HTTP status/network state × retryability;
- active × in time window × priority/tie.

## 6. Test data design

Make data executable:

| Data ID | Setup/seed | Input/state | Secret reference | Expected | Cleanup |
|---|---|---|---|---|---|

Rules:

- Use deterministic QA fixtures.
- Record timezone and clock mocking for time boundaries.
- Reset counters, locks, inventory, and feature flags between boundary sets.
- Use reserved/example domains unless the environment owns a QA domain.
- Store passwords and tokens in vault/environment variables.
- Avoid production personal data.
- Map every Data ID to partitions, boundaries, or decision rules.

## 7. Testcase writing

Write observable behavior, not implementation guesses.

Each case must have:

- stable unique ID in `{FEATURE}-{AREA}-{NNN}` form;
- UI execution order;
- priority and type;
- technique and partition/rule ID;
- deterministic preconditions;
- concrete Data ID;
- numbered, minimal steps;
- exact expected result;
- automation classification;
- readiness status.

Avoid duplicate cases. One case may cover multiple techniques only when its steps and expected result prove each mapping.

## 8. Cross-cutting coverage

After the primary UI flow, cover relevant:

- session, authorization, and permissions;
- loading, empty, partial, error, retry, and recovery;
- concurrency and duplicate submission;
- data consistency across UI/API/source;
- keyboard, screen reader, focus, contrast, zoom, and touch targets;
- responsive breakpoints and supported browsers;
- transport, injection, enumeration, CSRF, session fixation, cache, and safe redirects;
- localization, timezone, currency, and Unicode;
- performance budgets and degraded networks.

Do not add irrelevant categories merely to inflate case count. Use risk and scope.

## 9. Traceability and readiness

Maintain a matrix:

| Case/range | UI order | Requirement/Assumption | Technique | Partition/Boundary/Rule | Data ID | Status |
|---|---:|---|---|---|---|---|

Allowed status examples:

- Ready;
- Ready – Manual;
- Ready – Automation candidate;
- Blocked – Awaiting requirement;
- Blocked – Missing fixture;
- Out of scope.

Blocked cases must not be included in pass-rate or release-gate calculations.

## 10. Review checklist

- UI inventory follows top-to-bottom and left-to-right order.
- Every meaningful partition has a representative.
- Every threshold has complete boundary values.
- Every multi-condition rule has a decision table.
- Every decision rule maps to a case.
- Every case has defined data.
- Expected results contain no unlinked policy/design language.
- Assumptions have IDs and blocked status.
- Test data contains no secrets or production PII.
- IDs are unique and Markdown tables are structurally valid.
- Smoke scope contains only ready P0 cases.
- Automation candidates have stable, observable assertions.
