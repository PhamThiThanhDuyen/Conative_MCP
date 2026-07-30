# Conative QE Codex Kit

Internal Quality Engineering capability library for Conative. Keep this
repository and its linked sources inside the approved private GitLab namespace.

## Quick Start

Prerequisites:

- Git with access to the private Conative GitLab repositories
- Python 3.10 or newer; repository validators use only the standard library
- Codex for Library Mode or Installed Mode usage

Clone the kit and Product Docs source together:

```powershell
git clone --recurse-submodules https://gitlab.cbidigital.dev/conative/knowledges/conative-tester-agent.git
cd conative-tester-agent
powershell -ExecutionPolicy Bypass -File 05-scripts/verify_kit.ps1
```

Use Library Mode immediately by opening Codex in the repository and asking it to
read a Goal or Skill path. To enable `$skill-name` discovery, install the bundled
Skills without overwriting existing installations:

```powershell
powershell -ExecutionPolicy Bypass -File 05-scripts/install_skills.ps1
```

Restart or reopen Codex after installation. Use `-Force` only after reviewing an
existing installed Skill that has the same name.

## Bắt đầu sử dụng

- Đọc [Hướng dẫn sử dụng](00-presentation/USER_GUIDE.md) để hiểu Concept,
  Terms, Core Items và cách chạy Goal/Skill.
- Dùng [Talk track 5 phút](00-presentation/TALK_TRACK.md) khi giới thiệu nhanh
  bộ kit với stakeholder.

Mục tiêu: biến slide "Manual QA → Quality Engineering" thành một thư viện Goal / Skill / Knowledge / Artifact có thể demo bằng Codex.

## Cách trình bày
1. Slide nói về Operating Model và 8 QE capabilities.
2. Thư mục này chứng minh cách triển khai thực tế.
3. Demo 1 luồng: Requirement → Gap/Risk → Test Matrix → Readiness/Verification → Evidence Package → Go/No-Go.

## Nguyên tắc
- Không copy nguyên repo bên ngoài.
- Mỗi repo chỉ dùng để benchmark cấu trúc, workflow hoặc kỹ thuật.
- Chuẩn Conative là nguồn sự thật: domain rule, evidence standard, human review.
- AI đề xuất; QA phê duyệt artifact và quyết định release.
- Với mỗi testcase, evidence nên bao gồm screenshot và video record ngắn để minh họa kết quả thực tế.

## Internal Sources

- BA requirements are stored under `00-sources/ba/`.
- Product Docs is linked under `00-sources/product-docs/` as a private GitLab
  submodule.
- Clone with `--recurse-submodules`, or run
  `git submodule update --init --recursive` after pulling.
