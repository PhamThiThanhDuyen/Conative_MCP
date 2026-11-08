# Forward evaluation — self-review, synthetic

Các snapshot và kết quả trong thư mục này là dữ liệu synthetic, không phải live testcase execution hoặc reviewer độc lập.

| Tình huống | Hành vi/kết quả đã kiểm | Giới hạn |
|---|---|---|
| Normal UI/log đúng conversation/turn, 2 ID và 3 field, thứ tự rows khác nhau | Helper PASSED, 6 field matches; có output artifact normal-output.json | Chỉ field values, không chấm cả TC |
| Thiếu observation ID | Helper BLOCK trước value comparison, missing-observation-output.json | Không thay bằng QE hoặc tự dựng observation |
| Cùng conversation nhưng khác lượt trả lời | Helper BLOCK, wrong-turn-output.json | Không cho dữ liệu lượt cũ pass lượt mới |
| UI làm tròn 1000.25 thành 1000 | Helper FAILED, ui_minus_log=-0.25, rounding-output.json | Không kết luận backend tính sai |
| UI khớp Output nhưng Input query dùng kỳ khác TC đã quy định | Walkthrough contract: FAILED assertion Input/scope, giữ value check có giới hạn | Không đổi query hoặc gọi Postman; không phải test live |
| Session ID chứa tenant + conversationId; có trace title và trace nội dung | Walkthrough runtime: lọc conversationId, xác minh tenant/turn; chọn trace nội dung và query_data | Bản quan sát live chỉ xác minh điều hướng và Raw; chưa so với Workspace UI |
| Chỉ sửa Note của evidence lịch sử | Walkthrough record: giữ nguồn lịch sử/status/Version, không tạo run/log mới | Không đổi nhãn QE cũ thành log |

Đã đọc lại lời gọi/root routing, runtime, contract, templates và dependency. Những walkthrough bằng văn bản là self-evaluation; không thay human review hoặc xác minh nghiệp vụ.
