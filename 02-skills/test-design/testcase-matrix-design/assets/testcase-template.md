# [Product] — [Feature] Test Scenarios

## 1. Scope and evidence

- Requirement sources:
- Environment:
- Confirmed requirements:
- Observed behavior:
- Out of scope:

## 2. Assumption register

| Assumption ID | Decision needed | Safe default recommendation | Status | Affected cases |
|---|---|---|---|---|
| ASM-FEATURE-01 | [Decision] | [Recommendation] | Blocked - Awaiting requirement | FEATURE-AREA-001 |

## 3. UI execution order

| UI Order | Region/control | Top-to-bottom, left-to-right checks | Case IDs |
|---:|---|---|---|

## 4. Equivalence partitions

| Partition ID | Object | Valid partitions | Invalid partitions | Representative data | Case IDs |
|---|---|---|---|---|---|
| EP-FEATURE-01 | [Object] | [Valid classes] | [Invalid classes] | [Data] | FEATURE-AREA-001 |

## 5. Boundary values

| Boundary ID | Object | Required values | Expected at boundary | Data IDs | Case IDs |
|---|---|---|---|---|---|
| BV-FEATURE-01 | [Object] | [min-1, min, min+1] | [Expected] | DATA-FEATURE-01 | FEATURE-AREA-001 |

## 6. Decision tables

### DT-FEATURE-01 - [Decision]

| Rule | Condition 1 | Condition 2 | Condition 3 | Outcome |
|---|---|---|---|---|
| DT-FEATURE-01-R1 | [Value] | [Value] | [Value] | [Expected] |

## 7. Test data and fixtures

| Data ID | Setup/seed | Input/state | Secret reference | Expected | Cleanup |
|---|---|---|---|---|---|

## 8. Test scenarios

| ID | UI Order | Priority | Type | Technique | Partition/Rule | Title | Preconditions | Data ID | Steps | Expected result | Automation | Status |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| FEATURE-AREA-001 | 01 | P0 | Functional | EP/BVA/Decision table | EP-FEATURE-01 / BV-FEATURE-01 / DT-FEATURE-01-R1 | [Observable behavior] | [Deterministic setup] | DATA-FEATURE-01 | 1. ...<br>2. ... | [Exact result] | Candidate/Manual | Blocked - Awaiting requirement |

## 9. Traceability

| Case/range | UI Order | Requirement/Assumption | Technique | Partition/Boundary/Rule | Data ID | Status |
|---|---:|---|---|---|---|---|

## 10. Smoke scope

- Include only Ready P0 cases.

## 11. Findings and coverage gaps

- Separate confirmed defects, defect candidates, assumptions, blocked cases, and out-of-scope gaps.
