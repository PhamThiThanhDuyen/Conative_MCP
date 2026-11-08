# Cấu hình của flow

Các tên dưới đây do người dùng cung cấp. Khi UI khác tên, kiểm tra với người
dùng thay vì tự chọn resource gần giống.

## Google Sheet

- Workbook: [GraphQLV2](https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit).
- Spreadsheet ID: `1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys`.
- Tab mapping: `Danh sách org`.
- Tab kết quả Variant: `Sales_by_variant`.
- Tab kết quả Product: `Sales_by_product`.
- Ngày kiểm tra trên header: `Asia/Ho_Chi_Minh`.

Đã đọc metadata và các vùng header/metric vào 2026-11-08. Hai tab kết quả
có header `ID`, `Group`, `Name`, `Key` ở hàng 1. Tab mapping có header
`ORG`, `from_source`, `Channel` ở hàng 1 và dữ liệu organization từ hàng 3.
Phải đọc lại dữ liệu live mỗi lần chạy, không dùng vị trí snapshot làm hằng số.

## Postman

| Mục | Tên |
| --- | --- |
| Workspace | DUYENQA_GraphQL |
| Collection | Duyen_GraphQL_Live |
| Environment | OpenSearch_Duyen |
| Folder gốc | Final |
| Folder đăng nhập | SignIn |
| Request đăng nhập | Login |
| Request chọn organization | Choose_Org |
| Đoạn URL để truyền ID | switch-organization/ |
| Folder / request Variant | Summary_Variant / Summary_Variant |
| Query Variant | Sales_by_variant |
| Folder / request Product | Summary_Product / Summary_Product |
| Query Product | Sales_by_product |
| Biến token cần kiểm tra | accessToken_Mizmooz |
| Input query | from_date, to_date, from_source |

Tên biến token được giữ đúng theo yêu cầu; không đổi theo organization đang
chọn. Không có credentials/token/endpoint đầy đủ trong bộ skill này. Đọc chúng
từ request và session có sẵn lúc thực thi. Chưa kiểm tra trực tiếp collection
hoặc chạy API khi xây bộ tài liệu này.

## Phạm vi

Chỉ đọc các API Summary và ghi kết quả kiểm tra vào hai tab được chỉ định.
Giữ nguyên script, công thức so sánh, query fields và các filter ngoài input
được yêu cầu. Không áp dụng quy tắc của Conative MCP Round 2 như chạy Claude,
field mapping QE, xóa filter active hoặc tự đặt forecast window vào flow OPS.

Không thay timezone của API nếu người dùng chưa yêu cầu. Nếu query có timezone
hoặc quy ước bao gồm/không bao gồm ngày cuối, kiểm tra cách request hiện tại
đang dùng. Nếu mâu thuẫn với timerange yêu cầu hoặc chưa thể xác định đúng
phạm vi, hỏi người dùng; không dùng timezone workbook thay cho timezone API.

Đọc các chính sách repository trước thao tác liên quan:
[bảo mật](../../../../03-knowledge/governance/information-security-policy.md),
[live testing](../../../../03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md),
[quản lý thay đổi skill](../../../../03-knowledge/governance/change-approval-policy.md).
