# Conative QE Codex Kit - Hướng dẫn sử dụng

> Mỗi mục `##` là một khối độc lập, có thể chuyển trực tiếp thành một slide.
> Thời lượng trình bày đề xuất: 7-10 phút, sau đó demo một flow thật.

## 1. Concept - Từ yêu cầu đến quyết định có bằng chứng

**Thông điệp chính**

Conative QE Codex Kit biến tri thức QA thành năng lực AI có thể tái sử dụng,
nhưng quyền quyết định nghiệp vụ và release vẫn thuộc về con người.

```text
Business outcome
      ↓
Goal → Skill → Knowledge → Script / Template → Artifact → Human gate
```

- Không xây một agent khổng lồ biết mọi thứ.
- Chia Quality Engineering thành capability ổn định và skill nhỏ.
- Skill thực hiện quy trình; Knowledge cung cấp sự thật có nguồn và authority.
- Mỗi lần chạy phải tạo artifact có thể review, truy vết và đánh giá.

**Câu nói khi trình bày**

> Bộ kit không thay QA ra quyết định. Nó giúp QA tạo quyết định nhanh hơn, nhất
> quán hơn và luôn chỉ ra quyết định đó dựa trên nguồn nào.

## 2. Concept - 8 capability của Quality Engineering

| Capability | Outcome |
|---|---|
| Requirement Engineering | Tìm gap, assumption và business risk |
| Test Design | Tạo testcase có traceability và test data |
| API Verification | Xác minh API, schema, rule và error handling |
| Data Readiness Assessment | Quyết định dữ liệu đã đủ điều kiện test chưa |
| Data Verification | Đối soát chất lượng và metric giữa các nguồn |
| UI Verification | Đối chiếu UI với API, data và requirement |
| Evidence & Diagnosis | Đóng gói evidence và hỗ trợ tìm nguyên nhân |
| Release Intelligence | Đánh giá residual risk và đề xuất Go/No-Go |

Capability trả lời câu hỏi **QA cần đạt outcome gì**. Skill trả lời câu hỏi
**Codex thực hiện thao tác nào để tạo outcome đó**.

## 3. Terms - Ngôn ngữ chung của bộ kit

| Term | Nghĩa ngắn | Ví dụ |
|---|---|---|
| Source | Tài liệu gốc, giữ để đối chiếu | BA document, Product Docs, Google Sheet |
| Goal | Workflow điều phối nhiều skill để tạo outcome hoàn chỉnh | `qe-release-readiness` |
| Capability | Nhóm năng lực nghiệp vụ ổn định | Test Design, Data Verification |
| Skill | Một thao tác AI nhỏ, có một trách nhiệm | `testcase-matrix-design` |
| Knowledge | Tri thức đã chuẩn hóa, có nguồn, scope và authority | Metric catalog, business contract |
| Script | Logic lặp lại cần chạy xác định | Validator |
| Template | Khung đầu ra thống nhất | Test matrix, evidence report |
| Artifact | Kết quả cụ thể của một lần chạy | Testcase, gap register, report |
| Evaluation | Kiểm tra artifact hoặc skill có đạt chuẩn không | Structure/quality validator |
| Human gate | Điểm con người phải duyệt | Assumption, risk, evidence, Go/No-Go |

**Phân biệt quan trọng**

- Source chưa chắc là Knowledge đã được phê duyệt.
- Current Product mô tả sản phẩm đang làm gì, không tự chứng minh điều đó đúng.
- Skill không chứa business truth; skill phải tìm Knowledge phù hợp khi chạy.
- Thiếu expected behavior phải báo `Requirement Gap`, không được tự đoán.

## 4. Core Items - Những phần người dùng cần biết

| Vị trí | Dùng khi nào |
|---|---|
| `01-goals/` | Cần chạy một workflow đầu-cuối |
| `02-skills/` | Cần một tác vụ QA cụ thể |
| `03-knowledge/` | Cần requirement, metric, mapping, rule hoặc standard |
| `04-templates/` | Cần định dạng artifact thống nhất |
| `05-scripts/` | Cần validation hoặc xử lý xác định |
| `06-demo/` | Cần xem ví dụ hoặc lưu pilot artifact |
| `07-evaluation/` | Cần đánh giá chất lượng output/skill |
| `00-sources/` | Cần truy ngược tài liệu gốc |

