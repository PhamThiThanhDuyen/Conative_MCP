---
name: residual-risk-assessment
description: >-
  Assess remaining release risk after verification by scoring impact,
  likelihood, evidence confidence, coverage gaps, blocked items, and owner
  acceptance. Use before go-no-go-report.
---

# Residual Risk Assessment

## Purpose

Convert verification gaps into explicit release risk so QA does not hide
unknowns behind a pass percentage.

## Inputs

- Risk Map
- Testcase Matrix
- API/UI/data verification results
- Evidence Package
- Open defects and blocked assumptions

## Workflow

1. Read `03-knowledge/qa-intelligence/standards/release-decision-standard.md`.
2. List unresolved failures, blocked cases, missing evidence, and open assumptions.
3. Score each residual risk:
   - Impact: 1-5
   - Likelihood: 1-5
   - Evidence confidence: High / Medium / Low
   - Blast radius: user segment, module, data, revenue, compliance
4. Classify release action:
   - No-Go
   - Conditional Go with owner acceptance
   - Go with monitored residual risk
5. Define mitigation, owner, and recheck trigger.

## Output

| Risk ID | Source | Impact | Likelihood | Score | Evidence confidence | Release action | Owner | Mitigation | Recheck |
|---|---|---:|---:|---:|---|---|---|---|---|

## Done When

- No Critical/High residual risk is ownerless.
- Every blocked item has a decision owner.
- The final recommendation can cite why the remaining risk is accepted or blocking.
