# Mẫu kết quả và Note ngắn

## Run record tối thiểu

- TC ID, workbook/tab/row và thời điểm đọc live.
- Org, model thực tế, prompt nguyên văn, fixture đã dùng.
- Steps/Expected của snapshot; kết quả từng assertion.
- Chat URL thực tế; UI rows/columns theo stable ID.
- conversationId, Session ID thực tế, tenant/org/environment đã xác minh, turn/thời điểm, trace/observation ID và URL cho mỗi query_data liên quan.
- Đối chiếu phạm vi/data UI công bố | Input/Output thực tế | match/mismatch/blocked; schema/path, rows/totals/pagination/meta/warnings và coverage đã thu. Không chấm Input giống prompt hoặc đưa khác biệt Input ↔ prompt vào Note.
- Field comparison: ID | field/path | UI | Log response Output | Difference | match/mismatch/blocked | lý do.
- Status logic, token live cho phép, phạm vi chưa xác minh và cells được phép ghi.
- Thời điểm hoàn tất thực thi và timezone; Version đúng model dùng `dd/MM/yyyy HH:mm:ss (GMT+7)`. Ghi status/Note/Version cùng batch khi thực thi; sửa Note giữ Version. Không bịa thời điểm cho evidence cũ.

Run record có thể giữ chi tiết so sánh tối thiểu. Note trong sheet chỉ giữ khác biệt, không sao chép toàn bộ record hoặc liệt kê các phần đã pass.

## Note khi có sai lệch

Giữ nhãn `conversion ID` theo format người dùng đã yêu cầu; giá trị là link conversation/chat quan sát được, không phải một ID tự dựng.

```text
- Actual result:
        + UI: [field lệch, giá trị UI và Product ID/Variant ID; tổng lệch nếu có]
        + Log response: [cùng ID/field, giá trị Output hoặc tham số Input tương ứng; observation URL]
        + Difference: [nội dung và phạm vi lệch; dùng count đã kiểm chứng]

- conversion ID: [chat URL thực tế]

- Expected result:
        + UI: [giá trị/hành vi đúng cho những nội dung bị lệch]
```

Chọn một ví dụ có ID cho cùng kiểu sai lệch lặp lại, kèm số dòng ảnh hưởng. Chỉ ghi rounding/precision là khác biệt hiển thị khi đó là bằng chứng; không khẳng định backend tính sai. Không đưa HTTP/body/token, tất cả check đã khớp hoặc setup dài vào Note. Chỉ nêu scope khi cần giải thích khác biệt.

Ví dụ synthetic:

```text
- Actual result:
        + UI: Product ID QA-101: Gross sales=100; tổng top 2=150.
        + Log response: Cùng ID: gross_sales=100.25; tổng đúng 2 ID=150.25. [observation URL]
        + Difference: Gross sales bị mất phần thập phân; tổng thấp hơn 0.25.
- conversion ID: [link chat đã quan sát trong run]
- Expected result:
        + UI: Gross sales=100.25; tổng=150.25.
```

Khi BLOCK, dùng các mục trên để ghi điều kiện thiếu và kỳ vọng cần có; không mô tả missing data thành giá trị sai. Nếu chưa có chat, ghi “Chưa tạo chat”, không dự đoán URL. Khi không có sai lệch, Note chỉ cần link chat hoặc một câu ngắn xác nhận không ghi nhận sai lệch; không thêm dữ liệu đã pass để lấp đầy template.
