# Claude Conative MCP — Test Scenarios and Matrix

> Input used: [Claude Conative MCP Setup and QA Summary](Claude%20Conative%20MCP%20Setup%20and%20QA%20Summary.md), summarizing DevTak #86341 and the Claude setup guide, plus its requirement analysis | Confirmed assumptions: rules identified as `[Source]` in the summary; no unconfirmed behavior is treated as expected.

## 1. Scope and evidence

- **Requirement sources:** QA ticket #86341, Conative to Claude setup guide, and requirement analysis in the input summary.
- **Environment:** Claude app; staging MCP endpoint `https://api.conative.ai/stg-mcp-svc/mcp`; QA organization `CBI_Demo1`.
- **Confirmed requirements:** connect through OAuth; grant read-only analytics access; denied, disconnected, expired, or revoked authorization prevents data access/query; reconnect after authorization; verify MCP and Query Engine request path; run a basic prompt for metric `Gross quantity` in the `Group` column of the referenced sheet.
- **Out of scope:** Conative plugin skills/agents; Claude Code setup; response speed/performance measurement.
- **Execution order:** Follow the Claude app UI top-to-bottom and left-to-right: Settings → Connectors → Add custom connector → connector/authentication setup → Connect → Conative sign-in → organization selection → consent → return to Claude → tool invocation and result. Perform authorization state variants and cross-cutting read-only checks after the primary flow.
- **Priority basis:** P1 for core connection, authorization boundaries, data read-only protection, and core query; P2 for reconnect and expired authorization-page recovery. The exact query case is blocked pending its oracle.

## 2. Assumption register

No assumptions are used as expected behavior. Missing criteria are tracked as questions and blocked cases below.

| Assumption ID | Decision needed | Safe default recommendation | Status | Affected cases |
|---|---|---|---|---|
| None | No behavior is inferred beyond source requirements. | Keep cases blocked wherever prompt, output, or observable evidence is undefined. | N/A | Case TC-CMCP-006, TC-CMCP-008 |

## 3. UI execution order

| UI Order | Region/control | Top-to-bottom, left-to-right checks | Case IDs |
|---:|---|---|---|
| 01 | Claude Settings → Connectors | Open connector settings and select Add custom connector. | Case TC-CMCP-001, TC-CMCP-002 |
| 02 | Connector configuration | Enter exact connector name and MCP URL; preserve documented OAuth defaults. | Case TC-CMCP-001 |
| 03 | Connector status | Connect and verify authorization state. | Case TC-CMCP-001, TC-CMCP-002, TC-CMCP-003, TC-CMCP-004, TC-CMCP-005, TC-CMCP-007 |
| 04 | Conative OAuth pages | Sign in, choose `CBI_Demo1`, review read-only scope, allow/deny; check time-limited page recovery. | Case TC-CMCP-001, TC-CMCP-002, TC-CMCP-005 |
| 05 | Claude connector tools | Verify the two documented tools and invoke query/schema discovery as relevant. | Case TC-CMCP-001, TC-CMCP-006 |
| 06 | Authorization/data boundary | Attempt a write/change operation if exposed; verify data is unchanged and access is refused. | Case TC-CMCP-007 |
| 07 | Query outcome / integration evidence | Run the specified `Gross quantity` prompt and inspect agreed request evidence. | Case TC-CMCP-006, TC-CMCP-008 |

## 4. Equivalence partitions

| Partition ID | Object | Valid partitions | Invalid partitions | Representative data | Case IDs |
|---|---|---|---|---|---|
| EP-CMCP-01 | OAuth authorization state | Authorized for selected organization | Denied; disconnected; expired; revoked | `CBI_Demo1`; each authorization state | Case TC-CMCP-001–005 |
| EP-CMCP-02 | Permission capability | Read datasets/fields/metrics and query analytics | Any data-changing or editing capability | Documented read-only scope; write/change attempt | Case TC-CMCP-001, TC-CMCP-007 |
| EP-CMCP-03 | MCP/Query Engine request | Endpoint available and query reaches engine | Endpoint unavailable or request fails before engine | Staging URL; evidence mechanism TBD | Case TC-CMCP-008 |
| EP-CMCP-04 | Query input | Exact approved Gross quantity prompt | No input partitions defined; prompt itself not yet retrieved | Prompt cell in referenced sheet, currently unavailable locally | Case TC-CMCP-006 |

