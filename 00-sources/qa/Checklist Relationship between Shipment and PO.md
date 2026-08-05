# Checklist Relationship between Shipment and PO

> Nguồn: [Google Sheet – (DEMO) Relationship between Shipment and PO](https://docs.google.com/spreadsheets/d/1h4dWH60VvWba9katEO1Z3I1w0MZ1QFgqmb267wbMggk/edit?gid=1381927022#gid=1381927022)
>
> Tab: `(DEMO) Relationship between Shipment and PO`
>
> Nội dung được chuyển từ các ô trong vùng đọc A1:AO250; ô trống được giữ trống.

### Row 1

- **A:** Status Shipment<br>Type of PO<br>(Stt)
- **B:** Điều kiện tiên quyết không thể không có
- **C:** Các field được edit
- **D:** Các field không được edit
- **E:** Validate các field input
- **F:** Next status
- **G:** Action user có thể làm
- **H:** Impact PO - Shipment
- **J:** Vinh check ngày 16/01/2026
- **K:** field On order sẽ được update khi shipment phát sinh recieved từ status in transit đối với các report <br>Riêng trang PO detail on order chỉ được update khi status shipment = delivery

### Row 2

- **A:** Schedule
- **B:** - Shipping label -> requried-> unique<br>- Type-> requried<br>- PO Number-> requried<br>- Expected Ship Date-> requried<br>- Expected Arrival Date -> requried<br>- Cần phải có tối thiếu 1 item
- **C:** - Shipment label<br>- Tracking ID<br>- Warehouse (Luồng Edit shipment mới được edit, luồng tạo mới sẽ đi theo PO number được chọn)<br>- Expected ship date<br>- Expected arrival date<br>- Actual ship date<br>- Actual received date<br>- Search line item<br>- Add more item<br>- Remove item (không được remove all item)<br>- Shipment qty<br>- Received qty<br>- Lot Code<br>- Expiration Date.<br>- Note for shipments & upload attachments
- **D:** - Type<br>- PO Number<br>- Vendor <br>- Remove all item
- **E:** 1. Shipment label<br>  + là kiểu text- chỉ giới hạn max 255 ký tự<br>2. Tracking ID<br>  + là kiểu text- chỉ giới hạn max 255 ký tự<br>3. Expected ship date/ Expected arrival date/ Actual ship date/ Actual received date<br>   + là kiểu date - có thể chọn ngày qk, hiện tại , tương đều được<br>4. Shipment qty<br>   + là số nguyên dương phải > 0 <br>   + defaul show = 0<br>5. Received Qty<br>   + là số nguyên dương phải >= 0<br>   + defaul show = 0<br>   + Received Qty<=Shipment qty<br>6. Lot Code<br>  + là kiểu text- chỉ giới hạn max 255 ký tự<br>  + Nếu trên cùng 1 WH- lotcode không được trùng (khác WH có thể trùng)<br>  + nếu cùng lot nhưng khác date -> báo lỗi<br>  + chưa có lot này tồn tại-> oki -> tạo mới<br>7. Expiration Date<br>   + là kiểu date - có thể chọn ngày qk, hiện tại , tương đều được<br>   + nếu đã nhập data lot- thì phải nhập data date<br>   + chỉ nhập date -> k nhập lot ?? (api đang cho đc- nhưng get lại vẫn là null)<br><br>--<br>note: 1 lot- 1item (1WH- n lot)
- **F:** - In Transit<br>- Delivered (Linh chốt tạm bỏ ý này, ngày 08/12)<br>- Cancel
- **G:** - Chuyển stt shipment (In Transit, Delivered, Cancel)-> UI k làm delivered<br>- Delete<br>- View/ Edit
- **H:** - Khi user có edit WH ở shipment -> thì không có ảnh hưởng tới PO? (đang hỏi lại ý này còn đúng k)<br><br>- Khi user edit WH ở PO<br>   + Shipment dc tạo trước khi update WH info: giữ nguyên<br>   + create new shipment sau khi edit: đi theo thông tin of PO<br><br>- Khi user edit các thông tin khác ở PO-> update real time tương ứng cho shipment<br><br>- Nếu stt PO đã là Fulfilled rồi thì không thể edit received qty< order qty ở shipment được (đợi đọc đến Uc PO r review lại ý này)<br><br>- Không cho edit bất kì field nào ở trang Shipment detail khi Shipment đó map với PO đã cancel / closed (41030)(đợi đọc đến Uc PO r review lại ý này)

### Row 3

- **A:** In Transit
- **B:** giống ở trên
- **C:** - Shipment label<br>- Tracking ID<br>- Expected ship date<br>- Expected arrival date<br>- Actual ship date<br>- Actual received date<br>- Search line item<br>- Add more item<br>- Remove item (không được remove all item)-- test impact để các chỗ liên quan-- ý này low check sau<br>- Shipment qty<br>- Received qty<br>- Lot Code<br>- Expiration Date.<br>- Note for shipments & upload attachments
- **D:** - Type<br>- PO Number<br>- Warehouse<br>- Vendor<br>- Remove all item
- **E:** giống ở trên
- **F:** - Delivered
- **G:** - Chuyển stt shipment (Delivered)<br>- View/ Edit

### Row 4

- **A:** Delivered
- **B:** giống ở trên<br>Actual received date-> requried?
- **C:** - Shipment label<br>- Tracking ID<br>- Expected ship date<br>- Expected arrival date<br>- Actual ship date<br>- Actual received date<br>- Search line item<br>- Add more item<br>- Remove item (không được remove all item)-- test impact để các chỗ liên quan-- ý này low check sau<br>- Shipment qty<br>- Received qty<br>- Lot Code <br>- Expiration Date.<br>- Note for shipments & upload attachments
- **D:** - Type<br>- PO Number<br>- Warehouse<br>- Vendor<br>- Remove all item
- **E:** giống ở trên
- **F:** - Closed
- **G:** - Chuyển stt shipment (Closed)<br>- View/ Edit

### Row 5

- **A:** Cancelled
- **C:** - Search line item
- **D:** all field - trừ Search line item
- **F:** -
- **G:** - Delete<br>- View

### Row 6

- **A:** Closed
- **C:** - Search line item
- **D:** all field - trừ Search line item
- **F:** -
- **G:** - View

### Row 7


### Row 8


### Row 9

- **A:** PO<br>(Stt)
- **B:** Điều kiện tiên quyết không thể không có
- **C:** Các field được edit
- **D:** Các field không được edit
- **E:** Validate các field input
- **F:** Next status
- **G:** Action user có thể làm
- **H:** Impact PO - Shipment

### Row 10

- **A:** Draft
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item<br>---<br>- Khi user tạo mới PO và chọn button [Save as Draft]
- **C:** - PO Number<br>- Vendor<br>- Warehouse <br>- Expected arrival date<br>- Search line item<br>- Add item<br>- Remove item<br>- Order qty<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Cost<br>- Note for PO & upload attachments
- **D:** - Created date
- **E:** 1. PO number<br>  + là kiểu text- Chỉ chấp nhận ký tự chữ và số - giới hạn max 50 ký tự?<br>2. Vendor/ Warehouse<br>  +  data được chọn ở 2 field này phải khác nhau?<br>3. Expected ship date/ Expected arrival date/ Actual ship date/ Actual received date<br>   + là kiểu date - có thể chọn ngày qk, hiện tại , tương đều được<br>4. Order qty<br>   + là số ...bổ sung thêm vào<br>   + defaul show =... bổ sung thêm vào<br>- Production Start Date<br>bổ sung thêm vào<br>- Estimated Completion <br>bổ sung thêm vào<br>- Completion Date<br>bổ sung thêm vào<br>- Cost<br>bổ sung thêm vào<br>- Note for TO & upload attachments<br>bổ sung thêm vào
- **F:** - Pending Approval<br>- Open<br>- Cancel
- **G:** - Chuyển stt PO (Pending Approval, Open, Cancel)<br>- View Detail/ Edit<br>- Delete PO
- **H:** Không thể tạo liên kết với shipment

### Row 11

- **A:** Pending Approval
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item<br>---<br>- Khi<br> 1.User tạo mới PO và chọn button [Request approval]<br> 2. Or chuyển từ stt.. sang stt Pending Approval
- **C:** - PO Number<br>- Warehouse <br>- Expected arrival date<br>- Search line item<br>- Add item<br>- Remove item (không được remove all item)<br>- Order qty<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Cost<br>- Note for PO & upload attachments
- **D:** - Created date<br>- Vendor
- **F:** - Open<br>- Rejected<br>- Cancel
- **G:** - Chuyển stt PO (Open, Rejected, Cancel)<br>- View Detail/ Edit<br>- Delete PO
- **H:** Không thể tạo liên kết với shipment

### Row 12

- **A:** Rejected
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item<br>---<br>- Khi chuyển từ stt.. sang stt Rejected (chọn button [Reject])
- **C:** - PO Number<br>- Warehouse <br>- Expected arrival date<br>- Search line item<br>- Add item<br>- Remove item <br>- Order qty<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Cost<br>- Note for PO & upload attachments
- **D:** - Created date<br>- Vendor
- **F:** - Pending Approval<br>- Cancel
- **G:** - Chuyển stt PO (Pending Approval, Cancel)<br>- View Detail/ Edit<br>- Delete PO
- **H:** Không thể tạo liên kết với shipment

### Row 13

- **A:** Open
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item<br>---<br>- Khi<br> 1.User tạo mới PO và chọn button [Issue PO]<br> 2. Or chuyển từ stt.. sang stt Open
- **C:** - Warehouse <br>- Expected arrival date<br>- Search line item<br>- Add item<br>- Remove item (không được remove all item)<br>- Order qty<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Cost<br>- Note for PO & upload attachments
- **D:** - PO Number<br>- Created date<br>- Vendor<br>--<br><br>- If PO has shipment status is "In transit": <br>can't update: PO nummber, creation date, warehouse, vendor, delete items- sẽ ghi rõ ý này sau
- **F:** - Partially Fulfilled<br>- Fulfilled<br>- Cancel
- **G:** - Chuyển stt PO (Cancel)<br>- View Detail/ Edit
- **H:** Có thể tạo liên kết với shipment

### Row 14

- **A:** Partially fulfilled
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item <br>---<br>- Khi có ít nhất 1 item of the PO có stt là ""Received"" / ""Under received"" / ""Over received"
- **C:** - Expected arrival date<br>- Search line item<br>- Add item<br>- Remove item không có phát sinh received<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Cost of items chưa received<br>- Note for PO & upload attachments
- **D:** - PO Number<br>- Created date<br>- Vendor<br>- Warehouse <br>- Remove item có phát sinh received<br>- Order qty<br>- Cost of items đã received
- **F:** - Fulfilled<br>- Closed
- **G:** - Chuyển stt PO (Closed)<br>- View Detail/ Edit
- **H:** Có thể tạo liên kết với shipment <br><br>+ Chỉ cần shipment có data received qty-> thì auto stt PO sẽ được chuyển sang Partially fulfilled/ Fulfilled<br>--Lưu ý: data received qty của shipment sẽ được tính cho PO, khi shipment có stt là Delivered/ Closed<br><br>+ Data <br>    Received Qty ở PO= sum Received Qty của item có shipment link với PO<br>    Received history ở PO<br>        1. Date -> = field “actual received date” ơ shipment<br>        2. number-> = field "received qty" ở shipment<br><br>Note của Received history: không có data nào thì show "-" ở phần đó

### Row 15

- **A:** Fulfilled
- **B:** - PO Number -> requried-> unique<br>- Vendor-> requried<br>- Warehouse -> requried<br>- Cần phải có tối thiếu 1 item<br>---<br>- Khi all items of the PO có stt là ""Received""/ ""Over received"
- **C:** - Search line item<br>- Production Start Date<br>- Estimated Completion <br>- Completion Date<br>- Note <br>- Attachments
- **D:** - PO Number<br>- Created date<br>- Vendor<br>- Warehouse <br>- Add item<br>- Remove item<br>- Order qty<br>- Cost
- **F:** - Closed
- **G:** - Chuyển stt PO (Closed)<br>- View Detail/ Edit
- **H:** Có thể tạo liên kết với shipment <br><br>+ Chỉ cần shipment có data received qty-> thì auto stt PO sẽ được chuyển sang Partially fulfilled/ Fulfilled <br><br>--Lưu ý: data received qty của shipment sẽ được tính cho PO, khi shipment có stt là Delivered/ Closed

### Row 16

- **A:** Closed
- **C:** - Search line item
- **D:** all field - trừ Search line item
- **H:** Không thể tạo liên kết với shipment <br><br>Nếu trc đó đã có link vs Shipment- rồi user update stt PO thành closed thì vẫn giữ link vs Shipment<br><br>Chỉ được close PO khi tất cả shipment đã được Received hoặc Cancelled.(41013)

### Row 17

- **A:** Cancelled
- **C:** - Search line item
- **D:** all field - trừ Search line item
- **H:** Không thể tạo liên kết với shipment
- **I:** -- Có update mới-- đã có thể xóa 69548

### Row 18


### Row 19


### Row 20


### Row 21

- **A:** Relationship between Shipment and PO Status - Details

### Row 22

- **A:** Case
- **B:** Case Con
- **C:** Case Con
- **D:** Case Con
- **E:** Status PO

### Row 23

- **A:** Case: PO có 1 item<br>PO (Open) có<br>   + 1 item với Order qty=100

### Row 24

- **B:** Link vs 1 shipment
- **F:** PASS

### Row 25

- **C:** Shipment (01) (scheduled)
- **E:** Open
- **F:** PASS

### Row 26

- **C:** Shipment (01) (cancel)
- **E:** Open
- **F:** PASS

### Row 27

- **C:** Shipment (01) (in transit)
- **E:** Open
- **F:** PASS

### Row 28

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:0
- **E:** Open
- **F:** PASS

### Row 29

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:1
- **E:** Partially Fulfilled
- **F:** PASS

### Row 30

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:100
- **E:** Fulfilled
- **F:** PASS

### Row 31

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:101
- **E:** Fulfilled
- **F:** PASS

### Row 32

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:0
- **E:** Open

### Row 33

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 34

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:100
- **E:** Fulfilled
- **F:** PASS

### Row 35

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:101
- **E:** Fulfilled
- **F:** PASS

### Row 36

- **B:** Link vs 2 shipment

### Row 37

- **C:** Shipment 1 có stt là scheduled/cancel/In transit<br>Shipment 2 sao cũng đc

### Row 38

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02) (scheduled/cancel/In transit)
- **E:** Open
- **F:** PASS

