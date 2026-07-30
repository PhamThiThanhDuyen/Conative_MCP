# Replenishment Flow Search Test Scenarios

## 1. Scope and evidence

- Requirement source: `01-requirement-gap-and-risk.md` and canonical Product Docs.
- Scope: Replenishment Flow, Shopify, Variant view, read-only search.
- Environment: CB/I DEMO7-compatible environment; exact URL/build must be captured at execution.
- Provided owner decision: `DEC-RFS-001` selects Product Docs for the current
  Replenishment Flow no-result message.
- Observed/source-derived behavior: `OBS-RFS-001` through `OBS-RFS-005`.
- Safety: every case is `Read-only`; no backup is required unless an observed control triggers a write.
- Execution state: testcase design complete; no case has been executed.

## 2. Assumption register

| Assumption ID | Decision needed | Safe default recommendation | Status | Affected cases |
|---|---|---|---|---|
| ASM-RFS-001 | Matching semantics for partial text and identifier queries | Use exact identifier equality for the smoke case; do not classify partial behavior as a defect | Blocked - Awaiting requirement | RFS-SEARCH-006 |
| ASM-RFS-002 | Clear-input result state | Restore the same scoped rows shown immediately before search | Blocked - Awaiting requirement | RFS-SEARCH-005 |
| ASM-RFS-003 | Whitespace and Unicode normalization | Trim outer whitespace and normalize equivalent Unicode before matching | Blocked - Awaiting requirement | RFS-SEARCH-007 |
| ASM-RFS-004 | Search input length limit | Use symbolic `Lmin/Lmax` boundaries until UI/API configuration is supplied | Blocked - Awaiting requirement | RFS-SEARCH-008 |
| ASM-RFS-005 | Unauthorized and expired-session behavior | Deny access without exposing data and redirect through the approved auth flow | Blocked - Awaiting requirement | RFS-SEARCH-011 |
| ASM-RFS-006 | Loading/error/retry behavior | Distinguish loading, no results, and technical failure | Blocked - Awaiting requirement | RFS-SEARCH-012 |

## 3. UI execution order

Manual execution follows the page from top-to-bottom and left-to-right.

| UI Order | Region/control | Checks | Case IDs |
|---:|---|---|---|
| 01 | Reporting date and Distribution Channel | Capture fixed reporting scope and select Shopify | RFS-SEARCH-001 |
| 02 | Default/Reorder tab and View in | Select Default and Variant; capture forecast scope | RFS-SEARCH-001 |
| 03 | Search for Title, SKU, Barcode | Supported identifiers, no-match, partial, whitespace, boundaries, inert input | RFS-SEARCH-002 through RFS-SEARCH-009 |
| 04 | Results table or no-result state | Matching rows, exact empty-state text, absence of unrelated rows | RFS-SEARCH-002 through RFS-SEARCH-004, RFS-SEARCH-010 |
| 05 | Clear input | Recovery from matched and no-match state | RFS-SEARCH-005 |
| 06 | Session and technical states | Authorization, loading, failure, retry | RFS-SEARCH-011 through RFS-SEARCH-012 |

## 4. Equivalence partitions

| Partition ID | Input/state | Representative data | Expected classification | Case IDs |
|---|---|---|---|---|
| EP-RFS-01 | Existing exact Title | Runtime sanitized observed fixture | Valid identifier; fixture required | RFS-SEARCH-002 |
| EP-RFS-02 | Existing exact SKU | Runtime sanitized observed fixture | Valid identifier; fixture required | RFS-SEARCH-003 |
| EP-RFS-03 | Existing exact Barcode | QA-owned or approved fixture | Valid identifier; fixture required | RFS-SEARCH-004 |
| EP-RFS-04 | Ordinary text with no matching row | `CBI Test Search No Match X9Q7Z3` | Valid no-match query | RFS-SEARCH-010 |
| EP-RFS-05 | Empty value after Clear input | Empty string | Recovery behavior unresolved | RFS-SEARCH-005 |
| EP-RFS-06 | Partial title token | Token derived from fixture | Matching rule unresolved | RFS-SEARCH-006 |
| EP-RFS-07 | Whitespace-only or padded identifier | Three spaces; padded fixture SKU | Normalization unresolved | RFS-SEARCH-007 |
| EP-RFS-08 | Oversized input | Symbolic `Lmax+1` string | Limit unresolved | RFS-SEARCH-008 |
| EP-RFS-09 | Security-like text | `<script>alert(1)</script>` | Must remain inert; match outcome unspecified | RFS-SEARCH-009 |
| EP-RFS-10 | Authorized scope with no base rows | Approved empty dataset/scope | Base empty-state behavior unresolved | RFS-SEARCH-013 |
| EP-RFS-11 | Unauthorized or expired session | Approved session fixture | Access behavior unresolved | RFS-SEARCH-011 |
| EP-RFS-12 | Technical loading/error state | Approved network/error fixture | Recovery behavior unresolved | RFS-SEARCH-012 |

