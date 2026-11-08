# Draft review — write-qa-testcases — 2026-11-04

Request: lưu skill vừa chốt trong conversation vào gói Workspace UI & Func. Author: Codex. Classification: behavioral vì thêm khả năng soạn/rà test case vào router. Decision: Draft / needs-review; chưa có approval cho promotion của bản dự án.

## Boundary và overlap

Existing skills đọc/chạy/đối chiếu/ghi kết quả; skill mới chỉ authoring, sửa format và rà coverage. Không đổi flow thực thi hoặc yêu cầu quyền ghi từ skill khác. Người dùng đã yêu cầu lưu tại thư mục dự án này. Không gọi Workspace/QE/DevTak hoặc ghi Google Sheets trong lần lưu.

## Thay đổi

Thêm skill/write-qa-testcases với agents/openai.yaml. Toàn bộ body của skill đã tạo trong conversation được giữ nguyên ở references/writing-standard.md; entrypoint được rút gọn theo size gate. Thêm một mục router và mô tả phạm vi authoring; không sửa các skill con đang có hoặc các file đang dirty khác. Bản global ~/.codex/skills/write-qa-testcases được giữ nguyên.

## Validation và forward walkthrough

baseline.txt lưu baseline root và initial WARN của bản import; validators.txt ghi kiểm tra bản hoàn chỉnh. normal-draft.json và missing-input-draft.json là hai output synthetic offline do author tự walkthrough, không phải independent evaluation hoặc kết quả live.

Normal: output 12 cột, prompt tiếng Anh có source/kỳ/PRODUCT ID nhưng không có ID cụ thể, Steps và Expected đánh số/xuống dòng, trạng thái Chưa chạy. Missing-input/existing sheet: tạo draft, nêu URL/validation còn thiếu, không đoán workbook, dropdown hoặc kết quả thực thi. Các output được kiểm tra cấu trúc và đọc lại; không chứng minh hành vi trên dịch vụ live.

## Chờ review/promotion

Theo change-approval-policy.md của repo, qualified reviewer/capability owner cần review trước khi approve, cài đặt từ gói hoặc publish team-wide. Chưa tạo approval giả, chưa thay approval register và không quảng bá bản dự án là approved. Đây là lưu draft local theo yêu cầu, không phải một lần promotion.
