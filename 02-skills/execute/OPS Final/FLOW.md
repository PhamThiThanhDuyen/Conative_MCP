# Flow OPS Summary

Mục tiêu: chạy API Summary, dùng kết quả kiểm tra có sẵn trong Postman và ghi
vào Google Sheet. Luôn làm xong Variant trước khi chuyển sang Product.

```text
Đọc Google Sheet
  ↓
Nhận organization + source + timerange
  ↓
Đối chiếu Danh sách org và chuẩn bị cột mới ở hai tab
  ↓
Postman: Login → tìm organization ID → Choose_Org
  ↓
Kiểm tra Authorization và token đã được script truyền
  ↓
Summary_Variant → Sales_by_variant → nhập 3 input → Send
  ↓
Đọc console của lần chạy Variant
  ↓
Ghi Sales_by_variant: Passed / Failed + note / N/A → đọc lại
  ↓
Summary_Product → Sales_by_product → nhập cùng 3 input → Send
  ↓
Đọc console của lần chạy Product
  ↓
Ghi Sales_by_product: Passed / Failed + note / N/A → đọc lại
  ↓
Báo kết quả hai tab
```

Ở bất kỳ bước nào bị kẹt: dừng tại bước đó → giữ browser in-app mở → hỏi
người dùng hỗ trợ → xác minh lại màn hình/input → tiếp tục đúng bước đang dở.

## I. Đọc tài liệu và nhận input

1. Đọc metadata workbook trong [run-settings.md](references/run-settings.md).
   Xác minh ba tab `Danh sách org`, `Sales_by_variant`, `Sales_by_product` tồn tại.
2. Đọc header và dữ liệu hiện tại. Trong hai tab kết quả, tìm cột `Name`, `Key`,
   dòng metric và cột kiểm tra ngoài cùng bên phải.
3. Nhận organization, source và timerange từ người dùng. Chỉ hỏi phần thiếu;
   dùng [mẫu input](assets/run-input-template.md) khi cần.
4. Đối chiếu organization/source với `Danh sách org`. `Channel` là tên hiển thị;
   `from_source` là giá trị gửi API. Không tự đổi tên organization hoặc source.
5. Xác minh ngày hợp lệ, from_date không sau to_date. API dùng `YYYY-MM-DD`;
   header dùng tên tháng tiếng Anh. Chưa rõ ngày tương đối hoặc timezone ảnh
   hưởng cách hiểu timerange thì hỏi trước khi chạy.

## II. Tạo cột cho lần kiểm tra

Tạo một cột mới trong mỗi tab kết quả, ngay sau cột kiểm tra cuối của từng tab.
Hai tab có lịch sử khác nhau nên vị trí cột có thể khác nhau. Không lấy cột
Variant để áp sang Product. Nếu còn cột khác ở bên phải như `AI Chat`, chèn
cột thật sự để đẩy cột đó sang phải, không ghi đè.

Thêm dropdown cho các ô status, giống cột kiểm tra trước trong cùng tab.
Làm theo [quy tắc dropdown](references/sheet-contract.md#dropdown-status).

Header chung cho hai tab:

```text
<organization> - <source hiển thị> Summary
<MMM dd, yyyy> - <MMM dd, yyyy>
Kiểm tra ngày <MMM dd yyyy>
```

Ví dụ theo input minh họa, ngày kiểm tra giả định Nov 08 2026:

```text
Mizmooz - Magento Summary
Jan 01, 2026 - Oct 21, 2026
Kiểm tra ngày Nov 08 2026
```

Ngày kiểm tra lấy lúc bắt đầu lần chạy theo `Asia/Ho_Chi_Minh`; không dùng
ngày ví dụ cố định. Hai tab dùng cùng header trong một lần chạy, kể cả khi
chạy qua nửa đêm. Lần chạy mới cùng ngày vẫn tạo cột mới. Khi tiếp tục lần
chạy đang dở, dùng lại cột đã xác minh của lần đó.

## III. Chọn organization trong Postman

Làm theo [execute-api-ops.md](execute-api-ops.md): chọn đúng workspace,
collection, environment; chạy Login và Choose_Org; xác minh organization
và cơ chế truyền token. Không chọn organization theo vị trí trong danh sách.

## IV. Chạy Variant và ghi kết quả

1. Mở `Final / Summary_Variant / Summary_Variant`.
2. Kiểm tra Authorization đang dùng biến `accessToken_Mizmooz`, biến đã có giá
   trị từ lần Choose_Org vừa hoàn tất, không phải token cũ hoặc biến chưa resolve.
3. Nếu chưa thấy query, dùng chức năng load/reload query/schema hiện có.
4. Chọn query `Sales_by_variant`, truyền from_date, to_date, from_source.
5. Kiểm tra lại request và script, sau đó Send một lần; chờ các kiểm tra hoàn tất.
6. Đọc console/test result đúng lần chạy và đúng request.
7. Áp dụng [quy tắc kết quả](references/result-rules.md), ghi vào cột Variant mới
   bằng [skill ghi Sheet](skill/record-ops-summary-results/SKILL.md), rồi đọc lại.

## V. Chạy Product và ghi kết quả

Sau khi Variant đã ghi và xác minh, mở `Final / Summary_Product /
Summary_Product`, kiểm tra Authorization, load query `Sales_by_product`,
truyền cùng input. Send một lần, chờ script xong, đọc console riêng của
Product và ghi vào cột mới trong `Sales_by_product`. Không dùng lại console
hoặc danh sách metric Variant cho Product.

## VI. Kết thúc hoặc tiếp tục khi bị kẹt

Báo kết quả theo [mẫu báo cáo](assets/run-report-template.md). Failed của metric
không chặn Product; lỗi đăng nhập, query, script, mapping hoặc ghi Sheet thì có.
Nếu Product chưa chạy, báo “Chưa chạy”; để trống cột Product, không điền N/A.

Khi bị kẹt, báo tab/request, bước lỗi, điều đã kiểm tra và phần cần người dùng
hỗ trợ. Nếu đang dùng connector mà không có browser mở, mở workbook hoặc
Postman trong browser in-app có hiển thị để người dùng xem. Chờ người dùng
phản hồi, giữ nguyên browser. Không tự Send lại khi chưa biết request trước
đã chạy hay chưa; kiểm tra kết quả hiện tại trước khi tiếp tục.

## Chỗ thường cần chỉnh

| Muốn chỉnh gì | Sửa ở đâu |
| --- | --- |
| Tên workspace, collection, environment, request | references/run-settings.md |
| Thao tác Login, Choose_Org, query, console | execute-api-ops.md |
| Vị trí cột, header và phạm vi ghi | references/sheet-contract.md và phần II ở trên |
| Tick xanh/đỏ, mapping metric, note | references/result-rules.md |
| Cách báo kết quả | assets/run-report-template.md |
