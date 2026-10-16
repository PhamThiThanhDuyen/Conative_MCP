---
name: access-claude-connect-org-success
description: Disconnect and reconnect the Claude app's Conative staging MCP connector for a user-selected organization, then run the exact requested testcase prompt in Claude and capture its response for later comparison with QE API. Use only for Claude app connector setup and testcase prompt capture; not for Claude Code or for running QE comparisons.
---

# Access Claude and connect to Conative successfully

Use this skill when the user requests a Conative MCP testcase that requires a fresh Claude connection, or when the current connection may be stale. The target is the Claude app in the in-app browser and the Conative staging MCP connector.

## Required inputs

- The exact organization supplied by the user. Do not choose or infer an organization from prior examples. If the user has not provided one in the current task context, ask for it before connecting.
- The exact testcase ID requested by the user. If absent, ask for it before sending a prompt.
- The testcase prompt, read verbatim from the authorized checklist row. Do not rewrite or summarize it.

## Connection details

Use these values from the Conative QA setup guide:

- Connector name: `conative-claude`
- Staging MCP URL: `https://api.conative.ai/stg-mcp-svc/mcp`
- OAuth client: `Use Claude’s published identity`
- Consent scope expected by the guide: read datasets, fields, and metrics; query analytics data (read-only)

If a maintained setup guide or user-provided environment details specify a different MCP URL, verify the target is the intended staging environment before using it. Do not use production or an unverified endpoint.

## Procedure

1. Open Claude in the in-app browser. If the tab is missing, open `https://claude.ai` visibly. If sign-in is needed, let the user sign in; never enter passwords, one-time codes, or other authentication secrets for the user.
2. Open **Settings → Connectors** and locate `conative-claude`.
3. If `conative-claude` is connected, choose **Disconnect** for that connector only. If Claude asks to confirm disconnection, confirm it. Verify Claude shows the connector as disconnected before continuing. Do not disconnect other connectors.
4. Reconnect the connector:
   - If `conative-claude` is already configured, use its **Connect** action; do not create a duplicate.
   - If it is not configured, choose **Add → Add custom connector**.
   - Enter `conative-claude` and the verified staging MCP URL above.
   - Keep **Sign in now** selected and keep **Use Claude’s published identity** selected.
   - Choose **Add**, then **Connect**.
5. On the Conative sign-in page, let the user complete sign-in if required. Select only the exact organization supplied by the user. If the organization list does not contain that organization, stop and report the blocker.
6. Inspect the live consent screen. It must identify the intended Conative staging connection and the expected read-only analytics scope. Because **Allow access** grants the connector access to organization data, show the live scope and ask the user to confirm it immediately before clicking **Allow access**. Do not proceed if the scope is broader, unclear, or differs from the expected read-only scope.
7. After approval, choose **Return to Claude**. Verify Claude visibly shows `conative-claude` connected to the selected organization. Do not continue to prompt submission unless this state is visible.
8. Open the exact testcase row identified by the user. Confirm its ID appears once and read the Prompt cell verbatim. Submit that prompt once in Claude. Do not add follow-up or exploratory prompts.
9. Wait for Claude's answer and capture the complete visible response, including returned metric values, labels, date/time range, channel/source, and any relevant tool call/result details. Preserve the response for the next QE API comparison step. Do not claim a comparison result at this stage.
10. Report the testcase ID, selected organization, connection status, exact prompt submitted, and captured response or any blocker. Keep credentials, tokens, cookies, and session data out of notes and evidence.

## Stop conditions

Stop without submitting the testcase prompt if:

- The requested organization or testcase ID is missing or ambiguous.
- The selected organization differs from the user's instruction.
- Claude does not visibly confirm the connector is connected to the selected organization.
- The consent scope is unclear or broader than the expected read-only analytics access, or the user has not confirmed the live scope.
- The exact testcase row or Prompt cell cannot be verified.

If stopped, state the precise missing input or UI condition. Do not invent a connection state, testcase prompt, or Claude response.
