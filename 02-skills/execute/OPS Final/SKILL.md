---
name: ops-summary-api-to-sheet
description: >-
  Chạy flow OPS theo từng org: Summary Variant, List Variant, Summary Product,
  List Product; ghi Google Sheet sau mỗi chặng rồi mới sang org tiếp theo.
---

# OPS Final — Summary và List theo từng org

Đọc [FLOW.md](FLOW.md) để thực thi flow tổng. Tên resource nằm trong
[run-settings.md](references/run-settings.md). Yêu cầu tạo/sửa skill chỉ cập
nhật tài liệu, chưa chạy API hoặc ghi Sheet.

## Input và đầu ra

Nhận org hoặc danh sách org theo thứ tự, source và timerange cho từng org.
Chỉ hỏi phần thiếu; không tự chạy mọi org/source trong Sheet.
Mặc định flow tổng chạy cả Summary và List theo thứ tự dưới đây. Nếu người
dùng chỉ yêu cầu một phần, chạy đúng phần đó, giữ thứ tự tương đối.

Mỗi org/source có hai cột riêng trong mỗi tab `Sales_by_variant` và
`Sales_by_product`: Summary và List. Tổng cộng bốn cột khi chạy flow đầy đủ.
Cột có dropdown và note cho Failed. Không gộp kết quả khác org, source,
timerange hoặc Summary/List vào cùng cột.

## Thứ tự cho từng org/source

1. Đọc metadata và ba tab Sheet, đối chiếu org/source với `Danh sách org`.
   Mở Postman in-app; chọn workspace, collection, environment và thực hiện
   Login/Choose_Org theo [execute-api-ops.md](execute-api-ops.md).
2. Chạy `Summary_Variant` → ghi cột Summary trong `Sales_by_variant` → đọc lại.
3. Chạy mọi API trong `List_Variant`, bắt đầu `Variant_List_Product_Info` →
   ghi cột List trong `Sales_by_variant` sau mỗi API → chốt và đọc lại cả cột.
4. Chỉ khi hai chặng Variant đã lưu và xác minh: chạy `Summary_Product` →
   ghi cột Summary trong `Sales_by_product` → đọc lại.
5. Chạy mọi API trong `List_Product` → ghi cột List trong `Sales_by_product`
   sau mỗi API → chốt và đọc lại cả cột.
6. Xác minh cả bốn chặng đã hoàn tất. Nếu org còn source được yêu cầu,
   làm tiếp source đó; xong toàn bộ phạm vi của org mới chuyển sang org kế.
   Chạy Choose_Org cho org mới và xác minh token/input; không dùng kết quả cũ.
7. Báo kết quả theo từng org/source và bốn chặng bằng
   [mẫu báo cáo](assets/run-report-template.md).

Summary theo [execute-api-ops.md](execute-api-ops.md), List theo
[execute-api-list.md](execute-api-list.md). Ghi và xác minh bằng
[skill ghi Sheet](skill/record-ops-summary-results/SKILL.md) và
[sheet-contract.md](references/sheet-contract.md).

## Quy tắc chính

- Chỉ sang chặng sau khi chặng hiện tại đã ghi và xác minh. Metric Failed
  vẫn là kết quả hợp lệ; lỗi thực thi hoặc chưa lưu được thì dừng tại chặng đó.
- Mỗi API List kiểm tra 100 item: limit 20, offset 0, 20, 40, 60, 80 ở cả
  query và script. Giữ logic kiểm tra và auth; không Save collection/query.
- List gộp lũy kế trong cột riêng: có đỏ ở bất kỳ item/trang/API nào thì
  Failed; xanh sau không xóa lỗi trước. Chỉ chốt N/A sau khi hết folder.
- Tick xanh → Passed; tick đỏ → Failed kèm nguyên văn lỗi trong cell note.
  Chưa chạy/chạy lỗi không phải N/A. Không suy ra Passed từ HTTP 200 hoặc số 0.
- Không lưu credentials, token, cookie hoặc auth response vào chat/file/Sheet.
- Bị kẹt: giữ browser in-app mở, báo org/source/chặng/API/offset và phần cần
  hỗ trợ; chờ người dùng. Resume đúng chặng/cột, không tự sang org tiếp,
  chạy lại từ đầu hoặc tạo cột trùng.