### Row 39

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (delivered) <br>  + Recevied qty:0
- **E:** Open
- **F:** PASS

### Row 40

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (delivered) <br>  + Recevied qty:1
- **E:** Partially Fulfilled
- **F:** PASS

### Row 41

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (delivered) <br>  + Recevied qty:100
- **E:** Fulfilled

### Row 42

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (delivered) <br>  + Recevied qty:101
- **E:** Fulfilled
- **F:** PASS

### Row 43

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (Closed) <br>  + Recevied qty:0
- **E:** Open

### Row 44

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (Closed) <br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 45

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (Closed) <br>  + Recevied qty:100
- **E:** Fulfilled

### Row 46

- **D:** Shipment (01) (scheduled/cancel/In transit) <br>Shipment (02)  (Closed) <br>  + Recevied qty:101
- **E:** Fulfilled

### Row 47

- **C:** Shipment 1 có stt là delivered<br>Shipment 2 sao cũng đc

### Row 48

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (delivered) <br>  + Recevied qty:0
- **E:** Open
- **F:** PASS

### Row 49

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (delivered) <br>  + Recevied qty:1
- **E:** Partially Fulfilled
- **F:** PASS

### Row 50

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:1<br>Shipment (02) (delivered) <br>  + Recevied qty:0
- **E:** Partially Fulfilled