## 5. Boundary values

No numeric input limit is documented. Do not invent one.

| Boundary ID | Object | Required values | Expected at boundary | Data IDs | Case IDs |
|---|---|---|---|---|---|
| BV-RFS-01 | Search input length | `Lmin-1`, `Lmin`, `Lmin+1`, `Lmax-1`, `Lmax`, `Lmax+1` | Await approved limits and behavior | DATA-RFS-BOUNDARY-01 | RFS-SEARCH-008 |

## 6. Decision tables

### DT-RFS-01 - Search result state

| Rule | Authorized page | Base rows available | Query matches | Expected visible outcome | Case ID |
|---|---|---|---|---|---|
| DT-RFS-01-R1 | Yes | Yes | Yes | Matching displayed results; approved row-matching rule still required | RFS-SEARCH-003 |
| DT-RFS-01-R2 | Yes | Yes | No | `No replenishment results for this search` | RFS-SEARCH-010 |
| DT-RFS-01-R3 | Yes | No | Not applicable | Base empty-state expectation unavailable | RFS-SEARCH-013 |
| DT-RFS-01-R4 | No/expired | Unknown | Not applicable | Access/session expectation unavailable | RFS-SEARCH-011 |
| DT-RFS-01-R5 | Yes | Unknown due to error | Unknown | Error/retry expectation unavailable | RFS-SEARCH-012 |

## 7. Test data and fixtures

| Data ID | Setup/seed | Input/state | Secret reference | Expected | Cleanup |
|---|---|---|---|---|---|
| DATA-RFS-SCOPE-01 | Open Replenishment Flow read-only; select Shopify, Default, Variant; record reporting and forecast ranges | Current scoped result list | Signed-in browser session only | Scope captured before search | None |
| DATA-RFS-OBS-01 | Select one currently visible row without opening mutation controls; mask values in evidence | Runtime Title and SKU | None | Repeatable only within the recorded run | None |
| DATA-RFS-BARCODE-01 | QA/Data owner supplies a sanitized row with visible searchable barcode | Approved Barcode | None | Stable positive barcode fixture | None |
| DATA-RFS-NOMATCH-01 | Confirm the synthetic phrase is absent from visible identifiers | `CBI Test Search No Match X9Q7Z3` | None | No matching row | None |
| DATA-RFS-EMPTY-01 | Start from a completed search | Empty value after Clear input | None | Await approved clear behavior | None |
| DATA-RFS-PARTIAL-01 | Derive a non-sensitive token from DATA-RFS-OBS-01 | Partial Title token | None | Await approved matching semantics | None |
| DATA-RFS-WHITESPACE-01 | Use whitespace and padded DATA-RFS-OBS-01 SKU | Three spaces; `  <SKU>  ` | None | Await normalization rule | None |
| DATA-RFS-BOUNDARY-01 | Obtain configured input limits | Symbolic BVA set around `Lmin/Lmax` | None | Await approved limits | None |
| DATA-RFS-SECURITY-01 | No setup | `<script>alert(1)</script>` | None | Input remains inert with no navigation, execution, or persistent change | None |
| DATA-RFS-EMPTYSET-01 | Data owner identifies an approved scope with zero base rows | Empty scoped dataset | None | Await base empty-state rule | None |
| DATA-RFS-SESSION-01 | Use approved expired/unauthorized session state | No valid session | Approved secret/session mechanism | Await role/session rule | None |
| DATA-RFS-ERROR-01 | Use approved request interception or test environment failure fixture | Loading, timeout, client/server error | None | Await error/retry rule | Restore interception only |

## 8. Test scenarios

