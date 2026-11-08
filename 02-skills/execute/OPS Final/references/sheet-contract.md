# Quy tắc đọc và ghi Google Sheet

## Đọc đúng dữ liệu

1. Dùng đúng workbook ID trong [run-settings.md](run-settings.md), đọc metadata
   trước. Dùng Google Drive/Sheets connector khi đáp ứng đủ thao tác; dùng browser
   in-app để xử lý UI hoặc để người dùng hỗ trợ khi bị kẹt.
2. Đọc ba tab đúng tên. Đọc vùng nhỏ, có giới hạn theo grid metadata: hàng header,
   các cột mapping/metric và vùng lịch sử kiểm tra cần dùng. Mở rộng khi còn dữ liệu;
   không coi số dòng hiện có trong ví dụ là giới hạn vĩnh viễn.
3. Tab `Danh sách org`: resolve header `ORG`, `from_source`, `Channel`.
   Một org có nhiều source; chọn đúng một dòng theo cặp org/source. Channel
   trống thì dùng source người dùng đã xác nhận để hiển thị; không tự tạo alias.
4. Hai tab kết quả: resolve `Name`, `Key` và row thực tế. Không dùng ID làm khóa
   duy nhất vì có dòng ID trống/trùng. Dòng có Name là dòng cần đánh kết quả,
   kể cả các dòng con như `> Category name`; bỏ hàng tiêu đề và dòng trống.
5. Đọc ô đích, note, formula, validation, merge và quyền/protection trước khi ghi.
   Nếu không ghi được đúng `Passed`, `Failed`, `N/A`, hỏi người dùng; không sửa
   validation để ép ghi.

## Chèn cột mới

- Xác định cột lần kiểm tra nằm ngoài cùng bên phải trong từng tab, dựa trên
  header và nội dung lịch sử; không chọn theo ngày lớn nhất trong chuỗi text.
- Chèn đúng một cột ngay sau cột đó. Nếu bên phải là cột chức năng như `AI Chat`,
  đẩy cột này sang phải. Chỉ dùng cột trống có sẵn khi đã xác minh cột thật sự trống,
  không có nội dung/note/formula cần giữ và nằm đúng vị trí.
- Nếu không xác định được ranh giới lịch sử với cột khác, hỏi trước khi chèn.
- Copy riêng định dạng cần thiết từ cột kiểm tra trước: độ rộng, wrap, header,
  border hoặc alignment. Sao chép dropdown theo phần dưới; không lấy status,
  note hoặc formula của lần kiểm tra cũ.
- Header theo phần II trong [FLOW.md](../FLOW.md). Kết quả chưa chạy để trống.
- Đọc lại header và vị trí sau khi chèn. Lưu địa chỉ cột riêng cho từng tab để
  tiếp tục khi bị gián đoạn. Chèn cột có thể đổi địa chỉ nên đọc lại trước mỗi ghi.
- Lần chạy mới tạo cột mới, kể cả header trùng cùng ngày. Khi đang resume, chỉ
  dùng lại cột đã xác minh thuộc đúng lần đang dở; header giống nhau chưa đủ.

## Dropdown status

- Mỗi ô status cần có dropdown giống cột kiểm tra trước trong cùng tab.
  Giữ các lựa chọn, màu và cách hiển thị của cột mẫu. Dropdown phải có
  `Passed`, `Failed`, `N/A`.
- Chọn một ô mẫu có đủ dropdown. Chỉ sao chép dropdown vào các dòng metric;
  bỏ qua header và dòng trống. Ô mẫu thiếu dropdown thì chọn ô đầy đủ khác.
- Với connector, dùng `copyPaste` và `PASTE_DATA_VALIDATION`. Không xóa
  dropdown sau khi sao chép. Không tạo lại danh sách bằng chữ thuần.
- Đọc lại từng ô để kiểm tra dropdown. Mở Sheet để kiểm tra màu và mũi tên
  thả xuống; chọn thử mở danh sách nhưng không đổi kết quả.
- Nếu chỉ sửa định dạng cho run đã có, dùng lại cột của run đó. Giữ nguyên
  header, status và note; không chạy lại API hoặc tạo cột mới.

## Ghi kết quả và note

Chỉ ghi dòng metric trong cột mới của tab tương ứng. Không thay các cột Name,
Key, ID, kết quả cũ, cột Note chung hoặc tab `Danh sách org`.

Nếu dùng Sheets batch update, ghi `userEnteredValue.stringValue` cho status
và `note` cho cell note; field mask chỉ gồm giá trị và note cần sửa. Đây là
cell note tương đương “Chèn → Ghi chú”, không phải Drive comment.
Đọc lại từng ô/note đã ghi. Không coi tool trả về thành công là đủ.

Một lần request lỗi/chưa hoàn tất: không ghi cả cột N/A. Giữ các ô chưa xác minh
trống, báo tiến độ thật. Nếu chỉ ghi một phần vì lỗi mạng, đọc lại và tiếp tục
cùng cột, không chạy API hoặc chèn cột mới chỉ để sửa lỗi lưu.

## Ví dụ vị trí đã đọc, không dùng làm cấu hình cố định

Ngày 2026-11-08: Variant có cột kiểm tra cuối ở GP, ngay sau đó GQ là `AI Chat`.
Product có cột kiểm tra cuối ở CK, ngay sau đó CL là `AI Chat `.
Vì vậy phải xác định vị trí từng tab độc lập. Mỗi lần chạy sau phải đọc lại
header; không hard-code GP/GQ/CK/CL.