### Row 51

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (delivered) <br>  + Recevied qty:100
- **E:** Fulfilled
- **F:** PASS

### Row 52

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (delivered) <br>  + Recevied qty:101
- **E:** Fulfilled
- **F:** PASS

### Row 53

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:50<br>Shipment (02) (delivered) <br>  + Recevied qty:50
- **E:** Fulfilled
- **F:** PASS

### Row 54

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (Closed) <br>  + Recevied qty:0
- **E:** Open

### Row 55

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (Closed) <br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 56

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:1<br>Shipment (02) (Closed) <br>  + Recevied qty:0
- **E:** Partially Fulfilled

### Row 57

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (Closed) <br>  + Recevied qty:100
- **E:** Fulfilled

### Row 58

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:0<br>Shipment (02) (Closed) <br>  + Recevied qty:101
- **E:** Fulfilled

### Row 59

- **D:** Shipment (01) (delivered)<br>  + Recevied qty:50<br>Shipment (02) (Closed) <br>  + Recevied qty:50
- **E:** Fulfilled

### Row 60

- **A:** Case: PO có 1 item<br>PO (Open) có<br>   + item (1) với Order qty=100<br>   + item (2) với Order qty=100

### Row 61

- **B:** Link vs 1 shipment cho 1 item

### Row 62

