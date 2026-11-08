# Phạm vi và trạng thái kiểm tra bộ skill

- Ngày tạo: 2026-11-08, theo ngày Việt Nam.
- Yêu cầu: tạo bộ flow/skill OPS Final riêng cho Summary API → Google Sheet.
- Nguồn: yêu cầu người dùng trong chat và workbook GraphQLV2 đã đọc qua connector.
- Mẫu cấu trúc: Conative MCP Final, gồm SKILL.md, tài liệu thực thi, references,
  assets và skill ghi kết quả. Không sửa bộ skill mẫu.
- Lý do tách riêng: OPS dùng Postman GraphQL/script console và workbook khác;
  không chạy Claude hay áp mapping QE Round 2.
- Phạm vi thay đổi: chỉ thư mục OPS Final; không cài vào thư viện skill,
  không publish hoặc ghi approval register bên ngoài thư mục này.

## Kiểm tra đã thực hiện

Xem [validation.txt](validation.txt) để biết kết quả lệnh thực tế.
Baseline khởi tạo của hai SKILL.md: mỗi file 12 words, 4 lines, đều PASS.
Kiểm tra gồm size, YAML/frontmatter, link/path, credential scan và helper offline.

Hai tình huống tạo artifact bằng helper:

1. Run giả lập hoàn tất: xanh Gross Sales, đỏ Total Sales, thiếu Ad spend →
   plan có Passed, Failed kèm nguyên văn note, N/A. Xem [normal-plan.json](normal-plan.json).
2. Run giả lập chưa hoàn tất → helper từ chối, không tạo plan mới;
   không ghi N/A thay lỗi thực thi. Kết quả trong validation.txt.

Unit tests bổ sung kiểm tra console rỗng, unknown metric, Failed thiếu note,
dòng/tên trùng, subcheck và tách dòng Product khỏi Variant.

## Giới hạn

Đã xác minh ba tab, header, vị trí lịch sử kiểm tra và Name/Key trong Sheet.
Chưa chạy Login, Choose_Org, Summary_Variant hoặc Summary_Product; chưa sửa Sheet.
Chưa kiểm chứng token propagation, schema reload, console output hoặc quyền
chèn cột/ghi cell note bằng một lần chạy live.

Đây là bản đã xây dựng và kiểm tra offline, chưa có phê duyệt dùng chung.
Theo change-approval-policy.md của repository, thay đổi liên quan credentials,
live data và external transmission thuộc nhóm high-risk. Trước khi cài/publish
cho cả team cần qualified reviewer và accountable domain/security owner review,
sau đó có approval record. Không tự coi việc tạo file là đã qua các review này.


## Cập nhật dropdown status — 2026-11-08

- Nguồn: người dùng yêu cầu thêm dropdown như các cột khác và viết hướng dẫn
  bằng câu ngắn, dễ hiểu.
- Sửa SKILL.md chính, skill ghi kết quả, FLOW.md và sheet-contract.md.
- Bỏ hướng dẫn cũ không sao chép validation. Cột kết quả mới cần giữ dropdown,
  các lựa chọn, màu và kiểu hiển thị của cột mẫu trong cùng tab.
- Với run đã có, chỉ thêm dropdown; giữ header, status và note, không chạy lại API.
- Đã áp dụng cho run CBI_DEMO3 / shopify, Oct 01–31 2026: Variant GQ2:GQ76
  và Product CL2:CL65. Đọc lại đủ 139 ô; status và note không đổi.
- Đã mở dropdown trên cả hai tab: có Passed, Failed, N/A và các lựa chọn cũ.
  Chip màu hiển thị đúng; note Failed của Product vẫn xem được.
- Các kiểm tra tự động và việc sửa run đang có được ghi trong validation.txt.
- Loại thay đổi: behavioral (định dạng đầu ra). Chỉ cập nhật bản local theo yêu
  cầu; không cài, publish hoặc ghi nhận là đã được duyệt dùng chung.