## 5. Boundary values

| Boundary ID | Object | Required values | Expected at boundary | Data IDs | Case IDs |
|---|---|---|---|---|---|
| BV-CMCP-01 | OAuth authorization validity | Just before expiry; at expiry; just after expiry, using configured/test clock | Access valid up to 30 days per guide; exact boundary semantics and ability to simulate are not specified | DATA-CMCP-04 | Case TC-CMCP-005 |
| BV-CMCP-02 | Organization/consent page lifetime | Before ~10-minute expiry; at expiry; after expiry | Guide says expired page requires returning to Claude and clicking Connect again; exact threshold is approximate | DATA-CMCP-05 | Case TC-CMCP-005 |

## 6. Decision tables

### DT-CMCP-01 — OAuth state and data access

| Rule | OAuth state | Read/query access expected | Source |
|---|---|---|---|
| DT-CMCP-01-R1 | Authorized for `CBI_Demo1` | Access permitted within read-only scope | `[Source]` Setup guide and summary requirement analysis |
| DT-CMCP-01-R2 | Denied | No Conative data access/query | `[Source]` Confirmed rule in requirement analysis |
| DT-CMCP-01-R3 | Disconnected | No Conative data access/query | `[Source]` Confirmed rule in requirement analysis |
| DT-CMCP-01-R4 | Expired | No Conative data access/query | `[Source]` Confirmed rule in requirement analysis |
| DT-CMCP-01-R5 | Revoked | No Conative data access/query | `[Source]` Confirmed rule in requirement analysis |

### DT-CMCP-02 — Permission scope

| Rule | Requested capability | Expected outcome | Source |
|---|---|---|---|
| DT-CMCP-02-R1 | Read datasets, fields, metrics, and query analytics | Allowed after OAuth consent | `[Source]` Setup guide |
| DT-CMCP-02-R2 | Change/edit Conative information | Must not be allowed; data must remain unchanged | `[Source]` Confirmed rule in requirement analysis |

## 7. Test data and fixtures

| Data ID | Setup/seed | Input/state | Secret reference | Expected | Cleanup |
|---|---|---|---|---|---|
| DATA-CMCP-01 | Claude app signed in; QA Conative account authorized for `CBI_Demo1`; staging MCP is configured | Connector `conative-claude`; URL `https://api.conative.ai/stg-mcp-svc/mcp`; OAuth published identity default | Use approved QA credential vault; never place password/token in artifact | Authorized read-only connection | Disconnect test connector if required by environment procedure |
| DATA-CMCP-02 | Same as DATA-CMCP-01 | OAuth consent denied | QA account only | No data access/query | Reset authorization state before next independent case |
| DATA-CMCP-03 | Connected QA account | Disconnect, then reconnect | Existing authorized QA account | While disconnected no access; reconnect can be attempted | Leave in agreed baseline state |
| DATA-CMCP-04 | Testable authorization expiry or controlled clock/fixture available | Authorization near/at/after 30-day limit | No secret value recorded | Expired authorization blocks access; exact edge behavior needs Q2 | Restore fixture/clock |
| DATA-CMCP-05 | OAuth flow started | Organization/consent page near or beyond approximately 10 minutes | QA account only | Expired page can be restarted from Claude using Connect | Restart flow; clear temporary test state |
| DATA-CMCP-06 | Referenced Google Sheet accessible | Exact prompt for metric `Gross quantity` in column `Group`; expected result | None | Exact output not available in local source; blocked pending Q1 | No data change expected |
| DATA-CMCP-07 | Connected read-only QA account and known safe QA data | Attempt any available write/edit action or documented write probe | None | Operation not allowed; persisted data unchanged | Restore only if an unexpected write succeeds, following QA data procedure |
| DATA-CMCP-08 | MCP/Query Engine observability enabled | One known prompt/query request | None | Evidence of request reaching MCP and Query Engine; evidence source needs Q3 | Remove/expire test logs only under normal retention rules |

