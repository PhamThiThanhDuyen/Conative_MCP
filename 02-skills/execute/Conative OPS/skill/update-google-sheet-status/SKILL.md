---
name: update-google-sheet-status
description: Ghi status đối chiếu GraphQL/data service vào Sales_by_variant và Sales_by_product, rồi tổng hợp lên hàng org trong Danh sách org của GraphQLV2.
---

# Cập nhật status vào Google Sheet

Đọc [workbook contract](../../references/workbook-contract.md), [comparison contract](../../references/comparison-contract.md) và [evidence contract](../../references/evidence-contract.md). Nhận bản ghi so sánh của đúng org/source/lần chạy cùng đường dẫn evidence của từng API call. Kiểm tra manifest và các file evidence tồn tại trước khi ghi status; nếu thiếu, dừng ghi và báo lần gọi bị thiếu. Xác nhận cột status đã tồn tại và các giá trị status được validation của workbook cho phép.

1. Ghép từng bản ghi variant/product với đúng hàng chỉ tiêu bằng khóa được phê duyệt. Kiểm tra trạng thái ô hiện tại; chỉ ghi các ô status thuộc lần chạy này trong `Sales_by_variant` và `Sales_by_product`.
2. Đọc lại các ô vừa ghi và xác định tập hàng đã chạy, chưa chạy, lỗi hoặc chưa thể so sánh.
3. Áp dụng quy tắc tổng hợp đã được phê duyệt để tính status variant và product, sau đó status cho đúng hàng org/source trong `Danh sách org`. Không mặc định mọi hàng trống là pass hoặc fail.
4. Ghi và đọc lại các ô tổng hợp; báo địa chỉ ô, giá trị trước/sau và các hàng bị chặn.

Nếu thiếu khóa ghép, bộ giá trị status, quy tắc tổng hợp hoặc cột đích, dừng phần ghi phụ thuộc vào thông tin đó và báo rõ nguyên nhân. Không ghi đè kết quả lịch sử hoặc các org/source khác.