| ID | UI Order | Priority | Type | Technique | Partition/Rule | Risk ID | Title | Preconditions | Data ID | Steps | Expected result | Automation | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| RFS-SEARCH-001 | 01 | P0 | Functional | State setup | OBS-RFS-005 | RISK-RFS-003 | Establish fixed read-only search scope | Authorized signed-in session; Replenishment Flow available | DATA-RFS-SCOPE-01 | 1. Open Replenishment Flow.<br>2. Capture environment/build and reporting date.<br>3. Select Shopify, Default, and Variant.<br>4. Capture forecasting range and initial row count. | Selected scope labels are visible and the initial table or documented scoped state is captured without a write action. | Manual | Ready - Manual |
| RFS-SEARCH-002 | 03 | P0 | Functional | EP | EP-RFS-01 | RISK-RFS-001, RISK-RFS-002 | Search by exact existing Title | RFS-SEARCH-001 completed; sanitized Title captured | DATA-RFS-OBS-01 | 1. Enter the exact captured Title.<br>2. Wait for the table to settle.<br>3. Inspect every visible identifying value. | Displayed results match the documented search behavior; defect classification remains blocked until the Title matching rule is approved. | Candidate | Blocked - Missing fixture |
| RFS-SEARCH-003 | 03 | P0 | Functional | EP, decision table | EP-RFS-02; DT-RFS-01-R1 | RISK-RFS-001, RISK-RFS-002 | Search by exact existing SKU | RFS-SEARCH-001 completed; sanitized SKU captured | DATA-RFS-OBS-01 | 1. Enter the exact captured SKU.<br>2. Wait for the table to settle.<br>3. Inspect every visible row and identifier. | At least one displayed result contains the captured SKU according to the documented current behavior; unrelated-row classification awaits the approved matching rule. | Candidate | Blocked - Missing fixture |
| RFS-SEARCH-004 | 03 | P1 | Functional | EP | EP-RFS-03 | RISK-RFS-001 | Search by exact existing Barcode | Stable sanitized barcode fixture available | DATA-RFS-BARCODE-01 | 1. Enter the approved Barcode.<br>2. Wait for results.<br>3. Verify the linked fixture row through approved evidence. | The linked fixture appears in the displayed results according to the documented current behavior. | Candidate | Blocked - Missing fixture |
| RFS-SEARCH-005 | 05 | P1 | Recovery | EP | EP-RFS-05 | RISK-RFS-004 | Clear a completed search | A matched or no-match search state is visible | DATA-RFS-EMPTY-01 | 1. Select Clear input.<br>2. Wait for the table to settle.<br>3. Compare scope and rows with the pre-search capture. | Expected restoration behavior requires BA/PO confirmation; record the observed result without pass/fail. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-006 | 03 | P1 | Functional | EP | EP-RFS-06; ASM-RFS-001 | RISK-RFS-001, RISK-RFS-002 | Search with a partial Title token | Sanitized Title fixture available | DATA-RFS-PARTIAL-01 | 1. Enter the approved partial token.<br>2. Wait for results.<br>3. Capture visible identifiers. | Matching expectation is unresolved; preserve observed behavior only. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-007 | 03 | P2 | Edge | EP | EP-RFS-07; ASM-RFS-003 | RISK-RFS-001 | Search with whitespace-only and padded SKU | Sanitized SKU fixture available | DATA-RFS-WHITESPACE-01 | 1. Enter three spaces and capture the result.<br>2. Enter the padded SKU and capture the result. | Trimming and normalization expectations are unresolved; no defect classification is allowed. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-008 | 03 | P2 | Boundary | BVA | BV-RFS-01; ASM-RFS-004 | RISK-RFS-005 | Verify search-length boundaries | Approved `Lmin/Lmax` configuration available | DATA-RFS-BOUNDARY-01 | 1. Execute each symbolic boundary value after it is resolved to concrete data.<br>2. Capture acceptance, validation, timing, and result state. | Each boundary follows the approved UI/API length contract without truncation or ambiguous failure. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-009 | 03 | P1 | Security | EP | EP-RFS-09 | RISK-RFS-005 | Treat security-like search input as inert text | Authorized read-only scope | DATA-RFS-SECURITY-01 | 1. Enter the security-like string.<br>2. Observe UI, navigation, console, and resulting state.<br>3. Clear the input. | No script executes, no unexpected navigation occurs, and no persistent data change is triggered; match/no-match outcome is not asserted. | Candidate | Ready - Manual |
| RFS-SEARCH-010 | 03 | P0 | Negative | EP, decision table | EP-RFS-04; DT-RFS-01-R2 | RISK-RFS-001 | Show documented no-search-results state | RFS-SEARCH-001 completed; base rows exist | DATA-RFS-NOMATCH-01 | 1. Enter `CBI Test Search No Match X9Q7Z3`.<br>2. Wait for the result state.<br>3. Inspect the message and table. | The page displays `No replenishment results for this search`; no result row is shown for the synthetic phrase. | Candidate | Ready - Automation candidate |
| RFS-SEARCH-011 | 06 | P1 | Permission | Decision table | EP-RFS-11; DT-RFS-01-R4; ASM-RFS-005 | RISK-RFS-003 | Verify unauthorized or expired-session search access | Approved session fixture and role matrix available | DATA-RFS-SESSION-01 | 1. Open the target URL without a valid authorized session.<br>2. Observe access and exposed content. | Expected route, message, and data-visibility behavior require the approved role/session contract. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-012 | 06 | P1 | Resilience | Decision table | EP-RFS-12; DT-RFS-01-R5; ASM-RFS-006 | RISK-RFS-001 | Distinguish loading, technical failure, and no results | Approved error fixture available | DATA-RFS-ERROR-01 | 1. Trigger each approved loading/error fixture.<br>2. Observe messages, retry controls, and retained scope.<br>3. Restore normal network behavior. | Loading/error/retry expectations require an approved technical contract; a technical failure must not be reported as a passed no-match case. | Candidate | Blocked - Awaiting requirement |
| RFS-SEARCH-013 | 04 | P2 | Empty state | EP, decision table | EP-RFS-10; DT-RFS-01-R3 | RISK-RFS-003 | Review search when the base scope has no rows | Approved empty scope available | DATA-RFS-EMPTYSET-01 | 1. Open the approved zero-row scope.<br>2. Inspect the base state.<br>3. Enter a no-match query. | Base and post-search empty-state expectations require BA/PO confirmation; record both observed states separately. | Manual | Blocked - Awaiting requirement |

