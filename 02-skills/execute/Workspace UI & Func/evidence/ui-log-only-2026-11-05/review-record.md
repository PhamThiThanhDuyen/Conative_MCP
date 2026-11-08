# Compare UI ↔ Input/Output only — draft update, 05/11/2026

User yêu cầu: “không cần kiểm tra input có giống prompt hay không, chỉ cần kiểm tra data trên UI trả về giống với input/output”. Nguồn đăng ký local: SRC-WORKSPACE-COMPARE-UI-LOG-20261105. Chỉ dẫn này thay thế phần kiểm Input ↔ prompt/Expected trong bản Langfuse trước.

## Thay đổi

- Compare skill, orchestrator, flow, runtime, contract, mẫu kết quả và hướng dẫn viết case thống nhất chỉ so UI trả về với Input/Output đúng response.
- Prompt vẫn dùng nhận diện session/turn và thực thi nguyên văn. Input khác prompt không tạo FAILED/BLOCK. UI công bố phạm vi trái Input/Output hoặc values khác Output vẫn được ghi sai lệch theo evidence; thiếu log đúng lượt vẫn BLOCK.
- Metric trực tiếp khớp Output không cần tính lại công thức backend. Phép tính do UI thực hiện vẫn cần đối chiếu từ input/output có căn cứ; không dùng thiếu daily forecast curve để block một field trực tiếp đã khớp log.
- Helper không đổi code/schema vì đã chỉ so actual UI/log provenance/scope/values. Snapshot helper có yêu cầu scope chặt; không biến thiếu nhãn UI không liên quan thành blocker toàn TC.
- Không rerun UI/API, thay báo cáo TC-001 lịch sử, ghi Sheet, tạo Bug, sửa sibling hoặc installed skills trong lượt cập nhật này.

## Validation và self-evaluation

- Baseline trước sửa: 9 skills PASS. Sau sửa: repo size validator và OpenAI quick_validate 9/9 PASS, không warning/failure mới. 13 synthetic tests hiện có PASS.
- Normal: prompt nói all statuses, Input active; scope UI công bố active khớp log, 6 values match → PASSED cho snapshot compare. Không có failure về prompt.
- Failure: cùng actual scope, UI gross_sales=999 còn log=1000.25 → FAILED.
- Missing-input: thiếu observation ID → BLOCK trước value compare. Không dựng ID hoặc bỏ provenance để pass.
- Walkthrough UI công bố kỳ/source khác log: ghi mismatch UI ↔ log; đây khác việc query khác prompt. Các case synthetic không phải live TC execution hoặc independent human review.
- Markdown links, reference metadata/source IDs và credential scan được kiểm trên thay đổi local; không thêm secrets hoặc raw customer payload.

## Trạng thái

Behavioral update; author/self-evaluation hoàn tất, qualified reviewer và owner review còn pending. Gói giữ draft/needs-review/source-derived; chưa cài/publish/promote hoặc mô tả approved. Evidence và kết quả cũ giữ nguyên lịch sử; yêu cầu cập nhật skill không tự cấp quyền regrade/writeback TC cũ.
