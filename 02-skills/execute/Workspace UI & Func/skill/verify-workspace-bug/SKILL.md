---
name: verify-workspace-bug
description: Verify a supplied Conative Workspace bug against linked Scenario_UI test cases, rerun them with existing skills, update Google Sheets status and notes, post ticket-scoped PASS/FAIL Activity notes with screenshots, and set the ticket to In testing.
---

# Verify Bug Workspace

Đầu vào: ticket Bug cần verify. Đầu ra: các TC liên quan đã chạy, status/Note/Version trên Sheet và comment Activity chỉ thuộc ticket; status ticket `In testing`. Dùng [flow hiện có](../../references/execution-flow.md); gói là draft/needs-review.

## 1. Đọc ticket và tìm TC

- Đọc ticket hiện tại, description, ảnh và Activity liên quan; ghi ID/URL, Steps, Actual, Expected, org/model/environment và phạm vi lỗi. Không coi “đã fix” là kết quả verify.
- Dùng Google Sheets skill, đọc metadata/header của [workbook nguồn](../../references/sources.md), tìm trong toàn tab `Scenario_UI` theo từng range nhỏ, gồm Note và cột Bug/link hiện có. Đọc hyperlink/rich text nếu nhãn che URL. Khớp đúng ticket ID trong URL hoặc tham chiếu Bug rõ ràng; không match một phần số hoặc chỉ vì status FAILED.
- TC mô tả cùng lỗi nhưng chưa có link cần đối chiếu với scope ticket; chỉ chọn khi quan hệ rõ, ghi lý do. Không chạy mọi TC FAILED. Lập danh sách TC/row/model, liên kết và assertion thuộc ticket; xử lý ID trùng theo [intake](../read-workspace-testcase/SKILL.md).
- Chỉ chạy và ghi model thuộc yêu cầu/context còn hiệu lực hoặc liên kết Bug đã xác minh; không tự mở rộng sang mọi model.
- Không tìm thấy TC hoặc ticket/scope không đọc được: báo phần thiếu, không tự tạo TC hay đánh fixed. Thiếu org/model thiết yếu thì tìm trong context/TC trước khi hỏi.

## 2. Chạy từng TC

Khi đã xác định ticket/TC và bắt đầu verify, chuyển đúng ticket sang `In testing`, đọc lại xác nhận. Nếu transition không có hoặc thiếu quyền, báo blocker và tiếp tục phần độc lập; không chọn status khác.

Dùng [read](../read-workspace-testcase/SKILL.md) → [run UI](../run-workspace-ui-testcase/SKILL.md) → [compare log](../compare-workspace-report-log/SKILL.md) khi kiểm dữ liệu, hoàn tất từng TC trước TC kế. Đọc live và tạo run mới, giữ prompt nguyên văn; xác minh đúng org/model/environment. Không đổi prompt để tái hiện lỗi. Áp dụng gate live trong flow cho thao tác ghi dữ liệu.

Đánh giá riêng: **lỗi ticket còn / không tái hiện / chưa xác minh**, và **kết quả toàn TC** theo mọi assertion bắt buộc. TC fail do lỗi khác không chứng minh ticket còn lỗi; ticket không tái hiện không tự làm TC PASSED. Dùng evidence đúng run; không dùng kết quả cũ hoặc thiếu fixture để kết luận fixed.

## 3. Cập nhật Sheet

Khi người dùng gọi workflow verify đầy đủ này, yêu cầu bao gồm chạy TC, ghi Sheet, comment và chuyển ticket sang `In testing`; kế thừa quyền đó, không hỏi lại. Yêu cầu chỉ đọc/soạn draft được giới hạn tương ứng. Build skill không tự kích hoạt verify live.

Dùng [record](../record-workspace-test-result/SKILL.md) và [format Note](../../assets/test-result-template.md): ghi mọi sai lệch đã chứng minh, gồm lỗi ticket còn và lỗi khác; phân biệt phạm vi bằng mô tả ngắn. Status phản ánh toàn TC, Version là giờ hoàn tất run đúng model. Giữ link ticket đang verify và các Bug reference hiện có để còn truy vết; không giữ mô tả lỗi cũ như phát hiện mới. Đọc lại snapshot/validation trước ghi, readback sau ghi. Nếu TC đã đổi thì chặn writeback cũ.

## 4. Comment Activity

Sau khi xử lý các TC, dùng đúng [mẫu PASS/FAIL](assets/activity-comment-template.md): thời gian kiểm tra, `conversion id`, hình ảnh đính kèm cả PASS/FAIL; chỉ FAIL có `Reason`, viết đơn giản như Note Sheet. Thu ảnh đúng run, liên quan ticket, che dữ liệu nhạy cảm và xác minh ảnh đã lưu. Chỉ comment kết quả thuộc ticket; loại lỗi khác dù Sheet FAILED. Thiếu bằng chứng kết luận thì không ép PASS/FAIL. Không tạo Bug khác hoặc @mention.

Ưu tiên connector đủ chức năng, nếu thiếu dùng browser. Kiểm Activity đã có comment của chính batch/run này trước gửi; timeout thì đọc lại trước retry. Mở lại ticket, xác minh comment, ảnh và status `In testing`; lỗi ở từng đích thì hoàn tất phần độc lập, báo phần chưa ghi. Không tuyên bố đã cập nhật nếu chưa readback.

Trả ticket, TC đã chạy, kết quả ticket và toàn TC, cells đã ghi, comment/ảnh/link và status ticket đã xác minh, cùng blocker. Không có TC liên quan thì trả kết quả tìm kiếm, không comment kết luận verify khi chưa chạy.
