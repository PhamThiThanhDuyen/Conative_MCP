# Repository Instructions

## Information Security

- Read `03-knowledge/governance/information-security-policy.md` before handling
  authentication data, credentials, customer data, project artifacts, or any
  operation that could transmit project information outside the workspace.
- Never store passwords, credentials, tokens, cookies, OTPs, private keys, or
  session state as plaintext in code, documentation, test data, logs, evidence,
  prompts, or version control.
- Store test credentials only through approved secret stores, protected and
  masked CI/CD variables, or local environment files excluded from version control.
- Store project information locally. When the Conative GitLab destination is
  approved and configured, project information may also be stored in its approved
  private repository.
- Do not upload, paste, publish, email, or otherwise transmit project information
  to public repositories or external services without explicit authorization from
  the responsible Conative owner.
- Public documentation and dependencies may be retrieved when needed, but do not
  include proprietary project content, customer data, or secrets in external
  queries, requests, issue reports, or prompts.

## Live Data Testing

- Read `03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md`
  before testing against a live or customer-connected environment.
- Never modify customer-owned data. Block live create/update/delete tests until a
  developer confirms a fresh backup and owns the restore.
- Prefix named persistent live test entities with `CBI Test` and keep the run
  blocked until the developer confirms restoration.

## Skill Governance

- Read `03-knowledge/governance/change-approval-policy.md` before creating or
  updating a Skill or Knowledge document.
- Before updating an existing skill, run
  `python 05-scripts/validate_skill_size.py <skill-directory>` and record its
  current result as the baseline.
- Run the same command again after the update. A change must not introduce a new
  warning or increase the word/line count of a skill that was already warning.
- For a new skill, run the validator immediately after creating its initial
  `SKILL.md` and again after the skill is complete.
- Treat `WARN` as a request to move detail into progressive-disclosure resources.
- Do not bypass a `FAIL`; reduce the SKILL.md body below the OpenAI context limit.
- Do not install, publish, or describe a changed Skill as approved until its
  required review gates pass and an approval record exists.

## Knowledge Governance

- Register the source and add required metadata before relying on new Knowledge.
- Never set `authority: approved` without identifiable owner approval evidence.
- Keep new or materially changed Knowledge at `status: needs-review` until the
  accountable content owner reviews scope, meaning, conflicts, and freshness.
- Record approval, rejection, or supersession in
  `03-knowledge/governance/change-approval-register.md`.
