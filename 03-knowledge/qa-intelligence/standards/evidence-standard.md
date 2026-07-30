# Conative Evidence Standard

## Evidence Must Include

| Field | Requirement |
|---|---|
| Scope | Feature, release, testcase ID, risk ID |
| Environment | URL, build/version, branch, account role, device/browser when UI |
| Steps/command | Minimal reproducible path or command |
| Expected | Approved requirement, AC, contract, or owner decision |
| Actual | Observed result, status, response, UI state, data state |
| Artifact | Screenshot, video, trace, console/network log, API response, query output |
| Timestamp | When evidence was captured |
| Owner action | Who must decide/fix/recheck |

For live-data mutation tests, also include backup confirmation, restore owner,
all `CBI Test` entity names and IDs, mutation completion notice, restore request,
and developer restore confirmation.

## Evidence States

- Confirmed: backed by approved requirement/spec/rule.
- Observed: seen in current environment only.
- Assumed: proposed but awaiting approval.
- Failed: observed conflict with confirmed expectation.
- Blocked: cannot verify due to missing access/data/env/decision.

## Sanitization Rules

- Mask tokens, cookies, passwords, OTPs, secret keys, internal customer data, and real PII.
- Use synthetic or QA-owned identifiers.
- Summarize sensitive payloads instead of copying raw values.
- Never persist plaintext authentication material in an evidence artifact.
- Store project evidence locally or in the approved private Conative GitLab only.
  Do not send it to an external destination without explicit authorization.

## Bug Evidence Format

| Field | Content |
|---|---|
| Summary | One-line failure |
| Environment/build | Exact tested target |
| Steps | Minimal reproduction |
| Expected | Requirement-backed expectation |
| Actual | Observed failure |
| Evidence | Paths or IDs |
| Suspected cause | Mark as suspected unless confirmed |
| Impact | User/business/release impact |
| Recheck | Command or steps to verify fix |
