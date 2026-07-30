# Freshness Policy

Review knowledge when any of these events occurs:

- A release changes the documented product area or API.
- BA/PO approves, replaces, or withdraws a business rule.
- A client, tenant, role, channel, or environment exception is introduced.
- A known issue is fixed, accepted, expires, or changes severity.
- QA evidence shows that documented current behavior is stale.

At minimum, release-critical knowledge must have a verification date and owner.
Do not silently use stale knowledge. Mark it `Needs Review` and identify the
decision or test coverage affected.
