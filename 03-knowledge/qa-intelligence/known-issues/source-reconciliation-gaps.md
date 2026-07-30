---
knowledge_id: QA-SOURCE-RECONCILIATION-GAPS
knowledge_type: qa-intelligence
source: SRC-QA-COMPARED-FIELDS
owner: QA/Data owner TBD
authority: source-derived
scope: gaps blocking reusable Shopify, NuORDER, and Amazon reconciliation
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Source Reconciliation Gaps

| Gap ID | Channel / area | Missing or unsafe information | Needed to close |
|---|---|---|---|
| GAP-RECON-001 | Source security | Original document contains plaintext credentials and credentials embedded in URLs | Revoke or rotate affected credentials, sanitize the authoritative source, and confirm incident owner |
| GAP-RECON-002 | All | Owner, approval date, effective release, environment, and last functional verification are absent | QA/Data ownership and review evidence |
| GAP-RECON-003 | All | Global `< 5%` tolerance has no denominator, zero rule, currency rule, or metric rationale | Approved per-metric tolerance contract |
| GAP-RECON-004 | All | Grain, timezone, date inclusivity, status filters, channel/location scope, and sync watermark are incomplete | Reconciliation scope contract |
| GAP-RECON-005 | Shopify | REST API version `2023-04` is historical and credential-in-URL examples are unsafe | Current approved API, version, auth method, scopes, and pagination |
| GAP-RECON-006 | Shopify | Export joins use first-match `VLOOKUP` without duplicate-key or unmatched-key controls | Deterministic aggregation and join policy |
| GAP-RECON-007 | Shopify | Collection eligibility and smart/custom overlap rules are not defined | Current collection inclusion, deduplication, pagination, and archival rules |
| GAP-RECON-008 | Metrics | Several formulas and response mappings conflict with the Data Dictionary or within the source | BA/Data decisions linked to metric IDs and mapping conflict IDs |
| GAP-RECON-009 | Data AI | Procedure is explicitly retired but replacement is not documented | Current approved AI verification workflow and versioned contract |
| GAP-RECON-010 | NuORDER | Only OpenProject `#50173` is named; no fields, steps, endpoints, grain, or tolerance are present | Import work package content and approved NuORDER mapping |
| GAP-RECON-011 | Amazon | Only OpenProject `#32737` is named; no FBA/FBM fields, steps, endpoints, grain, or tolerance are present | Import work package content and approved Amazon mapping |
| GAP-RECON-012 | Evidence | Embedded screenshots have no environment/build/freshness metadata and may expose customer data | Sanitized, dated evidence samples with tenant-safe identifiers |

## Readiness Decision

- Shopify summary and export reconciliation can support a controlled pilot after
  GAP-RECON-001 through GAP-RECON-006 are addressed or explicitly accepted.
- NuORDER and Amazon flows are not runnable from this source.
- No agent may invent missing channel mappings from Shopify similarity.