## 8. Test scenarios

| ID | UI Order | Priority | Type | Technique | Partition/Rule | Title | Preconditions | Data ID | Steps | Expected result | Automation | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| TC-CMCP-001 | 01–05 | P1 | Integration | EP / DT | EP-CMCP-01 valid; EP-CMCP-02 read; DT-CMCP-01-R1; DT-CMCP-02-R1 | Connect Claude to Conative MCP with read-only access | Claude app signed in; QA account has access to `CBI_Demo1` | DATA-CMCP-01 | 1. Open Settings → Connectors.<br>2. Add custom connector `conative-claude` with the staging MCP URL.<br>3. Keep “Sign in now” and “Use Claude’s published identity”.<br>4. Connect and sign in to Conative.<br>5. Select `CBI_Demo1` and allow the displayed read-only scope.<br>6. Return to Claude and inspect connector tools. | Connector shows connected for `CBI_Demo1`; documented tools **Query Conative analytics** and **Discover Conative CQL schema** are available; consent scope is read-only `[Source: Setup guide; requirement analysis]`. | Manual; UI flow | Ready – Manual |
| TC-CMCP-002 | 01–04 | P1 | Permission | EP / Decision table | EP-CMCP-01 denied; DT-CMCP-01-R2 | Deny OAuth consent | Connector configuration is present; OAuth consent page displayed | DATA-CMCP-02 | 1. Start Connect for `conative-claude`.<br>2. Sign in and select `CBI_Demo1`.<br>3. Deny OAuth consent.<br>4. Return to Claude and attempt a Conative data query. | No authorized connection is established and Conative data cannot be accessed or queried `[Source: Confirmed requirement analysis]`. Exact UI message/state: NOT DEFINED `[Missing: Q4]`. | Manual; UI flow | Ready – Manual; message assertion blocked by Q4 |
| TC-CMCP-003 | 03, 07 | P1 | State transition | EP / Decision table | EP-CMCP-01 disconnected; DT-CMCP-01-R3 | Disconnect an authorized connector | Connector is initially authorized for `CBI_Demo1` | DATA-CMCP-03 | 1. Disconnect `conative-claude` in Claude/Conative using the supported control.<br>2. Attempt a Conative query. | No Conative data access/query is available while disconnected `[Source: Confirmed requirement analysis]`. Exact status/message: NOT DEFINED `[Missing: Q4]`. | Manual; UI flow | Ready – Manual; message assertion blocked by Q4 |
| TC-CMCP-004 | 03–05 | P2 | State transition | EP / Decision table | EP-CMCP-01 reauthorized; DT-CMCP-01-R1, R3 | Reconnect after disconnect | Connector was disconnected; valid QA account and organization access remain available | DATA-CMCP-03 | 1. Start Connect for `conative-claude` again.<br>2. Sign in, choose `CBI_Demo1`, and allow the read-only scope.<br>3. Return to Claude and invoke a read-only tool. | Connection returns to authorized state and read-only access is available after consent `[Source: Setup guide reconnect instruction; requirement analysis]`. Exact status label: NOT DEFINED `[Missing: Q4]`. | Manual; automation candidate if OAuth test fixture exists | Ready – Manual; exact status assertion blocked by Q4 |
| TC-CMCP-005 | 03–04 | P2 | Boundary | BVA / Decision table | BV-CMCP-01, BV-CMCP-02; DT-CMCP-01-R4 | Handle expired OAuth authorization and expired consent page | QA authorization expiry can be controlled/tested; OAuth flow can be restarted | DATA-CMCP-04, DATA-CMCP-05 | 1. Verify access before authorization expiry.<br>2. Exercise authorization at/after its configured expiry.<br>3. Attempt a query.<br>4. Separately allow the organization/consent page to expire.<br>5. Return to Claude and click Connect to restart. | After authorization expiry, Conative data cannot be accessed/queried `[Source: Confirmed requirement analysis]`. Expired organization/consent page can be recovered by returning to Claude and clicking Connect `[Source: Setup guide]`. Exact 30-day edge and ~10-minute threshold are NOT DEFINED `[Missing: Q2]`. | Manual; needs controllable clock/fixture | Blocked – Awaiting requirement / fixture (Q2) |
| TC-CMCP-006 | 05, 07 | P1 | Functional | EP / data oracle | EP-CMCP-04; prompt/output rule R4 | Run the approved Gross quantity prompt | Authorized read-only connector; referenced Google Sheet accessible | DATA-CMCP-06 | 1. Retrieve the exact prompt for metric `Gross quantity` in the `Group` column from the referenced sheet.<br>2. Submit that prompt using the documented query tool.<br>3. Compare the returned result with the approved expected output. | Exact prompt, expected values, and comparison rules: NOT DEFINED `[Missing: Q1]`; case remains blocked. | Automation candidate after oracle is defined | Blocked – Awaiting requirement (Q1) |
| TC-CMCP-007 | 06 | P1 | Security | EP / decision table | EP-CMCP-02 invalid; DT-CMCP-02-R2 | Confirm connected MCP access cannot change Conative information | Authorized read-only connector; safe QA data and a supported write probe/action exist | DATA-CMCP-07 | 1. Record the relevant QA data state.<br>2. Attempt an available operation that would change/edit Conative information.<br>3. Re-read the data state. | Write/edit capability is not allowed and the data remains unchanged `[Source: Confirmed requirement analysis]`. Specific write probe/API/tool is NOT DEFINED `[Missing: Q5]`. | Manual; API candidate if a non-destructive probe is defined | Blocked – Awaiting requirement (Q5) |
| TC-CMCP-008 | 07 | P1 | Integration | EP / evidence check | EP-CMCP-03; ticket checklist | Verify MCP availability and Query Engine invocation | Staging environment available; approved observability/log source exists | DATA-CMCP-08 | 1. Submit one approved read-only query.<br>2. Inspect the agreed MCP availability signal.<br>3. Inspect the agreed evidence that the request reached Query Engine. | Ticket requires MCP availability and Query Engine invocation to be verified, but exact signal/log and failure assertions are NOT DEFINED `[Missing: Q3]`. | API/log automation candidate | Blocked – Awaiting evidence definition (Q3) |

