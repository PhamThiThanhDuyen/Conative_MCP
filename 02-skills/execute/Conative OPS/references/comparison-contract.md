# Comparison contract — cần hoàn thiện trước khi chạy

## Đã biết

- Mục tiêu: so sánh kết quả API GraphQL với data service cho cùng org/source.
- Grain: variant (`Sales_by_variant`) và product (`Sales_by_product`).
- Source của org lấy từ tab `Danh sách org`.
- Kết quả chi tiết được ghi vào hai tab Sales trước khi tổng hợp lên `Danh sách org`.

## Thông tin cần bổ sung

| Nhóm | Cần xác định |
| --- | --- |
| API GraphQL | Endpoint/môi trường, query hoặc operation, biến đầu vào, cách xác thực. |
| Data service | Endpoint hoặc công cụ truy vấn, request tương ứng, cách xác thực. |
| Phạm vi | Khoảng thời gian, timezone, quy tắc biên ngày, source/channel, filter, đơn vị/tiền tệ, phân trang và thứ tự. |
| Ánh xạ | Chỉ tiêu và path phản hồi của mỗi bên; khóa ghép hàng product/variant. |
| So sánh | Quy tắc null/thiếu dữ liệu, làm tròn hoặc tolerance số, xử lý khác biệt scope. |
| Status | Giá trị hợp lệ cho pass/fail/blocked hoặc trạng thái khác, điều kiện của từng giá trị. |
| Tổng hợp | Cách gộp status hàng chỉ tiêu thành status variant/product, rồi thành status org; xử lý hàng chưa chạy. |
| Ghi Sheet | Tên cột mới, vị trí, format/validation, ghi chú và cách đánh dấu lần chạy. |

Chỉ kết luận khớp khi hai kết quả có cùng metric, grain và phạm vi. Nếu thiếu hợp đồng cần thiết, ghi rõ phần chưa thể so sánh; không tự chọn giá trị hoặc status thay người dùng.
