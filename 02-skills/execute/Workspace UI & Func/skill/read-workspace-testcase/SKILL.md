---
name: read-workspace-testcase
description: Read the current live Conative Workspace test case and resolve its exact scope and expected behavior.
---

# Đọc TC Workspace

1. Đọc [sources](../../references/sources.md) và [column contract](../../references/sheet-column-contract.md). Dùng Google Drive/Sheets connector: metadata trước, xác định tab `Scenario_UI` mặc định, sau đó đọc phạm vi nhỏ theo headers thực tế; chỉ dùng tab khác khi người dùng chỉ định.
2. Tìm TC ID chính xác, đọc toàn bộ Precondition, Description, Prompt, URL, Steps và Expected Result. Đừng giả định dòng 2 hoặc cùng ID luôn có cùng nội dung. Nếu ID trùng, xác định từng biến thể bằng title/prompt/row; không tự chọn một biến thể hay mở rộng sang ID khác.
3. Ghi snapshot và ngôn ngữ sẽ chạy. Bỏ tiền tố đánh số prompt; giữ nguyên phần còn lại. Chỉ thay placeholder bằng fixture đã xác minh. `Prompt` là nguồn bổ trợ, không thay prompt trực tiếp trong dòng TC.
4. Xác định org từ yêu cầu hiện tại hoặc context còn hiệu lực. Đọc nguồn/channel, ngày, grain, filter và ranking mà prompt yêu cầu. Ghi rõ tiêu chí TC còn mơ hồ; không tự bổ sung nghiệp vụ. Nếu TC còn ghi QE/Postman, giữ snapshot nguyên văn và ghi override nguồn đối chiếu sang Langfuse Input/Output theo yêu cầu 05/11/2026; không tự sửa nội dung Sheet.
5. Đọc ReportConative cho các field cần đối chiếu Title/Unit/Format. Nếu TC chỉ kiểm giá trị, tách phát hiện format khỏi phép so sánh số; không tự tạo điều kiện fail ngoài Expected.
6. Xác minh fixture/ảnh nếu được yêu cầu. Nếu người dùng yêu cầu lưu workbook, dùng export của Google Drive sau metadata, lưu định dạng phù hợp và kiểm tra tab cần thiết; bản local chỉ là cache, không thay nguồn live.

Đầu ra: TC snapshot, org, prompt chính xác, Steps, Expected, fixture và danh sách assertion. Bước tiếp theo: [run-workspace-ui-testcase](../run-workspace-ui-testcase/SKILL.md).
