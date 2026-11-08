# Draft change record — Langfuse comparison, 05/11/2026

## Outcome and authorization

User yêu cầu thay so UI values với QE API Postman thành so UI với log response output, cung cấp quy trình Sessions → conversationId → Open observation → Tree → tool.execution:query_data → Preview → Raw. User tự đăng nhập Langfuse và cung cấp một conversationId để kiểm tra thao tác. Không yêu cầu chạy TC mới hoặc sửa live workbook trong lượt này.

## Scope and migration

- Existing Workspace compare capability hấp thụ thay đổi, không thêm Postman/Langfuse API integration. Skill chính mới: skill/compare-workspace-report-log/SKILL.md. Path compare-workspace-report-qe cũ là redirect; references/postman-ui-runtime.md chuyển thành redirect, không để lệnh Send cũ là fallback.
- Flow, capability map, sources, orchestrator/intake/UI/record, templates và bản write-case/bug trong gói Workspace được cập nhật nhất quán sang Input/Output log. Input kiểm với prompt/TC/UI; Output so values theo ID, scope và turn đã xác minh. Nguồn TC live, quyền ghi và Version contract hiện có được giữ.
- Helper/example/tests đổi schema qe_* sang log_*, key/fields.log; output dùng log_field/log/ui_minus_log. Thêm provenance guard. Snapshot QE cũ bị BLOCK, không tự migrate bằng đổi nhãn. Evidence cũ không sửa. Caller cũ đi qua redirect; schema mới cần capture log thật rồi tạo snapshot mới.
- Không sửa sibling Conative MCP Final, installed/vendor skill, Google Sheets, DevTak hoặc cấu hình Langfuse. Source mới đăng ký trong references/sources.md của gói draft; source registry và approval register toàn repo chưa được promote.

## Validation and observation

- Baseline trước sửa và baseline initial skill mới được lưu. Repo size validator và OpenAI quick_validate: 9/9 skills PASS, không WARN/FAIL. PyYAML chỉ tải từ PyPI vào thư mục tạm cho validator.
- 13 synthetic unittest PASS; gồm exact Decimal, locale/percent/null/missing/pagination, fail kèm blocker, CLI exit/output, provenance thiếu/sai turn và legacy QE. Xem tests.txt, validators.txt và forward-evaluation.md.
- Link/path check cho các Markdown đã sửa: không có liên kết local bị thiếu; metadata reference/source ID nhất quán; quét thay đổi không có auth material hoặc raw customer payload. Chỉ giữ source pointer/ID tối thiểu do user cung cấp và observation đã xem.
- Live read-only: sau user đăng nhập, đã lọc Session ID theo conversationId được cung cấp, mở trace Connie, Open observation → Open in new tab → Tree → query_data → Preview/Raw; thấy Input CQL và Output rows/columns/totals/pagination/meta. UI có composite Session ID. Đây là kiểm chứng thao tác log, chưa so toàn bộ TC/live UI; không ghi PASSED testcase.

## Review status

Behavioral/breaking oracle and snapshot-schema migration; conservatively high-risk review class vì xử lý telemetry/customer-connected logs. Author implementation và self-evaluation hoàn tất. Qualified reviewer và QA/Product/Security owner review còn pending theo policy repo; chưa có approval record, không cài/publish/promote hoặc mô tả approved. Nguồn Knowledge giữ needs-review/source-derived. Bản sửa local này đáp ứng yêu cầu cập nhật draft của user.
