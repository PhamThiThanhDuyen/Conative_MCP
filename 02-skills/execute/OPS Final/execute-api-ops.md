# Chạy API Summary trên Postman

Với List, dùng [execute-api-list.md](execute-api-list.md). Các bước chọn
workspace, collection, environment, Login và Choose_Org ở phần 1–2 dưới đây
được dùng chung, không thay đổi.

Đọc [cấu hình](references/run-settings.md) và nhận đủ input trước khi Send.
Dùng request và script đã có; không tự viết lại logic so sánh.

Trong flow tổng [FLOW.md](FLOW.md), thứ tự là Summary Variant → ghi và đọc
lại Sheet → List Variant → ghi và đọc lại Sheet → Summary Product → ghi và
đọc lại Sheet → List Product → ghi và đọc lại Sheet → org tiếp theo.
Tài liệu này mô tả thao tác Summary; không tự chuyển sang Product ngay sau
Summary Variant khi đang chạy flow tổng.

## 1. Mở Postman và chọn môi trường

1. Mở hoặc dùng lại Postman web trong browser in-app có hiển thị.
2. Chọn workspace `DUYENQA_GraphQL`.
3. Chọn collection `Duyen_GraphQL_Live`, environment `OpenSearch_Duyen`.
4. Mở folder `Final`. Xác minh các request có đúng tên trong cấu hình.

Flow này cần thao tác Send, GraphQL query và console/script output của
Postman. Connector có thể giúp đọc resource nếu hỗ trợ, nhưng không thay
thế bằng một run monitor/collection khác. Nếu connector không cung cấp đúng
thao tác, tiếp tục bằng browser in-app. Không dùng collection runner để chạy
toàn bộ collection.

## 2. Login và chọn organization

1. Trong `Final / SignIn`, mở `Login`. Kiểm tra endpoint/environment thuộc
   luồng đăng nhập đã được người dùng cho phép. Yêu cầu thực thi flow này đã
   xác định rõ việc Send Login; chỉ hỏi thêm nếu có endpoint hoặc tài khoản
   khác chưa được phép. Nếu cần đăng nhập tương tác, để người dùng nhập bí mật.
2. Click Send một lần. Trong response, tìm phần `organizations`.
3. Tìm organization đúng yêu cầu và lấy `id`. Đối chiếu tên thực tế với
   `Danh sách org`; nếu chỉ có alias, trùng tên hoặc không thấy organization,
   dừng hỏi người dùng. Không lấy ID ở cấp response khác.
4. Mở `Choose_Org`. Thay phần organization ID ngay sau `switch-organization/`
   theo URL có sẵn. Giữ nguyên host, path khác và cấu hình request.
5. Click Send một lần. Kiểm tra response đã chọn đúng organization và script
   post-response chạy thành công. Response thành công nhưng không xác minh
   được organization thì chưa chuyển sang query.
6. Để script hiện có truyền token. Không copy/paste hoặc xuất token ra chat,
   file hay Sheet. Không sửa script hoặc Save thêm token thủ công.

## 3. Chạy Summary Variant

1. Mở folder `Summary_Variant`, request `Summary_Variant`.
2. Trong Authorization, kiểm tra cấu hình dùng `accessToken_Mizmooz` theo
   request có sẵn. Xác minh biến có giá trị sau Choose_Org, đã resolve và
   không bị token literal/biến ở scope khác ghi đè. Chỉ kiểm tra trạng thái,
   không chép hoặc chụp giá trị token. Nếu chưa được truyền, xem lỗi script
   Choose_Org rồi hỏi người dùng, không tự thay tên biến.
3. Vào phần GraphQL query. Nếu chưa load, dùng load/reload query/schema có sẵn;
   không tự sửa schema, endpoint hay gửi query khác để dò.
4. Chọn query `Sales_by_variant`. Đọc query/variables hiện tại rồi đặt:
   - `from_date`: ngày bắt đầu dạng YYYY-MM-DD.
   - `to_date`: ngày kết thúc dạng YYYY-MM-DD.
   - `from_source`: đúng giá trị từ dòng organization/source trong Sheet.
5. Nếu input nằm trong GraphQL variables, cập nhật variables; nếu nằm trực tiếp
   trong query, cập nhật đúng arguments tương ứng. Không sửa chỉ dựa vào tên
   biến nếu query không tham chiếu biến đó. Giữ nguyên field list và filter khác.
6. Xác minh organization, environment, query, ba input và request là truy vấn
   đọc dữ liệu. Đọc script đủ để biết các request phụ chỉ phục vụ so sánh.
7. Mở Postman Console, phân biệt/clear log cũ nếu cần và ghi nhận mốc bắt đầu.
   Không export toàn bộ console vì có thể chứa auth headers.
8. Click Send một lần. Chờ response và tất cả script/request phụ hoàn tất.
   Các request phụ do script có sẵn chạy là một phần của lần Send này.
9. Xác minh không có lỗi network/auth/GraphQL hoặc script chưa chạy xong.
   HTTP 200 có `errors` hoặc console chỉ có log dở dang chưa phải lần chạy hợp lệ.
10. Đọc tick xanh/đỏ và thông báo metric trong console/test result đúng lần chạy,
    giữ tên metric và dòng lỗi gốc. Làm theo
    [result-rules.md](references/result-rules.md), ghi và xác minh Variant.

Test assertion đỏ của một metric là kết quả Failed cần ghi, không phải lý do
dừng run. Chỉ lỗi thực thi script như exception làm mất các kiểm tra còn lại,
request phụ lỗi hoặc chưa hoàn tất mới khiến kết quả chưa đủ để ghi cả tab.

## 4. Chạy Summary Product

Trong flow tổng, chỉ sau khi cả Summary Variant và List Variant đã lưu,
đọc lại xong mới chạy bước này. Nếu chỉ được yêu cầu Summary thì sau khi
Summary Variant lưu xong có thể tiếp tục Summary Product.
Mở folder `Summary_Product`, request
`Summary_Product`, query `Sales_by_product`. Lặp lại phần 3 với cùng
organization, from_source, from_date, to_date. Kiểm tra token và input ở
request Product, không giả định chúng giống request Variant.

Không Login hoặc Choose_Org lại khi session vẫn đúng và còn hiệu lực.
Token hết hạn hoặc organization thay đổi thì xử lý đúng bước auth, rồi kiểm tra
lại input trước khi tiếp tục. Không dùng kết quả Variant làm kết quả Product.

Ghi và xác minh Summary Product xong thì quay về flow tổng để chạy List
Product. Chỉ chuyển org sau khi cả bốn chặng đã hoàn tất và đọc lại Sheet.

## 5. Nếu không thực thi được

Giữ browser in-app mở tại bước lỗi. Báo request/query, lỗi không chứa bí mật,
phần đã hoàn tất và phần cần người dùng hỗ trợ. Chờ phản hồi rồi kiểm tra lại
trạng thái. Không tự retry nhiều lần để có Passed. Retry được người dùng cho
phép phải phân biệt rõ với lần chạy trước; không trộn console hai lần chạy.
