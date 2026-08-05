# Import PO _v2

> Nguồn: [Google Sheet – 75191_Import Purchase Order Updates (UC4)_Checklist](https://docs.google.com/spreadsheets/d/1lxfkZKZZ9ju53dzojPtXzRk2tfX8fazY0IrPes-6DDQ/edit?gid=0#gid=0)
> Tab: `Test case` (gid: `0`)

Tổng số dòng có dữ liệu: **47**.

## Dữ liệu

| Cột 1 | Cột 2 | Cột 3 | Cột 4 | Cột 5 | Cột 6 | Cột 7 | Cột 8 | Cột 9 | Cột 10 | Cột 11 | Cột 12 | Cột 13 | Cột 14 | Cột 15 | Cột 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Priority | EST/h | Precondition | Test Case ID | Test Case Title | Description | Description - SubData test | Application URL/Route hoặc API Endpoint | Steps | Expected Result (Front-end) | Expected Result (Back-end) | Expected Impact | Automation Candidate | Confirmation Status | Note (How to Verify) | QA Status |
| Import Purchase Order Updates (UC4) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Kiểm tra wording Received Qty và Received Date |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra ở trên UI |  |  |  | Hiển thị wording là Received Qty và Received Date |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra ở file template |  |  |  |  | Hiển thị wording là Received Qty và Received Date |  |  |  |  |  |
|  |  |  |  | Kiểm tra vị trí Received Qty và Received Date |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra ở trên UI |  |  |  |  + Received Qty: Sau cột Order Qty và trước cột Received Date<br> + Received Date: Sau cột Received Qty và trước cột Cost |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra ở file template |  |  |  |  |  + Received Qty: Sau cột Order Qty và trước cột Received Date<br> + Received Date: Sau cột Received Qty và trước cột Cost |  |  |  |  |  |
|  |  |  |  | Kiểm tra không còn hiển thị cột Status và Expected Arrival Date* |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra không còn hiển thị trên UI |  |  |  | Không còn hiển thị trên UI cột Status và Expected Arrival Date* |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra không còn hiển thị trên file template |  |  |  |  | Không còn hiển thị trên file template cột Status và Expected Arrival Date* |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra import thành công khi không còn hiển thị cột Status và Expected Arrival Date* |  |  |  |  | Vẫn import thành công khi không còn hiển thị cột Status và Expected Arrival Date* |  |  |  |  |  |
|  |  |  |  | Kiểm tra template PO đúng gồm các cột |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra trên UI |  |  |  | 1) PO Number*<br>2) Supplier*<br>3) Warehouse*<br>4) Warehouse ID<br>5) Item SKU*<br>6) Order Qty*<br>7) Received Qty<br>8) Received Date<br>9) Cost |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra trên template import |  |  |  |  | 1) PO Number*<br>2) Supplier*<br>3) Warehouse*<br>4) Warehouse ID<br>5) Item SKU*<br>6) Order Qty*<br>7) Received Qty<br>8) Received Date<br>9) Cost |  |  |  |  |  |
|  |  |  |  | Kiểm tra import PO thành công |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Import thành công khi nhập tất cả field thông tin |  |  | 1) PO Number*<br>2) Supplier*<br>3) Warehouse*<br>4) Item SKU*<br>5) Order Qty*<br>6) Received Qty<br>7) Received Date<br>8) Cost |  |  |  |  |  |  |  |
|  |  |  |  |  | Khi file import không có data tại cột Received Qty |  |  |  |  |  + Import PO thành công > Hiển thị PO và line item<br> + Không phát sinh shipment |  |  |  |  |  |
|  |  |  |  |  |  | Import thành công PO với status Open |  |  |  | Kiểm tra PO chuyển status Open khi chưa có item nào được receied |  |  |  |  |  |
|  |  |  |  |  | Khi file import có data tại cột Received Qty = 0 |  |  |  |  |  + Import PO thành công > Hiển thị PO và line item<br> + Không phát sinh shipment |  |  |  |  |  |
|  |  |  |  |  |  | Import thành công PO với status Open |  |  |  | Kiểm tra PO chuyển status Open khi chưa có item nào được receied |  |  |  |  |  |
|  |  |  |  |  | Khi file import có data tại cột Received Qty > 0 |  |  |  |  |  + Import PO thành công > Hiển thị PO và line item<br> + Phát sinh shipment theo số received qty |  |  |  |  |  |
|  |  |  |  |  |  | Import thành công PO với status Partially Received |  |  |  | Kiểm tra PO chuyển status Partially Received khi có item được nhận 1 phần |  |  |  |  |  |
|  |  |  |  |  |  | Import thành công PO với status Received và số lượng Received Qty =  Order Qty |  |  |  | Kiểm tra PO chuyển status Received khi tất cả item được nhận |  |  |  |  |  |
|  |  |  |  |  |  | Import thành công PO với status Received và số lượng Received Qty >  Order Qty |  |  |  | Kiểm tra PO chuyển status Received khi tất cả item được nhận |  |  |  |  |  |
|  |  |  |  |  | Khi file import có data tại cột Received Date hợp lệ |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Kiểm tra import PO thất bị khi import thông tin invalid |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Received Qty < 0 |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Received Qty là số thập phân |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Received Date không hợp lệ |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Kiểm tra định dạng file |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Cho phép upload file với định dạng CSV / XLSX |  |  |  |  | Upload file thành công |  |  |  |  |  |
|  |  |  |  |  | Không cho phép upload file với định dạng khác CSV / XLSX |  |  |  |  | Hiển thị thông báo lỗi Unsupported file type. Please upload CSV. |  |  |  |  |  |
|  |  |  |  | Kiểm tra khi file không có header  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra khi  file thiếu số lượng header |  |  |  |  | Disable Continue button |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra khi  file thừa số lượng header |  |  |  |  | Disable Continue button |  |  |  |  |  |
|  |  |  |  | Kiểm tra khi các field require thiếu thông tin data |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | PO Number* |  |  |  |  | Disable continue button; show tooltip listing missing required mappings. |  |  |  |  |  |
|  |  |  |  |  | Supplier* |  |  |  |  | Disable continue button; show tooltip listing missing required mappings. |  |  |  |  |  |
|  |  |  |  |  | Warehouse* |  |  |  |  | Disable continue button; show tooltip listing missing required mappings. |  |  |  |  |  |
|  |  |  |  |  | Item SKU* |  |  |  |  | Disable continue button; show tooltip listing missing required mappings. |  |  |  |  |  |
|  |  |  |  |  | Order Qty* |  |  |  |  | Disable continue button; show tooltip listing missing required mappings. |  |  |  |  |  |
|  |  |  |  | Kiểm tra giới hạn upload file |  |  |  | file contains > 10,000 rows |  | Reject upload on step 3 and show error: "Maximum rows per file: 10,000 rows. Your file contains X rows. Split your file into multiple files (≤10,000 rows each) and try again."<br> |  |  |  |  |  |
|  |  |  |  | Import trùng với PO trong hệ thống |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Import thành công trùng với PO có status Draft, Pending Approved, Open, Partially Fulfilled |  |  |  |  | Merge line items theo rules: duplicate SKU sum Order Qty, lấy giá trị cuối cho non-additive fields |  |  |  |  |  |
|  |  |  |  |  | Import thất bại trùng với PO có status Closed, Fulfilled, or Canceled |  |  |  |  | Hiển thị thông báo PO number already exists and is {current_status}. Cannot update this PO. |  |  |  |  |  |
|  |  |  |  |  | Kiểm tra data không bị mất khi PO đã có sẵn data PRODUCTION START DATE, Est. completion, <br>COMPLETION DATE thì không bị mất khi import PO |  |  |  |  |  |  |  |  |  |  |
