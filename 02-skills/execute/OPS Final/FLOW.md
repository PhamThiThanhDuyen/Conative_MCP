# Flow tổng OPS — Summary và List

Chạy xong từng org rồi mới sang org tiếp theo. Trong mỗi org/source, làm đủ
Summary và List của Variant trước, sau đó mới làm tương tự cho Product.

```text
Đọc Sheet → nhận danh sách org/source/timerange theo thứ tự
  ↓
Chọn org hiện tại trong Postman → xác minh org và token
  ↓
Summary Variant → ghi Sheet Sales_by_variant (cột Summary) → đọc lại
  ↓
List Variant, từng API đủ 5 trang → ghi Sheet sau mỗi API (cột List)
  → xong folder → chốt N/A → đọc lại cả cột
  ↓
Summary Product → ghi Sheet Sales_by_product (cột Summary) → đọc lại
  ↓
List Product, từng API đủ 5 trang → ghi Sheet sau mỗi API (cột List)
  → xong folder → chốt N/A → đọc lại cả cột
  ↓
Xác minh bốn chặng của org/source đã hoàn tất
  ↓
Org còn source được yêu cầu? → lặp bốn chặng cho source đó
  ↓
Xong org hiện tại → Choose_Org cho org tiếp theo → lặp lại
  ↓
Báo kết quả theo org/source và từng chặng
```

Mặc định yêu cầu chạy flow tổng là chạy đủ cả Summary và List. Không hỏi lại
chế độ đã được xác định trong flow này. Nếu người dùng chỉ yêu cầu Summary,
List hoặc một chặng, chỉ chạy phần đó và giữ thứ tự tương đối ở trên.

## I. Đọc tài liệu và nhận input

1. Đọc metadata workbook trong [run-settings.md](references/run-settings.md).
   Xác minh ba tab `Danh sách org`, `Sales_by_variant`, `Sales_by_product`.
2. Nhận danh sách org theo thứ tự và source/timerange cho từng org.
   Nếu cùng scope áp dụng cho cả danh sách, dùng đúng scope đó. Chỉ hỏi phần
   thiếu; không lấy toàn bộ org/source trong Sheet làm phạm vi mặc định.
3. Đối chiếu từng cặp org/source với `Danh sách org`. `Channel` là tên hiển thị;
   `from_source` là giá trị API. Không tự gộp alias hoặc chọn org gần giống.
4. API dùng ngày `YYYY-MM-DD`; kiểm tra from_date không sau to_date.
   Nếu ngày tương đối hoặc timezone làm timerange chưa rõ, hỏi trước khi chạy.
5. Với mỗi org/source, giữ một mốc bắt đầu run theo `Asia/Ho_Chi_Minh` cho
   header của bốn chặng. Khi resume, giữ lại mốc và cột đã tạo của run đó.

## II. Chuẩn bị cột kết quả

Flow đầy đủ tạo hai cột riêng ở mỗi tab: một Summary, một List.
Tạo cột trước chặng tương ứng hoặc dùng lại đúng cột của run đang dở.
Không ghi List vào cột Summary; không lấy kết quả org trước cho org mới.

Chèn sau cột kiểm tra cuối của từng tab. Nếu bên phải có `AI Chat`, đẩy cột
đó sang phải. Copy định dạng và dropdown theo
[sheet-contract.md](references/sheet-contract.md); không copy status/note cũ.
Chặng chưa chạy thì ô kết quả để trống.

Header Summary:

```text
<tên org> - <tên source> Summary
<MMM dd, yyyy> - <MMM dd, yyyy>
Kiểm tra ngày <MMM dd yyyy hh:mm<AM/PM>>
```

Header List:

```text
<tên org> - <tên source> List
<MMM dd, yyyy> - <MMM dd, yyyy>
Kiểm tra ngày <MMM dd yyyy hh:mm<AM/PM>>
```

Ví dụ header List, ngày giờ giả định:

```text
Mizmooz - Magento List
Jan 01, 2026 - Oct 21, 2026
Kiểm tra ngày Nov 08 2026 08:30PM
```

Một folder List dùng chung một cột cho các API/offset của folder đó.
Ghi lại địa chỉ theo org/source/timerange/chặng; hai tab có thể khác vị trí.
Lần kiểm tra mới tạo cột mới; resume không tạo cột trùng dù header giống nhau.

## III. Chọn org hiện tại

