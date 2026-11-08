---
name: run-workspace-ui-testcase
description: Execute a grounded Conative Workspace test case through the UI and capture its completed report.
---

# Chạy UI Workspace

Đầu vào là snapshot từ [read-workspace-testcase](../read-workspace-testcase/SKILL.md). Trước bước live, áp dụng các quy định trong [flow](../../references/execution-flow.md); phân biệt trả lời/report trong chat với tạo saved app/view/report hoặc business record.

1. Dùng browser control đang có. Kiểm tra đăng nhập và org hiển thị; chỉ chọn org người dùng yêu cầu. Nếu thiếu phiên đăng nhập, để người dùng đăng nhập qua UI; không yêu cầu gửi password trong chat.
2. Chọn agent/model theo TC hoặc yêu cầu còn hiệu lực, ghi model thực tế. Không suy ra model từ tên cột kết quả.
3. Thực hiện Steps theo đúng thứ tự. Khi TC yêu cầu New chat, mở composer trống; không tiếp tục chat cũ. Chỉ đính kèm ảnh khi TC yêu cầu, kiểm tra trạng thái Ready trước Send.
4. Gửi prompt nguyên văn một lần. Không sửa thêm yêu cầu về cột, scope hoặc ID. Chờ phản hồi hoàn tất; trạng thái “Thinking”, tool finished riêng lẻ hoặc có text đang stream chưa phải hoàn tất.
5. Mở artifact/report nếu được tạo và TC yêu cầu. Kiểm tra bảng/biểu đồ thực tế, pagination, cột, đơn vị và thông báo lỗi. Lời Connie nói “đã tạo report” không thay cho việc quan sát report mở được.
6. Thu giá trị hiển thị theo từng Product ID/Variant ID, thứ tự và tổng được nêu. Ghi nguồn, kỳ, timezone, filters và forecast window mà UI công bố; thiếu thông tin thì đánh dấu thiếu, không suy đoán.
7. Lưu link chat và `conversationId` từ UI/URL đã quan sát, prompt/lượt trả lời và thời điểm để chọn log tương ứng. Không suy ra ID từ tên report. Theo [evidence contract](../../evidence/README.md), chỉ giữ dữ liệu phục vụ đối chiếu; không lưu auth state.

Nếu gửi prompt bị timeout nhưng chưa rõ đã tạo chat chưa, kiểm tra UI hiện tại trước khi thử lại để tránh chạy trùng. Nếu người dùng thay prompt trong sheet, không tự gửi lại giữa một lần chạy; kết thúc/bỏ ghi kết quả cũ khi không còn đúng snapshot và thông báo thay đổi.

Đầu ra: response hoàn tất, các hàng/cột thực tế, chat URL, conversationId, turn/thời điểm và các bước chưa hoàn thành. Tiếp tục [compare-workspace-report-log](../compare-workspace-report-log/SKILL.md) khi TC kiểm dữ liệu.
