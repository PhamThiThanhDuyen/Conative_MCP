---
knowledge_id: QA-WORKSPACE-UI-FUNC-SHEET-001
knowledge_type: qa-intelligence
source: SRC-WORKSPACE-USER-FLOW-20261104; SRC-WORKSPACE-UI-WORKBOOK; SRC-WORKSPACE-VERSION-20261105
owner: Conative QA owner (review pending)
authority: source-derived
scope: Authorized testcase status, Note and model-specific execution Version writeback
target_release: current
status: needs-review
last_verified: 2026-11-05
supersedes: []
---

# Contract cột và ghi kết quả

Đọc metadata trước. Dùng exact tab names, bounded ranges và header hiện tại. Khi chuẩn bị ghi, dùng CellData (`get_spreadsheet_cells`) để đọc value/formula, validation và format; plain values không đủ để xác nhận dropdown.

## Intake

Nguồn TC mặc định hiện tại là `Scenario_UI`. Đã đọc live ngày 05/11/2026: `Prompt (English)` ở E, `Prompt (Vietnamese)` ở F; `Bước thực hiện` ở I và `Kết quả mong đợi` ở J. Đây là vị trí quan sát, không phải hằng số; luôn đọc metadata, headers và validation live.

Các header đã quan sát: `Precondition`, `Test Case ID`, `Test Case Title`, `Description`, `Prompt (English)`, `Prompt (Vietnamese)`, `Application URL/Route hoặc API Endpoint`, `Steps`, `Expected Result (Front-end)`.

- Match ID chính xác. Trùng ID có thể là nhiều biến thể; ghi row/title/prompt để phân biệt. Nếu chưa xác định được phạm vi, hỏi một câu cụ thể, không đoán.
- Bỏ tiền tố số thứ tự của từng prompt; không thay câu chữ hoặc thêm yêu cầu. Ngôn ngữ và chuỗi hội thoại theo TC/yêu cầu người dùng.
- `Prompt` phụ trợ có thể chứa nhiều TC ID phân tách bằng dấu phẩy. Không lấy row order làm liên kết, không để prompt tham khảo mở rộng Expected.
- Khi TC đổi giữa intake và writeback, không ghi kết quả của bản cũ lên bản mới. Yêu cầu rerun mới cho prompt mới.

## Kết quả

Ngày 05/11/2026, sau khi sheet thêm Prompt (Vietnamese) và QA Review, các header trên Scenario_UI được quan sát là:

| Header chính xác | Vai trò | Vị trí khi quan sát, không phải hằng số |
|---|---|---|
| `QA Status\nClaude Sonnect 5.5` | Status Claude | L |
| `QA Review\nClaude Sonnect 5.5` | Review riêng, không tự ghi khi update status | M |
| `Ghi chú Claude Sonnect 5.5` | Note Claude | N |
| `Version Claude Sonnect 5.5` | Thời điểm hoàn tất lần chạy Claude | O |
| `QA Status\nGPT Sol 6.1` | Status GPT | P |
| `Ghi chú GPT Sol 6.1` | Note GPT | Q |

Tên header có typo `Sonnect`: giữ đúng tên hiện tại để định vị, không tự sửa sheet. Không suy ra model thực chạy từ header.

Dropdown đã quan sát: `FAILED`, `PASSED`, `BLOCK`. Luôn đọc validation lại. Nếu kết luận không có token tương ứng, không thêm option hay ghi token tùy ý; dùng token đã được cho phép phù hợp hoặc báo chưa thể ghi.

Status PASSED yêu cầu mọi assertion bắt buộc đã xác minh. Một failure đã chứng minh đủ cho FAILED, đồng thời ghi blocker còn lại nếu ảnh hưởng kết luận. Không có failure nhưng thiếu bằng chứng bắt buộc thì BLOCK. Không chuyển một field thiếu mapping thành failure số liệu.

## Writeback

1. Kiểm tra TC ID/prompt, header, target value và quyền ghi hiện hành.
2. Khi thực thi và ghi status, ghi status, Note và Version đúng model. Theo yêu cầu người dùng ngày 05/11/2026, Version chứa thời điểm hoàn tất thực thi trong run record, định dạng `dd/MM/yyyy HH:mm:ss (GMT+7)`, timezone `Asia/Ho_Chi_Minh`. Đây là timestamp, không phải thời lượng hay phiên bản model. Với evidence cũ, dùng mốc thực thi có căn cứ; thiếu mốc thì ghi rõ chưa xác minh, không thay bằng giờ hiện tại. Yêu cầu chỉ sửa Note giữ status/Version. Giữ cột model còn lại, công thức, validation, formatting và các row khác.
3. Dùng `updateCells` với `fields: userEnteredValue`, range zero-based chính xác. Group status/Note/Version của cùng lần chạy trong một batch; đọc lại cả ba ô. Tìm cột theo header live, không hardcode vị trí. Hiện chưa quan sát Version GPT; nếu model đích thiếu Version thì báo phần thiếu, không ghi vào Version Claude hoặc tự thêm cột.
4. Đọc lại và kiểm tra bằng nhau sau write. Kiểm tra hiển thị native khi có thể; không auto-fit toàn sheet.

Chỉ dùng dữ liệu của lần chạy được chỉ định. Khi thay Note kết quả hiện tại, bỏ đoạn cũ không còn đúng; không ghép các lần chạy khác prompt thành cùng một Actual result.
