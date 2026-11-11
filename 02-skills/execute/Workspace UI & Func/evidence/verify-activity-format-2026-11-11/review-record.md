# Activity format and In testing update — 2026-11-11

Source: latest explicit user instructions in this chat: Activity note must contain PASS/FAIL, test time, conversion link, image for both outcomes, and simple Sheet-like Reason only for FAIL; set the ticket status to In testing. Registered as the same-day amendment to SRC-WORKSPACE-VERIFY-BUG-20261111 in the local source index.

Author: Codex. Classification: high-risk (future ticket comments, attachments and workflow status writes). Decision: draft / needs-review; no install, publish, approval promotion or live operation in this session. This instruction supersedes the earlier “do not change ticket status” behavior for this verification workflow only. Earlier evidence remains historical.

Changed the verify skill and Activity template, and synchronized flow, capability map and source index. Ticket outcome remains separate from overall TC status: a new unrelated Sheet failure does not become a ticket FAIL or Reason. In testing is the workflow status for either PASS or FAIL, with live transition/readback checks. An incomplete verification with no proven failure is not forced into PASS/FAIL.

Baseline is in baseline.txt; final size/link/credential checks are in validators.txt. OpenAI quick_validate.py was attempted; the host Python still lacks PyYAML. Simple frontmatter/name/description/scaffold checks were performed locally without claiming the unavailable validator passed.

Author forward walkthroughs: pass-activity-draft.md verifies PASS with no Reason despite an unrelated TC failure; fail-activity-draft.md shows simple ticket-only Actual/Difference/Expected for a UI error with no unnecessary log line. missing-evidence-walkthrough.md covers missing input, unavailable transition, upload failure, timeout and no-associated-case behavior. All fixtures and attachment references are synthetic; nothing was posted or uploaded.

These are author evaluations, not an independent qualified review or live-tool integration test. Qualified capability and accountable domain/security-owner review remain pending before promotion.
