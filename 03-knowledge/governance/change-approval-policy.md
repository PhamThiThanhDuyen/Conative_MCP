---
knowledge_id: GOV-SKILL-KNOWLEDGE-CHANGE-APPROVAL
knowledge_type: governance-policy
source: SRC-TEAM-CAPABILITY-APPROVAL-RULES
owner: Conative QE owner
authority: provided
scope: all Skill and Knowledge changes in the Conative QE Codex Kit
target_release: not-applicable
status: active
last_verified: 2026-07-30
supersedes: []
---

# Skill And Knowledge Change Approval

This policy applies before a Skill or Knowledge item is installed, published,
used as an approved test oracle, or promoted for team-wide reuse.

## Change Classes

| Class | Examples | Required review |
|---|---|---|
| Editorial | Typo, formatting, link repair with no semantic change | Owner review; automated checks |
| Behavioral | Trigger, steps, inputs, outputs, formula, rule, scope, authority, or artifact behavior changes | Author plus one qualified reviewer |
| High-risk | Security, credentials, live data, customer data, release decision, destructive operation, external transmission, or cross-team contract | Author, qualified reviewer, accountable domain/security owner |

If classification is uncertain, use the higher class. The author cannot be the
sole approver of a behavioral or high-risk change.

## Skill Lifecycle

```text
Need identified
→ overlap and capability check
→ draft or baseline
→ implementation
→ deterministic validation
→ forward evaluation
→ human review
→ approval record
→ install or publish
```

### Skill Gates

1. **Need and boundary**: state the outcome, trigger examples, owning capability,
   expected artifact, and why an existing Skill cannot absorb the change.
2. **Separation**: keep one responsibility; move business/domain facts into
   governed Knowledge and deterministic repeated logic into scripts.
3. **OpenAI shape**: keep `SKILL.md` concise, discoverable, and progressively
   disclose references, scripts, and assets. Do not add approval status to Skill
   frontmatter unless OpenAI supports that field.
4. **Baseline**: for an update, run the size validator before editing and retain
   the result. Preserve user changes and existing artifact contracts unless a
   breaking change is explicitly approved.
5. **Validation**: run the repository size validator, OpenAI Skill validator when
   available, skill-local validators, link/path checks, and credential scan.
6. **Evaluation**: execute at least one normal case and one failure, missing-input,
   or existing-artifact update case. Confirm the Skill creates its promised
   artifact and does not invent business rules.
7. **Review**: the capability owner reviews responsibility, composability,
   discoverability, inputs, outputs, human gates, and failure behavior. Add a
   security/domain reviewer when the change class requires one.
8. **Promotion**: record approval before installation, team-wide publication, or
   claiming the Skill is approved. Rejected changes stay uninstalled and must
   retain the rejection reason.

## Knowledge Lifecycle

```text
Source identified
→ source registered
→ raw source preserved or safely referenced
→ normalized Knowledge drafted
→ metadata and conflict review
→ content-owner review
→ approval record
→ active use at its approved authority
```

### Knowledge Gates

1. **Source**: register a stable source ID, owner, location, scope, authority, and
   status. Do not copy plaintext credentials or unsafe customer data into the kit.
2. **Metadata**: assign a unique stable `knowledge_id` and all fields required by
   `knowledge-metadata-standard.md`.
3. **Boundary**: place intended behavior in Business Contracts, observed behavior
   in Current Product, context in Industry Domain, execution knowledge in QA
   Intelligence, and decision policy in Governance.
4. **Normalization**: preserve source meaning, identify inferences, and list
   missing formula inputs, mappings, grain, exceptions, and freshness.
5. **Conflict and freshness**: compare overlapping sources and use the conflict
   policy. Never silently replace a stronger or newer approved decision.
6. **Validation**: check metadata, unique IDs, internal links, sensitive data,
   duplicated rules, and referenced source availability.
7. **Content approval**: BA/PO or domain owner approves intended business behavior;
   Product/Engineering owner verifies current behavior; QA owner approves QA
   operating knowledge; Security owner approves security policy.
8. **Authority promotion**: only set `authority: approved` with identifiable
   approver, approval date, scope, and evidence. `status: active` means available
   for use; it does not automatically mean approved business truth.
9. **History**: supersede or add a decision record when meaning changes. Do not
   erase material decision history.

## Approval Decision

An approval record must answer:

- What changed and why?
- Is it Skill or Knowledge, and what is its stable ID/path?
- What change class applies?
- Which checks and evaluations passed?
- Who reviewed domain meaning, QA usability, and security when applicable?
- What scope, authority, release, and effective date were approved?
- Is the decision Approved, Approved with Conditions, Rejected, or Superseded?

`Approved with Conditions` must name an owner, condition, and review date. It
must not be represented as fully approved after the condition expires.

## Breaking Changes

A change is breaking when it removes or renames an input/output, changes artifact
semantics, changes a business formula or authority, changes failure behavior, or
invalidates an existing Goal/Skill reference. Update all consumers, demos,
templates, evaluations, and documentation in the same change. Record migration
impact and approval before promotion.
