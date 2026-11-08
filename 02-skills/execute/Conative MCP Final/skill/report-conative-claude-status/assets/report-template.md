- TỔNG QUAN
  - ORG: <org> - <PASS | FAIL | NOT RUN>
    - Source: <source> - <🟢 PASS | 🔴 FAIL | NOT RUN>
- CHI TIẾT:
  - ORG: <org> - <PASS | FAIL | NOT RUN>
    - Source: <source> - <🟢 PASS | 🔴 FAIL | NOT RUN>
      - Product: TOTAL: <PASS + FAIL> fields
        - PASS: <positive pass count> fields
        - FAIL: <positive fail count> fields
        - CHƯA CÓ STATUS: <positive blank count> fields
      - Variant: TOTAL: <PASS + FAIL> fields
        - PASS: <positive pass count> fields
        - FAIL: <positive fail count> fields
        - CHƯA CÓ STATUS: <positive blank count> fields
- BUGS:
  - <ticket ID> - <verified ticket title, or Chưa xác minh title>
    - ORG: <affected org 1> / <affected org 2>

Repeat ORG and Source items for every selected live group. Omit zero-count PASS,
FAIL, and blank lines. Show `NOT RUN` under a grain whose TOTAL is zero. Show
`STATUS CHƯA NHẬN DIỆN: <count> fields (<tokens>)` for unexpected tokens.
Add `Giới hạn: <precise issue>` beneath the affected scope when necessary.
Keep the three top-level sections and their order; do not substitute summary
tables or omit organizations with no recorded results.

Use the colored source status in both sections: `🟢 PASS` for PASS and `🔴 FAIL`
for FAIL. Keep NOT RUN neutral; colors never change the recorded status.

Build each bug ORG line from current failing testcases across all selected
organizations/sources, including verified same-defect matches without a ticket
reference. Do not copy the affected-org list from the ticket title or description.
