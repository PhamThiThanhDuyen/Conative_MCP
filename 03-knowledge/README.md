# Conative QE Knowledge

This directory separates what Conative currently does, what approved business
contracts require, what the industry suggests, and what QA has learned. Skills
must select knowledge by authority and scope instead of treating every document
as an equally strong source of expected behavior.

## Structure

| Layer | Purpose | Testing authority |
|---|---|---|
| `current-product/` | Verified current implementation, product docs, architecture, deployed API contracts, and reference data | Regression baseline and implementation evidence; not proof that behavior is correct |
| `business-contracts/` | BA/PO-approved requirements, acceptance criteria, formulas, permissions, state transitions, and business rules | Primary expected behavior for the stated target release and scope |
| `industry-domain/` | Industry concepts, terminology, common operating rules, and domain constraints | Context for risk analysis and requirement-gap questions; not a pass/fail oracle by itself |
| `qa-intelligence/` | QA standards, heuristics, defect patterns, known issues, and evidence examples | Governs QA execution and records reusable QA learning |
| `governance/` | Source registry, authority, metadata, conflict resolution, freshness, and decision policy | Determines which knowledge may be used and how conflicts are handled |

## Task Routing

| QA task | Required knowledge |
|---|---|
| New feature verification | Approved business contract, relevant industry domain, API expectations, and QA standards |
| Regression testing | Current product baseline, known issues, defect patterns, and QA standards |
| Bug investigation | Business contract, current product evidence, known issues, and captured evidence |
| API or contract testing | Business rules, current API specification, contract-change rules, and API testing standard |
| Release decision | Test evidence, approved deviations, known issues, risk rules, and release-decision standard |
| Client-specific testing | Global contract plus approved client-specific rules and exceptions |

## Mandatory Rules

- Read `governance/source-registry.md` and `governance/authority-matrix.md` before treating a source as authoritative.
- Do not infer correctness from current implementation. Current behavior may contain a defect.
- Do not turn industry practice into expected behavior unless BA/PO has adopted it in an approved business contract.
- When credible sources disagree, follow `governance/conflict-resolution.md`; do not silently choose one.
- Mark missing or unapproved expected behavior as `Requirement Gap` or `Open Question`.
- Cite requirement, rule, risk, issue, evidence, and source IDs where possible.
- Apply `governance/knowledge-metadata-standard.md` to new knowledge documents.
- Apply `governance/information-security-policy.md` before handling credentials,
  project information, repositories, or external transmission.
