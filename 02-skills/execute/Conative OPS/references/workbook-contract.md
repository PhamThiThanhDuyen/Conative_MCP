# Workbook contract — GraphQLV2

Nguồn: https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit?usp=sharing

Đã kiểm tra metadata ngày 2026-10-27. Trước mỗi lần ghi, đọc lại metadata, header, vùng dữ liệu và validation vì workbook có thể thay đổi.

| Tab | Vai trò | Cấu trúc header quan sát được |
| --- | --- | --- |
| `Danh sách org` | Xác định org, `from_source`, `Channel`; nhận status tổng hợp | Hai hàng đầu là header; các cột đầu gồm `ORG`, `from_source`, `Channel`. Các cột tiếp theo thể hiện ngày chạy và loại `Summary variant`/`Summary product`. |
| `Sales_by_variant` | Danh mục chỉ tiêu variant và status theo org/lần chạy | Hàng 1 là header; các cột đầu gồm `ID`, `Group`, `Name`, `Key`, `Type`; sau đó là nhiều cột kết quả cũ. |
| `Sales_by_product` | Danh mục chỉ tiêu product và status theo org/lần chạy | Hàng 1 là header; các cột đầu gồm `ID`, `Group`, `Name`, `Key`, `Type`; sau đó là nhiều cột kết quả cũ. |

## Khi thao tác

- Tìm org theo tên chính xác và kiểm tra cặp `ORG` + `from_source`/`Channel`. Không lấy source từ tên org hoặc tên cột lịch sử.
- Xác định cột status hiện có bằng header đầy đủ và phạm vi lần chạy. Chỉ tạo cột mới khi chưa có cột phù hợp; không ghi đè dữ liệu lịch sử.
- Chưa chốt cách đặt tên cột status mới, vị trí chèn, định dạng, validation, và liệu `Danh sách org` cần một hay hai cột status cho variant/product. Bổ sung hợp đồng này trước khi tạo cột.
- Xác định hàng chỉ tiêu bằng khóa được phê duyệt từ các cột nhận dạng. Không mặc định `Name` là duy nhất.
- Ghi và đọc lại đúng ô theo tab, org, source, grain và lần chạy. Giữ nguyên công thức, ghi chú và định dạng ngoài phạm vi cập nhật.
