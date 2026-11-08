---
name: write-qa-testcases
description: Write, revise, compare, or extend QA test cases and scenarios using the user's agreed spreadsheet format. Use for viết test case, lên scenario, sửa steps/expected, or bổ sung coverage. Produces natural Vietnamese QA content and simple English end-user prompts; does not execute tests.
---

# Viết test case và scenario QA

Đọc [chuẩn viết và ví dụ](references/writing-standard.md) khi soạn, sửa hoặc rà test case. File này giữ toàn bộ quy tắc người dùng đã chốt; không dùng mẫu cũ thay cho yêu cầu mới.

## Phạm vi

Chỉ soạn và cập nhật tài liệu theo yêu cầu. Không tự chạy test, tạo dữ liệu nghiệp vụ hoặc chuyển trạng thái thành Pass. Bản trong dự án là draft chờ review, chưa được promote hoặc cài đặt từ gói này.

## Cách làm

1. Đọc nguồn, mẫu và header/validation thực tế. Nếu được yêu cầu dùng toàn bộ prompt, kiểm kê đủ từng dòng và ánh xạ nguồn; giữ đúng nghiệp vụ.
2. Rà coverage theo mục tiêu, thao tác và assertion; chỉ thêm phần thiếu. Không cố định số case hoặc dữ liệu của lần trước.
3. Viết ngắn và tự nhiên: nội dung QA tiếng Việt; prompt AI tiếng Anh đơn giản, có source và kỳ/ngày chốt. Không lọc bằng product/variant ID cụ thể trừ khi người dùng yêu cầu; report sản phẩm phải có cột PRODUCT ID để compare.
4. Giữ format cột của mẫu. Bộ mới dùng TC-001, TC-002… từ trên xuống; chỉ đánh lại ID cũ khi được yêu cầu và cập nhật tham chiếu nội bộ.
5. Steps đánh số, xuống dòng thật; dùng 3.1, 3.2 khi cần. Expected mỗi ý một dòng, đánh số lại từ 1. Chỉ nêu thao tác và kết quả đặc thù, tránh lặp checklist dài.
6. Với report AI, đối chiếu mọi thông tin text/KPI/table/chart và mọi trang với Output log Langfuse của đúng response; so phạm vi UI công bố với Input, không kiểm Input giống prompt. Số UI tự tính phải có input/rule; ghi rõ dữ liệu thiếu, không bịa fixture hay kết quả.
7. Không thêm kiểm tra Title, Unit, Format theo ReportConative. Vẫn kiểm dữ liệu, cột và hiển thị theo prompt/contract khi case yêu cầu.
8. Khi ghi Sheets, dùng skill Google Sheets hiện có, sửa đúng phạm vi, giữ trạng thái/dropdown/format và đọc lại kết quả. Không ghi live workbook nếu yêu cầu chỉ là soạn draft.

Xem schema 12 cột, quy tắc đối chiếu, cách xử lý thiếu đầu vào và mẫu Steps/Expected trong [writing-standard.md](references/writing-standard.md). Ưu tiên chỉ dẫn mới nhất của người dùng; không thêm vòng xin lại quyền cho việc đã được cho phép.