- **C:** Shipment (01) (scheduled)
- **E:** Open

### Row 63

- **C:** Shipment (01) (cancel)
- **E:** Open

### Row 64

- **C:** Shipment (01) (in transit)
- **E:** Open
- **F:** PASS

### Row 65

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:0
- **E:** Open
- **F:** PASS

### Row 66

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 67

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:100
- **E:** Partially Fulfilled

### Row 68

- **C:** Shipment (01) (delivered) <br>  + Recevied qty:200
- **E:** Partially Fulfilled
- **F:** PASS

### Row 69

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:0
- **E:** Open

### Row 70

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 71

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:100
- **E:** Partially Fulfilled

### Row 72

- **C:** Shipment (01) (Closed) <br>  + Recevied qty:200
- **E:** Partially Fulfilled

### Row 73

- **B:** Link vs 1 shipment cho 2 item

### Row 74

- **C:** Shipment (01) (scheduled)
- **E:** Open

### Row 75

- **C:** Shipment (01) (cancel)
- **E:** Open

### Row 76

- **C:** Shipment (01) (in transit)
- **E:** Open

### Row 77

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty:0 <br>item (2)<br>  + Recevied qty:0
- **E:** Open
- **F:** PASS

### Row 78

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty:200 <br>item (2)<br>  + Recevied qty:1
- **E:** Partially Fulfilled
- **F:** PASS

### Row 79

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty: 1<br>item (2)<br>  + Recevied qty: 200
- **E:** Partially Fulfilled

