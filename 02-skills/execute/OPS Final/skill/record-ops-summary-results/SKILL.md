---
name: record-ops-summary-results
description: Ghi kết quả Summary hoặc List OPS vào Google Sheet. List gộp các trang và API trong cùng cột, giữ Failed và thêm note cho từng lỗi.
---

# Ghi kết quả Summary hoặc List OPS

Dùng sau khi một request Summary hoàn tất, hoặc sau mỗi API List đủ 5 trang.
List gộp lũy kế từ đầu folder theo [quy tắc List](../../references/result-rules.md#kết-quả-list-qua-nhiều-trang-và-api).
Skill này chỉ ghi kết quả đã có;
không chạy API và không tự tính lại pass/fail.

1. Đọc [sheet-contract.md](../../references/sheet-contract.md) và
   [result-rules.md](../../references/result-rules.md).
2. Xác minh workbook ID, tab, organization/source/timerange, chặng Summary/List,
   cột riêng của chặng hiện tại và
   lần chạy Postman tương ứng. Đọc lại header, dòng metric và ô đích.
   Mỗi ô status cần dropdown giống cột kiểm tra trước trong cùng tab.
3. Lập bảng gồm: dòng Sheet, Name, Key, kết quả, dòng thông báo lỗi.
   Chỉ dùng Name/Key và script hiện tại để xác định metric; không đoán theo ID
   hoặc số thứ tự dòng. Nếu mapping mơ hồ, dừng hỏi người dùng.
4. Ghi đúng `Passed`, `Failed`, `N/A`. Với List chưa xong folder, chỉ ghi metric
   đã có kết quả; chưa điền N/A. Giữ Failed từ mọi trang/API trước.
   Mỗi ô Failed phải có cell note
   chứa nguyên văn thông báo tick đỏ của metric đó; nhiều dòng lỗi thì xuống dòng.
   Dùng “Chèn → Ghi chú”, không dùng comment hoặc cột Note chung.
5. Chỉ ghi các dòng metric trong cột của lần chạy này. Không sửa metric,
   kết quả cũ hoặc tab `Danh sách org`. Nên ghi status và note cùng một batch.
6. Đọc lại header, từng status, note và dropdown sau khi ghi. Khi hoàn tất
   folder List hoặc request Summary, số ô kết quả phải bằng số dòng metric.
   Mọi Failed đều có note. Phân biệt đã lưu một API với đã xong cả folder.

Quay lại [flow tổng](../../FLOW.md) sau khi xác minh: Summary Variant →
List Variant → Summary Product → List Product. Chỉ báo org đã xong khi cả
bốn chặng đã lưu; chưa lưu xong thì không chuyển chặng hoặc org tiếp theo.

Summary dùng [build_result_plan.py](../../scripts/build_result_plan.py);
List dùng [build_list_result_plan.py](../../scripts/build_list_result_plan.py) để tạo
bảng ghi từ dữ liệu đã xác minh, theo
[hướng dẫn input](../../references/result-plan.md). Script chạy offline,
không đọc console, không gọi API, không sửa Google Sheet.

Nếu lệnh ghi bị timeout, đọc lại trước khi thử lại. Giữ các ô đúng đã lưu,
chỉ ghi tiếp phần còn thiếu của cùng lần chạy. Chưa xác định được trạng thái
lưu thì báo rõ và giữ browser in-app mở để người dùng kiểm tra.
