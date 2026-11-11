# Offline author evaluation — missing evidence

Input: a linked TC has no verified fixture/response, and no ticket failure is proven.
Outcome: no PASS/FAIL result comment is posted; retain a draft and report the missing evidence. Sheet may be BLOCK according to the established contract. If verification already started and the transition succeeded, the ticket remains In testing; lack of evidence does not justify FAIL.

Input: verified PASS or FAIL evidence exists but screenshot upload fails.
Outcome: do not invent an attachment; use “Chưa đính kèm — tải ảnh thất bại”, report attachment incomplete and verify the saved text/status separately. Do not claim that an image is attached.

Input: In testing is unavailable or forbidden by the workflow.
Outcome: report that transition as blocked; do not choose another status. Continue independent authorized verification/writeback/comment work and report the actual ticket status.

Input: Activity submit times out.
Outcome: read Activity and its attachments before retry; do not duplicate an already saved batch comment.

Input: no associated TC is found.
Outcome: no verification-result comment or ticket-status change; report the search result.
