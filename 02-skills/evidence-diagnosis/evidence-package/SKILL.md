---
name: evidence-package
description: >-
  Package QA evidence for Conative handoff, including scope, environment,
  screenshots/video, API/network logs, data validation, trace/log findings,
  suspected causes, limitations, and reproducible recheck commands.
---

# Evidence Package

## Purpose

Turn raw QA observations into a dev-ready and release-ready evidence bundle.
Use this after manual, API, UI, or automation verification.

## Inputs

- Test results and testcase IDs
- Risk IDs and release scope
- Screenshots/video/traces/network logs/API responses
- Environment/build/version
- Known limitations or blockers

## Workflow

1. Read `03-knowledge/qa-intelligence/standards/evidence-standard.md`.
   Read `03-knowledge/governance/information-security-policy.md` before packaging
   credentials, customer data, project artifacts, or repository output.
   For a live-data mutation run, also read
   `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`.
2. Classify each item as Confirmed, Observed, Assumed, Failed, or Blocked.
3. Attach or cite evidence paths with timestamp and environment.
4. For failures, write expected vs actual and minimal reproduction.
5. Mark suspected root cause as suspected unless backed by code/log evidence.
6. Produce owner actions and recheck conditions.
7. For live-data mutations, record backup confirmation, all `CBI Test` entity
   names/IDs, restore request, and developer restore confirmation.

## Output

Use `04-templates/evidence-package.md`.

Required sections:
- Scope
- Environment/build
- Result summary
- Evidence table
- Findings
- Data/API/log validation
- Suspected root cause
- Limitations/blocked items
- Owner actions
- Recheck condition

## Done When

- Evidence is sanitized and reproducible.
- Evidence contains no plaintext authentication material and remains local or in
  the approved private Conative GitLab unless external transfer is explicitly authorized.
- Every finding has severity, owner, evidence ID, and recheck condition.
- Blocked evidence is explicit and not counted as pass/fail.
- Live mutation evidence remains Blocked until developer restoration is confirmed.