`08-research/` là benchmark để phát triển bộ kit, không phải expected-result
authority khi thực hiện test Conative.

## 5. Core Items - Knowledge được đọc như thế nào

```text
Task scope
   ↓
Source Registry + Authority Matrix
   ↓
Business Contract ── expected behavior
Current Product ───── regression baseline
Industry Domain ───── risk context
QA Intelligence ───── execution method
   ↓
Conflict / freshness check
   ↓
Test oracle hoặc Requirement Gap
```

Thứ tự ưu tiên không dựa vào tên file mới hơn hay nội dung có vẻ hợp lý hơn.
Codex phải xét source, owner, authority, scope, release và ngày xác minh.

Ví dụ: BA document và Product Docs khác empty-state message thì không được chọn
ngầm một bên. Phải áp dụng conflict rule hoặc sử dụng decision record đã duyệt.

## 6. How To Use - Chọn Goal hay Skill

**Chọn Goal khi:**

- cần outcome đầu-cuối;
- chưa biết phải gọi những skill nào;
- cần nhiều artifact và human gate liên tiếp.

**Chọn Skill khi:**

- chỉ cần một kết quả cụ thể;
- đã có input và phạm vi rõ;
- muốn cập nhật hoặc kiểm tra lại một artifact có sẵn.

| Nhu cầu | Entry point |
|---|---|
| Đánh giá release | Goal `01-goals/qe-release-readiness.md` |
| Phân tích requirement | Skill `analyze-requirement-risk` |
| Viết/cập nhật testcase | Skill `testcase-matrix-design` |
| Check API | Skill `qa-api-verification` |
| Check data/metric | Skill `verify-data-quality` |
| Đối chiếu API-data-UI | Skill `api-data-ui-verification` |
| Đóng gói evidence | Skill `evidence-package` |
| Đề xuất release | Skill `go-no-go-report` |

## 7. How To Use - Input tối thiểu

Một yêu cầu tốt nên có:

```text
Outcome: Muốn Codex tạo hoặc kiểm tra điều gì?
Scope: Feature, API, metric, channel hoặc release nào?
Source: Requirement/testcase/tài liệu nào đã có?
Environment: Local, staging hay live?
Identity: Organization, role, tenant hoặc channel nào?
Data: Fixture, ID hoặc time range nào được phép dùng?
Constraints: Read-only, tolerance, format và nơi lưu artifact?
```

Không cần đủ mọi input ngay từ đầu. Khi thiếu dữ liệu, Codex phải:

1. Tìm trong source và knowledge nội bộ trước.
2. Khám phá read-only nếu được phép.
3. Hỏi đúng input còn thiếu có ảnh hưởng đến kết quả.
4. Đánh dấu `Blocked`, `Assumption` hoặc `Requirement Gap` nếu chưa thể xác nhận.
5. Không tự tạo business rule, credential hoặc customer fixture.

## 8. How To Use - Prompt mẫu

**Flow đầu-cuối**

```text
Dùng goal qe-release-readiness cho tính năng <feature>.
Requirement: <file/link>.
Environment: <environment>; organization: <organization>; role: <role>.
Chỉ thực hiện read-only. Lưu artifact tại <output-folder>.
Báo input còn thiếu trước khi execution.
```

**UI / Function**

```text
Dùng testcase-matrix-design để tạo hoặc cập nhật testcase cho Search của
Replenishment Flow. Đọc business contract và Product Docs liên quan, giữ nguyên
testcase ID đã có, đánh dấu requirement gap, chưa chạy thao tác ghi dữ liệu.
```

**Data reconciliation**

```text
Dùng verify-data-quality để đối soát Gross Sales giữa Conative và Shopify.
Grain: variant; time range: <from-to>; timezone: <timezone>;
join key: Shopify Variant ID; tolerance: <approved-rule>.
Kiểm tra duplicate và unmatched key trước khi so sánh metric.
```

