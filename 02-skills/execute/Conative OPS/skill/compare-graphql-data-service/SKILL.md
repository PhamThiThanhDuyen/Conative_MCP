---
name: compare-graphql-data-service
description: Chạy các request đọc GraphQL và data service cho một org/source Conative OPS, rồi đối chiếu chỉ tiêu variant và product theo hợp đồng đã xác nhận.
---

# So sánh GraphQL với data service

Đọc [comparison contract](../../references/comparison-contract.md), [workbook contract](../../references/workbook-contract.md) và [evidence contract](../../references/evidence-contract.md). Lấy org, `from_source` và `Channel` từ đúng hàng `Danh sách org`. Dùng hai tab Sales làm danh mục chỉ tiêu cần kiểm tra; không coi các cột kết quả cũ là API contract.

Trước khi gọi API, xác nhận endpoint, query/request, môi trường, kỳ dữ liệu, timezone, filter, grain, phân trang, ánh xạ field và khóa ghép hàng. Tạo thư mục evidence cho lần chạy trước request đầu tiên. Chạy các request đọc với cùng phạm vi; giữ credential và token ngoài file, Sheet, log và báo cáo. Ngay sau **mỗi** lần gọi GraphQL hoặc data service, kể cả khi lỗi, lưu request, response/lỗi và metadata theo evidence contract. Nếu không lưu được evidence, báo rõ và dừng trước lần gọi tiếp theo hoặc trước khi ghi status.

So sánh từng chỉ tiêu có ánh xạ xác nhận. Tách kết quả variant và product. Nêu giá trị GraphQL, data service, chênh lệch và phạm vi; dùng status theo quy tắc đã được bổ sung. Không suy diễn một field tương đương chỉ vì tên gần giống. Nếu một điều kiện thiết yếu chưa rõ hoặc request lỗi, ghi nhận phần bị chặn thay vì báo pass.

Trả về bản ghi so sánh có thể truy vết tới hàng chỉ tiêu, org/source, lần chạy và đường dẫn evidence của từng API call để skill cập nhật Sheet sử dụng. Skill này không tự sửa workbook.
