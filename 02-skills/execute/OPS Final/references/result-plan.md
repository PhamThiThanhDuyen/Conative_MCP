# Helper tạo bảng kết quả trước khi ghi

Helper này tùy chọn. Nó giúp giữ status/note nhất quán, không tự chạy Postman
hoặc ghi Sheet. Người dùng chỉ cần chỉnh các file flow nếu không dùng helper.

## Input

Sau khi xác minh toàn bộ console của một run, chuẩn hóa vào JSON ở thư mục
scratch được phép. Không đưa raw response, credentials hoặc token vào file.
`metric` trong results phải là Name chính xác đã resolve từ Sheet/script.
Helper không tự đoán mapping từ câu log.

Ví dụ giả lập, không phải kết quả live:

```json
{
  "run_complete": true,
  "sheet_name": "Sales_by_variant",
  "metrics": [
    {"row": 18, "name": "Gross Sales"},
    {"row": 24, "name": "Total Sales"},
    {"row": 51, "name": "Ad spend"}
  ],
  "results": [
    {"metric": "Gross Sales", "status": "Passed"},
    {"metric": "Total Sales", "status": "Failed", "message": "❌ Test giả lập total_sales: A=10, B=12, Difference=2"}
  ]
}
```

`metrics` phải chứa mọi dòng metric đọc từ tab live, không chỉ ba dòng ví dụ.
Chỉ đặt `run_complete: true` khi đã kiểm tra response/script và đọc đủ log.
Nếu cùng metric có nhiều subcheck, cần xác minh chúng thuộc đúng metric và
cùng run, rồi thêm `subchecks_verified: true`.

## Chạy helper

Từ thư mục `OPS Final`:

```sh
python3 scripts/build_result_plan.py /private/tmp/ops-input.json --output /private/tmp/ops-plan.json
```

Output có `cells` gồm row, metric, value, note và tổng số Passed/Failed/N/A.
Helper chặn input chưa hoàn tất, console rỗng, metric chưa map, dòng/tên trùng,
status sai và Failed thiếu note. Không có tolerance hay phép tính Difference.

Sau đó đối chiếu plan với org/source/timerange, header và cột của đúng run.
Helper không biết organization, cột hoặc quyền ghi; người thực thi phải xác minh
những phần này theo [sheet-contract.md](sheet-contract.md), rồi mới ghi Sheet.
Mỗi lần ghi cần dùng plan vừa tạo thành công; helper lỗi thì không dùng file cũ.

## Kiểm tra helper

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_*.py' -v
```