**Cập nhật nhỏ testcase có sẵn**

```text
Cập nhật <testcase-file> theo requirement mới <source>.
Giữ testcase ID và traceability; chỉ sửa case bị ảnh hưởng.
Chạy validator trước và sau, rồi báo diff và requirement còn thiếu.
```

## 9. How To Use - Hai chế độ sử dụng

### Library Mode

Phù hợp khi vừa clone repo hoặc đang phát triển kit.

1. Mở Codex tại thư mục repo.
2. Yêu cầu Codex dùng Goal hoặc Skill và nêu đường dẫn nếu cần.
3. Codex đọc Knowledge theo scope rồi tạo artifact vào output folder đã chỉ định.

Ví dụ:

```text
Đọc 01-goals/qe-release-readiness.md và chạy goal cho scope này: ...
```

### Installed Mode

Phù hợp với người dùng thường xuyên và cú pháp `$skill-name`.

- Skill phải được cài vào thư mục skill mà Codex khám phá.
- Sau khi cài, gọi `$testcase-matrix-design`, `$verify-data-quality`, ...
- Goal orchestration một-chạm cần được đóng thành runner skill riêng; file Goal
  trong `01-goals/` không tự trở thành lệnh `$goal-name`.

Hiện repo hỗ trợ đầy đủ Library Mode. Cơ chế installer và runner một-chạm cần
được đóng gói trước khi công bố Installed Mode cho toàn team.

## 10. How To Use - Guardrails bắt buộc

- Không lưu password, token, cookie, OTP hoặc private key dạng plaintext.
- Không đưa thông tin dự án ra dịch vụ hoặc repository chưa được phê duyệt.
- Không thay đổi dữ liệu khách hàng.
- Test create/update/delete trên live chỉ được chạy sau khi Dev xác nhận backup
  mới và nhận trách nhiệm restore.
- Entity tồn tại trên live như report, PO hoặc view phải có tiền tố `CBI Test`.
- Sau test phải có xác nhận restore và evidence.
- AI đề xuất; QA duyệt assumption, priority, evidence và release recommendation.

## 11. Quick Start - 60 giây cho người mới

```powershell
git clone --recurse-submodules https://gitlab.cbidigital.dev/conative/knowledges/conative-tester-agent.git
cd conative-tester-agent
python 05-scripts/validate_skill_size.py
```

Sau đó mở Codex tại repo và gửi:

```text
Tôi muốn kiểm tra <feature>.
Hãy chọn Goal/Skill phù hợp, đọc Knowledge có authority cao nhất,
liệt kê input còn thiếu, chỉ chạy read-only và tạo artifact tại <output-folder>.
```

**Kết quả đúng không chỉ là câu trả lời trong chat.** Kết quả đúng là artifact
có source, scope, status, evidence, gap và human gate rõ ràng.

## 12. Demo Story - Cách trình bày bộ kit

1. Chọn một requirement thật nhưng phạm vi nhỏ.
2. Cho thấy Codex phát hiện một requirement gap.
3. Sinh testcase có traceability và test data.
4. Chạy một verification read-only hoặc dùng evidence đã được sanitize.
5. Cho thấy một Passed, một Failed, một Blocked và một residual risk.
6. Kết thúc bằng artifact và quyết định QA cần duyệt.

Demo hiện có tại `06-demo/search-ui-function/` minh họa phần Requirement Risk và
Test Design cho Search của Replenishment Flow. Đây là design demo; execution chỉ
được tiếp tục sau khi environment, signed-in session và fixture preflight đạt.

## 13. Worked Example - Đối soát Conative với Shopify

**Mục tiêu demo**

Chứng minh Skill có thể đọc Knowledge, thu thập dữ liệu read-only từ hai nguồn,
đối soát cùng scope và tạo artifact có evidence. Demo không nhằm chứng minh mọi
metric Shopify đã đúng hoặc thay thế phê duyệt của QA/Data owner.

