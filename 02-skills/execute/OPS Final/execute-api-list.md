# Chạy API List cho Variant và Product

Đọc [cấu hình](references/run-settings.md), [Sheet](references/sheet-contract.md)
và [quy tắc kết quả](references/result-rules.md) trước khi chạy.
Đây là thao tác List cho từng chặng trong [flow tổng](FLOW.md).
List Variant chạy sau khi Summary Variant đã ghi và đọc lại Sheet.
List Product chạy sau khi Summary Product đã ghi và đọc lại Sheet.
Nếu chỉ được yêu cầu List, dùng đúng phần List, giữ thứ tự Variant → Product.

## 1. Chuẩn bị

1. Xác minh organization, source, from_date, to_date và chặng List hiện tại.
2. Tạo cột List trong tab của chặng hiện tại, sau cột kiểm tra cuối; hoặc
   dùng lại cột List của run đang dở. Giữ dropdown như cột mẫu.
   Không ghi vào cột Summary đã dùng trước đó.
3. Dùng mốc bắt đầu run org/source theo Asia/Ho_Chi_Minh, giữ cùng mốc với
   chặng Summary trước đó trong flow tổng:

```text
<tên org> - <tên source> List
<MMM dd, yyyy> - <MMM dd, yyyy>
Kiểm tra ngày <MMM dd yyyy hh:mm<AM/PM>>
```

Ví dụ: `Mizmooz - Magento List`, `Jan 01, 2026 - Oct 21, 2026`,
`Kiểm tra ngày Nov 08 2026 08:30PM` trên ba dòng cùng ô.

4. Dùng nguyên các bước chọn workspace, collection, environment, `Login`,
   `Choose_Org` ở phần 1–2 của [execute-api-ops.md](execute-api-ops.md).
   Không đổi cấu hình auth hoặc script truyền token.
5. Đọc danh sách request thực tế trong `Final / List_Variant` và
   `Final / List_Product`. Ghi nhận tên/path và thứ tự để không bỏ sót API.
   Chưa biết tên các API còn lại thì đọc từ folder, không tự đoán tên.

## 2. Variant — API đầu tiên

1. Mở `Final / List_Variant / Variant_List_Product_Info`.
2. Mở Authorization. Kiểm tra token đã được truyền vào biến
   `accessToken_Mizmooz` sau Choose_Org, đã resolve và không bị giá trị cũ
   ở scope khác ghi đè. Không chép token ra chat/file/Sheet.
3. Nếu query chưa load thì dùng load/reload query/schema hiện có.
4. Chọn query `Sales_by_variant`, đặt from_date, to_date, from_source như
   flow Summary. Kiểm tra đúng organization, source và timerange.
5. Đọc query và script để tìm limit/offset thực sự dùng cho request GraphQL
   và request đối chiếu. Kiểm tra request và request phụ chỉ đọc dữ liệu.
   Giữ nguyên field list, filter và logic kiểm tra.

## 3. Chạy đủ 100 variant cho API này

| Lần Send | Limit | Offset trong query | Offset trong script |
| --- | --- | --- | --- |
| 1 | 20 | 0 | 0 |
| 2 | 20 | 20 | 20 |
| 3 | 20 | 40 | 40 |
| 4 | 20 | 60 | 60 |
| 5 | 20 | 80 | 80 |

Ở mỗi dòng trong bảng:

1. Đặt cùng offset vào query/GraphQL variables và tham số phân trang trong
   script đang dùng để gọi API đối chiếu. Nếu dùng chung một biến thì cập nhật
   biến đó và xác minh cả hai nơi resolve đúng; không tạo thêm hằng số riêng.
2. Chỉ sửa offset phục vụ phân trang; không sửa index vòng lặp, công thức,
   tolerance, điều kiện pass/fail hoặc script auth. Không Save collection.
3. Trước Send, kiểm tra limit 20 và offset đã khớp ở cả hai phía. Nếu không
   xác định được vị trí offset trong script, hỏi người dùng; không tìm/thay
   toàn bộ số 0/20 trong script.
4. Mở console, phân biệt log theo tên API, offset và mốc Send. Send đúng một
   lần cho trang đó, chờ response và các request phụ/script hoàn tất.
5. Ghi nhận tick xanh/đỏ, tên metric và nguyên văn dòng lỗi cho trang này.
   Không clear log nếu chưa giữ đủ phần kết quả cần gộp; không export auth log.
