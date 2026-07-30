---
knowledge_id: BC-CONATIVE-METRIC-GAPS
knowledge_type: business-contract
source: SRC-CONATIVE-DATA-DICTIONARY
owner: BA/Data owner TBD
authority: source-derived
scope: unresolved Conative metric contracts
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Metric Quality Gaps

These gaps block deterministic expected-value testing unless a narrower approved
contract supplies the missing rule.

## Cross-Cutting Gaps

| Gap ID | Gap | Affected scope | Required decision |
|---|---|---|---|
| GAP-MTR-001 | Owner, approver, release, and effective date are absent | All metrics | Identify accountable BA/Data owner and approval evidence |
| GAP-MTR-002 | Calculation grain is absent | All aggregates | Define product/variant/SKU/location/channel/client grain per metric |
| GAP-MTR-003 | Time semantics are incomplete | Sales, forecast, marketing | Define timezone, inclusive boundaries, partial days, comparison period, and late-arriving data |
| GAP-MTR-004 | Null, zero-denominator, negative, and missing-data handling are absent | Rates, averages, inventory cover | Define blank/zero/error behavior and data-quality treatment |
| GAP-MTR-005 | Rounding, precision, unit, and currency conversion are absent | Monetary, percentage, quantity, day metrics | Define storage and display precision plus FX source/date |
| GAP-MTR-006 | `Formula Input` is empty throughout the source | All calculated metrics | Map each symbol to source system, table/field, type, and transformation |
| GAP-MTR-007 | `Price`, `Cost`, `Discount`, `Return`, `Tax`, and `Shipping Charges` lack canonical meanings | Sales and inventory value | Define source values, signs, allocation, tax inclusion, and historical price policy |
| GAP-MTR-008 | Data freshness and recomputation behavior are absent | All metrics | Define refresh cadence, watermark, backfill, and correction behavior |

## Metric-Specific Gaps

| Gap ID | Metrics | Finding | Required decision |
|---|---|---|---|
| GAP-MTR-009 | MTR-PROD-005 | Day counting is ambiguous | Calendar vs elapsed days, first-day inclusion, unpublished/republished behavior |
| GAP-MTR-010 | MTR-PROD-006 | Grade thresholds and tie/boundary ownership are not supplied | Threshold source, ordering window, zero/negative revenue, tie handling |
| GAP-MTR-011 | MTR-SALES-001, MTR-SALES-005 | `qty * price` does not define line-level vs aggregate price behavior | Use transaction line price, list price, average price, or another source |
| GAP-MTR-012 | MTR-SALES-008..010 | Sales-day denominator and stock snapshot timing are undefined | Eligible date set, stock timezone/snapshot, zero-stock and negative-stock policy |
| GAP-MTR-013 | MTR-SALES-011 | Sell-through contract uses current stock, which may not represent available inventory during the period | Confirm intended denominator and stock point-in-time |
| GAP-MTR-014 | MTR-SALES-015 | Definition subtracts COGS and operating expenses; formula subtracts only `Cost` | Define Gross Profit and what `Cost` contains |
| GAP-MTR-015 | MTR-SALES-016 | Prose describes a value while formula returns a percentage | Confirm Gross Margin definition, numerator, and zero-Net-Sales behavior |
| GAP-MTR-016 | MTR-AI-001 | Slope thresholds for Increasing, Stable, and Decreasing are absent | Define model/input series, minimum observations, and classification thresholds |
| GAP-MTR-017 | MTR-AI-002 | Forecast formula/model and versions are absent | Define output grain, horizon, model/version, overrides, and fallback behavior |
| GAP-MTR-018 | MTR-INV-001 | `Override Quantity OR Forecasted Sales` precedence is ambiguous | Define override semantics, forecast interval, rounding, MOQ, and caps |
| GAP-MTR-019 | MTR-INV-004, MTR-INV-005 | `AI Not Yet`, `AI Stock Date`, and `maximum forecast value` are undefined | Define fields, units, horizon, and branch precedence |
| GAP-MTR-020 | MTR-INV-008, MTR-INV-009 | ROP and XX-Day Sales have no formulas | Supply lead-time, safety-stock, sales-window, and fallback rules |
| GAP-MTR-021 | MTR-INV-010, MTR-INV-011 | MOQ allocation lacks contribution window, rounding, remainder, and zero-sales rules | Define deterministic allocation algorithm |
| GAP-MTR-022 | MTR-INV-012..013 | Active locations and open PO statuses are not enumerated | Supply location and PO state mappings plus cancellation/over-receipt behavior |
| GAP-MTR-023 | MTR-INV-015, MTR-INV-016 | Nearest arrival selection and tie/cancelled/late shipment handling are absent | Define eligible inbound records and deterministic selection |
| GAP-MTR-024 | MTR-INV-017..021 | Amazon source fields, statuses, and synchronization semantics are absent | Supply Amazon-to-Conative field/status mapping and freshness SLA |
| GAP-MTR-025 | MTR-INV-022, MTR-INV-023 | FBA recommendation calculations are absent | Supply demand, lead time, buffers, transit, rounding, and fallback rules |
| GAP-MTR-026 | MTR-MKT-002 | Definition is visitor/order conversion, but formula is units/page views and can exceed 100% | Choose event grain and numerator/denominator contract |

## QA Use Rule

- Use a `usable` formula for initial test design only with explicit source citation.
- For `partial`, add cases around the known formula and mark unresolved branches as
  requirement gaps.
- Do not assert exact expected values for `missing` or `conflict` entries until an
  approved decision resolves the listed gap.
- When a decision is approved, create a decision record or revised contract,
  update readiness, and retain this source-derived history.
