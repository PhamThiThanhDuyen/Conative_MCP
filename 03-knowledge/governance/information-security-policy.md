---
knowledge_id: GOV-SEC-001
knowledge_type: governance-policy
source: User-provided Conative team operating rules, 2026-07-30
owner: Conative team owner
authority: provided
scope: all Conative QA kit users, agents, project data, and repositories
target_release: not-applicable
status: active
last_verified: 2026-07-30
supersedes: []
---

# Conative Information Security Policy

Apply this policy to all team members, agents, automation, scripts, generated
artifacts, and future GitLab workflows.

## Project Information Boundary

Project information includes source code, requirements, product and client
knowledge, architecture, API specifications, schemas, tickets, test cases,
screenshots, recordings, logs, traces, payloads, reports, data extracts,
credentials, and environment details.

Approved storage destinations:

1. The authorized local machine or workspace.
2. The approved private Conative GitLab repository after it is configured.

Until the GitLab destination is approved and configured, keep project information
local only.

Do not independently upload, publish, paste, email, share, or transmit project
information to public GitHub repositories, paste sites, personal storage, public
issue trackers, unapproved AI/SaaS tools, or any other external destination.
External disclosure requires explicit authorization from the responsible
Conative owner and must contain only the minimum approved information.

Retrieving public documentation or dependencies is allowed when it does not send
proprietary content, customer data, credentials, or secrets in the request.

## Authentication And Secret Storage

Never store authentication material as plaintext in code, configuration,
documentation, test fixtures, spreadsheets, logs, screenshots, videos, evidence,
chat prompts, generated reports, or version control.

Use these controls:

| Material | Required handling |
|---|---|
| Application user password | Store only a salted one-way password hash using an approved password-hashing algorithm such as Argon2id, bcrypt, or scrypt |
| Test account credential | Store in an approved secret manager, protected and masked GitLab CI/CD variable, or local environment file excluded from Git |
| API token, session cookie, OTP, refresh token | Keep ephemeral where possible; store only in an approved secret mechanism and redact from all evidence |
| Reversible secret that must persist | Encrypt at rest with approved key management; keep the key outside the repository and separate from the ciphertext |
| Public test placeholder | Use a clearly fake value or secret reference name, never a working credential |

Password encryption alone is not an acceptable substitute for password hashing.
Do not commit encrypted secrets to Git merely because they are encrypted unless
Conative has approved the encryption and key-management process.

## Local And GitLab Rules

- Keep local secret files excluded through `.gitignore`.
- Before the first GitLab push, verify the destination is the approved private
  Conative namespace and repository.
- Use least-privilege membership, protected branches, protected and masked CI/CD
  variables, and secret scanning when GitLab is configured.
- Never store decryption keys beside encrypted values.
- Review staged changes for credentials, customer data, auth state, logs, and
  sensitive evidence before every push.
- Do not push browser storage state, session state, local `.env` files, private
  keys, certificates, or raw production payloads.

## Evidence And Reporting

- Replace secrets and customer identifiers with masked or synthetic values.
- Store only the minimum evidence required to reproduce the finding.
- Keep sensitive raw evidence local in an access-controlled location.
- Do not attach project evidence to an external ticket, chat, email, or service
  without explicit authorization.

## Incident Handling

If plaintext credentials or project information are exposed outside the approved
boundary:

1. Stop the upload, push, or transmission when possible.
2. Notify the responsible Conative owner immediately.
3. Revoke or rotate affected credentials and sessions.
4. Preserve a minimal incident record without repeating the exposed secret.
5. Remove the material from local history or Git history only through an approved
   remediation process.
6. Verify that copies, logs, artifacts, and CI/CD output no longer expose it.