6. Kiểm tra 20 item thực sự được script đối chiếu, không chỉ nhìn HTTP 200.
   Đối chiếu ID/key ổn định và thứ tự phân trang để tránh kiểm tra trùng item.
   Giữ cùng sort/filter cho cả năm trang; không tự thêm sort mới khi chưa rõ.

Offset 0 phải được Send trước khi tăng lên 20. Xong 80 là đủ năm trang,
không chạy tiếp 100. Chỉ báo đã kiểm tra 100 khi xác minh 100 item khác nhau
đã được kiểm tra và script không bỏ qua item.

Nếu dataset dưới 100, trang thiếu/rỗng, item bị lặp hoặc script chỉ so sánh một
phần trang, báo số thực tế và hỏi người dùng cách tiếp tục. Không dùng dữ liệu
giả, không tự coi đã đủ 100 và không dùng N/A thay cho thiếu coverage.
Tick đỏ metric vẫn là kết quả hợp lệ; lỗi network/auth/GraphQL/runtime script
hoặc không có log kiểm tra thì dừng ở trang đó để hỏi người dùng.

## 4. Ghi Sheet sau API, rồi làm API tiếp theo

1. Xong đủ năm trang của `Variant_List_Product_Info`, tổng hợp kết quả cả năm
   trang. Dùng [skill ghi Sheet](skill/record-ops-summary-results/SKILL.md).
2. Ghi metric đã kiểm tra vào cột List của Variant. Có ít nhất một đỏ ở bất
   kỳ item/trang nào → Failed; note giữ dòng đỏ và thông tin API/offset.
   Chưa xong folder thì để trống metric chưa được kiểm tra, chưa ghi N/A.
3. Đọc lại status, note, dropdown. Chỉ sau khi xác minh đã lưu mới sang API sau.
4. Với từng API còn lại trong `List_Variant`, lặp lại các bước trên: kiểm tra
   Authorization/query/input, bắt đầu lại offset 0, chạy đến 80, rồi ghi Sheet.
   Không dùng offset 80 của API trước làm trang bắt đầu của API sau.
5. Mọi API trong cùng tab dùng cùng cột List. Gộp thêm kết quả, giữ Failed và
   note từ API trước. Xanh ở API sau không xóa lỗi của API trước.
6. Xong toàn bộ folder, điền N/A cho metric không có trong kết quả của bất kỳ
   API nào. Đọc lại toàn cột và xác minh số ô kết quả khớp số dòng metric.

Helper tùy chọn [build_list_result_plan.py](scripts/build_list_result_plan.py)
hỗ trợ gộp từng API vào kế hoạch ghi; xem [input helper](references/result-plan.md).

## 5. Product

Trong flow tổng, xong List Variant thì quay về [FLOW.md](FLOW.md) để chạy
Summary Product và ghi, đọc lại Sheet trước. Sau đó mới mở `Final / List_Product`.
Nếu chỉ được yêu cầu List, sau khi List Variant lưu và xác minh xong có thể
tiếp tục List Product. Làm từng API theo thứ tự folder, dùng query `Sales_by_product`
và cột List trong tab `Sales_by_product`.

Mỗi API Product cũng chạy limit 20, offset 0, 20, 40, 60, 80 trong query và
script; xong năm trang mới ghi Sheet rồi sang API tiếp theo. Kiểm tra 100
product khác nhau, không dùng số lượng hoặc console Variant để suy ra Product.
Cuối folder Product mới chốt N/A và đọc lại cả cột. Trong flow tổng, xác minh
đủ bốn chặng đã lưu cho org/source hiện tại rồi mới sang org tiếp theo.

## 6. Khi bị kẹt hoặc tiếp tục run đang dở

Giữ browser in-app mở tại bước lỗi. Báo mode, tab, API, offset, input đã kiểm
tra và phần cần người dùng hỗ trợ; chờ phản hồi. Resume đúng trang đang dở,
dùng lại cột và timestamp của run, giữ kết quả trước đó.
Không tự chuyển chặng hoặc org khi bước hiện tại còn bị kẹt.
Trước khi Send lại, xác minh trang đó đã hoàn tất hay chưa; không trộn hai
lần thử hoặc tự tạo cột mới. Nếu chỉ lỗi ghi Sheet, đọc lại và ghi tiếp cùng
cột bằng kết quả đã có, không chạy API lại.