### Row 80

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty: 100 <br>item (2)<br>  + Recevied qty: 100
- **E:** Fulfilled
- **F:** PASS

### Row 81

- **C:** Shipment (01) (closed) cho<br>item (1)<br>  + Recevied qty:0 <br>item (2)<br>  + Recevied qty:0
- **E:** Open

### Row 82

- **C:** Shipment (01) (closed) cho<br>item (1)<br>  + Recevied qty:200 <br>item (2)<br>  + Recevied qty:1
- **E:** Partially Fulfilled

### Row 83

- **C:** Shipment (01) (closed) cho<br>item (1)<br>  + Recevied qty: 1<br>item (2)<br>  + Recevied qty: 200
- **E:** Partially Fulfilled

### Row 84

- **C:** Shipment (01) (closed) cho<br>item (1)<br>  + Recevied qty: 100 <br>item (2)<br>  + Recevied qty: 100
- **E:** Fulfilled

### Row 85

- **B:** 2 shipment cho 2 item

### Row 86

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty: 1<br>Shipment (02) (delivered)<br>  + Recevied qty: 200
- **E:** Partially Fulfilled
- **F:** PASS

### Row 87

- **C:** Shipment (01) (delivered) cho<br>item (1)<br>  + Recevied qty: 1<br>item (2)<br>  + Recevied qty: 200
- **E:** Fulfilled
- **F:** PASS

### Row 88

- **A:** Relationship between Shipment/ PO and stock

### Row 89

- **A:** Case impact về số lượng stock (giả thuyết là item và WH đều thuộc conative)

### Row 90

- **A:** 1. Happy case (flow tổng thể, 1PO, 1 item, 1 shipment)
- **F:** PASS

### Row 91

- **A:** Thời điểm/ Hành động
- **B:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 92

- **B:** Shipment label
- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 93

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 94

- **A:** Tạo 1 PO gồm<br>1.  Order qty=100, và stt của PO là Draft
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** 0
- **G:** Draft
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0
- **M:** Failed on order

### Row 95

- **A:** User chuyển sang stt PO sang Pending
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** 0
- **G:** Pending
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0
- **M:** Failed on order

### Row 96

- **A:** User chuyển sang stt PO sang Open
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0
- **M:** Failed:52413
- **N:** oki
- **O:** Passed on order

### Row 97

- **A:** Tạo 1 Shipment link vs PO, có thông tin<br>+ stt Shipment là schedule<br>+ Shipment qty=100<br>+ received qty= 40
- **B:** Shipment 01
- **C:** 100
- **D:** 40
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0
- **M:** Passed on order

### Row 98

- **A:** Chuyển stt Shipment thành In transit
- **B:** Shipment 01
- **C:** 100
- **D:** 40
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0
- **M:** Failed:52415
- **N:** oki
- **O:** Passed on order
- **P:** Failed on order đối với các report # inventory item

### Row 99

- **A:** Chuyển stt Shipment thành Delivered
- **B:** Shipment 01
- **C:** 100
- **D:** 40
- **E:** Delivered
- **F:** 40
- **G:** Partially Fulfilled
- **H:** -
- **I:** -
- **J:** 60
- **K:** 60
- **L:** 40
- **O:** Passed on order
- **P:** Passed on order đối với các report # inventory item

### Row 100

- **A:** Edit received qty lên 100
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100
- **O:** Passed on order
- **P:** Passed on order đối với các report # inventory item

### Row 101

- **A:** Chuyển stt shipment thành closed
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Closed
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100
- **M:** done
- **O:** Passed on order

### Row 102


### Row 103

- **A:** 2. Case shipment qty và receive qty > order qty
- **F:** FAILED

### Row 104

- **A:** Thời điểm/ Hành động
- **B:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 105

- **B:** Shipment label
- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 106

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 107

- **A:** Tạo 1 PO gồm<br>1.  Order qty=100, và stt của PO là Open<br>2. Tạo thêm 1 shipment schedule với<br>   + Shipment qty=200<br>   + received qty= 200
- **B:** Shipment 01
- **C:** 200
- **D:** 150
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0
- **M:** Failed:52413
- **O:** Passed on order
- **P:** Passed on order đối với các report # inventory item

### Row 108

- **A:** Chuyển stt Shipment thành In transit
- **B:** Shipment 01
- **C:** 200
- **D:** 150
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 200
- **L:** 0
- **M:** Failed:52415
- **O:** Passed on order
- **P:** Passed on order đối với các report # inventory item

### Row 109

- **A:** Chuyển stt Shipment thành Delivered
- **B:** Shipment 01
- **C:** 200
- **D:** 150
- **E:** Delivered
- **F:** 150
- **G:** Fulfilled
- **J:** 0
- **K:** 0
- **L:** 150
- **M:** failed: 52517
- **O:** Passed on order
- **P:** Passed on order đối với các report # inventory item

