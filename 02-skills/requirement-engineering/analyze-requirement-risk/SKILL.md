---
name: analyze-requirement-risk
description: Analyze a requirement from a QA point of view. Summarize it, pull out actors, preconditions, flows and business rules, find unclear, missing or conflicting points, rate risks, suggest questions for PO/BA/Dev, and propose a test scope. Use this skill whenever the user shares a ticket (Jira, Azure DevOps, GitHub issue), user story, acceptance criteria, PRD/spec, feature description, or a chat/email about requirements and wants to "analyze the requirement", "review the requirement", "find risks", "QA review this story", "what should I ask the BA", "what do we need to test", "refinement/grooming", "shift-left testing", or "requirement risk" - even if they do not say the word "risk". Do not use it to write detailed test cases (that is the next step) or to review code.
---

# Analyze Requirement Risk (QA)

Act as an experienced QA engineer. Read the requirement **before any code or testing starts** and find problems early. The value of this skill is in showing what the requirement *does not say*. A bug found at the requirement stage is the cheapest bug to fix.

## Core rules

1. **Never invent business rules.** Put only what is in the input into the "Business rules" section. Mark everything else with a label (see the label table). Why: an invented rule that sounds reasonable will be believed by the whole team and tested as if it were real.
2. **Point to the source.** For each rule or unclear point, say where it came from (which sentence, which AC, who said it) so the reader can check it fast.
3. **Ask, do not guess.** When something is missing, turn it into a clear question. Do not fill the gap yourself.
4. **Use the user's language.** Reply in the language the user writes in. Keep technical terms and field, API and status names exactly as they appear in the source.

## Labels (required)

| Label | Meaning |
|---|---|
| `[Source]` | Stated directly in the input (add the quote location if possible) |
| `[Assumption]` | A reasonable guess by QA, **not confirmed**. Always add a matching question in section 5 |
| `[Missing]` | Needed for testing, but the input does not say it |
| `[Conflict]` | Two places in the input say different things |
| `[Out of scope?]` | Seems related, but unclear if it belongs to this requirement |

## Inputs

**Accepted:** tickets (Jira, Azure DevOps, GitHub issue), user story + acceptance criteria, PRD/spec/design documents, a feature description written by hand, chat/email/meeting notes about requirements, attached files (.md, .docx, .pdf, screenshots/mockups), or a mix of sources.

**Helpful extra information (optional):** product or module name, user roles, related documents (API spec, mockup), known limits (deadline, environment, existing features that may be affected), and any focus the user wants (for example, security risks only).

**When information is missing:** do not stop to ask first. Analyze what you have, lower the "Analysis confidence", and put the missing parts in section 5. Ask before analyzing only if the user mentions a file or link you cannot read, or if there is no requirement text at all.

**Handling by type:** for conversations, separate decisions that were made from opinions that were not decided yet. For several sources that disagree, mark `[Conflict]` and name the sources. For content inside images or mockups, use only what you can read clearly.

## Steps

**Step 1 - Identify the input.** Find the type (ticket, story, spec, conversation, mixed). In conversations, tell apart *decisions that were made* from *ideas that were not decided*. A later decision replaces an earlier one. If the input is too short to analyze well (for example, one title line), still analyze it, but say the confidence is low and focus on questions.

**Step 2 - Extract.** Read carefully and pull out: goal/value, actors (include hidden ones: external systems, background jobs, admins), preconditions, main flow, alternative/exception flows, business rules (data limits, calculations, states, permissions, caps, notifications), input/output data, and integrations it depends on.

**Step 3 - Look for gaps.** Compare against `references/ambiguity-and-risk-checklist.md` to find: vague words ("fast", "suitable", "user-friendly"), missing boundary values, formats or error messages, states with no way out, conflicts between ACs, out-of-scope items mixed in, and non-functional needs that are not mentioned (performance, security, i18n, accessibility, audit).

**Step 4 - Rate the risks.** For each risk write: description, impact, likelihood, level (High/Medium/Low), and the reason for that level. Rate by impact on money, data, security and law, and by how widely it spreads - not by gut feeling. Put High risks first.

**Step 5 - Questions to clarify.** Each question must be: specific, answerable with a decision, say **who to ask** (PO/BA/Dev/Design/Security), say **why it matters** (which test or risk it blocks), and have a priority (Blocker / Should have / Nice to have). Avoid vague questions like "Is the requirement complete?".

