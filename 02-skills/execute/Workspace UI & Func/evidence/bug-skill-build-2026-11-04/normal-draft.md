Title: [OpenUI & UI Platform]_Sort desc cột Stock chưa sắp xếp giảm dần

### Thông tin:
- org: Synthetic QA
- prompt: Show inventory for synthetic products.
- conversion: Chưa cung cấp
- Thời gian kiểm tra: 04/11/2026 11:30 Asia/Ho_Chi_Minh (fixture synthetic)
- TC ID: SYNTHETIC-SORT-001; phạm vi: ba hàng của trang hiện tại.

### Steps:
1. Mở report inventory của fixture Synthetic QA.
2. Chọn sort desc cột Stock.

### Actual result:
- Sau sort desc, thứ tự ID/Stock: QA-A=120, QA-B=98, QA-C=145; hàng QA-C có Stock lớn hơn hai hàng trước.
- Hình ảnh: Chưa đính kèm.

### Expected result:
- Theo yêu cầu sort desc của fixture: QA-C=145, QA-A=120, QA-B=98.
