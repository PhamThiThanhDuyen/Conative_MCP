---
knowledge_id: BC-CONATIVE-3-QUALITY-GAPS
knowledge_type: business-contract
source: SRC-BA-CONATIVE-3-SERVICES-USE-CASES
owner: BA/PO owner TBD
authority: source-derived
scope: quality and approval gaps in the supplied Conative 3.0 document
target_release: Conative 3.0
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Contract Quality Gaps

These are source-quality findings, not product defects.

| Gap ID | Finding | Impact | Required decision |
|---|---|---|---|
| BCG-001 | No approval status, approver, or approval date | Rules cannot automatically become release-blocking expected behavior | BA/PO confirms approval and applicable release |
| BCG-002 | Declared last modified is 2023-07-27, while change records include 2023-07-31 | Source version is internally inconsistent | Identify canonical revision and change history |
| BCG-003 | UC 1.5 has a heading but no detailed contract | Update-name behavior cannot be tested from this source | Supply objective, inputs, workflow, rules, and AC |
| BCG-004 | UC 3.3.2 is labeled `deUC`; UC 4.5.3 is labeled `reUC` | Automated discovery and traceability may miss these UCs | Correct stable UC identifiers |
| BCG-005 | UC 4.1.8 and `4.1.8_new` coexist; UC 10.2 is duplicated | References can resolve to the wrong contract | Assign unique IDs and supersession links |
| BCG-006 | UC 4.1.12-4.1.16 are struck out but remain in the document | Retired scope may be treated as active | Mark formally retired/superseded with replacement IDs |
| BCG-007 | UC 6.4 says Updating; Archive PO says Pending; one payment flow says on hold | Incomplete behavior may enter Ready test scope | Define release inclusion and acceptance status |
| BCG-008 | UC 4.2.1 Category and UC 4.3.1 Collection inputs name Category/Collection, but business rules list Product Title/SKU/Barcode | Search expectations conflict within each UC | BA corrects copied rules and defines actual fields |
| BCG-009 | UC 11.3 Sales by Month workflow names Replenishment Flow | Test navigation target is ambiguous | Correct source page and expected result scope |
| BCG-010 | Search uses `search gần đúng` without algorithm, case, whitespace, Unicode, ranking, or length rules | Boundary and deterministic matching tests remain incomplete | Define searchable fields and matching semantics |
| BCG-011 | BA no-result messages differ from current Product Docs | Resolved for Replenishment Flow by `BC-CONATIVE-3-DEC-RFS-EMPTY`; other areas may still represent planned change, stale requirement, or regression | Apply the scoped decision; BA/PO resolves remaining areas separately |
| BCG-012 | Listed Authorization, Notification, Tenancies, and Event services lack dedicated use cases | Service contracts are not testable | Supply detailed contracts or remove from release scope |

## QA Handling

1. Use stable Rule/UC IDs only after ambiguity is resolved.
2. Keep affected cases `Blocked - Awaiting requirement` when expected behavior
   depends on a listed gap.
3. Compare supplied BA intent with current product knowledge and target release.
4. Do not rewrite the source file; resolve gaps through an approved BA/PO update.
