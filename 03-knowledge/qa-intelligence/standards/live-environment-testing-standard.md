---
knowledge_id: QA-STD-LIVE-001
knowledge_type: qa-intelligence
source: User-provided Conative QA operating rules, 2026-07-30
owner: Conative QA owner
authority: provided
scope: Conative live databases and customer-connected environments
target_release: not-applicable
status: active
last_verified: 2026-07-30
supersedes: []
---

# Conative Live Environment Testing Standard

Apply this standard before designing or executing a test against a Conative live
database or an environment containing customer data.

## Non-Negotiable Rules

1. Do not modify existing customer-owned data.
2. Treat create, update, and delete operations as live-data mutations.
3. Do not execute a live-data mutation until a developer confirms that a fresh
   database backup exists for the test scope.
4. After testing, notify the developer that mutation testing is complete and
   request restoration of the database to its pre-test state.
5. Record the developer's restore confirmation. Do not assume that manual cleanup
   is equivalent to database restoration.
6. If backup or restore ownership is unclear, mark the mutation cases `Blocked -
   Awaiting live backup/restore owner` and do not execute them.

Read-only navigation, search, filtering, reporting, and data comparison do not
require a backup when they cannot persist state or trigger a write indirectly.
Verify that an apparently read-only control has no write side effect before using
this exception.

## Pre-Test Gate

Capture all required items before the first mutation:

| Gate item | Required evidence |
|---|---|
| Environment classification | Live URL, database/environment name, organization, and role |
| Mutation scope | Planned create, update, and delete cases plus affected entities |
| Customer-data protection | Confirmation that existing customer records will not be modified |
| Backup | Developer confirmation, backup time, backup identifier or reference when available, and covered database/scope |
| Restore owner | Named developer responsible for restoring the database |
| Test records | Planned `CBI Test` names and testcase IDs |

Do not proceed when any required item is missing.

## Live Naming Convention

Every report, purchase order, view, or other named persistent test entity created
on a Conative live database must start with the exact prefix `CBI Test`.

Preferred format:

```text
CBI Test - <entity> - <case-id> - <YYYYMMDD-HHmm>
```

Examples:

- `CBI Test - Report - SEARCH-001 - 20260730-1430`
- `CBI Test - PO - PO-CREATE-001 - 20260730-1430`
- `CBI Test - View - INVENTORY-FILTER-002 - 20260730-1430`

If a field has a strict length limit, retain `CBI Test` at the beginning and
shorten the remaining segments. If the system generates an immutable identifier,
apply the prefix to the user-controlled display name and record the generated ID.

## Execution Rules

- Create only the minimum records required for the approved cases.
- Update or delete only QA-owned records whose names begin with `CBI Test` and
  whose IDs are recorded in the evidence package.
- Never use an existing customer record as a mutation fixture.
- Stop immediately if a test affects unexpected customer records or scope.
- Record every created, updated, and deleted entity name and identifier.
- Do not run parallel mutation tests when they make restore scope ambiguous.

## Post-Test Restore Gate

1. Stop all mutation execution.
2. Send the developer the completion notice, mutation window, affected entity
   types, and recorded test IDs.
3. Request restoration to the confirmed pre-test backup.
4. Record the restore confirmation and timestamp.
5. Perform only an approved read-only sanity check after restoration.
6. Keep the test run `Blocked - Awaiting restore confirmation` until the developer
   confirms restoration.

## Required Evidence

- Backup confirmation and restore owner.
- Mutation start and completion timestamps.
- Testcase IDs and all `CBI Test` entity names/IDs.
- Unexpected side effects, if any.
- Restore request and developer restore confirmation.
- Read-only post-restore sanity result when performed.
