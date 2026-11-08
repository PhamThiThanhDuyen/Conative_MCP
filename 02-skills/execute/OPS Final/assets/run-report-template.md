# Mẫu báo kết quả

```text
Organization: <tên đã xác minh>
Source hiển thị / from_source: <tên> / <giá trị>
Timerange: <YYYY-MM-DD> → <YYYY-MM-DD>
Kiểm tra ngày: <ngày chạy, Asia/Ho_Chi_Minh>

Variant — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột kết quả: <header, địa chỉ cột và link tab>
- Passed: <số lượng>
- Failed: <số lượng; metric và ô có note>
- N/A: <số lượng>

Product — <Đã lưu và xác minh / Đang dở / Chưa chạy>
- Cột kết quả: <header, địa chỉ cột và link tab>
- Passed: <số lượng>
- Failed: <số lượng; metric và ô có note>
- N/A: <số lượng>

Vướng mắc: <Không có / bước bị kẹt, điều đã kiểm tra, phần cần hỗ trợ>
Browser in-app: <đang mở ở đâu nếu cần hỗ trợ>
```

Phần chưa chạy/không đọc được thì ghi “Chưa có kết quả”, không điền số 0.
Không đưa token, auth response hoặc toàn bộ console vào báo cáo.
