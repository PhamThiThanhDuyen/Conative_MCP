# Evidence cho mỗi lần gọi API

Mỗi lần chạy so sánh có một thư mục riêng dưới `evidence/`:

```text
evidence/<org-slug>__<source-slug>/<YYYYMMDDTHHMMSSZ>/
├── manifest.json
├── calls/
│   ├── 001-graphql-variant/
│   │   ├── request.json
│   │   ├── response.json
│   │   └── metadata.json
│   └── 002-data-service-variant/
│       ├── request.json
│       ├── response.json
│       └── metadata.json
└── comparison.md
```

Tên call tiếp tục tăng số thứ tự cho product, phân trang hoặc lần thử lại. Không ghi đè call cũ. `org-slug` và `source-slug` chỉ dùng ký tự an toàn cho đường dẫn; giữ tên org/source gốc trong manifest. Timestamp UTC xác định duy nhất lần chạy.

## Ghi ngay sau từng API call

- `request.json`: method, endpoint không chứa secret, GraphQL operation/query và variables hoặc request body data service, gồm source, kỳ dữ liệu, filter, grain và pagination đã gửi thực tế. Không lưu Authorization, cookie, API key, password hoặc token.
- `response.json`: status HTTP, GraphQL `data`/`errors` hoặc body/lỗi từ data service. Giữ nguyên giá trị và trường dùng để so sánh. Nếu không có JSON response, lưu nội dung quan sát được dưới tên phù hợp và ghi giới hạn trong metadata. Không ghi dữ liệu cá nhân hoặc dữ liệu ngoài phạm vi cần chứng minh kết quả.
- `metadata.json`: API, grain, thời điểm bắt đầu/kết thúc và timezone, thời lượng nếu biết, trạng thái thành công/lỗi, source/channel, khoảng ngày, tên file request/response và phần đã che (nếu có).
- `manifest.json`: org/source, run ID, các call theo đúng thứ tự cùng đường dẫn và trạng thái, quy tắc so sánh áp dụng. Cập nhật manifest sau mỗi call, kể cả call lỗi.
- `comparison.md`: đối chiếu có dẫn đường dẫn tới các call liên quan, giá trị GraphQL/data service, chênh lệch, status theo hợp đồng và lý do chưa thể so sánh. Chỉ tạo kết luận khi đủ dữ liệu.

Nếu công cụ chạy API không xuất được body, lưu ảnh chụp request/response có nhãn cùng metadata, che secret, và nêu rõ evidence chỉ phản ánh phần hiển thị. Không gọi API thêm chỉ để tạo evidence nếu đã có kết quả đáng tin cậy. Nếu evidence cho một call không lưu được, báo thiếu evidence và dừng trước bước ghi status vào Sheet.

Không đưa credential hoặc token vào tên file, nội dung file, ảnh, ghi chú hoặc báo cáo. Giữ nguyên các con số và phạm vi quyết định kết quả so sánh; nếu phải che một phần, ghi cụ thể phần nào đã che để người đọc hiểu giới hạn của evidence.