## 9. Traceability

| Case/range | UI Order | Requirement/Assumption | Technique | Partition/Boundary/Rule | Data ID | Status |
|---|---:|---|---|---|---|---|
| Trace: TC-CMCP-001 | 01–05 | R1 connector setup; R2 authorized read-only access | EP, integration | EP-CMCP-01 valid; EP-CMCP-02 read; DT-CMCP-01-R1; DT-CMCP-02-R1 | DATA-CMCP-01 | Ready – Manual |
| Trace: TC-CMCP-002 | 01–04 | R3 denial prevents data access | EP, decision table | EP-CMCP-01 denied; DT-CMCP-01-R2 | DATA-CMCP-02 | Ready – Manual; message assertion blocked Q4 |
| Trace: TC-CMCP-003 | 03, 07 | R3 disconnected prevents data access | EP, state transition | EP-CMCP-01 disconnected; DT-CMCP-01-R3 | DATA-CMCP-03 | Ready – Manual; message assertion blocked Q4 |
| Trace: TC-CMCP-004 | 03–05 | R1 reconnect after consent | State transition | DT-CMCP-01-R1, R3 | DATA-CMCP-03 | Ready – Manual; exact status assertion blocked Q4 |
| Trace: TC-CMCP-005 | 03–04 | R3 expired access blocked; setup guide recovery | BVA, decision table | BV-CMCP-01/02; DT-CMCP-01-R4 | DATA-CMCP-04, DATA-CMCP-05 | Blocked Q2/fixture |
| Trace: TC-CMCP-006 | 05, 07 | R4 Gross quantity prompt in `Group` column | EP, data oracle | EP-CMCP-04 | DATA-CMCP-06 | Blocked Q1 |
| Trace: TC-CMCP-007 | 06 | R2 no edits/changes | EP, security | EP-CMCP-02 invalid; DT-CMCP-02-R2 | DATA-CMCP-07 | Blocked Q5 for probe definition |
| Trace: TC-CMCP-008 | 07 | R5 MCP availability and Query Engine invocation | Integration | EP-CMCP-03 | DATA-CMCP-08 | Blocked Q3 |

