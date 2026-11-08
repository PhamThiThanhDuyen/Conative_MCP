---
name: execute-workspace-ui-func
description: Orchestrate a Conative Workspace test run from fresh testcase intake through UI execution, Langfuse query_data Input/Output comparison and authorized result recording.
---

# Thực thi Workspace UI & Func

1. Đọc [flow](../../references/execution-flow.md) và áp dụng quy định repo đúng với hành động dự kiến. Kế thừa org, model và quyền ghi kết quả còn hiệu lực trong chat; không yêu cầu xác nhận lại nếu phạm vi không đổi.
2. Dùng [read-workspace-testcase](../read-workspace-testcase/SKILL.md). Đóng băng snapshot gồm prompt, Steps, Expected, org, fixture và tiêu chí đối chiếu cho lần chạy này.
3. Dùng [run-workspace-ui-testcase](../run-workspace-ui-testcase/SKILL.md). Thực hiện lần lượt các bước và đợi phản hồi hoàn tất. Không sửa prompt để ép có Product ID hoặc ép số liệu khớp.
4. Khi kiểm dữ liệu, dùng [compare-workspace-report-log](../compare-workspace-report-log/SKILL.md): conversationId → đúng session/turn → query_data Preview/Raw. Chỉ so dữ liệu UI trả về với Input/Output đúng run; không chấm Input có đúng prompt/Expected hay không. Sai khác Input ↔ prompt không tạo failure/blocker compare. Không dùng QE API Postman. TC cũ còn nhắc QE thì giữ nguyên snapshot, ghi override nguồn theo yêu cầu hiện tại; không tự sửa Sheet. Nếu một phần bị chặn, hoàn tất phần độc lập và nêu giới hạn.
5. Kết luận theo [comparison contract](../../references/comparison-contract.md). Ghi phạm vi thực sự đã kiểm tra và phần chưa xác minh.
6. Nếu đã có yêu cầu ghi Sheet, dùng [record-workspace-test-result](../record-workspace-test-result/SKILL.md): ghi status, Note và thời điểm hoàn tất thực thi vào Version đúng model. Nếu chỉ yêu cầu chạy, trả báo cáo và link chat; không suy ra quyền ghi lần đầu.

Khi người dùng yêu cầu “đọc lại và chạy lại”, bắt đầu một lần chạy mới từ snapshot live mới. Nếu người dùng chỉ đổi format Note, dùng kết quả đã xác minh, không chạy UI hoặc thu log mới. Khi nhận “stop”, dừng action mới, gửi prompt và ghi Sheet; không tự tiếp tục sau đó.

Đầu ra: kết quả có bằng chứng, link chat thực tế, session/trace/observation URL, bảng Input và khác biệt Output theo field/ID, và xác nhận các ô status/Note/Version đã ghi khi được phép. Không dùng kết quả lịch sử để chấm lần chạy mới.
