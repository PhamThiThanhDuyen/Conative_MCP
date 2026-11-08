---
name: record-ops-summary-results
description: Ghi kết quả metric từ một lần chạy Summary OPS hoàn tất vào cột mới trên Google Sheet, kèm ghi chú cho ô Failed.
---

# Ghi kết quả Summary OPS

Dùng sau khi một request Summary đã hoàn tất. Skill này chỉ ghi kết quả đã có;
không chạy API và không tự tính lại pass/fail.

1. Đọc [sheet-contract.md](../../references/sheet-contract.md) và
   [result-rules.md](../../references/result-rules.md).
2. Xác minh workbook ID, tab, organization/source/timerange, cột mới và
   lần chạy Postman tương ứng. Đọc lại header, dòng metric và ô đích.
   Mỗi ô status cần dropdown giống cột kiểm tra trước trong cùng tab.
3. Lập bảng gồm: dòng Sheet, Name, Key, kết quả, dòng thông báo lỗi.
   Chỉ dùng Name/Key và script hiện tại để xác định metric; không đoán theo ID
   hoặc số thứ tự dòng. Nếu mapping mơ hồ, dừng hỏi người dùng.
4. Ghi đúng `Passed`, `Failed`, `N/A`. Mỗi ô Failed phải có cell note
   chứa nguyên văn thông báo tick đỏ của metric đó; nhiều dòng lỗi thì xuống dòng.
   Dùng “Chèn → Ghi chú”, không dùng comment hoặc cột Note chung.
5. Chỉ ghi các dòng metric trong cột của lần chạy này. Không sửa metric,
   kết quả cũ hoặc tab `Danh sách org`. Nên ghi status và note cùng một batch.
6. Đọc lại header, từng status, note và dropdown sau khi ghi. Số ô đã ghi phải
   bằng số dòng metric; mọi Failed đều có note. Sau đó mới báo đã lưu thành công.

Có thể dùng [build_result_plan.py](../../scripts/build_result_plan.py) để tạo
bảng ghi từ dữ liệu đã xác minh, theo
[hướng dẫn input](../../references/result-plan.md). Script chạy offline,
không đọc console, không gọi API, không sửa Google Sheet.

Nếu lệnh ghi bị timeout, đọc lại trước khi thử lại. Giữ các ô đúng đã lưu,
chỉ ghi tiếp phần còn thiếu của cùng lần chạy. Chưa xác định được trạng thái
lưu thì báo rõ và giữ browser in-app mở để người dùng kiểm tra.
