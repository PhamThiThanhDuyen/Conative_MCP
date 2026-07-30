# Talk track 5 phút

Tài liệu trình bày và onboarding đầy đủ: `USER_GUIDE.md`.

## 1. Vấn đề
QA Conative có domain knowledge và manual execution tốt, nhưng tri thức, evidence và metrics còn rời rạc.

## 2. Ý tưởng
Không xây một "AI QA agent" khổng lồ. Xây QE Operating Model gồm 8 capability, rồi đóng từng capability thành skill nhỏ và goal điều phối.

## 3. Benchmark GitHub
Top 10 repo được dùng để học 4 thứ: Agent Skills format, QA workflow, Playwright execution, prompt/template library.

## 4. Cấu trúc triển khai
- Goal = workflow tạo outcome hoàn chỉnh.
- Skill = thao tác chuyên biệt.
- Knowledge = tiêu chuẩn/domain rule đã kiểm chứng.
- Artifact = đầu ra đo được.
- Evaluation = kiểm tra output của agent có đúng chuẩn không.

## 5. Demo
Chạy goal `qe-release-readiness` trên 1 requirement thật và sinh Requirement Gap Register, Risk Map, Test Matrix, các verification report phù hợp, Evidence Package, và Go/No-Go Report.

## 6. Điều CEO cần chốt
Pilot use case, owner, 4 tuần, success metrics.
