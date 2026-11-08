---
knowledge_id: QA-WORKSPACE-DEVTAK-BUG-001
knowledge_type: qa-intelligence
source: SRC-WORKSPACE-DEVTAK-BUG-90468
owner: Conative QA owner (review pending)
authority: source-derived
scope: Workspace UI and functional Bug drafting and authorized DevTak creation
target_release: current
status: needs-review
last_verified: 2026-11-04
supersedes: []
---

# Contract Bug từ ticket mẫu 90468

## Nguồn đã đọc

[Bug 90468](https://devtak.cbidigital.com/projects/conative-paas/work_packages/90468/activity) được đọc qua browser ngày 04/11/2026 theo yêu cầu người dùng. Source ID được đăng ký tại [source index của gói](../../../references/sources.md). Đây là mẫu cấu trúc do người dùng chọn, không phải phê duyệt toàn bộ nghiệp vụ hoặc cấu hình mặc định cho mọi Bug.

Quan sát live:

- Project `Conative PaaS`, project slug `conative-paas`; Type `Bug`, status `New`.
- Title: `[OpenUI & UI Platform]_Lỗi sort sai thứ tự trên report của workspace`.
- Hierarchy: `[Internal] OpenUI & UI Platform` (#77761) → `[OpenUI & UI Platform]_Fix bug` (#90410) → Bug #90468.
- Description có bốn heading cấp 3. `Thông tin:` có bullet org, prompt, conversion, thời gian kiểm tra; `Steps:` là danh sách đánh số; `Actual result:` và `Expected result:` dùng bullet.
- Mẫu mô tả org `Demo 7`, prompt `Which products could sell more in last 3 month?`; Steps mở conversation rồi sort desc cột stock. Actual mô tả sort sai và có ảnh; Expected yêu cầu thứ tự từ lớn xuống nhỏ.
- Screenshot hiển thị thứ tự Stock không giảm dần. Đây là evidence có sẵn của ticket mẫu; chưa tự chạy lại report hoặc kiểm toàn bộ dataset trong lần đọc này.
- Files có một ảnh `Screenshot_2026-11-04_at_11.01.42.png`. Activity ghi đổi Description, gán Assignee/Accountable và đổi Priority từ Normal thành High. Không thấy xác nhận fix/retest trong activity đã đọc.

Giá trị org, prompt, chat, thời điểm, parent, priority, người phụ trách và ngày của mẫu không được mang sang Bug mới. `New` chỉ là status quan sát ở mẫu; kiểm tra workflow/default live cho ticket mới, không ép theo mẫu.

## Thông tin tối thiểu và phần mở rộng

Để soạn: dùng bằng chứng hiện có và đánh dấu chỗ thiếu. Để submit: cần đích được yêu cầu, lỗi cụ thể, Steps đủ tái hiện, Actual có căn cứ, Expected có nguồn, và các trường bắt buộc của form đã resolve. Chat URL hoặc ảnh không có thì nói rõ; không tự dựng để lấp template. Khi không có org vì lỗi xảy ra trước chọn org, ghi rõ hoàn cảnh thay vì bịa tenant.

`conversion` giữ cách gọi trong mẫu và chứa URL conversation đã quan sát. TC ID/model chỉ thêm khi có thật. Giữ prompt nguyên văn, không thêm yêu cầu ID/scope vào prompt gốc. Nếu nguồn có các snapshot khác nhau, chỉ dùng một run đã định danh và chỉ rõ Expected lấy từ snapshot nào.

Theo cập nhật 05/11/2026, lỗi UI dùng trạng thái/control/report và ảnh; lỗi value đối chiếu Output log Langfuse của đúng turn, ghi observation URL. Lỗi value phải nối đúng ID và cùng source/kỳ/timezone/grain/filter; thiếu điều kiện này thì mô tả giới hạn, không gán nguyên nhân backend. Nếu Input log hữu ích cho tái hiện, thêm phần tối thiểu đã che secrets; không dump response/auth hoặc toàn bộ fields. Các đoạn request dài cần code snippet thật của editor nếu được dùng.

Với sort, Expected dựa vào yêu cầu/control đã quan sát: desc giảm dần, asc tăng dần; null/ties/pagination chỉ được khẳng định theo quy tắc có nguồn. Khi chỉ kiểm một trang, ghi đúng phạm vi. Không biến screenshot mẫu thành số liệu của run mới.

## Đích và trạng thái sau ghi

Mặc định tham chiếu project mẫu khi người dùng yêu cầu Bug Workspace trong project này; trước khi gửi phải xác minh project live và mọi yêu cầu đích khác trong chat. Parent #90410 chỉ là parent của mẫu, không tự chọn cho run mới. Thiếu parent/người phụ trách không bắt buộc thì có thể để trống theo form; nếu form bắt buộc mà chưa có căn cứ thì hỏi phần đó.

Tạo Bug là thao tác ghi ticket, khác với rerun tạo business entity trên môi trường khách hàng. Nếu cần tái hiện bằng thao tác live, nạp [live testing standard](../../../../../../03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md) và áp dụng đúng gate; không rerun chỉ để có ảnh.

Chỉ coi ticket đã tạo khi trang detail mới có ID/URL thực và nội dung đọc lại khớp. Nếu title có nhưng description/file chưa lưu, báo phần thiếu, hoàn tất sửa trong cùng ticket khi được phép; không tạo ticket thứ hai. Không tự comment/@mention, thêm watchers, đổi sharing hoặc gửi thông báo riêng. Không suy ra quyền ghi Google Sheet từ yêu cầu tạo Bug.
