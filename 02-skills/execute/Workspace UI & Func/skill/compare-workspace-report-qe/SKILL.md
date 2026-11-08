---
name: compare-workspace-report-qe
description: Compatibility redirect for older Workspace QE comparison references; route to compare-workspace-report-log using Langfuse instead of Postman.
---

# Tham chiếu cũ đã chuyển sang Langfuse

Từ yêu cầu ngày 05/11/2026, dùng [compare-workspace-report-log](../compare-workspace-report-log/SKILL.md). Path này chỉ giữ tương thích liên kết cũ; không thực hiện signIn/chooseOrg hoặc data request Postman. So Input/Output của `tool.execution:query_data` với UI đúng conversation và lượt trả lời. Evidence QE lịch sử không trở thành evidence log của lần chạy mới.
