# Checklist Enhance new PO - Happycase

> Nguồn: [Google Sheet – Enhance new PO - Happycase](https://docs.google.com/spreadsheets/d/1h4dWH60VvWba9katEO1Z3I1w0MZ1QFgqmb267wbMggk/edit?gid=1577106752#gid=1577106752)
>
> Tab: `Enhance new PO - Happycase`
>
> Nội dung được chuyển từ vùng A1:Y400; ô trống được giữ trống.

### Row 1

- **A:** Priority
- **B:** EST/h
- **C:** Precondition
- **D:** Test case title
- **E:** Description
- **F:** Description-sub
- **G:** Description-sub-sub
- **H:** Steps
- **I:** Expected result FE
- **J:** Expected result BE
- **K:** Note
- **L:** STT FE
- **M:** STT BE update API

### Row 2

- **A:** PO List

### Row 3

- **A:** High
- **D:** Kiểm tra UI hiển thị đủ field và wording như design
- **L:** FAILED

### Row 4

- **A:** High
- **D:** Kiểm tra danh sách các status có trong dropdown status
- **I:** Value: Draft, Pending approval, Rejected, Open, Partially Fulfilled, Fulfilled, Closed, Canceled.
- **L:** PASS

### Row 5

- **A:** High
- **D:** Kiểm tra hiển thị đúng list warehouse của soure
- **I:** 1. Kiểm tra số lượng warehouse trả về đúng so với API<br>2. Kiểm tra warehouse name hiển thị đúng so với API
- **J:** 1. Chỉ hiển thị warehouse active<br>2. So sánh số lượng warehouse bằng với số lượng warehouse ở page warehouse list
- **L:** PASS
- **M:** PASS

### Row 6

- **A:** High
- **D:** Kiểm tra search với các thông tin thành công

### Row 7

- **A:** Medium
- **E:** Product Title
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm

### Row 8

- **A:** High
- **E:** Variant Title
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm
- **L:** PASS

### Row 9

- **A:** High
- **E:** SKU
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm
- **L:** PASS

### Row 10

- **A:** Medium
- **E:** ASIN
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm

### Row 11

- **A:** High
- **E:** PO Number
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm
- **L:** PASS

### Row 12

- **A:** High
- **E:** PO ID
- **I:** Hiển thị các PO giống với từ khóa tìm kiếm
- **J:** 1. Kiểm tra số lượng trả về match với list PO trả về<br>2. Kiểm tra số lượng PO trả về đúng với từ khóa tìm kiếm
- **L:** PASS

### Row 13

- **A:** Medium
- **E:** Kiểm tra màn hình tìm kiếm khi search ko có data
- **I:** 1. Hiển thị thông báo "No transfer orders found for <keyword>"<br>2. Hiển thị nội dung thông báo "Try adjusting your search or filters."
- **L:** PASS

### Row 14

- **A:** High
- **D:** Kiểm tra filter thành công
- **L:** FAILED

### Row 15

- **E:** Source
- **L:** PASS

### Row 16

- **A:** High
- **E:** Supplier
- **L:** PASS

### Row 17

- **A:** High
- **E:** Created date
- **K:** Bug 52617
- **L:** FAILED

### Row 18

- **A:** High
- **E:** Expected arrival date
- **K:** Bug 52619
- **L:** FAILED

### Row 19

- **A:** High
- **E:** Received status
- **F:** List: Not received, Under received, Received, Over received. <br>Not received: When {received_qty} = 0<br>Under received: when {received_qty} < {order_qty} <br>Received: when {received_qty} = {order_qty}<br>Over received: when {received_qty} > {order_qty}
- **L:** PASS

### Row 20

- **A:** High
- **D:** Kiểm tra sort cột

### Row 21

- **A:** High
- **E:** Mặc định sort theo Created date by desc
- **L:** PASS

### Row 22

- **A:** High
- **E:** Kiểm tra sort desc và asc cho các cột thành công
- **K:** chưa lên ID kiểm tra lại sau
- **L:** FAILED

### Row 23

- **A:** High
- **F:** PO ID
- **L:** PASS

### Row 24

- **A:** High
- **F:** PO Number
- **L:** PASS

### Row 25

- **A:** High
- **F:** Supplier
- **K:** Bug 52623
- **L:** FAILED

### Row 26

- **A:** High
- **F:** Warehouse
- **K:** Bug 52623
- **L:** FAILED

### Row 27

- **A:** High
- **F:** Create date
- **L:** PASS

### Row 28

- **A:** High
- **F:** Expected arrivel date
- **L:** PASS

### Row 29

- **A:** High
- **F:** Status
- **L:** PASS

### Row 30

- **F:** Received status không có sort
- **K:** Chưa lên ID
- **L:** FAILED

### Row 31

- **A:** High
- **D:** Bulk action > Kiểm tra delete PO thành công

### Row 32

- **A:** High
- **E:** Delete thành công 1 PO
- **H:** xóa PO có status = Draft / Pending Approval / Rejected
- **I:** 1. hiển thị popup confirm khi chọn option delete<br>2. content popup confirm hiển thị đúng<br>3. Delete thành công và hiển thị thông báo "Purchase order deleted successfully" <br>4. Không hiển thị PO đã xóa trong list PO
- **J:** Delete thành công
- **K:** Không có popup confirm
- **L:** FAILED

### Row 33

- **A:** High
- **E:** Delete thành công nhiều PO
- **H:** xóa các PO có status = Draft / Pending Approval / Rejected
- **I:** 1. hiển thị popup confirm khi chọn option delete<br>2. content popup confirm hiển thị đúng<br>3. Delete thành công và hiển thị thông báo "Purchase order deleted successfully" <br>4. Không hiển thị PO đã xóa trong list PO
- **J:** Delete thành công
- **L:** PASS

### Row 34

- **A:** High
- **E:** Delete thành công tất cả PO
- **I:** 1. hiển thị popup confirm khi chọn option delete<br>2. content popup confirm hiển thị đúng<br>3. Delete thành công và hiển thị thông báo "Purchase order deleted successfully" <br>4. Không hiển thị PO đã xóa trong list PO
- **J:** Delete thành công
- **K:** Chờ kiểm tra sau
- **L:** PENDING

### Row 35

- **A:** High
- **E:** Delete PO thất bại
- **H:** xóa các PO có status = Open / Partially Fulfilled / Fulfilled / Closed / Canceled
- **I:** Hiển thị popup error: You cannot delete the selected PO(s). It has already been processed or received.<br>CTA: Close
- **K:** Không cho delete nhưng hiển thị sai wording chưa lên ID
- **L:** FAILED

### Row 36

- **A:** High
- **D:** Phân trang

### Row 37

- **A:** High
- **E:** Kiểm tra hiển thị đúng số lượng PO hiện có của org
- **I:** Kiểm tra total PO hiển thị giống data so với API trả về
- **J:** Kiểm tra hiển thị đúng số lượng PO hiện có của org
- **L:** PASS

### Row 38

- **A:** High
- **E:** Kiểm tra chức năng phân trang hoạt động đúng khi next qua page kế tiếp
- **K:** Chờ có hơn 100 PO r kiểm tra lại
- **L:** PENDING

### Row 39

- **A:** High
- **D:** Kiểm tra hiển thị đúng thông tin PO ngoài list table ở các cột hiển thị đúng
- **H:** 1. Import 1 PO và kiểm tra lại thông PO hiển thị đúng ngoài list<br>2. Create 1 PO và kiểm tra lại thông tin PO hiển thị đúng ngoài list

### Row 40

- **A:** High
- **E:** PO ID
- **I:** 1. Hiển thị tối đa 6 ký tự<br>2. Hiển thị data giống với API trả về
- **J:** 1. Thông tin PO ID hiển thị đúng khi import<br>2. Thông tin PO ID hiển thị đúng khi create PO
- **L:** FAILED

### Row 41

- **A:** High
- **E:** PO NUMBER
- **I:** Hiển thị data giống với API trả về
- **J:** 1. Thông tin PO NUMBER hiển thị đúng khi import<br>2. Thông tin PO NUMBER hiển thị đúng khi create PO
- **L:** PASS

### Row 42

- **A:** High
- **E:** SUPPLIER
- **I:** Hiển thị data giống với API trả về
- **J:** 1. Thông tin SUPPLIER hiển thị đúng khi import<br>2. Thông tin SUPPLIER hiển thị đúng khi create PO
- **L:** PASS

### Row 43

- **A:** High
- **E:** WAREHOUSE
- **I:** Hiển thị data giống với API trả về
- **J:** 1. Thông tin WAREHOUSE hiển thị đúng khi import<br>2. Thông tin WAREHOUSE hiển thị đúng khi create PO
- **L:** PASS

### Row 44

- **A:** High
- **E:** CREATE DATE
- **I:** 1. Hiển thị data giống với API trả về<br>2. Format MMM DD, YYYY
- **J:** 1. Thông tin CREATE DATE hiển thị đúng khi import<br>2. Thông tin CREATE DATE hiển thị đúng khi create PO
- **L:** PASS

### Row 45

- **A:** High
- **E:** EXPECTED ARRIVAL DATE
- **I:** 1. Hiển thị data giống với API trả về<br>2. Format MMM DD, YYYY
- **J:** 1. Thông tin EXPECTED ARRIVAL DATE hiển thị đúng khi import<br>2. Thông tin EXPECTED ARRIVAL DATE hiển thị đúng khi create PO
- **L:** PASS

### Row 46

- **A:** High
- **E:** STATUS
- **I:** 1. Hiển thị data giống với API trả về
- **J:** 1. Thông tin STATUS hiển thị đúng khi import<br>2. Thông tin STATUS hiển thị đúng khi create PO
- **L:** PASS

### Row 47

- **A:** High
- **E:** RECEIVED STATUS
- **I:** 1. Hiển thị data giống với API trả về
- **J:** Received status: {received_qty} of {ordered_qty} <br>If the PO hasn’t received yet → the card is grey<br>If the received qty ≠ ordered qty  → the card is orange<br>If the received qty = ordered qty → the card is green  <br>if the received qty > orderaty -> show the card is orange
- **K:** Chờ dev làm phần PO partial r kiểm tra lại
- **L:** PENDING

### Row 48

- **A:** High
- **E:** ACTIONS

### Row 49

- **A:** High
- **F:** Ẩn bulk action và 3 chấm khi org dùng ERP
- **I:** Ẩn bulk action và 3 chấm khi org dùng ERP
- **K:** Chưa có org nào
- **L:** PENDING

### Row 50

- **A:** High
- **F:** Delete 1 PO thành công
- **H:** xóa PO có status = Draft / Pending Approval / Rejected
- **I:** 1. Delete thành công và hiển thị thông báo "Purchase order deleted successfully" <br>4. Không hiển thị PO đã xóa trong list PO
- **J:** Delete thành công
- **L:** PASS

### Row 51

- **A:** High
- **F:** Delete 1 PO không thành công
- **H:** xóa PO có status = Open / Partially Fulfilled / Fulfilled / Closed / Canceled
- **I:** Disable button Delete
- **K:** Chỉ mới kiểm tra cho Open và Canceled
- **L:** PENDING

### Row 52

- **A:** Tạo mới PO khi không apply MOQ

### Row 53

- **D:** Kiểm tra UI Create PO
- **L:** FAILED

### Row 54

- **A:** High
- **B:** 0.1
- **C:** Đã truy cập trang "Create New PO"
- **E:** UI_NAV_001: Kiểm tra Tiêu đề trang
- **F:** Xác nhận tiêu đề trang hiển thị chính xác.
- **G:** N/A
- **H:** 1. Mở trang "Create New PO".
- **I:** Tiêu đề trang hiển thị là "Create New PO".
- **J:** N/A
- **L:** PASS

### Row 55

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_LAYOUT_002: Kiểm tra Cấu trúc và Bố cục
- **F:** Đảm bảo bố cục trang phù hợp với thiết kế.
- **G:** N/A
- **H:** 1. Mở trang "Create New PO".
- **I:** Trang được chia thành 3 phần chính: Thông tin PO Header, Chi tiết Order Items, và Footer Actions.
- **J:** N/A
- **L:** PASS

### Row 56

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_FIELD_004: Kiểm tra Supplier/Warehouse Field UI
- **F:** Kiểm tra nhãn và placeholder của các trường Supplier và Warehouse.
- **G:** N/A
- **H:** 1. Quan sát trường Supplier và Warehouse.
- **I:** Nhãn: "Supplier*" và "Warehouse*". Placeholder: "Select supplier" và "Select warehouse".
- **J:** N/A
- **L:** FAILED

### Row 57

- **A:** High
- **B:** 0.2
- **C:** N/A
- **E:** UI_BUTTON_007: Kiểm tra Wording và Trạng thái của các nút Action
- **F:** Kiểm tra text và trạng thái kích hoạt của các nút ở footer.
- **G:** N/A
- **H:** 1. Quan sát các nút hành động ở cuối trang.
- **I:** 1. Các nút phải có wording: "Back", "Save as draft", "Request approval", "Issue PO". <br>2. Khi chưa nhập đủ thông tin require thì các button "Save as draft", "Request approval", "Issue PO" đều bị disable<br>3. Khi nhập đủ thông tin thì enable các button
- **J:** N/A
- **L:** PASS

### Row 58

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_FIELD_003: Kiểm tra PO Number Field UI
- **F:** Kiểm tra nhãn, placeholder, và tooltip của trường PO Number.
- **G:** N/A
- **H:** 1. Quan sát trường nhập liệu PO Number. <br>2. Hover chuột lên biểu tượng tooltip.
- **I:** 1. Nhãn: "PO Number*". <br>2. Placeholder: "Enter PO number". <br>3. Tooltip hiển thị: "A number you can create or customize to identify the purchase order on the platform."
- **J:** N/A
- **L:** FAILED

### Row 59

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_DATE_005: Kiểm tra Expected Arrival Date UI
- **F:** Kiểm tra nhãn, placeholder và định dạng ngày.
- **G:** N/A
- **H:** 1. Quan sát trường Expected arrival date. <br>2. Mở Datepicker.
- **I:** 1. Nhãn: "Expected arrival date". <br>2. Placeholder: "Select expected arrival date". <br>3. Định dạng hiển thị ngày: MMM DD, YYYY.
- **J:** N/A
- **L:** PASS

### Row 60

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_ITEM_006: Kiểm tra Search Item UI
- **F:** Kiểm tra nhãn và placeholder của thanh tìm kiếm item.
- **G:** N/A
- **H:** 1. Quan sát thanh tìm kiếm trong phần "Order Items".
- **I:** Placeholder: "Search for Title, SKU".
- **J:** N/A
- **L:** PASS

### Row 61

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_TABLE_008: Kiểm tra Header Order Items Table
- **H:** 1. Quan sát tiêu đề các cột trong bảng Order Items.
- **I:** Wording tiêu đề cột hiển thị như design.<br>  +TITTLE, ON HAND, MOQ, ORDER QTY, RECEIVED QTY, UOM, PRODUCTION START DATE, ESTIMATED COMPLETION, COMPLETION DATE, COST, TOTAL COST, ACTION
- **J:** N/A
- **L:** FAILED

### Row 62

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_TEXTAREA_009: Kiểm tra Note for PO UI
- **F:** Kiểm tra nhãn và placeholder của trường Note.
- **G:** N/A
- **H:** 1. Quan sát trường nhập liệu Note for PO.
- **I:** 1. Nhãn: "Note for PO". <br>2. Placeholder: "Type here".
- **J:** N/A
- **L:** PASS

### Row 63

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** UI_ATTACHMENT_010: Kiểm tra Attachments UI
- **F:** Kiểm tra khu vực tải file đính kèm.
- **G:** N/A
- **H:** 1. Quan sát khu vực Attachments.
- **I:** 1. Khu vực tải file có hướng dẫn: "Click to upload or Drag and Drop files here."
- **J:** N/A
- **L:** FAILED

### Row 64

- **A:** High
- **B:** 0.1
- **C:** Đã thêm ít nhất 1 item
- **E:** UI_ITEM_011: Kiểm tra Total Cost và Total Line
- **F:** Đảm bảo tính toán Total Order Qty và Total Cost hiển thị ở hàng tổng kết trên bảng.
- **G:** N/A
- **H:** 1. Thêm 1 item với Order Qty > 0 và Cost > 0.
- **I:** Hàng tổng kết trên bảng hiển thị tổng số lượng<br>1. Total order qty = SUM of all items ordered qty)<br>2. tổng chi phí (Total cost = Total_cost_1 + ... + Total_cost_n).
- **J:** N/A
- **L:** FAILED