### Row 110


### Row 111

- **A:** 3. Case PO - 1 item - link vs 2 shipment

### Row 112

- **A:** 3.1. Chỉ cần 1 shipment là đủ fulfilled

### Row 113

- **A:** Thời điểm/ Hành động
- **B:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 114

- **B:** Shipment label
- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 115

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 116

- **A:** Tạo 1 PO gồm<br>1.  Order qty=100, và stt của PO là Open<br>2. Tạo thêm 2 shipment schedule với thông tin sau<br>2.1<br>   + Shipment qty=100<br>   + received qty= 100<br>2.2 <br>   + Shipment qty=100<br>   + received qty= 100
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 117

- **B:** Shipment 02
- **C:** 100
- **D:** 100
- **E:** Schedule

### Row 118

- **A:** chuyển stt của shipment 01 thành In transit
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 119

- **B:** Shipment 02
- **C:** 100
- **D:** 100
- **E:** Schedule

### Row 120

- **A:** chuyển stt của shipment 01 thành Delivered
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 121

- **B:** Shipment 02
- **C:** 100
- **D:** 100
- **E:** Schedule

### Row 122

- **A:** chuyển stt của shipment 02 thành In transit
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 100

### Row 123

- **B:** Shipment 02
- **C:** 100
- **D:** 100
- **E:** In transit
- **M:** failed: 52517

### Row 124

- **A:** chuyển stt của shipment 02 thành Delivered
- **B:** Shipment 01
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 200
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 200

### Row 125

- **B:** Shipment 02
- **C:** 100
- **D:** 100
- **E:** Delivered

### Row 126

- **A:** 3.2  Hai shipment cộng lại mới fulfilled

### Row 127

- **A:** Thời điểm/ Hành động
- **B:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 128

- **B:** Shipment label
- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 129

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 130

- **A:** Tạo 1 PO gồm<br>1.  Order qty=100, và stt của PO là Open<br>2. Tạo thêm 2 shipment schedule với thông tin sau<br>2.1<br>   + Shipment qty=50<br>   + received qty= 50<br>2.2 <br>   + Shipment qty=50<br>   + received qty= 50
- **B:** Shipment 01
- **C:** 50
- **D:** 50
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 131

- **B:** Shipment 02
- **C:** 50
- **D:** 50
- **E:** Schedule

### Row 132

- **A:** chuyển stt của shipment 01 thành In transit
- **B:** Shipment 01
- **C:** 50
- **D:** 50
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 50
- **K:** 50
- **L:** 0

### Row 133

- **B:** Shipment 02
- **C:** 50
- **D:** 50
- **E:** Schedule

### Row 134

- **A:** chuyển stt của shipment 01 thành Delivered
- **B:** Shipment 01
- **C:** 50
- **D:** 50
- **E:** Delivered
- **F:** 50
- **G:** Partially Fulfilled
- **H:** -
- **I:** -
- **J:** 50
- **K:** 0
- **L:** 50

### Row 135

- **B:** Shipment 02
- **C:** 50
- **D:** 50
- **E:** Schedule

### Row 136

- **A:** chuyển stt của shipment 02 thành In transit
- **B:** Shipment 01
- **C:** 50
- **D:** 50
- **E:** Delivered
- **F:** 50
- **G:** Partially Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 50
- **L:** 50

### Row 137

- **B:** Shipment 02
- **C:** 50
- **D:** 50
- **E:** In transit

### Row 138

- **A:** chuyển stt của shipment 02 thành Delivered
- **B:** Shipment 01
- **C:** 50
- **D:** 50
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 139

- **B:** Shipment 02
- **C:** 50
- **D:** 50
- **E:** Delivered

### Row 140


### Row 141

- **A:** 4. Case PO - 2 item - link vs 1 shipment

### Row 142

- **A:** 4.1 Cả 2 item cùng received

### Row 143

- **A:** Thời điểm/ Hành động
- **B:** Item
- **C:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 144

- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 145

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 146

- **A:** Tạo 1 PO (Open) gồm 2 item<br>1.  Item (1) Order qty=100<br>2.  Item (2) Order qty=100<br><br>Và tạo thêm 1 shipment (schedule) cho 2 item<br> + item 1: Shipment qty=100, received qty= 100<br> + item 1: Shipment qty=100, received qty= 100
- **B:** item 1
- **C:** 100
- **D:** 100
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 147

- **B:** Item 2
- **C:** 100
- **D:** 100
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 148

- **A:** Chuyển stt shipment thành In transit
- **B:** item 1
- **C:** 100
- **D:** 100
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 149

