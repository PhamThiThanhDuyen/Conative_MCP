# Choosing test types by risk

Read this in Step 6. For each type, say **choose / skip / not sure**, with a reason linked to the risks in section 4.

| Test type | Choose when | Signs in the requirement |
|---|---|---|
| Functional (main + alternative flows) | Always | Every AC |
| Validation / boundary / equivalence | There are input fields, limits, dates, money | "minimum", "maximum", formats |
| Business rule / decision table | Many conditions combine | formulas, price tables, priority rules |
| State transition | There is a lifecycle or states | approve, cancel, expire, order status |
| Negative / error handling | User or system errors are possible | error messages, timeout, rejection |
| API / integration | Calls internal or external services | webhook, payment gateway, sync |
| Data / migration | Schema or old data changes | import/export, upgrade |
| Security / authorization | Roles, sensitive data | permissions, tokens, personal info |
| Concurrency / idempotency | Parallel actions, retries | booking, stock, payment |
| Performance / load | Large volume, SLA | reports, search, batch |
| Compatibility / responsive | UI on many platforms | browsers, mobile |
| Accessibility / localization | Diverse users, many languages | i18n, regional formats |
| Usability / exploratory | New flow, many unclear points | UX not final, open requirements |
| Regression | Touches existing areas | changing an old feature, shared components |
| Notification / audit / logging | Email/SMS/log required | notifications, traceability |

## How to write section 6
1. Prioritize by risk (P1 = High risk, test early and deeply).
2. Key scenario groups: a few lines each, not full test cases.
3. Automation ideas: stable, repeated tests; API and unit level before UI.
4. Data/environment: accounts by role, boundary data, mocks for external systems, feature flags.
5. Blocked parts: say which questions in section 5 must be answered before which groups can be tested.