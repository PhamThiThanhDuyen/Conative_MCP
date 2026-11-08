# Helper tạo bảng kết quả trước khi ghi

Helper này tùy chọn. Nó giúp giữ status/note nhất quán, không tự chạy Postman
hoặc ghi Sheet. Người dùng chỉ cần chỉnh các file flow nếu không dùng helper.

## Input Summary

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

## Chạy helper Summary

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

## Input và helper List

Dùng `scripts/build_list_result_plan.py` cho List. Không dùng helper Summary
để ghi sau từng API List vì helper Summary tự điền N/A cho metric chưa xuất hiện.

- `sheet_name`, `metrics`: như Summary, lấy toàn bộ dòng metric của đúng tab live.
- `requests`: danh sách tên/path duy nhất của mọi API trong folder đã đọc live.
- `pages`: kết quả lũy kế từ đầu folder đến hết API vừa chạy; không chỉ trang
  cuối hoặc API cuối. Mỗi API đã đưa vào pages phải có đủ offset 0–80.
- Mỗi page có `request`, `offset` (query), `script_offset`, `limit: 20`,
  `items_checked: 20`, `run_complete: true`, `results` như Summary.
- `distinct_items_verified`: object tên/path API → true, chỉ đặt true sau khi
  thực tế xác minh 100 item khác nhau đã được script kiểm tra.
- `finalize: false`: ghi sau một API; chỉ xuất metric đã có kết quả, chưa xuất N/A.
- `finalize: true`: chỉ khi mọi API trong folder hoàn tất; lúc đó mới xuất N/A.

Xem [input giả lập đầy đủ](../evidence/list-normal-input.json) và
[plan tạo từ input đó](../evidence/list-normal-plan.json). Đây là dữ liệu test;
tên `Test_Sales` không phải request đã xác minh trong collection live.

```sh
python3 scripts/build_list_result_plan.py /private/tmp/ops-list-input.json --output /private/tmp/ops-list-plan.json
```

Helper chặn thiếu trang, offset query/script lệch nhau, trang lỗi hoặc thiếu
20 item, chưa xác minh 100 item khác nhau, log rỗng và chốt N/A quá sớm.
Helper giữ Failed từ API/offset trước và thêm API/offset vào note, không sửa
thông báo lỗi gốc. Phải cung cấp kết quả lũy kế để không mất lỗi cũ.
Helper kiểm tra metadata đầu vào; không tự kiểm chứng response hoặc coverage live.
Trước khi ghi vẫn đọc lại cột đích và giữ các Failed/note đang có của cùng run.

## Kiểm tra các helper

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_*.py' -v
```