### Row 65

- **D:** Kiểm tra tạo thành công PO khi không apply MOQ

### Row 66

- **E:** Kiểm tra data show ở Create PO hiển thị đúng
- **I:** PO summary: Total order, PO MOQ, % Archieved<br>Table item: name, SKU, On hand, MOQ, cost (hiện tại lấy theo item),gram, total cost<br>Style summary: name, MOQ,order qty, %Archieved
- **J:** Failed on hand 52803<br>Failed style summary 52806
- **L:** FAILED

### Row 67

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **E:** FUNC_MAIN_001: Tạo PO thành công với Status "Open" (Issue PO)
- **F:** Thực hiện tạo PO thành công qua luồng chính và chuyển trạng thái sang Open.
- **G:** BR03: PO phải có ít nhất 1 item.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Issue PO".
- **I:** 1. System hiển thị toast message: "Purchase order created successfully" (M10). User được redirect về trang PO list. PO mới tạo có Status: Open.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Open. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **K:** 1. Tạo thành công nhưng thông báo hiển thị sai
- **L:** FAILED

### Row 68

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **E:** FUNC_MAIN_002.1: Tạo PO thành công với Status "Draft" (Save as Draft) mà nhập thông tin item
- **F:** Thực hiện tạo PO thành công qua luồng chính và lưu nháp.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Save as draft".
- **I:** 1. System hiển thị toast message: "Purchase order saved as draft successfully.". User được redirect về trang PO list. PO mới tạo có Status: Draft.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Draft. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **K:** Bug 52600<br>Bug 52601<br>Tạo thành công
- **L:** FAILED

### Row 69

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **E:** FUNC_MAIN_002.2: Tạo PO thành công với Status "Draft" (Save as Draft) mà không nhập thông tin item
- **F:** Thực hiện tạo PO thành công qua luồng chính và lưu nháp.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Save as draft".
- **I:** 1. System hiển thị toast message: "Purchase order saved as draft successfully.". User được redirect về trang PO list. PO mới tạo có Status: Draft.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Draft. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **K:** Bug 52599
- **L:** FAILED

### Row 70

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **E:** FUNC_MAIN_003: Tạo PO thành công với Status "Pending Approval" (Request Approval)
- **F:** Thực hiện tạo PO thành công qua luồng chính và gửi yêu cầu phê duyệt.
- **G:** BR03: PO phải có ít nhất 1 item.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Request approval".
- **I:** 1. System hiển thị toast message: "Purchase Order submitted for approval successfully.". User được redirect về trang PO list. PO mới tạo có Status: Pending Approval.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Pending Approval. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **K:** 1. Tạo thành công nhưng thông báo hiển thị sai
- **L:** FAILED

### Row 71

- **A:** High
- **B:** 0.3
- **C:** N/A
- **E:** FUNC_MAIN_004: Tính toán Total Cost (Order Item)
- **F:** Đảm bảo trường Total Cost tự động tính toán chính xác sau khi nhập Order Qty và Cost.
- **G:** Total cost = Order qty * Cost.
- **H:** 1. Add item. <br>2. Nhập Order Qty = 10, Cost = $12.5. <br>3. Thay đổi Order Qty thành 20.
- **I:** 1. Total Cost của line item hiển thị: $125.0 (cho 10*12.5)<br>2. sau đó cập nhật thành $250.0 (cho 20*12.5).
- **L:** PASS

### Row 72

- **A:** High
- **B:** 0.5
- **C:** Item có trong Replenishment flow
- **E:** AF_005: Tạo PO từ Replenishment Flow (Pre-filled Data)
- **K:** Dev chưa làm
- **L:** PENDING

### Row 73

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **F:** Tạo PO thành công với Status "Open" (Issue PO)
- **G:** Thực hiện tạo PO thành công qua luồng chính và chuyển trạng thái sang Open.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Issue PO".
- **I:** 1. System hiển thị toast message: "Purchase order created successfully" (M10). <br>2. User được redirect về trang Replenishment Flow<br>3. PO mới tạo có Status: Open và thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Open. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 74

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **F:** Tạo PO thành công với Status "Draft" (Save as Draft)
- **G:** Thực hiện tạo PO thành công qua luồng chính và lưu nháp.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Save as draft".
- **I:** 1. System hiển thị toast message: "Purchase order saved as draft successfully."<br>2. User được redirect về trang Replenishment Flow<br>3. PO mới tạo có Status: Open và thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Draft. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 75

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **F:** Tạo PO thành công với Status "Draft" (Save as Draft) mà không nhập thông tin item
- **G:** Thực hiện tạo PO thành công qua luồng chính và lưu nháp.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Save as draft".
- **I:** 1. System hiển thị toast message: "Purchase order saved as draft successfully."<br>2. User được redirect về trang Replenishment Flow<br>3. PO mới tạo có Status: Open và thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Draft. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 76