### Phạm vi khuyến nghị

| Thuộc tính | Giá trị demo |
|---|---|
| Source | Conative Dashboard và Shopify `Sales by product` |
| Grain | Summary |
| Metrics | Gross Sales, Gross Quantity, Net Sales |
| Time range | Một khoảng ngày ngắn, cố định trên cả hai nguồn |
| Execution | Read-only |
| Skill | `verify-data-quality` |
| Knowledge | `qa-intelligence/heuristics/source-data-reconciliation.md` và `business-contracts/conative-metrics/` |

### Input bắt buộc

```text
Organization: <conative-organization>
Environment: <staging-or-live>
Shopify store: <store-name>
Time range: <YYYY-MM-DD> đến <YYYY-MM-DD>
Timezone: <timezone>
Currency: <currency>
Tolerance: <approved-rule-or-demo-heuristic>
```

Codex được phép tìm organization/store từ signed-in session để gợi ý, nhưng
không được tự chọn nếu có nhiều lựa chọn hoặc scope không rõ.

### Preflight

1. Xác nhận Conative và Shopify đã có signed-in session hợp lệ.
2. Không yêu cầu, hiển thị hoặc lưu credential plaintext.
3. Xác nhận cùng store, organization, channel, time range, timezone và currency.
4. Ghi nhận sync timestamp hoặc cảnh báo nếu không xác định được độ mới dữ liệu.
5. Dừng với `Blocked` nếu login hoặc scope bắt buộc chưa sẵn sàng.
6. Không tạo, sửa, xóa dữ liệu hay thay đổi integration setting.

### Luồng thực hiện

```text
Conative Dashboard Summary
          ┐
          ├─ Normalize scope and values
          ┘             ↓
Shopify Sales by product Summary
                        ↓
           Compare → Evidence → Gap/Result
```

| Conative | Shopify |
|---|---|
| `summary.gross_sales` | Gross sales |
| `summary.gross_quantity` | Ordered quantity |
| `summary.net_sales` | Net sales |

Với mỗi metric, ghi nhận giá trị hai bên, signed difference, absolute difference
và percentage difference:

```text
Signed difference = Conative - Shopify
Absolute difference = ABS(Conative - Shopify)
Difference % = Absolute difference / ABS(Shopify) * 100
```

Nếu Shopify bằng `0`, không tự chia; đánh dấu `Denominator Zero`. Nếu timezone,
currency, date boundary hoặc sync scope không khớp, dùng `Not Comparable`.

Tài liệu QA cũ có heuristic `<5%`, nhưng chưa có approval evidence. Có thể dùng
để minh họa và phải ghi rõ `Demo Heuristic`; không được kết luận QA Pass/Fail
chính thức từ ngưỡng này.

### Artifact đầu ra

```text
06-demo/shopify-data-reconciliation/runs/<run-id>/
├── 01-preflight.md
├── 02-reconciliation-scope.md
├── 03-reconciliation-result.md
├── 04-evidence-package.md
└── 05-gaps-and-recommendations.md
```

Result table tối thiểu:

| Metric | Conative | Shopify | Difference | Difference % | Status | Evidence |
|---|---:|---:|---:|---:|---|---|

Đối với từng testcase, evidence package nên có thêm:
- screenshot của bước thực thi và kết quả;
- video record ngắn (ví dụ 10–20 giây) để ghi lại hành vi thực tế;
- ghi chú expected vs actual và tình trạng pass/fail/block.

Trạng thái được phép: `Within Demo Heuristic`, `Outside Demo Heuristic`,
`Not Comparable`, `Blocked`, hoặc `Requirement Gap`.

### Prompt chạy demo

