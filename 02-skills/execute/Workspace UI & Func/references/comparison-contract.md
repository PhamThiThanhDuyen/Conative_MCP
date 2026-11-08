---
knowledge_id: QA-WORKSPACE-UI-FUNC-COMPARISON-001
knowledge_type: qa-intelligence
source: SRC-WORKSPACE-USER-FLOW-20261104; SRC-WORKSPACE-LANGFUSE-FLOW-20261105; SRC-WORKSPACE-LANGFUSE-OBS-20261105; SRC-WORKSPACE-COMPARE-UI-LOG-20261105
owner: Conative QA/Data owner (review pending)
authority: source-derived
scope: Displayed Workspace UI data to matching Langfuse query_data Input/Output reconciliation
target_release: current
status: needs-review
last_verified: 2026-11-05
supersedes: []
---

# Contract đối chiếu UI ↔ log response

Nguồn được ghi trong [source index draft](sources.md). Đây là quy trình đối chiếu, không phê duyệt công thức/format ngoài TC và mapping UI ↔ path Input/Output đã xác minh.

## Chọn đúng log và phạm vi compare

Dùng [Langfuse runtime](langfuse-log-runtime.md). Xác minh conversationId, Session ID thực tế/tenant/org/environment, đúng lượt response và trace/observation `tool.execution:query_data`. Session ID có thể là `[tenantId,conversationId]`. Prompt chỉ dùng nhận diện lượt trả lời; không so độ đúng của Input query với prompt/Expected. Nhiều query cấp dữ liệu cho report thì ghi mapping từng phần UI → observation → Output path.

Theo yêu cầu mới nhất 05/11/2026, **chỉ kiểm dữ liệu UI trả về có khớp Input/Output của đúng response**. Không tạo FAILED/BLOCK vì Input có filter, source, kỳ, grain hoặc sort khác prompt. Ví dụ Input có `status = 'active'` dù prompt không nói active: nếu UI mô tả đúng phạm vi thực tế và data khớp log thì compare không fail vì filter đó.

Đọc Input để hiểu dataset, source, grain, fields, kỳ, timezone, filters, sort, limit, aggregation và forecast window thực tế. So các thông tin/phạm vi UI công bố với Input và Output meta. Nếu UI công bố source/kỳ hoặc data khác log đã xác minh, đó là mismatch UI ↔ log. UI không công bố một tham số mà không cần tham số đó để nối/so dữ liệu thì không tự block chỉ vì thiếu nhãn UI.

Kiểm Output theo cấu trúc thực tế: rows/columns, totals, pagination, meta, success, warnings/errors, snapshotPage hoặc trường tương đương nếu có. Chọn Preview → Raw và đọc đủ Input/Output. Không dùng lời assistant đã render trong session làm dữ liệu nguồn cho chính UI đó.

## Cùng dữ liệu trước khi so sánh

Ghi scope thực tế của dataset đang hiển thị: org ID, grain, source/channel, từ/đến, timezone, end-date convention, filters, sort, pagination và forecast window nếu field cần. Scope UI/log lệch hoặc thiếu đến mức chưa nối được cùng dữ liệu thì block phép so field values; một lời công bố UI trái với log đủ bằng chứng là failure riêng. Không tạo gate so scope prompt với Input.

“Last 3 months” trong lời UI không tự đồng nghĩa 90 ngày: đối chiếu kỳ UI công bố với Input/meta có căn cứ. Top-N kiểm thứ tự, tập ID và ties theo dữ liệu/sort log; không tạo N mới từ prompt trong bước compare. Phân biệt tổng top N với tổng toàn dataset.

Historical sales và forecast dùng các cửa sổ thực tế trong Input/Output. `sales_forecast` có thể dùng planning window theo từng sản phẩm; không đổi nhãn thành Next 90-Day Sales chỉ vì cùng tên field trong log. Nếu UI mô tả kỳ tương lai, so mô tả đó với forecast window log; không chấm query theo kỳ của prompt hoặc sửa query để ép khớp.

