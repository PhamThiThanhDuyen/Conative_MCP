Synthetic evaluation — no live action.

- TC-001 liên quan ticket nhưng chưa có fixture/response để kiểm assertion bắt buộc: kết quả lỗi ticket chưa xác minh; toàn TC BLOCK nếu chưa có failure độc lập.
- Không dùng kết quả normal walkthrough để chấm run này. Không bịa chat URL, Version hoặc trạng thái đã ghi.
- Khi chưa thực thi, giữ status/Version theo contract; chuẩn bị Note blocker để ghi khi có quyền và target live đã xác minh, báo ô chưa ghi. Nếu một run đã thực sự kết thúc bị BLOCK thì dùng timestamp kết thúc run đó.
- Activity draft: “Verify Bug #QA-201: Chưa xác minh TC-001 do thiếu fixture/response để kiểm Stock desc. Chưa đủ bằng chứng kết luận lỗi còn hay hết.”
- Không nêu Gross sales hoặc lỗi ngoài ticket.
- Nhánh không có TC liên quan: QA-2019 không khớp QA-201; TC FAILED không liên quan bị loại. Không chạy, không đổi Sheet và không comment kết luận verify.
