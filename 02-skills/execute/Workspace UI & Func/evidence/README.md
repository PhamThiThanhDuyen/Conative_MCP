# Bằng chứng QA

Lưu bằng chứng được phép theo `<test-case-id>/<run-timestamp>/`. Tách các lần chạy khác prompt; source snapshot và kết quả phải truy được về cùng run. Với Langfuse, ghi conversationId, session/trace/observation ID/URL, turn/thời điểm và field/path; không gộp query khác scope.

Evidence QE lịch sử giữ nguyên nguồn/ngày; không đổi nhãn thành Log response hoặc dùng như log run mới. Thư mục `langfuse-comparison-2026-11-05/` ghi migration và synthetic validation; không phải kết quả PASSED một TC live.

Chỉ giữ các ID, field, scope và sai lệch cần tái hiện. Không lưu password, token, cookies, OTP, browser storage/session hoặc raw auth response. Không dump toàn bộ payload customer data khi vài field đủ chứng minh.

Routine run ưu tiên run record tối thiểu và chat URL. Lưu screenshot khi được yêu cầu làm evidence/bug hoặc host cần proof; chỉ vùng có liên quan, không auth pane, và xử lý dữ liệu nhạy cảm trước khi lưu/chia sẻ. Không tự tạo bug hoặc tải evidence ra dịch vụ khác.

`skill-build-2026-11-04/` chứa baseline, kiểm tra và draft review của lần authoring skill; đây không phải evidence của một lần chạy live mới.
