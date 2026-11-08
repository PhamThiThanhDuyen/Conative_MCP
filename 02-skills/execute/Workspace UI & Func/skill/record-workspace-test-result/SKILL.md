---
name: record-workspace-test-result
description: Write authorized Conative Workspace QA status, a concise differences-only Note, and the execution timestamp in the matching model Version cell.
---

# Ghi status và Note

Chỉ ghi khi người dùng đã yêu cầu, kể cả quyền ghi còn hiệu lực trong cùng quy trình. Yêu cầu sửa Note không tự cho phép chạy lại TC, đổi status hoặc cập nhật TC khác; giữ Version của lần chạy đã có.

1. Đọc metadata và `get_cells` của TC ID, prompt, headers, status, Note và Version của đúng model ngay trước ghi. Dùng [column contract](../../references/sheet-column-contract.md); tìm theo header, không hardcode L2/N2.
2. Xác minh snapshot đang ghi vẫn đúng TC/prompt/org đã chạy. Nếu prompt thay đổi trong lúc chạy, giữ bằng chứng lần cũ nhưng không ghi kết quả cũ như kết quả của prompt mới.
3. Đọc validation của ô status. Ánh xạ kết luận sang đúng token được phép. Với cột đã quan sát: `FAILED`, `PASSED`, `BLOCK`; không ghi `PARTIAL`, `FAIL`, `Not Run` nếu dropdown không cho phép.
4. Soạn Note theo [mẫu](../../assets/test-result-template.md): ngắn, chỉ các sai lệch; Actual có UI/Log response/Difference, link ở nhãn `conversion ID`, Expected có UI. Chọn ví dụ có ID, giá trị UI và Output log; bỏ các kiểm tra đã khớp, payload và thông tin setup dài.
5. Mỗi lần thực thi và ghi status, ghi cùng batch status, Note và Version đúng model. Version là thời điểm hoàn tất thực thi đã ghi trong run record, dùng giờ Việt Nam `dd/MM/yyyy HH:mm:ss (GMT+7)`; không dùng thời điểm sửa Note làm thời điểm chạy. Dùng `updateCells` với mask `userEnteredValue`, giữ format/validation và cột model khác. Chỉ sửa Note thì không đổi status/Version. Thiếu cột Version của model thì báo phần thiếu, không mượn cột khác hoặc tự thêm cột.
6. Đọc lại và so khớp text/token và Version thực tế. Kiểm tra hiển thị Google-rendered khi khả dụng; giữ bố cục hiện có, không tự resize cả sheet. Báo chính xác cells đã ghi và link.

`FAILED` chỉ khi có sai lệch đã chứng minh. Thiếu log đúng run, mapping, ID hoặc scope không phải bằng chứng giá trị sai; không chấm PASSED toàn bộ khi còn assertion bắt buộc chưa xác minh. Xem [comparison contract](../../references/comparison-contract.md) để xử lý trường hợp vừa có fail vừa có blocker.