```text
Dùng Library Mode và skill verify-data-quality để chạy demo read-only đối soát
Conative với Shopify.

Organization: <organization>; environment: <environment>;
Shopify store: <store>; time range: <from-to>;
timezone: <timezone>; currency: <currency>; grain: Summary.
Metrics: Gross Sales, Gross Quantity, Net Sales.

Đọc source-data-reconciliation.md, metric-catalog.md, metric-quality-gaps.md,
data-quality-standard.md và các security/live-testing rules liên quan.

Chạy preflight trước. Dùng signed-in sessions, không yêu cầu credential plaintext,
không mutation. Xác nhận cùng scope và sync freshness rồi mới đối soát.
Tính signed, absolute và percentage difference; không chia khi source bằng 0.
Ngưỡng <5% chỉ là Demo Heuristic, không phải approved Pass/Fail rule.

Lưu preflight, scope, result, evidence và gap report tại:
06-demo/shopify-data-reconciliation/runs/<run-id>/

Nếu thiếu input bắt buộc, vẫn tạo preflight và gap report rồi đánh dấu Blocked;
không tự đoán organization, store, business rule hoặc customer fixture.
```

**Điểm cần trình bày:** cùng một run cho thấy input governance, source mapping,
deterministic calculation, evidence và requirement gap; không chỉ cho thấy hai
con số được đặt cạnh nhau.

## 14. Team Maintenance - Những nội dung team cần duy trì

Một team dùng Conative QE Codex Kit không chỉ cần chạy workflow, mà còn phải duy
trì các lớp nền tảng để process luôn ổn định, kết quả kiểm thử có thể tin cậy và
hiệu quả công việc được cải thiện theo thời gian:

- Knowledge & source authority: duy trì business contract, rule, metric và nguồn
  dữ liệu có thẩm quyền để đảm bảo quyết định QA luôn dựa trên truth source.
- Skill & prompt quality: version hóa prompt, kiểm tra regression và đánh giá chất
  lượng output để process không bị suy giảm khi team mở rộng.
- Evaluation & benchmark: duy trì gold set, failure cases và benchmark để đo lường
  hiệu quả thực tế và phát hiện drift trước khi ảnh hưởng release.
- Guardrails & safety: bảo vệ dữ liệu nhạy cảm, kiểm soát access và duy trì
  approval flow để giảm rủi ro trong vận hành.
- Governance & ownership: phân rõ owner, review cadence và human gate để đảm bảo
  quyết định Go/No-Go vẫn có trách nhiệm và có thể audit được.

## 15. Team Contribution - Tạo hoặc cập nhật Skill và Knowledge

Mọi thay đổi phải tuân theo
`03-knowledge/governance/change-approval-policy.md`. Tạo được file chưa có nghĩa
là nội dung đã được duyệt hoặc sẵn sàng cài cho toàn team.

### Chọn đúng loại thay đổi

| Nhu cầu | Tạo hoặc cập nhật |
|---|---|
| Outcome hoặc trigger mới, không skill hiện tại nào sở hữu hợp lý | Tạo Skill |
| Sửa bước, input, output hoặc failure behavior của workflow hiện có | Update Skill |
| Có source/rule/mapping/standard mới | Tạo Knowledge |
| Source đổi, rule được duyệt lại, conflict được giải quyết hoặc scope thay đổi | Update Knowledge |

Nếu một Skill hiện có có cùng trách nhiệm, ưu tiên cập nhật và khử trùng thay vì
tạo Skill gần giống. Business rule không được nhét vào `SKILL.md` để tiện dùng;
hãy chuẩn hóa nó thành Knowledge rồi để Skill đọc khi cần.

### Tạo Skill mới

1. Xác định capability, outcome, trigger examples và artifact đầu ra.
2. Search toàn bộ `02-skills/` để kiểm tra overlap và tên trùng.
3. Tạo folder verb-led, lowercase, hyphen-case và `SKILL.md` theo chuẩn OpenAI.
4. Chỉ giữ procedure cốt lõi trong `SKILL.md`; dùng `references/`, `scripts/` và
   `assets/` cho nội dung chi tiết.
5. Chạy size validator, OpenAI validator khi có, skill-local validator, link check
   và credential scan.
6. Forward-test ít nhất một normal case và một missing-input/failure/update case.
7. Capability owner review; thêm domain/security reviewer nếu có rủi ro tương ứng.
8. Ghi quyết định vào `change-approval-register.md`, rồi mới install/publish.

