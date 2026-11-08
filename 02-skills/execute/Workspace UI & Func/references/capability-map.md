---
knowledge_id: QA-WORKSPACE-UI-FUNC-CAPABILITIES-001
knowledge_type: qa-intelligence
source: SRC-WORKSPACE-LANGFUSE-FLOW-20261105; SRC-WORKSPACE-LANGFUSE-OBS-20261105
owner: Conative QA owner (review pending)
authority: source-derived
scope: Skill routing for Workspace UI and functional testing
target_release: current
status: needs-review
last_verified: 2026-11-05
supersedes: []
---

# Bản đồ skill/capability

| Giai đoạn | Skill/capability | Phạm vi |
|---|---|---|
| Đọc/lưu Drive | `google-drive:google-drive` | Metadata/export khi được yêu cầu |
| Đọc/ghi TC | `google-drive:google-sheets` | Bounded ranges, validation, updateCells và readback |
| Điều phối | [execute-workspace-ui-func](../skill/execute-workspace-ui-func/SKILL.md) | Run hiện tại từ intake đến kết quả |
| Intake | [read-workspace-testcase](../skill/read-workspace-testcase/SKILL.md) | TC mới nhất, prompt và assertions |
| UI | [run-workspace-ui-testcase](../skill/run-workspace-ui-testcase/SKILL.md) + browser control | Org/model, Steps, report, chat URL, conversationId và lượt response |
| Xem log và đối chiếu | [compare-workspace-report-log](../skill/compare-workspace-report-log/SKILL.md) + [Langfuse runtime](langfuse-log-runtime.md) | Sessions → đúng turn → query_data → Preview/Raw; Input/Output và values UI |
| Tính offline | [compare_snapshot.py](../scripts/compare_snapshot.py) | Decimal, provenance/scope gate, row IDs và field values; không gọi dịch vụ |
| Ghi kết quả | [record-workspace-test-result](../skill/record-workspace-test-result/SKILL.md) | Đúng model, status/Note/Version |
| Bug theo yêu cầu | [create-workspace-bug](../skill/create-workspace-bug/SKILL.md) | Evidence đúng run, mẫu DevTak #90468, readback |
| Viết case | [write-qa-testcases](../skill/write-qa-testcases/SKILL.md) | Soạn/rà case, chưa thực thi |
| Cập nhật bộ skill | `skill-creator` | Authoring/validation, không phải bước chạy TC |

“Chạy WS-… cho org …” đi từ intake → UI → Langfuse log/compare nếu kiểm dữ liệu. “Chỉ rút gọn Note” dùng evidence đã xác minh của đúng run, giữ status/Version.

Path [compare-workspace-report-qe](../skill/compare-workspace-report-qe/SKILL.md) giữ làm redirect cũ. QE Postman, Round 2, Claude.ai và `Field compare` QE không tham gia flow đối chiếu Workspace hiện tại. Không tự tạo bug, gửi tin, publish/cài skill hoặc export workbook vì đã chạy TC.
