---
name: execute-workspace-ui-func
description: Run selected Workspace UI or functional test cases from Update_TestCase and record observed results against their expected behavior.
---

# Thực thi Workspace UI & Func

1. Xác định môi trường, tổ chức và TC ID theo phạm vi yêu cầu. Mở Update_TestCase theo [tài liệu nguồn](../../references/sources.md) và xác nhận ID duy nhất.
2. Đọc Precondition, dữ liệu test, URL, Steps, Expected Result và các prompt liên quan. Dùng [quy ước cột](../../references/sheet-column-contract.md) để chọn ngôn ngữ và điền placeholder. Nếu thiếu fixture hoặc quyền cần thiết, ghi rõ điều kiện chưa đáp ứng.
3. Trước khi chạy trên môi trường live hoặc kết nối khách hàng, áp dụng tiêu chuẩn live testing của repo. Chạy đúng các bước của TC và đối chiếu phần giao diện cùng phần backend khi được yêu cầu. Phân biệt dữ liệu quan sát với suy luận.
4. Ghi kết quả theo [mẫu](../../assets/test-result-template.md). Pass khi toàn bộ kỳ vọng bắt buộc đã được xác minh; Fail khi có sai lệch quan sát được; Blocked khi thiếu điều kiện để thực thi hoặc xác minh; Not Run khi chưa thực thi. Chỉ ghi vào Google Sheets khi người dùng yêu cầu.