- **B:** Item 2
- **C:** 100
- **D:** 100
- **F:** 0
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 150

- **A:** Chuyển stt shipment thành Delivered
- **B:** item 1
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 151

- **B:** Item 2
- **C:** 100
- **D:** 100
- **F:** 100
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 152


### Row 153

- **A:** 4.2 Có 1 item received trc

### Row 154

- **A:** Thời điểm/ Hành động
- **B:** Item
- **C:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 155

- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 156

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 157

- **A:** Tạo 1 PO (Open) gồm 2 item<br>1.  Item (1) Order qty=100<br>2.  Item (2) Order qty=100<br><br>Và tạo thêm 1 shipment (schedule) cho 2 item<br> + item 1: Shipment qty=100, received qty= 40<br> + item 1: Shipment qty=100, received qty= 100
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 158

- **B:** Item 2
- **C:** 100
- **D:** 100
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 159

- **A:** Chuyển stt shipment thành In transit
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 160

- **B:** Item 2
- **C:** 100
- **D:** 100
- **F:** 0
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 161

- **A:** Chuyển stt shipment thành Delivered
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** Delivered
- **F:** 40
- **G:** Partially Fulfilled
- **H:** -
- **I:** -
- **J:** 60
- **K:** 60
- **L:** 40

### Row 162

- **B:** Item 2
- **C:** 100
- **D:** 100
- **F:** 100
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 163

- **A:** Edit lại received của item 1
- **B:** item 1
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 164

- **B:** Item 2
- **C:** 100
- **D:** 100
- **F:** 100
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 165


### Row 166

- **A:** 4.3 Có 1 item over received và 1 item under received

### Row 167

- **A:** Thời điểm/ Hành động
- **B:** Item
- **C:** Shipment
- **F:** PO
- **H:** Stock tại warehouse A (warehouse chuyển đi)
- **J:** Stock tại warehouse B (warehouse nhận)

### Row 168

- **C:** Shipment qty
- **D:** Received qty
- **E:** Stt
- **F:** Received qty
- **G:** Stt
- **H:** On Hand
- **I:** In Transit
- **J:** On Order
- **K:** In Transit
- **L:** On Hand

### Row 169

- **A:** Ban đầu
- **B:** N/A
- **C:** N/A
- **D:** N/A
- **E:** N/A
- **F:** N/A
- **G:** N/A
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 0

### Row 170

- **A:** Tạo 1 PO (Open) gồm 2 item<br>1.  Item (1) Order qty=100<br>2.  Item (2) Order qty=100<br><br>Và tạo thêm 1 shipment (schedule) cho 2 item<br> + item 1: Shipment qty=100, received qty= 40<br> + item 1: Shipment qty=200, received qty= 200
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** Schedule
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 171

- **B:** Item 2
- **C:** 200
- **D:** 200
- **H:** -
- **I:** -
- **J:** 100
- **K:** 0
- **L:** 0

### Row 172

- **A:** Chuyển stt shipment thành In transit
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** In transit
- **F:** 0
- **G:** Open
- **H:** -
- **I:** -
- **J:** 0
- **K:** 100
- **L:** 0

### Row 173

- **B:** Item 2
- **C:** 200
- **D:** 200
- **F:** 0
- **H:** -
- **I:** -
- **J:** 0
- **K:** 200
- **L:** 0

### Row 174

- **A:** Chuyển stt shipment thành Delivered
- **B:** item 1
- **C:** 100
- **D:** 40
- **E:** Delivered
- **F:** 40
- **G:** Partially Fulfilled
- **H:** -
- **I:** -
- **J:** 60
- **K:** 60
- **L:** 40

### Row 175

- **B:** Item 2
- **C:** 200
- **D:** 200
- **F:** 200
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 200

### Row 176

- **A:** Edit lại received của item 1
- **B:** item 1
- **C:** 100
- **D:** 100
- **E:** Delivered
- **F:** 100
- **G:** Fulfilled
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 100

### Row 177

- **B:** Item 2
- **C:** 200
- **D:** 200
- **F:** 200
- **H:** -
- **I:** -
- **J:** 0
- **K:** 0
- **L:** 200

### Row 178


### Row 179


### Row 180

- **C:** PO- open
- **D:** Shipment có stt Scheduled
- **E:** Shipment có stt In transit
- **F:** Shipment có stt Delivered

### Row 181

- **A:** Item (Conative)

### Row 182

- **B:** WH from(conative)- WH to(conative)
- **C:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: tăng (Order Qty)
- **D:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: giữ nguyên
- **E:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng (Shipment Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Shipment Qty)
- **F:** WH to: <br> + On Hand tăng (Received Qty)<br> + Incoming: giảm (Received Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Received Qty)
- **G:** pass

### Row 183

