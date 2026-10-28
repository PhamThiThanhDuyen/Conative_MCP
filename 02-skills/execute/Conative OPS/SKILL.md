---
name: conative-ops
description: Điều phối kiểm thử doanh số theo organization và source, so sánh GraphQL với data service, rồi ghi trạng thái vào workbook GraphQLV2. Dùng khi người dùng yêu cầu chạy hoặc cập nhật kết quả Conative OPS.
---

# Conative OPS

## Nguồn dữ liệu

Workbook: [GraphQLV2](https://docs.google.com/spreadsheets/d/1Ds-d0KrVq7AUSgz-WKcS5UtdGxxvHnn-HxMWCqMkWys/edit?usp=sharing). Ba tab của luồng này là `Danh sách org`, `Sales_by_variant` và `Sales_by_product`. Đọc [workbook-contract.md](references/workbook-contract.md) trước khi chọn org hoặc sửa cột. Các tab khác trong workbook nằm ngoài luồng hiện tại.

## Luồng tổng quan

1. Tìm đúng org trong `Danh sách org`; lấy `from_source` và `Channel` từ hàng tương ứng. Nếu một org có nhiều hàng/source, xác định đúng cặp org–source được yêu cầu trước khi chạy.
2. Dùng [add-org-status-columns](skill/add-org-status-columns/SKILL.md) để chuẩn bị cột status cho org ở `Danh sách org`, `Sales_by_variant` và `Sales_by_product`.
3. Dùng [compare-graphql-data-service](skill/compare-graphql-data-service/SKILL.md) để chạy GraphQL và data service với cùng phạm vi, lưu evidence ngay sau mỗi lần gọi API, rồi đối chiếu kết quả theo variant và product.
4. Dùng [update-google-sheet-status](skill/update-google-sheet-status/SKILL.md) để ghi kết quả vào hai tab Sales, sau đó tổng hợp và cập nhật hàng org trong `Danh sách org`.

Đọc [comparison-contract.md](references/comparison-contract.md) khi thiết lập request, quy tắc đối chiếu và status. Tuân thủ [evidence-contract.md](references/evidence-contract.md) cho mọi lần gọi API; lưu evidence tại `evidence/`. Dùng [run-report-template.md](assets/run-report-template.md) để lưu tóm tắt một lần chạy nếu cần báo cáo.

## Ranh giới hiện tại

Đây là bộ khung. Chưa có endpoint, query, cách ghép hàng, tolerance, bộ giá trị status, quy tắc tổng hợp và tên cột mới được phê duyệt. Không tự suy diễn các thông tin đó từ cột lịch sử. Khi thực thi, xác minh hợp đồng còn thiếu trước bước phụ thuộc vào nó. Chỉ cập nhật workbook và org/source được yêu cầu; đọc lại những ô đã ghi. Không lưu token hoặc credential vào file, Sheet hay báo cáo.
