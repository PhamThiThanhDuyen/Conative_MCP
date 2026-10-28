---
knowledge_id: QA-CONATIVE-ORG-TIMEZONES-001
knowledge_type: qa-intelligence
source: SRC-CONATIVE-ROUND2-TIMEZONE-SHEET
owner: Conative QA owner (review pending)
authority: source-derived
scope: Conative Round 2 QE API execution by organization
target_release: current
status: needs-review
last_verified: 2026-10-28
supersedes: []
---

# Organization timezones for QE runs

Source: [native Round 2 workbook, tab ` Timezone` (leading space), columns A:B, rows 1:26](https://docs.google.com/spreadsheets/d/1-z8rvDg6C6v9irJjH7njGoudkJu57pEnzRkNX5gv3xQ/edit?gid=1549254386#gid=1549254386). This is a source-derived snapshot, not proof of the live organization's current setting. Re-read the exact tab and row before every QE run; never substitute the spreadsheet-level timezone (`America/Los_Angeles`) for an organization timezone.

| Row | Organization as written | Timezone cell as written |
|---:|---|---|
| 2 | Melinda Maria | `America/Los_Angeles` |
| 3 | Hammitt | `America/Los_Angeles` |
| 4 | ChanLuu | `America/Los_Angeles` |
| 5 | Raquel Allegra | `America/Los_Angeles` |
| 6 | Annmarie Skin Care | `America/Los_Angeles` |
| 7 | Miz Mooz | `America/New_York` |
| 8 | A.S.98 | `America/New_York` |
| 9 | NakedCashmere | `America/Los_Angeles` |
| 10 | Bando | `America/Los_Angeles` |
| 11 | Ipolita | *(blank)* |
| 12 | Qalo | `America/Los_Angeles` |
| 13 | Homesick | `America/New_York` |
| 14 | Pacific Cycle | `--- chắc là mặc định LA ^^` |
| 15 | Annmarie CBD | `America/Los_Angeles` |
| 16 | Honest Paws | `America/New_York` |
| 17 | Magnolia Coffee | `(GMT-05:00) Eastern Time (US & Canada)` |
| 18 | Millanova | `Europe/Warsaw` |
| 19 | Ippolitajewelry | `(GMT-05:00) Eastern Time (US & Canada)` |
| 20 | Purely Optimal | `America/Los_Angeles` |
| 21 | Noonday | `America/Chicago` |
| 22 | DARLAC FARMS FRUIT | `America/New_York` |
| 23 | Bearchop | `America/New_York` |
| 24 | Jungmaven | `America/Los_Angeles` |
| 25 | Noli Shop | `America/New_York` |
| 26 | Uncle Todd | `America/Los_Angeles` |

## QE lookup gate

1. Confirm the selected organization from the user/testcase, Claude connection, and Postman `signIn`/`chooseOrg`. Match it to one unique organization in the live ` Timezone` tab. Spelling differs between workbook areas (for example, `Mizmooz` vs `Miz Mooz`); treat a likely alias as a candidate and confirm it against the selected live organization. Do not merge similarly named rows such as `Annmarie Skin Care` and `Annmarie CBD`, or `Ipolita` and `Ippolitajewelry`.
2. Accept the live B-cell value as `<timezone>` only when it is a single unambiguous IANA zone identifier (for example, `America/New_York`). Inspect the selected QE request and set its `timezone` parameter to this exact value in the unsaved request-local overlay. Verify the resolved outgoing value before sending. Use the same zone to resolve relative date periods and forecast “today”; record it with the QE evidence.
3. Blank, speculative, display-label, duplicate, missing, or conflicting values require confirmation from the current organization setting or accountable owner. The two Eastern Time labels are not literal QE timezone parameter values and must not be silently converted to `America/New_York`; a fixed GMT offset may not encode daylight-saving behavior. If the exact timezone remains unresolved, stop before the QE request and report BLOCKED. Do not fall back to the saved Postman value, the workbook timezone, browser timezone, or the operator's timezone.

Local snapshot last read on 2026-10-28. Review owner and freshness before team-wide approval; any later live sheet change takes precedence over this snapshot.