- **B:** WH from(conative)- WH to(ERP)
- **C:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: tăng (Order Qty)
- **D:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: giữ nguyên
- **E:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng (Shipment Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Shipment Qty)
- **F:** WH to: <br> + On Hand tăng (Received Qty)<br> + Incoming: giảm (Received Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Received Qty)
- **G:** pass

### Row 184

- **B:** WH from(ERP)- WH to(conative)
- **C:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **D:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **E:** WH From: <br> + On Hand giảm<br> + Incoming: (giữ nguyên)<br> + Outgoing: tăng<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng<br> + Outgoing: (giữ nguyên)
- **F:** WH From: <br> + Incoming: (giữ nguyên)<br> + Outgoing: giảm<br> + On Hand: (giữ nguyên)<br><br>WH to: <br> + On Hand tăng<br> + Incoming: giảm<br> + Outgoing: (giữ nguyên)

### Row 185

- **B:** WH from(ERP)- WH to(ERP)
- **C:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **D:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **E:** WH From: <br> + On Hand giảm<br> + Incoming: (giữ nguyên)<br> + Outgoing: tăng<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng<br> + Outgoing: (giữ nguyên)
- **F:** WH From: <br> + Incoming: (giữ nguyên)<br> + Outgoing: giảm<br> + On Hand: (giữ nguyên)<br><br>WH to: <br> + On Hand tăng<br> + Incoming: giảm<br> + Outgoing: (giữ nguyên)

### Row 186

- **A:** Item (ERP)

### Row 187

- **B:** WH from(conative)- WH to(conative)
- **C:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **D:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **E:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng<br> + Outgoing: (giữ nguyên)
- **F:** WH to: <br> + On Hand tăng<br> + Incoming: giảm<br> + Outgoing: (giữ nguyên)
- **G:** pass

### Row 188

- **B:** WH from(conative)- WH to(ERP)
- **C:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: tăng (Order Qty)
- **D:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br> + stockOnOrder: giữ nguyên
- **E:** WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng (Shipment Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Shipment Qty)
- **F:** WH to: <br> + On Hand: giữ nguyên<br> + Incoming: giảm (Received Qty)<br> + Outgoing: (giữ nguyên)<br> + stockOnOrder: giảm (Received Qty)
- **G:** pass

### Row 189

- **B:** WH from(ERP)- WH to(conative)
- **C:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **D:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **E:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: (giữ nguyên)<br> + Outgoing: tăng<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng<br> + Outgoing: (giữ nguyên)
- **F:** WH From: <br> + Incoming: (giữ nguyên)<br> + Outgoing: giảm<br> + On Hand: (giữ nguyên)<br><br>WH to: <br> + On Hand tăng<br> + Incoming: giảm<br> + Outgoing: (giữ nguyên)

### Row 190

- **B:** WH from(ERP)- WH to(ERP)
- **C:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **D:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: 0<br> + Outgoing: 0
- **E:** WH From: <br> + On Hand: (giữ nguyên)<br> + Incoming: (giữ nguyên)<br> + Outgoing: tăng<br><br>WH To: <br> + On Hand: (giữ nguyên)<br> + Incoming: tăng<br> + Outgoing: (giữ nguyên)
- **F:** WH From: <br> + Incoming: (giữ nguyên)<br> + Outgoing: giảm<br> + On Hand: (giữ nguyên)<br><br>WH to: <br> + On Hand: (giữ nguyên)<br> + Incoming: giảm<br> + Outgoing: (giữ nguyên)

### Row 191


### Row 192


### Row 193


### Row 194

- **A:** Lot code (tuy chưa tạo ra item- lot nhưng lot đã đc sinh ra)

### Row 195

- **D:** Mong muốn

### Row 196

- **A:** Cùng 1 WH

### Row 197

- **B:** add 2 item có cùng lot
- **D:** báo failed

### Row 198

- **C:** cùng lot- cùng expirationDate
- **D:** báo failed

### Row 199

- **C:** cùng lot- khác expirationDate
- **D:** báo failed

### Row 200

- **B:** add 2 item khác lot
- **C:** cùng lot- cùng expirationDate
- **D:** oki

### Row 201

- **A:** 2 WH
- **B:** cùng 1 item cùng lot code
- **D:** oki

### Row 202


### Row 203

- **A:** 1 item - edit

### Row 204

- **B:** lotcode
- **C:** nếu giá trị lotcode này đã item đã có từ trước

### Row 205

- **D:** expirationDate trùng -> oki

### Row 206

- **D:** expirationDate khác-> báo lỗi

### Row 207

- **C:** nếu giá trị lotcode này đã item chưa có -> thì tạo mới

### Row 208

- **B:** có giá trị lot- nhưng bỏ trống expirationDate
- **D:** báo failed


