# Design import PO

> Nguồn: [Conative Dev v1.0 Part1 – Figma](https://www.figma.com/design/SnkmfUvAkvGFQMWWyNdAAB/Conative_Dev_v1.0_Part1?node-id=40008633-393019&t=knE1F4BxrniH7imT-4)
> Node chính: `Import PO` — `40008633:393019`

## 1. Tổng quan

Design mô tả luồng Import Purchase Order trong màn hình Purchase Order, gồm wizard 3 bước:

1. Upload file.
2. Map Column.
3. Import và Results.

Màn hình nằm trong layout Inventory Management, có sidebar, header người dùng và khu vực nội dung chính.

## 2. Step 1 — Upload file

### Thành phần giao diện

- Modal/wizard có tiêu đề Import PO.
- Thanh tiến trình hiển thị các bước Upload file, Map Column và Import/Results.
- Khu vực upload file CSV.
- Link tải template file.
- Hiển thị tên file sau khi upload thành công.
- Icon chỉnh sửa/thay thế file.
- Icon xóa file.
- Nút `Cancel` để đóng luồng.
- Nút `Map column` chỉ được enable sau khi file hợp lệ được upload.

### Trạng thái lỗi

- Không chọn file: hiển thị lỗi required tại khu vực upload.
- File không hợp lệ hoặc thiếu column bắt buộc: hiển thị trạng thái lỗi và hướng dẫn sửa file.
- Khi file lỗi nghiêm trọng, không cho phép tiếp tục sang bước mapping.

## 3. Step 2 — Map Column

### Thành phần giao diện

- Cột trái: field của Conative.
- Cột phải: dropdown chọn column từ file upload.
- Field bắt buộc được đánh dấu `*`.
- Mapping progress hiển thị số field đã map và số field còn thiếu.
- Có tooltip hoặc inline message liệt kê required mapping còn thiếu.
- Nút `Back` quay về bước Upload file.
- Nút `Continue` chỉ enable khi các required field đã được map.

### Field theo template Import PO hiện hành

Template hiện hành gồm 8 column:

1. `PO Number*`
2. `Supplier*`
3. `Warehouse*`
4. `Item SKU*`
5. `Order Qty*`
6. `Received Qty`
7. `Received Date`
8. `Cost`

`Status`, `Expected Arrival Date` và `Warehouse ID` không thuộc template import hiện hành.

### Mapping validation

- Thiếu required mapping: disable Continue và hiển thị field còn thiếu.
- Một column trong file được map cho hai field Conative: hiển thị lỗi conflict trên các field liên quan.
- Mapping phải được giữ nguyên khi user quay lại từ bước kế tiếp.
- Warehouse mapping sử dụng danh sách warehouse hợp lệ trong hệ thống.

## 4. Step 3 — Import và Results

### Import state

- Khi user nhấn Import, hệ thống xử lý dữ liệu theo từng dòng.
- Các dòng cùng `PO Number` được group thành một PO.
- Một PO có thể có nhiều line item theo SKU.
- Nút Import cần chuyển sang trạng thái loading/disabled trong lúc xử lý để tránh submit trùng.

### Kết quả thành công

- Hiển thị trạng thái Import Successful.
- Hiển thị số dòng import thành công.
- Có action `Import Another File`.
- Có action `View Imported Items`.

### Kết quả partial

- Hiển thị summary gồm:
  - Success count.
  - Error count.
  - Warning count.
- Có action xem các item thành công.
- Có action tải file kết quả hoặc file lỗi.

### Kết quả thất bại nghiêm trọng

Design hiển thị modal `Import Failed` với:

- Icon lỗi.
- Tiêu đề `Import Failed`.
- Nội dung reason, ví dụ thiếu required columns.
- Danh sách column cần bổ sung.
- Nút `Download template file`.
- Nút `Try Again`.
- Nút đóng modal.

## 5. Data behavior cần đối chiếu với testcase

- `Received Qty` rỗng hoặc bằng `0`: tạo/cập nhật PO và PO line, không tạo shipment.
- `Received Qty > 0`: tự tạo shipment cho PO line và lưu `Received Date` hợp lệ.
- `Received Qty < 0`: reject row, không tạo shipment.
- `Received Date` không hợp lệ: reject row, không tạo shipment.
- Duplicate SKU trong cùng PO: hiển thị warning và merge theo business rule.
- Dòng lỗi phải được giữ trong Error File cùng `error_reason`.

## 6. UI checklist cho QA

| Khu vực | Điểm kiểm tra |
|---|---|
| Wizard | Đúng thứ tự 3 bước, progress state rõ ràng |
| Upload | File name, success state, edit/delete, Cancel |
| Mapping | Field list, required marker, dropdown, progress, lỗi mapping |
| Import | Loading/disable, chống double submit |
| Results | Success/Error/Warning count và action buttons |
| Failed modal | Reason, missing columns, download template, retry |
| Data outcome | PO grouping, line item, shipment, Error File |

## 7. Tham chiếu liên quan

- [SRS_PO](./SRS_PO.md)
- [Template_Import_PO](./Template_Import_PO.md)
- [Testcase UC4 đầy đủ](../../06-demo/import-po-uc4/testcase-uc4-full.md)
- [Data test theo template chuẩn](../qa/Data%20test%20Import%20PO%20-%20Template%20Standard.md)
