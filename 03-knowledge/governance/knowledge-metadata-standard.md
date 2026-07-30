# Knowledge Metadata Standard

Add this frontmatter to new authoritative knowledge documents:

```yaml
---
knowledge_id: <stable unique ID>
knowledge_type: <current-product|business-contract|industry-domain|qa-intelligence|governance-policy>
source: <source ID or evidence pointer>
owner: <accountable role or person>
authority: <draft|provided|source-derived|verified-current-behavior|approved|advisory>
scope: <global, client, tenant, role, channel, environment, or product area>
target_release: <release, current, or not-applicable>
status: <draft|active|needs-review|superseded|retired>
last_verified: YYYY-MM-DD
supersedes: []
---
```

Requirements:

- Keep `knowledge_id` stable across edits.
- Use `scope` to prevent tenant- or role-specific behavior from becoming universal.
- Use `authority: approved` only with identifiable approval evidence.
- Use `source-derived` for a normalized summary that remains bounded by its
  named source and has not been independently verified against the product.
- Use `verified-current-behavior` for observed implementation, not intended correctness.
- Link superseded documents instead of deleting decision history.