## Nối hàng và mapping

- Dùng Product ID hoặc Variant ID theo grain, giữ ID dưới dạng string. Không dùng thứ tự row, số liệu giống nhau hoặc tên rút gọn để tự chứng minh ID. Với aggregate/time series dùng khóa nhóm/thời gian tương ứng đã xác minh, không ép PRODUCT ID vào mọi dataset.
- Kiểm unique keys và mọi ID UI nằm trong Output log window đã thu. Thiếu row do pagination không có nghĩa giá trị bằng 0 hoặc product không tồn tại.
- Tên không đủ phân biệt size/variant: ghi candidate và phần identity chưa xác minh. Không chấm toàn bộ các candidate là matched.
- Xác minh mapping từ UI sang schema/columns/path của Output đúng query và ý nghĩa theo TC/contract; ghi path và observation cho từng field. Không tự dùng `Field compare` QE cũ làm mapping log; nhãn tùy biến trong UI chưa tự có mapping. `Trend` thiếu mapping thì không thay bằng field “gần giống”. Số do UI tự tính phải truy được về Input/Output và phép tính có căn cứ. Metric có trực tiếp trong Output chỉ cần so giá trị, không đòi công thức backend để xác nhận phép so đó.

## Giá trị, precision và format

1. Tách value assertions khỏi Title/Unit/Format assertions. Áp dụng những gì Steps/Expected thực sự yêu cầu. Không biến khác format vô hại thành lỗi tính toán backend.
2. Với cùng đơn vị/locale, bỏ dấu phân cách và so số bằng Decimal. `129,298` khác `129,297.55`; `15.1` bằng `15.10`. Không đặt tolerance mới hoặc làm tròn Output log theo UI nếu TC chưa cho phép.
3. `%` là đơn vị, không tự chia/nhân 100. Xác minh ratio hay percentage point từ mapping trước. Currency khác nhau không tự quy đổi.
4. `K/M`, “about”, khoảng số hoặc ô bị che mất precision không chứng minh raw value chính xác. Chấm format/precision theo Expected nếu có; khi không thể khôi phục giá trị thì ghi chưa xác minh, không tạo giá trị gốc giả.
5. Null, missing và 0 là các trạng thái khác nhau. Chỉ so null bằng nhau khi TC quy định rõ; không coi missing row/value là zero.
6. Product title chỉ áp dụng equivalence quotation marks nếu mapping/rule được duyệt cho phép; không chuẩn hóa tùy ý dấu gạch, khoảng trắng, ngoặc hoặc size.

## Tổng và diễn giải

Tính lại tổng cho đúng tập ID bằng Decimal; phân biệt tổng top N với totals toàn dataset và trang đang thấy. Kiểm tổng trong phần văn bản, không chỉ bảng. Giữ giá trị gốc và ví dụ sai lệch có ID. Không kết luận nguyên nhân khi chỉ có hai số khác nhau.

Đối chiếu các số có thể truy vết trong cột diễn giải như reorder, views, on-order; tách nhận xét chủ quan và field không có mapping. Ghi phần chưa xác minh, không kéo một failure của cột sang mọi cột khác.

So UI với **log của cùng response** chỉ kết luận tính nhất quán UI ↔ Input/Output. Kiểm Input ↔ prompt và xác minh độc lập công thức/backend không nằm trong bước compare; không dùng thiếu daily forecast curve làm blocker cho metric UI đã khớp trực tiếp Output. Số UI tự tính chưa có đủ input/phép tính thì ghi chưa xác minh riêng. Kiểm mọi thông tin data UI sinh ra: text/insight có thể truy vết, KPI, table từng cell/mọi trang, chart series/points/tooltip, số lượng/thiếu/thừa/trùng, tổng và ranking. Log có 100 rows chưa chứng minh đủ toàn dataset; phân biệt rows trả về, snapshot lưu, backend pagination và totals.

