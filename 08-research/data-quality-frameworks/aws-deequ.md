# AWS Deequ Benchmark

- Primary source: https://github.com/awslabs/deequ
- Reviewed: 2026-07-30

## Concepts Worth Adopting

- Turn implicit data assumptions into explicit constraints.
- Compute reusable metrics through analyzers, then evaluate constraints against
  those metrics.
- Group constraints in verification suites and preserve per-constraint results.
- Support metrics history and anomaly detection for large or changing datasets.
- Quarantine or block bad data before downstream use when the operating model
  supports it.

## Conative Mapping

Conative separates observed metric from pass/fail threshold and preserves
per-check evidence. Spark, Scala, Deequ classes, and quarantine implementation
remain replaceable execution details.
