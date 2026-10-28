---
name: add-org-status-columns
description: Chuẩn bị cột status cho một org/source trong ba tab GraphQLV2 thuộc luồng Conative OPS, giữ nguyên kết quả các lần chạy cũ.
---

# Thêm cột status cho org

Đọc [workbook contract](../../references/workbook-contract.md). Xác định đúng org và source từ `Danh sách org`, rồi kiểm tra header và cột status hiện có ở cả ba tab.

Lập kế hoạch cột cần có cho `Danh sách org`, `Sales_by_variant` và `Sales_by_product`: tên header đầy đủ, vị trí, grain, lần chạy, format và validation. Nếu hợp đồng đặt tên/vị trí chưa được người dùng cung cấp hoặc chưa thể xác định từ quy ước được phê duyệt, dừng trước khi tạo cột và nêu đúng thông tin còn thiếu.

Khi đã đủ hợp đồng và được yêu cầu thực hiện, chỉ thêm cột còn thiếu, giữ nguyên cột lịch sử, dữ liệu, công thức và định dạng khác. Kiểm tra lại header và vị trí cột sau thao tác; trả về địa chỉ cột ở cả ba tab. Không ghi status ở bước này.