## Kết luận

| Bằng chứng | Kết luận logic | Token khi dropdown hiện tại cho phép |
|---|---|---|
| Mọi assertion bắt buộc đủ bằng chứng và đạt | pass | PASSED |
| Ít nhất một sai lệch đã chứng minh | fail, kèm giới hạn còn lại | FAILED |
| Không có failure đã chứng minh nhưng thiếu điều kiện bắt buộc | blocked | BLOCK |
| Chưa thực thi | not run | Không đổi status hoặc dùng token live được phép |

Không ghi PARTIAL nếu dropdown không có. PASS một số field không phải PASSED cả TC. Log có `success: true` hoặc response hoàn tất không phải status test. Thiếu log hoặc bị truncate không tự trở thành failure số liệu. Không gọi QE API Postman để thay thế.

## Helper offline

Chuẩn hóa snapshot UI/log tối thiểu theo [input ví dụ](../assets/comparison-input.example.json), rồi chạy:

```sh
python3 scripts/compare_snapshot.py input.json --output comparison.json
```

Schema hiện tại dùng `log_scope`, `log_rows`, `key.log`, `fields[].log`, `log_window_complete`. `log_provenance` cần các chuỗi `conversation_id`, `session_id`, `trace_id`, `observation_id`, `observation_name` và `response_turn`, cùng `ui_conversation_id` và `ui_response_turn` để kiểm liên kết. `response_turn` là định danh lượt/thời điểm đã xác minh; nếu UI/log có ID khác, chuẩn hóa về cùng run/turn có căn cứ. `session_id` là chuỗi thực tế, có thể chứa JSON `[tenantId,conversationId]`. Chỉ ghi `response_link_verified: true` sau khi đã đối chiếu prompt, response, tenant/org/environment và query cấp dữ liệu đó; script không tự chứng minh provenance browser. `observation_name` phải là `tool.execution:query_data`.

Trong snapshot helper, scope đã chuẩn hóa của hai bên cần `org_id`, `grain`, `sources`, `from`, `to`, `timezone`, `date_boundary`, `filters`; thêm `required_scope` cho forecast/currency nếu cần. Đây là scope UI và log thực tế, không phải scope prompt. Helper áp dụng schema chặt; nếu UI chỉ thiếu nhãn scope không liên quan phép so, dùng đối chiếu thủ công với log đã định danh thay vì bịa nhãn hoặc biến giới hạn helper thành BLOCK toàn TC. Thiếu scope cần thiết không được tự điền từ QE/default. Snapshot v1 có khóa `qe_*` hoặc `key/fields.qe` bị BLOCK; evidence cũ giữ nguyên, chỉ tạo snapshot log mới khi có log thực tế. Không chỉ đổi tên schema QE cũ thành log.

Fields gồm `ui`, `log`, `type` (`decimal`, `percent`, `string`). Values dùng decimal string/integer. `grouping_separator: ","` và `nulls_equal: true` chỉ đặt khi có căn cứ; không đổi ratio thành percentage point. ID string, hoặc composite key đã chuẩn hóa đúng grain, phải unique. `log_window_complete` chỉ true khi log window so với UI đã thu đủ có bằng chứng; không đồng nghĩa toàn dataset. Kết quả dùng `log_field`, `log`, `ui_minus_log`.

Helper chỉ so value field theo ID, không gọi API/browser hoặc ghi Sheet. Phạm vi/data UI ↔ Input/Output, tổng, ranking, text/chart, thiếu hàng UI, format và coverage vẫn kiểm riêng; exit code snapshot không thay status toàn TC. Exit codes: 0 PASSED, 1 FAILED, 2 BLOCK. Chạy synthetic checks: `python3 -m unittest discover -s scripts -p 'test_*.py' -v`.
