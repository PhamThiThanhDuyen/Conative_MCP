# Architecture Knowledge

Store system knowledge that helps QA understand what can break and where to collect evidence.

## Files To Add

| File | Purpose |
|---|---|
| `system-map.md` | Product/module map and ownership |
| `data-flow-map.md` | Data movement across UI/API/services/database/reporting |
| `dependency-map.md` | Third-party/internal dependencies and failure behavior |
| `environment-map.md` | Dev/staging/production differences |

## System Map Template

| Module | Owner | Users / roles | Upstream dependencies | Downstream dependencies | Criticality | Notes |
|---|---|---|---|---|---|---|

## Data Flow Template

| Flow ID | Trigger | Source | Processing step | Destination | Evidence point | Risk |
|---|---|---|---|---|---|---|

## Usage

- Risk Map uses architecture to estimate blast radius.
- API/UI/data verification uses architecture to pick evidence layers.
- Go/No-Go uses architecture to identify critical paths and rollback risk.
