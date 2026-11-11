# Verify Workspace Bug skill — 2026-11-11

Source: explicit user request in this chat, 11/11/2026: read a supplied bug, find associated Scenario_UI testcases, run each with existing project skills, update status/Note in the established format, then comment only ticket-scoped findings in Activity.
Source ID: SRC-WORKSPACE-VERIFY-BUG-20261111, registered in the package source index. Source authority: provided; review pending.

Author: Codex. Classification: high-risk under repository governance because the authored workflow includes future live runs, external Sheet writes and ticket comments. This authoring session performs local edits and offline evaluation only. Decision: draft / needs-review, not installed or published.

## Need and boundary

New skill: skill/verify-workspace-bug/SKILL.md. Existing execute skill starts from known TC IDs; it does not discover cases from a bug, distinguish ticket-specific outcomes from complete TC outcomes, or post a scoped Activity retest comment. This skill composes intake, UI, log comparison and result recording rather than replacing them.

Added an Activity template and routing in the package entrypoint, flow, capability map and local source index. No testcase, business formula, test workbook or DevTak ticket is changed during authoring.

## Validation and evaluation

Baseline and initial new-skill size results are retained alongside this record; final results are in validators.txt. Changed skills remain below warning limits. Link/path checks and a credential-pattern scan are recorded there. OpenAI quick_validate.py was attempted; the host Python lacks PyYAML. Its name/frontmatter/description/scaffold checks were checked locally without claiming that the unavailable validator ran successfully.

Offline author forward walkthroughs use evaluation-input.json, a synthetic fixture. normal-sheet-draft.json and normal-activity-draft.md are the promised draft artifacts: select only matching linked rows, exclude a near-match ticket ID and unrelated FAILED row, keep full-TC FAILED for a different value error, and omit that error from the ticket comment. TC-003 retains the ticket sort error. missing-input-draft.md demonstrates insufficient fixture and no-associated-case branches without invented pass/writeback.

Additional author walkthrough: if linked rows all show correct sort with full evidence, the ticket conclusion is “Không tái hiện lỗi ticket trong phạm vi đã kiểm”; a different assertion may still keep the TC FAILED. If a row changes before writeback, reject the stale write; if Submit times out, read Activity before retry. Missing model Version is handled by the existing column contract, without borrowing another model column.

These are synthetic author evaluations, not independent qualified review, browser execution or proof of live tool integration. Required qualified capability and accountable domain/security-owner reviews remain pending before approval or team promotion. No approval record has been fabricated.
