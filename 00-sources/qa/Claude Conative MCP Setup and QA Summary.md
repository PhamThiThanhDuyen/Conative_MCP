# Conative MCP with Claude: Setup and QA Summary

## Purpose

Enable Claude to connect to Conative MCP, access organization analytics in read-only mode, and run a basic query. The setup guide describes the Claude app connector and an optional Conative plugin. The referenced QA ticket tracks connection and basic query validation.

## Source documents

- [DevTak QA ticket #86341](https://devtak.cbidigital.com/projects/conative-paas/work_packages/86341/activity) — `[QA]_Ensure that Conative MCP Connection with Claude`
- [Conative to Claude setup guide](https://docs.google.com/document/d/1Wm3HECpg8fxC_212bl0wSp7ZojRf7Rlq2Y0Vo6g43Vk/edit?tab=t.0)

## Connection details

| Setting | Value |
|---|---|
| Connector name | `conative-claude` |
| MCP server URL | `https://api.conative.ai/stg-mcp-svc/mcp` |
| QA organization | `CBI_Demo1` |
| Permission scope | Read datasets, fields, and metrics; query analytics data |

The guide describes access as read-only. It says authorization is valid for up to 30 days and can be revoked under **Connected apps** in Conative. The organization and consent pages are time-limited (about 10 minutes); restart the connection flow in Claude if they expire.

## Claude app setup

### Connect the MCP connector

1. In Claude, open **Settings → Connectors → Add → Add custom connector**.
2. Enter the connector name and MCP URL from the table above.
3. Keep **Sign in now** selected and use the default **Use Claude’s published identity** OAuth client.
4. Add the connector, then click **Connect**.
5. Sign in with a Conative account, select the organization, review the read-only permissions, and click **Allow access**.
6. Return to Claude after the access approval page.

After connection, the guide expects two read-only tools: **Query Conative analytics** and **Discover Conative CQL schema**. Tool use defaults to **Needs approval**. Users can set tools to **Always allow** if they want to omit per-use approval.

### Optional Conative plugin

1. In **Settings → Plugins → Add → Upload plugin**, upload the provided `conative-claude-0.1.0.zip` (or the current version) without unzipping it.
2. Confirm the preview identifies the `conative` plugin, then upload it.
3. In the plugin’s **Connectors** tab, connect `conative-claude`.
4. Complete Conative sign-in, organization selection, and access approval if the connector is not already connected.

The guide says the plugin includes **7 skills and 3 agents** for inventory workflows. Once enabled, use **Try in chat** to start a conversation.

## QA ticket checklist

Ticket #86341’s stated goal is to confirm Claude can connect to Conative MCP and execute a basic query. Validate:

- [ ] Connect Claude to the MCP endpoint.
- [ ] Approve OAuth access.
- [ ] Deny OAuth access and confirm access is not granted.
- [ ] Disconnect and reconnect.
- [ ] Verify the MCP endpoint is available.
- [ ] Verify a query reaches the Query Engine.
- [ ] Execute a simple query successfully.

Ticket inputs include the staging MCP URL, OAuth account, organization `CBI_Demo1`, and client. Its output field names the MCP connection as Claude.

## Scope and open gap

The setup guide documents the **Claude app** workflow. It does not provide a separate configuration procedure for **Claude Code**. A Claude Code connection should therefore be treated as out of scope for this guide until its client-specific setup and verification steps are documented.

## Requirement analysis (Vietnamese)

> Nguồn: Tài liệu QA này và các câu trả lời làm rõ của người phụ trách | Độ tin cậy: Trung bình (đã làm rõ phạm vi và quy tắc chính; chưa xác định được nội dung ô prompt/kết quả mong đợi trong sheet tham chiếu)

### 1. Tóm tắt yêu cầu

- **Mục tiêu:** `[Source]` Kết nối Claude với Conative MCP ở chế độ chỉ đọc và chạy truy vấn analytics cơ bản.
- **Các bên tham gia:** `[Source]` Người dùng Claude, tài khoản Conative, Conative MCP, OAuth và Query Engine.
- **Điều kiện trước:** `[Source]` Dùng endpoint staging, tổ chức `CBI_Demo1` và tài khoản Conative phù hợp.
- **Luồng chính:** Thêm connector `conative-claude` trong Claude; kết nối OAuth; chọn tổ chức và cho phép quyền đọc; chạy truy vấn dùng prompt từ metric `Gross quantity` trong cột `Group` của [sheet tham chiếu](https://docs.google.com/spreadsheets/d/1fNGCNLP8LXFuNxhuzPbXGQEu1uanFLeO/edit?gid=460147179#gid=460147179).
- **Luồng thay thế / lỗi:** `[Source]` Từ chối OAuth, ngắt kết nối, hết hạn hoặc thu hồi quyền thì người dùng không thể truy cập hay truy vấn dữ liệu Conative. Có thể kết nối lại. Trang chọn tổ chức/cấp quyền hết hạn sau khoảng 10 phút thì bắt đầu lại luồng kết nối.
- **Dữ liệu và tích hợp:** `[Source]` MCP URL `https://api.conative.ai/stg-mcp-svc/mcp`; chỉ được đọc, không được thay đổi hoặc chỉnh sửa thông tin. Connector cung cấp **Query Conative analytics** và **Discover Conative CQL schema**.

### 2. Trong phạm vi / ngoài phạm vi

| Trong phạm vi | Ngoài phạm vi | Chưa rõ `[Out of scope?]` |
|---|---|---|
| Kết nối Claude app; OAuth cho phép/từ chối; ngắt kết nối/kết nối lại; truy cập chỉ đọc; endpoint và truy vấn tới Query Engine; chạy prompt theo metric `Gross quantity` tại cột `Group` | `[Source]` Không kiểm tra skills và agents của plugin Conative. Claude Code không thuộc hướng dẫn hiện tại. | Không còn điểm chưa rõ về việc kiểm tra plugin. Kết quả cụ thể mong đợi của prompt cần được đọc từ sheet. |

### 3. Quy tắc nghiệp vụ

| # | Quy tắc | Nhãn | Nguồn / vị trí |
|---|---|---|---|
| 1 | Connector là `conative-claude`, dùng MCP staging URL đã nêu. | `[Source]` | Bảng Connection details |
| 2 | Người dùng chỉ có quyền đọc; không có quyền thay đổi hoặc chỉnh sửa thông tin. | `[Source]` | Câu trả lời làm rõ của người phụ trách; mô tả quyền trong tài liệu |
| 3 | Nếu OAuth bị từ chối, kết nối bị ngắt, quyền hết hạn hoặc bị thu hồi, người dùng không thể truy cập hoặc truy vấn dữ liệu Conative. | `[Source]` | Câu trả lời làm rõ về trạng thái truy cập |
| 4 | Truy vấn QA dùng prompt cho metric `Gross quantity` tại cột `Group` trong sheet tham chiếu. | `[Source]` | Câu trả lời làm rõ về truy vấn |
| 5 | Không cần kiểm tra skills/agents có trong plugin Conative. | `[Source]` | Câu trả lời làm rõ về phạm vi plugin |
| 6 | Không cần kiểm tra thời gian phản hồi hoặc tốc độ response. | `[Source]` | Câu trả lời làm rõ về hiệu năng |
| 7 | Quyền OAuth có hiệu lực tối đa 30 ngày; trang chọn tổ chức và cấp quyền tồn tại khoảng 10 phút. | `[Source]` | Connection details trong tài liệu QA |

### 4. Rủi ro

| # | Rủi ro | Ảnh hưởng | Khả năng xảy ra | Mức độ | Lý do |
|---|---|---|---|---|---|
| 1 | Quyền chỉ đọc bị cấu hình sai và cho phép chỉnh sửa dữ liệu. | Có thể làm thay đổi dữ liệu trong tổ chức QA. | Trung bình | **Cao** | Quy tắc chỉ đọc là yêu cầu bảo mật chính; cần xác nhận các thao tác ghi đều bị từ chối. |
| 2 | Sau khi từ chối, ngắt kết nối, hết hạn hoặc thu hồi OAuth, người dùng vẫn truy cập được dữ liệu. | Truy cập dữ liệu ngoài quyền được cấp. | Trung bình | **Cao** | Quy tắc truy cập sau các trạng thái này đã được nêu rõ và cần được kiểm tra trực tiếp. |
| 3 | Prompt hoặc kết quả mong đợi của truy vấn `Gross quantity` không được xác định chính xác từ sheet. | QA không thể so sánh kết quả và có thể bỏ sót lỗi dữ liệu. | Trung bình | **Trung bình** | Người phụ trách đã chỉ rõ sheet, metric và cột; nội dung prompt/kết quả cụ thể chưa được trích xuất. |
| 4 | Lỗi MCP hoặc Query Engine không có đủ bằng chứng để phân biệt nguyên nhân. | Khó xác định điểm lỗi khi truy vấn thất bại. | Trung bình | **Thấp** | Cần kiểm tra endpoint và truy vấn tới Query Engine; không yêu cầu đo thời gian phản hồi. |

### 5. Câu hỏi cần làm rõ

| # | Câu hỏi | Hỏi ai | Vì sao cần hỏi | Ưu tiên |
|---|---|---|---|---|
| 1 | Trong sheet, ô hoặc hàng nào chứa prompt `Gross quantity` cần chạy, và kết quả dữ liệu nào được xem là đúng? | PO / BA | Cần tiêu chí so sánh để xác nhận truy vấn thành công và xử lý rủi ro 3. | Blocker |
| 2 | Có thể cung cấp log hoặc dấu hiệu nào để xác nhận request đã đến MCP endpoint và Query Engine? | Dev | Giúp xác định điểm lỗi khi tích hợp thất bại; không nhằm đo tốc độ response. | Nên có |

### 6. Phạm vi kiểm thử đề xuất

- **Loại kiểm thử đề xuất**
  - **P1 — Bảo mật / phân quyền:** Kiểm tra connector chỉ có quyền đọc; thử các thao tác thay đổi/chỉnh sửa và xác nhận bị từ chối, không làm đổi dữ liệu. Xử lý rủi ro 1.
  - **P1 — Vòng đời OAuth và trạng thái truy cập:** Kiểm tra từ chối, ngắt kết nối, hết hạn và thu hồi quyền; trong mỗi trạng thái, xác nhận người dùng không truy cập hoặc truy vấn được dữ liệu. Kết nối lại rồi xác nhận có thể tiếp tục theo luồng được cấp quyền. Xử lý rủi ro 2.
  - **P1 — Chức năng / tích hợp:** Kết nối Claude, kiểm tra MCP endpoint và chạy truy vấn prompt `Gross quantity` từ cột `Group` đến Query Engine. Cần nội dung prompt và kết quả chuẩn từ Q1.
  - **P2 — Luồng hết hạn trang:** Để trang chọn tổ chức/cấp quyền hết hạn khoảng 10 phút rồi kiểm tra có thể bắt đầu lại như tài liệu mô tả.
  - **Plugin:** Không kiểm tra skills và agents theo quyết định đã chốt. Có thể bỏ qua kiểm thử workflow inventory của plugin nếu không có yêu cầu riêng.
  - **Hiệu năng:** Bỏ kiểm tra thời gian phản hồi/tốc độ response theo quyết định đã chốt.
  - **Dữ liệu chuyển đổi, concurrency, tương thích, accessibility/localization, thông báo/audit:** Không có yêu cầu trong tài liệu hiện tại; chưa đưa vào phạm vi này.

- **Nhóm tình huống chính**
  - Kết nối OAuth thành công với `CBI_Demo1`; xác nhận các công cụ đọc dữ liệu xuất hiện.
  - Từ chối OAuth, ngắt kết nối, hết hạn và thu hồi quyền; mỗi lần xác nhận không thể truy cập hoặc truy vấn dữ liệu Conative.
  - Kiểm tra các thao tác chỉnh sửa/thay đổi bị từ chối và dữ liệu không bị thay đổi.
  - Chạy prompt cho metric `Gross quantity` tại cột `Group`; so sánh kết quả với giá trị chuẩn trong sheet.
  - Kiểm tra endpoint và xác nhận truy vấn tới Query Engine bằng log hoặc dấu hiệu đã thống nhất; không đo tốc độ phản hồi.

- **Dữ liệu / môi trường cần chuẩn bị**
  - Claude app, MCP staging endpoint, tổ chức `CBI_Demo1` và tài khoản Conative QA.
  - Truy cập sheet tham chiếu để lấy đúng prompt trong cột `Group` và kết quả chuẩn cho `Gross quantity`.
  - Dữ liệu QA an toàn để kiểm tra thao tác chỉnh sửa bị từ chối; phương thức xem log/dấu hiệu request tới MCP và Query Engine.

- **Ý tưởng tự động hóa**
  - Tự động hóa kiểm tra endpoint và prompt truy vấn ở mức API/tích hợp khi đã có prompt và kết quả chuẩn.
  - Có thể tự động đối chiếu trạng thái truy cập sau các thao tác OAuth nếu môi trường có giao diện hoặc API kiểm thử ổn định.

- **Phần chưa thể chốt do câu hỏi mở**
  - Cần trả lời Q1 để chốt prompt và kết quả mong đợi cho kiểm thử truy vấn.
  - Q2 giúp xác định bằng chứng/log cần thu thập khi kiểm tra endpoint và Query Engine.

## References

- [DevTak ticket #86341](https://devtak.cbidigital.com/projects/conative-paas/work_packages/86341/activity)
- [Google Doc: Conative_Claude_Setup_Guide](https://docs.google.com/document/d/1Wm3HECpg8fxC_212bl0wSp7ZojRf7Rlq2Y0Vo6g43Vk/edit?tab=t.0)
