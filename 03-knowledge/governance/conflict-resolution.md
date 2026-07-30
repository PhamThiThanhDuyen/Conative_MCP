# Conflict Resolution

When credible sources disagree:

1. State the conflicting claims precisely.
2. Record each source, scope, status, target release, and verification date.
3. Determine whether the difference is current versus target behavior.
4. Apply the authority matrix for the decision being made.
5. Classify the result as `Defect`, `Planned Change`, `Approved Deviation`, `Requirement Gap`, or `Unresolved Conflict`.
6. Escalate to the named owner when authority or scope remains unclear.
7. Do not mark the affected case Ready until the conflict is resolved or explicitly accepted with an owner and expiry.

Examples:

- Approved BA rule differs from current implementation: candidate defect or planned change.
- Industry convention differs from approved BA rule: domain risk; BA rule remains expected behavior.
- Current product docs differ by organization or role: scoped behavior gap requiring verification.
- Two approved business contracts overlap and disagree: unresolved conflict requiring BA/PO decision.