## 10. Smoke scope

- **Ready P1 smoke cases:** TC-CMCP-001 and TC-CMCP-002 (core connect and denied-consent behavior). TC-CMCP-003 is executable as a manual case when starting from the authorized baseline.
- **Blocked cases are excluded from pass-rate/release-gate calculations:** TC-CMCP-005, TC-CMCP-006, TC-CMCP-007, TC-CMCP-008.

## 11. Findings and coverage gaps

- **Confirmed requirements covered:** connector setup and authorized read-only state; OAuth denial; disconnect; reconnect; expired/revoked state access rule; basic Gross quantity prompt intent; MCP/Query Engine validation intent; no data edits.
- **Blocked cases:** TC-CMCP-005 needs authorization expiry semantics and an expiry fixture (Q2); TC-CMCP-006 needs exact prompt and expected result (Q1); TC-CMCP-007 needs an approved safe write probe or visible write-capability definition (Q5); TC-CMCP-008 needs a named health/log/evidence source (Q3).
- **Missing UI assertions:** exact status labels and denial/error messages are not stated (Q4). The access-control outcomes can be checked, but message assertions must wait for clarification.
- **Test types considered:** Functional/integration, permission/security, negative, state transition and boundary apply to explicit requirements. Performance is out of scope by confirmed direction; plugin skills/agents and Claude Code are out of scope. Data migration, concurrency, responsive compatibility, accessibility/localization, notifications/audit, and general error injection are not specified and are not included.
- **Priority/type counts:** P1: 6 cases (4 Ready or partly executable; 2 Blocked); P2: 2 cases (1 Ready, 1 Blocked). Types: Integration 2, Permission 1, State transition 2, Boundary 1, Functional 1, Security 1.

## 12. Questions to clarify

| # | Question | Ask who | Which tests it blocks | Priority |
|---|---|---|---|---|
| Q1 | Which exact cell/range contains the `Gross quantity` prompt in the `Group` column, and what exact returned values/shape constitute the expected result? | PO / BA | Case TC-CMCP-006 | Blocker |
| Q2 | Can authorization expiry be simulated, and what exact expiry boundary should QA assert for the “up to 30 days” validity? Is the approximately 10-minute page timeout an exact configurable threshold? | Dev / PO | Case TC-CMCP-005 | Should have |
| Q3 | Which health endpoint, log, trace, or other observable signal should QA use to prove MCP availability and that a query reached Query Engine? | Dev | Case TC-CMCP-008 | Should have |
| Q4 | What exact connector status and user-facing message should appear after OAuth denial, disconnect, reconnect, expiry, and revocation? | Product / Dev | Exact message/status assertions in TC-CMCP-002–005 | Should have |
| Q5 | What non-destructive write/edit probe or permission evidence is approved to demonstrate that Conative information cannot be changed? | Security / Dev | Case TC-CMCP-007 | Blocker |

---

## Requirement trace IDs

| ID | Confirmed requirement |
|---|---|
| R1 | Use connector `conative-claude` and staging MCP URL; OAuth authorization through Claude connects the selected organization. |
| R2 | Access is read-only; users may read datasets, fields, metrics, and query analytics but must not change/edit information. |
| R3 | OAuth denial, disconnection, expiration, or revocation prevents Conative data access/query; reconnect is supported. |
| R4 | QA query uses prompt for metric `Gross quantity` in the `Group` column of the referenced sheet; exact prompt/output oracle remains unavailable. |
| R5 | Verify MCP availability and that the query reaches Query Engine; evidence mechanism is not specified. |
