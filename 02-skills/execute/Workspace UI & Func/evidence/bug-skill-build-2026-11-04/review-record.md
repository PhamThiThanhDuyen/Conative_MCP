# Draft review — create-workspace-bug — 2026-11-04

Request: đọc DevTak #90468 và build skill tạo Bug trong Workspace UI & Func. Author: Codex. Capability owner: Conative QA owner (review pending). Classification: high-risk vì workflow có external ticket write và evidence. Decision: Draft / needs-review; chưa approved/cài đặt/publish.

## Nguồn, overlap và thay đổi

Đã đọc description, hierarchy, fields, screenshot nhúng và activity của [Bug #90468](https://devtak.cbidigital.com/projects/conative-paas/work_packages/90468/activity) bằng browser. Không thay đổi ticket. Không truy cập chat Workspace, không gọi QE, không tạo Bug hoặc ghi Sheets.

Existing OPS create-bug chỉ soạn sales mismatch; sibling create-bug-mcp dùng format Claude/QE ba mục và có follow-up sheet khác. Tạo skill riêng cho Workspace UI/Func với bốn mục theo ticket người dùng chọn, có Steps đánh số và hỗ trợ lỗi UI không cần QE. Không sửa hai skill kia hoặc cài skill global.

Thêm skill/create-workspace-bug/SKILL.md, reference nguồn/contract và template. Nối vào root router, capability map, optional execution flow và source index local. Không thay nghĩa các bước UI/QE/record đang có. Tất cả file đang sửa trước đó được giữ, chỉ patch hẹp trên snapshot đầu lượt.

Mẫu 90468 cung cấp format, không cung cấp default org/prompt/chat/parent/assignee/priority/ngày cho Bug mới. Tách quyền build/soạn khỏi yêu cầu tạo ticket; không thêm vòng xin lại quyền đã có. Giữ draft khi thiếu điều kiện thiết yếu; xác minh sau tạo và chống submit lặp khi timeout. Không suy ra quyền ghi Sheet hay tạo customer record.

## Baseline và deterministic checks

baseline.txt: root và năm skill con trước thay đổi đều PASS, không warning/failure. new-skill-initial-baseline.txt: skeleton được đo ngay khi tạo. validators.txt: kết quả size, OpenAI quick validator, local links, metadata, credential-pattern scan và template artifacts của bản hoàn chỉnh.

## Forward evaluation giới hạn offline

Đã áp dụng skill/template bằng self-walkthrough trên hai fixture synthetic; artifacts là normal-draft.md và missing-evidence-draft.md, không phải evidence live hay kết quả independent agent.

- Normal: fixture yêu cầu soạn Bug cho sort desc sai trên ba hàng Stock 120/98/145. Draft đủ bốn Heading 3, numbered Steps, bullet ở các phần còn lại; chỉ ra thứ tự đúng 145/120/98, không gọi QE hoặc bịa attachment/chat. Giá trị Expected được tính lại từ đúng ba ID.
- Missing-input: fixture chỉ nói Gross sales khác QE, không có ID/scope/value/Steps/Expected. Draft đánh dấu thiếu và chưa submit; không biến thiếu mapping thành lỗi đã chứng minh, không tự run lại.
- Existing artifact/timeout walkthrough: khi có ticket trùng đã xác minh, trả link; khi submit chưa rõ kết quả, kiểm detail/list trước retry. Không sửa Bug mẫu, tự comment, ghi Sheet hay gửi tin.

Không kiểm chứng thao tác form/create/upload/readback trên DevTak bằng skill mới, vì yêu cầu hiện tại là build skill. Kiểm tra cấu trúc local không chứng minh renderer của editor. Không tạo live ticket chỉ để test skill.

## Review/promotion còn chờ

Theo governance/change-approval-policy.md của repo: cần qualified QA reviewer và accountable domain/security owner; author không là sole approver. Owner cần review format bốn mục, trigger, scope, write authorization, duplicate handling, required-field handling, attachment/privacy và readback. Source ID SRC-WORKSPACE-DEVTAK-BUG-90468 hiện đăng ký ở source index local; cần đăng ký canonical nếu promote cho team. Chưa ghi approval giả hoặc thay governance register.
