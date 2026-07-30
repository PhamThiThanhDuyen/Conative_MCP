---
name: testcase-matrix-design
description: Design, review, or revise Conative execution-ready manual QA test scenarios, testcase matrices, and test data from requirements, risk maps, BRDs, user stories, live-product discovery, screenshots, or incomplete specifications. Use when Codex must apply equivalence partitioning, boundary value analysis, decision tables, top-to-bottom/left-to-right UI execution order, requirement and assumption tracking, concrete test fixtures, traceability, priorities, or manual-versus-automation classification.
---

# Manual QA Test Design

## Goal

Produce a test suite that another QC can execute without guessing. Treat equivalence partitioning (EP), boundary value analysis (BVA), decision tables, concrete test data, and UI execution order as mandatory—not optional enrichments.

In the `qe-release-readiness` goal, this skill converts confirmed requirements, open assumptions, and the Risk Map into the required Testcase Matrix artifact.

## Required workflow

1. Inspect available requirements, existing tests, designs, live UI, API evidence, and data contracts.
   Read `03-knowledge/governance/information-security-policy.md` when the scope
   includes login, credentials, customer data, project artifacts, repositories,
   or external transmission.
   If the target is live or customer-connected, read
   `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`
   and classify every case as `Read-only` or `Mutation`.
2. Record three categories separately:
   - confirmed requirement;
   - directly observed behavior;
   - assumption or unresolved decision.
3. Inventory UI controls from top to bottom and left to right. Use this order for manual execution and testcase numbering.
4. Build an equivalence-partition matrix before writing cases.
5. Build a boundary matrix for every count, length, time, price, threshold, pagination, retry, and session value.
6. Build decision tables for behavior controlled by two or more conditions.
7. Define concrete test fixtures and expected outcomes. Reference secrets through vault/environment keys only.
8. Write cases in UI order. Add cross-cutting security, accessibility, responsive, browser, resilience, and performance coverage after the UI flow.
9. Map every case or case range to its partition, boundary, decision rule, data ID, requirement/assumption, and readiness status.
10. Validate the Markdown artifact with `scripts/validate_testcase_design.py`; fix every error before delivery.

Read [references/test-design-standard.md](references/test-design-standard.md) before designing or reviewing a suite. Use [assets/testcase-template.md](assets/testcase-template.md) as the starting structure when creating a new artifact.

## Mandatory case schema

Use these columns unless an existing repository has a stronger schema:

| ID | UI Order | Priority | Type | Technique | Partition/Rule | Title | Preconditions | Data ID | Steps | Expected result | Automation | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|

Use testcase IDs in `{FEATURE}-{AREA}-{NNN}` form, for example `LOGIN-EMAIL-001` or `HOME-HERO-003`. Use `{DT-ID}-R1` for individual decision rules.

Keep steps observable and expected results deterministic. Do not use phrases such as “theo policy”, “theo thiết kế”, “hoạt động đúng”, or “phù hợp” without a linked, approved requirement/assumption ID.

## Requirement gaps

When requirements are missing:

- discover the visible flow safely;
- record facts as observations, not requirements;
- assign unresolved behavior an assumption ID;
- provide a safe default recommendation;
- mark affected cases `Blocked – Awaiting requirement`;
- exclude blocked cases from pass/fail and release gates.

Do not invent exact limits. Use symbolic boundaries such as `N−1/N/N+1`, `Pmin−1/Pmin/Pmin+1`, or `T−1s/T/T+1s` until configuration is confirmed.

## Test data rules

- Cover every valid and invalid equivalence partition with at least one fixture.
- Cover every boundary tuple explicitly.
- Give each fixture a stable Data ID and expected outcome.
- Include setup/seed state and cleanup needs.
- Never store real credentials, tokens, OTPs, personal data, or production identifiers.
- Use reserved domains or QA-owned accounts and secret references.
- Never include plaintext authentication material in testcases or fixtures; use
  approved secret references only.
- On a Conative live database, never modify customer-owned data. Block mutation
  cases until developer backup and restore ownership are confirmed, and prefix
  every named persistent test entity with `CBI Test`.

## Review gate

Reject or return a suite for rework when any condition is true:

- EP, BVA, or decision-table artifacts are missing where applicable;
- testcase order does not follow the UI;
- decision combinations are represented only by ad-hoc cases;
- data is described only as “valid/invalid” without fixtures;
- expected results are ambiguous;
- case IDs or Data IDs are duplicated or undefined;
- blocked assumptions are counted as ready;
- secrets appear in the artifact;
- traceability cannot prove coverage.

## Validation

Run:

```powershell
python scripts/validate_testcase_design.py <testcase-file.md>
```

Resolve validator errors. Treat warnings as review items and explain any accepted exception in the final handoff.
