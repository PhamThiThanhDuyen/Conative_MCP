# Draft review record — 2026-11-04

Request: tổng hợp toàn bộ quy trình trong chat và build flow/skill tại `02-skills/execute/Workspace UI & Func`.

Author: Codex, theo yêu cầu người dùng. Capability owner: Conative QA owner, chưa có xác nhận review. Classification: **high-risk** vì flow bao gồm auth, live/customer-connected reporting và ghi kết quả. Không có thay đổi endpoint, credential store, collection, Google Sheet hay dữ liệu live trong lần authoring này.

## Thay đổi và ranh giới

- Giữ entrypoint và path runner cũ; bổ sung bốn module intake, UI, QE/compare và record. Tổng cộng sáu SKILL.md gồm root router và năm subskills.
- Dùng workbook Workspace do người dùng chỉ định; bỏ chỉ dẫn lấy `Update_TestCase` cũ làm nguồn mặc định. Metadata/header/validation vẫn phải đọc live.
- Tái sử dụng flow QE sibling; không copy auth hay chuyển TC sang Round 2/Claude.ai. Không sửa sibling, vendor skills hoặc global skill installation.
- Giữ Note ngắn chỉ sai lệch theo yêu cầu cuối cùng, nhãn `conversion ID`; tách Note-only khỏi rerun. Status chỉ ghi token live cho phép và đúng cột người dùng yêu cầu.
- Helper offline so Decimal và stable IDs, chặn scope thiếu/lệch. Không tự xác nhận mapping, phép làm tròn hay business formula; không thay manual assertions về tổng/ranking/chart/format.
- Không tìm thấy consumer ngoài package của các reference/template hiện có khi kiểm tra overlap. Giữ các path hiện có để tránh làm hỏng link; ý nghĩa nguồn TC và Note đã cập nhật theo chỉ dẫn mới của người dùng.

## Deterministic validation

Baseline cũ trong `baseline.txt`: hai skills PASS, 0 warnings. Bốn module mới được đo ngay khi tạo skeleton: `new-skill-initial-baseline.txt`.

Sau authoring: sáu skills PASS size validator, 0 warnings/0 failures; sáu skills PASS OpenAI quick validator. PyYAML chỉ được tải vào thư mục tạm của máy để chạy validator, không vendor vào package hoặc cài hệ thống. Link/path checks và metadata checks ghi trong `validators.txt`. Credential-pattern scan không phát hiện mẫu secret; đây không phải security approval.

`python3 -m unittest discover -s scripts -p 'test_*.py' -v`: 10 tests đạt, bao gồm CLI/output/exit codes, exact precision, thứ tự QE khác UI, missing scope, duplicate IDs, pagination, null/missing, percentage scale, title và trường hợp vừa fail vừa block.

## Forward evaluation giới hạn offline

Dùng input synthetic, không có customer data, chat giả hoặc live request. Các file `*-input.json` và `*-output.json` cùng thư mục là artifacts được tạo thực tế bởi CLI:

| Scenario | Quan sát thực tế | Giới hạn |
|---|---|---|
| Normal snapshot | PASSED; 6 value checks match dù thứ tự QE khác UI | Chỉ value assertions, không phải PASSED một TC live |
| UI làm tròn Gross sales 1000.25 thành 1000 | FAILED; 5 match, 1 mismatch, delta -0.25 theo ID QA-101 | Không suy diễn backend sai hoặc tolerance mới |
| Thiếu QE timezone | BLOCK; không thực hiện value comparison | Không dùng timezone operator hoặc default để lấp chỗ thiếu |

Walkthrough các nhánh orchestration (đọc trực tiếp skill, không thao tác live):

- TC ID trùng: intake yêu cầu phân biệt title/prompt/row, không tự chọn. TC đổi trước ghi: record chặn stale writeback.
- “Chỉ rút gọn Note”: đi thẳng record bằng evidence đã có; không gọi UI/QE, không đổi status. Chưa có evidence thì báo thiếu, không dựng số liệu.
- “Stop”: ngừng action mới, không tự retry hoặc tự ghi Sheet.
- UI có failure đã chứng minh và field khác thiếu mapping: FAILED kèm giới hạn, không PASSED hoặc tự invent PARTIAL.

Chưa kiểm chứng end-to-end trên trình duyệt/Google Sheets bằng bộ skill mới. Không dùng live execution chỉ để author-test skill. Walkthrough là self-evaluation, không thay qualified reviewer.

## Review và promotion còn chờ

Decision: **Draft / needs-review**. Chưa được approved, cài đặt hoặc publish.

Required reviewers: một qualified QA reviewer và accountable domain/security owner; tác giả không là người duyệt duy nhất. Owner cần kiểm ý nghĩa mapping/date/forecast, auth/live gates, quyền ghi, failure behavior, nguồn live và đăng ký nguồn canonical trước promotion. Approval phải có evidence và record theo governance repo; chưa tạo approval giả hoặc ghi approved vào register.

Gói có thể được đọc/review tại project theo yêu cầu người dùng. Không quảng bá kết quả synthetic thành live test evidence hoặc một approval cho team-wide reuse.