### Update Skill

1. Chạy size validator trước thay đổi để lấy baseline.
2. Xác định change class: `Editorial`, `Behavioral` hoặc `High-risk`.
3. Kiểm tra Goal, template, demo, evaluation và Skill khác đang gọi Skill này.
4. Giữ input/output contract và artifact semantics nếu chưa có breaking-change approval.
5. Chỉ sửa phần bị ảnh hưởng; không trộn refactor không liên quan.
6. Chạy lại toàn bộ validator và forward-test trước/sau.
7. Nếu breaking change, cập nhật mọi consumer và migration impact trong cùng change.
8. Ghi approval record trước khi cài hoặc công bố version mới.

Lệnh baseline và validation:

```powershell
python 05-scripts/validate_skill_size.py 02-skills/<capability>/<skill>
```

### Tạo Knowledge mới

1. Xác định đây là Business Contract, Current Product, Industry Domain, QA
   Intelligence hay Governance.
2. Đăng ký source trong `governance/source-registry.md`.
3. Giữ raw source trong `00-sources/` hoặc tham chiếu an toàn; không copy secret.
4. Tạo Knowledge có `knowledge_id`, owner, authority, scope, release, status và
   ngày xác minh theo metadata standard.
5. Tách source fact, normalization inference, conflict và missing information.
6. Kiểm tra duplicate ID, duplicated rule, link, freshness và sensitive data.
7. Content owner review đúng authority; QA owner review khả năng sử dụng.
8. Chỉ nâng `authority: approved` khi có approver, ngày, scope và evidence.

### Update Knowledge

1. Đọc source registry, authority matrix, freshness và conflict policy.
2. Xác định source mới bổ sung, sửa lỗi hay thay thế quyết định cũ.
3. Không âm thầm ghi đè rule mạnh hơn hoặc decision history.
4. Nếu meaning thay đổi, tạo decision record hoặc dùng `supersedes`.
5. Đánh dấu các Skill, Goal, testcase, demo và artifact bị ảnh hưởng.
6. Giữ `status: needs-review` cho tới khi content owner duyệt.
7. Cập nhật approval register sau review; không dùng `active` như đồng nghĩa với
   approved business truth.

### Approval Matrix

| Item | Reviewer bắt buộc | Gate trước khi approve |
|---|---|---|
| Skill editorial | Skill/capability owner | Validator và diff không đổi behavior |
| Skill behavioral | Capability owner + qualified reviewer | Validators, normal case, failure/update case, consumer impact |
| Skill high-risk | Capability owner + qualified reviewer + domain/security owner | Behavioral gates + security/live/external transmission review |
| Business Knowledge | BA/PO hoặc domain owner + QA knowledge owner | Source, scope, formula/rule, conflict, freshness, approval evidence |
| Current Product Knowledge | Product/Engineering owner + QA knowledge owner | Runtime/product evidence, environment, role, version và verification date |
| QA/Governance Knowledge | QA hoặc policy owner + qualified reviewer | Applicability, conflicts, security và operational impact |

Tác giả không được là người duy nhất approve behavioral hoặc high-risk change.
Decision hợp lệ gồm `Approved`, `Approved with Conditions`, `Rejected` hoặc
`Superseded`; approval có điều kiện phải có owner và review date.

### Prompt đóng góp

```text
Tạo hoặc cập nhật <Skill|Knowledge> cho <outcome/source>.

Trước khi sửa, đọc change-approval-policy.md, kiểm tra overlap, authority và
change class. Với Skill update, chạy size validator lấy baseline. Với Knowledge,
đăng ký source và dùng metadata standard.

Thực hiện thay đổi nhỏ nhất cần thiết; không trộn business knowledge vào Skill,
không tự nâng authority thành approved. Chạy validator, credential/link/ID checks
và forward evaluation phù hợp. Báo reviewer bắt buộc, consumer impact và nội dung
còn thiếu. Giữ trạng thái needs-review và chưa install/publish cho đến khi có
approval record trong change-approval-register.md.
```
