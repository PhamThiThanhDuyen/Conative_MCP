# Mẫu báo kết quả theo org/source

Lặp block sau cho từng org/source theo thứ tự thực thi.

```text
Organization: <tên đã xác minh>
Source hiển thị / from_source: <tên> / <giá trị>
Timerange: <YYYY-MM-DD> → <YYYY-MM-DD>
Mốc bắt đầu run: <MMM dd yyyy hh:mmAM/PM, Asia/Ho_Chi_Minh>
Phạm vi: <Flow tổng / phần được yêu cầu>

1. Summary Variant — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột Summary của Sales_by_variant: <header, địa chỉ, link>
- Passed / Failed / N/A: <số lượng từng loại>
- Failed: <metric và ô có note>

2. List Variant — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột List của Sales_by_variant: <header, địa chỉ, link>
- API hoàn tất/tổng API, offset, số item thực tế: <coverage>
- Passed / Failed / N/A: <số lượng từng loại>
- Failed: <metric và ô có note>

3. Summary Product — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột Summary của Sales_by_product: <header, địa chỉ, link>
- Passed / Failed / N/A: <số lượng từng loại>
- Failed: <metric và ô có note>

4. List Product — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột List của Sales_by_product: <header, địa chỉ, link>
- API hoàn tất/tổng API, offset, số item thực tế: <coverage>
- Passed / Failed / N/A: <số lượng từng loại>
- Failed: <metric và ô có note>

Trạng thái org: <Đã hoàn tất phạm vi được yêu cầu / Đang dở / Chưa chạy>
Đang dừng tại: <org/source/chặng/API/offset, nếu có>
Org tiếp theo: <tên / Không còn; chưa chạy nếu org hiện tại chưa xong>
Vướng mắc: <bước lỗi, phần đã kiểm tra và cần người dùng hỗ trợ>
Browser in-app: <đang mở ở đâu nếu cần hỗ trợ>
```

List chưa hết folder thì nêu status tạm thời. Phần chưa chạy hoặc chưa đọc
được ghi “Chưa có kết quả”, không điền số 0 hoặc N/A thay chặng chưa chạy.
Không gộp số liệu Summary và List. Không đưa token/auth response/console đầy đủ
vào báo cáo. Chỉ báo org xong khi các chặng thuộc phạm vi yêu cầu đã lưu và đọc lại.
