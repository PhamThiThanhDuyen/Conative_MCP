# Soda Core Benchmark

- Primary sources:
  - https://docs.soda.io/soda-cl-overview
  - https://docs.soda.io/sodacl-reference/metrics-and-checks
  - https://docs.soda.io/sodacl-reference/recon
- Reviewed: 2026-07-30

## Concepts Worth Adopting

- Checks combine a metric, comparison, and threshold in a readable contract.
- Standard checks cover numeric, missing, and validity metrics.
- Specialized checks cover freshness, reference integrity, reconciliation,
  distribution, cross-schema behavior, and anomaly detection.
- User-defined queries remain necessary for business-specific rules.
- A scan runs checks and returns results suitable for investigation.

## Conative Mapping

Conative adopts readable check definitions, explicit thresholds, reconciliation,
freshness, and extensibility for business queries. SodaCL syntax and Soda Cloud
are implementation choices, not repository architecture requirements.
