# Replenishment Flow Search - Requirement Gap And Risk

## Scope And Sources

| Field | Value |
|---|---|
| Feature | Replenishment Flow Search |
| Demo scope | Shopify, Variant view, read-only search |
| Product source | `docs/product/features/inventory-buying/replenishment-flow.md` |
| Source authority | Source-derived current product behavior; not an approved business contract |
| Execution state | Test design only; browser execution not started |

## Evidence Classification

| ID | Classification | Statement | Source |
|---|---|---|---|
| OBS-RFS-001 | Observed/source-derived | Search accepts a title, SKU, or barcode through `Search for Title, SKU, Barcode` | Product Docs, Search section |
| OBS-RFS-002 | Observed/source-derived | The table shows matching displayed results | Product Docs, Search section |
| OBS-RFS-003 | Observed/source-derived | A no-match query displays `No replenishment results for this search` | Product Docs, Search section |
| OBS-RFS-004 | Observed/source-derived | Clear input and forecasting-range adjustment are visible recovery choices | Product Docs, Search section |
| OBS-RFS-005 | Observed/source-derived | The documented behavior is scoped to Shopify in CB/I DEMO7 on 2026-07-26 | Product Docs scope statement |

No approved BA requirement or acceptance criteria were available. A difference
from an observed statement is a documentation/current-behavior finding, not an
approved business defect, until an accountable owner confirms the expectation.

## Requirement Gap Register

| Gap ID | Missing decision | Business impact | Recommendation | Owner | Status |
|---|---|---|---|---|---|
| GAP-RFS-001 | Exact, prefix, substring, case-sensitive, and token matching rules | Valid products may be omitted or unrelated rows may appear | BA/PO defines matching semantics per identifier | BA/PO | Open |
| GAP-RFS-002 | Trimming, Unicode normalization, and whitespace-only behavior | Equivalent user input may return inconsistent results | Define normalization before matching | BA/PO + Engineering | Open |
| GAP-RFS-003 | Minimum/maximum input length and oversized-query behavior | UI or API may become slow or reject input inconsistently | Publish UI/API limits and response behavior | Engineering | Open |
| GAP-RFS-004 | Expected state after Clear input | User may remain in an empty or stale result state | Confirm whether scoped unfiltered rows must return | BA/PO | Open |
| GAP-RFS-005 | Role and permission behavior | Search availability may differ across users | Provide role-permission matrix | BA/PO + Engineering | Open |
| GAP-RFS-006 | Loading, timeout, API error, retry, and recovery states | Failure may be mistaken for no results | Define observable error and retry behavior | Engineering | Open |
| GAP-RFS-007 | Stable sanitized Title/SKU/Barcode fixture | Positive cases cannot be repeated deterministically | Provide QA-owned fixture or approve read-only runtime discovery | QA + Engineering | Open |

## Business Risk Map

| Risk ID | Gap/Source | Failure mode | Business impact | Likelihood | Priority | Verification approach | Status |
|---|---|---|---|---|---|---|---|
| RISK-RFS-001 | OBS-RFS-002, GAP-RFS-001 | Search omits a matching replenishment row | User may miss an item requiring review or reorder | Medium | High | Exact identifier and approved partial-match cases | Open |
| RISK-RFS-002 | OBS-RFS-002, GAP-RFS-001 | Search displays rows unrelated to the query | User may act on the wrong item | Medium | High | Assert every visible identifying value against the approved matching rule | Open |
| RISK-RFS-003 | OBS-RFS-005 | Search is executed under the wrong channel, grain, date, or forecast scope | Result appears valid but answers a different business question | Medium | High | Capture all scope controls in preconditions and evidence | Mitigated in design |
| RISK-RFS-004 | OBS-RFS-004, GAP-RFS-004 | Clear input does not restore the scoped result list | User cannot recover from a search without reloading | Low | Medium | Clear after matching and no-match queries | Open |
| RISK-RFS-005 | GAP-RFS-002, GAP-RFS-003 | Special or oversized input causes unsafe execution, crash, or persistent side effect | Security or availability impact | Low | High | Inert security string and symbolic boundary coverage | Open |

## Safety Decision

All designed cases are read-only. Do not select bulk actions, edit values, export,
create a purchase order, or use any control that can persist data during this demo.
