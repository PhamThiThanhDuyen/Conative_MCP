# Release Defect Patterns

| Pattern | Release signal | Gate impact |
|---|---|---|
| Critical path unverified | Smoke/core flow not run or blocked | No-Go or Conditional Go with owner acceptance |
| Open P0/P1 defect | Active blocker in release scope | No-Go |
| Contract break | Active consumer impacted by API/schema change | No-Go unless versioned/mitigated |
| Missing rollback | Change has high blast radius and no rollback path | Conditional Go or No-Go |
| Irreversible migration risk | Data migration cannot be safely reverted | No-Go until mitigation is approved |
| Monitoring blind spot | New critical feature lacks alert/health signal | Conditional Go |
| Evidence gap | Critical claim lacks reproducible evidence | No-Go for critical path, otherwise residual risk |
| Flaky gate | Release decision depends on unstable test | Re-run/triage; do not count as clean pass |