- **A:** High
- **B:** 0.5
- **C:** Item có trong hệ thống
- **F:** Tạo PO thành công với Status "Pending Approval" (Request Approval)
- **G:** Thực hiện tạo PO thành công qua luồng chính và gửi yêu cầu phê duyệt.
- **H:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Request approval".
- **I:** 1. System hiển thị toast message: "Purchase Order submitted for approval successfully"<br>2. User được redirect về trang Replenishment Flow<br>3. PO mới tạo có Status: Open và thông tin trong PO detail hiển thị đúng
- **J:** 1. PO được tạo với Status = Pending Approval. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 77

- **D:** Kiểm tra tạo PO thất bại

### Row 78

- **E:** Kiểm tra field require

### Row 79

- **A:** High
- **B:** 0.2
- **F:** VAL_HEADER_002: Thiếu trường bắt buộc PO Number
- **G:** Kiểm tra trường PO Number bị bỏ trống.
- **H:** 1. Bỏ trống PO Number. <br>2. Điền đủ các trường bắt buộc khác (Supplier, Warehouse, Expected arrival date, Items). <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường PO number: "The field is required" (M04).
- **J:** PO không được tạo.
- **K:** Sai wording chưa tạo ID
- **L:** FAILED

### Row 80

- **A:** High
- **B:** 0.2
- **F:** VAL_HEADER_005: Thiếu trường bắt buộc Supplier
- **G:** Kiểm tra các trường Single Selection bắt buộc bị bỏ trống.
- **H:** 1. Bỏ trống Supplier. <br>2. Điền đủ các trường bắt buộc còn lại. <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường bị thiếu: "The field is required" (M04).
- **J:** PO không được tạo.
- **K:** Bắt buộc select<br>Nếu không select thì disable button
- **L:** N/A

### Row 81

- **A:** High
- **B:** 0.2
- **F:** VAL_HEADER_005: Thiếu trường bắt buộc Warehouse
- **G:** Kiểm tra các trường Single Selection bắt buộc bị bỏ trống.
- **H:** 1. Bỏ trống Warehouse<br>2. Điền đủ các trường bắt buộc còn lại. <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường bị thiếu: "The field is required" (M04).
- **J:** PO không được tạo.
- **K:** Bắt buộc select<br>Nếu không select thì disable button
- **L:** N/A

### Row 82

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** VAL_ITEM_002: Thiếu trường bắt buộc (Order Qty)
- **G:** Kiểm tra Order Qty bị bỏ trống.
- **H:** 1. Add item. <br>2. Bỏ trống Order Qty. <br>3. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Order Qty: "The field is required" (M04).
- **J:** Tạo PO không thành công
- **K:** Chuyển về số 0
- **L:** N/A

### Row 83

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** VAL_ITEM_004: Thiếu trường bắt buộc (Cost)
- **G:** Kiểm tra Cost bị bỏ trống.
- **H:** 1. Add item. <br>2. Bỏ trống Cost. <br>3. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Cost: "The field is required" (M04).
- **J:** Tạo PO không thành công
- **K:** Chuyển về số 0
- **L:** N/A

### Row 84

- **A:** High
- **B:** 0.2
- **F:** VAL_HEADER_002: Thiếu trường bắt buộc Expected arrival date
- **G:** Kiểm tra trường Expected arrival date bị bỏ trống.
- **H:** 1. Bỏ trống Expected arrival date<br>2. Điền đủ các trường bắt buộc khác<br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường PO number: "The field is required" (M04).
- **J:** PO không được tạo.
- **K:** Bắt buộc select<br>Nếu không select thì disable button
- **L:** N/A

### Row 85

- **A:** High
- **B:** 0.3
- **C:** PO không có Order Item
- **F:** BR_AF_001.1: Tạo PO với status = Issue PO khi không có item
- **G:** Kiểm tra BR03: PO phải có ít nhất 1 item để Issue
- **H:** 1. Điền đủ các trường bắt buộc (trừ item). <br>2. Click "Issue PO"
- **I:** 1. System hiển thị toast message lỗi (màu cam) ở trên cùng: "Please add at least one item to the purchase order before creating it.". <br>2. PO không được tạo.
- **J:** PO không được tạo.
- **K:** Chờ fix bug 52599<br>rồi kiểm tra lại
- **L:** PENDING

### Row 86

- **A:** High
- **B:** 0.3
- **C:** PO không có Order Item
- **F:** BR_AF_001.2: Tạo PO với status = Request Approval khi không có item
- **G:** Kiểm tra BR03: PO phải có ít nhất 1 item để Request Approval.
- **H:** 1. Điền đủ các trường bắt buộc (trừ item). <br>2. Click "Request approval".
- **I:** 1. System hiển thị toast message lỗi (màu cam) ở trên cùng: "Please add at least one item to the purchase order before creating it.". <br>2. PO không được tạo.
- **J:** PO không được tạo.
- **K:** Chờ fix bug 52599<br>rồi kiểm tra lại
- **L:** Chờ fix bug 52599<br>rồi kiểm tra lại

### Row 87

- **E:** Kiểm tra input invalid

### Row 88

