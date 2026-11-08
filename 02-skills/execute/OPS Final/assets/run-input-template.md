# Input chạy flow tổng OPS

```text
Dùng skill OPS Final để chạy API và cập nhật Google Sheet.
Phạm vi: Flow tổng Summary và List.
Danh sách theo thứ tự:
1. Org: <tên org> | Source: <tên source hoặc from_source> | From: <YYYY-MM-DD> | To: <YYYY-MM-DD>
2. Org: <tên org kế tiếp nếu có> | Source: <source> | From: <YYYY-MM-DD> | To: <YYYY-MM-DD>
Mỗi org: Summary Variant → ghi và đọc lại Sheet → List Variant → ghi và đọc lại Sheet
→ Summary Product → ghi và đọc lại Sheet → List Product → ghi và đọc lại Sheet.
Xong org hiện tại mới sang org tiếp theo.
List: mỗi API limit 20, offset 0, 20, 40, 60, 80; ghi Sheet sau mỗi API.
Nếu bị kẹt, giữ browser in-app mở để tôi kiểm tra.
```

Đây là mẫu gọi skill, không phải yêu cầu chạy ngay. Chưa có input thực tế thì
chỉ chuẩn bị/đọc dữ liệu, không chọn organization hoặc timerange thay người dùng.
Nếu chỉ muốn chạy một phần, ghi rõ chặng hoặc phạm vi đó thay cho “Flow tổng”.
