---
knowledge_id: BC-CONATIVE-METRICS-SOURCE-INDEX
knowledge_type: business-contract
source: SRC-CONATIVE-DATA-DICTIONARY
owner: BA/Data owner TBD
authority: source-derived
scope: Data Dictionary source provenance
target_release: current-unspecified
status: needs-review
last_verified: 2026-07-30
supersedes: []
---

# Data Dictionary Source Index

| Attribute | Value |
|---|---|
| Title | Data Dictionary |
| Source type | Google Sheet |
| Spreadsheet ID | `1-rpKEDAqHpGWyVlFEfoscgjfSXsvEAH10fE48YWv7DY` |
| Source link | [Open Google Sheet](https://docs.google.com/spreadsheets/d/1-rpKEDAqHpGWyVlFEfoscgjfSXsvEAH10fE48YWv7DY/edit?gid=0#gid=0) |
| Tab | `Sheet1`, sheet ID `0` |
| Locale / timezone | `en_US` / `Asia/Saigon` |
| Retrieved | 2026-07-30 |
| Physical grid | 1,014 rows x 27 columns |
| Populated source range observed | `A1:E54` |
| Source columns | Category, Field/Metric, Explain, Formula, Formula Input |
| Owner / approver | TBD |
| Release / effective date | Not stated |

## Extraction Notes

- Rows after row 54 were empty when read on 2026-07-30.
- Rows 3 and 4 contained only `Product Information` and no metric name.
- The `Formula Input` column was empty for every populated metric row.
- `XX-Day Sales (Rule-based)` had no category value; it is grouped under
  Inventory here based on its neighboring rows and usage context. This is an
  explicit normalization inference, not a source fact.
- Wording and formulas are normalized only for whitespace and catalog layout.
  Material ambiguities remain listed in `metric-quality-gaps.md`.
