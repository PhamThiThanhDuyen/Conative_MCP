# Testing Heuristics

Store reusable testing lenses. Heuristics suggest where to look; they do not
replace approved business rules.

## Core Lenses

| Lens | Use for | Prompts |
|---|---|---|
| CRUD lifecycle | Resource APIs and admin screens | create/read/update/delete/verify deleted |
| Auth boundary | Role/session/security | missing token, expired token, wrong role, IDOR |
| Data consistency | Dashboards/reports/workflows | UI vs API vs data source |
| Boundary values | Numeric/date/count/length limits | min-1/min/min+1/max-1/max/max+1 |
| State transitions | Workflow/status features | allowed transition, denied transition, rollback |
| Error recovery | API/UI/network failures | timeout, retry, empty, partial, server error |
| Cross-module | Multi-step business flows | upstream/downstream side effects |
| Observability | Production-informed testing | logs, traces, metrics, recent errors |

## Usage

- Apply heuristics after confirmed requirements are mapped.
- Mark heuristic-derived cases as assumptions until owner-approved if expected behavior is unknown.

## Available Guides

- `source-data-reconciliation.md`: read-only Conative-to-source comparison flow,
  Shopify coverage, required inputs, safety rules, and NuORDER/Amazon readiness.
