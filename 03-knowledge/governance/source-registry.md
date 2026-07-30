# Source Registry

Register a source before relying on it as canonical knowledge.

| Source ID | Source | Knowledge type | Owner | Authority | Scope | Location | Status |
|---|---|---|---|---|---|---|---|
| SRC-CURRENT-PRODUCT-DOCS | Conative product docs at `b375c3b0407dd5335aa082121c58368cdbb94ee0` | Current product | TBD | Verified current behavior | User-visible behavior | `00-sources/product-docs/docs/product` submodule | Active |
| SRC-BA-BUSINESS-CONTRACTS | BA/PO-approved business documents | Business contract | BA/PO | Approved expected behavior | Per document | `business-contracts/` | Pending owner confirmation |
| SRC-BA-CONATIVE-3-SERVICES-USE-CASES | Conative 3.0 - Services & Use cases, documentation code v3.0.0 | Business contract | Frank Tran (author); approval owner TBD | Provided, approval not evidenced | Conative 3.0 services and use cases | `00-sources/ba/Conative 3.0 - Services & Use cases.md`; SHA-256 `C77B9B2DE139729B7EBF3874FB3666AF93880755276988E49CF5C2AB6D26F360` | Needs review |
| SRC-CONATIVE-DATA-DICTIONARY | Google Sheet `Data Dictionary`, spreadsheet ID `1-rpKEDAqHpGWyVlFEfoscgjfSXsvEAH10fE48YWv7DY`, tab `Sheet1` | Business contract | BA/Data owner TBD | Provided, approval not evidenced | Conative product, sales, forecast, inventory, and marketing metrics | [Google Sheet](https://docs.google.com/spreadsheets/d/1-rpKEDAqHpGWyVlFEfoscgjfSXsvEAH10fE48YWv7DY/edit?gid=0#gid=0); normalized at `business-contracts/conative-metrics/` | Needs review |
| SRC-QA-COMPARED-FIELDS | `Docs_Comparedfield.md`, local source supplied 2026-07-30 | QA operating knowledge and legacy field mappings | QA/Data owner TBD | Provided, approval and freshness not evidenced | Shopify reconciliation; legacy metric checks; NuORDER and Amazon placeholders | Original intentionally not copied because it contains plaintext credentials; SHA-256 `D93140CFF04C190D788D7B9A5A75C06B1EEEEC3CA5F61AACD95CCCFFCDEB1B3D` | Restricted; needs sanitization and review |
| SRC-INDUSTRY-DOMAIN | Approved domain references | Industry domain | BA/domain expert | Advisory | Per source | `industry-domain/` | Pending source registration |
| SRC-QA-INTELLIGENCE | Conative QA knowledge | QA intelligence | QA owner | QA operating authority | QA execution | `qa-intelligence/` | Active |
| SRC-QA-LIVE-OPERATING-RULES | User-provided live-data testing rules, 2026-07-30 | QA intelligence | Conative QA owner | Provided operating rule | Live/customer-connected environments | `qa-intelligence/standards/live-environment-testing-standard.md` | Active |
| SRC-TEAM-SECURITY-RULES | User-provided team security rules, 2026-07-30 | Governance policy | Conative team owner | Provided operating rule | All project information and authentication material | `governance/information-security-policy.md` | Active |
| SRC-TEAM-CAPABILITY-APPROVAL-RULES | User-provided Skill and Knowledge approval rule, 2026-07-30 | Governance policy | Conative QE owner | Provided operating rule | Creation, update, approval, installation, and publication of Skills and Knowledge | `governance/change-approval-policy.md` | Active |

For each external source, record a stable repository or document identifier when
available. A local path is a convenience pointer, not a portable source identity.
