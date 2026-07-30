# Top 10 GitHub kits để benchmark cho Conative QA Codex

> Xếp theo độ phù hợp với mục tiêu deck, không phải bảng xếp hạng tuyệt đối.

| # | Repository | Dùng để học | Capability phù hợp | Quyết định |
|---|---|---|---|---|
| 1 | openai/skills | Chuẩn folder Agent Skills, SKILL.md, script/reference/template | Toàn bộ | Base architecture |
| 2 | petrkindlmann/qa-skills | Pack QA/test automation đa kỹ năng, tương thích Codex | Taxonomy QE tham khảo | Fork ý tưởng taxonomy |
| 3 | fugazi/test-automation-skills-agents | Workflow requirement → ISTQB cases → Playwright plan/generation | Risk, Test Design, Automation | Benchmark goal orchestration |
| 4 | LambdaTest/agent-skills | Skill production-grade cho nhiều framework/ngôn ngữ | Automation, CI | Chọn skill theo stack |
| 5 | jaktestowac/awesome-copilot-for-testers | Prompt, instruction, chat mode cho tester/QE | Test Design, Evidence | Benchmark instruction library |
| 6 | lackeyjb/playwright-skill | Browser testing, screenshot, console output | Automation, Evidence | Demo web UI nhanh |
| 7 | testdino-hq/playwright-skill | Hướng dẫn Playwright cho coding agents | Automation | So sánh pattern Playwright |
| 8 | tayyabakmal1/qa-prompt-library | Prompt manual QA, bug report, test planning | Risk, Test Design, Evidence | Nguồn tham khảo template |
| 9 | PramodDutta/qaskills | Directory skill chuyên QA | Skill discovery | Backlog skill dài hạn |
| 10 | VoltAgent/awesome-agent-skills | Catalog lớn, tương thích nhiều agent gồm Codex | Discovery/governance | Radar tìm skill mới |

## Không nên làm
- Clone cả 10 repo vào production library.
- Trộn prompt không version, không owner, không review.
- Dùng Playwright skill như đại diện cho toàn bộ QA.
- Đo thành công bằng số testcase AI sinh ra.

## Nên làm
- Chọn 3 nguồn để pilot: `openai/skills`, `petrkindlmann/qa-skills`, `fugazi/test-automation-skills-agents`.
- Chọn 1 execution skill: Playwright.
- Chuyển hóa về chuẩn Conative và thêm validator/evaluation.
