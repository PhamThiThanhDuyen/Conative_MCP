# Conative Release Decision Standard

## Recommendation Types

| Recommendation | Meaning |
|---|---|
| Go | Release can proceed with evidence-backed confidence |
| Conditional Go | Release can proceed only with named mitigation/monitoring/owner acceptance |
| No-Go | Release should not proceed until blocking risks are resolved |

## No-Go Triggers

- Critical path not verified or evidence missing.
- Open P0/P1 defect in release scope.
- Auth bypass, IDOR/BOLA, sensitive data exposure, or critical security risk.
- Data integrity issue, irreversible migration risk, or reporting metric corruption.
- Public API breaking change affecting active consumer without mitigation.
- High residual risk without owner acceptance.

## Conditional Go Requirements

- Risk and blast radius documented.
- Owner accepts the risk.
- Mitigation or rollback exists.
- Monitoring/recheck condition is concrete.
- Support/release stakeholders know the limitation.

## Evidence Completeness

| Level | Meaning |
|---|---|
| High | Critical paths verified across needed layers, artifacts complete |
| Medium | Core paths verified, some non-critical evidence gaps accepted |
| Low | Missing critical evidence or too many blocked assumptions |

## Residual Risk Score

Score = Impact x Likelihood.

| Score | Zone | Action |
|---:|---|---|
| 15-25 | Critical | No-Go unless explicitly accepted by release owner with mitigation |
| 10-14 | High | Conditional Go or No-Go |
| 5-9 | Medium | Track mitigation, usually not blocking |
| 1-4 | Low | Record and monitor |