Dùng nguyên phần 1–2 [execute-api-ops.md](execute-api-ops.md): chọn workspace,
collection, environment, Login, tìm ID đúng org, Choose_Org và kiểm tra token.
Giữ session khi còn hợp lệ; chuyển org phải Choose_Org và xác minh lại.
Trước mỗi chặng vẫn kiểm tra org, token, source, timerange trong request.

## IV. Summary Variant → ghi Sheet

Chạy `Final / Summary_Variant / Summary_Variant`, query `Sales_by_variant`,
theo phần 3 [execute-api-ops.md](execute-api-ops.md). Ghi và đọc lại status,
note, dropdown trong cột Summary của `Sales_by_variant` bằng
[skill ghi Sheet](skill/record-ops-summary-results/SKILL.md).
Xong bước ghi và xác minh mới sang List Variant.

## V. List Variant → ghi Sheet

Theo [execute-api-list.md](execute-api-list.md), chạy mọi API trong `List_Variant`,
bắt đầu `Variant_List_Product_Info`. Mỗi API limit 20, offset 0, 20, 40, 60, 80
ở query và script; xác minh đã kiểm tra 100 variant khác nhau.
Đủ năm trang → gộp console → ghi và đọc lại cột List Variant → sang API tiếp.
Giữ Failed xuyên trang/API. Xong toàn bộ folder mới chốt N/A và đọc lại cả cột.
Chưa hoàn tất bước này thì chưa chạy Summary Product hoặc org tiếp theo.

## VI. Summary Product → ghi Sheet

Sau khi cả hai chặng Variant đã lưu và xác minh, chạy `Final / Summary_Product /
Summary_Product`, query `Sales_by_product`, theo phần 4
[execute-api-ops.md](execute-api-ops.md). Ghi cột Summary trong `Sales_by_product`
và đọc lại. Xác minh xong mới sang List Product.

## VII. List Product → ghi Sheet

Chạy từng API trong `Final / List_Product`, query `Sales_by_product` theo
[execute-api-list.md](execute-api-list.md). Mỗi API cũng đủ 5 offset, kiểm tra
100 product, ghi và xác minh sau mỗi API. Xong folder mới chốt N/A,
đọc lại cả cột List Product.

## VIII. Xong org hiện tại rồi mới chuyển org

- Xác minh đủ bốn chặng: Summary Variant, List Variant, Summary Product,
  List Product. Mỗi chặng phải có kết quả đã lưu và đọc lại trong đúng cột.
- Nếu org có nhiều source được yêu cầu, làm xong bốn chặng của từng source
  trước khi chuyển org. Không tự mở rộng sang source chưa được yêu cầu.
- Sang org kế theo danh sách người dùng: Choose_Org, xác minh tên/ID, token,
  từ đầu đặt lại input và offset; tạo cột riêng cho org/source mới.
- Không tổng hợp Failed/N/A/console từ org hoặc source trước sang org mới.
- Báo kết quả theo [mẫu báo cáo](assets/run-report-template.md).

## IX. Nếu bị kẹt

Giữ browser in-app mở tại bước lỗi, nêu org/source/chặng/API/offset, phần đã
lưu và phần cần hỗ trợ. Chờ người dùng, không tự sang chặng hoặc org kế.
Nếu connector đang dùng không có browser mở, mở Postman/Sheet in-app để
người dùng kiểm tra. Resume đúng bước/cột; lỗi lưu Sheet thì đọc lại và ghi
tiếp bằng kết quả đã có, không tự chạy lại API.

Metric Failed không chặn chặng tiếp theo nếu đã kiểm tra đầy đủ, ghi và đọc
lại xong. Lỗi thực thi, thiếu coverage, mapping chưa rõ hoặc chưa lưu được
thì dừng. Chưa chạy để trống, không điền N/A thay kết quả chưa có.

## Chỗ thường cần chỉnh

| Muốn chỉnh gì | Sửa ở đâu |
| --- | --- |
| Thứ tự chặng và chuyển org | FLOW.md và SKILL.md |
| Workspace, collection, environment, request | references/run-settings.md |
| Login, Choose_Org, Summary | execute-api-ops.md |
| List, offset query/script, thứ tự API | execute-api-list.md |
| Cột, header, dropdown | references/sheet-contract.md và phần II ở trên |
| Status, mapping, note | references/result-rules.md |
| Input và báo cáo | assets/run-input-template.md, assets/run-report-template.md |
