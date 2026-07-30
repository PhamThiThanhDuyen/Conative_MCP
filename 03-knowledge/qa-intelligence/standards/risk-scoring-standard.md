# Conative Risk Scoring Standard

Risk Score = Impact x Likelihood.

## Impact

| Score | Level | Definition |
|---:|---|---|
| 5 | Catastrophic | Revenue loss, data breach, legal/compliance issue, core system unavailable |
| 4 | Major | Significant user impact, SLA breach, critical workflow blocked |
| 3 | Moderate | Workflow disrupted but workaround exists |
| 2 | Minor | Limited user impact, non-critical defect |
| 1 | Negligible | Internal-only or cosmetic issue |

## Likelihood

| Score | Level | Indicators |
|---:|---|---|
| 5 | Frequent | High churn, recent failures, weak/no tests, complex branching |
| 4 | Likely | Recent changes, partial coverage, known tech debt |
| 3 | Possible | Moderate complexity, has happened before |
| 2 | Unlikely | Stable area, good coverage |
| 1 | Rare | Simple, well-tested, rarely changed |

## Zones

| Score | Zone | Testing action |
|---:|---|---|
| 15-25 | Critical | Full verification, automation where stable, evidence required, release owner review |
| 10-14 | High | Strong coverage, owner review, residual risk explicit |
| 5-9 | Medium | Core positive/negative coverage, monitor gaps |
| 1-4 | Low | Smoke/manual coverage or defer if out of scope |

## Failure Mode Analysis

For Critical/High items, record:

- Failure mode
- Trigger
- Blast radius
- Detection method
- Current mitigation
- Gap
- Owner/action
