---
name: analyze-requirement-risk
description: >-
  Analyze a Conative requirement for ambiguity, missing decisions, and business
  risk, then generate a traceable Requirement Gap Register and Business Risk
  Map. Use before test design when requirements, workflows, rules, roles, data,
  or acceptance criteria need to be clarified and prioritized.
---

# Analyze Requirement Risk

## Inputs

- Requirement or release scope
- Business workflow and acceptance criteria
- Applicable business and domain knowledge
- Known constraints, dependencies, roles, and data context

## Steps

1. Read the knowledge authority and conflict rules under
   `03-knowledge/governance/` and the risk scoring standard under
   `03-knowledge/qa-intelligence/standards/`.
2. Extract requirement statements and label each claim as `Confirmed`,
   `Observed`, `Assumed`, or `Open Question`.
3. Record missing actors, preconditions, calculations, mappings, permissions,
   states, exceptions, data rules, and acceptance criteria in a Requirement Gap
   Register. Never invent a business rule to close a gap.
4. Identify the business outcome affected by each confirmed requirement or gap.
5. Score risks using the approved impact and likelihood scales; record the
   rationale, affected flow, and proposed verification.
6. Link each risk to its source requirement or gap and flag unresolved gaps that
   block test design.
7. Generate the artifact using `assets/requirement-risk-report-template.md`.

## Outputs

- Requirement Gap Register with source, classification, impact, owner, and status
- Business Risk Map with risk ID, source/gap ID, impact, likelihood, priority,
  rationale, and verification approach

Do not promote an assumption or open question into an expected test result.