- **A:** High
- **B:** 0.2
- **C:** PO Number đã tồn tại trong hệ thống
- **F:** VAL_HEADER_001: PO Number trùng lặp (Issue PO)
- **G:** PO number is unique.
- **H:** 1. Tạo PO với PO Number đã tồn tại (vd: #CDUPLICATE01). <br>2. Điền đủ các trường require<br>3. click "Issue PO".
- **I:** System hiển thị in-line error message "This PO number already exists" (M08).
- **J:** PO không được tạo.
- **K:** Bug 52608
- **L:** FAILED
- **M:** FAILED

### Row 89

- **A:** Medium
- **B:** 0.2
- **C:** N/A
- **F:** VAL_HEADER_003: PO Number vượt quá Max Length (50 chars)
- **G:** Kiểm tra giới hạn ký tự cho PO Number.
- **H:** 1. Nhập chuỗi 51 ký tự vào trường PO Number. <br>2. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường PO number: "This PO ID is not over 50 characters".
- **J:** N/A

### Row 90

- **A:** High
- **B:** 0.2
- **C:** N/A
- **F:** VAL_HEADER_004: Expected Arrival Date là ngày trong quá khứ
- **G:** Expected arrival date >= {Today date}.
- **H:** 1. Chọn ngày Expected arrival date là ngày hôm qua. <br>2. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Expected arrival date: "Expected day should not be in the past".
- **J:** PO không được tạo nếu Expected arrival date trong quá khứ.
- **K:** Bug 52605
- **L:** FAILED

### Row 91

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** VAL_ITEM_001: Order Qty = 0
- **G:** Kiểm tra Business Rule Order Qty phải > 0.
- **H:** 1. Add item. <br>2. Nhập Order Qty = 0. <br>3. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Order Qty: "Quantity must be greater than 0.".
- **J:** Tạo PO không thành công
- **K:** Hiển thị sai wording -> Xài chung ID với TO
- **L:** FAILED

### Row 92

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** VAL_ITEM_003: Order Qty là số âm
- **G:** Kiểm tra Business Rule Order Qty phải là số dương.
- **H:** 1. Add item. <br>2. Nhập Order Qty = -1.
- **I:** Không cho nhập order quantity < 0
- **J:** Tạo PO không thành công
- **L:** PASS

### Row 93

- **F:** Order Qty là số thập phân
- **I:** Không cho input số thập phân
- **K:** Bug 52674
- **L:** FAILED

### Row 94

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** VAL_ITEM_005: Cost là số âm
- **G:** The cost >= 0.
- **H:** 1. Add item. <br>2. Nhập Cost = -1.
- **I:** Không cho nhập cost < 0
- **J:** Tạo PO không thành công
- **L:** PASS

### Row 95

- **A:** Medium
- **B:** 0.3
- **C:** Đã thêm item
- **F:** VAL_ITEM_006: Max digits cho trường Cost
- **G:** Kiểm tra giới hạn số chữ số cho phần nguyên và phần thập phân của Cost.
- **H:** 1. Nhập số Cost vượt quá giới hạn (ví dụ: > 131072 chữ số phần nguyên). <br>2. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Cost: "Please limit the integer part to 131072 digits and the decimal part to 16383 digits.".
- **J:** N/A

### Row 96

- **A:** Medium
- **B:** 0.3
- **C:** PO có Note
- **F:** BR_AF_004: Max Length cho Note for PO
- **G:** Kiểm tra giới hạn ký tự cho Note for PO (5000 ký tự).
- **H:** 1. Nhập chuỗi 5001 ký tự vào trường Note for PO. <br>2. Click ra khỏi field.
- **I:** System hiển thị error message: "The input exceeds 5000 characters.”.
- **J:** N/A

### Row 97

- **A:** Medium
- **B:** 0.2
- **C:** Tải file > 5MB
- **F:** EDGE_001: Lỗi Max Size Attachment
- **G:** Kiểm tra lỗi khi tải file vượt quá giới hạn 5MB.
- **H:** 1. Click vào khu vực Attachments và chọn file có dung lượng 5.1MB.
- **I:** System hiển thị toast message lỗi: "The attachment exceeds the size limit of 5MB. Please upload a smaller file.".
- **J:** File không được upload.

### Row 98

- **A:** Medium
- **B:** 0.2
- **C:** Tải file định dạng không hỗ trợ
- **F:** EDGE_002: Lỗi Invalid File Format Attachment
- **G:** Kiểm tra lỗi khi tải file không đúng định dạng cho phép.
- **H:** 1. Click vào khu vực Attachments và chọn file .zip.
- **I:** System hiển thị toast message lỗi: "Invalid file format.".
- **J:** File không được upload.

### Row 99

- **D:** Kiểm tra delete item thành công

### Row 100

- **A:** High
- **B:** 0.2
- **C:** Đã thêm nhiều item
- **E:** EDGE_005: Xóa Line Item và cập nhật Total Cost
- **F:** Kiểm tra chức năng xóa item và đảm bảo Total Cost được tính lại chính xác.
- **G:** The delete icon (Trash icon) is on each row item allows the user remove item. Total cost updates when Order Qty or Cost changes.
- **H:** 1. Add 2 items (A và B). <br>2. Ghi nhận Total Cost hiện tại. <br>3. Click biểu tượng thùng rác để xóa Item B.
- **I:** 1. Item B biến mất khỏi danh sách. <br>2. Total Cost được tính lại = Cost của Item A.
- **L:** PASS

### Row 101

- **A:** High
- **C:** Đã thêm nhiều item
- **E:** Xóa nhiều item thành công
- **F:** Kiểm tra chức năng xóa nhiều item và đảm bảo Total Cost được tính lại chính xác.
- **H:** 1. Add 5 items<br>2. Tick chọn 3 item <br>3. Click button Delete
- **I:** 1. 3 item biến mất khỏi danh sách. <br>2. Total Cost được tính lại = Cost của 2 item còn lại
- **L:** PASS

### Row 102

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **D:** EDGE_006.1: Tìm kiếm Item thành công
- **K:** Bug 52609
- **L:** FAILED

### Row 103

- **A:** High
- **E:** Tìm kiếm matching by title
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị item có title trùng với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 104

- **A:** High
- **E:** Tìm kiếm matching by SKU
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị item có SKU trùng với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 105

- **A:** High
- **E:** Tìm kiếm matching by ASIN
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị item có ASIN trùng với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 106

- **A:** High
- **E:** Tìm kiếm contains từ khóa so với title
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị những item có title chứa từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 107

- **A:** High
- **E:** Tìm kiếm không phân biệt chữ hoa / chữ thường
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị những item có title chứa với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 108

- **A:** High
- **E:** Tìm kiếm chứa warehouseảng trắng trước / sau
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị những item có title chứa với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 109

- **A:** High
- **E:** Tìm kiếm chứa warehouseảng trắng
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **I:** Hiển thị tất cả item<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 110

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **D:** EDGE_006.2: Tìm kiếm Item không có kết quả
- **E:** Kiểm tra giao diện khi tìm kiếm item trong danh sách Order Items không có kết quả.
- **F:** When no result is matched to searching value, show message like this: [No Data Found Image].
- **H:** 1. Add 1 item. <br>2. Nhập từ khóa không tồn tại vào ô Search Item (ví dụ: "NONEXISTENT").
- **I:** System hiển thị hình ảnh "SORRY! No data found" và text hướng dẫn: "Please try searching other keywords or adjusting your filter".
- **J:** N/A
- **L:** STUCK

### Row 111

- **A:** High
- **B:** 0.3
- **C:** Đã thêm item
- **D:** VAL_ITEM_007: Kiểm tra hiển thị On Hand
- **E:** Xác nhận On Hand Qty hiển thị đúng dựa trên Warehouse đã chọn.
- **F:** If no warehouse is selected, stock = 0. Once a warehouse is selected, stock updates based on the selected warehouse..
- **H:** 1. Chưa chọn Warehouse. <br>2. Chọn Warehouse (A) có On Hand Item X = 100. <br>3. Đổi sang Warehouse (B) có On Hand Item X = 50.
- **I:** 1. Ban đầu On Hand hiển thị: 0. <br>2. Sau khi chọn W(A), On Hand hiển thị: 100. <br>3. Sau khi chọn W(B), On Hand cập nhật thành: 50.
- **J:** BE trả về On Hand Qty chính xác.
- **K:** Bug 52598
- **L:** FAILED

### Row 112

- **A:** High
- **C:** Đã upload file đính kèm
- **D:** Kiểm tra xóa file Attachments thành công
- **H:** 1. Mở màn hình Create PO<br>2. Upload file đính kèm<br>3. Click icon delete
- **I:** Delete file đính kèm thành công
- **L:** PASS

### Row 113

- **A:** High
- **D:** Kiểm tra chức năng phân trang danh dách item
- **K:** Chờ fix Bug 52647
- **L:** STUCK

### Row 114

- **A:** High
- **B:** 0.2
- **C:** PO có <= 100 item
- **E:** PAGI_UI_001: Kiểm tra UI khi số lượng item nhỏ hơn giới hạn phân trang
- **F:** Pagination: Hidden (khi số lượng item <= 100)
- **G:** 1. Thêm 50 item vào PO. <br>2. Quan sát khu vực dưới cùng của bảng Order Items.
- **H:** Hiển thị thông tin "Showing 50 of 50 results"
- **I:** N/A
- **L:** PENDING

### Row 115

- **A:** High
- **B:** 0.3
- **C:** PO có > 100 item (ví dụ 105 item)
- **E:** PAGI_FUNC_002: Kiểm tra UI và chức năng phân trang mặc định
- **F:** Fixed 100 results per page. Format show: Select all Y orders Showing X of Y results >
- **G:** 1. Thêm 105 item vào PO. <br>2. Quan sát khu vực phân trang.
- **H:** 1. Thanh phân trang hiển thị. <br>2. Trang 1 hiển thị 100 item. Text hiển thị: "Showing 100 of 105 results" (hoặc format tương đương).
- **I:** BE trả về 100 item đầu tiên.
- **L:** PENDING

### Row 116

- **A:** High
- **B:** 0.3
- **C:** PO có > 100 item (105 item), đang ở trang 1
- **E:** PAGI_FUNC_003: Kiểm tra chuyển trang (Next Page)
- **G:** 1. Click vào nút chuyển trang (>) để sang trang 2. <br>2. Quan sát số lượng item hiển thị.
- **H:** Trang 2 hiển thị 5 item. Text hiển thị: "Showing 5 of 105 results" (hoặc tương đương).
- **I:** BE trả về 5 item còn lại.
- **L:** PENDING

### Row 117

- **A:** High
- **B:** 0.4
- **C:** PO có > 100 item, đang ở trang 2
- **E:** Kiểm tra chức năng có thể chọn tất cả item trên tất cả các trang.
- **G:** 1. Chọn checkbox ở header bảng (trên trang 2). <br>2. Quan sát text hiển thị. <br>3. Click vào "Select all Y orders".
- **H:** 1. Bước 2: Text hiển thị "X selected. Select all 105 orders" (X là số item trên trang 2, vd: 5). <br>2. Bước 3: Text hiển thị: "All 105 results are selected. Clear selection."
- **I:** N/A
- **L:** PENDING

### Row 118

- **A:** High
- **B:** 0.4
- **C:** Đang ở trạng thái "All Y results are selected"
- **E:** Kiểm tra chức năng hủy chọn tất cả item và quay lại trạng thái mặc định.
- **G:** 1. Click vào "Clear selection".
- **H:** Hủy chọn tất cả 105 item. Checkbox ở header bảng bỏ chọn. Text quay lại trạng thái mặc định: "Showing X of Y results".
- **I:** N/A
- **L:** PENDING

### Row 119

- **D:** Kiểm tra popup Add item

### Row 120

- **A:** High
- **B:** 0.2
- **C:** Pop-up đang mở
- **E:** UI_ADD_001: Kiểm tra UI và các cột hiển thị mặc định
- **F:** Xác nhận tiêu đề pop-up và các cột dữ liệu hiển thị đúng.
- **G:** 1. Mở pop-up "Add item" (Click nút Add item). <br>2. Quan sát tiêu đề và các cột.
- **H:** 1. Tiêu đề hiển thị: "Add item". <br>2. Các cột hiển thị: Title, SKU, UOM, Type, On hand qty.
- **I:** N/A
- **L:** FAILED

### Row 121

- **A:** High
- **B:** 0.3
- **C:** Pop-up đang mở
- **E:** FUNC_SEARCH_002: Tìm kiếm hợp lệ bằng Title (Fuzzy Search)
- **F:** Xác nhận chức năng tìm kiếm item bằng Title hoạt động theo luật tìm kiếm chung (GR02).
- **G:** 1. Nhập một phần Title của item (ví dụ: "Petite") vào thanh tìm kiếm.
- **H:** Hệ thống hiển thị tất cả các item có Title chứa từ khóa "Petite" (ví dụ: "Petite Crescent White").
- **I:** BE trả về danh sách item khớp với tìm kiếm fuzzy theo Title.
- **L:** PASS

### Row 122

- **A:** High
- **B:** 0.3
- **C:** Pop-up đang mở
- **E:** FUNC_SEARCH_003: Tìm kiếm hợp lệ bằng SKU (Fuzzy Search)
- **F:** Xác nhận chức năng tìm kiếm item bằng SKU hoạt động theo luật tìm kiếm chung (GR02).
- **G:** 1. Nhập một phần SKU của item (ví dụ: "R6000") vào thanh tìm kiếm.
- **H:** Hệ thống hiển thị tất cả các item có SKU chứa từ khóa "R6000".
- **I:** BE trả về danh sách item khớp với tìm kiếm fuzzy theo SKU.
- **L:** PASS

### Row 123

- **A:** High
- **B:** 0.3
- **C:** N/A
- **E:** tìm kiếm item không trả về kết quả.
- **F:** When no result is matched to searching value, show message like this: [No Data Found Image].
- **G:** 1. Nhập từ khóa không tồn tại (ví dụ: "XYZ123") vào thanh tìm kiếm.
- **H:** Hệ thống hiển thị hình ảnh "No items available".
- **I:** BE trả về danh sách rỗng.
- **K:** Pass trả về danh sách rỗng<br>Nội dung thông báo hiển thị tương tự như ở màn hình TO
- **L:** PASS

### Row 124

- **A:** Medium
- **B:** 0.2
- **C:** Pop-up đang mở
- **E:** FUNC_SORT_004: Kiểm tra sắp xếp item mặc định
- **F:** Xác nhận item được sắp xếp theo Title từ A → Z.
- **G:** 1. Quan sát danh sách item khi pop-up vừa mở.
- **H:** Danh sách item phải được sắp xếp theo Title (tên item) từ A → Z.
- **I:** BE trả về dữ liệu đã sắp xếp.
- **K:** Bug 52615
- **L:** FAILED

### Row 125

- **A:** High
- **B:** 0.4
- **C:** Item tồn tại trong hệ thống
- **E:** FUNC_ADD_005: Thêm một Item hợp lệ vào PO
- **F:** Kiểm tra chức năng thêm item thành công sau khi chọn.
- **G:** 1. Chọn 1 item (đánh dấu checkbox). <br>2. Quan sát số lượng selected. <br>3. Click nút "Add".
- **H:** Bước 2: Text hiển thị "1 selected". Bước 3: Pop-up đóng lại, item đã chọn được thêm vào bảng Order Items của PO.
- **L:** PASS

### Row 126

- **A:** High
- **B:** 0.4
- **C:** Item tồn tại trong hệ thống
- **E:** FUNC_ADD_006: Thêm nhiều Items hợp lệ vào PO
- **F:** Kiểm tra chức năng thêm nhiều item thành công.
- **G:** 1. Chọn ngẫu nhiên 5 item khác nhau (Variant và Component). <br>2. Quan sát số lượng selected (ví dụ: 5 selected). <br>3. Click nút "Add".
- **H:** Pop-up đóng lại, 5 item đã chọn được thêm vào bảng Order Items của PO.
- **L:** PASS

### Row 127

- **A:** High
- **B:** 0.3
- **C:** N/A
- **E:** FUNC_CANCEL_007: Hủy bỏ thao tác "Add item"
- **F:** Kiểm tra chức năng Cancel hoặc Close pop-up.
- **G:** 1. Chọn một vài item (ví dụ 2 item). <br>2. Click nút "Cancel" hoặc nút "X" ở góc trên bên phải.
- **H:** Pop-up đóng lại. Các item đã chọn không được thêm vào bảng Order Items.
- **L:** PASS

### Row 128

- **A:** Medium
- **B:** 0.3
- **C:** Pop-up có > 100 kết quả
- **E:** PAGI_ITEM_009: Kiểm tra chức năng Load More/Pagination
- **F:** Showing X of Y results. Load next Z → Load thêm 100
- **G:** 1. Danh sách hiển thị >100 results<br>2. Quan sát khu vực phân trang. <br>3. Click nút icon >
- **H:** Bước 2: Text hiển thị: "Showing x of <total item> results.<br>Bước 3: Tổng số item hiển thị tăng lên<br>Text hiển thị: "Showing <total item> of <total item> results".
- **I:** BE trả về dữ liệu tiếp theo.
- **K:** Bug 52647
- **L:** FAILED

### Row 129

- **A:** Medium
- **B:** 0.2
- **C:** Pop-up đang mở
- **E:** UI_FIELD_010: Kiểm tra Item Type và UOM hiển thị
- **F:** Xác nhận Item Type hiển thị Variant/Component và UOM của Variant hiển thị là "-" nếu không có data
- **G:** 1. Quan sát cột Type và UOM của các dòng Item.
- **H:** Cột Type hiển thị: "Variant" hoặc "Component". Cột UOM của item Variant hiển thị: "-" nếu không có data
- **I:** N/A
- **K:** Chỉ mới kiểm tra type=variant
- **L:** PASS

### Row 130

- **A:** Medium
- **B:** 0.2
- **C:** PO có > 100 item
- **D:** PAGI_UI_007: Kiểm tra cố định cột 'Title' khi cuộn ngang
- **E:** Đảm bảo cột Title (Item line) được giữ cố định khi người dùng cuộn ngang để xem các cột khác.
- **F:** Note: The user can scroll horizontally to view all columns, but the 'Title' column is fixed.
- **G:** 1. Cuộn ngang bảng Order Items.
- **H:** Cột Title (bao gồm tên item và SKU) phải được giữ cố định, các cột khác cuộn theo.
- **I:** N/A
- **K:** Màn hình TO vẫn không cố định -> xem sau
- **L:** N/A

### Row 131

- **A:** Medium
- **B:** 0.3
- **C:** Đã chỉnh sửa dữ liệu trên trang
- **D:** BR_AF_002: Cảnh báo khi thoát trang có dữ liệu chưa lưu (Cancel/Back)
- **E:** Kiểm tra BR01: Hiển thị popup cảnh báo khi người dùng cố gắng thoát trang mà chưa lưu thay đổi.
- **F:** Case 1: When the user has edited the PO and attempts to exit the page, the system will display the message log M07..
- **H:** 1. Thay đổi Order Qty. <br>2. Click "Cancel" hoặc nút Back trên trình duyệt.
- **I:** System hiển thị Pop-up confirm (M07): "You have not saved all changes... Do you still want to continue closing this PO without saving?"
- **J:** N/A
- **K:** Đã hiển thị popup nhưng wording khác -> Đang lấy nội dung giống TO -> xem lại sau
- **L:** PASS

### Row 132

- **A:** Medium
- **B:** 0.2
- **C:** Chưa chỉnh sửa dữ liệu trên trang
- **D:** BR_AF_003: Thoát trang khi không có dữ liệu thay đổi
- **E:** Kiểm tra BR01: Không hiển thị popup cảnh báo khi thoát trang mà không có thay đổi.
- **F:** Case 2: When the user has not edited the PO, the system allows closing the PO without displaying a confirmation pop-up..
- **H:** 1. Truy cập trang Create PO. <br>2. Click "Cancel" ngay lập tức.
- **I:** Trang PO list được hiển thị mà không có pop-up nào.
- **J:** N/A
- **L:** PASS

### Row 133

- **A:** Medium
- **B:** 0.2
- **C:** Đã điền 1 vài field
- **D:** EDGE_003: Kiểm tra Data Persistence khi Refresh trang
- **E:** Đảm bảo dữ liệu người dùng nhập không bị mất khi Refresh trang.
- **F:** BR01: Khi đã edit và cố gắng thoát trang sẽ hiển thị M07.
- **H:** 1. Nhập PO Number, Vendor, và Order Qty cho 1 item. <br>2. Nhấn F5 (Refresh trình duyệt).
- **I:** Hệ thống hiển thị Pop-up cảnh báo (M07). Nếu chọn Cancel, dữ liệu vẫn còn. Nếu chọn Leave, trang được làm mới và dữ liệu bị mất.
- **J:** N/A

### Row 134

- **A:** Medium
- **B:** 0.2
- **C:** N/A
- **D:** EDGE_004: Kiểm tra Tab Order
- **E:** Đảm bảo thứ tự Tab (phím) di chuyển giữa các trường nhập liệu là hợp lý.
- **F:** N/A
- **H:** 1. Bắt đầu từ trường PO Number. <br>2. Nhấn phím "Tab" liên tục.
- **I:** Con trỏ di chuyển theo thứ tự logic giữa các trường input.
- **J:** N/A

### Row 135

- **A:** Tạo mới PO khi apply MOQ
- **K:** Chờ dev làm
- **L:** PENDING

### Row 136

- **D:** Kiểm tra UI Create PO

### Row 137

- **A:** High
- **B:** 0.1
- **C:** N/A
- **E:** Kiểm tra Wording và Required Fields cho các trường bắt buộc ở phần Header.
- **F:** PO Number, Supplier, Warehouse, Expected Arrival Date: Required
- **H:** 1. Quan sát các trường PO Number, Supplier, Warehouse, Expected Arrival Date.
- **I:** Nhãn hiển thị: "PO Number*", "Supplier*", "Warehouse*", "Expected arrival date*".
- **J:** N/A

### Row 138

- **A:** Medium
- **B:** 0.1
- **C:** N/A
- **E:** Kiểm tra UI và nhãn của các trường trong PO Summary.
- **F:** Chỉ hiển thị khi có setting PO MOQ level ở supplier
- **H:** 1. Chọn Supplier có cấu hình PO MOQ Level. <br>2. Quan sát mục PO Summary.
- **I:** Hiển thị: "Total Ordered", "Purchase Order MOQ", "% Achieved".
- **J:** N/A

### Row 139

- **A:** Medium
- **B:** 0.1
- **C:** N/A
- **E:** Kiểm tra Header Table UI của các cột trong bảng Order Items (tiêu đề viết hoa chữ cái đầu - GR04 ).
- **H:** 1. Quan sát tiêu đề các cột trong bảng Order Items.
- **I:** Các cột phải có: TITLE, ON HAND, MOQ, ORDER QTY, RECEIVED QTY, UOM, PRODUCTION START DATE, ESTIMATED COMPLETION, COMPLETION DATE, COST, TOTAL COST, ACTION.
- **J:** N/A

### Row 140

- **A:** High
- **B:** 0.2
- **C:** N/A
- **E:** Kiểm tra Wording và Trạng thái của các nút Action Footer
- **F:** Cancel, Save as draft, Request approval, Issue PO
- **H:** 1. Quan sát các nút hành động ở cuối trang.
- **I:** Các nút phải có wording: "Back", "Save as draft", "Request approval", "Issue PO". Tất cả các nút đều phải Disable nếu chưa nhập thông tin require.
- **J:** N/A

### Row 141

- **A:** Medium
- **B:** 0.1
- **C:** N/A
- **E:** Kiểm tra UI và nhãn của các trường trong Style Summary.
- **F:** Chỉ hiển thị khi có config Style level ở supplier này
- **H:** 1. Chọn Supplier có cấu hình Style MOQ Level. <br>2. Quan sát mục Style Summary.
- **I:** Hiển thị bảng với các cột: STYLE NAME, MOQ (STYLE), ORDERED QTY, % ARCHIVED.
- **J:** N/A

### Row 142

- **A:** Medium
- **B:** 0.1
- **C:** N/A
- **E:** Kiểm tra Note for PO & Attachments UI
- **F:** 1. Note for PO: Optional. <br>2. Attachments: Format .xls, .xlsx, .pdf, .csv, .doc, .docx.
- **I:** 1. Nhãn: "Note for PO". <br>2. Khu vực Attachments hiển thị hướng dẫn tải file.
- **J:** N/A

### Row 143

- **D:** Kiểm tra Pop-up "Add Item" UI
- **G:** 1. Click nút "+ Add Item". <br>2. Quan sát pop-up.
- **I:** Kiểm tra UI hiển thị đúng so với design

### Row 144

- **A:** High
- **B:** 0.5
- **C:** Supplier (A) Active, có Lead Time = 10 ngày, có Linked Variants (X).
- **D:** Tự động Load Dữ liệu Supplier (Lead Time, Linked Variants)
- **E:** Kiểm tra BR04 (SRS_Supplier ) và BR01 (SRS_Supplier ) về việc tự động load dữ liệu.
- **F:** Expected Arrival Date = Today + Lead Time. Chỉ hiển thị Linked Variants.
- **G:** 1. Chọn Supplier (A). <br>2. Quan sát Expected Arrival Date. <br>3. Click + Add Item và quan sát danh sách variants.
- **H:** Bước 2: Expected Arrival Date = Today + 10<br>Bước 3: Danh sách variants trong pop-up chỉ hiển thị các Linked Variants (X) của Supplier (A). Thông tin MOQ hiển thị đúng so với page supplier
- **I:** BE trả về Lead Time và Linked Variants.
- **L:** FAILED

### Row 145

- **A:** High
- **B:** 0.4
- **C:** Supplier (A) có cấu hình Style MOQ Level (Style 1: MOQ=1000).
- **D:** Kiểm tra logic Style Summary (BR02)
- **E:** Xác nhận Style Summary hiển thị và tính toán chính xác.
- **G:** 1. Chọn Supplier (A). <br>2. Add 2 variants thuộc Style 1. <br>3. Nhập Order Qty: 600 và 300 (Total = 900).
- **H:** Mục Style Summary hiển thị <br>+ Style name = 1 với Ordered Qty = 900, MOQ = 1000 và % Achieved = 90%.
- **I:** Tính toán % Achieved phải chính xác.

### Row 146

- **A:** High
- **B:** 0.4
- **C:** Supplier (C) có cấu hình PO MOQ Level = 5000.
- **D:** FUNC_MOQ_011: Kiểm tra logic PO Summary (BR02)
- **E:** Xác nhận PO Summary hiển thị và tính toán chính xác.
- **F:** Total Ordered ≥ MOQ PO.
- **G:** 1. Chọn Supplier (C). <br>2. Add item và nhập Ordered (Total = 4850).
- **H:** Mục PO Summary hiển thị Purchase Order MOQ = 5,000, Total Ordered = 4,850, % Achieved = 97.0%.
- **I:** Tính toán % Achieved phải chính xác.

### Row 147

- **D:** Tạo PO thành công khi apply MOQ

### Row 148

- **A:** High
- **B:** 0.5
- **C:** Supplier (A) Active, có Lead Time = 10 ngày, có Linked Variants (X).
- **E:** FUNC_MAIN_012.1: Tạo PO thành công với Status "Open" và supplier có linked với variant
- **F:** Issue PO → trạng thái “Open”.
- **G:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Issue PO".
- **H:** 1. System hiển thị toast message: "Purchase order created successfully" (M10). User được redirect về trang PO list. PO mới tạo có Status: Open.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **I:** 1. PO được tạo với Status = Open. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **L:** PASS

### Row 149

- **G:** Chọn item không link với supplier
- **I:** item tự động linked với supplier
- **L:** PASS

### Row 150

- **G:** Chọn item không link với supplier nhưng có nằm trong group style MOQ
- **L:** FAILED

### Row 151

- **G:** Chọn item link với variant nhưng không nằm trong config style MOQ
- **L:** PASS

### Row 152

- **G:** Chọn item link với variant và nằm trong config style MOQ
- **L:** PASS

### Row 153

- **E:** Tạo PO thành công với Status "Draft" và không add item
- **L:** PASS

### Row 154

- **A:** High
- **B:** 0.5
- **C:** Supplier (A) có cấu hình Style MOQ Level (Style 1: MOQ=1000).
- **E:** FUNC_MAIN_012.2: Tạo PO thành công với Status "Draft" và supplier có cấu hình Style MOQ Level
- **F:** Issue PO → trạng thái “Draft”.
- **G:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Save as draft".
- **H:** 1. System hiển thị toast message: "Purchase order saved as draft successfully.". User được redirect về trang PO list. PO mới tạo có Status: Draft.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **I:** 1. PO được tạo với Status = Draft. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **L:** PASS

### Row 155

- **A:** High
- **C:** Supplier (C) có cấu hình PO MOQ Level = 5000.
- **E:** FUNC_MAIN_012.3: Tạo PO thành công với Status "Pending Approval" và supplier có cấu hình PO MOQ
- **F:** Issue PO → trạng thái “Pending Approval”.
- **G:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Request approval".
- **H:** 1. System hiển thị toast message: "Purchase Order submitted for approval successfully.". User được redirect về trang PO list. PO mới tạo có Status: Pending Approval.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **I:** 1. PO được tạo với Status = Pending Approval. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 156

- **A:** High
- **B:** 0.5
- **C:** 1. Supplier (A) Active, có Lead Time = 10 ngày, có Linked Variants (X).<br>2. Supplier (A) có cấu hình Style MOQ Level (Style 1: MOQ=1000).<br>3. Supplier (A) có cấu hình PO MOQ Level = 5000.
- **E:** FUNC_MAIN_012.1: Tạo PO thành công với Status "Open" và supplier có linked với variant, có cấu hình style MOQ và PO MOQ
- **F:** Issue PO → trạng thái “Open”.
- **G:** 1. Nhập PO number hợp lệ. <br>2. Chọn Supplier và Warehouse. <br>3. Chọn Expected arrival date (trong tương lai). <br>4. Click "Add item", chọn 1 item, Order Qty > 0, nhập Cost > 0. <br>5. Click "Issue PO".
- **H:** 1. System hiển thị toast message: "Purchase order created successfully" (M10). User được redirect về trang PO list. PO mới tạo có Status: Open.<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng
- **I:** 1. PO được tạo với Status = Open. PO ID được generate (Cxxxxx).<br>2. Kiểm tra thông tin trong PO detail hiển thị đúng

### Row 157

- **D:** Kiểm tra tạo PO thất bại

### Row 158

- **E:** Kiểm tra field require

### Row 159

- **A:** High
- **B:** 0.2
- **F:** Thiếu trường bắt buộc PO Number
- **G:** Kiểm tra trường PO Number bị bỏ trống.
- **H:** 1. Bỏ trống PO Number. <br>2. Điền đủ các trường bắt buộc khác (Supplier, Warehouse, Expected arrival date, Items). <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường PO number: "The field is required" (M04).
- **J:** PO không được tạo.

### Row 160

- **A:** High
- **B:** 0.2
- **F:** Thiếu trường bắt buộc Supplier
- **G:** Kiểm tra các trường Single Selection bắt buộc bị bỏ trống.
- **H:** 1. Bỏ trống Supplier. <br>2. Điền đủ các trường bắt buộc còn lại. <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường bị thiếu: "The field is required" (M04).
- **J:** PO không được tạo.

### Row 161

- **A:** High
- **B:** 0.2
- **F:** VAL_HEADER_005: Thiếu trường bắt buộc Warehouse
- **G:** Kiểm tra các trường Single Selection bắt buộc bị bỏ trống.
- **H:** 1. Bỏ trống Warehouse<br>2. Điền đủ các trường bắt buộc còn lại. <br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường bị thiếu: "The field is required" (M04).
- **J:** PO không được tạo.

### Row 162

- **A:** High
- **B:** 0.2
- **F:** Thiếu trường bắt buộc Expected arrival date
- **G:** Kiểm tra trường Expected arrival date bị bỏ trống.
- **H:** 1. Bỏ trống Expected arrival date<br>2. Điền đủ các trường bắt buộc khác<br>3. Click "Issue PO".
- **I:** System hiển thị in-line error message dưới trường PO number: "The field is required" (M04).
- **J:** PO không được tạo.

### Row 163

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** Thiếu trường bắt buộc (Order Qty)
- **G:** Kiểm tra Order Qty bị bỏ trống.
- **H:** 1. Add item. <br>2. Bỏ trống Order Qty. <br>3. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Order Qty: "The field is required" (M04).
- **J:** Tạo PO không thành công

### Row 164

- **A:** High
- **B:** 0.2
- **C:** Đã thêm item
- **F:** Thiếu trường bắt buộc (Cost)
- **G:** Kiểm tra Cost bị bỏ trống.
- **H:** 1. Add item. <br>2. Bỏ trống Cost. <br>3. Click ra khỏi field.
- **I:** System hiển thị in-line error message dưới trường Cost: "The field is required" (M04).
- **J:** Tạo PO không thành công

### Row 165

- **A:** High
- **B:** 0.3
- **C:** Supplier (D) Active, nhưng chưa có Linked Variants.
- **F:** Cảnh báo khi Supplier không có Linked Variants
- **H:** 1. Chọn Supplier (D). <br>2. Click "+ Add Item".
- **I:** 1. Pop-up Add Item không hiển thị danh sách variants. <br>2. System hiển thị cảnh báo (toast/modal) "No variants found for this supplier. Please link variants in Supplier Profile."

### Row 166

- **A:** High
- **B:** 0.3
- **C:** Pop-up "Add Item" đang mở
- **D:** SCENARIO_019: Tìm kiếm hợp lệ bằng Style (Pop-up Add Item)
- **E:** Xác nhận tìm kiếm item bằng Style Name hoạt động.
- **F:** Tìm kiếm theo Product name, Style, SKU.
- **G:** 1. Click + Add Item. <br>2. Nhập tên Style (ví dụ: "Petite Crescent Collection").
- **H:** Pop-up hiển thị danh sách variants thuộc Style đã tìm kiếm.
- **I:** BE trả về variants khớp với tìm kiếm Style Name.

### Row 167

- **A:** High
- **B:** 0.4
- **C:** Pop-up có > 100 item
- **D:** SCENARIO_020: Kiểm tra Phân trang/Load More trong Pop-up Add Item
- **G:** 1. Mở Pop-up Add Item (có 100 results). <br>2. Quan sát số lượng kết quả hiển thị. <br>3. Click icon >
- **H:** Bước 2: Hiển thị "Showing 100 of <total item> results" <br>Bước 3: Danh sách hiển thị tăng lên.
- **I:** BE trả về dữ liệu theo pagination.

### Row 168

- **A:** High
- **B:** 0.4
- **C:** Đã thêm item
- **D:** Kiểm tra chức năng xóa item và đảm bảo các trường Summary được tính lại.
- **F:** Total Cost, Total Ordered tự cập nhật mỗi khi thay đổi item.
- **G:** 1. Add 2 items (A: Qty=100, Cost=10; B: Qty=50, Cost=5). <br>2. Quan sát Total Cost (150) và Total Ordered (15). <br>3. Click icon xóa (thùng rác) Item B.
- **H:** Bước 3: Item B biến mất. <br>Total Cost cập nhật thành 10. <br>Total Ordered cập nhật thành 100.
- **I:** BE loại bỏ item B và cập nhật total.

### Row 169

- **A:** Medium
- **B:** 0.3
- **C:** Item có MOQ/Cost
- **D:** SCENARIO_022: Kiểm tra Read-only của các trường tự động điền (MOQ, Cost)
- **E:** Đảm bảo các trường MOQ tự động điền không thể chỉnh sửa thủ công trừ Order Qty,Cost.
- **F:** Order Qty là Input, Cost/MOQ là Number (tự động load).
- **G:** 1. Add item có MOQ, Cost. <br>2. Thử nhập vào các trường MOQ, Cost (trên bảng Order Items).
- **H:** Trường Order Qty,Cost cho phép nhập. <br>Các trường MOQ không cho phép nhập liệu trực tiếp (read-only/disabled) trên bảng Order Items.
- **I:** N/A
- **L:** FAILED

### Row 170

- **A:** View  PO detail

### Row 171

- **A:** High
- **D:** Kiểm tra UI hiển thị đúng so với design

### Row 172

- **A:** High
- **E:** Kiểm tra UI của PO có status là Draft
- **L:** PASS

### Row 173

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Pending approval
- **K:** Bug 52643
- **L:** FAILED

### Row 174

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Reject
- **K:** Bug 52643
- **L:** FAILED

### Row 175

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Open
- **K:** Chờ dev thêm cột received
- **L:** PENDING

### Row 176

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Partially fulfilled
- **K:** Chờ dev fix bug 52627
- **L:** PENDING

### Row 177

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Fulfilled
- **K:** Chờ dev fix bug 52627
- **L:** PENDING

### Row 178

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Closed
- **K:** Chờ dev fix bug 52627
- **L:** PENDING

### Row 179

- **A:** High
- **E:** Kiểm tra UI đối với PO có status là Cancelled
- **K:** Không có UI
- **L:** N/A

### Row 180

- **A:** Medium
- **E:** Kiểm tra UI History log sau khi thực hiện edit PO
- **K:** Dev chưa làm
- **L:** PENDING

### Row 181

- **A:** High
- **E:** Kiểm tra chỉ enable button Save khi có thực hiện edit
- **L:** PASS

### Row 182

- **D:** Kiểm tra function

### Row 183

- **A:** High
- **E:** Search order item thành công
- **K:** Chờ fix bug 52645 rồi kiểm tra lại
- **L:** FAILED

### Row 184

- **A:** High
- **F:** Tìm kiếm matching by title variant/ title component
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị item có title trùng với từ khóa<br> + Số lượng item trùng với danh sách item
- **K:** pass variant
- **L:** PASS

### Row 185

- **A:** High
- **F:** Tìm kiếm matching by SKU
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị item có SKU trùng với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** PASS

### Row 186

- **A:** High
- **F:** Tìm kiếm matching by ASIN
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị item có ASIN trùng với từ khóa<br> + Số lượng item trùng với danh sách item

### Row 187

- **A:** High
- **F:** Tìm kiếm contains từ khóa so với title
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị những item có title chứa từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** PASS

### Row 188

- **A:** High
- **F:** Tìm kiếm không phân biệt chữ hoa / chữ thường
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị những item có title chứa với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 189

- **A:** High
- **F:** Tìm kiếm chứa warehouseảng trắng trước / sau
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị những item có title chứa với từ khóa<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 190

- **A:** High
- **F:** Tìm kiếm chứa warehouseảng trắng
- **I:** 1. Add 1 item. <br>2. Nhập từ khóa tìm kiếm
- **J:** Hiển thị tất cả item<br> + Số lượng item trùng với danh sách item
- **L:** STUCK

### Row 191

- **A:** High
- **E:** Download CSV
- **K:** Bug 52640
- **L:** FAILED

### Row 192

- **A:** High
- **E:** Dowload PDF
- **K:** Bug 52640
- **L:** FAILED

### Row 193

- **A:** High
- **E:** Chọn button Close để đóng màn hình PO detail
- **K:** Sai wording button
- **L:** FAILED

### Row 194

- **A:** High
- **E:** Phân trang thành công
- **K:** Chờ fix Bug 52647
- **L:** STUCK

### Row 195

- **A:** Edit  PO

### Row 196

- **D:** Update thông tin PO có status là Draft

### Row 197

- **E:** > PO number

### Row 198

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update PO number thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Bug 52650
- **L:** FAILED

### Row 199

- **A:** Medium
- **F:** Xóa data PO number
- **I:** Show error message under the field is The field is required
- **L:** FAILED

### Row 200

- **A:** Medium
- **G:** Không cho phép  nhập ký tự đặc biệt
- **I:** show mess: This PO number is not valid

### Row 201

- **A:** Medium
- **G:** case bổ sung- không cho nhập warehouseảng trống<br>-> show mess: This PO number is not valid
- **I:** Không cho phép nhập warehouseảng trắng
- **L:** PASS

### Row 202

- **A:** Medium
- **F:** Update không thành công khi nhập data > 50 kí tư
- **I:** Show error message under the field “This PO ID is not over 50 characters”

### Row 203

- **A:** High
- **E:** > Supplier
- **I:** 1/ Update Supplier thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Update thành công
- **L:** PASS

### Row 204

- **A:** High
- **E:** > Warehouse
- **I:** 1/ Update Warehouse thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Update thành công<br>Kiểm tra thêm case thay đổi on hand trong popup add item sau khi dev fix bug 52598
- **L:** FAILED

### Row 205

- **E:** > Expected arrival date

### Row 206

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update Expected arrival date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Update thành công
- **L:** PASS

### Row 207

- **A:** High
- **F:** Không thể chọn Expected arrival date < {Today date}
- **I:** mess: Expected day should not be in the past
- **L:** FAILED

### Row 208

- **A:** Medium
- **F:** Kiểm tra giờ FE truyền xuống cho  BE lưu
- **I:** Mặc định sẽ lấy  0h ngày dc chọn trên FE đem đi trừ lùi lại theo múi giờ local của máy để ghi nhận giờ
- **K:** Bug 52655
- **L:** FAILED

### Row 209

- **A:** High
- **E:** > Add item
- **I:** 1/ Add item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 210

- **F:** Add variant
- **L:** PASS

### Row 211

- **A:** High
- **F:** > Active

### Row 212

- **A:** Medium
- **F:** > Archive

### Row 213

- **A:** Medium
- **F:** > Draft

### Row 214

- **A:** High
- **F:** Add component

### Row 215

- **E:** > Remove item
- **L:** PASS

### Row 216

- **A:** High
- **F:** Remove tất cả item thành công
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Chờ fix bug
- **L:** PASS

### Row 217

- **A:** Medium
- **F:** Remove khi chọn icon delete 1 variant trên order line item
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 218

- **G:** Remove variant
- **L:** PASS

### Row 219

- **A:** Medium
- **G:** > Active

### Row 220

- **A:** Medium
- **G:** > Archive

### Row 221

- **A:** Medium
- **G:** > Draft

### Row 222

- **A:** Medium
- **G:** Remove component

### Row 223

- **A:** Medium
- **F:** Remove khi select nhiều variant và chọn button Remove
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order updated successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 224

- **G:** Remove variant
- **L:** PASS

### Row 225

- **A:** Medium
- **G:** > Active

### Row 226

- **A:** Medium
- **G:** > Archive

### Row 227

- **A:** Medium
- **G:** > Draft

### Row 228

- **A:** Medium
- **G:** Remove component

### Row 229

- **E:** > Order Qty trong Order item

### Row 230

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update order quantity thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 231

- **A:** Medium
- **F:** Nhập data = 0
- **I:** Show error message under the field is "Quantity must be greater than 0."
- **K:** sai nội dung thông báo
- **L:** FAILED

### Row 232

- **A:** Medium
- **F:** bổ sung: nhập số thập phân
- **I:** không thể nhập
- **L:** FAILED

### Row 233

- **F:** Xóa data và để data = null
- **G:** case này không xảy ra- vì xóa data thì UI default về 0
- **I:** Show error message under the field is "The field is required"

### Row 234

- **A:** High
- **E:** > Production start date trong Order item
- **I:** 1/ Update Production start date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 235

- **A:** High
- **E:** > Estimated completion trong Order item
- **I:** 1/ Update Estimated completion thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 236

- **A:** High
- **E:** > Completion date trong Order item
- **I:** 1/ Update Completion date  thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 237

- **E:** > Cost trong Order item

### Row 238

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update cost thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 239

- **G:** Update cost nếu order item đang có data cost

### Row 240

- **G:** Update cost nếu order item đang không có data cost (null)
- **L:** PASS

### Row 241

- **F:** Xóa data và để data = null
- **I:** Show error message under the field is "The field is required"

### Row 242

- **A:** Medium
- **F:** Chỉ được nhập cost >= 0 và cho nhập số thập phân
- **L:** PASS

### Row 243

- **A:** Medium
- **F:** Nhập quá 131072 trước chữ số thập phân và quá 16383 sau chữ số thập phân
- **I:** Show error message under the field is Please limit the integer part to 131072 digits and the decimal part to 16383 digits.

### Row 244

- **A:** High
- **E:** > Note for PO

### Row 245

- **A:** High
- **F:** Update thành data khác khi đang có data note
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 246

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 247

- **E:** > Attachments
- **L:** FAILED

### Row 248

- **A:** High
- **F:** Update file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 249

- **A:** Medium
- **F:** Không thể chọn format khác với .xls, .xlsx, .pdf, .csv, .doc, .docx
- **I:** Hiển thị message: Invalid file format.

### Row 250

- **A:** Medium
- **F:** Update file > 5MB
- **I:** Error message in the popup “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

### Row 251

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 252

- **E:** Kiểm tra back về màn hình PO list thành công

### Row 253

- **F:** Nếu chưa edit mà bấm Close
- **I:** Đóng popup Edit và back về màn hình PO list
- **L:** PASS

### Row 254

- **F:** Nếu đã edit mà bấm Close
- **I:** Hiển thị popup Confirm
- **L:** PASS

### Row 255

- **D:** Update thông tin PO có status là Pending approval

### Row 256

- **E:** > PO number

### Row 257

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update PO number thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 258

- **A:** Medium
- **F:** Xóa data PO number
- **I:** Show error message under the field is The field is required
- **L:** PASS

### Row 259

- **A:** Medium
- **G:** case bổ sung- không cho nhập ký tự đặc biệt- copy rule ở PO cũ<br>-> show mess: This PO number is not valid

### Row 260

- **A:** Medium
- **G:** case bổ sung- không cho nhập warehouseảng trống<br>-> show mess: This PO number is not valid

### Row 261

- **A:** Medium
- **F:** Update không thành công khi nhập data > 50 kí tư
- **I:** Show error message under the field “This PO ID is not over 50 characters”

### Row 262

- **E:** > Supplier
- **I:** Không cho edit
- **L:** PASS

### Row 263

- **E:** > Warehouse
- **I:** 1/ Update Warehouse thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Bug 52661
- **L:** FAILED

### Row 264

- **E:** > Expected arrival date

### Row 265

- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update Expected arrival date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 266

- **F:** Không thể chọn Expected arrival date < {Today date}
- **I:** mess: Expected day should not be in the past
- **L:** FAILED

### Row 267

- **A:** High
- **E:** > Add item
- **I:** 1/ Add item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 268

- **F:** Add variant
- **L:** PASS

### Row 269

- **A:** High
- **F:** > Active

### Row 270

- **A:** Medium
- **F:** > Archive

### Row 271

- **A:** Medium
- **F:** > Draft

### Row 272

- **A:** High
- **F:** Add component

### Row 273

- **E:** > Remove item

### Row 274

- **A:** High
- **F:** Remove khi chọn icon delete 1 variant trên order line item
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 275

- **G:** Remove variant

### Row 276

- **A:** High
- **G:** > Active

### Row 277

- **A:** Medium
- **G:** > Archive

### Row 278

- **A:** Medium
- **G:** > Draft

### Row 279

- **A:** High
- **G:** Remove component

### Row 280

- **A:** Medium
- **F:** Remove khi select nhiều variant và chọn button Remove
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 281

- **A:** Medium
- **G:** Remove variant

### Row 282

- **A:** Medium
- **G:** > Active

### Row 283

- **A:** Medium
- **G:** > Archive

### Row 284

- **A:** Medium
- **G:** > Draft

### Row 285

- **A:** Medium
- **G:** Remove component

### Row 286

- **A:** High
- **F:** Không cho Remove hết item
- **I:** Disable các button
- **L:** FAILED

### Row 287

- **A:** High
- **G:** Remove 1 item
- **I:** hide icon delete cho line cuối cùng đi
- **L:** FAILED

### Row 288

- **A:** High
- **G:** Remove nhiều item
- **I:** show toast mess: "This PO does not contain any items. Please add items before issuing."
- **L:** FAILED

### Row 289

- **E:** > Order Qty trong Order item

### Row 290

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update order quantity thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 291

- **A:** Medium
- **F:** Nhập data = 0
- **I:** Show error message under the field is "Quantity must be greater than 0."
- **K:** Hiển thị sai nội dung thông báo
- **L:** FAILED

### Row 292

- **A:** Medium
- **F:** bổ sung: nhập số thập phân
- **I:** không thể nhập

### Row 293

- **F:** Xóa data và để data = null
- **G:** case này không xảy ra- vì xóa data thì UI default về 0
- **I:** Show error message under the field is "The field is required"

### Row 294

- **A:** High
- **E:** > Production start date trong Order item
- **I:** 1/ Update Production start date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 295

- **A:** High
- **E:** > Estimated completion trong Order item
- **I:** 1/ Update Estimated completion thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 296

- **A:** High
- **E:** > Completion date trong Order item
- **I:** 1/ Update Completion date  thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 297

- **E:** > Cost trong Order item

### Row 298

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update cost thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 299

- **A:** Medium
- **G:** Update cost nếu order item đang có data cost

### Row 300

- **A:** Medium
- **G:** Update cost nếu order item đang không có data cost (null)

### Row 301

- **F:** Xóa data và để data = null
- **I:** Show error message under the field is "The field is required"

### Row 302

- **A:** Medium
- **F:** Chỉ được nhập cost >= 0
- **L:** PASS

### Row 303

- **A:** Medium
- **F:** Nhập quá 131072 trước chữ số thập phân và quá 16383 sau chữ số thập phân
- **I:** Show error message under the field is Please limit the integer part to 131072 digits and the decimal part to 16383 digits.

### Row 304

- **E:** > Note for PO

### Row 305

- **A:** High
- **F:** Update thành data khác khi đang có data note
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 306

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Bug 52665
- **L:** FAILED

### Row 307

- **E:** > Attachments
- **L:** FAILED

### Row 308

- **A:** High
- **F:** Update file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 309

- **A:** Medium
- **F:** Không thể chọn format khác với .xls, .xlsx, .pdf, .csv, .doc, .docx
- **I:** Hiển thị message: Invalid file format.

### Row 310

- **A:** Medium
- **F:** Update file > 5MB
- **I:** Error message in the popup “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

### Row 311

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 312

- **E:** Kiểm tra back về màn hình PO list thành công
- **L:** PASS

### Row 313

- **F:** Nếu chưa edit mà bấm Close
- **I:** Đóng popup Edit và back về màn hình PO list
- **L:** PASS

### Row 314

- **F:** Nếu đã edit mà bấm Close
- **I:** Hiển thị popup Confirm
- **L:** PASS

### Row 315

- **D:** Update thông tin PO có status là Reject

### Row 316

- **E:** > PO number

### Row 317

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update PO number thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 318

- **A:** Medium
- **F:** Xóa data PO number
- **I:** Show error message under the field is The field is required
- **L:** PASS

### Row 319

- **A:** Medium
- **G:** case bổ sung- không cho nhập ký tự đặc biệt- copy rule ở PO cũ
- **I:** show mess: This PO number is not valid

### Row 320

- **A:** Medium
- **G:** case bổ sung- không cho nhập warehouseảng trống
- **I:** show mess: This PO number is not valid

### Row 321

- **A:** Medium
- **F:** Update không thành công khi nhập data > 50 kí tư
- **I:** Show error message under the field “This PO ID is not over 50 characters”

### Row 322

- **A:** High
- **E:** > Supplier
- **I:** Không cho update
- **L:** PASS

### Row 323

- **A:** High
- **E:** > Warehouse
- **I:** 1/ Update Warehouse thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 324

- **E:** > Expected arrival date

### Row 325

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update Expected arrival date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 326

- **A:** High
- **F:** Không thể chọn Expected arrival date < {Today date}
- **L:** FAILED

### Row 327

- **E:** > Add item
- **I:** 1/ Add item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 328

- **F:** Add variant

### Row 329

- **A:** High
- **F:** > Active

### Row 330

- **A:** Medium
- **F:** > Archive

### Row 331

- **A:** Medium
- **F:** > Draft

### Row 332

- **A:** High
- **F:** Add component

### Row 333

- **E:** > Remove item
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 334

- **F:** Remove khi chọn icon delete 1 variant trên order line item
- **L:** PASS

### Row 335

- **G:** Remove variant

### Row 336

- **A:** High
- **G:** > Active

### Row 337

- **A:** Medium
- **G:** > Archive

### Row 338

- **A:** Medium
- **G:** > Draft

### Row 339

- **A:** High
- **G:** Remove component

### Row 340

- **F:** Remove khi select nhiều variant và chọn button Remove
- **L:** PASS

### Row 341

- **G:** Remove variant

### Row 342

- **A:** High
- **G:** > Active

### Row 343

- **A:** Medium
- **G:** > Archive

### Row 344

- **A:** Medium
- **G:** > Draft

### Row 345

- **A:** High
- **G:** Remove component

### Row 346

- **E:** > Order Qty trong Order item

### Row 347

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update order quantity thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 348

- **A:** Medium
- **F:** Nhập data = 0
- **I:** Show error message under the field is "Quantity must be greater than 0."

### Row 349

- **A:** Medium
- **F:** bổ sung: nhập số thập phân
- **I:** không thể nhập

### Row 350

- **F:** Xóa data và để data = null
- **G:** case này không xảy ra- vì xóa data thì UI default về 0
- **I:** Show error message under the field is "The field is required"

### Row 351

- **A:** High
- **E:** > Production start date trong Order item
- **I:** 1/ Update Production start date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 352

- **A:** High
- **E:** > Estimated completion trong Order item
- **I:** 1/ Update Estimated completion thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 353

- **A:** High
- **E:** > Completion date trong Order item
- **I:** 1/ Update Completion date  thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 354

- **E:** > Cost trong Order item

### Row 355

- **A:** High
- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update cost thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 356

- **A:** Medium
- **G:** Update cost nếu order item đang có data cost

### Row 357

- **A:** Medium
- **G:** Update cost nếu order item đang không có data cost (null)

### Row 358

- **F:** Xóa data và để data = null
- **I:** Show error message under the field is "The field is required"

### Row 359

- **A:** Medium
- **F:** Chỉ được nhập cost >= 0

### Row 360

- **A:** Medium
- **F:** Nhập quá 131072 trước chữ số thập phân và quá 16383 sau chữ số thập phân
- **I:** Show error message under the field is Please limit the integer part to 131072 digits and the decimal part to 16383 digits.

### Row 361

- **E:** > Note for PO

### Row 362

- **A:** High
- **F:** Update thành data khác khi đang có data note
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 363

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update note thành công và hiển thị thông báo Purchase order updated successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** FAILED

### Row 364

- **E:** > Attachments
- **L:** FAILED

### Row 365

- **A:** High
- **F:** Update file with format: .xls, .xlsx, .pdf, .csv, .doc, .docx
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 366

- **A:** Medium
- **F:** Không thể chọn format khác với .xls, .xlsx, .pdf, .csv, .doc, .docx

### Row 367

- **A:** Medium
- **F:** Update file > 5MB
- **I:** Error message in the popup “The attachment exceeds the size limit of 5MB. Please upload a smaller file."

### Row 368

- **A:** High
- **F:** Xóa data và lưu
- **I:** 1/ Update Attachments thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save

### Row 369

- **E:** Kiểm tra back về màn hình PO list thành công
- **L:** PASS

### Row 370

- **F:** Nếu chưa edit mà bấm Close
- **I:** Đóng popup Edit và back về màn hình PO list
- **L:** PASS

### Row 371

- **F:** Nếu đã edit mà bấm Close
- **I:** Hiển thị popup Confirm
- **L:** PASS

### Row 372

- **D:** Update thông tin PO có status là Open

### Row 373

- **A:** High
- **E:** > PO Number
- **I:** Không cho edit<br> + Nếu PO không có shipment In transit<br> + Nếu PO có shipment In transit
- **L:** PASS

### Row 374

- **A:** High
- **E:** > Supplier
- **I:** Không cho edit<br> + Nếu PO không có shipment In transit<br> + Nếu PO có shipment In transit
- **L:** PASS

### Row 375

- **E:** > Warehouse

### Row 376

- **A:** High
- **F:** Edit thành công Nếu PO không có shipment In transit
- **I:** 1/ Update Warehouse thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Bug 52661
- **L:** FAILED

### Row 377

- **A:** High
- **F:** Không cho edit Nếu PO có shipment In transit
- **I:** Không cho edit
- **K:** Bug 52672
- **L:** FAILED

### Row 378

- **E:** > Expected arrival date

### Row 379

- **F:** Update thành công khi nhập data hợp lệ
- **I:** 1/ Update Expected arrival date thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 380

- **F:** Không thể chọn Expected arrival date < {Today date}
- **L:** FAILED

### Row 381

- **E:** > Add item
- **I:** 1/ Add item thành công và hiển thị thông báo Purchase order saved successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **L:** PASS

### Row 382

- **F:** Add variant

### Row 383

- **A:** High
- **F:** > Active

### Row 384

- **A:** Medium
- **F:** > Archive

### Row 385

- **A:** Medium
- **F:** > Draft

### Row 386

- **A:** High
- **F:** Add component

### Row 387

- **E:** > Remove item
- **I:** 1/ Remove item thành công và hiển thị thông báo Purchase order updated successfully<br>2/ Vẫn ở màn hình PO detail và disable button Save
- **K:** Bug 52672
- **L:** FAILED

### Row 388

- **A:** High
- **F:** Không cho remove item nếu PO có shipment In transit
- **L:** FAILED

### Row 389

- **A:** High
- **G:** Remove 1 item
- **I:** hide icon delete cho line cuối cùng đi

### Row 390

- **A:** High
- **G:** Remove nhiều item
- **I:** show toast mess: "This PO does not contain any items. Please add items before issuing."

### Row 391

- **F:** Remove khi chọn icon delete 1 variant trên order line item
- **L:** PASS

### Row 392

- **G:** Remove variant

### Row 393

- **A:** High
- **G:** > Active

### Row 394

- **A:** Medium
- **G:** > Archive

### Row 395

- **A:** Medium
- **G:** > Draft

### Row 396

- **A:** High
- **G:** Remove component

### Row 397

- **F:** Remove khi select nhiều variant và chọn button Remove
- **L:** PASS

### Row 398

- **G:** Remove variant

### Row 399

- **A:** High
- **G:** > Active

### Row 400

- **A:** Medium
- **G:** > Archive


