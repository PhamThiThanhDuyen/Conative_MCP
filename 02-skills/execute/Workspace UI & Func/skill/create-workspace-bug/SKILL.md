---
name: create-workspace-bug
description: Draft or create Conative Workspace UI and functional bugs in DevTak using ticket 90468 as the report format. Use when the user requests a Workspace bug from a verified test run or supplied evidence.
---

# Tạo Bug Workspace trên DevTak

Đầu ra: nội dung Bug tiếng Việt theo [template](assets/bug-template.md), và ID/link thực tế nếu đã tạo. Đọc [contract và nguồn mẫu](references/devtak-bug-contract.md) trước khi soạn. Gói đang draft/needs-review; không tự cài đặt hoặc công nhận approved.

## Chốt đầu vào

- Dùng TC snapshot và evidence của đúng run: org, prompt nguyên văn, Steps, Expected, chat URL, thời điểm kiểm tra và sai lệch đã chứng minh. Đọc lại TC bằng [intake](../read-workspace-testcase/SKILL.md) khi người dùng yêu cầu; không tự rerun UI hoặc query để viết Bug.
- Lỗi UI như sort/layout có thể dùng evidence UI. Lỗi số liệu dùng đối chiếu đã xác minh cùng scope theo [comparison contract](../../references/comparison-contract.md). Thiếu mapping/ID không tự trở thành lỗi dữ liệu; scope sai có thể là lỗi riêng có bằng chứng.
- Tận dụng context và quyền còn hiệu lực. Thiếu thông tin thì hoàn tất bản nháp, đánh dấu `Chưa cung cấp`/`Chưa xác minh`; chỉ hỏi phần thiết yếu không tìm được. Không bịa giá trị, ảnh, thời điểm, nguyên nhân hoặc Expected ngoài TC/nguồn có căn cứ.

## Soạn Bug

1. Tiêu đề: `[OpenUI & UI Platform]_<mô tả lỗi cụ thể>`. Giữ prefix khác nếu người dùng chỉ định. Tóm tắt thao tác gây lỗi và hành vi quan sát được.
2. Dùng bốn Heading 3 thực: `Thông tin:`, `Steps:`, `Actual result:`, `Expected result:`. Thông tin/Actual/Expected dùng bullet; Steps đánh số. Khi nhập editor, kiểm tra cấu trúc đã render, không để ký tự Markdown thay heading/list.
3. Thông tin gồm org, prompt, `conversion` là chat URL thực tế, thời gian kiểm tra. Thêm TC ID/model/source/kỳ/timezone nếu cần tái hiện; phân biệt thời điểm run với lúc soạn ticket. Không đổi thời gian lịch sử sang giờ hiện tại.
4. Actual nêu sai lệch cụ thể và evidence; lỗi giá trị có ID, field, UI, Output log và chênh lệch đã xác minh; dẫn observation đúng run. Expected mô tả kết quả đúng có căn cứ. Ảnh liên quan nằm dưới Actual; thiếu ảnh ghi `Chưa đính kèm`.

## Tạo và xác minh

- “Build skill” hoặc “soạn Bug” chỉ tạo artifact local. Chỉ gửi DevTak khi người dùng yêu cầu tạo ticket ở đích xác định; kế thừa yêu cầu đó, không thêm bước xin lại quyền khi scope không đổi. Không sửa ticket mẫu 90468.
- Áp dụng [information security](../../../../../03-knowledge/governance/information-security-policy.md). Chỉ đưa evidence tối thiểu được phép lên đích được yêu cầu; che secrets/customer data. Dùng session UI đang có; thiếu đăng nhập thì để người dùng đăng nhập qua UI, không hỏi password trong chat.
- Ưu tiên connector đủ khả năng; nếu không có, dùng browser control. Xác minh project, Type `Bug`, title, description và các thuộc tính bắt buộc hiện tại. Parent, assignee, accountable, priority, ngày/version lấy từ yêu cầu hoặc quy định đã xác minh; không sao chép giá trị mẫu.
- Tìm Bug liên quan bằng TC/title/chat trong project khi có search. Nếu thấy ứng viên trùng, đọc đối chiếu; chỉ khi xác nhận trùng thì trả link và không tự tạo trùng hoặc sửa ticket cũ nếu chưa được yêu cầu. Không xác minh được search thì nêu giới hạn, không khẳng định không có trùng.
- Hoàn thiện nội dung, kiểm tra heading/list/ảnh và đích trước Submit. Thiếu điều kiện thiết yếu hoặc không đủ quyền thì giữ draft và nêu blocker. Lỗi submit/timeout chưa rõ kết quả: kiểm tra UI/list trước retry; không gửi lặp khi chưa loại trừ đã tạo.
- Sau tạo, mở ticket và đọc lại Type, project, title, description, thuộc tính đã yêu cầu và file thực tế. Trả ID/link đã quan sát, ảnh nào có/thiếu, và phần chưa xác minh; không tuyên bố thành công chỉ từ click/toast.

Không tự ghi Sheet hoặc đổi status vì đã tạo Bug. Khi người dùng yêu cầu, dùng [record](../record-workspace-test-result/SKILL.md), giữ nội dung hiện có và chỉ thêm Bug reference vào ô được chỉ định, rồi readback. Nhận “stop” thì ngừng action mới.
