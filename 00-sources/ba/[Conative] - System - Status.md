# [Conative] - System - Status

> Nguồn: [Google Sheet – [Conative] - System - Status](https://docs.google.com/spreadsheets/d/1iJ2WlqGr3tmCX1dFw5MhQb8grW6i38YJP983zPPSnwY/edit?gid=1429042187#gid=1429042187)
>
> Tất cả 10 sheet được đọc và giữ riêng theo từng tab. Nội dung lấy từ các vùng dữ liệu giới hạn đến hàng 300; ô trống được giữ trống.

## Subscription

### Row 1


### Row 2


### Row 3

- **A:** Stripe
- **B:** Conative - Hiện tại
- **C:** Conative - New
- **D:** Description
- **E:** Note

### Row 4

- **A:** Trialing
- **B:** Pending
- **C:** Free Trial
- **D:** mặc định khi tạo 1 subscription
- **E:** xác định time free trial

### Row 5

- **A:** Active
- **B:** Enabled
- **C:** Active
- **D:** hết free trial

### Row 6

- **A:** Active
- **B:** Enabled
- **C:** Active
- **D:** charge thành công

### Row 7

- **A:** past_due
- **B:** Pending
- **C:** Pause
- **D:** - tạo ra invoice và thanh toán không thành công. <br>- retry không thành công
- **E:** xác định theo time expried time free trial

### Row 8

- **A:** Canceled
- **B:** Cancel
- **C:** Cancel
- **D:** hết time retry, cancel subscription

### Row 9

- **A:** các status còn lại stripe trả về chưa handle
- **B:** Pending
- **C:** Pending

## PO item status

### Row 1

- **A:** Status
- **B:** Next status
- **C:** Trigger when

### Row 2

- **A:** Not received
- **B:** Received
- **C:** Received qty = order qty

### Row 3

- **B:** Under received
- **C:** Received qty < order qty

### Row 4

- **B:** Over received
- **C:** Received qty > order qty

### Row 5

- **A:** Under received
- **B:** Received
- **C:** Received qty = order qty

### Row 6

- **A:** Received
- **B:** Over received
- **C:** Received qty > order qty

### Row 7

- **A:** Over received
- **B:** -

### Row 8


### Row 9

- **A:** Note: The received quantity is the total quantity received across all shipments linked to the purchase order.

## PO Status

### Row 1

- **A:** NOTE: If a status transition does not have a note indicating "auto change," it means the user needs to update it manually.
- **G:** PO sync

### Row 2

- **A:** Status
- **B:** Description
- **C:** Next status
- **D:** Trigger when
- **E:** Condition to change
- **F:** Allowed actions

### Row 3

- **A:** -
- **B:** On the creating page, the user can create a new PO with status:
- **C:** Draft
- **D:** The PO has been created but is not yet finalized or submitted for approval.<br>Action: Further edits or changes can be made.
- **E:** The required fields: <br>- PO number<br>- Vendor <br>- Warehouse<br>- Expected Arrival Date

### Row 4

- **C:** Pending Approval
- **D:** send to approver
- **E:** The required fields: <br>- PO number<br>- Vendor <br>- Warehouse<br>- At least 1 item (Cost + order qty)

### Row 5

- **C:** Open
- **D:** Issue PO
- **E:** The required fields: <br>- PO number<br>- Vendor <br>- Warehouse<br>- At least 1 item (Cost + order qty)

### Row 6

- **A:** Draft
- **B:** The PO is in draft status - haven't been finalized yet
- **C:** Pending Approval
- **D:** send to approver
- **E:** All required fields have been filled
- **F:** - Updated all fields except "Creation date" <br>- Delete PO

### Row 7

- **C:** Open
- **D:** Issue PO
- **E:** All required fields have been filled

### Row 8

- **C:** Cancelled

### Row 9

- **A:** Pending approval
- **B:** The PO is waiting for approval
- **C:** Open
- **D:** The PO is approved
- **E:** All required fields have been filled
- **F:** - Updated all fields except "Creation date" & "Vendor"<br>- Delete PO

### Row 10

- **C:** Rejected
- **D:** The PO was rejected during the approval process or by the vendor.<br>Action: Review the rejection reason and revise the PO if necessary.
- **E:** NO

### Row 11

- **C:** Cancelled

### Row 12

- **A:** Rejected
- **B:** Approver rejects the PO → Do not record the data in the system for further calculation.
- **C:** Pending approval
- **D:** The user considers approving the PO again.
- **E:** All required fields have been filled
- **F:** - Updated all fields except "Creation date"  & "Vendor"<br>- Delete PO

### Row 13

- **C:** Cancelled

### Row 14

- **A:** Open
- **B:** The warehouse and supplier have agreed on prices, production dates, etc. → The PO is being prepared and is in transit.
- **C:** Partially Fulfilled Received
- **D:** Vendor begins delivery of items/services.<br>The system auto changes the status to "Partially fulfilled" if at least 1 item of the PO has the status "Received" / "Under received" / "Over received"
- **F:** - Updated all fields except "PO number" + "Creation date" + "Vendor"<br><br><br>- If PO has shipment status is "In transit": <br>can't update: PO nummber, creation date, warehouse, vendor, delete items

### Row 15

- **C:** Fulfilled Received
- **D:** The system auto changes the status to "Fulfilled" if all items of the PO has the status "Received" / "Over received"

### Row 16

- **C:** Cancelled

### Row 17

- **A:** Partially fulfilled Received
- **B:** The warehouse has received a partial delivery of the PO
- **C:** Fulfilled Received
- **D:** All items/services are delivered and accepted.<br>The system auto changes the status to "Fulfilled" if all items of the PO has the status "Received" / "Over received"
- **F:** The user can update:<br>- Expected arrival date <br>- Cost of items not yet received<br>- Production date + Estimated completion + Completion date of all items <br>- Add more items (with order qty + cost)<br>- Delete "not received" item<br>- Note <br>- Attachments

### Row 18

- **C:** Closed
- **D:** Action: Close the PO after all processes, including payment, are completed.<br>Condition: No pending actions remain, and the PO is archived.
- **E:** NO

### Row 19

- **A:** Fulfilled Received
- **B:** The warehouse has received all items from the PO
- **C:** Closed
- **D:** Action: Close the PO after all processes, including payment, are completed.<br>Condition: No pending actions remain, and the PO is archived.
- **E:** NO
- **F:** The user can update:<br>- Production date + Estimated completion + Completion date of all items <br>- Note <br>- Attachments

### Row 20

- **A:** Any Status (except Partially Fulfilled, Fulfilled, Closed)
- **C:** Cancelled
- **D:** Action: Cancel the PO due to changes in requirements or other reasons.<br>Condition: Cancellation is authorized and communicated to stakeholders. The PO has received qty that couldn't be canceled. All the fields of the original PO are kept.
- **E:** NO

### Row 21

- **A:** Closed
- **B:** The PO is completed - no further action are required.
- **F:** Can't update anything

### Row 22

- **A:** Cancelled
- **B:** The PO is canceled for some reason → Do not record the data in the system for further calculation
- **F:** Just can delete PO

## Shipment status

### Row 1

- **A:** Status
- **B:** Meaning
- **C:** Next action
- **D:** Trigger event
- **E:** Allowed actions
- **F:** Required fields

### Row 2

- **A:** When creating a new shipment
- **C:** Scheduled/In transit/Delivered
- **D:** The system will use the expected arrival date from the shipment to calculate the estimated incoming stock.<br>When changing the status to "Delivered", the quantity in the "Ship From" warehouse is deducted from its stock.

### Row 3

- **A:** Scheduled
- **B:** The shipment is in progress - preparing - haven't shipped yet
- **C:** In transit / Delivered / Cancel
- **D:** For type "Warehouse transfer", When changing the status from "Scheduled" to "In transit" / "Delivered", The quantity in the "Ship From" warehouse is deducted from its stock,
- **E:** - For the type "Warehouse transfer", The user can update all fields<br>- For the type "Purchase order", the user can update all fields except ( vendor + order qty + cost since those fields are related to PO ID) + warehouse can edit if shipment status = schedule<br>- The user can delete shipment for both type
- **F:** - Shipping labels<br>- Item <br>- Expected arrival date

### Row 4

- **A:** In transit
- **B:** Shipment is being transported to the destination.
- **C:** Delivered
- **D:** - The shipment has been successfully delivered to the recipient and the recipient received all items. <br>- At least 1 item is received.
- **E:** - For the type "Warehouse transfer", The user can update all fields<br>- For the type "Purchase order", the user can update all fields except (warehouse + vendor + order qty + cost since those fields are related to PO ID)<br>- The user can't delete shipment for both type
- **F:** - Shipping labels<br>- Item <br>- Shipment Qty<br>- Expected arrival date

### Row 5

- **A:** Delivered
- **B:** The shipment is done<br>The "Ship to" warehouse receives all transferred items
- **C:** Closed
- **E:** - For the type "Warehouse transfer", The user can update all fields<br>- For the type "Purchase order", the user can update all fields except (warehouse + vendor + order qty + cost since those fields are related to PO ID)<br>- The user can't delete shipment for both type
- **F:** - Shipping labels<br>- Item <br>- Received Qty <br>- Shipment Qty<br>- Actual received date

### Row 6

- **A:** Schedule
- **C:** Canceled
- **D:** Action: Cancel the shipment due to changes in requirements or other valid reasons.<br>Condition: Cancellation is authorized and properly communicated to all relevant stakeholders.<br>Result: Upon cancellation, the stock levels in both the "Ship From" and "Ship To" warehouses must revert to their original states, as they were before the warehouse transfer initiation.

### Row 7

- **A:** Canceled
- **B:** The shipment is canceled
- **E:** Can't update anything

## Transfer Order Status

### Row 1

- **A:** Status
- **B:** Next status
- **C:** Trigger when
- **D:** Condition to change
- **E:** Allowed actions

### Row 2

- **B:** Scheduled
- **C:** Khi TO vừa được tạo hoặc đã Approved, nhưng chưa có Shipment hoặc tất cả Shipment = Scheduled/Cancelled.<br><br>Chưa phát sinh dịch chuyển tồn kho.
- **D:** "The required fields: <br>- TO ID<br>- Ship From<br>- Ship To <br>- Expected Arrival Date<br>- At least 1 item<br>Button [Created TO] sẽ disable cho đến khi các thông tin trên đc điền đầy đủ
- **E:** Can updated:<br>- Ship From<br>- Ship To<br>- Expected Arrival Date<br>- Item List (transfer qty)<br>- Note <br>- Attachments

### Row 3

- **A:** Scheduled
- **B:** In Transit
- **C:** Khi ít nhất 1 Shipment = In Transit, và còn Shipment chưa Delivered/Closed.<br><br>Tức đang có hàng trên đường đi.
- **E:** Can update:<br>- Expected Arrival Date<br>- Item List<br>- Note <br>- Attachments

### Row 4

- **B:** Cancelled
- **C:** when user click Cancel order.<br>Chỉ hợp lệ nếu:<br><br>Không có Shipment, hoặc<br><br>Tất cả Shipment = Cancelled.

### Row 5

- **A:** In Transit
- **B:** Partially Fulfilled
- **C:** Khi một số Shipment đã Delivered/Closed, nhưng tổng qty received < tổng qty planned.<br><br>Có thể song song vẫn còn Shipment In Transit.
- **E:** Can update:<br>- Expected Arrival Date<br>- Item List<br>- Note <br>- Attachments

### Row 6

- **B:** Fulfilled
- **C:** Khi tất cả qty planned đã được Delivered, tức sum(Shipment.received_qty) = sum(TO.requested_qty).<br><br>Nhưng còn Shipment ở trạng thái mở (chưa Close).
- **E:** Can update: <br>- Note <br>- Attachments

### Row 7

- **A:** In Transit/Partially Fulfilled
- **B:** Fulfilled
- **C:** "Khi tất cả qty planned đã được Delivered, tức sum(Shipment.received_qty) = sum(TO.requested_qty).<br><br>Nhưng còn Shipment ở trạng thái mở (chưa Close)."
- **E:** Can update: <br>- Note <br>- Attachments

### Row 8

- **A:** Fulfilled
- **B:** Closed
- **C:** Khi điều kiện Fulfilled đạt và tất cả Shipment liên quan đã Closed.<br><br>Không còn hành động nào khả thi.
- **E:** Can update: <br>- Note <br>- Attachments

### Row 9

- **A:** Cancelled
- **B:** -

## Shipment status of Transfer Order

### Row 1

- **A:** Status
- **B:** Next status
- **C:** Trigger when
- **D:** Validation

### Row 2

- **B:** Scheduled
- **C:** Khi shipment vừa được tạo<br>Chưa có tác động tồn kho.

### Row 3

- **A:** Scheduled
- **B:** In Transit
- **C:** Khi hàng đã rời kho nguồn.<br><br>Trigger: Mark as In Transit
- **D:** Source WH: On Hand giảm, In Transit tăng.<br><br>Shipment phải có ít nhất một line với qty_shipped > 0.

### Row 4

- **B:** Cancelled
- **C:** user cancel shipment

### Row 5

- **A:** In Transit
- **B:** Delivered
- **C:** Khi kho đích đã nhận đủ một phần hoặc toàn bộ số lượng shipment.<br>Trigger: Mark as Delivered
- **D:** Hệ thống ghi nhận:<br><br>Dest WH: On Hand tăng.<br><br>Source WH: In Transit giảm.<br><br>Cho phép partial receive → Shipment có thể Delivered với qty_received < qty_shipped.

### Row 6

- **A:** Delivered
- **B:** Closed
- **C:** Shipment đã hoàn tất, không còn qty outstanding.
- **D:** - Được close khi:<br>+ stt của shipment = Delivered

### Row 7

- **A:** Cancelled
- **B:** -
- **C:** Shipment bị hủy.<br><br>Trigger: Cancel Shipment.
- **D:** Điều kiện:<br><br>Shipment vẫn ở trạng thái Scheduled, chưa In Transit.<br><br>Nếu đã In Transit thì không hủy trực tiếp mà cần reverse transaction.<br><br>Không tác động tồn kho (nếu hủy trước khi ship).

## TRANSFER ORDER

### Row 1

- **A:** TRANSFER ORDER TABLE

### Row 2

- **A:** TO Status
- **B:** Impact từ Shipment
- **C:** Editable Fields
- **D:** Validation Rules
- **E:** Inventory Impact
- **F:** System Behavior / Notes

### Row 3

- **A:** Scheduled
- **B:** - Khi có shipment đầu tiên (Scheduled) → TO vẫn Scheduled
- **C:** ✅ transfer_qty editable
- **D:** - transfer_qty ≤ on_hand_from<br>- transfer_qty > 0
- **E:** ❌ Không ảnh hưởng tồn kho
- **F:** Đây là giai đoạn lên kế hoạch chuyển hàng giữa kho.

### Row 4

- **A:** In Transit
- **B:** - Khi ít nhất 1 shipment = In Transit<br>- Và còn shipment chưa Delivered/Closed
- **C:** ❌
- **D:** - Không chỉnh transfer_qty khi đã có shipment in transit
- **E:** ✅ Giảm tồn kho warehouse_from theo sum(shipment_qty)<br>✅ Tăng in_transit của warehouse_from
- **F:** Thể hiện hàng đang rời kho nguồn.

### Row 5

- **A:** Partially Fulfilled
- **B:** - Có ít nhất 1 shipment Delivered/Closed<br>- Còn shipment đang In Transit hoặc chưa ship (Scheduled)
- **C:** ❌
- **D:** - sum(received_qty) < transfer_qty
- **E:** ✅ Một phần hàng đã cộng vào warehouse_to <br>(Theo received_qty of shipment)<br>✅Giảm in_transit of warehouse_from (tương ứng)
- **F:** Hàng đang được nhận dần tại kho đích.

### Row 6

- **A:** Fulfilled
- **B:** - Tất cả shipment đã Delivered/Closed AND Received qty đủ
- **C:** ❌
- **D:** sum(received_qty) >= transfer_qty → TO status = Fulfilled
- **E:** ✅ Tồn kho giữa hai kho ghi nhận:<br>Giảm in_transit of warehouse_from<br>Tăng on_hand of warehouse_to
- **F:** TO hoàn tất, không thể thêm shipment mới.

### Row 7


### Row 8


### Row 9


### Row 10


### Row 11


### Row 12

- **A:** Case ID
- **B:** Condition
- **C:** Inventory Impact
- **D:** TO Status
- **E:** System Action / Rule (dev)
- **F:** Flags / Audit
- **G:** UI message

### Row 13

- **A:** 1
- **B:** Create TO: transfer_qty ≤ on_hand_from
- **C:** No immediate change
- **D:** Scheduled
- **E:** Allow create. <br>Validate transfer_qty > 0.
- **F:** audit create TO
- **G:** -

### Row 14

- **A:** 2
- **B:** Create TO: transfer_qty > on_hand_from
- **C:** -
- **D:** N/A (rejected)
- **E:** Reject create. Error.
- **F:** none
- **G:** Error: "Insufficient stock. Available {A}, Requested {R}."

### Row 15

- **A:** 3
- **B:** Create Shipment (Scheduled): shipment_qty ≤ transfer_qty and ≤ on_hand_from
- **C:** No immediate change until In Transit
- **D:** TO stays Scheduled
- **E:** Allow create. Mark shipment Scheduled.
- **F:** audit
- **G:** -

### Row 16

- **A:** 4
- **B:** Create Shipment: shipment_qty > transfer_qty and shipment_qty ≤ on_hand_from
- **C:** No immediate change until In Transit
- **D:** TO remains (or can be auto-updated later)
- **E:** create shipment
- **F:** audit
- **G:** -

### Row 17

- **A:** 5
- **B:** Create Shipment: shipment_qty > on_hand_from
- **C:** -
- **D:** Block
- **E:** Block creation. Hard rule.
- **F:** none
- **G:** Error: "Cannot create: available {A} < requested {S}."

### Row 18

- **A:** 6
- **B:** Shipment → In Transit (status change)
- **C:** on_hand_from -= shipment_qty<br><br>in_transit_from +=shipment_qty
- **D:** TO → In Transit (if ≥1 in transit)
- **E:** On status change do stock move and record inventory transaction. Can't shipment_qty edits after this.
- **F:** create stock-move audit
- **G:** -

### Row 19

- **A:** 7
- **B:** Receive (Delivered) partial: received_qty < shipment_qty
- **C:** on_hand_to += received_qty<br><br>in_transit_from -= received_qty
- **D:** TO → Partially Fulfilled (if total_received < total_planned)
- **E:** Accept partial receive. Update shipment.received_qty. <br>Keep shipment open or Delivered (per UX).
- **F:** audit receive
- **G:** -

### Row 20

- **A:** 8
- **B:** Receive equal: received_qty == shipment_qty and total_received == total_planned
- **C:** on_hand_to += received_qty
- **D:** TO → Fulfilled
- **E:** Accept. Update shipment.received_qty. If sum(received) == sum(transfer) → TO = Fulfilled.
- **F:** audit
- **G:** -

### Row 21

- **A:** 9
- **B:** Receive greater than shipment: received_qty > shipment_qty
- **C:** on_hand_to += received_qty
- **D:** TO → Fulfilled (after confirm)
- **E:** Warning and need to confirm
- **F:** none
- **G:** Warning: "Received {} exceeds shipped {}.<br>Record this as over-receive?

### Row 22

- **A:** 10
- **B:** After receives: sum(received) < sum(transfer) and no shipments in transit
- **C:** on_hand_to updated per receives
- **D:** Partially Fulfilled
- **E:** Compute totals; set TO status = Partially Fulfilled.
- **F:** audit

### Row 23

- **A:** 11
- **B:** After receives: sum(received) == sum(transfer)
- **C:** on_hand_to updated
- **D:** Fulfilled
- **E:** Compute totals; set TO status = Fulfilled.
- **F:** audit

### Row 24

- **A:** 12
- **B:** After receives: sum(received) > sum(transfer)
- **C:** on_hand_to updated
- **D:** TO = Fulfilled
- **F:** set flags; audit; notify
- **G:** Highlight: received_qty > transfer_qty

## SHIPMENT OF TO

### Row 1

- **A:** SHIPMENT TABLE

### Row 2

- **A:** Shipment Status
- **B:** Editable Fields
- **C:** Validation Rules
- **D:** Inventory Impact
- **E:** Impact lên TO
- **F:** System Behavior / Notes

### Row 3

- **A:** Scheduled
- **B:** ✅ shipment_qty editable<br>❌ received_qty
- **C:** - shipment_qty ≤ on_hand_from (hard)<br>- shipment_qty > 0
- **D:** ❌ Chưa trừ kho
- **E:** TO vẫn Scheduled (nếu tất cả shipment = Scheduled)
- **F:** Shipment ở giai đoạn chuẩn bị, chưa trừ tồn kho.

### Row 4

- **A:** In Transit
- **B:** ❌ shipment_qty<br>✅ received_qty (optional)
- **C:** - received_qty < = shipment_qty<br>- Không được chỉnh shipment_qty nữa<br>- Received_qty > = 0 (cho phép nhập 0 khi shipment chưa nhận)
- **D:** ✅ Giảm tồn kho warehouse_from (on_hand_from -= shipment_qty)<br>✅ + in_transit_from += shipment_qty
- **E:** TO → In Transit
- **F:** Biểu thị hàng đang trên đường đi.

### Row 5

- **A:** Delivered
- **B:** ✅ received_qty editable
- **C:** - received_qty < = shipment_qty<br>- Received_Qty > = 0
- **D:** ✅ Cộng tồn kho warehouse_to (on_hand_to += received_qty)<br>✅ - in_transit_from (received_qty)
- **E:** TO có thể là Partially Fulfilled nếu chưa nhận đủ
- **F:** Cho phép nhận từng phần.

### Row 6

- **A:** Closed
- **B:** ❌ tất cả fields
- **D:** ❌ Không còn tác động tồn kho
- **F:** Shipment kết thúc, không thể chỉnh sửa hoặc reopen.

### Row 7


### Row 8


### Row 9


### Row 10

- **A:** RELATION RULES GIỮA TO & SHIPMENT (Qty Relationship)

### Row 11

- **A:** Field
- **B:** Source to update
- **C:** Rule
- **D:** Type
- **E:** System Behavior / Notes

### Row 12

- **A:** transfer_qty
- **B:** User nhập tại TO
- **C:** ≤ on_hand_from
- **D:** Hard
- **E:** Không thể tạo TO vượt tồn kho thực tế.

### Row 13

- **A:** shipment_qty
- **B:** User nhập tại Shipment
- **C:** ≤ on_hand_from
- **E:** Khồn cần validate với transfer_qty

### Row 14

- **A:** received_qty
- **B:** User nhập tại Shipment (In Transit/Delivered/Closed)
- **C:** ≤ shipment_qty or > shipment_qty
- **E:** Cho phép nhận vượt với flag over-receive để reconcile sau.

## inventory impact TO

### Row 1

- **A:** Shipment status
- **B:** From Warehouse (nguồn)
- **C:** To Warehouse (đích)
- **D:** Notes / hành xử

### Row 2

- **A:** Scheduled (shipment lập xong, chưa ship)
- **B:** On Hand: no change<br>In Transit Outbound: 0<br>In Transit Inbound: 0<br>On Order: no change<br>On Hold: no change
- **C:** On Hand: no change<br>In Transit Inbound: 0<br>In Transit Outbound: 0<br>On Order: (PO only) may already show On Order if PO created
- **D:** Chỉ là plan

### Row 3

- **A:** In Transit (đã shipped, đang vận chuyển)
- **B:** On Hand ↓ (trừ thực tế khi ship) <br>In Transit Outbound ↑ = shipment_qty<br>On Order: - <br>On Hold: -
- **C:** In Transit Inbound ↑ = shipment_qty <br>On Hand: no change (chưa tăng) <br><br><br>On Order: (PO case) may still show On Order until receive
- **D:** Nếu partial ship: update shipped_qty, <br>in_transit = shipped - received. <br>From đã giảm On Hand ngay khi ship. <br>To thấy inbound amount.

### Row 4

- **A:** Delivered (to warehouse đánh dấu received / hoàn tất từng shipment)
- **B:** On Hand: (no change additional, đã giảm khi ship) <br>In Transit Outbound: decrease theo received_qty (có thể =0 nếu fully received) <br>On Hold: -
- **C:** In Transit Inbound: decrease theo received_qty <br>On Hand: increase theo received_qty <br><br>On Order: (PO) decrease corresponding received_qty
- **D:** Partial receives: mỗi lần receive → From.InTransitOut -= r_qty, <br>To.InTransitIn -= r_qty, To.OnHand += r_qty

### Row 5

- **A:** Closed (TO/shipment closed / archived)
- **B:** In Transit Outbound: 0 (should be 0; mọi in-transit đã resolved or adjusted) <br>On Hand: unchanged <br>On Hold: unchanged
- **C:** In Transit Inbound: 0 <br>On Hand: reflects final received_qty <br>On Order: PO closed if all received
- **D:** Close = trạng thái cuối; nếu còn discrepancy phải create adjustment documents (returns, lost, correction).

## Inventory Impact PO

### Row 1

- **A:** Scenario
- **B:** On Order
- **C:** On Hand

### Row 2

- **A:** PO is Open
- **B:** Increases (Order Qty)
- **C:** –

### Row 3

- **A:** Shipment In Transit
- **B:** -
- **C:** –

### Row 4

- **A:** Shipment Delivered
- **B:** Decreases (Received Qty)
- **C:** Increases (Received Qty)

### Row 5

- **A:** PO becomes Partially Fulfilled
- **B:** Remaining On Order<br>Order_Qty - Receive_qty
- **C:** Increases (Received Qty)

### Row 6

- **A:** PO becomes Fulfilled
- **B:** 0
- **C:** All items added

### Row 7

- **A:** Shipment Canceled
- **B:** Restore depending on config
- **C:** No on-hand change

### Row 8

- **C:** Increases (Received Qty)

### Row 9


### Row 10


### Row 11


### Row 12

- **A:** Note: Nếu điều chỉnh on order qty thì việc sử dụng số liệu on order vào ATS phải được + từ on order & in transit (upcoming)


