---
name: workspace-ui-func
description: Write, read, and execute Conative Workspace UI or functional test cases, compare displayed UI data with matching Langfuse query_data Input/Output logs, record authorized results in the live test workbook, and prepare requested Workspace bugs in DevTak.
---

# Workspace UI & Func

Đầu vào: TC ID, org và phạm vi người dùng yêu cầu. Nguồn chính là **Scenario_UI** và **ReportConative** trong [workbook live](references/sources.md). Đọc lại TC mỗi lần chạy; không lấy prompt hoặc kết quả cũ làm mặc định.

## Chọn skill

Khi soạn hoặc rà case, dùng nguồn và mẫu người dùng chỉ định; skill viết case không tự chạy test hoặc ghi kết quả thực thi.

| Yêu cầu | Skill |
|---|---|
| Soạn, rà hoặc bổ sung test case/scenario | [write-qa-testcases](skill/write-qa-testcases/SKILL.md) |
| Chạy TC từ đầu đến cuối | [execute-workspace-ui-func](skill/execute-workspace-ui-func/SKILL.md) |
| Đọc lại TC, xác định prompt và scope | [read-workspace-testcase](skill/read-workspace-testcase/SKILL.md) |
| Thực thi các bước trên Workspace | [run-workspace-ui-testcase](skill/run-workspace-ui-testcase/SKILL.md) |
| So sánh dữ liệu UI với Input/Output log response | [compare-workspace-report-log](skill/compare-workspace-report-log/SKILL.md) |
| Soạn hoặc tạo Bug Workspace theo yêu cầu | [create-workspace-bug](skill/create-workspace-bug/SKILL.md) |
| Ghi status hoặc sửa Note | [record-workspace-test-result](skill/record-workspace-test-result/SKILL.md) |

Xem [flow toàn bộ](references/execution-flow.md), [bản đồ capability](references/capability-map.md) và [mẫu kết quả](assets/test-result-template.md). Chỉ đọc reference của bước đang thực hiện.

Nguồn đối chiếu dữ liệu là Langfuse: Sessions → conversationId → đúng lượt response → Open observation → Tree → `tool.execution:query_data` → Preview → Raw. Xem [runtime](references/langfuse-log-runtime.md). Không dùng QE API Postman; không hardcode session/trace/observation của ví dụ hoặc sửa prompt để lấy log.

Đọc các quy định repo được liên kết trong flow trước khi xử lý dữ liệu hoặc chạy live. Việc ghi Google Sheets, tạo bug hay lưu evidence phải nằm trong phạm vi đã được người dùng cho phép.

Gói này là draft chờ các review gate của repo; chưa được cài đặt hay công nhận approved.
