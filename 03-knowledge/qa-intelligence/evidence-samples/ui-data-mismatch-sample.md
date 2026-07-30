# Evidence Sample: UI / Data Mismatch

Synthetic example only.

## Scope

- Case ID: DASH-METRIC-003
- Risk ID: RISK-REPORT-001
- Environment/build: staging / build `2026.07.29-rc1`

## Expected

Dashboard total should match approved source API total for selected date range.

## Actual

UI shows `128`; source API returns `126`.

## Evidence

| Evidence ID | Type | Sanitized details |
|---|---|---|
| EVD-UI-001 | Screenshot | Dashboard total card shows `128` |
| EVD-API-001 | API response | `GET /api/report?range=last7days` returns `total: 126` |
| EVD-RULE-001 | Rule | Metric rule says UI displays API `total` without client-side adjustment |

## Finding

- Severity: Medium
- Pattern: Report metric mismatch
- Suspected cause: UI aggregation/cache mismatch
- Recheck: Reload dashboard and compare UI value to API response for same range.
