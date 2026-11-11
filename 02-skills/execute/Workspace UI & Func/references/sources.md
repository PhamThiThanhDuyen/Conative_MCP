---
knowledge_id: QA-WORKSPACE-UI-FUNC-SOURCES-001
knowledge_type: qa-intelligence
source: SRC-WORKSPACE-VERIFY-BUG-20261111; SRC-WORKSPACE-USER-FLOW-20261104; SRC-WORKSPACE-LANGFUSE-FLOW-20261105; SRC-WORKSPACE-LANGFUSE-OBS-20261105; SRC-WORKSPACE-COMPARE-UI-LOG-20261105
owner: Conative QA owner (review pending)
authority: source-derived
scope: Workspace UI and functional testcase execution sources
target_release: current
status: needs-review
last_verified: 2026-11-11
supersedes: []
---

# Tài liệu nguồn và độ ưu tiên

Các nguồn sau đã được người dùng chỉ định trong chat ngày 04/11/2026. Tên tab, header, row và dữ liệu phải được đọc live mỗi lần dùng; ID/gid chỉ giúp nhận diện, không thay việc kiểm tra metadata.

## Đăng ký nguồn trong gói draft

| Source ID | Owner | Authority / status | Phạm vi và location |
|---|---|---|---|
| SRC-WORKSPACE-USER-FLOW-20261104 | Người yêu cầu; QA owner review pending | Provided / needs-review | Các chỉ dẫn trong chat hiện tại: TC live, org được chọn, status và Note ngắn; phần QE đã được yêu cầu mới thay thế |
| SRC-WORKSPACE-VERSION-20261105 | Người yêu cầu; QA owner review pending | Provided / needs-review | Chỉ dẫn trong chat ngày 05/11/2026: mỗi lần thực thi và ghi status, điền thời điểm hoàn tất thực thi vào Version đúng model; giờ Việt Nam, giữ Version khi chỉ sửa Note |
| SRC-WORKSPACE-VERIFY-BUG-20261111 | Người yêu cầu; QA owner review pending | Provided / needs-review | Chỉ dẫn chat 11/11/2026: đọc ticket, tìm TC Scenario_UI liên quan, rerun bằng skill sẵn có, ghi status/Note theo mẫu và comment Activity chỉ trong scope ticket; cập nhật cùng ngày: Activity có PASS/FAIL, thời gian, conversion link, ảnh, Reason chỉ khi FAIL và status ticket In testing; [skill](../skill/verify-workspace-bug/SKILL.md) |
| SRC-WORKSPACE-UI-WORKBOOK | Conative QA owner review pending | Provided / needs-review | Workbook Workspace; nguồn TC mặc định Scenario_UI theo cập nhật của người dùng ngày 04/11/2026; các tab bổ trợ bên dưới |
| SRC-WORKSPACE-QE-MAPPING | Conative QA/Data owner review pending | Historical / superseded for Workspace comparison | Mapping QE lịch sử; không dùng làm oracle log hiện tại |
| SRC-WORKSPACE-QE-FLOW | Conative QA owner review pending | Historical / superseded for Workspace comparison | Sibling Conative MCP Final/execute-api-QE.md; không còn dependency thực thi Workspace |
| SRC-WORKSPACE-LANGFUSE-FLOW-20261105 | Người yêu cầu; QA owner review pending | Provided / needs-review | Chỉ dẫn trong chat 05/11/2026: UI values so Output log, UI/prompt so Input; 8 bước Sessions → query_data → Preview/Raw |
| SRC-WORKSPACE-COMPARE-UI-LOG-20261105 | Người yêu cầu; QA owner review pending | Provided / needs-review | Chỉ dẫn mới nhất 05/11/2026: compare chỉ so data UI với Input/Output log, bỏ kiểm Input giống prompt; thay thế phần Input ↔ prompt của chỉ dẫn trước |
| SRC-WORKSPACE-LANGFUSE-OBS-20261105 | Conative Product/QA owner review pending | Observed / needs-review | Điều hướng read-only sau user đăng nhập; composite Session ID, Open observation panel → Open in new tab → Tree; [runtime](langfuse-log-runtime.md) |
| SRC-WORKSPACE-DEVTAK-BUG-90468 | Conative QA owner review pending; reporter of sample ticket | Provided format example / needs-review | [DevTak Bug #90468](https://devtak.cbidigital.com/projects/conative-paas/work_packages/90468/activity), đọc qua browser 04/11/2026; chuẩn hóa tại [Bug contract](../skill/create-workspace-bug/references/devtak-bug-contract.md) |

Đây là source index local của bản draft, không phải phê duyệt nghiệp vụ. Trước khi dùng làm canonical Knowledge hoặc promote cho team, owner cần đối chiếu/đăng ký vào [source registry của repo](../../../../03-knowledge/governance/source-registry.md) và hoàn thành review. Lần cập nhật này chỉ đọc Langfuse do người dùng chỉ định, không chạy TC/UI/QE hoặc ghi Sheet; các quan sát cũ chỉ giúp định vị lần chạy kế tiếp.

## Workbook Workspace

ID: `1orhYq-ZAqQbYUTDMc_88XLUNDUQ0mtAhEz3a6BMQ3Ug`.

| Tab / gid | Vai trò |
|---|---|
| [Scenario_UI](https://docs.google.com/spreadsheets/d/1orhYq-ZAqQbYUTDMc_88XLUNDUQ0mtAhEz3a6BMQ3Ug/edit) | Nguồn TC mặc định theo yêu cầu hiện tại; xác minh gid, headers và vị trí kết quả từ metadata live trước khi dùng |
| [ReportConative — 535144085](https://docs.google.com/spreadsheets/d/1orhYq-ZAqQbYUTDMc_88XLUNDUQ0mtAhEz3a6BMQ3Ug/edit#gid=535144085) | Title, Tooltip, Unit, Format và phạm vi report |
| [Prompt — 1869112976](https://docs.google.com/spreadsheets/d/1orhYq-ZAqQbYUTDMc_88XLUNDUQ0mtAhEz3a6BMQ3Ug/edit#gid=1869112976) | Nguồn bổ trợ Anh–Việt khi dòng TC cần tra cứu |

`Update_TestCase` là tên trong hướng dẫn cũ; gid `119542077` được quan sát là `Final_TestCase`. Không tự chuyển sang đó thay Scenario_UI. `TC_Gen Report UI` là nguồn trước đây, không còn là mặc định. Chưa xác minh gid của `Scenario_UI`; không tái sử dụng gid `1374457320` của tab cũ. Các số đếm prompt/coverage cũ không được dùng làm kết quả hiện tại.

Người dùng có thể chỉ định Testcase_Function hoặc tab khác cho một đợt chạy; khi đó dùng metadata và contract thực tế của tab được chọn, không sao chép row/status của tab UI.

## Nguồn đối chiếu hiện tại: Langfuse

[Sessions project](https://us.cloud.langfuse.com/project/cmw1nvrgd0ebaad0gikzek0rh/sessions). Dùng [Langfuse runtime](langfuse-log-runtime.md): conversationId của UI → Session ID → đúng conversation/response → Open observation → Tree → `tool.execution:query_data` → Preview → Raw.

Đọc Input/Output của đúng turn và query, xác minh tenant/org/environment. Theo SRC-WORKSPACE-COMPARE-UI-LOG-20261105, chỉ so dữ liệu/phạm vi UI trả về với log; không chấm Input giống prompt/Expected. Prompt vẫn dùng chọn đúng lượt response. Mapping dựa vào schema/columns/path của log và ý nghĩa field đã xác minh, không tự mang mapping hoặc default timezone QE sang log. Nếu thiếu timezone/phạm vi cần cho assertion thì ghi chưa xác minh.

Cập nhật này thay thế dependency QE của Workspace; không thay đổi project sibling Conative MCP Final. Workbook mapping QE và evidence QE cũ là lịch sử. Không gọi Postman thay log thiếu, không chuyển TC sang Round 2/Claude.ai. Chưa đồng bộ source registry toàn repo hoặc promote; source mới đăng ký ở gói draft này để chờ owner review.

## Snapshot và export

Ghi source workbook/tab/row, prompt, Steps, Expected và thời điểm intake trong run record. File XLSX tải về chỉ để lưu trữ/tham khảo. Khi người dùng yêu cầu đọc lại sheet, dùng connector live, không dùng cache. Không hardcode org/timezone theo ví dụ trong chat hoặc snapshot của dependency.
