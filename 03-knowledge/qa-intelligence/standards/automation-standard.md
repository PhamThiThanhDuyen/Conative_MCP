# Conative Automation Standard

## Scope

Automation should prove high-value, stable behavior. Do not automate blocked
requirements or unclear expected results.

Read `../../governance/information-security-policy.md` before handling auth state,
credentials, customer data, generated artifacts, or external transmission.

## Locator Rules

- Prefer user-facing locators: role, label, placeholder, text with stable name.
- Use stable test IDs when user-facing locators are ambiguous or copy changes often.
- Avoid brittle CSS, generated class names, position selectors, and XPath unless already unavoidable.
- Verify locators against the real DOM before shipping automation.

## Test Rules

- Tests must be independent unless explicitly marked serial for lifecycle flow.
- Use deterministic data and cleanup.
- Load credentials only from approved secret stores, protected and masked CI/CD
  variables, or ignored local environment files. Never persist plaintext auth data.
- Avoid fixed sleeps. Wait for observable states.
- Assertions must explain expected behavior.
- Capture failure artifacts: screenshot/video/trace/console/network where supported.

## API Automation

- Use fixtures for auth; do not hardcode tokens.
- Do not commit browser storage state, cookies, passwords, tokens, or session files.
- Validate schema/status/body/header.
- Cleanup created data.
- Keep API client/helper logic separate from assertions.

## Done When

- Narrow relevant command passes.
- Evidence path is recorded.
- Case IDs and risk IDs are traceable.
- Remaining product failures are reported as findings, not hidden by changing tests.
- Reports and artifacts remain local or in the approved private Conative GitLab;
  no project information is uploaded elsewhere without explicit authorization.
