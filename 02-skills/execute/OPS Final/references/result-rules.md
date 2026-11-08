# Quy tắc metric, status và ghi chú

## Nguồn kết quả

Dùng tick xanh/đỏ và nội dung kiểm tra do script của request Summary vừa chạy
trả về trong Postman Console/test result. Giữ tách biệt Variant và Product.
Chỉ lấy log sau mốc Send của đúng request, organization, source và timerange.

Không suy ra kết quả từ status HTTP, response data đơn thuần hoặc cột kiểm tra
cũ. Dữ liệu bằng 0 vẫn theo kết quả script. Không tự đổi threshold/tolerance,
công thức Difference hoặc nội dung script để làm kết quả khớp.

## Mapping vào dòng Sheet

1. Đọc Name và Key của đúng tab live. Một thông báo phải xác định được một metric.
2. Ưu tiên tên metric trùng Name hoặc key trùng một Key duy nhất, sau khi bỏ
   wrapper hiển thị như “summary” theo script thực tế. Có thể bỏ khoảng trắng
   ở hai đầu và khác biệt hoa/thường; không gộp các metric có tên gần giống.
3. Với thông báo như “Chênh lệch summary total sales”, chỉ gán vào `Total Sales`
   khi script hiện tại xác nhận đó là kiểm tra `total_sales`. Không suy ra từ
   việc hai chuỗi có từ “sales”. Cần đọc script nếu log không ghi key rõ ràng.
4. Một Key trùng nhiều dòng thì cần Name hoặc mapping trong script phân biệt.
   Ví dụ Key `ordered_qty_percentage` hiện xuất hiện ở nhiều metric Variant;
   không gán một kết quả vào tất cả các dòng có Key đó.
5. Không lấy mapping từ bộ skill Conative MCP Final: OPS có tên key khác, như
   `gross_qty` và `forecast_value`. Key trống không có nghĩa là N/A: vẫn có thể
   tìm metric theo Name và script.
6. Log có metric chưa map được, hoặc Name/Key mơ hồ: dừng ghi tab đó và hỏi
   người dùng. Không coi metric chưa map được là “không xuất hiện”.

## Status

| Kết quả của lần chạy đã hoàn tất | Giá trị ghi | Cell note |
| --- | --- | --- |
| Tick xanh cho metric | Passed | Không cần |
| Tick đỏ cho metric | Failed | Nội dung dòng lỗi gốc |
| Metric không có trong toàn bộ kết quả của lần chạy | N/A | Không cần |
| API/script lỗi, log chưa đủ hoặc chưa chạy | Để trống | Báo lỗi trong chat |
| Không xác định được metric hoặc kết quả mâu thuẫn | Chưa ghi, hỏi người dùng | Không tự đoán |

Nếu cùng metric có nhiều subcheck đã xác minh thuộc cùng metric: có ít nhất
một subcheck đỏ → Failed, lưu mọi dòng đỏ; tất cả subcheck xanh → Passed.
Nếu không rõ đây là subcheck hay log cũ/trộn run, hỏi thay vì tự gộp.

N/A chỉ áp dụng sau khi đã có lần chạy hợp lệ và đọc đủ kết quả. Console rỗng,
lỗi auth, GraphQL errors hoặc script không hoàn tất không đủ điều kiện ghi N/A.

## Note cho Failed

Chọn ô Failed → Chèn → Ghi chú → dán nguyên văn dòng tick đỏ, ví dụ người dùng:

```text
❌ Chênh lệch summary total sales: API data-svc = 31200311.89, API GraphlQL = 31201783.25, Difference = 1471.36
```

Giữ số, dấu, tên API và Difference như output; không tự sửa cách viết hoặc
tính lại Difference. Nhiều dòng đỏ cho cùng metric thì mỗi thông báo một dòng.
Nếu thông báo có bí mật, che phần bí mật và báo đã che; không lưu bí mật vào note.
Không sửa note ở cột cũ. Nếu đang hoàn tất lại cùng cột và cùng run, giữ các
note đã đúng; không xóa note chưa xác định được nguồn.
