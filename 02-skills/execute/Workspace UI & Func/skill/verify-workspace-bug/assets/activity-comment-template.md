# Format note verify trong Activity

Dùng đúng các nhãn dưới đây. Status của comment là kết quả **lỗi thuộc ticket**, độc lập status toàn TC trên Sheet. Status workflow của ticket là **In testing**, cho cả PASS và FAIL; không chuyển Closed/Resolved. Một comment cho mỗi batch, ghi TC/model bên cạnh link để phân biệt các prompt.

## PASS

```text
- Status: PASS
- Thời gian kiểm tra: [dd/MM/yyyy HH:mm:ss (GMT+7)]
- conversion id: [TC ID / model: link conversation của prompt verify]
- Hình ảnh đính kèm: [ảnh verify đúng run cho thấy hành vi đã kiểm]
```

PASS khi mọi assertion thuộc ticket trên các TC/model đã chọn đều đủ evidence và đạt. Không thêm `Reason` khi PASS, kể cả TC FAILED vì lỗi ngoài ticket. Thời gian lấy từ run; nhiều run thì ghi thời gian từng TC hoặc khoảng bắt đầu–kết thúc có căn cứ. Liệt kê đủ link prompt đã verify, không dùng link chat cũ.

## FAIL

```text
- Status: FAIL
- Thời gian kiểm tra: [dd/MM/yyyy HH:mm:ss (GMT+7)]
- conversion id: [TC ID / model: link conversation của prompt verify]
- Hình ảnh đính kèm: [ảnh verify đúng run thể hiện lỗi ticket]
- Reason:
  - Actual result:
    + UI: [TC/model, thao tác và lỗi thực tế; ID/field/giá trị nếu là lỗi số liệu]
    + Log response: [giá trị cùng ID/field và observation URL khi có đối chiếu dữ liệu]
    + Difference: [khác biệt thuộc ticket, viết ngắn và đơn giản]
  - Expected result:
    + UI: [hành vi/giá trị đúng theo ticket và TC snapshot]
```

FAIL khi ít nhất một lỗi thuộc ticket đã được chứng minh. Reason chỉ chứa lỗi ticket; không copy Note tổng hợp có lỗi khác từ Sheet. Với lỗi UI không cần log, bỏ dòng `Log response`. Ví dụ đơn giản: `UI: Chọn Stock desc nhưng 5 đứng trước 10.`; `Difference: Stock chưa giảm dần.`; `Expected result / UI: 10 đứng trước 5.` Nêu TC thuộc ticket chưa kiểm được nếu ảnh hưởng phạm vi kết luận; không đưa thành kết quả đạt.

## Evidence và trường hợp chưa kết luận

- Chụp và đính kèm ảnh liên quan cho cả PASS/FAIL, theo evidence/security contract của project; không lấy ảnh ticket cũ làm ảnh verify mới. Đặt ảnh thực dưới nhãn hoặc ghi tên attachment đã lưu, không chỉ nhập tên file chưa upload. Sau gửi, đọc lại nội dung và mở/kiểm ảnh thực tế.
- Không lấy giờ soạn comment làm giờ kiểm tra. Không bịa URL hoặc ảnh. Nếu không thể đính kèm ảnh, ghi `Chưa đính kèm — [lý do]`, báo phần thiếu; không tuyên bố đủ evidence.
- Không có failure đã chứng minh nhưng còn thiếu evidence bắt buộc: chưa có kết quả PASS/FAIL. Giữ comment kết quả ở draft, báo điều kiện thiếu; không ghi BLOCK vào trường Status của mẫu và không gán FAIL vì không chạy được. Ticket đã bắt đầu verify giữ `In testing` nếu chuyển thành công; Sheet theo contract BLOCK khi phù hợp.
- Không có TC liên quan hoặc chưa bắt đầu verify: báo kết quả tìm kiếm, không tự chuyển status ticket hay comment kết luận.
- Trước gửi, kiểm Activity để tránh lặp comment batch/run; timeout thì đọc lại trước retry. Kiểm status live và transition `In testing`; thiếu quyền/transition thì báo blocker, không thay bằng status gần giống. Sau gửi, xác minh ticket vẫn `In testing`.