## 9. Traceability

| Case/range | UI Order | Requirement/Assumption | Technique | Partition/Boundary/Rule | Data ID | Status |
|---|---:|---|---|---|---|---|
| `RFS-SEARCH-001` | 01-02 | OBS-RFS-005 | State setup | Scope capture | DATA-RFS-SCOPE-01 | Ready - Manual |
| `RFS-SEARCH-002` through `RFS-SEARCH-004` | 03-04 | OBS-RFS-001, OBS-RFS-002, GAP-RFS-007 | EP | EP-RFS-01 through EP-RFS-03 | DATA-RFS-OBS-01, DATA-RFS-BARCODE-01 | Blocked - Missing fixture |
| `RFS-SEARCH-005` | 05 | OBS-RFS-004, ASM-RFS-002 | EP | EP-RFS-05 | DATA-RFS-EMPTY-01 | Blocked - Awaiting requirement |
| `RFS-SEARCH-006` through `RFS-SEARCH-008` | 03 | GAP-RFS-001 through GAP-RFS-003 | EP, BVA | EP-RFS-06 through EP-RFS-08; BV-RFS-01 | DATA-RFS-PARTIAL-01, DATA-RFS-WHITESPACE-01, DATA-RFS-BOUNDARY-01 | Blocked - Awaiting requirement |
| `RFS-SEARCH-009` | 03 | QA cross-cutting security standard | EP | EP-RFS-09 | DATA-RFS-SECURITY-01 | Ready - Manual |
| `RFS-SEARCH-010` | 03-04 | OBS-RFS-003, DEC-RFS-001 | EP, decision table | EP-RFS-04; DT-RFS-01-R2 | DATA-RFS-NOMATCH-01 | Ready - Automation candidate |
| `RFS-SEARCH-011` through `RFS-SEARCH-013` | 04-06 | GAP-RFS-005, GAP-RFS-006 | EP, decision table | EP-RFS-10 through EP-RFS-12; DT-RFS-01-R3 through R5 | DATA-RFS-SESSION-01, DATA-RFS-ERROR-01, DATA-RFS-EMPTYSET-01 | Blocked - Awaiting requirement |

## 10. Smoke scope

- `RFS-SEARCH-001`: establish and capture the fixed read-only scope.
- `RFS-SEARCH-010`: verify the documented no-match empty state.
- Promote `RFS-SEARCH-003` after a sanitized SKU fixture is captured.

## 11. Findings and coverage gaps

- Ready now: scope capture, inert security input, and documented no-match state.
- Blocked by fixture: exact Title, SKU, and Barcode positive searches.
- Blocked by requirement: partial matching, normalization, clear behavior, limits,
  authorization, base empty state, and technical recovery.
- No case mutates live or customer-owned data.
- Browser execution and evidence collection have not started.
