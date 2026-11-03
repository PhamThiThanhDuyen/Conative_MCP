# Quy ước Google Sheets

- Đọc metadata, xác nhận tên tab và tìm cột theo tiêu đề hiện tại.
- Trong Prompt, dùng Test Case ID để nối với Update_TestCase. Một ô có thể chứa nhiều ID phân tách bằng dấu phẩy. Ô trống biểu thị chưa có TC tương ứng. Đọc ghi chú ô để nhận biết ánh xạ một phần.
- Prompt (English) và Prompt (Vietnamese) trong Update_TestCase chứa danh sách đánh số từ 1, mỗi prompt một dòng. Khi có cả hai ngôn ngữ, đối chiếu theo số thứ tự. Bỏ tiền tố số thứ tự khi gửi prompt.
- Thay placeholder bằng dữ liệu QA đúng với precondition. Tách các bước hội thoại dựa trên Steps. Chỉ chạy biến thể độc lập hoặc cả hai ngôn ngữ khi nằm trong phạm vi được yêu cầu.
- Prompt tham chiếu không mở rộng Expected Result của TC. Ghi rõ phần thiếu bao phủ. Nếu cần ghi kết quả theo yêu cầu, kiểm tra cột và danh sách giá trị QA Status hiện tại trước khi cập nhật.
