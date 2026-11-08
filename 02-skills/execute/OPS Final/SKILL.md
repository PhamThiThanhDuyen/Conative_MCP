---
name: ops-summary-api-to-sheet
description: Chạy API Summary Variant rồi Summary Product trong Postman và ghi kết quả vào Google Sheet OPS.
---

# OPS Final — Run Summary API và ghi Google Sheet

Dùng khi người dùng yêu cầu kiểm tra Summary cho một organization, source và
timerange. Đầu ra là một cột mới trong từng tab `Sales_by_variant` và
`Sales_by_product`, có kết quả từng metric và ghi chú cho ô Failed.

## Cách bắt đầu

Ví dụ: “Dùng OPS Final, kiểm tra organization Mizmooz, source Magento,
từ 2026-01-01 đến 2026-10-21 và cập nhật Google Sheet.”

Đọc [FLOW.md](FLOW.md) để theo dõi toàn bộ quy trình.
Tên workspace, request và file Sheet ở [run-settings.md](references/run-settings.md).
Chỉ yêu cầu tạo/sửa skill thì chỉ sửa tài liệu, chưa chạy API hay ghi Sheet.

## Thứ tự thực hiện

1. Đọc metadata và ba tab Google Sheet. Nhận đủ organization, source,
   from_date và to_date. Đối chiếu đúng dòng trong `Danh sách org`.
2. Xác định vị trí thêm một cột mới trong mỗi tab kết quả theo
   [sheet-contract.md](references/sheet-contract.md). Tạo cột, header và dropdown
   status giống cột kiểm tra trước.
   Giữ các ô kết quả trống cho đến khi chạy xong API tương ứng.
3. Mở Postman trong browser in-app, chọn đúng workspace, collection,
   environment và folder `Final`. Theo [execute-api-ops.md](execute-api-ops.md),
   chạy `Login`, lấy đúng organization ID rồi chạy `Choose_Org`.
4. Chạy `Summary_Variant` với query `Sales_by_variant`. Chờ request và các
   script hoàn tất; chỉ đọc console/test result của lần chạy này.
5. Dùng [record-ops-summary-results](skill/record-ops-summary-results/SKILL.md)
   để ghi và đọc lại kết quả Variant.
6. Sau khi xác minh Variant đã lưu, chạy `Summary_Product` với query
   `Sales_by_product`; ghi và đọc lại kết quả Product bằng cùng quy tắc.
7. Báo số Passed, Failed, N/A và địa chỉ cột của từng tab theo
   [mẫu báo cáo](assets/run-report-template.md).

## Quy tắc chính

- Chạy tuần tự Variant → Product. Một metric Failed vẫn là kết quả hợp lệ;
  ghi đầy đủ rồi tiếp tục Product. Nếu bị lỗi thực thi/ghi Sheet, dừng ở bước đó.
- Tick xanh → `Passed`; tick đỏ → `Failed` và cell note chứa nguyên văn dòng
  lỗi; metric không xuất hiện trong lần chạy hoàn tất → `N/A`.
- Chưa chạy hoặc chạy lỗi không phải N/A. Không suy ra Passed từ HTTP 200,
  giá trị bằng 0, dữ liệu rỗng hay status của lần chạy cũ.
- Không tự đặt tolerance, sửa công thức test hoặc thay kết quả script.
- Chỉ thay input cần thiết cho lần chạy; không Save collection/query,
  không sửa script. Dùng cơ chế truyền token có sẵn của `Choose_Org`.
- Không ghi credentials, token, cookie hoặc toàn bộ auth response vào tài liệu,
  Sheet, console export hay file bằng chứng.
- Nếu bị kẹt: giữ browser in-app mở tại bước lỗi, nêu điều đã kiểm tra,
  hỏi người dùng hỗ trợ và chờ phản hồi. Tiếp tục đúng bước sau khi được hỗ trợ.
  Không tự đóng tab, chạy lại toàn bộ hay tạo cột trùng.
