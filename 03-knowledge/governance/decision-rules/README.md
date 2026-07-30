# Decision Rules

Store AI reasoning policy for Conative QA artifacts. These rules guide how skills
prioritize, classify, escalate, and recommend release decisions.

## Decision Hierarchy

1. Confirmed requirement/business rule/API contract.
2. Conative QA standards.
3. Observed evidence.
4. Benchmark heuristic.
5. Assumption requiring human approval.

## Escalation Rules

| Situation | Action |
|---|---|
| Business rule missing | Mark `Assumed` or `Open Question`; do not mark Ready |
| Critical path evidence missing | No-Go or Conditional Go with owner acceptance |
| Security/auth/data integrity risk | Escalate to owner; default No-Go until assessed |
| Contract break with active consumer | No-Go unless versioned/mitigated/accepted |
| Conflicting sources | Cite both and request owner decision |

## Prioritization Rules

| Signal | Priority impact |
|---|---|
| High impact x high likelihood | P0/P1 verification |
| Recent incident or near miss | Increase likelihood |
| High code churn + low coverage | Increase likelihood |
| Customer-facing critical flow | Increase impact |
| Blocked assumption on critical path | Release risk |

## Output Rules

- Always separate facts, assumptions, and recommendations.
- Never present suspected root cause as confirmed without code/log evidence.
- Every recommendation needs owner action and recheck condition.
