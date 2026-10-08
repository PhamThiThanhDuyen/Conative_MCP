# Checklist: finding unclear points, gaps and risks

Read this file in Step 3-4. For a small requirement you do not need every line; pick the groups that fit.

## Signs of unclear language
- Words that cannot be measured: fast, many, suitable, user-friendly, on time, reasonable, often, "etc.", "similar"
- Verbs with no subject: "is sent", "is updated" (who or which system does it? when?)
- Unclear pronouns: "it", "that item", "as above"
- "Can/should" mixed with "must" (is it required or optional?)
- Conditions with no else branch: "if A then X" but nothing for "not A"

## Data and validation
- Type, format, length, allowed characters, required/optional, default value
- Boundary values (min/max, dates and times, time zones, rounding, currency, decimals)
- Exact error messages, language, where they appear
- Duplicates, empty values, null, special characters, very long text, Unicode / accented characters

## States and lifecycle
- List of states, which changes are allowed, who can make them
- "Stuck" states with no way out; actions on deleted/cancelled/expired records
- Behavior with existing data when the new feature is released (migration, backward compatibility)

## Permissions and security
- Which roles can view/create/edit/delete; access to other users' data (IDOR)
- Sensitive data (personal info, payment), masking/encryption, logs, audit trail
- Session timeout, not logged in, brute force, injection in input fields

## Concurrency and reliability
- Two users or two tabs on the same record; double click; retry; idempotency
- External system errors, slow responses or strange data; timeouts; partial rollback
- Background jobs, queues, event order, duplicate notifications

## Often-forgotten non-functional needs
- Performance and volume (number of records, number of users), pagination
- Compatibility (browsers, devices, app versions), responsive layout
- Accessibility, multiple languages, date and currency formats by region
- Observability: logs, metrics, alerts; feature flags, rollback

## Conflicts and scope
- Compare the description with each AC, with the design/mockup, and with related documents
- "Out of scope" items mixed into ACs, or dependencies on other tickets/teams that are not done
- Old features that may be affected (regression area)

## Rating the risk level
- **High:** affects money, user data, security or legal matters, or spreads widely and is hard to roll back; or is likely to happen in the main flow
- **Medium:** affects one user group or a side flow, and a workaround exists
- **Low:** cosmetic, rare, small impact, easy to fix
Always write a short *reason* so others can challenge it.