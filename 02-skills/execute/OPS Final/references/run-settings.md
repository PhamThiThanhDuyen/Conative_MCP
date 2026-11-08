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
| Folder List Variant | List_Variant |
| API List Variant đầu tiên | Variant_List_Product_Info |
| Folder List Product | List_Product |
| Query List Variant / Product | Sales_by_variant / Sales_by_product |
| Limit mỗi trang List | 20 |
| Offset mỗi API List | 0, 20, 40, 60, 80 |
| Mục tiêu mỗi API List | 100 item |
| Biến token cần kiểm tra | accessToken_Mizmooz |
| Input query | from_date, to_date, from_source |

Tên biến token được giữ đúng theo yêu cầu; không đổi theo organization đang
chọn. Không có credentials/token/endpoint đầy đủ trong bộ skill này. Đọc chúng
từ request và session có sẵn lúc thực thi. Chưa kiểm tra trực tiếp collection
hoặc chạy API khi xây bộ tài liệu này.

## Phạm vi

Flow tổng mặc định: mỗi org/source chạy Summary Variant → ghi và xác minh →
List Variant → ghi và xác minh → Summary Product → ghi và xác minh →
List Product → ghi và xác minh. Xong phạm vi được yêu cầu của org mới chuyển org.
Nếu người dùng chỉ yêu cầu một phần thì chỉ chạy phần đó, theo thứ tự tương đối.
Mỗi tab có cột Summary và List riêng cho từng org/source/timerange/run.

Đọc API Summary hoặc List và ghi kết quả vào hai tab được chỉ định.
Summary giữ nguyên script. List được cập nhật offset trong query và script
để hai phía kiểm tra cùng trang; không đổi logic so sánh, tolerance, query fields
hoặc filter khác. Chỉ sửa tạm cho lần chạy, không Save collection.

Danh sách các API còn lại phải đọc từ folder live khi thực thi; chưa có tên
được xác minh thì không tự đặt tên. Với List_Variant, bắt đầu bằng
`Variant_List_Product_Info`, sau đó theo thứ tự folder; với List_Product,
theo thứ tự folder. Không tự tạo request nếu thiếu request/query.

Không áp dụng quy tắc của Conative MCP Round 2 như chạy Claude,
field mapping QE, xóa filter active hoặc tự đặt forecast window vào flow OPS.

Không thay timezone của API nếu người dùng chưa yêu cầu. Nếu query có timezone
hoặc quy ước bao gồm/không bao gồm ngày cuối, kiểm tra cách request hiện tại
đang dùng. Nếu mâu thuẫn với timerange yêu cầu hoặc chưa thể xác định đúng
phạm vi, hỏi người dùng; không dùng timezone workbook thay cho timezone API.

Đọc các chính sách repository trước thao tác liên quan:
[bảo mật](../../../../03-knowledge/governance/information-security-policy.md),
[live testing](../../../../03-knowledge/qa-intelligence/standards/live-environment-testing-standard.md),
[quản lý thay đổi skill](../../../../03-knowledge/governance/change-approval-policy.md).
