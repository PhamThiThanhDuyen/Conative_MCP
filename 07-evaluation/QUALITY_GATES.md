# Agent output quality gates

1. Traceability: requirement → risk → testcase → evidence → decision.
2. No invented domain rule.
3. Negative/edge coverage present.
4. Evidence is reproducible and tied to build/environment.
5. Residual risks are explicit.
6. Final decision has owner and next action.
7. Human review recorded.

## Skill Context Budget

- Run `python 05-scripts/validate_skill_size.py <skill-directory>` before and
  after changing an existing skill.
- Use the pre-update result as the baseline. Do not introduce a warning or make
  an existing warning larger.
- For a new skill, validate after the initial `SKILL.md` is created and after the
  implementation is complete.
- Warn when a `SKILL.md` body exceeds 800 words or 150 lines.
- Fail when it exceeds 5,000 words or 500 lines.
- A warning requires a progressive-disclosure review but does not block local work.
- CI may use `--fail-on-warning` when the team wants warnings to block merging.
