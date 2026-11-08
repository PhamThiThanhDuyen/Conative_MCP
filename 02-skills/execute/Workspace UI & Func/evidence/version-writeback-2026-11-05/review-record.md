# Execution Version writeback update - 2026-11-05

Source: explicit user request in the active chat to put execution time in the matching Version cell whenever executing and updating status, then update this project skill.
Classification: behavioral. Author: Codex. Decision: draft / needs-review; no installation, publication or approval promotion.

## Change

- Record workflow now writes status, Note and matching model Version in one value-only batch.
- Version is the run completion timestamp, Vietnam time, dd/MM/yyyy HH:mm:ss (GMT+7), recorded with execution evidence. It is not duration or model version.
- Note-only edits preserve status and Version. Old evidence uses an established execution time; never replace it with the current editing time.
- Resolve live headers. Observed Scenario_UI: Claude status K, Note L, Version M; GPT status N and Note O. GPT Version is not currently observed. Missing matching Version must be reported; never borrow another model's column or silently add a column.
- Updated orchestration, flow, column contract, result template and local source index consistently.

## Validation

- Record SKILL baseline: PASS, 290 words / 13 lines. After: PASS, 357 words / 13 lines.
- Execute SKILL baseline: PASS, 263 words / 13 lines. After: PASS, 278 words / 13 lines. No size warnings or failures.
- OpenAI quick validator unavailable: Python runtime lacks PyYAML. Existing name/frontmatter shape preserved except description wording.
- Normal authorized writeback: TC-001 Version Claude M2 backfilled from the completed execution record timestamp, 05/11/2026 09:45:58 (GMT+7); connector readback matched. Existing status/Note were preserved.
- Missing-column walkthrough: GPT has no observed matching Version header; do not put a GPT timestamp in Claude M.
- Note-only walkthrough: no UI/QE rerun and no Version change. No extra live write was performed to test this branch.
- These are deterministic checks and author walkthroughs, not an independent qualified review or approval.

Qualified capability/content-owner review remains pending before promotion under repository governance.

## Live column movement validation

During the authorized Immediate batch, the sheet owner inserted Prompt (Vietnamese) and QA Review columns. Fresh native CellData showed Claude status L, QA Review M, Note N, Version O; GPT status P and Note Q. The writer resolved headers for every update and preserved QA Review and the other model. The column contract now reflects this later observation; earlier K/L/M evidence above describes the actual positions at the time of that write. The original timestamps survived the column movements. No extra test rows or formatting changes were made.
