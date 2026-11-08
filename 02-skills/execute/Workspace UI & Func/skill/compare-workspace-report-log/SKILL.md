---
name: compare-workspace-report-log
description: Compare Conative Workspace displayed data with the matching Langfuse query_data Input and Output for the same conversation and response turn.
---

# So sánh UI với log response

Đọc [Langfuse runtime](../../references/langfuse-log-runtime.md) và [comparison contract](../../references/comparison-contract.md). Nguồn đối chiếu là log `tool.execution:query_data` của đúng lần trả lời; không chạy hoặc dùng QE API Postman thay thế.

1. Nhận snapshot UI, org, prompt, chat URL, `conversationId` và lượt trả lời/thời điểm từ [run UI](../run-workspace-ui-testcase/SKILL.md). Nếu thiếu, tìm trong UI/context đã có; không tự dựng ID hoặc rerun prompt để lấy log.
2. Mở Sessions tại project trong [sources](../../references/sources.md). Nếu cần đăng nhập, chờ người dùng đăng nhập trực tiếp. Lọc `Session ID` bằng conversationId, mở kết quả và xác minh tenant/org. Session có thể là `[tenantId,conversationId]`; không coi chuỗi chứa ID là đủ chứng minh đúng run.
3. Tìm prompt và response tương ứng UI trong conversation; dùng thời điểm, trace và lượt trả lời để phân biệt follow-up/retry. Mở `Open observation`; nếu panel chưa có Tree, dùng `Open in new tab`. Chọn `Tree` → `tool.execution:query_data` → `Preview` → `Raw`.
4. Thu đầy đủ Input và Output của các query thực sự tạo dữ liệu UI đang kiểm. Ghi session/trace/observation ID và URL; nối mỗi field/dataset với đúng query. So dữ liệu/phạm vi mà UI thực tế công bố với Input/Output: source, kỳ, grain, filter, sort và mọi giá trị text/KPI/bảng/biểu đồ/tổng/ranking trên các trang liên quan. Không kiểm Input có giống prompt/Expected của TC hay không; prompt chỉ giúp nhận diện đúng lượt response. Input khác prompt không tự tạo FAILED hoặc BLOCK.
5. Nối theo stable ID đúng grain và mapping path đã xác minh từ log. Kiểm `rows`, `columns`, `totals`, `pagination`, `meta`, warnings/errors và tính đầy đủ nếu có. Không coi 100 rows là toàn dataset hoặc lấy response assistant trong Langfuse làm Output nguồn.
6. Có thể dùng [helper offline](../../scripts/compare_snapshot.py) cho snapshot UI/log tối thiểu theo [ví dụ](../../assets/comparison-input.example.json). Helper chỉ so field values; phạm vi UI ↔ log, coverage, tổng, ranking và chart vẫn kiểm riêng. Metric trực tiếp khớp Output không cần tính lại công thức backend; số UI tự tính phải truy được về Input/Output và phép tính có căn cứ.

Thiếu log, sai lượt, Input/Output bị cắt hoặc thiếu mapping: ghi BLOCK cho assertion chưa xác minh; giữ failure độc lập đã chứng minh. Không gọi lại API, sửa query hoặc chạy Postman để lấp phần thiếu. Đầu ra: provenance, bảng Input và bảng ID/field/UI/Log response/Difference, coverage và kết luận có giới hạn. Chuyển [record](../record-workspace-test-result/SKILL.md) khi đã có quyền ghi Sheet.