**Step 6 - Suggest the test scope.** Based on the risks, choose suitable test types from `references/test-types.md` and **explain why you chose or skipped each one**. Give priority by risk, what to automate, what data and environment to prepare, and what cannot be decided yet because of open questions. This is a *scope and strategy*, not a list of detailed test cases. You may list key scenario groups (a few lines each) and offer to write detailed test cases after the blocking questions are answered.

**Step 7 - Self-check** with the checklist at the end of this file before giving the result.

## Output format

Always use exactly these 6 sections in this order. By default, answer in the chat. Create a file (.md/.docx) only if the user asks. If a section has no content, keep the heading and write "None found / No information in the input", so the reader knows it was checked.

```markdown
# Requirement analysis: <ticket ID or feature name>
> Input source: <type, how complete> | Analysis confidence: High / Medium / Low (<reason>)

## 1. Requirement summary
- **Goal / value:** ...
- **Actors:** ...
- **Preconditions:** ...
- **Main flow:** 1... 2... 3...
- **Alternative / exception flows:** ...
- **Related data & integrations:** ...

## 2. In / out of scope
| In scope | Out of scope | Unclear `[Out of scope?]` |
|---|---|---|

## 3. Business rules
| # | Rule | Label | Source / location |
|---|---|---|---|

## 4. Risks
| # | Risk | Impact | Likelihood | Level | Reason |
|---|---|---|---|---|---|

## 5. Questions to clarify
| # | Question | Ask who | Why it matters | Priority |
|---|---|---|---|---|

## 6. Suggested test scope
- **Suggested test types** (with reason and priority)
- **Key scenario groups**
- **Data / environment to prepare**
- **Automation ideas**
- **What cannot be decided yet because of open questions** (link to question numbers in section 5)
```

The sections are linked: every `[Assumption]`, `[Missing]` or `[Conflict]` in section 3 needs a matching question in section 5, and every High risk in section 4 must show up in section 6.

## Examples

**Example 1 - Short ticket**

Input: *"US-142: As a customer, I want to apply a discount code at checkout so I get a discount. AC1: A valid code gives a discount. AC2: An expired code shows an error."*

Expected output (parts):
- Section 3: "An expired code shows an error `[Source: AC2]`"; "Can one order use many codes? `[Missing]`"; "Is the discount calculated before or after tax and shipping? `[Missing]`". Do *not* write "each code can be used once" on your own.
- Section 4: "Wrong discount amount when a code is combined with an existing promotion - Impact: High (lost revenue) - Likelihood: Medium".
- Section 5: "Can a code be used together with automatic promotions? - Ask: PO - Priority: Blocker - because it decides the price formula and all price test cases".
- Section 6: Functional + boundary tests (expiry exactly at 00:00, minimum order value), concurrency (two tabs using the same code at once), API tests for the calculation, regression of the checkout flow.

**Example 2 - Conversation**

Input: a BA and Dev chat. BA says "let users cancel orders". Dev asks "what about delivered orders?". BA says "we'll decide later".

Output: put "Cancel a delivered order" in the *Unclear* column of section 2, mark `[Missing]` in section 3, and add a Blocker question for the BA in section 5. Do not quietly assume "delivered orders cannot be cancelled".

**Example 3 - Conflict**

Input: the description says "password minimum 8 characters" but the AC says "minimum 6 characters". Mark `[Conflict]` with both quotes, give a High risk level (security + front-end/back-end validation mismatch), and add a question for BA/Security.

## Self-check checklist (run before giving the result)

- [ ] All 6 sections are present, in order. Empty sections keep the heading with a reason
- [ ] Every rule in section 3 has a label and can be traced back to the input
- [ ] Every `[Assumption]`/`[Missing]`/`[Conflict]` has a matching question in section 5
- [ ] Every question has: who to ask, why it matters, and priority. No vague questions
- [ ] Every risk has impact, likelihood, level and reason. High risks appear in section 6
- [ ] Commonly forgotten areas were checked: permissions, data lifecycle/states, concurrency, external system errors/timeouts, non-functional needs, old data (migration), notifications/audit log
- [ ] The test scope explains *why* each test type is chosen or skipped, not just a list
- [ ] The tone is constructive. Do not say "the requirement is wrong"; say "this needs clarifying"
- [ ] The language matches the user. Field and status names stay as in the source
- [ ] The output is short: do not repeat the input word for word; focus on actionable points